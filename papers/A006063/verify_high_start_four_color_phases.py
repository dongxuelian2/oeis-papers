#!/usr/bin/env python3
"""Experimental four-cube phase audit for A006063, 467<=n<=665.

Requires networkx. Uses Edmonds blossom, NOT a computation-free
matching theorem. Builds a perfect matching after removing the selected
fixed point and confirms the resulting cube-sum involution.
"""
import networkx as nx

PHASES=(
    (467,560,(216,343,512,729)),
    (561,579,(216,512,729,1000)),
    (580,665,(343,512,729,1000)),
)


def verify_length(n,cubes,fix):
    G=nx.Graph()
    G.add_nodes_from(range(1,n+1))
    if fix is not None:
        assert 2*fix in cubes and fix<=n
        G.remove_node(fix)
    for c in cubes:
        for i in range(max(1,c-n),min(n,c-1)+1):
            j=c-i
            if i<j and i in G and j in G:
                G.add_edge(i,j)
    matching=nx.max_weight_matching(G,maxcardinality=True)
    assert len(matching)*2==len(G),(n,cubes,fix)
    p={}
    for i,j in matching:
        assert i+j in cubes
        p[i]=j
        p[j]=i
    if fix is not None:
        p[fix]=fix
    assert len(p)==n
    assert all(p[p[i]]==i and i+p[i] in cubes for i in range(1,n+1))
    fixed={i for i in range(1,n+1) if p[i]==i}
    assert fixed==({fix} if fix is not None else set())
    return p


def main():
    found=0
    for first,last,cubes in PHASES:
        for n in range(first,last+1):
            # Odd phases I/II fix 108 (cube 216); odd phase III
            # fixes 256 (cube 512), as 216 is not in that palette.
            fixed=None if n%2==0 else (108 if n<=579 else 256)
            verify_length(n,cubes,fixed)
            found+=1
        print(f"PASS (experimental): [{first},{last}] "
              f"uses precisely {cubes}, {last-first+1} lengths")
    assert found==199
    for n in range(581,666,2):
        verify_length(n,(343,512,729,1000),500)
    print("PASS: all 43 odd Phase III lengths allow fixed point 256 OR 500")
    print("PASS: 199/199 involutions with at most FOUR cubes per n")
    print("WARNING: this is NOT a computation-free proof of the phase theorem")


if __name__=="__main__":
    main()
