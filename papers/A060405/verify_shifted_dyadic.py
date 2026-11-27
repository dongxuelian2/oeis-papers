#!/usr/bin/env python3
"""Verify the prime range for the shifted dyadic residue criterion."""

from verify_anchor_forcing import A, B, I, mp
from verify_norm_order import prime


def order_depth(matrix, odd_part, depth_bound, modulus):
    power = mp(matrix, odd_part, modulus)
    for depth in range(depth_bound + 1):
        if power == I:
            return depth
        power = mp(power, 2, modulus)
    raise AssertionError("The split matrix order must divide p - 1.")


def verify():
    bound = 10**8
    depth_start = 14
    prime_step = 2 ** (depth_start + 2)
    tested = 0
    for p in range(1 + prime_step, bound + 1, prime_step):
        if p % 5 not in (1, 4) or not prime(p):
            continue
        tested += 1
        group_order = p - 1
        p_depth = (group_order & -group_order).bit_length() - 1
        odd_part = group_order >> p_depth
        depth = max(
            order_depth(A, odd_part, p_depth, p),
            order_depth(B, odd_part, p_depth, p),
        )
        if depth < depth_start + 2:
            continue

        lucas, pell_companion = 3, 3
        for layer in range(1, depth - 2):
            next_lucas = (lucas * lucas - 2) % p
            mixed = (next_lucas + 2 * pell_companion) % p
            assert lucas and pell_companion and mixed, (p, layer, depth)
            lucas = next_lucas
            pell_companion = (2 * pell_companion * pell_companion - 1) % p

    assert tested == 80
    print(f"{tested} split primes tested. No qualifying lower dyadic factor.")


if __name__ == "__main__":
    verify()
