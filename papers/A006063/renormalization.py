#!/usr/bin/env python3
"""Cube-sum permutation renormalization, independent of the 173 threshold.

A four-interval reversal gives a legal length-171 permutation.
The map T(n)=343*n+171 satisfies P(T(n))>=P(n)**343.
The 343 independent fibers embed arbitrary tuples of valid matchings.

Run without dependencies. Tests m=7 and m=316, plus exact fifth-cycle
modification confined to one fiber.
"""
from math import isqrt

L, A = 343, 171
SEED = [(1,7,8),(8,19,27),(20,44,64),(45,171,216)]

def cube_sum_check(p):
    n=len(p)-1
    assert sorted(p[1:])==list(range(1,n+1)), f"not a permutation n={n}"
    cubes={k**3 for k in range(2,2*isqrt(n)+10) if k**3<=2*n}
    assert all(i+p[i] in cubes for i in range(1,n+1)), f"not a cube-sum n={n}"

def seed171():
    p=[0]*(A+1)
    for lo,hi,c in SEED:
        for i in range(lo,hi+1):
            assert p[i]==0
            p[i]=c-i
    cube_sum_check(p)
    assert all(p[p[i]]==i for i in range(1,A+1))
    return p

def two_reflections316():
    p=[0]*317
    for i in range(1,27):
        p[i]=27-i
    for i in range(27,317):
        p[i]=343-i
    cube_sum_check(p)
    return p

def other_316(p):
    q=p.copy()
    cycle=(1,219,50,268,99)
    for j,i in enumerate(cycle):
        q[i]=p[cycle[(j+1)%len(cycle)]]
    cube_sum_check(q)
    assert sum(p[i]!=q[i] for i in range(1,317))==5
    return q

def renormalize(fibers):
    n=len(fibers[0])-1
    assert len(fibers)==L
    assert all(len(p)==n+1 for p in fibers)
    out=[0]*(L*n+A+1)
    out[:A+1]=seed171()
    for r,p in enumerate(fibers,1):
        for i in range(1,n+1):
            x=A+L*(i-1)+r
            out[x]=A+L*(p[i]-1)+L+1-r
            assert x+out[x]==L*(i+p[i])
    cube_sum_check(out)
    return out

def main():
    p7=[0]+[8-i for i in range(1,8)]
    cube_sum_check(p7)
    q=renormalize([p7]*L)
    assert len(q)-1==2572
    print("PASS: pure 4-block seed n=171, affine lift 7 -> 2572.")

    a=two_reflections316()
    b=other_316(a)
    base=renormalize([a]*L)
    family=[a]*L
    family[0]=b
    alt=renormalize(family)
    assert len(base)-1==343*316+171==108559
    changed=[i for i in range(1,len(base)) if base[i]!=alt[i]]
    assert len(changed)==5
    assert all((i-A-1)%L==0 for i in changed)
    print("PASS: n=316 -> 108559; independent fiber modification "
          "changes exactly 5 positions.")
    for n in (7,316):
        curr=n
        for iteration in range(1,5):
            curr=L*curr+A
            assert 2*curr+1==(2*n+1)*L**iteration
        print(f"PASS: T^4({n})={((2*n+1)*L**4-1)//2} "
              f"and exact affine composition.")

if __name__=="__main__":
    main()
