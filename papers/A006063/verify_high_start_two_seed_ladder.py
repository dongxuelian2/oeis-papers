#!/usr/bin/env python3
"""Experimental two-seed, same-parity +2 augmenting ladder for [467,665].

Unlike verify_high_start_five_cubes.py, this program calls a blossom
solver *only twice*: at 467 and 468. All 197 subsequent steps use an
elementary alternating-path BFS and flip, with exact cube-sum checks.
The experiments are NOT a proof that the BFS always succeeds for
arbitrary matchings or arbitrary n. Requires networkx >= 3.
"""
from collections import Counter, deque
import networkx as nx

CUBES=(216,343,512,729,1000)


def base_matching(n):
    G=nx.Graph()
    G.add_nodes_from(i for i in range(1,n+1)
                     if not (n%2 and i==108))
    for c in CUBES:
        for i in range(max(1,c-n),min(n,c-1)+1):
            j=c-i
            if i<j and i in G and j in G:
                G.add_edge(i,j)
    edges=nx.max_weight_matching(G,maxcardinality=True)
    assert len(edges)*2==len(G)
    p={}
    for i,j in edges:
        p[i]=j
        p[j]=i
    return p


def augmenting_path(p,n):
    """Alternating simple path from newly exposed n+1 to n+2."""
    x,y=n+1,n+2
    def neighbors(i):
        return [c-i for c in CUBES
                if 1<=c-i<=y and not (y%2 and c-i==108)]
    queue=deque([(x,[x])])
    seen={x}
    while queue:
        v,path=queue.popleft()
        if y in neighbors(v):
            return path+[y]
        for u in neighbors(v):
            if u in (x,y) or u not in p:
                continue
            w=p[u]
            if w not in seen and u not in path and w not in path:
                seen.add(w)
                queue.append((w,path+[u,w]))
    return None


def flip(p,path):
    assert len(path)%2==0
    assert len(path)==len(set(path))
    assert all(i+j in CUBES for i,j in zip(path,path[1:]))
    q=p.copy()
    for i in range(0,len(path)-1,2):
        u,v=path[i:i+2]
        q[u]=v
        q[v]=u
    return q


def verify(p,n):
    V=set(range(1,n+1))
    if n%2:
        V.remove(108)
    assert set(p)==V
    assert all(p.get(p[i])==i and p[i]!=i
               and i+p[i] in CUBES for i in V)


def main():
    total_steps=0
    for base,end in ((467,665),(468,664)):
        p=base_matching(base)
        verify(p,base)
        hist=Counter()
        worst=(0,base)
        for n in range(base,end,2):
            path=augmenting_path(p,n)
            assert path is not None, (base,n)
            length=len(path)-1
            hist[length]+=1
            if length>worst[0]:
                worst=(length,n)
            p=flip(p,path)
            verify(p,n+2)
            total_steps+=1
        assert max(p)==end
        print(f"PASS: {base}->{end}, {sum(hist.values())} +2 steps; "
              f"maximum alternating path {worst[0]} edges "
              f"(at n={worst[1]}); histogram {dict(sorted(hist.items()))}")
    assert total_steps==197
    print("PASS: 2 independently found seeds + 197 successive flips")
    print("EXPERIMENT ONLY: path existence has no uniform proof here")


if __name__=="__main__":
    main()
