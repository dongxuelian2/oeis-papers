#!/usr/bin/env python3
"""Finite, independent reproducibility checks for the A001292 partial theorems.

The infinite assertions require the proofs in README.md; this is NOT a
computational proof of Kashihara's conjecture.
"""
from collections import Counter

QR13 = {x*x % 13 for x in range(13)}


def digit_len(x):
    return len(str(x))


def digits_total(m):
    d = digit_len(m)
    return d*m - sum(10**j - 1 for j in range(1, d))


def direct_prefix_mod(m, p):
    z = 0
    for k in range(1, m+1):
        z = (z * pow(10, digit_len(k), p) + k) % p
    return z


def mmul(a, b, p):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) % p
             for j in range(3)] for i in range(3)]


def append_block(z, a, n, d, p=13):
    """Append a,a+1,...,a+n-1 in d-digit blocks modulo p by matrix powering."""
    T = [[pow(10, d, p), 1, 1], [0, 1, 1], [0, 0, 1]]
    E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    while n:
        if n & 1:
            E = mmul(T, E, p)
        T = mmul(T, T, p)
        n >>= 1
    return (E[0][0]*z + E[0][1]*((a-1) % p) + E[0][2]) % p


def family_mod13(t):
    d = 6*t + 3
    z = 0
    for j in range(1, d):
        a = 10**(j-1)
        z = append_block(z, a, 9*a, j)
    a = 10**(d-1)
    return append_block(z, a, 9*a-9, d)


def rotations_mod(m, p):
    D = digits_total(m)
    whole = direct_prefix_mod(m, p)
    pref, pref_len = 0, 0
    for j in range(m):
        yield (pow(10, pref_len, p)*whole
               + pref*(1-pow(10, D, p))) % p
        k = j+1
        pref = (pref*pow(10, digit_len(k), p)+k) % p
        pref_len += digit_len(k)


def main():
    value = 0
    count1 = count2 = 0
    for m in range(1, 100001):
        d = digit_len(m)
        value = (value*pow(10, d, 27)+m) % 27
        assert value == (m*(m+1)//2+9*d*((m+1)//3)) % 27, m
        assert digits_total(m) % 9 == d*m % 9
        if m % 27 == 9:
            assert value == 18 and digits_total(m) % 3 == 0
            count1 += 1
        if m % 27 == 17 and d % 3 == 0:
            assert value == 18 and digits_total(m) % 3 == 0
            count2 += 1
    print("PASS: mod-27 and length formulas for 100000 values", count1, count2)

    for m in [9, 36, 63, 90, 117, 125, 152, 171, 234, 990]:
        values = set(rotations_mod(m, 27))
        if m % 27 == 9 or (m % 27 == 17 and digit_len(m) % 3 == 0):
            assert values == {18}, (m, values)
        if m == 990:
            assert values == {9}
            assert set(rotations_mod(m, 13)).isdisjoint(QR13)
    print("PASS: all rotations for selected cases; combined sieve at m=990")

    table = [5, 8, 11, 4, 7, 12]
    for j in range(2, 56):
        a = 10**(j-1)
        assert append_block(0, a, 9*a, j) == table[(j-2) % 6]
    print("PASS: mod-13 complete-block period")

    for t in range(28):
        d = 6*t+3
        m = 10**d-10
        assert digits_total(m) % 6 == 0
        assert m % 27 == 18
        z = family_mod13(t)
        assert z == (6+5*t) % 13, (t, z)
        assert (z not in QR13) == (t % 13 in (0,1,3,5,7,8))
    print("PASS: large symbolic family t=0..27")
    print("Global conjecture remains OPEN")


if __name__ == "__main__":
    main()
