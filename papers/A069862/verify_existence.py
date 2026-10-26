#!/usr/bin/env python3
"""Construct A069862 witnesses, with independent exact-arithmetic audits.

No search cutoff is used by witness().  The proof is in main.tex.
The returned endpoint is a witness, not necessarily the least endpoint.
Standard library only; python3 verify_existence.py [--limit 250].
"""
import argparse
from math import gcd, lcm


def factor(n):
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def order10(m):
    assert m > 1 and gcd(m, 10) == 1
    phi = m
    for p in factor(m):
        phi = phi // p * (p - 1)
    r = phi
    for p in factor(phi):
        while r % p == 0 and pow(10, r // p, m) == 1:
            r //= p
    return r


def append(value, endpoint, count, width, modulus):
    """Binary composition of (value,t) -> (10**width*value+t+1,t+1)."""
    a, s, b, length = pow(10, width, modulus), 1, 1, 1
    t = endpoint
    while count:
        if count & 1:
            value = (a * value + s * t + b) % modulus
            t += length
        a, s, b = (a * a % modulus, s * (a + 1) % modulus,
                   (b * (a + 1) + s * length) % modulus)
        length *= 2
        count //= 2
    return value


def residue(n, endpoint, modulus=None):
    """Residue of (n+1)||...||endpoint, without constructing the word."""
    if modulus is None:
        modulus = n
    value, first = 0, n + 1
    width = len(str(first))
    boundary = 10 ** width
    while first <= endpoint:
        last = min(endpoint, boundary - 1)
        value = append(value, first - 1, last - first + 1, width, modulus)
        first, width, boundary = last + 1, width + 1, boundary * 10
    return value


def independent_residue(n, endpoint, modulus=None):
    """Geometric-derivative formula; exact division, no modular inverses.

    For a block a,...,a+L-1, (B-1)^2 times its concatenation equals
    a*B^(L+1)-(a-1)*B^L-(a+L)*B+(a+L-1).
    Reduction modulo modulus*(B-1)^2 preserves the subsequent division.
    """
    if modulus is None:
        modulus = n
    value, first = 0, n + 1
    base = 10 ** len(str(first))
    while first <= endpoint:
        last = min(endpoint, base - 1)
        length = last - first + 1
        denominator = (base - 1) ** 2
        extended = modulus * denominator
        power = pow(base, length, extended)
        numerator = (first * base * power - (first - 1) * power
                     - (first + length) * base + first + length - 1) % extended
        assert numerator % denominator == 0
        value = (pow(base, length, modulus) * value
                 + numerator // denominator) % modulus
        first, base = last + 1, base * 10
    return value


def witness(n):
    """Return (endpoint, digit width, displacement bound) from the proof."""
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 2, 1, 0
    factors = factor(n)
    alpha, beta, e = (factors.get(p, 0) for p in (2, 5, 3))
    smooth = 2 ** alpha * 5 ** beta
    primes = [(p, exp) for p, exp in sorted(factors.items()) if p >= 7]
    period = 2 * 3 ** e if e else 1
    digit_period = 1
    stages = []
    for a in range(1, e):
        stages.append((3, a, lcm(2 * 3 ** a, smooth)))
    for p, exp in primes:
        h = order10(p)
        full_order = order10(p ** exp)
        digit_period = lcm(digit_period, full_order)
        for a in range(exp):
            stages.append((p, a, lcm(h * p ** a, period, smooth)))
        period = lcm(period, p ** exp * full_order)
    displacement = sum((p - 1) * step for p, _, step in stages)
    initial_modulus = smooth * (3 if e else 1)
    width = 1
    lower = 1
    while (width < max(alpha, beta) or lower <= n
           or 9 * lower <= initial_modulus + displacement):
        width += digit_period
        lower = 10 ** (width - 1)
    assert width <= n  # Uniform bound proved separately in existence.tex.
    endpoint = (lower + initial_modulus - 1) // initial_modulus * initial_modulus
    initial = endpoint
    value = residue(n, endpoint)
    installed = initial_modulus
    assert value % installed == 0 and endpoint % smooth == 0
    for p, a, step in stages:
        modulus = p ** (a + 1)
        # The normalized slope is a unit by the two local lifting lemmas.
        if p == 3:
            slope = (step // (2 * 3 ** a)) * (2 * endpoint + 1) % 3
        else:
            slope = -(step // p ** a) * pow(pow(10, width, p) - 1, -1, p) % p
        assert slope and step % p ** a == 0 and value % p ** a == 0
        choice = -(value // p ** a) * pow(slope, -1, p) % p
        value = append(value, endpoint, choice * step, width, n)
        endpoint += choice * step
        installed = lcm(installed, modulus)
        assert value % installed == 0 and endpoint % smooth == 0
        assert initial <= endpoint <= initial + displacement < 10 ** width
    assert value == 0 and installed == n
    return endpoint, width, displacement


def audit(limit):
    # Direct digit appending across width boundaries checks both fast evaluators.
    checks = 0
    for n in range(1, 61):
        value = 0
        for t in range(n + 1, 240):
            value = (value * 10 ** len(str(t)) + t) % n
            assert residue(n, t) == independent_residue(n, t) == value
            checks += 1
    # Independently recompute all constructed huge endpoints, not just slopes.
    cases = sorted(set(range(1, limit + 1)) | {
        2 ** 12, 5 ** 7, 3 ** 8, 7 ** 2, 11 ** 3, 19 ** 2,
        2 ** 5 * 3 ** 4 * 5 ** 2 * 7 ** 2 * 11,
        3 ** 5 * 7 * 13 * 37, 9 * 11 * 31, 3 * 7 * 43,
    })
    widths = []
    for n in cases:
        endpoint, width, _ = witness(n)
        assert endpoint > n
        assert independent_residue(n, endpoint) == 0, n
        widths.append(width)
    print(f"PASS {checks} direct recurrence comparisons across digit boundaries")
    print(f"PASS {len(cases)} constructive witnesses, independently recomputed")
    print(f"Largest tested witness endpoint has {max(widths)} decimal digits")
    print("Universal existence follows from main.tex; these are finite implementation checks.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=250)
    args = parser.parse_args()
    audit(args.limit)
