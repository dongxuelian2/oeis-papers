#!/usr/bin/env python3
"""Check exact power-residue certificates at complete decimal boundaries.

The universal character and period arguments are proved in main.tex. This
checker verifies their finite inputs, with complete Lucas primality proofs,
independent matrix concatenations, and literal rotations at small boundaries.
"""
import json
from fractions import Fraction as F
from math import gcd, isqrt, lcm
from pathlib import Path

from verify_a001292 import append_block, rotations_mod
from verify_boundary_valuations import valuation

CERTIFICATE = Path(__file__).with_name('BOUNDARY_CHARACTERS.json')


def trial_prime(n):
    if n < 2:
        return False
    return all(n % a for a in range(2, isqrt(n)+1))


def distinct_factors(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def check_lucas(record):
    q = record['q']
    factors = record['q_minus_1_factorization']
    product = 1
    assert len({p for p, _ in factors}) == len(factors)
    for p, e in factors:
        assert trial_prime(p) and e > 0
        product *= p**e
    assert product == q-1
    a = record['lucas_witness']
    assert pow(a, q-1, q) == 1
    for p, _ in factors:
        assert gcd(pow(a, (q-1)//p, q)-1, q) == 1
    r, P = record['order_10'], record['block_period']
    assert gcd(10, r) == 1 and r % 2 == 1
    assert pow(10, r, q) == 1
    assert all(pow(10, r//p, q) != 1 for p in distinct_factors(r))
    assert P % r == 0 and pow(10, P, 9*r) == 1
    return q, r, P


def closed_boundary(d, q, r):
    """Arithmetic-geometric formula, independent of matrix concatenation."""
    V = 0
    a_q, a_r = 1, 1 % r
    S_r = 0
    for j in range(1, d+1):
        B = 10*a_q % q
        N = 9*a_q % q
        shift = pow(B, 9*a_r % r, q)
        if B == 1:
            U = (N*a_q+N*(N-1)*pow(2, -1, q)) % q
        else:
            c = B-1
            U = ((a_q*c+1)*shift-(B*c+1))*pow(c*c, -1, q) % q
        V = (shift*V+U) % q
        S_r = (S_r+9*j*a_r) % r
        a_q = 10*a_q % q
        a_r = 10*a_r % r
    return V, S_r


def matrix_boundary(d, q):
    V = 0
    a = 1
    for j in range(1, d+1):
        V = append_block(V, a, 9*a, j, q)
        a *= 10
    return V


def adic_exclusions(d):
    h = valuation(d)
    unit = d//3**h*(2+6*d) % 9
    exponents = set(distinct_factors(h+2))
    if 2 in exponents and unit % 3 != 1:
        exponents.remove(2)
    if 3 in exponents and unit not in (1, 8):
        exponents.remove(3)
    return exponents


def density_audit(data, moduli):
    Q = 440334654777631
    square_primes = (37, 333667, 757, Q)
    alpha = beta = F(1)
    for q in square_primes:
        row = moduli[q]
        r, P = row['order_10'], row['block_period']
        assert 27 % P == 0 and pow(10, (q-1)//2, q) == 1
        C, S = closed_boundary(27, q, r)
        assert C != 0 and S == 0
        for a in range(27):
            first, S_a = closed_boundary(a, q, r)
            second, _ = closed_boundary(a+27, q, r)
            assert (second-first) % q == C*pow(10, S_a, q) % q
        alpha *= F(q+1, 2*q)
    for q in (37, 333667):
        assert pow(10, (q-1)//3, q) == 1
        beta *= F(q+2, 3*q)
    assert len({x*x % 757 for x in range(757)}) == 379
    assert len({pow(x, 7, 757) for x in range(757)}) == 109
    # Audit the disjoint 3-adic parts over their common exact period.
    counts = [0]*7
    for d in range(1, 730):
        tags = [d % 3 == 2, d % 27 in (12, 15),
                d % 27 == 18, d % 27 == 0]
        assert sum(tags) <= 1
        for i, tag in enumerate(tags):
            counts[i] += tag
        h = valuation(d)
        extra = [h == 3, h == 5,
                 d % 729 in (81, 567)]
        assert sum(extra) <= 1
        if any(extra):
            assert tags[3]
        for i, tag in enumerate(extra, 4):
            counts[i] += tag
        if extra[2]:
            assert not adic_exclusions(d)
    assert counts == [243, 54, 27, 27, 18, 2, 2]
    assert all(gcd(a, b) == 1 for i, a in enumerate(square_primes)
               for b in square_primes[i+1:])
    delta5 = F(2, 81)*F(4*(Q-1), 5*Q)
    delta7 = F(2, 729)*F(6*756, 7*757)
    rho = 1-(10*alpha+2*beta+1)/27+delta5+delta7+F(2, 729)
    numerator, denominator = data['density_bound']
    assert rho == F(numerator, denominator)
    assert rho > F(191, 200)
    print('PASS: four independent affine square characters, two cube',
          'characters, seven disjoint class counts, and exact CRT density',
          rho, '=', float(rho))


def main():
    data = json.loads(CERTIFICATE.read_text())
    moduli = {row['q']: row for row in data['moduli']}
    for row in moduli.values():
        check_lucas(row)
    print('PASS:', len(moduli), 'complete Lucas primality certificates,',
          'exact orders, and universal block-period hypotheses')

    covered = {}
    for row in data['exclusions']:
        d, e, q = row['d'], row['exponent'], row['q']
        r, P = moduli[q]['order_10'], moduli[q]['block_period']
        assert trial_prime(e) and distinct_factors(valuation(d)+2) == [e]
        assert (q-1) % e == 0 and pow(10, (q-1)//e, q) == 1
        V, S_r = closed_boundary(d, q, r)
        assert S_r == 0 and V == row['V_d_mod_q'] != 0
        assert matrix_boundary(d, q) == V
        character = pow(V, (q-1)//e, q)
        assert character == row['power_character'] != 1
        period = q*lcm(P, 3**(valuation(d)+1))
        assert period == row['digit_length_progression_modulus']
        # Check the large progressions with the independent closed formula.
        # It reduces exponents in j analytically: V_(tP+s)=t*V_P*10^S(s)+V_s.
        V_P, S_P = closed_boundary(P, q, r)
        assert S_P == 0
        for multiplier in (0, 1, 2, 19, 10**30+7):
            D = d+period*multiplier
            blocks, rem = divmod(D, P)
            V_rem, S_rem = closed_boundary(rem, q, r)
            actual = (blocks*V_P*pow(10, S_rem, q)+V_rem) % q
            assert actual == V and S_rem == 0
            assert valuation(D) == valuation(d)
        covered.setdefault(d, set()).add(e)
    for d in range(1, 28):
        assert adic_exclusions(d) <= covered.get(d, set()), d
    for d in (54, 243):
        assert adic_exclusions(d) <= covered[d]
    print('PASS:', len(data['exclusions']), 'character certificates by two',
          'independent algorithms; all digit lengths 1..27, 54, and 243')
    print('PASS: every certificate extends to its stated infinite arithmetic',
          'progression; large parameter checks through 10**30+7')

    for row in data['linear_families']:
        q, base, e = row['q'], row['d_unit_multiplier'], row['exponent']
        r, P = moduli[q]['order_10'], moduli[q]['block_period']
        assert P == r and base % r == 0
        C, _ = closed_boundary(r, q, r)
        assert C == matrix_boundary(r, q)
        coefficient = base//r*C % q
        assert coefficient == row['coefficient']
        assert pow(coefficient, (q-1)//e, q) == 1
        assert valuation(base)+2 == e and pow(10, (q-1)//e, q) == 1
        for u in range(1, 121):
            V, S_r = closed_boundary(base*u, q, r)
            assert S_r == 0 and V == coefficient*u % q
            if u % 3 and pow(u, (q-1)//e, q) not in (0, 1):
                assert valuation(base*u)+2 == e
                assert pow(V, (q-1)//e, q) not in (0, 1)
    print('PASS: linear fifth- and seventh-power families, independent period',
          'coefficients, and 240 sample units')

    density_audit(data, moduli)

    # Literal whole-block rotations check the character transfer itself.
    count = 0
    for m in (9, 99, 999):
        for q in (37, 757):
            if m == 9 and q == 757:  # 27 does not divide D(9)=9.
                continue
            W = next(iter(rotations_mod(m, q)))
            for R in rotations_mod(m, q):
                assert pow(R, (q-1)//2, q) == pow(W, (q-1)//2, q)
                count += 1
    print('PASS:', count, 'literal rotation characters at m=9,99,999')


if __name__ == '__main__':
    main()
