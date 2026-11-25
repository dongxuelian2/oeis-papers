#!/usr/bin/env python3
"""Exact sparse CRT and p-adic divisibility certificates for A060405."""
from math import gcd, isqrt
from verify_sieve import certificate, M as BASE

EXT = (449,641,14081,7681,107,15121,7129,2267,9721,3889,4373,8747,
       21871,9601,2801,3001,22751,251,23813,587,5881,33751,13751,
       22639,6173,22637,12347,13721,12289,9437)
TAIL = (37,47,59,61,67,73,101,103,113,137,139,149,157,163,167,173,
        179,191,193,211,223,227,229,233,263,277)
LIMIT = 10**18
IDENTITY = (1,0,0,1)
LUCAS = (0,1,1,1)
PELL = (0,1,1,2)


def period(q):
    start = (2 % q,1,0,1)
    a,b,c,d = start
    squares = {x*x % q for x in range(q)}
    flags = []
    for _ in range(2*(q*q-1)):
        flags.append((a+c)%q in squares)
        a,b,c,d = b,(a+b)%q,d,(c+2*d)%q
        if (a,b,c,d) == start:
            return flags
    raise AssertionError(q)


def sparse_sieve():
    modulus, residues = BASE, certificate()
    for q in EXT:
        flags = period(q)
        p = len(flags)
        f = p//gcd(p,modulus)
        residues = sorted(r+k*modulus for k in range(f) for r in residues
                          if flags[(r+k*modulus)%p])
        modulus *= f
    assert (modulus,len(residues)) == (3020727790080000,722)
    candidates = [r+k*modulus for r in residues
                  for k in range((LIMIT-r)//modulus+1)]
    assert len(candidates) == 239014
    for q in TAIL:
        flags = period(q)
        candidates = [n for n in candidates if flags[n%len(flags)]]
    assert candidates == [3]
    print('Only square index in [0, 10^18]:', candidates)


def mul(a,b,q):
    x,y,z,w=a; u,v,s,t=b
    return ((x*u+y*s)%q,(x*v+y*t)%q,(z*u+w*s)%q,(z*v+w*t)%q)


def matpow(a,n,q):
    result=IDENTITY
    while n:
        if n&1: result=mul(result,a,q)
        a=mul(a,a,q); n//=2
    return result


def primes(N):
    sieve=bytearray(b'\x01')*N
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(N-1)+1):
        if sieve[p]: sieve[p*p:N:p]=b'\x00'*len(range(p*p,N,p))
    return [p for p in range(17,N) if sieve[p]]


def forcing_round(D, ps):
    hits=[]
    for p in ps:
        if D%p==0: continue
        h=gcd(D,p*p-1)
        if any(matpow(A,h,p)!=IDENTITY for A in (LUCAS,PELL)): continue
        a,b=matpow(LUCAS,h,p*p),matpow(PELL,h,p*p)
        z=(-a[0]+2*a[1]+b[0])%(p*p)
        assert z%p==0
        if z: hits.append(p)
    return hits


def forced_divisor():
    D=BASE
    ps=primes(30000)
    for expected in (38,263,338,161,32):
        hits=forcing_round(D,ps)
        assert len(hits)==expected
        for p in hits: D*=p
        print('Forced primes:',len(hits),'digits of divisor:',len(str(D)))
    assert len(str(D))==3230 and D>10**3229
    assert len(set(p for p in ps if D%p==0))==832
    return D


def two_adic():
    for A in (LUCAS,PELL):
        assert matpow(A,48,16)==IDENTITY
    a,b=matpow(LUCAS,48,128),matpow(PELL,48,128)
    assert (-a[0]+2*a[1]+b[0])%128==16


if __name__=='__main__':
    sparse_sieve()
    two_adic()
    forced_divisor()
