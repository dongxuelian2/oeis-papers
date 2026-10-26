#!/usr/bin/env python3
"""Reproducible checks of the constructive theorem for OEIS A181373.

The infinite theorem is established by main.tex, not by finite computation.
"""
from math import isqrt


def primes_up_to(n):
    a = bytearray(b"\x01") * (n + 1)
    a[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if a[p]:
            a[p*p::p] = b"\x00" * ((n - p*p)//p + 1)
    return [p for p in range(n + 1) if a[p]]


def mul(A, B, mod):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) % mod
                       for j in range(3)) for i in range(3))


def append_block(z, start, count, d, p):
    """Affine 3x3 matrix exponentiation across a run of d-digit blocks."""
    B = pow(10, d, p)
    T = ((B, 1, 1), (0, 1, 1), (0, 0, 1))
    E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    while count:
        if count & 1:
            E = mul(E, T, p)
        T = mul(T, T, p)
        count >>= 1
    return (E[0][0]*z + E[0][1]*(start-1) + E[0][2]) % p


def prefix_mod(m, p):
    z, start, d = 0, 1, 1
    while start <= m:
        last = min(m, start*10 - 1)
        z = append_block(z, start, last - start + 1, d, p)
        start *= 10
        d += 1
    return z


def digits(m):
    if m < 1:
        return 0
    d = len(str(m))
    return d*m - sum(10**k - 1 for k in range(1, d))


def witness(p):
    """Witness for p>=7, using only FLT and the p-digit block."""
    if p == 3:
        return 2
    assert p >= 7 and p % 2 and p % 5
    r = p - 1
    L = 10**r
    delta = (-digits(L - 1) - 1) % r
    m0 = L + delta
    j = (-9 * prefix_mod(m0, p)) % p
    m = m0 + j*r
    assert 0 <= j < p and L <= m < 10*L
    assert m <= L + p*r - 1
    assert digits(m) % r == 0
    assert prefix_mod(m, p) == 0
    return m



def multiplicative_order_10(p):
    """Order of 10 mod prime p, found without assuming a primitive root."""
    r, residue = 1, 10 % p
    while residue != 1:
        residue = residue * 10 % p
        r += 1
    assert (p - 1) % r == 0
    return r


def order_witness(p):
    """Correct corollary witness; note j has an inverse of r modulo p."""
    assert p >= 7 and p % 2 and p % 5
    r = multiplicative_order_10(p)
    d = 2*r + 1
    L = 10**(d-1)
    delta = (-digits(L-1)-1) % r
    m0 = L + delta
    j = (9 * prefix_mod(m0, p) * pow(r, -1, p)) % p
    m = m0 + j*r
    assert 0 <= j < p and L <= m < 10*L
    assert m <= L + p*r - 1
    assert digits(m) % r == 0
    assert prefix_mod(m, p) == 0
    return m

def brute_min(p, cap=1400):
    z, dcount = 0, 0
    for m in range(1, cap+1):
        d = len(str(m))
        z = (z*pow(10, d, p)+m) % p
        dcount += d
        if z == 0 and pow(10, dcount, p) == 1:
            return m
    return 0


def main():
    known = {3:2, 7:100, 11:106, 13:120, 17:196, 19:102,
             23:542, 29:400, 31:181, 37:21, 41:216, 43:372}
    for p, m in known.items():
        assert brute_min(p) == m, (p, brute_min(p), m)
    print("PASS: 12 OEIS published minimal values")

    for p in (3, 7, 11, 13, 17, 37, 101):
        for m in (1, 2, 9, 10, 18, 42, 99, 100, 125, 999, 1034):
            s = "".join(str(k) for k in range(1, m+1))
            assert digits(m) == len(s)
            assert prefix_mod(m, p) == int(s) % p, (p, m)
    print("PASS: matrix evaluator independently agrees with concatenation")

    ps = [p for p in primes_up_to(101) if p >= 7]
    for p in ps:
        m = witness(p)
        r, L = p-1, 10**(p-1)
        delta = (-digits(L-1)-1) % r
        m0 = L+delta
        assert (prefix_mod(m0+r,p)-prefix_mod(m0,p)) % p == pow(9,-1,p)
        if p <= 67:
            residue_list = [prefix_mod(m0+j*r,p) for j in range(p)]
            assert len(set(residue_list)) == p
            assert residue_list.count(0) == 1
    print(f"PASS: FLT construction for {len(ps)} primes 7..101")
    for p in (7, 11, 13, 17, 37, 101):
        m = order_witness(p)
        r = multiplicative_order_10(p)
        L = 10**(2*r)
        delta = (-digits(L-1)-1) % r
        m0 = L + delta
        assert (prefix_mod(m0+r, p)-prefix_mod(m0, p)) % p == (-r*pow(9,-1,p)) % p
        if p in (11, 13, 37):
            wrong_j = (-9*prefix_mod(m0,p)) % p
            # Explicit regression: the main theorem's j choice fails here.
            assert prefix_mod(m0+wrong_j*r,p) != 0
    print("PASS: order-sensitive witnesses for 7,11,13,17,37,101")
    print("PASS: wrong inverse-free j choice rejected for 11,13,37")

    assert witness(3) == 2
    print("PASS: p=3 and explicit upper bounds")
    print("Note: p=2,5 are impossible by the rotation ending in 1")


if __name__ == "__main__":
    main()
