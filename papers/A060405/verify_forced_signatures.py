#!/usr/bin/env python3
"""Combine exact zero-anchor local square classes as linear equations over F_2."""
from math import gcd
from verify_smooth_support import A, B, I, primes, power, zero_value, local_data, unit

M = 720720
CUTOFF = 9857
DUAL = int('1c8b31d13bbead82c2bd7fc78c326f22c508e656d29ec271b6edb0e0e3b85d5aadc3ab0ac0bff4e327372c7da87c5b3b433b98f29a1bcf131a144f3014f39b2e635b4c401cb4a168f8a4b416092766cfba373f3646da5e9ee0a6833175aa7aa2396e48f4218149a750',16)


def forced_divisor():
    D = M
    units = {}
    ps = [p for p in primes(29999) if p >= 17]
    for expected in (38,263,338,161,32):
        hits = []
        for p in ps:
            if D % p == 0:
                continue
            h = gcd(D,p*p-1)
            if any(power(C,h,p)!=I for C in (A,B)):
                continue
            z = zero_value(h,p*p)
            assert z%p == 0
            if z:
                units[p] = (z//p)*pow(h,-1,p)%p
                hits.append(p)
        assert len(hits) == expected
        for p in hits:
            D *= p
    assert len(units)==832 and len(str(D))==3230
    return D,units


def unit_bits_2(u):
    assert u%2
    return int(u%4==3) | (int(u%8 in (3,5))<<1)


def add(basis,v):
    while v:
        j = v.bit_length()-1
        if j in basis:
            v ^= basis[j]
        else:
            basis[j] = v
            return True
    return False


def reduce(basis,v):
    while v:
        j = v.bit_length()-1
        if j not in basis:
            break
        v ^= basis[j]
    return v


def certificate():
    D, units = forced_divisor()
    E = 7*11*13
    for p in units:
        E *= p
    for p in (2,3,7,11,13):
        h,par,c,d,e = local_data(p)
        assert D%h==0 and par==int(p in (7,11,13))
        units[p]=c
    assert (E%8,E%3)==(3,1)
    odd_test = sorted(set(units)-{2})
    assert len(odd_test)==836

    def vector(q):
        assert q not in units and q%2
        z=unit_bits_2(q)
        for i,p in enumerate(odd_test,2):
            if pow(q%p,(p-1)//2,p)==p-1:
                z |= 1<<i
        return z

    target=unit_bits_2(unit(E,2)*units[2])
    for i,p in enumerate(odd_test,2):
        z=unit(E,p)*units[p]%p
        assert z
        if pow(z,(p-1)//2,p)==p-1:
            target |= 1<<i
    assert target.bit_count()==379
    assert D%CUTOFF!=0 and CUTOFF in primes(CUTOFF)
    eligible=[5]+[p for p in primes(CUTOFF-1) if D%p!=0]
    assert len(eligible)==836
    basis={}
    for p in eligible:
        v=vector(p)
        assert (DUAL&v).bit_count()%2==0
        add(basis,v)
    assert len(basis)==835 and reduce(basis,target)!=0
    assert DUAL.bit_count()==420 and DUAL%4==0
    assert (DUAL&target).bit_count()%2==1
    # Confirm that 9857 is the first possible bound for this relaxation.
    assert add(basis,vector(CUTOFF))
    assert len(basis)==836 and reduce(basis,target)==0
    print('Forced primes:',832,'local character constraints:',838)
    print('Columns below 9857:',len(eligible),'rank:',835)
    print('Dual obstruction:',DUAL.bit_count(),'rows')
    print('Every square offset must contain a new odd-valuation prime >=',CUTOFF)
    print('Adding 9857 makes this necessary linear system consistent.')


if __name__=='__main__':
    certificate()
