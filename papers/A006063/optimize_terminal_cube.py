#!/usr/bin/env python3
"""Verify optimally shortened terminal-cube construction.

Odd t>=9, L=t^3, B=(473L-1)/2,
k=min {integer k: k^3>473L},
N=k^3-B-1.
Then N=(473/2+o(1))*L and P(N)>=P((L-1)//2)*512^L.
No floating-point cube roots.
"""
import argparse
from construct_linear import make as valid_prefix
from count_236 import template as base_236


def optimal_params(t):
    assert t>=9 and t&1
    L=t**3
    A=(L-1)//2
    B=A+236*L
    threshold=473*L
    lo,hi=0,1
    while hi**3<=threshold:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**3<=threshold:lo=mid
        else:hi=mid
    k=hi
    N=k**3-B-1
    assert (k-1)**3<=threshold<k**3
    assert N>B and N-B==k**3-473*L
    return L,A,B,k,N


def verify(t):
    L,A,B,k,n=optimal_params(t)
    p=[0]*(n+1)
    p[1:A+1]=valid_prefix(A)
    base=base_236()
    for i in range(1,237):
        for r in range(1,L+1):
            x=A+(i-1)*L+r
            p[x]=A+(base[i]-1)*L+(L+1-r)
            assert x+p[x]==L*(i+base[i])
    for x in range(B+1,n+1):
        p[x]=k**3-x
    assert sorted(p[1:])==list(range(1,n+1))
    possible={j**3 for j in range(2,2*k+2) if j**3<=2*n}
    assert all(i+p[i] in possible for i in range(1,n+1))
    count=0
    for shift in range(9):
        cycle=(10+shift,137+shift,46+shift,198+shift,71+shift)
        for r in range(1,L+1):
            V=[A+(i-1)*L+r for i in cycle]
            assert all(V[z]+p[V[(z+1)%5]] in possible for z in range(5))
            count+=1
    assert count==9*L
    print(f"PASS t={t}, k={k}, N={n}, suffix={n-B}; "
          f"at least 2**{count} matchings.")


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--t",type=int,nargs="*",default=[9,11])
    args=ap.parse_args()
    for t in args.t:verify(t)
