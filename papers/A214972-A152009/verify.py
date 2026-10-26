#!/usr/bin/env python3
"""Exact controls for the L-sieve theorems; Python standard library only."""
from bisect import bisect_right
from functools import lru_cache
from pathlib import Path


def thresholds(d, bound):
    result, value = [], 1
    while value <= bound:
        result.append(value)
        value = 1+(d*value+d-2)//(d-1)
    return result


def literal_sieve(deleted, bound):
    """Finite initial list; every term produced is also an infinite-sieve term."""
    values, result = list(range(1, bound+1)), []
    while values:
        result.append(values.pop(0))
        values = [v for j, v in enumerate(values, 1) if not deleted(j)]
    return result


class Sieve:
    """Lazy exact complement rank, independent of threshold formulas."""
    def __init__(self, contains):
        self.contains = contains
        self.outputs = [1]
        self.complement = []
        self.scanned = 0

    def term(self, index):
        while len(self.outputs) < index:
            needed = self.outputs[-1]
            while len(self.complement) < needed:
                self.scanned += 1
                if not self.contains(self.scanned):
                    self.complement.append(self.scanned)
            self.outputs.append(1+self.complement[needed-1])
        return self.outputs[index-1]

    @lru_cache(None)
    def member(self, value):
        while self.outputs[-1] < value:
            self.term(len(self.outputs)+1)
        return value in self.outputs


def audit():
    bound = 100000
    for d in range(2, 13):
        hs = [0]*(bound+1)
        ts = thresholds(d, bound)
        for n in range(1, bound+1):
            hs[n] = 1+hs[(d-1)*(n-1)//d]
            assert hs[n] == bisect_right(ts, n), (d, n)
        direct = literal_sieve(lambda j: j % d == 1, bound)
        assert direct == ts, d
    print('PASS exact jump identity and literal L-sieve for d=2..12, n<=100000')
    rows = [tuple(map(int, line.split())) for line in
            Path(__file__).with_name('published-A152009.txt').read_text().splitlines()
            if line and not line.startswith('#')]
    ts = thresholds(3, rows[-1][1])
    assert [(i+1, v) for i, v in enumerate(ts)] == rows
    print(f'PASS all {len(rows)} published A152009 terms')
    sets = [frozenset(j+1 for j in range(8) if mask >> j & 1)
            for mask in range(1, 256)]
    predicates = [(lambda x, s=s: x in s) for s in sets]
    predicates += [(lambda x, d=d, r=r: x % d == r)
                   for d in range(2, 7) for r in range(d)]
    for contains in predicates:
        current = contains
        for iteration in range(1, 12):
            sieve = Sieve(current)
            k = (iteration+1)//2
            assert [sieve.term(j) for j in range(1, k+1)] == [j*(j+1)//2 for j in range(1, k+1)]
            current = sieve.member
    print(f'PASS stabilization through 11 transforms for {len(predicates)} deletion sets')
    # Use exact membership for the actual fixed-point control.
    from math import isqrt
    triangular = Sieve(lambda n: isqrt(8*n+1)**2 == 8*n+1)
    assert [triangular.term(j) for j in range(1, 101)] == [j*(j+1)//2 for j in range(1, 101)]
    print('PASS triangular fixed point for first 100 terms')


if __name__ == '__main__':
    audit()
