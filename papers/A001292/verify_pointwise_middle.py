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

    # Complete Lucas primality certificate for the second cyclic-modulus factor.
    N = delta//9
    factors = {2: 1, 5: 1, 11: 2, 23: 1, 4093: 1, 8779: 1,
               21649: 1, 513239: 1}
    assert math.prod(p**e for p, e in factors.items()) == N-1
    assert all(all(p % d for d in range(2, math.isqrt(p)+1)) for p in factors)
    assert pow(11, N-1, N) == 1
    assert all(math.gcd(pow(11, (N-1)//p, N)-1, N) == 1 for p in factors)
    assert N % 3 == 2 and R % 9 == 1
    cubic = subprocess.check_output(
        [args.binary, '--odd-candidate', '16', '1', '3', '1', '7'], text=True)
    assert 'ROOT_CLASS 2393321\n' in cubic and 'WINDOW_CANDIDATES=0' in cubic
    cube_roots = [27393321, 28393321, 29393321, 30393321]
    assert all(2*10**22 <= y**3 < 3*10**22 and y**3 % 10**6 == R % 10**6
               for y in cube_roots)
    assert [y**3//10**6 % 10 for y in cube_roots] == [6, 9, 2, 5]
    assert R//10**6 % 10 == 1
    print('PASS: complete Lucas certificate; all-precision local cubes; middle-digit cube exclusion.')

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

    odd_checks = 0
    for m in range(3, 15):
        blocks = list(map(str, range(1, m+1)))
        for k in range(m):
            word = ''.join(blocks[k:]+blocks[:k])
            E, value = len(word), int(word)
            for e in (3, 7, 9, 11):
                q = min(E, max(3, (E+e-1)//e+2))
                U = value % 10**q
                if not U or U % 2**q == 0 or U % 5**q == 0:
                    continue
                # Independent digit-by-digit lifting, without inverse exponents.
                roots, M = [0], 1
                for _ in range(q):
                    roots = [r+t*M for r in roots for t in range(10)
                             if pow(r+t*M, e, 10*M) == U % (10*M)]
                    M *= 10
                result = subprocess.check_output(
                    [args.binary, '--odd-candidate', str(m), str(k), str(e),
                     '1', str(q)], text=True)
                classes = list(map(int, re.findall(r'^ROOT_CLASS (\d+)$', result, re.M)))
                H = int(re.search(r'^H=(\d+)$', result, re.M)[1])
                lifted = sorted(r+j*H for r in classes for j in range(M//H))
                assert lifted == sorted(roots), (m, k, e, q)
                ys = list(map(int, re.findall(r'^CANDIDATE (\d+) POWER', result, re.M)))
                assert all(str(y**e)[0] == word[0] and len(str(y**e)) == E
                           and y**e % M == U for y in ys)
                if E <= 9:
                    brute = [y for y in range(1, 1001)
                             if int(word[0])*10**(E-1) <= y**e < (int(word[0])+1)*10**(E-1)
                             and y**e % M == U]
                    assert ys == brute, (m, k, e)
                odd_checks += 1
    print(f'PASS: {odd_checks} odd-exponent native/digit-lifting comparisons and small brute force.')

    result = subprocess.check_output([args.binary, '--late', '10000', '4'], text=True)
    counts = dict(re.findall(r'(\w+)=([\d.]+)', result))
    expected_counts = dict(odd=4442, unit=4861, local=688, branches=5504,
                           digit_gaps=3830, earlier=0, comparisons=1674,
                           head_matches=0, squares=0)
    assert all(int(counts[key]) == value for key, value in expected_counts.items())
    print('PASS: native 10,000-cut dispositions agree with the earlier full-prefix certificate.')
    print('No uniform nonexistence conclusion is inferred; fifth powers are outside the native root solver.')


if __name__ == '__main__':
    main()
