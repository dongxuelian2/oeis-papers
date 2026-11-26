#!/usr/bin/env python3
"""Independent finite checks for POWERFUL_SIEVE.md; standard library only."""
from fractions import Fraction
from math import factorial, lcm, prod
from random import Random


def local_counts():
    rng = Random(1292)
    cases = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 29, 43):
        for B in (2, 3, 10, 100):
            if B % p == 0:
                continue
            Q = p*p
            for _ in range(3):
                a, c = rng.randrange(Q), rng.randrange(Q)
                beta = rng.randrange(1, Q)
                while beta % p == 0:
                    beta = rng.randrange(1, Q)
                counts, power = [0]*(p-1), 1
                for n in range(Q*(p-1)):
                    value = (a*power + beta*n + c) % Q
                    if value % p == 0 and value:
                        counts[n % (p-1)] += 1
                    power = power*B % Q
                assert counts == [p-1]*(p-1), (p, B, counts)
                cases += 1
    print('PASS: local law in every phase;', cases, 'coefficient/base cases')


def joint_counts():
    cases = [
        ((7, 29), 10, [(21, 2, 8), (13, 3, 15)]),
        ((7, 43), 100, [(0, 1, 2), (35, 2, 1)]),
        ((3, 5, 7), 2, [(2, 2, 1), (3, 3, 2), (4, 4, 3)]),
    ]
    total_period = 0
    for ps, B, coefficients in cases:
        T = lcm(*(p*p*(p-1) for p in ps))
        powers, hit = [1]*len(ps), 0
        for n in range(T):
            yes = True
            for i, (p, (a, beta, c)) in enumerate(zip(ps, coefficients)):
                value = (a*powers[i]+beta*n+c) % (p*p)
                yes &= value % p == 0 and value != 0
                powers[i] = powers[i]*B % (p*p)
            hit += yes
        expected = Fraction(prod(p-1 for p in ps), prod(p*p for p in ps))*T
        assert expected.denominator == 1 and hit == expected, (ps, hit, expected)
        total_period += T
    print('PASS: simultaneous laws with overlapping periods;', total_period,
          'residues in three complete-period audits')


def digits(n, g):
    out = []
    while n:
        n, r = divmod(n, g)
        out.append(r)
    return out[::-1]


def rotation_formulas():
    count = rotations = 0
    for g in (2, 3, 5, 10, 12):
        W, D, blocks = [0], [0], []
        for m in range(1, 61):
            block = digits(m, g)
            blocks.append(block)
            W.append(W[-1]*g**len(block)+m)
            D.append(D[-1]+len(block))
        for m in range(2, 61):
            d = len(digits(m, g))
            B, L = g**d, g**(d-1)
            c = B-1
            A = c*c*W[L-1]+L*c+1
            seen = set()
            for k in range(m):
                literal = 0
                for block in blocks[k:m]+blocks[:k]:
                    for digit in block:
                        literal = literal*g+digit
                R = g**D[k]*W[m]-(g**D[m]-1)*W[k]
                assert R == literal
                seen.add(R)
                rotations += 1
                for p in (3, 7, 11, 13, 17, 19, 29, 43):
                    if (g*c) % p == 0:
                        continue
                    Q = p*p
                    u, inv_c = pow(g, D[k], Q), pow(c, -1, Q)
                    a = ((u*A*inv_c*inv_c-W[k]*pow(g, D[L-1], Q))
                         * pow(B, 1-L, Q)) % Q
                    beta = -u*inv_c % Q
                    gamma = (W[k]-u*B*inv_c*inv_c) % Q
                    assert beta % p
                    assert R % Q == (a*pow(B, m, Q)+beta*m+gamma) % Q
                    count += 1
            assert len(seen) == m, (g, m)
    print('PASS:', rotations, 'literal rotations and', count,
          'affine-exponential reductions in five bases')


def bonferroni():
    probabilities = [Fraction(p-1, p*p) for p in (3, 5, 7, 11, 13, 17)]
    sums = [Fraction(1)]
    for rho in probabilities:
        sums.append(Fraction(0))
        for j in range(len(sums)-1, 0, -1):
            sums[j] += rho*sums[j-1]
    product = prod(1-rho for rho in probabilities)
    lam = sum(probabilities)
    for K in (0, 2, 4, 6):
        truncated = sum((-1)**j*sums[j] for j in range(K+1))
        next_sum = sums[K+1] if K+1 < len(sums) else 0
        assert product <= truncated <= product+next_sum
        assert next_sum <= lam**(K+1)/factorial(K+1)
    print('PASS: exact rational Bonferroni remainder and factorial bound')


if __name__ == '__main__':
    local_counts()
    joint_counts()
    rotation_formulas()
    bonferroni()
