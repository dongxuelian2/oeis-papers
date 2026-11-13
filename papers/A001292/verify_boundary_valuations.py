#!/usr/bin/env python3
"""Exact checks of the complete-digit-boundary theorem in main.tex."""
from fractions import Fraction as F
from math import factorial

from verify_a001292 import append_block


def valuation(n, p=3):
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def rational_valuation(x):
    return valuation(abs(x.numerator))-valuation(x.denominator) if x else 10**9


def rational_mod(x, mod):
    return x.numerator*pow(x.denominator, -1, mod) % mod


def taylor_audit(N=13):
    # The omitted logarithm terms have valuation at least 27. This is
    # beyond the precision needed for the first thirteen coefficients.
    ell = sum((F((-1)**(j+1)*9**j, j) for j in range(1, 14)), F(0))

    def add(a, b):
        return [x+y for x, y in zip(a, b)]

    def scale(a, c):
        return [x*c for x in a]

    def mul(a, b):
        return [sum((a[j]*b[n-j] for j in range(n+1)), F(0))
                for n in range(N)]

    def constant(c):
        return [F(c)]+[F(0)]*(N-1)

    def exp_zero(a):
        assert a[0] == 0
        out = term = constant(1)
        for j in range(1, N):
            term = mul(term, a)
            out = add(out, scale(term, F(1, factorial(j))))
        return out

    E = [ell**n/factorial(n) for n in range(N)]
    a = scale(E, F(1, 10))
    q = scale(a, 9)
    b = add(E, constant(-1))
    U, bpower = mul(a, a), constant(1)
    for r in range(N):
        choose = constant(1)
        for j in range(r+2):
            choose = mul(choose, add(q, constant(-j)))
        choose = scale(choose, F(1, 9*factorial(r+2)))
        U = add(U, mul(mul(add(mul(a, b), constant(1)), choose), bpower))
        bpower = mul(bpower, b)
    S = scale(add(mul([-F(1), F(9)]+[F(0)]*(N-2), E), constant(1)), F(1, 9))
    coefficients = mul(U, exp_zero(scale(S, -ell)))
    expected = [F(1, 200), F(169, 3000)*ell+ell**2/1800,
                F(671, 80000)*ell**2+F(353, 54000)*ell**3+ell**4/32400]
    assert coefficients[:3] == expected
    assert all(rational_valuation(c) >= n for n, c in enumerate(coefficients))
    assert rational_mod(coefficients[0], 9) == 5
    assert rational_mod(coefficients[1], 9) == 3
    assert rational_valuation(coefficients[2]) >= 3
    for d in range(1, 101):
        for n in range(1, 13):
            average = F(sum(j**n for j in range(1, d+1)), d)
            log_bound, power = 0, 3
            while power <= n+1:
                log_bound += 1
                power *= 3
            assert rational_valuation(average) >= -log_bound
    print('PASS: 13 exact Taylor coefficients, their valuation bounds,',
          'and 1200 rational power-sum averages')


def fast_boundary_audit(max_d=60000, precision=20):
    """Closed block formula with Euler reduction, not the matrix algorithm."""
    mod = 3**precision
    word = matrix_word = 0
    for d in range(1, max_d+1):
        h = valuation(d)
        e = h+2  # LTE for 10**d-1, before dividing its square.
        lifted = 3**(precision+2*e)
        phi = 2*(lifted//3)
        start = pow(10, d-1, lifted)
        B = pow(10, d, lifted)
        c = (B-1) % lifted
        shift = pow(B, 9*pow(10, d-1, phi) % phi, lifted)
        numerator = ((start*c+1)*shift-(B*c+1)) % lifted
        assert numerator % 3**(2*e) == 0
        c_unit = (pow(10, d, 3**(precision+e))-1)//3**e
        block = (numerator//3**(2*e)*pow(c_unit*c_unit, -1, mod)) % mod
        word = (word*(shift % mod)+block) % mod
        assert word % 3**e == 0 and word % 3**(e+1) != 0, d
        u = d//3**h
        assert word//3**e % 9 == u*(2+6*d) % 9, d
        if d <= 80:
            a = 10**(d-1)
            matrix_word = append_block(matrix_word, a, 9*a, d, mod)
            assert word == matrix_word, d
    print('PASS: exact boundary valuation and normalized unit for d=1..',
          max_d, '; independent matrix blocks for d=1..80', sep='')


def literal_audit():
    # A separate rolling concatenation reaches m=999999 in bounded memory.
    cuts = {0, 1, 2, 9, 10, 41, 99, 100, 998, 999, 1000, 999998}
    saved = {0: (0, 0)}
    mod = 3**10
    W = D = 0
    width, B, upper = 1, 10, 9
    all_prefixes = [(0, 0)]
    rotation_count = 0
    for m in range(1, 1000000):
        if m > upper:
            width += 1
            B *= 10
            upper = B-1
        W = (W*B+m) % mod
        D += width
        if m in cuts:
            saved[m] = W, D
        if m <= 999:
            all_prefixes.append((W, D))
        if m != upper:
            continue
        d = width
        h, u = valuation(d), d//3**valuation(d)
        v = h+2
        predicted = u*(2+6*d) % 9
        assert W//3**v % 9 == predicted
        assert valuation(D) == 2+h+valuation(d+1)
        selected = range(m) if m <= 999 else sorted(k for k in saved if k < m)
        for k in selected:
            P, length = all_prefixes[k] if m <= 999 else saved[k]
            R = (pow(10, length, mod)*W-(pow(10, D, mod)-1)*P) % mod
            assert R % 3**v == 0 and R % 3**(v+1) != 0
            assert R//3**v % 9 == predicted, (d, k)
            rotation_count += 1
    print('PASS: literal rolling prefixes through m=999999;', rotation_count,
          'actual rotation residues at complete boundaries')


def exclusion_table():
    checked = 0
    for h in range(33):
        v, rest = h+2, h+2
        for p in (2, 3):
            while rest % p == 0:
                rest //= p
        if rest != 1:
            continue
        for u in (1, 2, 4, 5, 7, 8):
            excluded = (u % 3 == 1 if v % 3 else
                        u in (1, 2, 7, 8) if v % 2 else u in (1, 7))
            d = 3**h*u
            unit = u*(2+6*d) % 9
            square_admissible = v % 2 == 0 and unit % 3 == 1
            cube_admissible = v % 3 == 0 and unit in (1, 8)
            assert excluded == (not square_admissible and not cube_admissible)
            checked += 1
    print('PASS: complete square/cube exclusion table;', checked,
          'valuation/unit classes')
    for d in range(1, 10001):
        if d % 27 not in (3, 6, 9, 21, 24):
            continue
        h = valuation(d)
        v = h+2
        unit = (d//3**h)*(2+6*d) % 9
        assert (v == 3 and unit not in (1, 8)) or (v == 4 and unit % 3 != 1)


if __name__ == '__main__':
    taylor_audit()
    fast_boundary_audit()
    literal_audit()
    exclusion_table()
