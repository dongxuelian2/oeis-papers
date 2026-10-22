#!/usr/bin/env python3
"""Small independent audit for exact witness-phase density theorems.

No external packages or imports from the research code. Directly checks
digit-layer states and affine witness formulas in small prime fields.
Synthetic anti-diagonal states check algebra only; they are NOT claimed
to be true prime-field drift vectors. The infinite results are PROVED
mathematically, not inferred from these examples.
"""
from math import gcd, lcm


def order10(p):
    if p == 1:
        return 1
    value, n = 10 % p, 1
    while value != 1:
        value = value * 10 % p
        n += 1
    return n


def layer(p, r, d, C, Y):
    q, L = pow(10, d, p), pow(10, d - 1, p)
    n = 9 * L % p
    A = pow(10, (9 * d * pow(10, d - 1, r)) % r, p)
    if q == 1:
        S = n
        J = n * (n - 1) * pow(2, -1, p) % p
    else:
        iv = pow(q - 1, -1, p)
        S = (A - 1) * iv % p
        J = (q - n * A + (n - 1) * A * q) * iv * iv % p
    return ((A * C + (q - 1) * S - J) % p,
            (Y + L * S + J) * pow(A, -1, p) % p)


def drift(p):
    r = order10(p)
    v = r
    for factor in (2, 5):
        while v % factor == 0:
            v //= factor
    t = v // gcd(v, 9)
    T = lcm(r, order10(t))
    C = Y = 0
    seed = None
    for d in range(1, 2 * T + 1):
        C, Y = layer(p, r, d, C, Y)
        if d == T:
            seed = C, Y
    return r, T, seed, ((C - seed[0]) % p, (Y - seed[1]) % p)


def next_window(p, r, C0, Y0, U, V):
    """Count distinct j mod p admitting k=10^(jT)+n, 0<=n<r."""
    phases, regular, exceptional = set(), 0, []
    inv10 = pow(10, -1, p)
    C, Y = C0, Y0
    for n in range(r):
        slope = (pow(10, n + 1, p) * U
                 + pow(10, -n, p) * V) % p
        intercept = (10 * C + Y + n + 1) % p
        if slope == 0:
            exceptional.append(n)
        else:
            j = 1 + (-intercept * pow(slope, -1, p)) % p
            phases.add(j)
            regular += 1
            Cj, Yj = (C0 + (j - 1) * U) % p, (Y0 + (j - 1) * V) % p
            for offset in range(n):
                k = offset + 1
                Cj = (10 * Cj + k) % p
                Yj = (Yj + k) * inv10 % p
            assert (10 * Cj + Yj + n + 1) % p == 0
        C = (10 * C + n + 1) % p
        Y = (Y + n + 1) * inv10 % p
    return phases, regular, exceptional


def audit():
    primes = (7, 13, 17, 23, 29, 37, 43, 73,
              101, 137, 211, 313, 617)
    for p in primes:
        r, T, (C, Y), (U, V) = drift(p)
        S = (U + V) % p
        if S:
            squares = {x * x % p for x in range(p)}
            good = [j for j in range(1, p + 1)
                    if (-(C + Y + (j - 1) * S)) % p in squares]
            assert len(good) == (p + 1) // 2
            multiplicity = sum(
                1 if (-(C + Y + (j - 1) * S)) % p == 0 else 2
                for j in good)
            assert multiplicity == p
        phases, nregular, exceptional = next_window(
            p, r, C, Y, U, V)
        assert len(exceptional) <= gcd(r, 2)
        assert 2 * len(phases) >= nregular
        print("PASS genuine prime", p, "r", r, "T", T,
              "S", S, "next-phase count", len(phases))

    # Exercises the alternative S=0, U!=0 even though no genuine
    # anti-diagonal drift is asserted or fabricated.
    for p in (23, 37, 43, 73):
        r = order10(p)
        C, Y, U, V = 19 % p, 29 % p, 1, p - 1
        phases, nregular, exceptional = next_window(
            p, r, C, Y, U, V)
        assert len(exceptional) == r % 2, (p, exceptional)
        assert nregular == r - r % 2
        assert 2 * len(phases) >= nregular
        print("PASS synthetic anti-diagonal algebra", p, r,
              "phase count", len(phases))

    print("PASS square-law and anti-diagonal phase bounds")
    print("No assertion about zero-drift existence or nonexistence.")


if __name__ == "__main__":
    audit()
