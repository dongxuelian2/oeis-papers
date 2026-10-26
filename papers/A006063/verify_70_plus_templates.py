#!/usr/bin/env python3
"""Independent 70-exception + four algebraic-template audit for A006063.

Only reads certificates/finite_70_exceptional_atlas.txt. The other twelve
base permutations are generated *from symbolic formulas* and the general
reflected-block rearrangement lemma; no old atlas, archive or matching
algorithm is used. Inductive closure uses integer cubic suffix reflection.
"""
from collections import Counter
from pathlib import Path

PATH = (Path(__file__).resolve().parent / "certificates" /
        "finite_70_exceptional_atlas.txt")
CUBES = {k**3 for k in range(2, 9)}
SPECIAL = {66, 85, 100, 103, 119, 122, 131, 150, 156, 175, 182, 254}


def block_template(lengths, order, cubes):
    """Exact block rearrangement; return (n, [(end, cuberoot), ...])."""
    size = len(lengths)
    assert all(isinstance(v, int) and v > 0 for v in lengths)
    assert sorted(order) == list(range(1, size + 1))
    assert len(cubes) == size and set(cubes) <= CUBES
    out_prefix = [None] * size
    total = 0
    for label in order:
        out_prefix[label-1] = total
        total += lengths[label-1]
    i_prefix = 0
    blocks = []
    for j, length in enumerate(lengths):
        c = 1 + i_prefix + out_prefix[j] + length
        assert c == cubes[j], (j, c, cubes[j])
        i_prefix += length
        root = next(k for k in range(2, 9) if k**3 == c)
        blocks.append((i_prefix, root))
    assert i_prefix == total
    return total, blocks


def parametric_rows():
    answers = {}
    def include(lengths, order, sums):
        n, blocks = block_template(lengths, order, sums)
        assert n not in answers
        answers[n] = blocks

    for U, V in ((64, 125), (125, 216), (216, 343)):
        a, b = 2*U-V-1, 2*V-3*U+1
        include((a,b,a,b), (3,4,1,2), (U,V,U,V))

    for X, Y, Z in ((27,64,125), (8,64,125)):
        a, b, c = 2*Y-Z-1, X+2*Z-4*Y+1, Y-X
        include((a,b,c,a,c), (4,2,5,1,3), (Y,X,Z,Y,Z))

    for X, W, Y, Z in ((8,64,64,125), (27,64,64,125),
                       (8,27,64,125)):
        a = 2*Y-Z-1
        b = X-2*a-1
        c = W+2*a-2*X+1
        d = Y+X-W-2*a-1
        include((a,b,c,d,a,d), (5,2,3,6,1,4),
                (Y,X,W,Z,Y,Z))
    # Eleven-block symbolic family (with the sixth block possibly empty).
    # The auxiliary Q at a deleted block need not be cubic.
    master_pi = (10,2,5,8,3,6,11,4,9,1,7)
    for X in (8,27):
        Y, Z, W = 64, 125, 216
        for Q in (125, 8*Z-4*W-2*X-1):
            a = 4*Z-2*W-Y-1
            b = 4*W+X+2*Y-8*Z+1
            c = 2*Z-W-X
            d = Q+4*W+2*X-8*Z+1
            e = 3*Z-W-X-Q
            f = 3*W+2*Y-6*Z+1
            lengths = (a,b,c,a,c,d,e,a,f,a,e)
            sums = (Z,X,Y,Z,Y,Q,W,Z,W,Z,W)
            assert min(a,b,c,e,f)>0 and d>=0
            if d == 0:
                order = tuple(v for v in master_pi if v != 6)
                lengths = tuple(v for i,v in enumerate(lengths,1) if i != 6)
                sums = tuple(v for i,v in enumerate(sums,1) if i != 6)
                # Renumber the 11 original labels after deletion of label 6.
                order = tuple(v if v<6 else v-1 for v in order)
            else:
                assert Q in CUBES
                order = master_pi
            include(lengths, order, sums)

    assert set(answers) == SPECIAL, sorted(answers)
    assert sum(map(len, answers.values())) == 82
    return answers


def read_exceptional():
    rows = {}
    total_segments = 0
    for raw in PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        tokens = line.split()
        n = int(tokens[0])
        assert 1 <= n <= 364 and n not in rows and n not in SPECIAL
        blocks = [tuple(map(int, token.split(":"))) for token in tokens[1:]]
        rows[n] = blocks
        total_segments += len(blocks)
    assert len(rows) == 70, len(rows)
    assert total_segments == 927, total_segments
    return rows


def validate_boundary_identity(n, blocks):
    previous = 0
    left, right = [n+1], [1]
    for b, k in blocks:
        assert 2 <= k <= 8 and previous < b <= n
        c = k**3
        lo, hi = c-b, c-previous
        assert 1 <= lo < hi <= n+1
        left.append(lo)
        right.append(hi)
        previous = b
    assert previous == n
    assert Counter(left) == Counter(right), n


def close_under_cubic_reflection(rows):
    present = {0}
    reflections = {}
    for n in range(1, 365):
        if n in rows:
            present.add(n)
            continue
        options = [(c, c-n-1) for c in sorted(CUBES)
                   if 0 <= c-n-1 < n and c-n-1 in present]
        if options:
            c, m = options[0]
            reflections[n] = (c, m)
            present.add(n)
    assert sum(1 for n in present if 1 <= n < 173) == 48
    assert all(n in present for n in range(173, 365))
    assert sum(n < 173 for n in reflections) == 26
    assert sum(n >= 173 for n in reflections) == 132
    return reflections


def main():
    exceptional = read_exceptional()
    templates = parametric_rows()
    rows = {**exceptional, **templates}
    assert len(rows) == 82
    assert sum(map(len, rows.values())) == 1009
    assert sum(n < 173 for n in rows) == 22
    for n, blocks in rows.items():
        validate_boundary_identity(n, blocks)
    refl = close_under_cubic_reflection(rows)
    print("PASS: 70 exceptional integer identities (927 blocks).")
    print("PASS: 4 algebraic template families produce 12 further lengths")
    print("      (82 blocks) with exact cube-sum block rearrangements.")
    print("PASS: all 82 base witnesses, 1009 blocks in total.")
    print("PASS: 26 small and 132 middle cubic suffix reflections.")
    print("PASS: all lengths 173..364 certified without matching.")
    print("Infinite tail follows from the symbolic cubic-gap lemma.")


if __name__ == "__main__":
    main()
