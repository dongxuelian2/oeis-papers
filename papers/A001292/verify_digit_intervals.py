#!/usr/bin/env python3
"""Exact audits of the quadratic reduction on complete digit intervals.

Matrix prefixes and literal appending do not use the quadratic formula.
The CRT audit enumerates every class of a two-prime product modulus.
The unbounded coverage corollary additionally uses Dirichlet's theorem.
"""
from fractions import Fraction
from math import gcd, lcm

from verify_a001292 import append_block, direct_prefix_mod, digits_total
from verify_boundary_characters import closed_boundary, trial_prime
from verify_boundary_valuations import valuation
from verify_general_boundary_primes import matrix_prefixes
from verify_local_primes import length_mod


def order(a, modulus):
    assert gcd(a, modulus) == 1
    value, exponent = a % modulus, 1
    while value != 1:
        value = value*a % modulus
        exponent += 1
    return exponent


def literal_audit():
    total = 0
    for m in (100, 101, 126, 371, 500, 999):
        text = ''.join(str(j) for j in range(1, m+1))
        target = (m*(m+1)//2+33) % 37
        length = 0
        for k in range(m):
            R = int(text[length:]+text[:length])
            assert R % 37 == pow(10, length, 37)*target % 37
            if m == 126:
                assert R % 27 == 9 and pow(R % 37, 18, 37) == 36
            length += len(str(k+1))
            total += 1
    # The next integer crosses the digit interval and the old formula fails.
    assert direct_prefix_mod(1000, 37) != (1000*1001//2+33) % 37
    print('PASS:', total, 'literal rotations, including all 126 rotations',
          'of the new residue-family example; digit-width crossing checked', flush=True)


def interval_audit(p, r, P, d):
    assert trial_prime(p) and p >= 7 and d % P == 0 and P % r == 0
    assert pow(10, P, 9*r) == 1 and P % p != 0
    assert order(10, p) == r
    a = valuation(d, p)
    precision = a+1
    mod = p**precision
    phi, period = (p-1)*p**(precision-1), (p-1)*mod
    C = closed_boundary(P, p, r)[0]
    prefix = 0
    for _, prefix in matrix_prefixes(p, d-1, precision):
        pass
    L, upper = 10**(d-1), 10**d-1
    B, start = pow(10, d, mod), pow(10, d-1, mod)
    before_length = length_mod(d-1, phi)
    small_cuts = [(direct_prefix_mod(k, mod), digits_total(k) if k else 0)
                  for k in (0, 1, 9, 41)]
    small_cuts.append((prefix, before_length))
    counts, checks, word = set(), 0, prefix
    limit = min(p*p, 9*L)
    for i in range(limit):
        m = (start+i) % mod
        previous = word
        word = (B*word+m) % mod
        polynomial = (m*(m+1)//2+C*(d//P)) % mod
        assert word == polynomial, (p, d, i)
        D = (before_length+d*(i+1)) % phi
        shift = (pow(10, D, mod)-1) % mod
        assert shift == 0
        for cut, cut_length in small_cuts+[(previous, (D-d) % phi)]:
            R = (pow(10, cut_length, mod)*word-shift*cut) % mod
            assert R == pow(10, cut_length, mod)*polynomial % mod
            checks += 1
        if a and word % p == 0 and word % (p*p) != 0:
            counts.add((start+i) % (p*p))
    if a:
        assert limit == p*p and len(counts) == 2*(p-1)
    # Matrix appending at the far endpoint and interior positions, including
    # truncation by zero blocks at m=10**d-1. Exponents use a matrix period.
    samples = sorted({m for m in (L, L+9*L//2, upper-p*p, upper-p, upper-1, upper)
                      if L <= m <= upper})
    for m in samples:
        count = m-L+1
        actual = append_block(prefix, start, count % period, d, mod)
        expected = (m*(m+1)//2+C*(d//P)) % mod
        assert actual == expected, (p, d, m % 10000)
        D = (before_length+d*(count % phi)) % phi
        assert pow(10, D, mod) == 1
    print(f'PASS: p={p}, d={d}, precision={precision}; {checks} rotation residues, '
          f'{len(samples)} endpoint/interior matrices, {len(counts)} valuation-one classes', flush=True)


def explicit_classes():
    for u in (1, 2, 7, 37, 37**2):
        roots = {296*u % 1369, (1073*u-1) % 1369}
        found = set()
        for m in range(1369):
            value = (m*(m+1)//2+1221*u) % 1369
            if value == 0:
                assert m in roots
            if value % 37 == 0 and value:
                found.add(m)
        expected = {m for m in range(1369)
                    if m % 37 in (0, 36) and m not in roots}
        assert found == expected and len(found) == 72
    # d=3 mod 111, m=126 mod 999: valuation 2 at 3 forces a square,
    # and the common 37-character excludes squares, uniformly in the cut.
    for t in (0, 1, 7, 10**30):
        d = 3+111*t
        for u in (0, 1, 13, 10**30):
            m = 126+999*u
            assert m % 27 == 18 and d % 3 == 0
            assert (m*(m+1)//2) % 27 == 9
            assert (m*(m+1)//2+33*(d//3)) % 37 == 5
    print('PASS: exact 37-adic root classes for five parameters, including zero',
          'offsets; the two-parameter m=126 mod 999 exclusion family', flush=True)


def crt_audit():
    p, q = 37, 43
    d = lcm(3*p, 42*q)
    modp, modq = p*p, q*q
    cp, cq = 33*(d//3) % modp, 21*(d//42) % modq
    A = {m for m in range(modp)
         if (m*(m+1)//2+cp) % p == 0 and (m*(m+1)//2+cp) % modp != 0}
    B = {m for m in range(modq)
         if (m*(m+1)//2+cq) % q == 0 and (m*(m+1)//2+cq) % modq != 0}
    assert len(A) == 72 and len(B) == 84
    both = union = 0
    M = modp*modq
    flags = bytearray(M)
    for m in range(M):
        ap, bq = m % modp in A, m % modq in B
        both += ap and bq
        union += ap or bq
        flags[m] = ap or bq
    theta = (1-Fraction(72, modp))*(1-Fraction(84, modq))
    assert both == 72*84
    assert union == M*(1-theta)
    prefix = [0]
    for flag in flags:
        prefix.append(prefix[-1]+flag)

    def count_before(n):
        return (n//M)*union+prefix[n % M]

    for start, H in ((0, 1), (17, 999), (2000, 7*M+123),
                     (M-31, 2*M+87), (10**30+7, 11*M+999)):
        actual = count_before(start+H)-count_before(start)
        assert actual >= H*(1-theta)-M
    print(f'PASS: all {M} CRT classes at d={d}, {union} excluded classes, '
          f'{both} joint classes, and five exact interval-discrepancy checks', flush=True)


def admissible_prime_audit():
    checked = 0
    for p in range(43, 1000, 40):
        if not trial_prime(p):
            continue
        r = order(10, p)
        assert pow(2, (p-1)//2, p) == p-1
        assert pow(5, (p-1)//2, p) == p-1
        assert (p-1)//2 % 10 == 1 and gcd(r, 10) == 1
        P = lcm(r, order(10, 9*r))
        assert P % p != 0 and pow(10, P, 9*r) == 1
        checked += 1
    print(f'PASS: {checked} primes in the progression 3 mod 40 have the',
          'required orders and admissible periods; divergence uses Dirichlet', flush=True)


def main():
    literal_audit()
    for case in ((37, 3, 3, 3), (37, 3, 3, 111), (37, 3, 3, 4107),
                 (43, 21, 42, 42), (43, 21, 42, 1806),
                 (53, 13, 78, 78), (53, 13, 78, 4134)):
        interval_audit(*case)
    explicit_classes()
    crt_audit()
    admissible_prime_audit()


if __name__ == '__main__':
    main()
