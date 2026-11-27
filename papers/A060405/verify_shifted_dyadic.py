#!/usr/bin/env python3
"""Verify the prime range for the shifted dyadic residue criterion."""

from verify_anchor_forcing import A, B, I, mp, val
from verify_norm_order import prime


def order_depth(matrix, odd_part, depth_bound, modulus):
    power = mp(matrix, odd_part, modulus)
    for depth in range(depth_bound + 1):
        if power == I:
            return depth
        power = mp(power, 2, modulus)
    raise AssertionError("The split matrix order must divide p - 1.")


def verify_base_characters():
    for lucas, pell_companion, p, root in (
        (2207, 577, 3361, 977),
        (4870847, 665857, 6202561, 2073677),
    ):
        assert p == lucas + 2 * pell_companion and prime(p)
        assert root * root % p == 5
        alpha = (1 + root) * pow(2, -1, p) % p
        assert pow(alpha, (p - 1) // 2, p) == p - 1


def verify_next_layer_example():
    p, root, odd_part = 590232001, 217849727, 9222375
    assert prime(p) and p - 1 == 64 * odd_part and odd_part % 2
    assert root * root % p == 5
    lucas, companion = mp(A, 64, p), mp(B, 32, p)
    assert (lucas[0] + lucas[3] + companion[0] + companion[3]) % p == 0
    alpha = (1 + root) * pow(2, -1, p) % p
    assert pow(alpha, (p - 1) // 2, p) == p - 1
    for anchor in (3, -3, -1):
        assert pow(val(anchor + 16 * odd_part, p), (p - 1) // 2, p) == p - 1


def verify_excluded_valuations():
    p, root = 167772161, 4943721
    power = 2**25
    assert prime(p) and p - 1 == 5 * power
    assert root * root % p == 5
    lucas, companion = mp(A, power, p), mp(B, power // 2, p)
    assert (lucas[0] + lucas[3] + companion[0] + companion[3]) % p == 0
    alpha = (root + 1) * pow(2, -1, p) % p
    assert pow(alpha, power // 2, p) == p - 1

    p = 230686721
    period = 44 * 2**20
    assert prime(p) and mp(A, period, p) == mp(B, period, p) == I
    for anchor in (3, -3):
        for multiplier in (11, 33):
            value = val(anchor + 2**20 * multiplier, p)
            assert pow(value, (p - 1) // 2, p) == p - 1


def verify():
    verify_base_characters()
    verify_next_layer_example()
    verify_excluded_valuations()
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
        for layer in range(1, depth - 1):
            next_lucas = (lucas * lucas - 2) % p
            mixed = (next_lucas + 2 * pell_companion) % p
            assert mixed, (p, layer, depth, "mixed")
            if layer < depth - 2:
                assert lucas and pell_companion, (p, layer, depth, "companion")
            lucas = next_lucas
            pell_companion = (2 * pell_companion * pell_companion - 1) % p

    assert tested == 80
    print(f"{tested} split primes tested. No qualifying dyadic factor.")


if __name__ == "__main__":
    verify()
