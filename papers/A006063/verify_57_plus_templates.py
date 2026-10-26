#!/usr/bin/env python3
"""Independent 57-exception + six algebraic-template audit for A006063.

Only reads certificates/finite_57_exceptional_atlas.txt. The other twenty-five
base permutations are generated *from symbolic formulas* and the general
reflected-block rearrangement lemma; no old atlas, archive or matching
algorithm is used. Inductive closure uses integer cubic suffix reflection.
"""
from collections import Counter
from pathlib import Path

PATH = (Path(__file__).resolve().parent / "certificates" /
        "finite_57_exceptional_atlas.txt")
CUBES = {k**3 for k in range(2, 9)}
SPECIAL = {66, 85, 100, 103, 119, 122, 131, 132, 150, 151, 155, 156, 174, 175, 182, 228, 229, 231, 238, 240, 241, 254, 345, 351, 357}


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
    # Twelve-block three-switch family: optional empty blocks 2, 3, and 7.
    mother_pi = (11,2,3,6,9,4,7,12,5,10,1,8)
    for X in (7,8):
        for T in (2*X-7,27):
            for Q in (121-2*T+2*X,125):
                u = X-7
                v = T-2*X+7
                w = X+27-T
                z = Q+2*T-2*X-121
                h = X+152-T-Q
                assert min(u,v,z)>=0 and min(w,h)>0
                lengths = (3,u,v,w,3,w,z,h,3,27,3,h)
                sums = (125,X,T,64,125,64,Q,216,125,216,125,216)
                nonempty = [j for j, L in enumerate(lengths,1) if L>0]
                renumber = {j:i for i,j in enumerate(nonempty,1)}
                lengths_active = tuple(lengths[j-1] for j in nonempty)
                sums_active = tuple(sums[j-1] for j in nonempty)
                order = tuple(renumber[j] for j in mother_pi if j in renumber)
                # Noncube nominal sums are permitted only at omitted blocks.
                assert set(sums_active) <= CUBES
                n, blocks = block_template(lengths_active, order, sums_active)
                assert n == 276+X-T-Q
                assert n not in answers
                answers[n] = blocks

    # Fifteen-block family: alpha<=beta; optional twelfth block t.
    mother_pi = (10,4,6,2,8,3,11,1,9,14,7,12,15,5,13)
    for alpha,beta in ((0,0),(0,1),(1,1)):
        t0 = 7+4*beta+2*alpha
        for t in (0,t0):
            lengths = (
                2*beta,
                7-alpha-4*beta-alpha*beta,
                alpha,
                alpha*beta,
                13+4*beta,
                alpha,
                23-4*beta-alpha,
                13+4*beta,
                48-alpha-45*beta+alpha*beta,
                2*beta,
                beta*(39-alpha),
                t,
                30+alpha-t,
                13+4*beta,
                91+alpha-t,
            )
            nominal = (
                21+43*beta,8,28-alpha,8,216,
                21+2*alpha+4*beta,125,64,125,
                105-41*beta,125,209-2*alpha-4*beta+t,
                343,216,343,
            )
            assert all(z>=0 for z in lengths)
            keep = tuple(j for j,L in enumerate(lengths,1) if L>0)
            renumber = {j:i for i,j in enumerate(keep,1)}
            live_lengths = tuple(lengths[j-1] for j in keep)
            live_sums = tuple(nominal[j-1] for j in keep)
            live_pi = tuple(renumber[j] for j in mother_pi if j in renumber)
            assert set(live_sums)<=CUBES
            n, blocks = block_template(live_lengths,live_pi,live_sums)
            assert n == 238+alpha+2*beta-t
            assert n not in answers
            answers[n] = blocks

    # Sixth algebraic family: two nested switches in ten-block output order.
    mother_pi = (1,2,8,5,6,9,4,10,3,7)
    for alpha,beta in ((0,0),(1,0),(1,1)):
        lengths = (
            7,12*alpha,159-24*alpha-99*beta,
            14*beta,28*beta,63*beta,
            10+24*alpha-6*beta,8*beta,
            159-24*alpha-107*beta,
            10+24*alpha+93*beta,
        )
        nominal = (
            8,8+19*alpha,343,
            167-12*alpha+61*beta,
            167-12*alpha-30*beta,
            167-12*alpha+61*beta,
            512,177+12*alpha+27*beta,343,512,
        )
        assert all(L>=0 for L in lengths)
        keep = tuple(j for j,L in enumerate(lengths,1) if L>0)
        renumber = {j:i for i,j in enumerate(keep,1)}
        live_lengths = tuple(lengths[j-1] for j in keep)
        live_sums = tuple(nominal[j-1] for j in keep)
        live_pi = tuple(renumber[j] for j in mother_pi if j in renumber)
        assert set(live_sums)<=CUBES
        n,blocks = block_template(live_lengths,live_pi,live_sums)
        assert n == 345+12*alpha-6*beta and n not in answers
        answers[n] = blocks

    assert set(answers) == SPECIAL, sorted(answers)
    assert sum(map(len, answers.values())) == 214
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
    assert len(rows) == 57, len(rows)
    assert total_segments == 795, total_segments
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
    print("PASS: 57 exceptional integer identities (795 blocks).")
    print("PASS: 6 algebraic template families produce 25 further lengths")
    print("      (214 blocks) with exact cube-sum block rearrangements.")
    print("PASS: all 82 base witnesses, 1009 blocks in total.")
    print("PASS: 26 small and 132 middle cubic suffix reflections.")
    print("PASS: all lengths 173..364 certified without matching.")
    print("Infinite tail follows from the symbolic cubic-gap lemma.")


if __name__ == "__main__":
    main()
