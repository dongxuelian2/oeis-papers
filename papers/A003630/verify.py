#!/usr/bin/env python3
"""Exact finite Euler-factor audits for the A003630 product theorem."""
from fractions import Fraction as Q
from math import isqrt,log,exp,sqrt,fsum
from pathlib import Path


def chi4(n):
    return 0 if n%2==0 else (1 if n%4==1 else -1)


def chi3(n):
    return 0 if n%3==0 else (1 if n%3==1 else -1)


def prime_sieve(limit):
    flags=bytearray(b'\x01')*(limit+1)
    flags[:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if flags[p]:
            flags[p*p::p]=b'\x00'*((limit-p*p)//p+1)
    return [p for p in range(2,limit+1) if flags[p]]


def main():
    rows=[]
    for line in Path(__file__).with_name('b003630-published.txt').read_text().splitlines():
        if line.strip() and not line.startswith('#'):
            rows.append(tuple(map(int,line.split())))
    assert [n for n,_ in rows]==list(range(1,1001))
    ps=prime_sieve(1_000_000)
    inert=[p for p in ps if p%12 in (5,7)]
    assert inert[:1000]==[p for _,p in rows]
    for p in ps:
        if p>3:
            # Independent Euler-criterion test for the inert-prime definition.
            assert (pow(3,(p-1)//2,p)==p-1)==(p%12 in (5,7))
    print('PASS all 1000 official prime terms and Euler criterion through 1000000')
    direct=[p for p in range(2,20001)
            if all(p%d for d in range(2,isqrt(p)+1))]
    assert direct==[p for p in ps if p<=20000]
    print('PASS independent trial-primality control through 20000')
    pprod,l3,l4=Q(1),Q(1),Q(1)
    checked=0
    for p in [p for p in ps if p<=10000]:
        l3*=Q(p,p-chi3(p))
        l4*=Q(p,p-chi4(p))
        if p%12 in (5,7):
            factor=Q(p-1,p+1)
            pprod*=factor if p%4==1 else 1/factor
        if p>=3:
            assert pprod==Q(9,8)*l3/l4
            checked+=1
    print(f'PASS exact rational partial-product identity at all {checked} prime cutoffs 3..10000')
    # The primitive characters differ at the two omitted primes. These
    # factors are essential and are checked without floating-point arithmetic.
    assert Q(2,2-chi3(2))/Q(2,2-chi4(2))==Q(2,3)
    assert Q(3,3-chi3(3))/Q(3,3-chi4(3))==Q(4,3)
    assert Q(2,3)*Q(4,3)==Q(8,9)
    print('PASS exceptional Euler factors p=2,3 and exact correction 9/8')
    for cutoff in [100,1000,10000,100000,1000000]:
        value=exp(fsum(chi4(p)*log((p-1)/(p+1)) for p in inert if p<=cutoff))
        print(f'Numerical control only: P({cutoff})={value:.12f}; limit={sqrt(3)/2:.12f}')
    print('The infinite limit is proved analytically in main.tex; finite products do not certify it.')


if __name__=='__main__':
    main()
