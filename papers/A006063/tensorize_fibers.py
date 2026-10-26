#!/usr/bin/env python3
"""Exact independent-fiber tensorization checks for cube-sum permutations.

On a shifted interval I with A=(L-1)//2 and L=t**3 (t odd),
select a potentially DIFFERENT 236-element cube-sum permutation p_r
for each r in [1,L]. Map x=A+(i-1)*L+r to
A+(p_r(i)-1)*L+(L+1-r). Then x+Q(x)=L*(i+p_r(i)).
The map from the tuple (p_1,...,p_L) is injective, so the interval
contains precisely P(236)**L constructed permutations.

Run on moderate t=3 and 5 by default; additionally compare two distinct
fiber choices while leaving every other fiber unchanged.
"""
import argparse
from count_236 import template

M=236
BLOCKS = ((10+j,137+j,46+j,198+j,71+j) for j in range(9))


def get_base_fiber(mask, base):
    p=base.copy()
    for j in range(9):
        if not (mask & (1<<j)):
            continue
        cycle=(10+j,137+j,46+j,198+j,71+j)
        for z,u in enumerate(cycle):
            p[u]=base[cycle[(z+1)%5]]
    cubes={k**3 for k in range(2,9)}
    assert sorted(p[1:])==list(range(1,M+1))
    assert all(i+p[i] in cubes for i in range(1,M+1))
    return p


def build(t, masks):
    assert t>=1 and t%2
    L=t**3
    A=(L-1)//2
    assert len(masks)==L
    base=template()
    distinct={mask:get_base_fiber(mask,base) for mask in set(masks)}
    Q=[0]*(A+M*L+1)
    for r,mask in enumerate(masks,1):
        p=distinct[mask]
        for i in range(1,M+1):
            x=A+(i-1)*L+r
            y=A+(p[i]-1)*L+(L+1-r)
            Q[x]=y
            assert x+y==L*(i+p[i])
    assert sorted(Q[A+1:])==list(range(A+1,A+M*L+1))
    return Q,A,L


def audit(t):
    L=t**3
    masks=[(73*(r-1)+19)%512 for r in range(1,L+1)]
    Q,A,L=build(t,masks)
    mutated=masks.copy()
    target=L//2
    mutated[target]=(mutated[target]+1)%512
    Q2,B,_=build(t,mutated)
    assert A==B and Q2!=Q
    indices=[i for i in range(A+1,A+M*L+1) if Q[i]!=Q2[i]]
    assert indices and all((i-A-1)%L==target for i in indices)
    print(f"PASS t={t}, cube-block L={L}, shifted size={M*L}, "
          f"independent fibers={L}, injection test PASS")


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--t",nargs="*",type=int,default=[3,5])
    args=ap.parse_args()
    for t in args.t:audit(t)
