#!/usr/bin/env python3
"""Direct XOR triangles versus an independent binomial-parity formula."""
from math import comb
from pathlib import Path


def triangle(n):
    row=[int(c) for c in bin(n)[2:]]
    result=0
    while row:
        result=2*result+row[-1]
        row=[a^b for a,b in zip(row,row[1:])]
    return result


def masks(length):
    return [sum(1<<i for i in range(j+1) if comb(j,i)%2) for j in range(length)]


def formula(n):
    result=0
    for mask in masks(n.bit_length()):
        result=2*result+((n&mask).bit_count()%2)
    return result


def transform(bits):
    return [sum(comb(j,i)*bits[i] for i in range(j+1))%2
            for j in range(len(bits))]


def main():
    official=[]
    for line in Path(__file__).with_name('b334595-published.txt').read_text().splitlines():
        if line.strip() and not line.startswith('#'):
            official.append(tuple(map(int,line.split())))
    assert [n for n,_ in official]==list(range(1,8192))
    for n,expected in official:
        assert triangle(n)==formula(n)==expected
    print('PASS all 8191 published terms against independent XOR and binomial implementations')
    record=0
    locations=[]
    for length in range(1,17):
        ms=masks(length)
        values=[]
        for n in range(1<<(length-1),1<<length):
            value=0
            for mask in ms:
                value=2*value+((n&mask).bit_count()%2)
            values.append(value)
            assert (value==1)==(n&(n-1)==0)
            if value>record:
                record=value
                locations.append(n)
        if length>1:
            assert max(values)==(1<<length)-2
            assert values.index(max(values))==1
            assert values.count(max(values))==1
    assert locations==[1]+[(1<<j)+1 for j in range(1,16)]
    print('PASS both conjectures and unique block maxima for all n=1..65535')
    for length in range(1,11):
        for n in range(1<<length):
            bits=[(n>>i)&1 for i in range(length)]
            assert transform(transform(bits))==bits
    print('PASS self-inverse Pascal transform on every binary vector of lengths 1..10')


if __name__=='__main__':
    main()
