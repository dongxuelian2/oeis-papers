#!/usr/bin/env python3
"""A077187: independent exact cyclotomic-gcd audit for orders 745..1000.

Input: rows emitted by the C++/GMP single-period ring certifier.
The checker does not call GMP, compute drift, or factor the repunit.
For all 35 new classes it verifies gcd(Phi_r(10), G_r) = 1, where
G_r = gcd(10^r-1,U_r,V_r). Therefore no prime dividing Phi_r(10)
can have zero drift. This is FINITE evidence, not an all-order proof.

Usage: python3 audit_cyclotomic_order_1000.py order1000_rows.tsv
"""
import hashlib
import math
import sys
from pathlib import Path

EXPECTED_SHA = "f4098f7f7113f0941c5423a33de3e9bf0c0a335c2e4d901b28851fab1495cddc"

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    sign=1
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0: return 0
            sign=-sign
        p+=1
    if n>1: sign=-sign
    return sign

def cyclotomic_at_ten(n):
    numerator=denominator=1
    for d in divisors(n):
        mu=mobius(n//d)
        if mu==1: numerator*=10**d-1
        if mu==-1: denominator*=10**d-1
    assert numerator%denominator==0
    phi=numerator//denominator
    assert phi>0 and (10**n-1)%phi==0
    return phi

def main(path):
    blob=Path(path).read_bytes()
    assert hashlib.sha256(blob).hexdigest()==EXPECTED_SHA
    rows=[tuple(map(int,line.split(","))) for line in blob.decode().splitlines()]
    assert len(rows)==35
    for r,T,G in rows:
        phi=cyclotomic_at_ten(r)
        h=math.gcd(phi,G)
        assert h==1,(r,T,G,h)
        print(f"PASS cyclotomic coprimality order={r} gcd={h}")
    print("PASS all 35 Phi_r(10) coprime to exact repunit drift gcds")
    print("NO unbounded-order theorem claimed")

if __name__ == "__main__":
    assert len(sys.argv)==2
    main(sys.argv[1])
