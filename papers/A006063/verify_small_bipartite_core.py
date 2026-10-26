#!/usr/bin/env python3
"""Three fixed 14/10/16-edge deletion certificates for the four-color graphs.

Python standard library only. The script is an exact arithmetic checker
of the stated finite planar-dual certificates, not a general-graph
matching solver or a phase-wide computer-assisted matching proof.
"""
from collections import Counter, deque
from itertools import combinations

CASES = (
    (467,560,(216,343,512,729),(216,343,512,729),
     ((166,177),(98,118),(70,146),(149,194),(101,115),
      (163,180),(84,132),(60,156),(139,204),(91,125),
      (170,173),(94,122),(142,201),(63,280)),
     (14,15,21)),
    (561,579,(216,512,729,1000),(216,512,729,1000),
     ((29,483),(24,192),(453,547),(197,532),(39,473),
      (66,150),(17,199),(180,549),(490,510),(431,569)),
     (10,13,16)),
    (580,665,(343,512,729,1000),(343,729,512,1000),
     ((358,371),(460,540),(221,508),(339,390),(224,288),
      (457,543),(355,374),(205,524),(280,449),(347,382),
      (213,516),(468,532),(363,366),(465,535),(216,296),
      (181,331)),
     (16,18,24)),
)


def adjacency(n,colors):
    a={v:set() for v in range(1,n+1)}
    for c in colors:
        for i in range(max(1,c-n),min(n,c-1)+1):
            j=c-i
            if i<j:
                a[i].add(j)
                a[j].add(i)
    return a


def color_and_connected(A,require_connected=True):
    colors={}
    components=0
    for start in sorted(A):
        if start in colors:
            continue
        components+=1
        colors[start]=0
        q=deque([start])
        while q:
            u=q.popleft()
            for v in sorted(A[u]):
                if v not in colors:
                    colors[v]=1-colors[u]
                    q.append(v)
                else:
                    assert colors[v]!=colors[u], (u,v)
    if require_connected:
        assert components==1,components
    return colors


def faces(n,colors,order):
    A=adjacency(n,colors)
    unseen={(u,v) for u,near in A.items() for v in near}
    face_of={}
    boundaries=[]
    while unseen:
        start=min(unseen)
        u,v=start
        current=[]
        while (u,v) in unseen:
            unseen.remove((u,v))
            face_of[(u,v)]=len(boundaries)
            current.append((u,v))
            present=[c for c in order if c-v in A[v]]
            j=present.index(u+v)
            u,v=v,present[(j+1)%len(present)]-v
        assert (u,v)==start
        boundaries.append(current)
    assert sum(len(b) for b in boundaries)==sum(map(len,A.values()))
    dual={i:set() for i in range(len(boundaries))}
    for (u,v),fi in face_of.items():
        fj=face_of[v,u]
        if fi!=fj:
            dual[fi].add(fj)
            dual[fj].add(fi)
    return A,boundaries,dual


def shortest_path_length(adj,start,goal):
    distance={start:0}
    q=deque([start])
    while q:
        u=q.popleft()
        if u==goal:
            return distance[u]
        for v in adj[u]:
            if v not in distance:
                distance[v]=distance[u]+1
                q.append(v)
    raise AssertionError("disconnected planar dual")


def audit_case(low,high,cubes,order,deleted,expected_pairings):
    A,boundaries,dual=faces(high,cubes,order)
    e=sum(map(len,A.values()))//2
    assert high-e+len(boundaries)==2
    odd=[i for i,b in enumerate(boundaries) if len(b)%2]
    assert len(odd)==4, (high,odd)
    a,b,c,d=odd
    def dis(x,y):return shortest_path_length(dual,x,y)
    pairings=sorted((dis(a,b)+dis(c,d),
                     dis(a,c)+dis(b,d),
                     dis(a,d)+dis(b,c)))
    assert tuple(pairings)==expected_pairings, (high,pairings)
    assert len(deleted)==min(pairings)
    delete_set={tuple(sorted(edge)) for edge in deleted}
    assert len(delete_set)==len(deleted)
    endpoints=[v for edge in delete_set for v in edge]
    assert len(endpoints)==len(set(endpoints)), "deleted edges are not disjoint"
    assert all(u in A and v in A[u] and u+v in cubes
               for u,v in delete_set)
    H={u:near.copy() for u,near in A.items()}
    for u,v in delete_set:
        H[u].remove(v)
        H[v].remove(u)
    coloring=color_and_connected(H)
    assert len(coloring)==high
    assert all(coloring[u]==coloring[v] for u,v in delete_set)
    charge_hist=Counter()
    balance_hist=Counter()
    # Every n is an induced subgraph; the same coloring and deletion
    # set still work. Deleting one allowed fixed point cannot harm this.
    for n in range(low,high+1):
        assert all(coloring[u]!=coloring[v]
                   for u in range(1,n+1)
                   for v in H[u] if v<=n)
        fixed = ((108 if high<=579 else 500) if n%2 else None)
        if fixed is not None:
            assert 2*fixed in cubes
        vertices=set(range(1,n+1))
        if fixed is not None:
            vertices.remove(fixed)
        charge=sum((1 if coloring[u]==0 else -1) for u in vertices)
        charge_hist[abs(charge)]+=1
        available=[(u,v) for u,v in sorted(delete_set)
                   if u in vertices and v in vertices]
        solution=None
        for r in range(3):
            for candidate in combinations(available,r):
                if 2*sum((1 if coloring[u]==0 else -1)
                         for u,v in candidate)==charge:
                    solution=candidate
                    break
            if solution is not None:
                break
        assert solution is not None,(n,charge,"no 2-edge balance")
        assert len(solution)==abs(charge)//2
        balance_hist[len(solution)]+=1
    expected={
       560:{0:8,2:54,4:32},
       579:{0:1,2:10,4:8},
       665:{0:34,2:48,4:4},
    }[high]
    assert charge_hist==Counter(expected),(high,charge_hist)
    assert balance_hist==Counter({k//2:v for k,v in expected.items()})
    print(f"PASS: [{low},{high}] absolute bipartition imbalance "
          f"0/2/4 occurs {dict(sorted(charge_hist.items()))}")
    print(f"PASS: same-color exceptional edges form a matching; "
          f"at most two edge toggles balance all these graphs")
    print(f"PASS: [{low},{high}]; {len(deleted)} fixed edges removed "
          f"at maximum n={high}; all graphs are bipartite")
    print(f"      four odd faces: dual pairing sums {pairings}; "
          f"minimum {min(pairings)} is attained")


def main():
    for args in CASES:
        audit_case(*args)
    print("PASS: 3 explicit deletions certify all 199 graphs.")
    print("PASS: the 14/10/16 edge sizes are optimal at the maxima.")
    print("NOTE: no matching-existence claim follows from bipartiteness alone.")


if __name__=="__main__":
    main()
