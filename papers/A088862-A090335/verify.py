#!/usr/bin/env python3
"""Exact witnesses and an independent string/divisor audit; Python stdlib only."""
from functools import lru_cache
from itertools import product
from math import isqrt, prod


def iroot(n, exponent):
    lo, hi = 0, 1 << ((n.bit_length() + exponent - 1) // exponent)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid**exponent <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


@lru_cache(None)
def is_prime(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def interval(b, r, k):
    return (iroot(b ** (k * r - 1), r) + 1,
            iroot(b ** (k * (r + 1) - 1) - 1, r + 1))


@lru_cache(None)
def cluster(b, r, count):
    for k in range(2, r * r + 33):
        lo, hi = interval(b, r, k)
        primes = []
        for p in range(lo, hi + 1):
            if is_prime(p):
                primes.append(p)
                if len(primes) == count:
                    assert all(p**r > b**(k*r-1) and
                               p**(r+1) < b**(k*(r+1)-1) for p in primes)
                    return k, tuple(primes)
    raise AssertionError((b, r, count))


def digits(n, b):
    out = []
    while n:
        n, d = divmod(n, b)
        out.append(d)
    return tuple(reversed(out))


def divisors(factors):
    return sorted(prod(p**e for (p, _), e in zip(factors, powers))
                  for powers in product(*(range(e+1) for _, e in factors)))


def prefix_free(ds, b):
    # Lexicographically adjacent words suffice: all extensions of a prefix
    # occupy a contiguous interval in this ordering.
    words = sorted(digits(d, b) for d in ds if d > 1)
    return all(v[:len(u)] != u for u, v in zip(words, words[1:]))


def factor(n):
    fs = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            fs.append((p, e))
        p += 1
    if n > 1:
        fs.append((n, 1))
    return fs


def audit():
    constructions = divisor_count = 0
    for b in range(2, 17):
        profiles = [(r,) for r in range(1, 25)]
        profiles += [(1,)*r for r in range(1, 11)]
        profiles += [(2, 1), (1, 3), (2, 2), (1, 2, 1), (3, 2, 1), (2, 2, 2)]
        for profile in profiles:
            r = sum(profile)
            k, ps = cluster(b, r, len(profile))
            fs = tuple(zip(ps, profile))
            ds = divisors(fs)
            assert prefix_free(ds, b), (b, fs)
            # Check lengths directly against actual numeral representations.
            for exponents in product(*(range(e+1) for e in profile)):
                d = prod(p**e for p, e in zip(ps, exponents))
                if d > 1:
                    assert len(digits(d, b)) == k * sum(exponents)
            constructions += 1
            divisor_count += len(ds) - 1

    # Published data start with factor count zero despite first offset 1.
    repeated = [1, 2, 9, 125, 625, 3125, 15625, 78125, 9921875,
                1260078125, 25937424601, 285311670611, 145223640340999,
                21557022777501157, 799006685782884121,
                15181127029874798299, 288441413567621167681,
                5480386857784802185939]
    distinct = [1, 2, 33, 2093, 239723, 29918977, 17597346187,
                17155385292853, 10633323942990239, 15790705299133143889]
    for values, total in [(repeated, True), (distinct, False)]:
        for r, n in enumerate(values):
            fs = factor(n)
            assert (sum(e for _, e in fs) if total else len(fs)) == r
            assert prefix_free(divisors(fs), 2)

    # Independent direct enumeration of the smallest counts.
    best_total, best_distinct = {}, {}
    for n in range(1, 5000):
        fs = factor(n)
        if prefix_free(divisors(fs), 2):
            best_total.setdefault(sum(e for _, e in fs), n)
            best_distinct.setdefault(len(fs), n)
    assert [best_total[r] for r in range(6)] == repeated[:6]
    assert [best_distinct[r] for r in range(4)] == distinct[:4]
    assert not prefix_free(divisors([(2, 2)]), 2)
    assert not prefix_free(divisors([(2, 1), (3, 1)]), 2)
    print(f"PASS: {constructions} constructions in bases 2..16; "
          f"{divisor_count} divisor words; 28 published entries; "
          "all integers below 5000 audited for initial minima.")


if __name__ == '__main__':
    audit()
