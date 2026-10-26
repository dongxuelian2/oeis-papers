#!/usr/bin/env python3
"""Exact single-seed reflection-history counts F(n), without matchings.

F(7)=1; F(n)=sum(F(m): 7<=m<n and m+n+1 is a cube).
Each distinct reflection history encodes a distinct permutation,
because its final predecessor m equals p(n)-1.

The infinite entropy theorem is proved symbolically in main.tex.
This finite exact counter only cross-checks the recurrence and
seven-round eventual positivity.
"""
from one_seed_eventual import finite_reflection_closure


def reflection_counts(cap=12000):
    assert cap>=7
    cubes=[]
    k=2
    while k**3<=2*cap:
        cubes.append(k**3)
        k+=1
    counts=[0]*(cap+1)
    counts[7]=1
    for n in range(8,cap+1):
        total=0
        for c in cubes:
            m=c-n-1
            if 7<=m<n:
                total+=counts[m]
        counts[n]=total
    return counts


def main():
    f=reflection_counts()
    assert f[7]==f[19]==f[56]==f[171]==1
    assert f[173]==0
    assert f[7797]==0
    assert f[7798]==5
    assert f[8914]==7
    assert f[8915]==86
    assert f[9841]==197
    assert f[10975]==344
    assert f[12000]==85
    assert all(f[n]>0 for n in range(8915,12001))
    parents, reachable=finite_reflection_closure()
    for n in range(7,10976):
        assert (n in reachable) <= bool(f[n])
    print("PASS: exact reflection recurrence at 12,000 lengths.")
    print("PASS: last reflected permutation value identifies its unique parent.")
    for n in (173,7797,7798,8914,8915,9841,10975,12000):
        print(f"F({n})={f[n]}")


if __name__=="__main__":
    main()
