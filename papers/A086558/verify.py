#!/usr/bin/env python3
"""Deterministic small certificates and the exact finite prime-tuple formula."""
import json
from functools import lru_cache
from itertools import permutations
from math import isqrt
from pathlib import Path


@lru_cache(None)
def is_prime(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def nextprime(n):
    p = n+1
    while not is_prime(p):
        p += 1
    return p


def iroot(n, e):
    lo, hi = 0, 1 << ((n.bit_length()+e-1)//e)
    while lo < hi:
        mid = (lo+hi+1)//2
        if mid**e <= n:
            lo = mid
        else:
            hi = mid-1
    return lo


def ceiling_root(n, e):
    r = iroot(n, e)
    return r if r**e == n else r+1


def factor(n):
    out, p = [], 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def signature(n):
    return sorted(e for _, e in factor(n))


def minimum(n):
    if n == 1:
        return 1
    d = len(str(n))
    L, U = n*10**(n-d), (n+1)*10**(n-d)
    best = U
    for exponents in set(permutations(signature(n))):
        def visit(j, C, previous):
            nonlocal best
            e = exponents[j]
            if j == len(exponents)-1:
                root = ceiling_root((L+C-1)//C, e)
                q = nextprime(max(previous, root-1))
                candidate = C*q**e
                if candidate < best:
                    best = candidate
                return
            bound = iroot((best-1)//C, sum(exponents[j:]))
            for p in range(previous+1, bound+1):
                if is_prime(p):
                    visit(j+1, C*p**e, p)
        visit(0, 1, 1)
    assert best < U
    return best


def audit():
    rows = json.loads(Path(__file__).with_name('finite_witnesses.json').read_text())
    assert [row['n'] for row in rows] == list(range(2, 17))
    for row in rows:
        n, C, q, e = (row[k] for k in ('n', 'C', 'q', 'e'))
        assert is_prime(q) and C % q != 0
        M = C*q**e
        sig = sorted([ee for _, ee in factor(C)]+[e])
        assert sig == signature(n)
        assert len(str(M)) == n and str(M).startswith(str(n))

    # Both integer-root endpoints are checked exhaustively, including powers.
    for e in range(1, 9):
        for n in range(1, 2000):
            r = ceiling_root(n, e)
            assert (r-1)**e < n <= r**e

    # Check the numerical inequalities only as controls; the paper proves
    # their infinite range analytically using monotonicity.
    from math import log, log2
    for n in range(17, 10001):
        p, e = factor(n)[-1]
        d = len(str(n))
        logx = log(p)+(n-d)*log(10)/e
        assert logx > log(396738)
        assert 25*logx*logx > e*(n+1)
        if n >= 64:
            assert d <= n/4 and e**3 <= 4*n

    published = [1, 23, 307, 4489, 50021, 600007, 7000003, 80062991,
                 900660121, 1000000006, 11000000021, 120000000004,
                 1300000000021, 14000000000001, 150000000000017,
                 1604502443050081]
    for n in range(1, 13):
        assert minimum(n) == published[n-1], (n, minimum(n))
    for n in (4, 8, 9, 16):
        e = signature(n)[0]
        L = n*10**(n-len(str(n)))
        value = nextprime(ceiling_root(L, e)-1)**e
        assert value == published[n-1]

    # Independent integer-by-integer minima on a complete small interval.
    for n in range(1, 7):
        L, U = n*10**(n-len(str(n))), (n+1)*10**(n-len(str(n)))
        exact = next(M for M in range(L, U) if signature(M) == signature(n))
        assert exact == minimum(n)
    print("PASS: 15 finite witnesses with exhaustive prime trial division; "
          "15992 integer-root controls; large-index inequalities n=17..10000; "
          "12 published minima, 4 prime-power reductions, and 6 direct scans.")


if __name__ == '__main__':
    audit()
