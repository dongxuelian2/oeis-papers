#!/usr/bin/env python3
"""Exact counting and selection for squared digit sums modulo any base."""
from functools import lru_cache


def squared_sum(n, base):
    total = 0
    while n:
        n, d = divmod(n, base)
        total += d * d
    return total


@lru_cache(None)
def blocks(base, k):
    if k == 0:
        return (1,) + (0,) * (base - 1)
    previous = blocks(base, k - 1)
    return tuple(sum(previous[(r - d * d) % base] for d in range(base))
                 for r in range(base))


def count(n, base=3, residue=0):
    """Number of 0<=x<n in the specified squared-digit residue class."""
    if base < 2 or n < 0:
        raise ValueError('base >= 2 and n >= 0 required')
    ds = []
    while n:
        n, d = divmod(n, base)
        ds.append(d)
    total = prefix = 0
    for k in range(len(ds) - 1, -1, -1):
        c = ds[k]
        total += sum(blocks(base, k)[(residue - prefix - d * d) % base]
                     for d in range(c))
        prefix += c * c
    return total


def term(j, base=3, residue=0):
    if j < 1 or base < 2:
        raise ValueError('j >= 1 and base >= 2 required')
    residue %= base
    k, high = 0, 1
    while blocks(base, k)[residue] < j:
        k += 1
        high *= base
    low = 0
    while low + 1 < high:
        mid = (low + high) // 2
        if count(mid, base, residue) >= j:
            high = mid
        else:
            low = mid
    return high - 1


PUBLISHED = [0,13,14,16,17,22,23,25,26,31,32,34,35,37,38,39,
             42,46,47,48,51,58,59,61,62,64,65,66,69,73,74,75,
             78,85,86,88,89,91,92,93,96,100,101,102,105,109,
             110,111,114,117,126,136,137,138,141,144,153,166,
             167,169,170,172,173]


def main():
    for base in range(2, 17):
        direct = [0] * base
        positions = [[] for _ in range(base)]
        for n in range(5001):
            assert [count(n, base, r) for r in range(base)] == direct, (base, n)
            r = squared_sum(n, base) % base
            direct[r] += 1
            positions[r].append(n)
        for r in range(base):
            for j, expected in enumerate(positions[r][:50], 1):
                assert term(j, base, r) == expected, (base, r, j)
        # Check complete-block vectors independently by direct digit extraction.
        high = 1
        for k in range(6):
            if high > 100_000:
                break
            actual = [0] * base
            for n in range(high):
                actual[squared_sum(n, base) % base] += 1
            assert blocks(base, k) == tuple(actual), (base, k)
            high *= base
    print('PASS all prefix counts N=0..5000, every residue, bases 2..16')
    print('PASS complete digit-block vectors and first 50 positions per residue/base')
    assert [term(j) for j in range(1, 64)] == PUBLISHED
    print('PASS all 63 official displayed A079495 terms')
    for k in range(101):
        expected = (3**(k - 1) if k % 2 else
                    (3**k + 2 * (-3)**(k // 2)) // 3)
        assert blocks(3, k)[0] == expected
        assert sum(blocks(3, k)) == 3**k
    print('PASS exact ternary zero-residue block formula through length 100')


if __name__ == '__main__':
    main()
