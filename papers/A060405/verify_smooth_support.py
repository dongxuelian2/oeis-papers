#!/usr/bin/env python3
"""Exact saturated-support square obstructions for a_(k-1)=L_(k-1)+P_(k-1)."""
from collections import Counter
from math import factorial, isqrt

A, B, I = (0, 1, 1, 1), (0, 1, 1, 2), (1, 0, 0, 1)
BOUND = 100000
EXPECTED = {2:7173, 3:1209, 5:579, 7:293, 11:142, 13:85,
            17:53, 19:22, 23:11, 29:11, 31:1, 37:5, 41:2, 43:1}


def mul(a, b, q):
    x,y,z,w = a; u,v,s,t = b
    return ((x*u+y*s)%q, (x*v+y*t)%q,
            (z*u+w*s)%q, (z*v+w*t)%q)


def power(a, n, q):
    assert n >= 0
    z = I
    while n:
        if n & 1:
            z = mul(z, a, q)
        a = mul(a, a, q)
        n //= 2
    return z


def primes(N):
    s = bytearray(b'\x01')*(N+1)
    s[:2] = b'\x00\x00'
    for p in range(2, isqrt(N)+1):
        if s[p]:
            s[p*p:N+1:p] = b'\x00'*len(range(p*p, N+1, p))
    return [p for p in range(2, N+1) if s[p]]


def vp(z, p):
    assert z != 0
    e = 0
    while z % p == 0:
        z //= p
        e += 1
    return e


def unit(z, p):
    return z//p**vp(z, p)


def zero_value(k, q):
    a, b = power(A, k, q), power(B, k, q)
    return (-a[0]+2*a[1]+b[0]) % q


def local_data(p):
    """h, valuation parity and unit of a_(h-1)/h, matrix depth, value depth."""
    h = {2:48, 3:24, 5:3000}.get(p, p*(p*p-1))
    q = p**8
    a, b = power(A, h, q), power(B, h, q)
    z = (-a[0]+2*a[1]+b[0]) % q
    assert z != 0
    e = vp(z, p)
    d = min(vp((x-y)%q, p) for C in (a,b) for x,y in zip(C,I) if (x-y)%q)
    w = 3 if p == 2 else 1
    assert d >= 1 and e+w <= 8 and 2*d-(p==2) >= e+w
    c = unit(z,p)*pow(unit(h,p), -1, p**w) % (p**w)
    return h, (e-vp(h,p))%2, c, d, e


def square_unit(u, p):
    return u%8 == 1 if p == 2 else pow(u%p, (p-1)//2, p) == 1


def certificate():
    ps = primes(BOUND)
    assert len(ps) == 9592
    data = {p:local_data(p) for p in ps}
    assert [p for p in ps if data[p][1]==0] == [2,3,5,19,307]
    assert all(factorial(13)**2 % data[p][0] == 0 for p in (2,3,5))
    assert data[2] == (48,0,3,4,4)

    # At prefix q, d_S=product of p with odd prescribed valuation.
    # Track only its p-unit residues, rather than constructing enormous d_S.
    probe = ps[:16]
    current = {p:1 for p in probe}
    failures = Counter()
    for q in ps:
        if data[q][1]:
            for p in probe:
                if p != q:
                    current[p] = current[p]*q % (8 if p==2 else p)
        if q < 13:
            continue
        bad = [p for p in probe if p<=q and not square_unit(current[p]*data[p][2],p)]
        assert bad, ('no obstruction',q)
        failures[bad[0]] += 1
    assert dict(failures) == EXPECTED
    assert sum(failures.values()) == 9587
    print('Prime-prefix supports excluded:',sum(failures.values()))
    print('First obstructing prime counts:',dict(sorted(failures.items())))

    # Independent sample checks of the exact leading-term congruence.
    count = 0
    for p in sorted(set(probe+[307]+ps[-10:])):
        h, par, c, d, e = data[p]
        w = 3 if p==2 else 1
        for t in (1,2,3,p,p*p,2*p,3*p*p):
            k = h*t
            v = e+vp(t,p)
            z = zero_value(k,p**(v+w))
            assert z and vp(z,p)==v
            assert unit(z,p) % p**w == c*unit(k,p)%p**w
            assert v%2 == (vp(k,p)+par)%2
            count += 1
    assert count==189
    print('Local formula sample checks:',count)

if __name__ == '__main__':
    certificate()
