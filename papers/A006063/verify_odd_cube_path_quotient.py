#!/usr/bin/env python3
"""Arithmetic-only audit of the 193 odd-cube path quotient theorem.

No matching solver, NetworkX, scipy, legacy atlas, or permutation file.
All formulas hold for every 467<=n<=665.
"""
from collections import Counter

ODD_CUBES=(343,729)
EVEN_CUBES=(216,512,1000)


def components(n):
    assert 467<=n<=665
    groups=[]
    for x in range(1,172):
        C={x,343-x}
        if x+386<=n:
            C.add(x+386)
        if 729-x<=n:
            C.add(729-x)
        groups.append(C)
    for j in range(343,365):
        groups.append({j,729-j})
    assert len(groups)==193
    assert len(set.union(*groups))==n
    assert sum(map(len,groups))==n
    assert all(2<=len(C)<=4 for C in groups)
    return groups


def neighbors(x,n):
    return {c-x for c in ODD_CUBES if 1<=c-x<=n and c-x!=x}


def odd_components_after_fixed_point(n,groups):
    if n%2==0:
        return groups
    out=[]
    for G in groups:
        subset=G-{108}
        if not subset:
            continue
        # At most four vertices per group; BFS without imports.
        while subset:
            v=next(iter(subset))
            stack=[v]
            visited={v}
            while stack:
                u=stack.pop()
                for w in neighbors(u,n)&subset:
                    if w not in visited:
                        visited.add(w)
                        stack.append(w)
            out.append(visited)
            subset-=visited
    return out


def predicted_counts(n):
    if n<=557:
        return Counter({2:579-n,3:n-386})
    return Counter({2:22,3:728-n,4:n-557})


def deficiency(n):
    d=n-386 if n<=557 else 728-n
    if n%2==0:
        return d
    if n<=493 or n>=621:
        return d+1
    return d-1


def main():
    worst=(0,0)
    for n in range(467,666):
        groups=components(n)
        counts=Counter(map(len,groups))
        assert counts==predicted_counts(n),(n,counts)
        # Check all odd-color edges lie in exactly one computed path.
        owner={v:i for i,G in enumerate(groups) for v in G}
        for i in range(1,n+1):
            for j in neighbors(i,n):
                assert owner[i]==owner[j], (n,i,j)
        after=odd_components_after_fixed_point(n,groups)
        q=sum(len(C)%2 for C in after)
        assert q==deficiency(n),(n,q,deficiency(n))
        assert q%2==0
        # Each odd component needs a non-odd edge leaving it.
        lower_bound=q//2
        if lower_bound>worst[1]:
            worst=(n,lower_bound)
    assert deficiency(556)==deficiency(557)==deficiency(558)==170
    assert deficiency(665)==64
    # At n=467 C_1 is a 3-path and its exposed endpoints
    # cannot be paired to exposed endpoints of any other odd path.
    n=467
    groups=odd_components_after_fixed_point(n,components(n))
    ix=next(i for i,G in enumerate(groups) if {1,342,387}==G)
    endpoints={1,387}
    for x in endpoints:
        for cube in EVEN_CUBES:
            y=cube-x
            if 1<=y<=n:
                for k,G in enumerate(groups):
                    if k!=ix and len(G)%2==1 and y in G:
                        assert y not in {z for z in G
                                         if len(neighbors(z,n)&G)==1}
    print("PASS: exact 193-component 2/3/4-path decomposition at all 199 lengths")
    print("PASS: symbolic size counts and fixed-108 parity defects")
    print("PASS: at least 85 even-cube matching edges required near n=557")
    print("PASS: explicit obstruction to the naive odd-component quotient")
    print("This is NOT a proof of five-cube matching existence.")


if __name__ == "__main__":
    main()
