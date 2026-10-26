#!/usr/bin/env python3
"""Exact polynomial-prime pairing and counterexample controls."""
from math import gcd,isqrt

def greatest_prime_factor(n):
    largest,p=1,2
    while p*p<=n:
        while n%p==0: largest,n=p,n//p
        p+=1
    return max(largest,n)

def term(n):
    assert n>=2
    p=greatest_prime_factor(n**3-1)
    return p if p>n else 1

def audit():
    published=[7,13,7,31,43,19,73,13,37,19,157,61,211,241,1,307,1,127,421,463,1,79,601,31,37,757,271,67,1,331,151,1123,397,97,43,67,1483,223,547,1723,139,631,283,109,103,61,181,1,2551,379,919,409,2971,79,103,3307,163,3541,523,97,3907,109,73,613]
    assert [term(n) for n in range(2,66)]==published
    checked=0
    for n in range(2,5001):
        p=term(n)
        q=greatest_prime_factor(n*n+n+1)
        assert p==(q if q>n else 1)
        if p==1: continue
        m=p-n-1
        assert m>=2 and m!=n and (m*m+m+1)%p==0 and (m*m+m+1)//p<p,(n,m,p)
        if m<=5000: assert term(m)==p
        assert gcd(n*n+n+1,m*m+m+1)==p*gcd((n*n+n+1)//p,m-n)
        checked+=1
    # Independent root enumeration for every prime p<=1000.
    for p in range(2,1001):
        if not all(p%d for d in range(2,isqrt(p)+1)): continue
        roots=[n for n in range(2,p) if (n*n+n+1)%p==0]
        assert len(roots)==(2 if p%3==1 else 0),(p,roots)
        assert all(term(n)==p for n in roots)
    assert term(16)==term(18)==1 # Literal conjecture 2 lacks a nonunit qualification.
    assert term(35)==term(61)==97 and gcd(1261,3783)==1261
    from pathlib import Path
    for line in Path(__file__).with_name('b357127.txt').read_text().splitlines():
        if not line.startswith('#'):
            n,k=map(int,line.split());assert term(n)==k
    print(f'PASS 64 official terms; {checked} nonunit involution/gcd cases n<=5000; roots of every prime <=1000; both counterexamples; 100-row table')

if __name__=='__main__': audit()
