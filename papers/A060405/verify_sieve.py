#!/usr/bin/env python3
"""Reproducible modular certificate for A060405 square indices."""
from math import isqrt

M = 720720
MODULI = (3,5,7,11,13,17,19,23,29,31,41,43,71,79,83,89,
          131,181,197,199,281,307,467,521,631,881,911,991,1249,1321,16)
EXPECTED = [3,360357,360363,720717,720718,720719]

def period_values(q):
    start = (2 % q, 1 % q, 0, 1)
    a,b,c,d = start
    values = []
    for _ in range(M):
        values.append((a+c) % q)
        a,b,c,d = b,(a+b)%q,d,(c+2*d)%q
        if (a,b,c,d) == start:
            return values
    raise AssertionError(f"no return within {M} for modulus {q}")

def certificate():
    residues = list(range(M))
    for q in MODULI:
        values = period_values(q)
        p = len(values)
        assert M % p == 0
        squares = {x*x % q for x in range(q)}
        residues = [n for n in residues if values[n % p] in squares]
        print(q, p, len(residues))
    assert residues == EXPECTED, residues
    return residues

def check_prefix(N=10000):
    a,b,c,d = 2,1,0,1
    hits = []
    for n in range(N+1):
        z = a+c
        if isqrt(z)**2 == z:
            hits.append(n)
        a,b,c,d = b,a+b,d,c+2*d
    assert hits == [3], hits
    return hits

if __name__ == "__main__":
    print("modular survivors:", certificate())
    print("square indices in 0..10000:", check_prefix())
    print("By the certificate, 3 is the only square index below 360357.")
