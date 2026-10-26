#!/usr/bin/env python3
"""Exact finite minimum versus independent factorization and direct x scans."""
from math import gcd, isqrt


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def iroot(n, e):
    lo, hi = 0, 1 << ((n.bit_length()+e-1)//e)
    while lo < hi:
        mid = (lo+hi+1)//2
        if mid**e <= n:
            lo = mid
        else:
            hi = mid-1
    return lo


def minimum_formula(p):
    if p == 2:
        return 5
    U, B = (p-1)//2, (p+1)**2//4
    candidates = [U]
    for r in range(3, (B-1).bit_length()):
        if not is_prime(r):
            continue
        lo = iroot(p, r)+1
        hi = iroot(B-1, r)
        for y in range(max(2, lo), hi+1):
            z = y**r-p
            x = isqrt(z)
            if x > 0 and x*x == z:
                candidates.append(x)
    return min(candidates)


def maximal_exponent(n):
    g, p = 0, 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            g = gcd(g, e)
        p += 1
    if n > 1:
        g = gcd(g, 1)
    return g


def brute(p):
    for x in range(1, (p-1)//2+1 if p > 2 else 6):
        e = maximal_exponent(x*x+p)
        if e > 1:
            return x, e, iroot(x*x+p, e)
    raise AssertionError(p)


def audit():
    ps = [p for p in range(2, 1224) if is_prime(p)]
    assert len(ps) == 200
    xs, es, ys = [], [], []
    for p in ps:
        actual = minimum_formula(p)
        x, e, y = brute(p)
        assert actual == x and y**e == x*x+p
        # Independent maximal-root characterization.
        V = x*x+p
        largest = max(k for k in range(2, V.bit_length()) if iroot(V, k)**k == V)
        assert largest == e
        xs.append(x)
        es.append(e)
        ys.append(y)
    assert xs[:20] == [5,1,2,1,4,6,8,9,2,14,1,18,20,21,9,26,29,8,33,21]
    assert es[:20] == [3,2,2,3,3,2,4,2,3,2,5,2,2,2,7,6,2,3,2,9]
    assert ys[:20] == [3,2,3,2,3,7,3,10,3,15,2,19,21,22,2,3,30,5,34,2]
    print("PASS: exact minima and both companions at the first 200 primes; "
          "60 published entries; maximal exponents checked by two methods.")


if __name__ == '__main__':
    audit()
