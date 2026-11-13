#!/usr/bin/env python3
"""Exact finite checks for STRUCTURE.md; not a proof of the global conjecture.

Only the standard library is required. Artificial power extensions below have
arbitrary prefixes and are explicitly NOT counterexamples to Kashihara.
"""
from math import gcd, isqrt
import sys

import verify_a001292 as previous

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(100000)  # Largest literal check has 38889 digits.


def word(a, b):
    """Literal decimal concatenation; an empty interval is the empty word."""
    return "".join(str(k) for k in range(a, b + 1))


def integer_root(a, e):
    """Floor of the positive e-th root, using integer binary search."""
    lo, hi = 0, 1 << ((a.bit_length() + e - 1) // e)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**e <= a:
            lo = mid
        else:
            hi = mid
    return hi if hi**e == a else lo


def primes_below(n):
    return [p for p in range(2, n)
            if all(p % q for q in range(2, isqrt(p) + 1))]


def valuation(a, p):
    assert a > 0
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def data(k, T=0):
    d = len(str(k))
    B, L = 10**d, 10**(d - 1)
    b = B - 1
    prefix = word(1, L - 1)
    A = b*b*int(prefix or "0") + L*b + 1
    H = A + b*b*T*10**len(prefix)
    return d, B, b, k - L + 1, (k + 1)*b + 1, A, H


def audit_previous():
    rotations = transitions = 0
    for m in range(1, 121):
        blocks = [str(k) for k in range(1, m + 1)]
        literal = [int("".join(blocks[j:] + blocks[:j])) for j in range(m)]
        for modulus in (13, 27, 81):
            assert list(previous.rotations_mod(m, modulus)) == [
                a % modulus for a in literal]
            rotations += m
    for modulus in (2, 5, 8, 9, 13, 27, 37, 81, 100, 169):
        for d in range(1, 5):
            a = 10**(d - 1)
            for n in (0, 1, 2, 7, 9, 20, 55):
                for z in (0, 1, 7):
                    direct = z % modulus
                    for k in range(a, a + n):
                        direct = (direct * 10**d + k) % modulus
                    assert previous.append_block(z, a, n, d, modulus) == direct
                    transitions += 1
    print("PASS: independent literal audit:", rotations, "rotation residues;",
          transitions, "matrix transitions")


def exact_identities():
    for d in range(1, 5):
        B, L, b = 10**d, 10**(d - 1), 10**d - 1
        A = b*b*int(word(1, L - 1) or "0") + L*b + 1
        for k in sorted({L - 1, L, L + 1, B - 2, B - 1}):
            W = int(word(1, k) or "0")
            assert b*b*W + (k + 1)*b + 1 == A*B**(k - L + 1)
        if d >= 2:
            assert (valuation(A, 2), valuation(A, 5)) == (d, d - 1)
            c, old_b = L, L - 1
            if d >= 3:
                assert A % (c*c) == 18*c % (c*c)
            else:
                assert A == 1209999989980
            old_L = L // 10
            old_A = old_b**2*int(word(1, old_L - 1) or "0")
            old_A += old_L*old_b + 1
            rhs = (10*c - 1)**2*old_A*c**(9*c//10)
            rhs -= 9*c*(10*c**3 - 11*c**2 + 12*c - 2)
            assert (c - 1)**2*A == rhs
    count = 0
    for m in range(2, 121):
        W = word(1, m)
        for k in range(1, m + 1):
            T = int(word(k + 1, m) or "0")
            F = int(word(k + 1, m) + word(1, k))
            d, B, b, t, C, A, H = data(k, T)
            assert b*b*F + C == H*B**t
            if len(str(m)) == d:
                C_m = (m + 1)*b + 1
                assert b*b*T == C*B**(m - k) - C_m
                assert H == A + 10**len(word(1, B//10 - 1))*(
                    C*B**(m - k) - C_m)
            assert F == 10**len(word(1, k))*int(W) - (
                10**len(W) - 1)*int(word(1, k))
            if k >= 10:
                assert (valuation(H, 2), valuation(H, 5)) == (d, d - 1)
            if m >= 11:
                assert H > b*b and H > 4*C*C
            count += 1
    print("PASS: fixed-digit identities d=1..4, coefficient recurrence;",
          count, "literal boundary rotations through m=120")


def small_cases():
    count = 0
    for m in range(2, 11):
        for k in range(1, m + 1):
            F = int(word(k + 1, m) + word(1, k))
            # x >= 2 implies 2**e <= F, hence e < F.bit_length().
            for e in primes_below(F.bit_length()):
                assert integer_root(F, e)**e != F, (m, k, e)
            count += 1
    print("PASS:", count, "small rotations, all possible prime exponents")


def extension(k, e):
    """Lift roots digit by digit, keeping ALL residue roots at each precision."""
    W = word(1, k)
    target = int(W)
    roots, modulus = [0], 1
    for _ in W:
        modulus_next = 10*modulus
        roots = [r + h*modulus for r in roots for h in range(10)
                 if (pow(r + h*modulus, e, modulus_next) -
                     target % modulus_next) % modulus_next == 0]
        assert roots, (k, e, modulus_next)
        modulus = modulus_next
    x = min(roots)
    if x**e <= target:
        x += modulus
    power = x**e
    T, remainder = divmod(power, modulus)
    assert remainder == target and T > 0
    assert str(power).endswith(W)
    d, B, b, t, C, A, H = data(k, T)
    n, s = divmod(d*t, e)
    Q = 10**n
    y = b*x
    a = b**(e - 2)*H*10**s
    c0 = b**(e - 2)*C
    g = gcd(y, Q)
    P, q = y//g, Q//g
    assert y**e == a*Q**e - c0
    assert C % g**e == 0 and P % b == 0 and gcd(P, q) == 1
    assert H > 4*C*C and H > b*b
    assert integer_root(a, e)**e != a
    # Exact certificate: alpha < y/Q + 1/(2*Q**e).
    assert a*(2*Q**e)**e < (2*y*Q**(e - 1) + 1)**e
    if e == 2:
        # Independent standard continued fraction of sqrt(a), no floats.
        u, v, digit = 0, 1, isqrt(a)
        p0, p1, q0, q1 = 0, 1, 1, 0
        while True:
            pc, qc = digit*p1 + p0, digit*q1 + q0
            if (pc, qc) == (P, q):
                break
            assert qc <= q, (k, e, pc, qc, P, q)
            p0, p1, q0, q1 = p1, pc, q1, qc
            u = v*digit - u
            v = (a - u*u)//v
            digit = (isqrt(a) + u)//v
    return g, x, power


def power_extensions():
    examples = [(41, 2), (11, 3), (11, 7), (11, 11), (112, 3)]
    for k, e in examples:
        g, _, _ = extension(k, e)
        if (k, e) == (112, 3):
            assert g == 2
    _, x, power = extension(41, 2)
    print("PASS: 5 artificial power extensions, including g=2; exact bounds",
          "and an independent square-root continued fraction")
    print("Example (NOT an A001292 counterexample):")
    print("x =", x)
    print("x^2 =", power)


if __name__ == "__main__":
    audit_previous()
    exact_identities()
    small_cases()
    power_extensions()
    print("Global Kashihara conjecture remains OPEN.")
