#!/usr/bin/env python3
"""Extend the square-index exclusion using exact recurrence periods."""

from math import lcm
from verify_anchor_forcing import A, B, I, M, ANCHORS, factors, four_anchors, mp, primes
from verify_composite_lifting import generalized_round
from verify_extension import forced_divisor


PRIME_BOUND = 1_000_000
LIFT_CAP = 2_000
EXPECTED = {
    3: ((171, 455), (151, 897), (4, 903), (0, 903)),
    -3: ((170, 451), (154, 901), (2, 904), (0, 904)),
    -1: ((188, 3760), (12, 3777), (0, 3777)),
}


def period(q):
    # For an inert eigenvalue lambda, lambda^(q+1) is the determinant -1.
    periods = []
    for matrix, discriminant in ((A, 5), (B, 8)):
        split = pow(discriminant, (q - 1) // 2, q) == 1
        h = q - 1 if split else 2 * (q + 1)
        for p in factors(h):
            while h % p == 0 and mp(matrix, h // p, q) == I:
                h //= p
        assert mp(matrix, h, q) == I
        periods.append(h)
    return lcm(*periods)


def certificate():
    assert four_anchors() == sorted(r % M for r in ANCHORS)
    zero_divisor = forced_divisor()
    test_primes = [q for q in primes(PRIME_BOUND) if q > 5]
    assert len(test_primes) == 78_495
    orders = [(q, period(q)) for q in test_primes]
    print(f"Verified periods for {len(orders):,} primes", flush=True)

    divisors = {}
    for r, expected in EXPECTED.items():
        divisor = zero_divisor if r == -1 else M
        for count, digits in expected:
            multiplier, forced = generalized_round(
                r, divisor, orders, cap=LIFT_CAP, singleton_cap=LIFT_CAP
            )
            divisor *= multiplier
            assert (len(forced), len(str(divisor))) == (count, digits)
            print(f"Anchor {r}: {count} prime powers, {digits} digits", flush=True)
        assert multiplier == 1
        divisors[r] = divisor

    # The norm descent excludes the even anchor -2.
    limit = min(divisor + r - 1 for r, divisor in divisors.items())
    assert limit >= 10**902
    print("Together with the even-index theorem, only index 3 survives in [0, 10^902].")
    return divisors


if __name__ == "__main__":
    certificate()
