#!/usr/bin/env python3
"""Independent constructive and exact-minimum tests for OEIS A075018.

The mathematical theorem is in main.tex; these finite checks are additional.
No third-party dependencies required.
"""
from math import gcd
import random

OEIS_FIRST_65 = [
    3, 3, 3, 5, 3, 3, 5, 5, 6, 3, 18, 9, 11, 5, 3, 15, 13,
    15, 19, 23, 18, 29, 29, 15, 28, 11, 33, 5, 4, 3, 40,
    15, 18, 13, 18, 15, 28, 19, 24, 23, 26, 39, 7, 51, 33,
    29, 55, 15, 53, 53, 30, 63, 54, 33, 18, 5, 57, 41,
    56, 63, 69, 71, 60, 15, 63,
]


def smooth_part(N, base):
    q, m = 1, N
    x = base
    for p in range(2, x + 1):
        if x % p != 0:
            continue
        while x % p == 0:
            x //= p
        while m % p == 0:
            m //= p
            q *= p
    assert gcd(m, base) == 1
    return q, m


def witness(N, t, base, perm):
    assert N >= 1 and t >= 1 and base >= 2 and base % 2 == 0
    assert sorted(perm) == list(range(t))
    q, m = smooth_part(N, base)
    g = gcd(t, m)
    s = m // g
    half_sum = t * (t - 1) // 2
    assert half_sum % g == 0
    # Solve t*a == -half_sum (mod m), giving a class mod s.
    a_mod_s = (-(half_sum // g) * pow(t // g, -1, s)) % s if s > 1 else 0
    a_mod_q = (-perm[-1]) % q
    if s > 1:
        # a = a_mod_q + q*z and solve for z modulo s.
        z = ((a_mod_s - a_mod_q) * pow(q, -1, s)) % s
    else:
        z = 0
    modulus = q * s
    a_star = (a_mod_q + q * z) % modulus
    d = 1
    while True:
        B = base ** d
        if (B % q == 0 and (m == 1 or B % m == 1)
                and (base - 1) * base ** (d - 1) >= modulus + t - 1):
            low = base ** (d - 1)
            a = a_star + modulus * ((low - a_star + modulus - 1) // modulus)
            if low <= a and a + t - 1 < B:
                return d, a
        d += 1
        if d > 5000:
            raise RuntimeError((N, t, base))


def concat_mod(a, d, base, perm, N):
    v = 0
    mult = pow(base, d, N)
    for j in perm:
        v = (v * mult + a + j) % N
    return v


def literal_base(x, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out = ''
    while x:
        out = digits[x % base] + out
        x //= base
    return out or '0'


def test_oeis():
    for N, expected in enumerate(OEIS_FIRST_65, 1):
        winner = next(k for k in range(3, 1000)
                      if int(''.join(map(str, (k, k-1, k-2, k-3)))) % N == 0)
        assert winner == expected, (N, winner, expected)
    print('PASS: all 65 OEIS A075018 minimum terms')


def test_decimal_four():
    for N in range(1, 601):
        d, a = witness(N, 4, 10, [3, 2, 1, 0])
        assert concat_mod(a, d, 10, [3, 2, 1, 0], N) == 0
        assert 10**(d-1) <= a and a+3 < 10**d
        if d <= 5:
            C = int(''.join(map(str, (a+3, a+2, a+1, a))))
            assert C % N == 0
    print('PASS: universal descending-four construction for N=1..600')


def test_general():
    rng = random.Random(20261017)
    checks = 0
    for base in (2, 4, 6, 8, 10, 12, 16):
        for N in range(1, 81):
            for t in range(1, 13):
                perm = list(range(t))
                rng.shuffle(perm)
                d, a = witness(N, t, base, perm)
                assert base**(d-1) <= a <= a+t-1 < base**d
                assert concat_mod(a, d, base, perm, N) == 0
                if d * t <= 100:
                    word = ''.join(literal_base(a+j, base) for j in perm)
                    assert int(word, base) % N == 0
                checks += 1
    print(f'PASS: {checks} arbitrary-permutation checks (7 bases, 80 moduli, 12 lengths)')


def main():
    test_oeis()
    test_decimal_four()
    test_general()


if __name__ == '__main__':
    main()
