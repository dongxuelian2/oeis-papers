#!/usr/bin/env python3
"""Exact official-data and independent implementation checks for A340138."""
from pathlib import Path


def digits(n, base):
    if n == 0:
        return [0]
    out = []
    while n:
        n, d = divmod(n, base)
        out.append(d)
    return out


def sequence(length, base=10):
    if base < 2 or length < 1:
        raise ValueError('base >= 2 and length >= 1 required')
    out = [0]
    used = {0}
    # Each pointer skips only used values or values permanently ineligible
    # for its root, so no smaller eligible candidate can be lost.
    pointers = [1] * base
    while len(out) < length:
        previous = out[-1]
        root = 0 if previous == 0 else 1 + (previous - 1) % (base - 1)
        k = pointers[root]
        while k in used or root not in digits(k, base):
            k += 1
        pointers[root] = k + 1
        out.append(k)
        used.add(k)
    return out


def direct(length, base):
    out = [0]
    while len(out) < length:
        root = out[-1]
        while root >= base:
            root = sum(digits(root, base))
        k = 1
        while k in out or root not in digits(k, base):
            k += 1
        out.append(k)
    return out


def main():
    path = (Path(__file__).resolve().parents[2] /
            'research/parallel-20261026/greedy/b340138-published.txt')
    official = []
    for line in path.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith('#'):
            n, value = map(int, line.split())
            assert n == len(official) + 1
            official.append(value)
    assert len(official) == 10_000
    assert sequence(len(official)) == official
    print('PASS all 10000 official b-file terms under immediate-predecessor indexing')
    for base in range(2, 17):
        assert sequence(200, base) == direct(200, base)
        assert sequence(2, base) == [0, base]
        for r in range(1, base):
            for s in range(1, base):
                d = (s - r) % (base - 1)
                assert 0 <= d <= base - 2
                for length in range(1, 21):
                    n = r * base**(length + 1) + d
                    ds = digits(n, base)
                    assert r in ds
                    root = n
                    while root >= base:
                        root = sum(digits(root, base))
                    assert root == s, (base, r, s, length)
    print('PASS independent direct scans: first 200 terms in bases 2..16')
    print('PASS every root-pair propagation word, bases 2..16 and lengths 1..20')


if __name__ == '__main__':
    main()
