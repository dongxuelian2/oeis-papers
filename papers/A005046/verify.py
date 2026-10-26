#!/usr/bin/env python3
"""Independent partition, finite-ring, and numerical Bessel checks."""
from decimal import Decimal, localcontext
from math import comb, factorial
from pathlib import Path


def terms(limit):
    a = [1]
    for n in range(1, limit + 1):
        a.append(sum(comb(2*n-1, 2*j-1)*a[n-j] for j in range(1, n+1)))
    return a


def step(v, m):
    """c*d/ds + s*d/dc + s on Z/m[s,c]/(s^m,c^m-1)."""
    w = [0]*(m*m)
    for i in range(m):
        for j in range(m):
            x = v[i*m+j]
            if i:
                w[(i-1)*m+(j+1)%m] += i*x
            if i+1 < m:
                if j:
                    w[(i+1)*m+j-1] += j*x
                w[(i+1)*m+j] += x
    return tuple(x % m for x in w)


def literal_partitions(size):
    """Generate restricted-growth words, keeping actual block sizes."""
    def visit(left, blocks):
        if not left:
            return int(all(x % 2 == 0 for x in blocks))
        answer = visit(left-1, blocks+[1])
        for j in range(len(blocks)):
            blocks[j] += 1
            answer += visit(left-1, blocks)
            blocks[j] -= 1
        return answer
    return visit(size, [])


def main():
    a = terms(250)
    rows = [tuple(map(int, line.split())) for line in
            Path(__file__).with_name('published-prefix.txt').read_text().splitlines()
            if line and not line.startswith('#')]
    assert [n for n, _ in rows] == list(range(len(rows)))
    assert all(a[n] == value for n, value in rows)
    for n in range(6):
        assert literal_partitions(2*n) == a[n]
    for m in range(2, 33):
        v = (1,)+(0,)*(m*m-1)
        for n in range(251):
            assert sum(v[:m]) % m == a[n] % m, (m, n)
            v = step(step(v, m), m)
    # Exact whole-polynomial certificates, not just scalar period samples.
    for m, start, period in ((2, 0, 3), (5, 1, 2)):
        v = (1,)+(0,)*(m*m-1)
        states = [v]
        for _ in range(start+period):
            v = step(step(v, m), m)
            states.append(v)
        assert states[start] == states[start+period]
    assert all(a[n] % 10 == (1, 4, 1, 9, 6, 9)[(n-1) % 6]
               for n in range(1, 251))
    # Numerical consistency only: the paper supplies convergence and equality.
    with localcontext() as ctx:
        ctx.prec = 100
        bessel = [sum(Decimal(1)/(Decimal(2)**(2*j+k)*factorial(j)*factorial(j+k))
                      for j in range(100)) for k in range(101)]
        for n in range(1, 13):
            value = 2/Decimal(1).exp()*sum(Decimal(k)**(2*n)*bessel[k]
                                         for k in range(1, 101))
            assert abs(value-Decimal(a[n])) < Decimal('1e-40')
    print(f'PASS A005046: {len(rows)} official terms; literal partitions through 10 elements;')
    print('  finite-ring controls modulo 2..32 through n=250; exact mod-2/mod-5 period certificates;')
    print('  Bessel numerical consistency n=1..12 (absolute error < 1e-40).')


if __name__ == '__main__':
    main()
