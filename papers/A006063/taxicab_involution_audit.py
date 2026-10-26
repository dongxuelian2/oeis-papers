#!/usr/bin/env python3
"""Exact algebraic audit of taxicab-switching involution families.

If A+B=C+D are perfect cubes and 3A/2 <= C < B/2,
the two-interval involution on [1,(B-A)*u**3] contains
floor((A*u**3-1)/2) disjoint four-vertex switching gadgets.
Each switch exchanges two dimers for two different dimers
and preserves the cube-sum involution constraint.

The proof is entirely algebraic and works for all u>=1.
This script independently verifies all integral inequalities
and, for n=54,406, materializes a full valid involution and
switches many disjoint gadgets.
"""
import argparse


def verify_identity(a,b,c,d):
    A,B,C,D = a**3,b**3,c**3,d**3
    assert A+B==C+D
    assert 2*C>=3*A and 2*C<B
    assert A<C<B-A
    return A,B,C,D


def parameters(roots,u):
    A,B,C,D=verify_identity(*roots)
    T=u**3
    N=(B-A)*T
    H=(A*T-1)//2
    assert H>=1 and H<=(C-A)*T
    assert 2*H<A*T
    return (A,B,C,D,T,N,H)


def verify_symbolically(roots,u):
    A,B,C,D,T,N,H=parameters(roots,u)
    a=(1,H)
    b=(A*T-H,A*T-1)
    c=(C*T-H,C*T-1)
    d=((B-C)*T+1,(B-C)*T+H)
    assert a[1]<b[0]<b[1]<A*T
    assert A*T<=c[0]<=c[1]<d[0]<=d[1]<=N
    if u%2:
        expected_fixed = ((1 if A%2==0 else 0) +
                          (1 if B%2==0 else 0))
        assert expected_fixed==(0 if roots==(17,39,26,36) else 1)
        if expected_fixed:
            assert A*T <= B*T//2 <= N
    # All switching quadruples consist of transpositions only.
    # Their members cannot be a central fixed point of either block.
    for s in (1,2,max(1,H//2),H):
        x,y,z,w=s,A*T-s,C*T-s,(B-C)*T+s
        assert x+y==A*T and z+w==B*T
        assert x+z==C*T and y+w==D*T
    print(f"PASS roots={roots}, u={u}, length={N}, "
          f"independent 4-vertex switches={H}, choices >=2**{H}.")
    return N,H


def materialize_small(roots):
    A,B,C,D,T,N,H=parameters(roots,1)
    p=[0]*(N+1)
    for i in range(1,A*T):
        p[i]=A*T-i
    for i in range(A*T,N+1):
        p[i]=B*T-i
    assert sorted(p[1:])==list(range(1,N+1))
    assert all(p[p[i]]==i for i in range(1,N+1))
    assert all(p[i]!=i for i in range(1,N+1))
    powers={x**3 for x in roots}
    assert all(i+p[i] in powers for i in range(1,N+1))

    # Select every third independent dimer switch: also check that
    # the unchanged transpositions remain undisturbed.
    q=p[:]
    for s in range(1,H+1,3):
        x,y,z,w=s,A*T-s,C*T-s,(B-C)*T+s
        q[x]=z
        q[z]=x
        q[y]=w
        q[w]=y
    assert sorted(q[1:])==list(range(1,N+1))
    assert all(q[q[i]]==i for i in range(1,N+1))
    assert all(q[i]!=i for i in range(1,N+1))
    assert all(i+q[i] in powers for i in range(1,N+1))
    assert sum(q[i]!=p[i] for i in range(1,N+1)) == 4*len(range(1,H+1,3))
    print(f"PASS: explicitly constructed original and modified "
          f"{N}-element involutions, all sums cubes.")


def main():
    cases=((17,39,26,36),(99,172,120,163))
    for roots in cases:
        verify_symbolically(roots,1)
        verify_symbolically(roots,3)
    materialize_small(cases[0])
    print("PASS: taxicab switching and the exact 4-to-1 Hamming metric.")


if __name__=="__main__":
    main()
