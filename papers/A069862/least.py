#!/usr/bin/env python3
"""Exact A069862 values for every positive index, with guaranteed termination.

Each fixed-width state orbit is exhausted or skipped only after an exact
repeat. The universal bound in existence.tex supplies at most n widths.
Run: python3 least.py 37 451
"""
import argparse

from verify_existence import append


def least(n):
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    endpoint, value = n, 0
    width = len(str(n + 1))
    boundary = 10 ** width
    while width <= n:
        seen = set()
        base = pow(10, width, n)
        while endpoint < boundary - 1:
            state = (value, endpoint % n)
            if state in seen:
                # All further states in this width recur among states that
                # have been tested. Compute the boundary state for next width.
                value = append(value, endpoint, boundary - 1 - endpoint, width, n)
                endpoint = boundary - 1
                break
            seen.add(state)
            endpoint += 1
            value = (base * value + endpoint) % n
            if value == 0:
                return endpoint - n
        width += 1
        boundary *= 10
    raise AssertionError("Universal existence bound violated")


def audit():
    from verify import least as direct_least
    from verify_existence import independent_residue

    for n in range(1, 1001):
        result = least(n)
        # Directly append every block through the candidate endpoint and
        # independently check that no earlier residue vanishes.
        assert direct_least(n, result) == result, (n, result)
        assert independent_residue(n, n + result) == 0
        assert len(str(n + result)) <= n
    expected = {7: 9, 37: 998, 74: 926, 143: 285, 385: 9860, 451: 100270}
    assert all(least(n) == result for n, result in expected.items())
    print("PASS exact minima for n=1..1000 against unskipped direct enumeration")
    print("PASS six OEIS examples, including digit-width transitions and a(451)=100270")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("indices", type=int, nargs="*")
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()
    if args.audit:
        audit()
    for n in args.indices:
        print(n, least(n))
    if not args.audit and not args.indices:
        parser.error("supply positive indices or --audit")
