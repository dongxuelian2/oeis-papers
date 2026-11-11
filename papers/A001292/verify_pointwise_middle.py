#!/usr/bin/env python3
"""Exact cyclic-modulus counterexample and independent native digit audit.

Run with --binary pointing to pointwise_rotation compiled from the C++ source.
Uses the earlier pure-Python root implementation as an independent comparator.
"""
import argparse
import math
import re
import subprocess
from verify_late_prefix_candidates import compressed_roots, local_root_audit


def native(binary, m, k, h, q):
    return subprocess.check_output(
        [binary, '--candidate', str(m), str(k), str(h), str(q)], text=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--binary', required=True)
    args = ap.parse_args()
    word = ''.join(map(str, range(2, 17))) + '1'
    R = int(word)
    W = int(''.join(map(str, range(1, 17))))
    delta = 10**len(word)-1
    r = 24515341518503348803133
    assert R == 23456789101112131415161 == 10*W-delta
    assert (r*r-R) % delta == 0
    assert math.gcd(2*r, delta) == math.gcd(R, delta) == 1
    assert R % 8 == R % 5 == 1
    print('PASS: actual rotation; nonsingular full cyclic root; Q_2 and Q_5 units.')

    lo = math.isqrt(2*10**22-1)+1
    hi = math.isqrt(3*10**22-1)
    assert (lo, hi) == (141421356238, 173205080756)
    expected = [55164164619, 104480570869, 395519429131, 444835835381,
                555164164619, 604480570869, 895519429131, 944835835381]
    H, roots, _ = compressed_roots(R % 10**12, 12)
    assert H == 10**12 and roots == expected
    assert all(not lo <= a <= hi for a in roots)
    assert hi < H
    output = native(args.binary, 16, 1, 1, 12)
    assert list(map(int, re.findall(r'^ROOT_CLASS (\d+)$', output, re.M))) == expected
    assert 'WINDOW_CANDIDATES=0' in output
    examples = [144835835381, 145519429131, 154480570869, 155164164619]
    assert all(lo <= a <= hi and a*a % 10**11 == R % 10**11 for a in examples)
    assert [(a*a//10**11) % 10 for a in examples] == [5, 6, 0, 9]
    assert R//10**11 % 10 == 1
    print('PASS: all eight 12-digit roots; empty real interval; four 11-digit completions.')

    comparisons = 0
    for m in range(3, 41):
        blocks = list(map(str, range(1, m+1)))
        for k in sorted({0, 1, m//2, m-1}):
            text = ''.join(blocks[k:]+blocks[:k])
            value, E = int(text), len(text)
            h = len(blocks[k])
            q = min(E, max(3, (E+1)//2+2))
            suffix = value % 10**q
            if not suffix:
                continue
            v2 = (suffix & -suffix).bit_length()-1
            v5, t = 0, suffix
            while t % 5 == 0:
                v5, t = v5+1, t//5
            if max(v2, v5) >= q:
                continue
            H, reference, _ = compressed_roots(suffix, q)
            result = native(args.binary, m, k, h, q)
            actual = list(map(int, re.findall(r'^ROOT_CLASS (\d+)$', result, re.M)))
            assert actual == reference, (m, k, q)
            P = int(text[:h])
            low = math.isqrt(P*10**(E-h)-1)+1
            high = math.isqrt((P+1)*10**(E-h)-1)
            expected_y = sorted(a+j*H for a in reference
                                for j in range(max(0, (low-a+H-1)//H), (high-a)//H+1))
            actual_y = sorted(map(int, re.findall(r'^CANDIDATE (\d+) SQUARE', result, re.M)))
            assert actual_y == expected_y
            if E <= 9:
                brute = [y for y in range(low, high+1) if y*y % 10**q == suffix]
                assert actual_y == brute
            comparisons += 1
    assert local_root_audit() == 871
    print(f'PASS: {comparisons} native/reference candidate comparisons, small brute force, 871 unit-root cases.')

    result = subprocess.check_output([args.binary, '--late', '10000', '4'], text=True)
    counts = dict(re.findall(r'(\w+)=([\d.]+)', result))
    expected_counts = dict(odd=4442, unit=4861, local=688, branches=5504,
                           digit_gaps=3830, earlier=0, comparisons=1674,
                           head_matches=0, squares=0)
    assert all(int(counts[key]) == value for key, value in expected_counts.items())
    print('PASS: native 10,000-cut dispositions agree with the earlier full-prefix certificate.')
    print('No universal nonexistence or odd-prime-power conclusion is inferred.')


if __name__ == '__main__':
    main()
