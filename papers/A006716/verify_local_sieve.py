#!/usr/bin/env python3
"""Exact finite audit of A006716 length-uniform local-square theorems.

Proofs are in LOCAL_SIEVE_BARRIER.md. No external packages.
This script NEVER infers ordinary integer squareness from modular tests.
"""
from itertools import product
from math import gcd


def modulo_decimal(digits, modulus):
    if modulus == 1:
        return 0
    residue = 0
    for c in digits:
        residue = (10 * residue + int(c)) % modulus
    return residue


def multiplicative_order_10(modulus):
    if modulus == 1:
        return 1
    assert gcd(modulus, 10) == 1
    k, residue = 1, 10 % modulus
    while residue != 1:
        residue = (residue * 10) % modulus
        k += 1
    return k


def coprime_component(modulus):
    result = modulus
    while result % 2 == 0:
        result //= 2
    while result % 5 == 0:
        result //= 5
    return result


def lower_length_bound(modulus):
    m = coprime_component(modulus)
    if m == 1:
        return 3
    h = multiplicative_order_10(m)
    return 4 + (((m + 13) // 3) - 1) * h


def construct(modulus, length, salt=0):
    """Produce n-digit word of {1,4,9} ending 441, square mod modulus."""
    m = coprime_component(modulus)
    h = multiplicative_order_10(m)
    reserved_count = (m + 13) // 3 if m > 1 else 0
    assert length >= lower_length_bound(modulus)
    reserved = [3 + j * h for j in range(reserved_count)]
    reserved_set = set(reserved)

    digits = ["1"] * length
    for position in range(3, length):
        if position not in reserved_set:
            # Deliberately make free digits nonperiodic-looking across examples.
            alphabet = "149"
            digits[length - 1 - position] = alphabet[
                (position * position + salt * position + salt) % 3
            ]
    digits[-3:] = list("441")
    if m > 1:
        baseline = modulo_decimal(digits, m)
        inv = pow(1000, -1, m)
        z = (-baseline * inv) % m
        r = 14 + (z - 14) % m
        v = (2 * r) % 3
        u = (r - 8 * v) // 3
        assert 3 * u + 8 * v == r
        assert 0 <= u and 0 <= v <= 2
        assert u + v <= reserved_count
        for j, position in enumerate(reserved):
            if j < u:
                digits[length - 1 - position] = "4"
            elif j < u + v:
                digits[length - 1 - position] = "9"
    word = "".join(digits)
    assert len(word) == length and set(word) <= set("149")
    assert word.endswith("441") and word[0] != "0"
    assert modulo_decimal(word, m) == 0
    assert modulo_decimal(word, 8) == 1
    assert modulo_decimal(word, 5) == 1
    return word


def check_unit_classification():
    for length in (3, 4, 5):
        modulus = 10 ** length
        roots_count = {}
        candidates = []
        for tup in product("149", repeat=length):
            word = "".join(tup)
            if word[-1] in "19":
                candidates.append(word)
                roots_count[int(word)] = 0
        for r in range(modulus):
            square = r * r % modulus
            if square in roots_count:
                roots_count[square] += 1

        qualifying = []
        for word in candidates:
            is_residue = roots_count[int(word)] > 0
            should_be = word.endswith(("441", "449"))
            assert is_residue == should_be, (length, word)
            if is_residue:
                qualifying.append(word)
                assert roots_count[int(word)] == 8, (length, word)
        assert len(qualifying) == 2 * 3 ** (length - 3)
        print(
            f"PASS n={length}: {len(qualifying)} odd unit words, "
            "exactly eight roots per permitted word"
        )


def check_all_moduli(max_modulus=100):
    # For each modulus, test the first three lengths following its
    # explicit constructive theorem bound and several free digit patterns.
    longest = 0
    for modulus in range(1, max_modulus + 1):
        available_squares = {x * x % modulus for x in range(modulus)}
        bound = lower_length_bound(modulus)
        for extra in (0, 1, 3):
            length = bound + extra
            longest = max(longest, length)
            for salt in (0, 1, 2):
                word = construct(modulus, length, salt)
                assert modulo_decimal(word, modulus) in available_squares, (
                    modulus, length, salt
                )
    print(
        f"PASS M=1..{max_modulus}, first three sampled lengths, "
        f"three free-digit patterns; max length {longest}"
    )


def main():
    check_unit_classification()
    check_all_moduli()
    print("All local-residue audit checks passed (no actual-square claim).")


if __name__ == "__main__":
    main()
