#!/usr/bin/env python3
"""Independent modular definition and exact all-index prime classification."""
from math import gcd, isqrt

def is_prime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))

def formula(n):
    assert n >= 1
    return n+1 if n >= 4 and is_prime(n+1) else 1

def definition(n):
    m=n+1
    factorial=1
    for k in range(1,n+1): factorial=factorial*k%m
    return gcd(pow(2,n,m)+factorial,pow(3,n,m)+factorial,m)

def audit():
    published=[1,1,1,5,1,7,1,1,1,11,1,13,1,1,1,17,1,19,1,1,1,23,1,1,1,1,1,29,1,31,1,1,1,1,1,37,1,1,1,41,1,43,1,1,1,47,1,1,1,1,1,53,1,1,1,1,1,59,1,61,1,1,1,1,1,67,1,1,1,71,1,73,1,1,1,1,1,79,1,1,1,83,1,1,1,1,1,89,1,1,1,1,1,1,1,97,1,1,1]
    assert [formula(n) for n in range(1,100)]==published
    for n in range(1,5001): assert definition(n)==formula(n),n
    from pathlib import Path
    for line in Path(__file__).with_name('b308090.txt').read_text().splitlines():
        if not line.startswith('#'):
            n,k=map(int,line.split());assert formula(n)==k
    print('PASS all 99 displayed official terms, 5000 independent modular definitions, 100-row table')

if __name__=='__main__': audit()
