#!/usr/bin/env python3
"""Exact witnesses for mixed-unit order/valuation implications."""
from math import gcd, isqrt

# q, p, sqrt(2), sqrt(5) modulo p, sign, two exact orders,
# (lambda^q-1)/p modulo p for the active factor.
ROWS = (
    (29,1023991,310331,35345,1,170665,29,497979),
    (31,311,66,117,1,31,155,56),
    (31,30071,10262,11959,1,15035,31,28073),
    (53,6679,2879,2199,1,53,371,4829),
    (61,1831,596,274,1,61,915,1547),
    (61,7321,1320,1521,-1,915,61,4868),
    (71,569,201,104,1,142,71,85),
    (73,33289,10005,8824,1,73,2774,12109),
    (97,3881,604,1070,-1,97,485,1088),
    (6679,66791,6823,26613,-1,6679,33395,32664),
)
FORBIDDEN = 2*5*7*11*13

def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))

def prime_factors(n):
    for d in range(2,isqrt(n)+1):
        if n%d==0:
            yield d
            while n%d==0:
                n//=d
    if n>1:
        yield n

def exact_order(a,h,p):
    return pow(a,h,p)==1 and all(
        pow(a,h//d,p)!=1 for d in prime_factors(h)
    )

def lift(a,d,p):
    assert 0<a<p and (a*a-d)%p==0
    b=a+p*((d-a*a)//p*pow(2*a,-1,p)%p)
    assert (b*b-d)%(p*p)==0
    return b

def verify():
    graph={}
    for q,p,r2,r5,sign,h,j,unit in ROWS:
        assert prime(q) and prime(p) and p>q>13
        assert p % 16 in (7, 9)
        mod=p*p
        beta=(1+lift(r2,2,p))%mod
        alpha=(1+lift(r5,5,p))*pow(2,-1,mod)%mod
        u=alpha*alpha%mod
        eta=sign*beta*pow(u,-1,mod)%mod
        xi=sign*beta*u%mod
        assert pow(sign*2*r2%p,(p-1)//2,p)==p-1
        assert exact_order(eta,h,p) and exact_order(xi,j,p)
        assert (h==q) != (j==q)
        active,other=(eta,j) if h==q else (xi,h)
        assert gcd(other,FORBIDDEN)>1
        assert 0<unit<p and pow(active,q,mod)==1+p*unit
        graph.setdefault(q,set()).add(p)
    assert 6679 in graph[53] and 66791 in graph[6679]
    for q,targets in sorted(graph.items()):
        print(q,'->',sorted(targets))
    print('Verified',len(ROWS),'exact norm-order implications.')

if __name__=='__main__':
    verify()
