#!/usr/bin/env python3
"""Independent finite checks of the constructive all-n A077306 theorem.

The theorem itself is proved for all positive integers in the matching
research note; this tests formulas, digit-width constraints and actual
concatenation residues, NOT a bounded replacement for the proof.

Python standard library only.
"""
from math import gcd


def order10(m: int) -> int:
    if m == 1:
        return 1
    assert gcd(m, 10) == 1
    x, count = 10 % m, 1
    while x != 1:
        x = x * 10 % m
        count += 1
        assert count <= m
    return count


def construction(n: int) -> tuple[int, int, int, int]:
    assert n >= 1
    m = n
    for p in (2, 5):
        while m % p == 0:
            m //= p
    s = n // m
    period = order10(m)
    d = period
    while 10**d % s or 9 * 10 ** (d - 1) <= n + s:
        d += period
    assert pow(10, d, m) == (1 % m)
    assert (10**d) % s == 0
    k = 10**d - n - s + 1
    assert 10 ** (d - 1) <= k <= k + n - 1 < 10**d
    assert k + n - 1 == 10**d - s
    return d, k, s, m


def independent_modular_concatenation(n: int, d: int, k: int) -> int:
    # Perform the original digit concatenation recurrence modulo n,
    # without using the closed-form congruence from the proof.
    q = pow(10, d, n)
    residue = 0
    for offset in range(n):
        residue = (residue * q + k + offset) % n
    return residue


def main() -> None:
    for n in range(1, 1001):
        d, k, s, m = construction(n)
        q = pow(10, d, n)
        assert independent_modular_concatenation(n, d, k) == 0
        assert (k + n - 1) % s == 0
        if m > 1:
            assert q % m == 1
            assert (n * k + n * (n - 1) // 2) % m == 0
    # Include some cases where the remaining coprime part has
    # unusually large order, and relatively large smooth factors.
    for n in (1024, 2025, 2187, 2401, 4096):
        d, k, _, _ = construction(n)
        assert independent_modular_concatenation(n, d, k) == 0
    print("PASS A077306: 1000 contiguous indices + five stress cases")
    for n in (6, 12, 14, 21, 30, 77, 100):
        d, k, s, m = construction(n)
        print(f"n={n}: d={d}, k={k}, last={k+n-1}, smooth={s}, coprime={m}")
    print("The unbounded existence theorem follows from CRT, not these tests.")


if __name__ == "__main__":
    main()
