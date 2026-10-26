#!/usr/bin/env python3
"""Construct a certified cube-sum permutation in linear output time.

Uses the 109 self-contained core witnesses, the exact integer cube-root
function, and the reflection recurrence proved in main.tex. For enormous
n, the planning phase can be run without materializing n output values.
"""
from pathlib import Path
import argparse
import json

from verify import check
from verify_extended import integer_cuberoot

CORE = Path(__file__).resolve().parent / "certificates" / "core_109.json"


def ceil_cube_root(x):
    k = integer_cuberoot(x)
    return k if k**3 == x else k+1


def plan(n):
    if n < 173:
        raise ValueError("construction theorem covers n>=173")
    blocks = []
    current = n
    while current > 364:
        k = ceil_cube_root(current + 174)
        c = k**3
        m = c - current - 1
        if not (173 <= m < current and c <= 2*current):
            raise AssertionError("cube-gap lemma violation")
        blocks.append((m+1, current, c))
        current = m
    return current, blocks


def make(n):
    if n < 173:
        raise ValueError("construction theorem covers n>=173")
    seed_size, blocks = plan(n)
    core = json.loads(CORE.read_text(encoding="utf-8"))
    if str(seed_size) in core:
        seed = core[str(seed_size)]
    else:
        if not (256 <= seed_size <= 338):
            raise AssertionError("uncovered seed")
        m = 511 - seed_size
        seed = list(core[str(m)]) + [512-i for i in range(m+1, seed_size+1)]
    if len(seed) != seed_size:
        raise AssertionError("base length mismatch")
    result = [0] * (n+1)
    result[1:seed_size+1] = seed
    for lo, hi, cube in reversed(blocks):
        for i in range(lo, hi+1):
            result[i] = cube-i
    return result[1:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=None,
                    help="construct and fully verify a permutation of length n")
    ap.add_argument("--plan", type=int, default=None,
                    help="show construction block plan for a very large n")
    args = ap.parse_args()
    if args.plan is not None:
        seed_size, blocks = plan(args.plan)
        print(f"n={args.plan}: {len(blocks)} reflection steps, seed={seed_size}")
        for lo, hi, c in blocks[:15]:
            print(f"  interval=[{lo},{hi}], cube={c}")
    if args.n is not None:
        perm = make(args.n)
        check(args.n, perm)
        print(f"PASS: n={args.n}, {len(perm)} entries, all cube sums and a permutation.")
    if args.plan is None and args.n is None:
        sizes = [173,174,175,255,256,338,339,364,365,555,556,
                 1000,10000,100000,1000000]
        for n in sizes:
            check(n, make(n))
            seed, blocks = plan(n)
            print(f"PASS n={n}, depth={len(blocks)}, seed={seed}")
        seed, blocks = plan(10**60)
        assert 173 <= seed <= 364
        print(f"PASS huge-n planning for 10**60: depth={len(blocks)}")


if __name__ == "__main__":
    main()
