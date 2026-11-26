#!/usr/bin/env python3
"""Independent audit. No imports from the proposed verifier or its dependencies."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT

def character(x, p):
    return 0 if x % p == 0 else 1 if pow(x, (p - 1) // 2, p) == 1 else -1

def f37(m, d):
    if d % 3 == 0:
        return (m * (m + 1) // 2 + 11 * d) % 37
    if d % 3 == 1:
        return (4 * m + 11 * (d - 1)) % 37
    return (34 * m + 26 + 11 * (d - 2)) % 37

def f13(m, d):
    phase = d % 6
    alpha, base = {1: (10, 0), 3: (7, 5), 5: (4, 11)}[phase]
    return (alpha * m + base + 5 * ((d - phase) // 6)) % 13

def append_closed(w, u, n, d):
    b = pow(10, d, 37)
    if b == 1:
        return (w + n * u + n * (n - 1) // 2) % 37
    inverse = pow(b - 1, -1, 37)
    bn = pow(b, n, 37)
    return (bn * w + u * (bn - 1) * inverse
            + (bn - n * b + n - 1) * inverse * inverse) % 37

def prefix_closed(m):
    w, u, d = 0, 1, 1
    while u <= m:
        w = append_closed(w, u, min(m + 1, 10 * u) - u, d)
        u *= 10
        d += 1
    return w

def exact_period(seq):
    n = len(seq)
    return next(k for k in range(1, n + 1)
                if n % k == 0 and all(seq[j] == seq[(j + k) % n] for j in range(n)))

def main():
    supplied = json.loads((SOURCE / 'all-width-thirty-seven-certificate.json').read_text())
    by_phase = {row['width_mod111']: row for row in supplied['width_phases']}
    for d in range(1, 112):
        classes = [m for m in range(999)
                   if m % 27 == 18 and character(f37(m, d), 37) == -1]
        assert classes == by_phase[d % 111]['classes_mod999']

    # A scalar geometric-sum implementation, independent of matrix exponentiation.
    prefix_checks = 0
    for d in range(2, 401):
        lower, upper = 10 ** (d - 1), 10 ** d - 1
        first, last = lower + (-lower) % 3, upper - upper % 3
        middle = (lower + upper) // 2
        middle -= middle % 3
        for m in {first, min(first + 3, last), middle, last}:
            assert prefix_closed(m) == f37(m, d)
            prefix_checks += 1

    # Encode all CRT triples (parity, m mod 13, m mod 37); m mod 27 is fixed.
    full_class_sets, counts = [], []
    for d in range(1, 2887, 2):
        neg37 = {m for m in range(37) if character(f37(m, d), 37) == -1}
        neg13 = {m for m in range(13) if character(f13(m, d), 13) == -1}
        bits = 0
        for parity in range(2):
            for r13 in range(13):
                for r37 in range(37):
                    if r37 in neg37 or (parity == 0 and r13 in neg13):
                        bits |= 1 << (parity * 481 + r13 * 37 + r37)
        assert bits.bit_count() == 20 * len(neg37) + 222
        full_class_sets.append(bits)
        counts.append(bits.bit_count())
    class_period, count_period = 2 * exact_period(full_class_sets), 2 * exact_period(counts)
    assert class_period == 2886 and count_period == 222

    # Literal integer rotations, independently of the modular rotation identity.
    literal_checks = 0
    for m in [45, 72, 1017, 1098, 1125]:
        pieces = [str(j) for j in range(1, m + 1)]
        digits = ''.join(pieces)
        cut = 0
        for piece in pieces:
            rotation = int(digits[cut:] + digits[:cut])
            assert rotation % 27 == 9
            assert character(rotation, 37) == -1
            cut += len(piece)
            literal_checks += 1
    assert literal_checks == supplied['individual_modular_rotation_checks']
    print('Independent scalar prefix checks:', prefix_checks, '(widths 2 through 400)')
    print('Full odd-width CRT class phases:', len(full_class_sets))
    print('Exact odd-width count period:', count_period)
    print('Exact odd-width class-set period:', class_period)
    print('Literal integer rotation checks:', literal_checks)
    print('All checks: PASS')

if __name__ == '__main__':
    main()
