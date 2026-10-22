#!/usr/bin/env python3
"""Independent exact arithmetic checks for A006716 sparse-root theorems.

C++ certificate does the complete classification through support 12.
This Python script independently exhausts support <=4, tests the
two gap lemmas and the familiar decimal digit-sum inequality.
"""
from itertools import product

EXPECTED = (
    1, 2, 3, 7, 12, 21, 38, 107, 212, 70107
)
ALLOWED = set("149")


def accepted_root(x):
    return set(str(x * x)) <= ALLOWED


def check_sparse_up_to_four():
    roots = set(range(1, 10))
    # Lowest root position must be 0; next must be <=2.
    for e2 in (1, 2):
        for a, b in product(range(1, 10), repeat=2):
            roots.add(a * 10**e2 + b)
    first_two_count = len(roots)
    assert first_two_count == 171

    for e2 in (1, 2):
        for e3 in range(e2 + 1, 2*e2 + 3):
            for a, b, c in product(range(1, 10), repeat=3):
                roots.add(a * 10**e3 + b * 10**e2 + c)

    four_count = 0
    for e2 in (1, 2):
        for e3 in range(e2 + 1, 2*e2 + 3):
            for e4 in range(e3 + 1, 2*e3 + 3):
                for a, b, c, d in product(range(1, 10), repeat=4):
                    roots.add(
                        a * 10**e4 + b * 10**e3 +
                        c * 10**e2 + d
                    )
                    four_count += 1

    assert four_count == 269001, four_count
    actual = tuple(x for x in sorted(roots) if accepted_root(x))
    assert actual == EXPECTED, actual
    print("PASS support<=4:", actual,
          "4-sparse raw candidates:", four_count)


def check_two_gap_lemmas():
    checked = 0
    for p in range(0, 5):
        for e in range(p + 4, p + 7):
            for a in range(1, 10):
                for t in (1, 10**p, 7 * 10**p + 1):
                    if t >= 10**(p+1):
                        continue
                    x = a * 10**e + t
                    # Position 2e-1 cannot receive a carry from low terms.
                    assert (x*x // 10**(2*e-1)) % 10 == 0
                    checked += 1
    for p in range(1, 5):
        for e in range(2*p + 1, 2*p + 5):
            for high in range(1, 10):
                for low in (1, 10**(p-1), 9 * 10**(p-1)):
                    assert low < 10**p
                    x = high * 10**e + low
                    assert (x*x // 10**(2*p)) % 10 == 0
                    checked += 1
    print("PASS both gap lemmas:", checked, "integer identities tested")


def check_digit_sum():
    def digit_sum(n):
        return sum(map(int, str(n)))
    for x in range(1, 50_001):
        sx = digit_sum(x)
        assert digit_sum(x*x) <= sx*sx
        if accepted_root(x):
            n = len(str(x*x))
            nonzero = sum(c != "0" for c in str(x))
            assert n <= 81 * nonzero * nonzero
    print("PASS digit-sum inequality: 50000 squares")


if __name__ == "__main__":
    check_sparse_up_to_four()
    check_two_gap_lemmas()
    check_digit_sum()
