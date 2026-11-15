"""Exact checks for Section 7 of IRRATIONAL_TARGET_ASSESSMENT.md.

The rational samples obey the inherited divisibilities; no sample is
claimed to be a perfect-power rotation.
"""
from fractions import Fraction
from math import gcd, isqrt

D = 17830
r = Fraction(297, 2)
example = []
for _ in range(2):
    r = (r*r+D)/(2*r)
    example.append(r)
assert example == [Fraction(159529, 1188),
                   Fraction(50613765361, 379040904)]
assert all(z.denominator % 99 == 0 for z in example)

checks = 0
for d in range(2, 6):
    B = 10**d
    C = B-1
    L = B//10
    for k in (L+7, 2*L, 4*L, 8*L):
        for e in (0, 1):
            D = 10**e*(k*C+B)
            if isqrt(D)**2 == D:
                continue
            q = 10**(20*d)
            p = C*(isqrt(D*q*q)//C)
            r = Fraction(p, q)
            assert r.numerator % C == 0 and gcd(D, C) == 1
            for _ in range(3):
                p, q = r.numerator, r.denominator
                aa, bb = p*p+D*q*q, 2*p*q
                assert gcd(aa, q) == 1
                assert gcd(aa, p) == gcd(D, p)
                assert (2*D) % gcd(aa, bb) == 0
                assert p*p <= aa <= 5*p*p and bb <= 2*p*p
                r = Fraction(aa, bb)
                assert r.denominator % C == 0
                height = max(r.numerator, r.denominator)
                assert 2*D*height >= p*p and height <= 5*p*p
                checks += 1
print(f'PASS: exact example and {checks} Newton denominator/height-bound checks.')
print('Synthetic rational samples; no square rotation or conjecture exclusion inferred.')
