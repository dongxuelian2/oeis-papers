#!/usr/bin/env python3
"""Independent integer-only proof audit for the six-digit leading-pair table.

A root with highest two nonzero decimal digits a at exponent e and c at
exponent e-g has x/10**e in [a+c/10**g, a+(c+1)/10**g).
Squared values hence lie in the corresponding exact rational interval.
If x**2 uses only {1,4,9}, its first six significant digits must be
one of 3**6 integers over that alphabet. This script tests all interval
intersections using exact cross multiplication (no floating point).
The C++ verifier's high_pair_possible() must have the same table.
"""
from itertools import product

K = 6
PREFIXES = tuple(int("".join(ds)) for ds in product("149", repeat=K))
EXPECTED = {
    1: {1:(1,2,3,4), 2:(1,2), 3:(1,3,4,7,8), 4:(3,4),
        5:(), 6:(4,6,7), 7:(), 8:(), 9:(5,7,9)},
    2: {1:(5,6,7,9), 2:(2,3,4), 3:(1,2,3,6,7,8),
        4:(), 5:(), 6:(), 7:(1,2,3,6,7), 8:(), 9:()},
    3: {1:(), 2:(), 3:(), 4:(), 5:(), 6:(),
        7:(7,8), 8:(), 9:()}
}

def interval_contains_possible_square_prefix(gap, high, below):
    base = 10 ** gap
    left = high * base + below
    denominator = base * base
    for integer_digits in (1, 2):
        factor = 10 ** (K - integer_digits)
        for p in PREFIXES:
            # [left**2/denominator, (left+1)**2/denominator)
            # meets [p/factor, (p+1)/factor) strictly iff:
            if (left*left*factor < (p+1)*denominator
                    and (left+1)**2*factor > p*denominator):
                return True
    return False

def main():
    for gap in (1, 2, 3):
        for a in range(1, 10):
            candidates = tuple(c for c in range(1, 10)
                               if interval_contains_possible_square_prefix(
                                   gap, a, c))
            assert candidates == EXPECTED[gap][a], (gap, a, candidates)
    print("PASS: all 243 exact leading-pair interval checks")
    print("PASS: for gap 3 only (highest digit, next digit)=(7,7),(7,8)")
    print("NOTE: this is a necessary condition, not sufficient for squareness")

if __name__ == "__main__":
    main()
