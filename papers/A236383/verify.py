#!/usr/bin/env python3
"""All-index witness and exact modular-root minima for OEIS A236383."""
from functools import lru_cache
from math import isqrt
from pathlib import Path


@lru_cache(None)
def factor(n):
    fs = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            fs.append((p,e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        fs.append((n,1))
    return tuple(fs)


def roots_prime_power(n, p, e):
    """All roots of r²=n² modulo an ODD prime power; no root search."""
    assert p % 2
    mod = p**e
    u, v = n, 0
    while u % p == 0:
        u //= p
        v += 1
    if 2*v >= e:
        step = p**((e+1)//2)
        return tuple(range(0,mod,step))
    small_mod = p**(e-2*v)
    return tuple(sorted({(p**v * (sign*u + j*small_mod)) % mod
                         for sign in [-1,1] for j in range(p**v)}))


def roots(n, mod):
    residues, current = [0], 1
    for p, e in factor(mod):
        q = p**e
        local = roots_prime_power(n,p,e)
        inv = pow(current,-1,q)
        residues = [r + current*((s-r)*inv % q)
                    for r in residues for s in local]
        current *= q
    return sorted(residues)


def witness(n):
    if n < 1:
        raise ValueError('n must be positive')
    lower = len(str(4*(n+1)**2))
    residue = next(d for d in range(1,23,2) if (5*d+2*n) % 11 == 0)
    d = residue + 22*max(0,(lower-residue+21)//22)
    b = 10**d
    c = (b+1)//11
    k = n+5*c
    x = 5*(2*n+5*c)//11
    y = x+n*n
    assert (2*n+5*c) % 11 == 0
    assert 10**(d-1) <= x <= y < b
    assert k*k == b*x+y
    return k,d,x,y


def least(n):
    _, limit, _, _ = witness(n)
    for d in range(1,limit+1):
        b=10**d
        low_x,high_x=b//10,b-1-n*n
        if high_x < low_x:
            continue
        low_sq=(b+1)*low_x+n*n
        low=isqrt(low_sq)
        if low*low < low_sq:
            low += 1
        high=isqrt((b+1)*high_x+n*n)
        candidates=[r for r in roots(n,b+1) if low <= r <= high]
        if candidates:
            return min(candidates)
    raise AssertionError('proved witness missing')


def main():
    published=[]
    for line in Path(__file__).with_name('b236383-published.txt').read_text().splitlines():
        if line.strip() and not line.startswith('#'):
            published.append(tuple(map(int,line.split())))
    assert [n for n,_ in published] == list(range(1,246))
    for n,k in published:
        assert least(n) == k,(n,k,least(n))
    print('PASS all 245 official published minima')
    # Exhaustively scan consecutive k, independent of modular roots and bound.
    found={}
    for k in range(1,1_000_001):
        z=k*k
        length=len(str(z))
        if length % 2:
            continue
        d=length//2
        x,y=divmod(z,10**d)
        if y < 10**(d-1) or y <= x:
            continue
        n=isqrt(y-x)
        if n*n == y-x:
            found.setdefault(n,k)
    for n,k in found.items():
        assert least(n) == k,(n,k,least(n))
    assert all(found.get(n)==k for n,k in published)
    print(f'PASS independent exhaustive scan k=1..1000000: {len(found)} attained minima, including all 245 published indices')
    for p in [3,5,7,11,13]:
        for e in range(1,5):
            mod=p**e
            if mod > 20000:
                continue
            for n in range(1,101):
                actual=[r for r in range(mod) if (r*r-n*n)%mod==0]
                assert list(roots_prime_power(n,p,e)) == actual,(n,p,e)
    for mod in [33,121,385,1001,10201]:
        for n in range(1,101):
            assert roots(n,mod)==[r for r in range(mod) if (r*r-n*n)%mod==0]
    print('PASS prime-power root lists and composite CRT lists against direct residue enumeration')
    for n in list(range(1,1001))+[11**j for j in range(1,21)]+[10**100+11]:
        witness(n)
    print('PASS explicit witnesses through n=1000, powers 11^1..11^20, and a 101-digit index')
    rows=''.join(f'{n} {least(n)}\n' for n in range(1,301))
    table=Path(__file__).with_name('b236383.txt')
    if table.exists():
        assert table.read_text()==rows
    else:
        table.write_text(rows)
    print('PASS exact 300-term table')


if __name__=='__main__':
    main()
