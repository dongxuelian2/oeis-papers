#!/usr/bin/env python3
"""Exact, independent certificate checker for OEIS A006063.

The JSON contains 192 complete permutation witnesses for n=173,...,364.
Neither floating-point arithmetic nor a matching library is used in checking.
"""
import json
from pathlib import Path

LOW, HIGH = 173, 364
HERE = Path(__file__).resolve().parent
WITNESSES = HERE / "certificates" / "base_permutations.json"


def cubes_through(bound):
    cubes = set()
    k = 2
    while k * k * k <= bound:
        cubes.add(k * k * k)
        k += 1
    return cubes


def check(n, perm):
    if not isinstance(perm, list) or len(perm) != n:
        raise AssertionError(f"length mismatch at n={n}")
    if any(type(x) is not int for x in perm):
        raise AssertionError(f"non-integer entry at n={n}")
    if sorted(perm) != list(range(1, n + 1)):
        raise AssertionError(f"not a permutation at n={n}")
    cubes = cubes_through(2 * n)
    for i, x in enumerate(perm, 1):
        if i + x not in cubes:
            raise AssertionError(f"not a cube: n={n}, i={i}, p_i={x}")


def load():
    data = json.loads(WITNESSES.read_text(encoding="utf-8"))
    if len(data) != HIGH - LOW + 1:
        raise AssertionError("incorrect number of rows")
    for n, perm in enumerate(data, LOW):
        check(n, perm)
    return data


def construct(n, base):
    """Construct a witness for any n>=173 by the proved cube reflection."""
    if n < LOW:
        raise ValueError("The theorem only covers n >= 173")
    if n <= HIGH:
        return base[n - LOW].copy()
    k = 2
    while k**3 < n + 174:
        k += 1
    cube = k**3
    if not n + 174 <= cube <= 2 * n:
        raise AssertionError(f"cube-gap inequality failed at n={n}")
    m = cube - n - 1
    if not LOW <= m < n:
        raise AssertionError(f"invalid induction predecessor at n={n}")
    return construct(m, base) + [cube - i for i in range(m + 1, n + 1)]


def main():
    base = load()
    print(f"PASS: {len(base)} explicit base permutations, "
          f"{sum(len(p) for p in base)} integer entries, n=173..364.")
    # The induction step is a theorem; these are extra implementation checks.
    for n in list(range(365, 1001)) + [1024, 5000, 10000, 100000]:
        check(n, construct(n, base))
    print("PASS: recursive construction checked for n=365..1000 "
          "and 1024, 5000, 10000, 100000.")


if __name__ == "__main__":
    main()
