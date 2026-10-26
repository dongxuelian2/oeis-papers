#!/usr/bin/env python3
"""Independent exact checks for all four formerly unproved A048702 formulas."""
from fractions import Fraction
from pathlib import Path


def digits(n, base):
    out = []
    while n:
        n, r = divmod(n, base)
        out.append(r)
    return out[::-1]


def palindrome_quotient(n, base=2):
    if n == 0:
        return 0
    ds = digits(n, base)
    p = 0
    for d in ds + ds[::-1]:
        p = base * p + d
    assert p % (base + 1) == 0
    return p // (base + 1)


def valuation(n, base):
    t = 0
    while n % base == 0:
        n //= base
        t += 1
    return t


def floor_formula(n, base=2):
    if n == 0:
        return 0
    level = len(digits(n, base)) - 1
    return n * base**level - (base - 1) * sum(
        base**(level - j) * (n // base**j) for j in range(1, level + 1))


def maple_direct(n):
    if n == 0:
        return 0
    level = n.bit_length() - 1
    return 2 * (4**level - 1) // 3 + 1 + sum(
        2**(level - j) * ((n - 2**level + 2**j) // 2**(j + 1))
        for j in range(level + 1))


def main():
    table = Path(__file__).with_name('b048702-published.txt')
    rows = [tuple(map(int, line.split())) for line in table.read_text().splitlines()
            if line and not line.startswith('#')]
    assert [n for n, _ in rows] == list(range(1001))
    for n, a in rows:
        assert palindrome_quotient(n) == floor_formula(n) == maple_direct(n) == a
    print('PASS all 1001 published b-file terms (indices 0..1000)')
    for base in range(2, 13):
        weighted_sum = Fraction(0)
        previous = 0
        for n in range(1, 20001):
            level = len(digits(n, base)) - 1
            t = valuation(n, base)
            weighted_sum += Fraction(1, base**t)
            recurrence = base * previous + 1 if n == base**level else previous + base**(level-t)
            expected = palindrome_quotient(n, base)
            assert expected == floor_formula(n, base) == base**level * weighted_sum == recurrence
            if base == 2:
                assert expected == maple_direct(n)
            previous = expected
    print('PASS four binary formulas and general-base theorem for bases 2..12, n=1..20000')
    # A separate scan checks that prefix concatenation really enumerates all
    # even-length palindromes in increasing order, including length boundaries.
    palindromes = [0]
    for p in range(1, 2**18):
        s = bin(p)[2:]
        if len(s) % 2 == 0 and s == s[::-1]:
            palindromes.append(p // 3)
    assert palindromes == [palindrome_quotient(n) for n in range(len(palindromes))]
    print(f'PASS independent integer scan: {len(palindromes)} binary palindromes below 2^18')


if __name__ == '__main__':
    main()
