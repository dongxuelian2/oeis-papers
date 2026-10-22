#!/usr/bin/env python3
"""Exact-int branch-and-bound certificate for A087354(20..25).

Usage:
    python verify_minima.py              # full n=20..24; witness check n=25
    python verify_minima.py --extended   # complete slower n=25 search
"""
import argparse
from functools import lru_cache
from math import isqrt

EXPECTED = {
    20: 111125911149919941444,
    21: 444411911999914911441,
    22: 11199444494448114419449,
    23: 144949449149149194448144,
    24: 1111425414199449191191449,
    25: 41914991191911941194149136,
}
ONE_DIGIT_SQUARES = (1, 4, 9)
TWO_DIGIT_SQUARES = (16, 25, 36, 49, 64, 81)


def positive_square_parts(value, parts):
    """Independent parsing check for every proposed upper-bound witness."""
    s = str(value)
    assert isqrt(value)**2 == value

    @lru_cache(None)
    def visit(pos, k):
        if k == parts:
            return () if pos == len(s) else None
        for end in range(pos+1, len(s)+1):
            if s[pos] == '0':
                return None
            block = int(s[pos:end])
            if isqrt(block)**2 != block:
                continue
            rest = visit(end, k+1)
            if rest is not None:
                return (block,) + rest
        return None

    found = visit(0, 0)
    assert found is not None, (value, parts)
    assert len(found) == parts
    assert ''.join(map(str, found)) == s
    return found


def least_at_length(n, length, cap):
    """Exhaust n square blocks occupying exactly length digits, up to cap.

    For length=n, blocks have one digit (1,4,9); for length=n+1,
    exactly one block has two digits (16,25,36,49,64,81).
    Each prefix p of d digits can only extend to an integer in
    [p*10^(length-d), (p+1)*10^(length-d)-1], intersected with [0,cap].
    A prefix with no square in this interval may be safely discarded.
    """
    assert n <= length <= n+1
    powers = [10**i for i in range(length+1)]
    best = None
    nodes = pruned = square_leaves = 0

    def dfs(prefix, digits, blocks):
        nonlocal best, nodes, pruned, square_leaves
        nodes += 1
        upper = min(cap, best) if best is not None else cap
        lo = prefix * powers[length-digits]
        hi = min((prefix+1)*powers[length-digits]-1, upper)
        if lo > hi:
            pruned += 1
            return
        lower_root = 0 if lo == 0 else isqrt(lo-1)+1
        if lower_root > isqrt(hi):
            pruned += 1
            return
        if blocks == n:
            if digits == length and isqrt(prefix)**2 == prefix:
                square_leaves += 1
                if best is None or prefix < best:
                    best = prefix
            return
        excess = length-digits-(n-blocks)
        if excess < 0:
            return
        for width, alphabet in ((1, ONE_DIGIT_SQUARES), (2, TWO_DIGIT_SQUARES)):
            if width-1 > excess:
                continue
            for block in alphabet:
                dfs(prefix*powers[width]+block, digits+width, blocks+1)

    dfs(0, 0, 0)
    return best, (nodes, pruned, square_leaves)


def certify(n, claimed):
    assert len(str(claimed)) in (n, n+1)
    assert positive_square_parts(claimed, n)
    least = None
    for length in range(n, len(str(claimed))+1):
        found, (nodes, pruned, square_leaves) = least_at_length(n, length, claimed)
        print(f'  L={length}: nodes={nodes}, interval_prunes={pruned}, square_leaves={square_leaves}, min={found}')
        if found is not None:
            least = found if least is None else min(least, found)
    assert least == claimed, (n, least, claimed)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--extended', action='store_true',
                        help='also exhaust n=25 (expensive with Python)')
    args = parser.parse_args()
    for n, value in EXPECTED.items():
        blocks = positive_square_parts(value, n)
        print(f'n={n}: {value} = {isqrt(value)}^2, blocks={blocks}')
        if n == 25 and not args.extended:
            print('  Witness verified. Run with --extended for n=25 minimality.')
            continue
        certify(n, value)
        print('  CERTIFIED MINIMUM')
    print('All checks passed.')


if __name__ == '__main__':
    main()
