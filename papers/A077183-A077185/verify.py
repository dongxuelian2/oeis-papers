#!/usr/bin/env python3
"""Independent modular and minimum-term tests for OEIS A077183/A077185.

No third-party packages. The proof in main.tex is universal; these tests are finite.
"""
from math import isqrt

# Values 1..63 from https://oeis.org/A077183/b077183.txt (17 Oct 2026).
A077183_63 = (
    0, 2, 0, 2, 14, 15, 9, 5, 16, 4, 25, 21, 40, 67, 78, 66,
    25, 111, 161, 49, 30, 15, 27, 20, 63, 98, 102, 3, 99, 92,
    296, 71, 22, 367, 4, 48, 50, 91, 45, 241, 137, 258, 23, 28,
    212, 40, 96, 408, 456, 110, 16, 731, 403, 667, 90, 130, 111,
    458, 146, 18, 577, 276, 708,
)
# Values 1..12 from https://oeis.org/A077185 (17 Oct 2026).
A077185_12 = (
    0, 7, 0, 3, 128465555544332211, 11647163162383665717,
    58097313, 2859, 702235353091782071927, 149,
    814268458452231668262948810358418956591,
    5730248154490578733002999666333,
)


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * ((n-i*i)//i+1)
    return [i for i in range(n + 1) if sieve[i]]


def digit_length(n, b):
    d = 0
    while n:
        d += 1
        n //= b
    return d


def total_digits(m, b):
    total, start, d = 0, 1, 1
    while start <= m:
        finish = min(m, b*start-1)
        total += d*(finish-start+1)
        start *= b
        d += 1
    return total


def modular_block_append(R, start, count, d, b, p):
    """Prepend a huge interval start..start+count-1 in O(log count)."""
    t = pow(b, d, p)
    A = pow(b, total_digits(start-1, b), p)
    if t == 1:
        s0 = count % p
        s1 = count*(count-1)//2 % p
    else:
        tn = pow(t, count, p)
        s0 = (tn-1)*pow(t-1, -1, p) % p
        s1 = (t-count*tn+(count-1)*tn*t)*pow(1-t, -2, p) % p
    return (R+A*(start*s0+s1)) % p


def reverse_prefix_mod(m, b, p):
    R, start, d = 0, 1, 1
    while start <= m:
        finish = min(m, b*start-1)
        R = modular_block_append(R, start, finish-start+1, d, b, p)
        start *= b
        d += 1
    return R


def order_mod(b, p):
    r, x = 1, b % p
    while x != 1:
        x = x*b % p
        r += 1
    assert (p-1) % r == 0
    return r


def witness(b, p):
    """Witness for every prime p not dividing b."""
    assert b >= 2 and p > 1 and b % p
    if (b-1) % p == 0:
        return 2*p, None
    r = order_mod(b, p)
    d = 2*r+1
    L = b**(d-1)
    m0 = L-1
    R0 = reverse_prefix_mod(m0, b, p)
    A = pow(b, total_digits(m0, b), p)
    delta = A*r*pow(b-1, -1, p) % p
    assert delta and r < p
    j = (-R0*pow(delta, -1, p)) % p
    k = m0+j*r
    assert k < b**d and k <= m0+(p-1)*r
    assert reverse_prefix_mod(k, b, p) == 0, (b, p, r, j)
    return k, (r, d, j, delta)


def test_naive_brute():
    ps = primes_upto(400)
    assert len(A077183_63) == 63
    for n, answer in enumerate(A077183_63, start=1):
        p = ps[n-1]
        if p in (2, 5):
            assert answer == 0
            continue
        residue, pwr = 0, 1
        for k in range(1, answer+1):
            residue = (residue + k*pwr) % p
            pwr = pwr*pow(10, len(str(k)), p) % p
            if residue == 0:
                assert k == answer, (n, p, k, answer)
                break
        else:
            raise AssertionError((n, p, answer))
    print('PASS: first 63 A077183 minimal endpoints independently reproduced')


def test_quotients():
    ps = primes_upto(100)
    for n, expected in enumerate(A077185_12, start=1):
        p, k = ps[n-1], A077183_63[n-1]
        if k == 0:
            assert expected == 0
        else:
            actual = int(''.join(str(j) for j in range(k, 0, -1)))
            assert actual % p == 0
            assert actual//p == expected, (n, actual//p, expected)
    print('PASS: first 12 A077185 quotient terms independently reproduced')


def test_summation_and_witnesses():
    tests = 0
    for b in (2, 3, 4, 5, 7, 10, 12, 16):
        for p in primes_upto(101):
            if b % p == 0:
                for k in range(1, 40):
                    assert reverse_prefix_mod(k, b, p) == 1
                continue
            k, detail = witness(b, p)
            assert reverse_prefix_mod(k, b, p) == 0
            if detail:
                r,d,j,delta = detail
                L = b**(d-1)
                m0 = L-1
                R0 = reverse_prefix_mod(m0, b, p)
                assert (reverse_prefix_mod(m0+r, b, p)-R0) % p == delta
                for m in range(5):
                    assert reverse_prefix_mod(m0+m*r, b, p) == (R0+m*delta) % p
            tests += 1
    print(f'PASS: {tests} constructive witnesses in eight bases for primes <=101')


def test_literal_and_recursion():
    for b in (2, 3, 7, 10, 16):
        for p in (3, 7, 11, 13, 17, 37):
            R, power = 0, 1
            digits = '0123456789ABCDEF'
            word = ''
            for k in range(1, 50):
                x, buf = k, ''
                while x:
                    buf = digits[x % b] + buf
                    x //= b
                word = buf + word
                R = (R + k*power) % p
                power = power*pow(b, len(buf), p) % p
                assert len(word) == total_digits(k,b)
                assert int(word,b) % p == R == reverse_prefix_mod(k,b,p)
    print('PASS: exact literal digit strings agree with both modular evaluators')


if __name__ == '__main__':
    test_naive_brute()
    test_quotients()
    test_literal_and_recursion()
    test_summation_and_witnesses()
