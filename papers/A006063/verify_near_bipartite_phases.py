#!/usr/bin/env python3
"""Three explicit dual T-joins prove 199 four-cube graphs nearly bipartite.

Only integer cubic reflection edges, the stated cyclic-color rotations,
face traversals, and a simple 2-color test. No matching solver,
networkx, planarity-finding library, optimization or archived permutations.
"""
from collections import Counter,deque
from verify_three_rotation_planarity import CASES, adjacency

PATHS = {
    560: (
        ((39,84),((166,177),(98,118),(146,197),(67,149),
                  (101,115),(163,180),(84,132))),
        ((60,63),((60,156),(139,204),(91,125),(170,173),
                  (94,122),(142,201),(63,280))),
    ),
    579: (
        ((29,14),((29,187),(192,537),(207,522),
                  (172,557),(14,202))),
        ((12,81),((66,150),(495,505),(61,155),
                  (490,510),(160,569))),
    ),
    665: (
        ((87,36),((358,371),(189,540),(221,291),
                  (336,393),(224,505),(186,543),
                  (355,374),(205,524))),
        ((63,12),((280,449),(347,382),(213,516),
                  (197,532),(363,366),(194,535),
                  (216,296),(181,331))),
    ),
}

DUAL_DISTANCES = {
    560: {(39,84):7,(39,60):7,(39,63):11,
          (84,60):10,(84,63):8,(60,63):7},
    579: {(29,14):5,(29,12):6,(29,81):8,
          (14,12):8,(14,81):7,(12,81):5},
    665: {(87,63):12,(87,12):8,(87,36):8,
          (63,12):8,(63,36):10,(12,36):12},
}

PHASES = ((467,560,(216,343,512,729)),
          (561,579,(216,512,729,1000)),
          (580,665,(343,512,729,1000)))


def face_data(A,rotation):
    darts={(u,v) for u,row in A.items() for v in row.values()}
    face_of={}
    faces=[]
    while darts:
        u,v=first=next(iter(darts))
        face=[]
        while (u,v) in darts:
            darts.remove((u,v))
            face_of[(u,v)]=len(faces)
            face.append(u)
            available=[c for c in rotation if c in A[v]]
            next_color=available[(available.index(u+v)+1)%len(available)]
            u,v=v,A[v][next_color]
        assert (u,v)==first
        faces.append(face)
    return faces,face_of


def two_color(n,colors,excluded):
    A=adjacency(n,colors)
    removed={tuple(sorted(e)) for e in excluded}
    colors_of={}
    for src in A:
        if src in colors_of:
            continue
        colors_of[src]=0
        Q=[src]
        for u in Q:
            for v in A[u].values():
                if tuple(sorted((u,v))) in removed:
                    continue
                if v not in colors_of:
                    colors_of[v]=1-colors_of[u]
                    Q.append(v)
                else:
                    assert colors_of[v]!=colors_of[u], (n,u,v)
    return colors_of


def dual_distance(dual, start):
    d={start:0}
    q=[start]
    for v in q:
        for w in dual[v]:
            if w not in d:
                d[w]=d[v]+1
                q.append(w)
    return d


def main():
    exceptional={}
    for maximum,cubes,rotation,expected_edges,expected_faces in CASES:
        A=adjacency(maximum,cubes)
        faces,face_of=face_data(A,rotation)
        assert len(faces)==sum(expected_faces.values())
        odd={j for j,F in enumerate(faces) if len(F)%2}
        assert len(odd)==4
        dual={i:set() for i in range(len(faces))}
        for u in A:
            for v in A[u].values():
                a=face_of[(u,v)]
                b=face_of[(v,u)]
                if a!=b:
                    dual[a].add(b)
                    dual[b].add(a)
        by_min={min(faces[i]):i for i in odd}
        for (a,b),expected in DUAL_DISTANCES[maximum].items():
            actual=dual_distance(dual,by_min[a])[by_min[b]]
            assert actual==expected,(maximum,a,b,actual,expected)
        labels=list(by_min)
        assert len(labels)==4
        A0,B0,C0,D0=labels
        def dist(x,y):
            return dual_distance(dual,by_min[x])[by_min[y]]
        metric=min(dist(A0,B0)+dist(C0,D0),
                   dist(A0,C0)+dist(B0,D0),
                   dist(A0,D0)+dist(B0,C0))
        assert metric=={560:14,579:10,665:16}[maximum]
        assert len(by_min)==4
        consumed=set()
        removed=[]
        path_sizes=[]
        for minima,edges in PATHS[maximum]:
            current=by_min[minima[0]]
            trail=[current]
            for a,b in edges:
                assert a<b and a in A and b in A[a].values()
                left=face_of[(a,b)]
                right=face_of[(b,a)]
                assert left!=right
                assert current in {left,right}, (maximum,minima,current,a,b)
                current=right if current==left else left
                trail.append(current)
                removed.append((a,b))
            assert current==by_min[minima[1]]
            assert len(set(trail))==len(trail)
            assert all(v not in odd for v in trail[1:-1])
            assert not consumed.intersection(trail)
            consumed.update(trail)
            path_sizes.append(len(edges))
        assert consumed.intersection(odd)==odd
        assert len(removed)==sum(path_sizes)
        assert len(removed)=={560:14,579:10,665:16}[maximum]
        maximal_coloring=two_color(maximum,cubes,removed)
        assert len(maximal_coloring)==maximum
        # Every color allowed by the maximum graph is inherited on the prefix.
        exceptional[maximum]=tuple(removed)
        print(f"PASS: maximum={maximum}, exactly four odd faces, "
              f"two disjoint dual paths of lengths {path_sizes}")
        print(f"      {len(removed)} deleted edges leave a bipartite graph")
        print(f"      six dual distances certify optimality: tau={metric}")

    for lower,upper,cubes in PHASES:
        edges=exceptional[upper]
        balance=Counter()
        for n in range(lower,upper+1):
            colors=two_color(n,cubes,edges)
            fixed=(108 if n<=579 else 500) if n%2 else None
            if fixed:
                assert 2*fixed in cubes
                colors.pop(fixed)
            delta=abs(sum(1 if c else -1 for c in colors.values()))
            assert delta%2==0
            balance[delta]+=1
        expected={560:{0:8,2:54,4:32},
                  579:{4:6,6:11,8:2},
                  665:{0:36,2:47,4:3}}[upper]
        # Difference in phase III can include one -2, hidden by absolute value.
        assert dict(balance)==expected,(upper,balance,expected)
        print(f"PASS: every n in [{lower},{upper}] is <=16-edge bipartizable")
        print("      bipartition absolute imbalance:",dict(sorted(balance.items())))
    print("PROVED: minimum bipartizing edge counts are exactly 14/10/16.")
    print("PROVED: three maximum planar graphs each admit two odd-face dual paths.")
    print("PROVED: all 199 phase graphs inherit the three fixed edge-transversals.")
    print("NOTE: no perfect-matching existence is inferred from near-bipartiteness.")


if __name__=="__main__":
    main()
