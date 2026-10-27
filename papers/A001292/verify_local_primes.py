#!/usr/bin/env python3
"""Exact audits of the additional boundary primes in main.tex.

The unbounded assertions follow from the manuscript's analytic argument.
This checker compares closed blocks, independent matrix blocks, and literal
concatenation; --extended also reaches the first positive 333667-adic valuation
by direct iteration over complete digit blocks.
"""
import argparse
from fractions import Fraction
from math import comb, gcd, isqrt

from verify_a001292 import append_block, digits_total


PAIRS = ((37, 3), (333667, 9))


def valuation(n, p):
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def local_constants(p, s):
    """Partial sums of the complete-block residues, including one full cycle."""
    out = [0]
    for j in range(1, s+1):
        B = pow(10, j, p)
        block = (9*pow(200, -1, p) if j == s else
                 -9*pow(10, j-1, p)*pow(B-1, -1, p))
        out.append((out[-1]+block) % p)
    return out


def boundary_residue(d, p, s):
    parts = local_constants(p, s)
    n, r = divmod(d, s)
    return (parts[-1]*n+parts[r]) % p


def length_mod(d, mod):
    # Divide the integer numerator before reducing modulo mod. This also
    # works when mod is divisible by 3, so 9 cannot be inverted modulo mod.
    return (((9*d-1)*pow(10, d, 9*mod)+1) % (9*mod))//9


def matrix_word(m, mod):
    word, start, width = 0, 1, 1
    while start <= m:
        count = min(10*start-1, m)-start+1
        word = append_block(word, start, count, width, mod)
        start *= 10
        width += 1
    return word


