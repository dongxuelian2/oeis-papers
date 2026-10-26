#!/usr/bin/env python3
from math import comb
from pathlib import Path


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def closed(n, k):
    return sum(choose(i, k-i)*choose(n+1, i+1) for i in range((k+1)//2, k+1))


def main():
    rows = []
    power, total = [1], []
    for n in range(151):
        total += [0]*(len(power)-len(total))
        total = [a+b for a,b in zip(total,power)]
        rows.append(total[:])
        new = [0]*(len(power)+2)
        for i,v in enumerate(power):
            for j in range(3):
                new[i+j] += v
        power = new
    def entry(n,k):
        return rows[n][k] if k < len(rows[n]) else 0
    for n in range(101):
        for k in range(41):
            assert entry(n,k) == closed(n,k)
            assert sum((-1)**m*comb(k+2,m)*entry(n+m,k) for m in range(k+3)) == 0
    print('PASS independent trinomial rows, closed column formula and differences: n<=100,k<=40')
    for m in range(101):
        actual = sum((-1)**k*entry(m-k,k) for k in range(m+1))
        q,r = divmod(m,4)
        assert actual == 2*q+([1,2,2,2][r])
    print('PASS all alternating antidiagonals through index100')
    p = Path(__file__).with_name('b260056-published.txt')
    pairs = [tuple(map(int,l.split())) for l in p.read_text().splitlines()
             if l.strip() and not l.startswith('#')]
    flat = [v for row in rows[:100] for v in row]
    assert len(pairs) == len(flat) == 10000
    assert [v for _,v in pairs] == flat
    print('PASS all10000 official flattened terms (100 complete rows)')


if __name__ == '__main__':
    main()
