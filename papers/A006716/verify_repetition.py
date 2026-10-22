#!/usr/bin/env python3
"""Exact finite checks for A006716 repeated-square research.

The symbolic non-square theorem uses Ljunggren (1943); these checks do not
replace it. This script has no dependencies outside the Python stdlib.
"""
from itertools import product
from math import isqrt

SEEDS = (144, 441, 1444, 11449, 44944)


def phi(n):
    r, p = n, 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            r -= r // p
        p += 1
    if n > 1:
        r -= r // n
    return r


def repeated_mod(a, k, modulus):
    """Compute a*(10**(d*k)-1)//(10**d-1) mod modulus exactly."""
    base = 10 ** len(str(a))
    den = base - 1
    r = pow(base, k, den * modulus)
    assert (r - 1) % den == 0
    return a * ((r - 1) // den) % modulus


def test_square_words():
    for a in SEEDS:
        assert isqrt(a) ** 2 == a
        for k in range(2, 13):
            word = int(str(a) * k)
            assert word == a * (10 ** (len(str(a)) * k) - 1) // (
                10 ** len(str(a)) - 1)
            assert isqrt(word) ** 2 != word
            for modulus in (8, 16, 32, 64, 128, 256, 5, 25, 125, 625):
                squares = {r * r % modulus for r in range(modulus)}
                assert repeated_mod(a, k, modulus) in squares
    print("PASS: direct concatenation identities, nonsquares, local prime powers")


def test_arithmetic_progressions():
    squares_by_modulus = {}
    for modulus in range(1, 351):
        squares_by_modulus[modulus] = {
            r * r % modulus for r in range(modulus)
        }
    for a in (144, 441, 1444):
        base = 10 ** len(str(a))
        for modulus in range(1, 351):
            m = modulus
            while m % 2 == 0:
                m //= 2
            while m % 5 == 0:
                m //= 5
            step = phi((base - 1) * m)
            for j in (1, 2, 3):
                assert repeated_mod(a, j * step, modulus) in (
                    squares_by_modulus[modulus]
                ), (a, modulus, step, j)
    print("PASS: explicit progression moduli 1..350 for seeds 144,441,1444")


def test_suffixes():
    squares = {r * r % 1000 for r in range(1000)}
    tails = [
        "".join(t)
        for t in product("149", repeat=3)
        if int("".join(t)) in squares
    ]
    assert tails == ["144", "441", "444", "449", "944"], tails
    print("PASS: 5 possible length-3 suffixes")


if __name__ == "__main__":
    test_square_words()
    test_arithmetic_progressions()
    test_suffixes()
