#!/usr/bin/env python3
"""Exact integer audit of the closed-form A075018(d*10**r) family.

This code checks the theorem for d|30, r=2,3 by literal decimal
concatenation and exhaustive exclusion of every smaller endpoint.
The proof for all r>=2 is in main.tex; finite checking is supplementary.
"""

DIVISORS_30 = (1, 2, 3, 5, 6, 10, 15, 30)


def four_block_number(k: int) -> int:
    assert k >= 3
    return int("".join(str(j) for j in range(k, k - 4, -1)))


def audit():
    checked = 0
    for r in (2, 3):
        for d in DIVISORS_30:
            n = d * (10 ** r)
            assert four_block_number(3) % n != 0
            for k in range(4, n + 3):
                assert four_block_number(k) % n != 0, (d, r, k)
                checked += 1
            assert four_block_number(n + 3) % n == 0, (d, r)
            for j in range(1, 6):
                k = j * n + 3
                assert four_block_number(k) % n == 0, (d, r, j)
                for offset in (1, 2, 3):
                    assert four_block_number(k + offset) % n != 0, (d, r, j, offset)
            print(f"PASS: n={n}, exact minimum k={n+3}")
    print(f"PASS: {checked} smaller positive endpoints excluded by literal arithmetic.")
    print("The infinite theorem is proved in main.tex, not inferred from these checks.")


if __name__ == "__main__":
    audit()
