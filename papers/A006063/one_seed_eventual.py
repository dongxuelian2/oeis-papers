#!/usr/bin/env python3
"""Seven-round reflection closure: a single seven-element seed proves
all sufficiently large cube-sum permutation lengths.

Unlike the original sharp-threshold proof, this construction uses:
  * one explicit seven-term reversal,
  * seven simultaneous rounds of reflection with cubes <= 21950,
  * an elementary cube-gap induction for all n >= 10976.

It does not call matching algorithms, read existence certificates, or
assume the n>=173 classification.

Exact finite statement: after seven rounds the closure contains every
integer n in [8915,10975]. Each edge m -> n is checked by
n = k**3 - m - 1 > m. The resulting construction proves P(n)>0 for
all n>=8915. The checked round counts act as regression certificates.
"""
from __future__ import annotations
import argparse

SEED = 7
CAP = 10975
TAIL_START = 8915
INFINITE_START = 10976
ROUND_SIZES = (1, 21, 189, 995, 3280, 6588, 8533, 8924)


def finite_reflection_closure():
    cubes = [(k, k**3) for k in range(2, 100) if k**3 <= 2*CAP]
    known = {SEED}
    parents = {}
    counts = [len(known)]
    for depth in range(1, 8):
        new = {}
        for m in sorted(known):
            for k, c in cubes:
                n = c - m - 1
                if m < n <= CAP and n not in known and n not in new:
                    assert m + n + 1 == k**3
                    new[n] = (m, k)
        known.update(new)
        parents.update(new)
        counts.append(len(known))
    assert tuple(counts) == ROUND_SIZES, counts
    assert all(n in known for n in range(TAIL_START, CAP+1))
    assert CAP in known and 8914 not in known
    print("PASS: seven reflection rounds from n=7; counts:", *counts)
    print(f"PASS: all {CAP-TAIL_START+1} lengths {TAIL_START}..{CAP} reachable.")
    return parents, known


def ceil_cube_root(x: int) -> int:
    assert x >= 1
    lo, hi = 0, 1
    while hi**3 < x:
        hi *= 2
    while lo+1 < hi:
        mid = (lo+hi)//2
        if mid**3 < x:
            lo = mid
        else:
            hi = mid
    return hi


def infinite_predecessor(n: int):
    assert n >= INFINITE_START
    k = ceil_cube_root(n+TAIL_START+1)
    c = k**3
    m = c-n-1
    assert k >= 28 and TAIL_START <= m < n
    assert n+m+1 == c
    # For k=28, n>=10976 implies 28^3<=2*n;
    # for k>=29 the polynomial
    #    k^3 - 6*k^2 + 6*k - 17832
    # is positive and increasing.
    if k >= 29:
        poly = k**3-6*k*k+6*k-17832
        assert poly >= 1685
    return m, k


def plan(n: int, parents: dict[int,tuple[int,int]]):
    if n < TAIL_START:
        raise ValueError("This global theorem only claims all n>=8915")
    blocks = []
    x = n
    while x >= INFINITE_START:
        m,k = infinite_predecessor(x)
        blocks.append((m+1,x,k**3))
        x=m
    while x!=SEED:
        m,k=parents[x]
        assert m < x and m+x+1 == k**3
        blocks.append((m+1,x,k**3))
        x=m
    return blocks


def construct(n: int, parents: dict[int,tuple[int,int]]):
    blocks = plan(n,parents)
    p = [0]*(n+1)
    for i in range(1,8):
        p[i]=8-i
    for start,stop,cube in reversed(blocks):
        for i in range(start,stop+1):
            assert p[i]==0
            p[i]=cube-i
    assert sorted(p[1:]) == list(range(1,n+1))
    cubes = set()
    k=2
    while k**3<=2*n:
        cubes.add(k**3)
        k+=1
    assert all(i+p[i] in cubes for i in range(1,n+1))
    return p[1:]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--n",nargs="*",type=int,
                        default=[8915,9841,10975,10976,20000,100000])
    args=parser.parse_args()
    parents,known=finite_reflection_closure()
    for n in args.n:
        p=construct(n,parents)
        print(f"PASS: n={n}, valid permutation, "
              f"reflection depth={len(plan(n,parents))}.")
    for n in [10976,12195,20000,100000,10**30]:
        steps=plan(n,parents)
        print(f"PASS: symbolic reflection plan n={n} in {len(steps)} steps.")
    print("CERTIFIED: P(n)>0 for every n>=8915 by induction.")


if __name__=="__main__":
    main()