def prime_and_density_audit():
    alpha = beta = Fraction(1)
    for p, s in PAIRS:
        assert all(p % k for k in range(2, isqrt(p)+1))
        assert pow(10, s, p) == 1
        assert all(pow(10, k, p) != 1 for k in range(1, s))
        assert valuation(10**s-1, p) == 1
        parts = local_constants(p, s)
        assert parts[-1] == 9*(11-10*s)*pow(200, -1, p) % p
        assert parts[-1] != 0
        assert (p-1) % (6*s) == 0
        # Count images of the power maps independently, retaining zero.
        squares = len({x*x % p for x in range(p)})
        cubes = len({x*x*x % p for x in range(p)})
        assert squares == (p+1)//2
        assert cubes == (p+2)//3
        alpha *= Fraction(squares, p)
        beta *= Fraction(cubes, p)
        # On every fixed class mod 27, the affine residue has nonzero slope.
        for r in range(27):
            slope = (boundary_residue(r+27, p, s)-boundary_residue(r, p, s)) % p
            assert slope == (27//s)*parts[-1] % p and slope
        print(f'PASS: p={p}, order={s}, C={parts[-1]}, '
              f'{squares} square residues, {cubes} cube residues (including zero)')
    assert gcd(PAIRS[0][0], PAIRS[1][0]) == 1
    assert alpha == Fraction(3169846, 12345679)
    assert beta == Fraction(1445899, 12345679)
    excluded = 1-(10*alpha+2*beta+1)/27
    assert excluded == Fraction(286397396, 333333333)
    for p, s, d, e in [(333667, 9, 2, 2), (37, 3, 12, 3),
                        (37, 3, 15, 3), (37, 3, 18, 2)]:
        assert pow(boundary_residue(d, p, s), (p-1)//e, p) != 1
    print('PASS: exact CRT density bound', excluded, '=', float(excluded))


def fast_block_audit(p, s, max_d, precision):
    """Iterate exact geometric block sums; no analytic interpolation is used."""
    mod = p**precision
    word = 0
    C = local_constants(p, s)[-1]
    positive = 0
    for d in range(1, max_d+1):
        e = 1+valuation(d//s, p) if d % s == 0 else 0
        lifted = p**(precision+2*e)
        phi = lifted//p*(p-1)
        start = pow(10, d-1, lifted)
        B = pow(10, d, lifted)
        c = (B-1) % lifted
        shift = pow(B, 9*pow(10, d-1, phi) % phi, lifted)
        numerator = ((start*c+1)*shift-(B*c+1)) % lifted
        assert numerator % p**(2*e) == 0
        c_unit = (pow(10, d, p**(precision+e))-1)//p**e
        block = numerator//p**(2*e)*pow(c_unit*c_unit, -1, mod) % mod
        word = (word*(shift % mod)+block) % mod
        assert word % p == boundary_residue(d, p, s), (p, d)
        if d <= 60:
            assert block == append_block(0, 10**(d-1), 9*10**(d-1), d, mod)
        if d % s == 0:
            a = valuation(d, p)
            assert a < precision
            assert word % p**a == 0 and word % p**(a+1) != 0, (p, d, a)
            assert word//p**a % p == C*(d//(s*p**a)) % p, (p, d)
            positive += a > 0
            phi_mod = mod//p*(p-1)
            rotation_shift = (pow(10, length_mod(d, phi_mod), mod)-1) % mod
            assert rotation_shift % p**(a+1) == 0, (p, d)
        if max_d > 1000000 and d % 500000 == 0:
            print(f'progress: p={p}, d={d}', flush=True)
    print(f'PASS: p={p}, direct complete blocks d=1..{max_d}; '
          f'{positive} positive valuation cases; independent matrices d=1..60',
          flush=True)


def interpolation_audit():
    """Check the group interpolant by matrix samples and its Newton sums.

    The coefficient bound in main.tex makes f a degree <= 6 polynomial modulo
    p**7. The huge-parameter checks below use that proved truncation, and are
    recorded separately from the direct block-iteration audits.
    """
    for p, s in PAIRS:
        precision = 7
        mod = p**precision
        samples = []
        for x in range(8):
            total = 0
            for r in range(1, s+1):
                j = s*x+r
                U = append_block(0, 10**(j-1), 9*10**(j-1), j, mod)
                S = ((9*j-1)*10**j+1)//9
                total += U*pow(10, -S, mod)
            samples.append(total % mod)
        first = []
        row = samples
        for n in range(8):
            first.append(row[0])
            assert row[0] % p**min(n, precision) == 0, (p, n)
            row = [(b-a) % mod for a, b in zip(row, row[1:])]
        assert first[0] % p == local_constants(p, s)[-1]
        for N in (1, 2, 3, 7):
            total = sum(comb(N, j+1)*first[j] for j in range(7) if j < N) % mod
            d = s*N
            S = ((9*d-1)*10**d+1)//9
            word = total*pow(10, S, mod) % mod
            assert word == matrix_word(10**d-1, mod), (p, N)
        C = local_constants(p, s)[-1]
        for a in range(6):
            for u in (1, 2, 4, 7, 13):
                N = p**a*u
                total = sum(comb(N, j+1)*first[j] for j in range(7) if j < N) % mod
                d = s*N
                S_mod = length_mod(d, mod//p*(p-1))
                word = total*pow(10, S_mod, mod) % mod
                assert word % p**a == 0
                assert word//p**a % p == C*u % p, (p, a, u)
        print(f'PASS: p={p}, 8 matrix group samples, finite differences, '
              '4 full matrix words, 30 Newton sums through valuation 5')
    # Audit the coefficient/averaging inequality beyond the sampled degrees.
    for p, _ in PAIRS:
        factorial_v = 0
        for n in range(1, 10001):
            factorial_v += valuation(n, p)
            lower = n-factorial_v-(n+1)//(p-1)
            log_floor, power = 0, p
            while power <= n+1:
                log_floor += 1
                power *= p
            assert lower >= 1+log_floor, (p, n)
    print('PASS: 20000 coefficient/averaging bounds')


def rotation_audit():
    # Rolling literal concatenation, with no geometric sums or interpolation.
    mod = 37**3*333667**2
    cuts = {0, 1, 2, 9, 10, 41, 99, 100, 998, 999, 1000, 999998}
    saved = {0: (0, 0)}
    prefixes = [(0, 0)]
    word = length = 0
    width, B, upper = 1, 10, 9
    count = 0
    for m in range(1, 1000000):
        if m > upper:
            width += 1
            B *= 10
            upper = B-1
        word = (word*B+m) % mod
        length += width
        if m in cuts:
            saved[m] = word, length
        if m <= 999:
            prefixes.append((word, length))
        if m != upper:
            continue
        selected = range(m) if m <= 999 else sorted(k for k in cuts if k < m)
        for k in selected:
            pref, cut_length = prefixes[k] if m <= 999 else saved[k]
            R = (pow(10, cut_length, mod)*word-(pow(10, length, mod)-1)*pref) % mod
            for p, s in PAIRS:
                expected = pow(10, cut_length, p)*boundary_residue(width, p, s) % p
                assert R % p == expected, (m, k, p)
                if width % s == 0:
                    assert R % p != 0
            count += 1
    print(f'PASS: literal prefixes through m=999999; {count} rotation residues')
    # Independent large-boundary words verify positive valuations and units.
    p, s, mod = 37, 3, 37**4
    count = 0
    for d in (111, 444):
        m = 10**d-1
        word = matrix_word(m, mod)
        length = digits_total(m)
        for k in (0, 1, 9, 10, 41, 99, 100, 998, 999, 1000, m-1):
            pref = matrix_word(k, mod)
            cut_length = digits_total(k) if k else 0
            R = (pow(10, cut_length, mod)*word-(pow(10, length, mod)-1)*pref) % mod
            a = valuation(d, p)
            assert R % p**a == 0 and R % p**(a+1) != 0
            unit = pow(10, cut_length, p)*33*(d//(s*p**a)) % p
            assert R//p**a % p == unit, (d, k)
            count += 1
    print(f'PASS: {count} matrix rotation checks at d=111,444, '
          'including cuts just before the final integer')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extended', action='store_true')
    args = parser.parse_args()
    prime_and_density_audit()
    fast_block_audit(37, 3, 200000, 7)
    fast_block_audit(333667, 9, 3003003 if args.extended else 10000, 4)
    interpolation_audit()
    rotation_audit()


if __name__ == '__main__':
    main()
