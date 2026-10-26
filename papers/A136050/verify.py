#!/usr/bin/env python3
"""Official-data and independent prime checks for A136050's conjecture."""
from math import isqrt
from pathlib import Path


def prime(n):
    return n >= 2 and all(n % d for d in range(2,isqrt(n)+1))


def twin_pairs(limit):
    flags=bytearray(b'\x01')*(limit+1)
    flags[:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if flags[p]:
            flags[p*p::p]=b'\x00'*((limit-p*p)//p+1)
    return [(p,p+2) for p in range(2,limit-1) if flags[p] and flags[p+2]]


def digit_sum(n):
    total=0
    while n:
        n,d=divmod(n,10)
        total+=d
    return total


def main():
    data=[]
    for line in Path(__file__).with_name('b136050-published.txt').read_text().splitlines():
        if line.strip() and not line.startswith('#'):
            data.append(tuple(map(int,line.split())))
    assert [n for n,_ in data] == list(range(1,5001))
    pairs=twin_pairs(2_000_000)
    assert len(pairs)>5000
    for index,((p,q),(_,expected)) in enumerate(zip(pairs,data),1):
        assert digit_sum(p*q)==sum(map(int,str(p*q)))==expected
        if index>1:
            assert p>3 and (p+1)%6==0
            m=(p+1)//6
            assert p*q==36*m*m-1
            assert digit_sum(p*q)%9==8
    assert data[0]==(1,6)
    print('PASS all 5000 official terms and every stated congruence')
    direct=[(p,p+2) for p in range(2,20001) if prime(p) and prime(p+2)]
    assert direct == [(p,q) for p,q in pairs if q<=20000]
    print(f'PASS independent trial-primality enumeration of {len(direct)} pairs through 20000')
    for p,q in pairs[1:]:
        assert digit_sum(p*q)%9==8
    print(f'PASS conjecture for all {len(pairs)-1} noninitial twin pairs through 2000000')


if __name__=='__main__':
    main()
