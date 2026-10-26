#!/usr/bin/env python3
"""Exact-integer checks for the A087354 / A391022 / A391189 paper.

The proof is in main.tex. This file demonstrates factor parity, exact digit
length, existing OEIS examples and ascending-square partitions. No packages.
"""
from functools import lru_cache
from fractions import Fraction
from math import isqrt


A087354_FIRST_19 = (
    1, 49, 144, 1444, 11449, 1119364, 36144144,
    251444449, 991494144, 4914991449, 149991994944,
    149991994944, 98191114994449, 118194491449441,
    1991164114941444, 9141411499911441,
    119499194999141136, 199499144494999441,
    9914419419914449449,
)

A391022_FIRST_8 = (
    1, 49, 1936, 1416100, 143664196,
    1491615214489, 149225256576841, 1416368119690022500,
)


def square_partition(value: int, block_count: int, strictly_increasing=False):
    """An independent exact search for a displayed square decomposition."""
    word = str(value)
    assert isqrt(value)**2 == value

    @lru_cache(None)
    def find(pos: int, count: int, previous: int):
        if pos == len(word):
            return () if count == block_count else None
        if count >= block_count:
            return None
        for end in range(pos+1, len(word)+1):
            chunk = word[pos:end]
            if chunk[0] == '0':
                continue
            x = int(chunk)
            if isqrt(x)**2 != x:
                continue
            if strictly_increasing and x <= previous:
                continue
            suffix = find(end, count+1, x if strictly_increasing else 0)
            if suffix is not None:
                return (x,)+suffix
        return None

    partition = find(0, 0, 0)
    if partition is not None:
        assert len(partition) == block_count
        assert ''.join(str(x) for x in partition) == word
        assert all(x > 0 and isqrt(x)**2 == x for x in partition)
        if strictly_increasing:
            assert all(x < y for x,y in zip(partition,partition[1:]))
    return partition


def exact_ratio(u: int, v: int) -> Fraction:
    return Fraction(2**max(u,0)*5**max(v,0),
                    2**max(-u,0)*5**max(-v,0))


def extension(X: int, u: int, v: int, h: int):
    """Construct with exact rational checks; no floating point used."""
    assert X >= 1 and h >= max(abs(u),abs(v))+1
    q=exact_ratio(u,v)
    assert q > 1
    alpha = Fraction(X,2)*(q-1/q)
    assert 10*alpha**2 > 1 and alpha**2 < 1, (X,u,v)
    A=Fraction(X*10**h,1)/q
    B=Fraction(X*10**h,1)*q
    assert A.denominator==B.denominator==1
    A,B=int(A),int(B)
    assert A%2==B%2==0
    Y=(B-A)//2
    Z=(B+A)//2
    square=Y*Y
    assert 10**(2*h-1) < square < 10**(2*h)
    assert len(str(square))==2*h
    assert X*X*10**(2*h)+square == Z*Z
    assert str(Z*Z)==str(X*X)+str(square)
    return Y,Z


def numerical_tests():
    assert 1*10**4 + 5625 == 125**2
    cases=[(1,1,0,2),(3,-2,1,3),(7,14,-6,15),
           (12,14,-6,15),(38,7,-3,8),(125,137,-59,138)]
    for X,u,v,h in cases:
        Y,Z=extension(X,u,v,h)
        for extra_h in (1,2):
            Y2,Z2=extension(X,u,v,h+extra_h)
            assert Y2**2 > Y**2
            assert len(str(Y2**2))==2*(h+extra_h)
            assert Z2**2 == X*X*10**(2*(h+extra_h))+Y2**2
    Y,Z=extension(7,14,-6,15)
    assert Y==332155892578125
    assert Z==7007876107421875
    assert 49*10**30+Y*Y==Z*Z
    assert '4'+'9'+str(Y*Y)==str(Z*Z)
    print('PASS: 6 independent exact Pythagorean extension witnesses, plus arbitrary h')
    print('PASS: strictly increasing 3-block example 4|9|square = square')


def oeis_examples():
    for n,a in enumerate(A087354_FIRST_19,1):
        result=square_partition(a,n)
        assert result is not None, ('A087354',n,a)
    print('PASS: 19 OEIS A087354 published squares admit n nonzero-square blocks')
    for n,a in enumerate(A391022_FIRST_8,1):
        result=square_partition(a,n,strictly_increasing=True)
        assert result is not None, ('A391022',n,a)
    print('PASS: 8 OEIS A391022 displayed values have strictly ascending square blocks')


def main():
    oeis_examples()
    numerical_tests()
    print('STATUS: universal result is proved symbolically, not by finite computation')


if __name__=='__main__':
    main()
