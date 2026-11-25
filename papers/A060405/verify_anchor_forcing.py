#!/usr/bin/env python3
"""Four-anchor congruence forcing for A060405 (Python 3, exact arithmetic)."""
from functools import lru_cache
from math import gcd, isqrt
from verify_sieve import M, certificate

ANCHORS = (3, -3, -2, -1)
I = (1,0,0,1)
A = (0,1,1,1)
B = (0,1,1,2)
EXPECTED = {
     3: ((53,109),(82,314),(20,365)),
    -3: ((43,86),(92,312),(20,365)),
    -2: ((46,93),(72,263),(25,323)),
    -1: ((52,107),(86,321),(21,374)),
}


def mul(a,b,q):
    x,y,z,w=a
    u,v,s,t=b
    return ((x*u+y*s)%q,(x*v+y*t)%q,
            (z*u+w*s)%q,(z*v+w*t)%q)


def mp(a,n,q):
    b=I
    while n:
        if n&1:
            b=mul(b,a,q)
        a=mul(a,a,q)
        n//=2
    return b


def primes(N):
    s=bytearray(b'\x01')*N
    s[:2]=b'\x00\x00'
    for p in range(2,isqrt(N-1)+1):
        if s[p]:
            s[p*p:N:p]=b'\x00'*len(range(p*p,N,p))
    return [p for p in range(2,N) if s[p]]


def val(n,q):
    a,b=mp(A,n,q),mp(B,n,q)
    return (2*a[0]+a[1]+b[1])%q


@lru_cache(None)
def factors(n):
    f=[]
    i=2
    while i*i<=n:
        if n%i==0:
            f.append(i)
            while n%i==0:
                n//=i
        i+=1 if i==2 else 2
    if n>1:
        f.append(n)
    return f


def order(q):
    # For prime q>5 both matrices have distinct nonzero roots in F_(q^2).
    h=q*q-1
    for d in set(factors(q-1)+factors(q+1)):
        while h%d==0 and all(mp(a,h//d,q)==I for a in (A,B)):
            h//=d
    assert all(mp(a,h,q)==I for a in (A,B))
    return h


def four_anchors():
    residues=certificate()
    q=2081
    assert q in primes(q+1)
    h=order(q)
    assert h==2080 and 2*M%h==0
    surviving=[]
    for r in residues:
        if any(pow(val(r+j*M,q),(q-1)//2,q)!=q-1 for j in (0,1)):
            surviving.append(r)
    assert surviving==sorted(r%M for r in ANCHORS)
    return surviving


def groups_for(D,orders,small):
    groups={}
    for q,h in orders:
        f=h//gcd(D,h)
        if f in small:
            groups.setdefault(f,[]).append((q,h))
    return groups


def forces(r,D,p,qs):
    ts=list(range(p))
    for q,h in qs:
        # D*p is a multiple of h. This tests all lifts modulo D*p.
        assert h//gcd(D,h)==p
        ts=[t for t in ts
            if pow(val((r+(D%h)*t)%h,q),(q-1)//2,q)!=q-1]
        assert 0 in ts  # Each anchor is an actual square at an integer index.
        if ts==[0]:
            return True
    return False


def anchor_divisors():
    small=set(primes(1001))
    orders=[(q,order(q)) for q in primes(100000) if q>5]
    assert len(orders)==9589
    result={}
    for r in ANCHORS:
        D=M
        for count,digits in EXPECTED[r]:
            groups=groups_for(D,orders,small)
            hits=[p for p,qs in sorted(groups.items())
                  if len(qs)>=2 and forces(r,D,p,qs)]
            assert len(hits)==count,(r,hits)
            # Distinct prime multipliers: the simultaneous conclusions combine.
            for p in hits:
                D*=p
            assert len(str(D))==digits,(r,D)
            print(r,count,digits)
        result[r]=D
    assert min(result.values())>10**322
    return result


if __name__=='__main__':
    print('Four anchors:',four_anchors())
    for r,D in anchor_divisors().items():
        print(f'anchor {r}: D = {D}')
    print('Only square index in [0, 10^322] is 3.')
