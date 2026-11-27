#!/usr/bin/env python3
"""Verify the prime range for the shifted dyadic residue criterion."""

from math import lcm

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
    roots = {3: (3361, 977), 4: (6202561, 2073677)}
    lucas, companion, half_companion, fibonacci = 3, 3, 1, 1
    for layer in range(1, 5):
        doubled_lucas = lucas * lucas - 2
        if layer in roots:
            p, root = roots[layer]
            assert p == doubled_lucas + 2 * companion and prime(p)
            assert p == 5 * fibonacci**2 + 4 * half_companion**2
            assert root * root % p == 5
            alpha = (1 + root) * pow(2, -1, p) % p
            assert pow(alpha, (p - 1) // 2, p) == p - 1
        fibonacci *= lucas
        half_companion, companion = companion, 2 * companion * companion - 1
        lucas = doubled_lucas


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


def verify_offset_depths(divisors):
    """Use the forced odd divisors to exclude depths 14 through 200."""
    for anchor, divisor in divisors.items():
        choices = [ell for ell in range(1, 12000, 2) if divisor % ell == 0]
        for depth in range(14, 201):
            if anchor == -1 and depth % 2:
                continue
            remaining = {3} if anchor == -1 else {1, 3}
            for ell in choices:
                modulus = 1 + (ell << (depth + 2))
                if modulus % 5 not in (1, 4):
                    continue
                for residue in tuple(remaining):
                    multiplier = ell * ((residue * ell) % 4)
                    value = val(anchor + (multiplier << depth), modulus)
                    if pow(value, (modulus - 1) // 2, modulus) == modulus - 1:
                        remaining.remove(residue)
                if not remaining:
                    break
            assert not remaining, (anchor, depth, sorted(remaining))
        print(f"Anchor {anchor}: all offset depths 14 through 200 excluded.")


def verify_small_boundary():
    factors = set()
    lucas, companion = 3, 3
    for _ in range(4):
        doubled_lucas = lucas * lucas - 2
        factors.update((lucas, companion, doubled_lucas + 2 * companion))
        lucas, companion = doubled_lucas, 2 * companion * companion - 1
    assert 81 in factors and 3 in factors
    factors.remove(81)
    assert all(prime(p) for p in factors)
    period = 45045
    for p in factors:
        group_order = p * p - 1
        period = lcm(period, group_order // (group_order & -group_order))
    multiplier = period * (3 * pow(period, -1, 32) % 32)
    for p in factors:
        shift = 16 * 32 * period
        assert mp(A, shift, p) == mp(B, shift, p) == I
        value = val(16 * multiplier - 1, p)
        assert pow(value, (p - 1) // 2, p) in (0, 1)


def verify():
    verify_base_characters()
    verify_next_layer_example()
    verify_excluded_valuations()
    verify_small_boundary()
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
