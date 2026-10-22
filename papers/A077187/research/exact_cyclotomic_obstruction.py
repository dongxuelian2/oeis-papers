#!/usr/bin/env python3
"""Exact primitive-order zero-drift decision via cyclotomic gcd.

For fixed r>=2:
 H_r = gcd(Phi_r(10), drift_U, drift_V).
 There exists a prime p with ord_p(10)=r and zero drift
 iff stripping factors of r from H_r leaves an integer > 1.

This is a complete equivalence for drift, not universal existence of
a mountain. Run from this directory, no third-party dependencies:
  python3 exact_cyclotomic_obstruction.py
"""
from math import gcd
from certify_orders_le500 import order_class_drift
from audit_cyclotomic_spots import cyclotomic_at_ten

def strip_index_factors(h,r):
    assert h>0 and r>=2
    while True:
        g=gcd(h,r)
        if g==1:
            return h
        h//=g

def decision(r):
    T,N,G,U,V=order_class_drift(r)
    phi=cyclotomic_at_ten(r)
    assert N%phi==0
    H=gcd(phi,G)
    assert H==gcd(phi,U,V)
    remaining=strip_index_factors(H,r)
    return r,T,G,H,remaining

def audit():
    # Includes lower-order contaminants, nontrivial index-supported
    # cyclotomic gcd, and larger-order samples.
    expected = {
        56:(9,1,1),
        88:(99,1,1),
        112:(9,1,1),
        168:(189,1,1),
        174:(189,1,1),
        258:(189,1,1),
        272:(153,17,1),
        312:(351,1,1),
        336:(189,1,1),
    }
    for r,(g,h,residue) in expected.items():
        got=decision(r)
        assert got[2:]==(g,h,residue),(r,got)
        print('PASS r',r,'G',g,'H',h,'primitive-residue',residue)
    print('PASS exact primitive-order obstruction identity on 9 diverse orders')
    print('General cyclotomic support conjecture remains OPEN.')

if __name__ == '__main__':
    audit()
