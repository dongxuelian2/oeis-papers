#!/usr/bin/env python3
"""Exact defect-matching and bipartite balance reduction for high A006063.

No matching solver, NetworkX, SciPy, optimization or archived
cube-sum permutations. Reads explicit two dual paths for each phase
and reconstructs the unique 2-coloring from arithmetic reflections.
"""
from collections import Counter
from verify_near_bipartite_phases import PATHS, PHASES, two_color
from verify_three_rotation_planarity import adjacency

EXPECTED_BALANCE = {
    560: {0:8,2:54,4:32},
    579: {4:6,6:11,8:2},
    665: {0:36,2:47,4:3},
}
EXPECTED_CUT = {560:14,579:10,665:16}
EXPECTED_SIDE_SIZE = {560:(8,6),579:(7,3),665:(9,7)}


def edge_set(maximum):
    return {tuple(sorted(e))
            for _,edges in PATHS[maximum]
            for e in edges}


def main():
    total_lengths=0
    for first,last,cubes in PHASES:
        F=edge_set(last)
        assert len(F)==EXPECTED_CUT[last]
        endpoints=[v for u,w in F for v in (u,w)]
        assert len(set(endpoints))==len(endpoints)
        A=adjacency(last,cubes)
        assert all(w in A[u].values() for u,w in F)
        col=two_color(last,cubes,F)
        assert len(col)==last
        sides=Counter()
        for u,v in F:
            assert col[u]==col[v],(last,u,v,col[u],col[v])
            sides[col[u]]+=1
        assert tuple(sorted(sides.values(),reverse=True))==EXPECTED_SIDE_SIZE[last]
        balances=Counter()
        comps=Counter()
        for n in range(first,last+1):
            fixed=(108 if n<=579 else 500) if n%2 else None
            if fixed is not None:
                assert 2*fixed in cubes
            V=range(1,n+1)
            signed=sum(1 if col[v]==1 else -1 for v in V
                       if v!=fixed)
            assert signed%2==0
            balances[abs(signed)]+=1
            # Confirm the inherited proper coloring of every intact edge.
            B=adjacency(n,cubes)
            for u,row in B.items():
                if u==fixed:
                    continue
                for v in row.values():
                    if v==fixed or tuple(sorted((u,v))) in F:
                        continue
                    assert col[u]!=col[v],(n,u,v)
            total_lengths+=1
        assert balances==Counter(EXPECTED_BALANCE[last]),(last,balances)
        print(f"PASS: {last}-vertex maximum, {len(F)} pairwise disjoint "
              f"monochromatic exceptional edges, split {dict(sides)}")
        print("PASS: all inherited graphs 2-color after deletion; "
              "absolute balances",dict(sorted(balances.items())))
    assert total_lengths==199
    print("PROVED: each high four-cube graph is bipartite plus <=16 disjoint edges.")
    print("PROVED: perfect matching iff a balanced subset of those edges "
          "leaves a Hall-perfect bipartite graph.")
    print("NOT PROVED: that one such Hall-perfect subset always exists.")


if __name__=="__main__":
    main()
