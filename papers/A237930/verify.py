#!/usr/bin/env python3
"""Exact modular audits for all six forbidden prime classes in A237930."""
from math import gcd,isqrt
from pathlib import Path

FORBIDDEN={11,13,23,61,71,73}


def primes(limit):
    f=bytearray(b'\x01')*(limit+1)
    f[:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if f[p]:
            f[p*p::p]=b'\x00'*((limit-p*p)//p+1)
    return [p for p in range(2,limit+1) if f[p]]


def symbol(value,p):
    r=pow(value,(p-1)//2,p)
    assert r in (1,p-1)
    return 1 if r==1 else -1


def main():
    classified=set()
    for r in range(1,84):
        if gcd(r,84)>1:
            continue
        three=1 if r%12 in (1,11) else -1
        seven=(1 if r%7 in (1,2,4) else -1)*(-1 if r%4==3 else 1)
        if (three,seven)==(1,-1):
            classified.add(r)
    assert classified==FORBIDDEN
    print('PASS exact CRT classification of all six residue classes modulo 84')
    ps=primes(200000)
    excluded=[p for p in ps if p%84 in FORBIDDEN]
    for p in ps:
        if p in (2,3,7):
            continue
        three=1 if p%12 in (1,11) else -1
        seven=(1 if p%7 in (1,2,4) else -1)*(-1 if p%4==3 else 1)
        assert symbol(3,p)==three and symbol(7,p)==seven
    for p in excluded:
        assert symbol(3,p)==1 and symbol(7,p)==-1
    print(f'PASS independent Euler-criterion checks for all {len(excluded)} prohibited primes below 200000')
    # Complete exponent orbits for each small prohibited prime, independent
    # of the quadratic-symbol obstruction used in the proof.
    cycles=0
    for p in excluded:
        if p>5000:
            continue
        value=1
        while True:
            assert (7*value-1)%p
            value=3*value%p
            cycles+=1
            if value==1:
                break
    print(f'PASS complete exponent cycles for prohibited primes below 5000: {cycles} residues')
    rows=[]
    for line in Path(__file__).with_name('b237930-published.txt').read_text().splitlines():
        if line.strip() and not line.startswith('#'):
            rows.append(tuple(map(int,line.split())))
    assert [n for n,_ in rows]==list(range(1001))
    current=3
    for n,expected in rows:
        assert expected==current==(7*3**n-1)//2
        if n:
            assert current%7 and current%12
        current=3*current+1
    print('PASS all 1001 official terms, independent affine recurrence and exponential formula')


if __name__=='__main__':
    main()
