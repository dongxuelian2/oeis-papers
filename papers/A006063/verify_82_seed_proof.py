#!/usr/bin/env python3
"""Arithmetic-only audit for the self-contained 82-seed proof of A006063.

Reads exactly 82 interval-reflection identity rows. All omissions through
364 are deduced by the elementary growing cubic suffix reflection; the
infinite tail is an algebraic cubic-gap lemma in COMPRESSED_FINITE_PROOF.md.

No matching, search, permutation-array archive or outside OEIS data is read.
"""
from collections import Counter
from pathlib import Path

ATLAS = Path(__file__).resolve().parent / "certificates" / "finite_82_seed_atlas.txt"
CUBES = tuple(k**3 for k in range(2, 9))
EXPECTED_SMALL_SEEDS = 22
EXPECTED_MIDDLE_SEEDS = 60
EXPECTED_SEGMENTS = 1009


def read_seeds():
    rows = {}
    total_segments = 0
    for raw in ATLAS.read_text(encoding="utf8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        cells = line.split()
        n = int(cells[0])
        assert 1 <= n <= 364 and n not in rows, n
        previous = 0
        left_endpoints = [n + 1]
        right_endpoints = [1]
        segments = []
        for cell in cells[1:]:
            b, k = (int(x) for x in cell.split(":"))
            assert 2 <= k <= 8, (n, cell)
            c = k**3
            left, right = c - b, c - previous
            assert 0 <= previous < b <= n, (n, cell)
            assert 1 <= left < right <= n + 1, (n, cell)
            left_endpoints.append(left)
            right_endpoints.append(right)
            segments.append((previous, b, c))
            previous = b
        assert previous == n, n
        # Exactly the multiset equality in the boundary-cancellation lemma.
        assert Counter(left_endpoints) == Counter(right_endpoints), n
        rows[n] = segments
        total_segments += len(segments)
    assert len(rows) == EXPECTED_SMALL_SEEDS + EXPECTED_MIDDLE_SEEDS
    assert sum(n < 173 for n in rows) == EXPECTED_SMALL_SEEDS
    assert sum(n >= 173 for n in rows) == EXPECTED_MIDDLE_SEEDS
    assert total_segments == EXPECTED_SEGMENTS, total_segments
    return rows


def close_under_reflections(seeds):
    # n=0 is legitimate as an empty base for c-1 = n.
    known = {0: None}
    ancestors = {}
    for n in range(1, 365):
        if n in seeds:
            known[n] = ("seed", n)
            # Irredundancy relative to these 82 seeds and cubic suffixes.
            assert not any(0 <= c-n-1 < n and c-n-1 in known
                           for c in CUBES), ("redundant seed", n)
            continue
        candidate = next(
            ((c, c - n - 1) for c in CUBES
             if 0 <= c-n-1 < n and c-n-1 in known),
            None,
        )
        if candidate is not None:
            c, m = candidate
            assert c - n == m + 1 and c - m - 1 == n
            known[n] = ("reflection", m, c)
            ancestors[n] = (m, c)
    for n in range(173, 365):
        assert n in known, ("uncovered length", n)
    assert sum(1 for n in known if 1 <= n < 173) == 48
    assert sum(1 for n in known if 173 <= n <= 364) == 192
    assert sum(1 for n in ancestors if n < 173) == 26
    assert sum(1 for n in ancestors if n >= 173) == 132
    return known, ancestors


def main():
    seeds = read_seeds()
    known, ancestors = close_under_reflections(seeds)
    print("PASS: 82 endpoint-multiset identities, 1,009 reflected intervals.")
    print("PASS: 22 small seeds and 60 middle seeds are irredundant")
    print("      under the specified strictly growing suffix-reflection rule.")
    print("PASS: derived 26 further lengths below 173 and")
    print("      132 further lengths from 173 through 364.")
    print("PASS: every n in 173..364 is covered without a matching solver.")
    print("The n>=365 tail uses the symbolic cube-gap inequality in")
    print("COMPRESSED_FINITE_PROOF.md and is not an executable assumption.")


if __name__ == "__main__":
    main()
