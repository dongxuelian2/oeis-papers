#!/usr/bin/env python3
"""Independent exact-arithmetic checks of OEIS A083468/A083469.
The mathematical proofs are in main.tex; finite checks are supplementary.
"""
from math import gcd


def smooth_10_part(n: int) -> int:
    q, r = 1, n
    for p in (2, 5):
        while r % p == 0:
            r //= p
            q *= p
    assert gcd(r, 10) == 1
    return q


def choose_parameters(n: int) -> tuple[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    q = smooth_10_part(n)
    m = n // q
    order = 1
    if m > 1:
        residue = 10 % m
        while residue != 1:
            residue = residue * 10 % m
            order += 1
    d = order
    while True:
        low = 10 ** (d - 1)
        high = 10 ** d - n
        a = ((low + q - 1) // q) * q
        if pow(10, d, q) == 0 and a <= high:
            assert pow(10, d, m) == 1 % m
            return d, a
        d += order


def concat_desc_mod(n: int, d: int, a: int) -> int:
    power = pow(10, d, n)
    residue = 0
    for x in range(a + n - 1, a - 1, -1):
        residue = (residue * power + x) % n
    return residue


def concat_desc(n: int, a: int) -> int:
    return int("".join(map(str, range(a + n - 1, a - 1, -1))))


def brute_minimum(n: int, top: int = 500) -> int | None:
    for k in range(n, top + 1):
        value = concat_desc(n, k - n + 1)
        if value % n == 0:
            return value
    return None


# Exact A083468 terms shown in OEIS for n=1,...,16.
OEIS_468_FIRST_16 = [
    1, 32, 321, 5432, 98765, 765432, 22212019181716, 98765432,
    987654321, 19181716151413121110, 2019181716151413121110,
    1312111098765432, 19181716151413121110987,
    2928272625242322212019181716, 1918171615141312111098765,
    27262524232221201918171615141312,
]


def main() -> None:
    for n in range(1, 513):
        d, a = choose_parameters(n)
        q = smooth_10_part(n)
        m = n // q
        assert 10 ** (d - 1) <= a <= a + n - 1 <= 10 ** d - 1
        assert a % q == 0
        assert pow(10, d, m) == 1 % m
        assert pow(10, d, q) == 0
        assert concat_desc_mod(n, d, a) == 0, (n, d, a)
        if n <= 30 and d <= 20:
            assert concat_desc(n, a) % n == 0
    print("PASS: constructive witnesses for n=1..512")

    for n, expected in enumerate(OEIS_468_FIRST_16, start=1):
        found = brute_minimum(n)
        assert found == expected, (n, found, expected)
        assert found % n == 0
    print("PASS: exact A083468 minima for n=1..16")
    print("PASS: A083469(1..16) = A083468(1..16)/n")

    verify_power_of_ten_minima()


def variable_width_concatenation_mod(n: int, a: int) -> int:
    """Independent literal modular concatenation; block widths may vary."""
    residue = 0
    for x in range(a + n - 1, a - 1, -1):
        residue = (residue * pow(10, len(str(x)), n) + x) % n
    return residue


def verify_power_of_ten_minima() -> None:
    """Check the exact formula and exclude smaller final blocks.

    The checks are finite; the proof for every exponent is in main.tex.
    """
    for r in (1, 2, 3):
        n = 10 ** r
        for a in range(1, n + 1):
            residue = variable_width_concatenation_mod(n, a)
            assert (residue == 0) == (a % n == 0), (n, a, residue)
        # All n blocks from n to 2*n-1 have exactly r+1 digits.
        B = 10 ** (r + 1)
        actual = concat_desc(n, n)
        formula = sum((n + j) * B ** j for j in range(n))
        assert actual == formula and actual % n == 0
        numerator = (2*n - 1) * B ** (n+1) - 2*n * B**n - (n-1)*B + n
        assert numerator % (B-1)**2 == 0
        assert numerator // (B-1)**2 == actual
        assert actual // n * n == actual  # A083469 exact quotient.
        if n == 10:
            assert actual == 19181716151413121110
        print(f"PASS: a({n}) = concat({2*n-1},...,{n}); "
              f"{n-1} smaller endpoints excluded; {len(str(actual))} digits")


if __name__ == "__main__":
    main()
