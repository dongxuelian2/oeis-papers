#!/usr/bin/env python3
"""Exact integer audit of the exponential-in-n subsequence construction.

For odd t>=9, n=(551*t**3-1)//2 has >=2**(9*t**3) cube-sum
permutations. Only one representative is materialized. The 9*t**3
vertex-disjoint alternating five-cycles are checked by local identities;
their independent switching is a mathematical counting argument.
"""
import argparse

from construct_linear import make as prefix_permutation
from count_236 import template as template_236


def parameters(t):
    assert t >= 9 and t % 2 == 1
    L = t**3
    A = (L-1)//2
    B = A+236*L
    cube = (8*t)**3
    n = cube-B-1
    assert n == (551*L-1)//2 and n-B == 39*L
    return L,A,B,cube,n


def lift(t):
    L,A,B,cube,n = parameters(t)
    p = [0]*(n+1)
    p[1:A+1] = prefix_permutation(A)
    seed = template_236()
    for i in range(1,237):
        target = seed[i]
        for r in range(1,L+1):
            u = A+(i-1)*L+r
            p[u] = A+(target-1)*L+(L+1-r)
            assert u+p[u] == L*(i+target)
    for u in range(B+1,n+1):
        p[u] = cube-u
    return p


def check(t):
    L,A,B,cube,n = parameters(t)
    p = lift(t)
    assert sorted(p[1:]) == list(range(1,n+1))
    allowed = {k**3 for k in range(2,150) if k**3 <= 2*n}
    assert all(i+p[i] in allowed for i in range(1,n+1))

    # The original 236-vertex gadget has nine cycles:
    # (10+j -> 137+j -> 46+j -> 198+j -> 71+j -> 10+j).
    # The odd-power lift gives one for EACH r in [1,L].
    used = bytearray(n+1)
    count = 0
    for j in range(9):
        cycle = (10+j,137+j,46+j,198+j,71+j)
        for r in range(1,L+1):
            vertices = [A+(i-1)*L+r for i in cycle]
            for u in vertices:
                assert not used[u]
                used[u] = 1
            for index,u in enumerate(vertices):
                v = vertices[(index+1)%5]
                assert u+p[v] in allowed
            count += 1
    assert count == 9*L
    assert sum(used)==5*9*L

    # An independently switched cycle must still give a bijection and
    # all five switched sums must be cubes.
    cycle = [A+(i-1)*L+1 for i in (10,137,46,198,71)]
    alternative = p[:]
    for index,u in enumerate(cycle):
        alternative[u] = p[cycle[(index+1)%5]]
        assert u+alternative[u] in allowed
    assert len(set(alternative[1:])) == n
    assert alternative != p
    print(f"PASS t={t}, n={n}, L={L}, independent cycles={count}.")
    print(f"Certified number of permutations at n={n}: >=2**{count}.")


def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--t",type=int,nargs="*",default=[9,11],
                     help="odd root scales (default: 9 11)")
    args=cli.parse_args()
    for t in args.t: check(t)


if __name__=="__main__":
    main()
