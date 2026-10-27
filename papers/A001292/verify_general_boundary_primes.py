#!/usr/bin/env python3
"""Audit the general prime-adic boundary theorem and local power equivalences.

Direct block iteration and matrix powering are independent algorithms. The
large-parameter Newton sums use the coefficient bound proved in main.tex;
they are reported separately from the direct positive-valuation checks.
"""
import json
from math import comb, gcd

from verify_a001292 import append_block, mmul, direct_prefix_mod, digit_len
from verify_boundary_characters import CERTIFICATE, check_lucas, closed_boundary, trial_prime
from verify_boundary_valuations import valuation
from verify_local_primes import length_mod


def geometric_prefixes(q, r, max_d, precision):
    """Complete blocks via lifted arithmetic-geometric sums, before division."""
    mod = q**precision
    lam = valuation(10**r-1, q)
    word = 0
    for d in range(1, max_d+1):
        e = lam+valuation(d//r, q) if d % r == 0 else 0
        lifted = q**(precision+2*e)
        phi = (lifted//q)*(q-1)
        start = pow(10, d-1, lifted)
        B = pow(10, d, lifted)
        shift = pow(B, 9*pow(10, d-1, phi) % phi, lifted)
        numerator = ((start*(B-1)+1)*shift-(B*(B-1)+1)) % lifted
        assert numerator % q**(2*e) == 0
        unit = (pow(10, d, q**(precision+e))-1)//q**e
        block = numerator//q**(2*e)*pow(unit*unit, -1, mod) % mod
        word = (word*(shift % mod)+block) % mod
        yield d, word


def matrix_power(T, n, mod):
    out = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    while n:
        if n & 1:
            out = mmul(T, out, mod)
        T = mmul(T, T, mod)
        n >>= 1
    return out


def matrix_prefixes(q, max_d, precision):
    """Exact matrix words with a proved exponent period, reducing large counts.

    Modulo q, T**(q-1) is unipotent of index at most 3, hence
    T**((q-1)*q) is the identity. Lifting gives the period
    (q-1)*q**precision modulo q**precision (q>3).
    """
    mod = q**precision
    period = (q-1)*mod
    word, start, start_period = 0, 1, 1
    for d in range(1, max_d+1):
        word = append_block(word, start, 9*start_period % period, d, mod)
        yield d, word
        start = 10*start % mod
        start_period = 10*start_period % period


def interpolation_audit(row, precision=9):
    q, r, P = row['q'], row['order_10'], row['block_period']
    assert q > 2*precision+1  # The coefficient bound then permits this truncation.
    C = row['boundary_cycle_value']
    assert gcd(q, P) == 1 and C == closed_boundary(P, q, r)[0] != 0
    mod, phi = q**precision, (q-1)*q**(precision-1)
    samples, previous, matrix_targets = [], 0, {}
    for d, word in geometric_prefixes(q, r, (precision+1)*P, precision):
        if d in (P, 2*P):
            matrix_targets[d] = word
        if d % P == 0:
            normal = word*pow(10, -length_mod(d, phi), mod) % mod
            samples.append((normal-previous) % mod)
            previous = normal
    for d, word in matrix_prefixes(q, 2*P, precision):
        if d in matrix_targets:
            assert word == matrix_targets[d], (q, d)
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for width in (1, r, r+1, P, 2*P+1):
        T = [[pow(10, width, mod), 1, 1], [0, 1, 1], [0, 0, 1]]
        assert matrix_power(T, (q-1)*mod, mod) == identity

    # The proved coefficient bound makes f a degree <=8 polynomial mod q**9.
    assert len(samples) == precision+1
    first, values = [], samples
    for n in range(precision+1):
        first.append(values[0])
        assert values[0] % q**min(n, precision) == 0, (q, n)
        values = [(b-a) % mod for a, b in zip(values, values[1:])]
    assert first[0] % q == C

    def value(N):
        total = sum(comb(N, j+1)*first[j]
                    for j in range(precision) if j < N) % mod
        d = P*N
        return total*pow(10, length_mod(d, phi), mod) % mod

    for a in range(precision):
        for unit in (1, 2, 4, 7, 13):
            N = q**a*unit
            word = value(N)
            assert word % q**a == 0 and word % q**(a+1) != 0
            assert word//q**a % q == C*unit % q
    print(f'PASS: q={q}, P={P}, C={C}; 10 exact group samples, '
          '2 independent matrix words, 45 Newton sums through valuation 8',
          flush=True)
    return value


def direct_positive_audit(max_d=327024):
    q, r, P, precision, C = 757, 27, 27, 3, 538
    mod = q**precision
    positive, last = 0, None
    for d, word in geometric_prefixes(q, r, max_d, precision):
        if d % P:
            continue
        a = valuation(d, q)
        assert word % q**a == 0 and word % q**(a+1) != 0
        assert word//q**a % q == C*(d//(P*q**a)) % q
        positive += a > 0
        if d == max_d:
            last = word
    assert last is not None and positive == 16
    phi = (q-1)*q**(precision-1)
    S = length_mod(max_d, phi)
    shift = (pow(10, S, mod)-1) % mod
    assert shift % q**2 == 0
    cuts = [(0, 0)]
    for k in (1, 9, 41):
        cuts.append((direct_prefix_mod(k, mod), sum(digit_len(i) for i in range(1, k+1))))
    B = pow(10, max_d, mod)
    # The exact final recurrence gives W_(m-1), without constructing m.
    cuts.append(((last-(B-1))*pow(B, -1, mod) % mod, (S-max_d) % phi))
    for prefix, cut_length in cuts:
        rotation = (pow(10, cut_length, mod)*last-shift*prefix) % mod
        assert rotation % q == 0 and rotation % (q*q) != 0
        expected = pow(10, cut_length, q)*C*(max_d//(P*q)) % q
        assert rotation//q % q == expected
    assert valuation(max_d) == 3 and valuation(max_d, q) == 1
    Q = 440334654777631
    assert pow(max_d//27, (Q-1)//5, Q) == 1
    print(f'PASS: q=757, direct complete blocks d=1..{max_d}, '
          f'{positive} positive valuations, and 5 rotation units at d={max_d}',
          flush=True)


def outside_table_audit():
    # Orders 7 and 13 exercise phases not present in the original 3-power
    # periods. These are checks of the universal theorem, not new hypotheses.
    for q, r, P, C in ((53, 13, 78, 16), (79, 13, 78, 30),
                       (239, 7, 42, 8)):
        assert trial_prime(q) and gcd(q, P) == 1
        assert pow(10, r, q) == 1
        assert all(pow(10, j, q) != 1 for j in range(1, r))
        assert P % r == 0 and pow(10, P, 9*r) == 1
        assert closed_boundary(P, q, r)[0] == C
        word = 0
        for d, word in geometric_prefixes(q, r, P*q, 3):
            pass
        assert word % q == 0 and word % (q*q) != 0
        assert word//q % q == C
    print('PASS: three further primes 53,79,239; orders 13,13,7;',
          'first positive valuations checked by direct blocks', flush=True)


def main():
    data = json.loads(CERTIFICATE.read_text())
    moduli = {row['q']: row for row in data['moduli']}
    functions = {}
    for row in moduli.values():
        check_lucas(row)
        functions[row['q']] = interpolation_audit(row)
    # Test both sides of each local equivalence, including positive valuations
    # divisible and not divisible by the prospective exponent.
    total = 0
    for row in data['linear_families']:
        q, e = row['q'], row['exponent']
        ratio = row['d_unit_multiplier']//moduli[q]['block_period']
        for a in (0, 1, e, e+1):
            for t in (1, 2, 4, 7, pow(2, e, q)):
                u = q**a*t
                word = functions[q](ratio*u)
                assert word % q**a == 0 and word % q**(a+1) != 0
                left = a % e == 0 and pow(word//q**a % q, (q-1)//e, q) == 1
                right = a % e == 0 and pow(t, (q-1)//e, q) == 1
                assert left == right
                total += 1
    print('PASS:', total, 'local power-equivalence cases, including valuation',
          'multiples 5 and 7 and both residue types', flush=True)
    outside_table_audit()
    direct_positive_audit()


if __name__ == '__main__':
    main()
