#!/usr/bin/env python3
"""Proof checker for compact OEIS A006063 augmentation-word certificate.

A word r1...rt uses single-digit cube roots 2,...,8. Given the
previous matching p on 1..(n-1), start with the new left vertex u=n,
traverse a cube-sum edge u -> v=r**3-u, and, unless v=n, continue from
the UNIQUE previously matched left endpoint of the right vertex v.
A valid word ends on the new free right vertex n, with no repeated
old matched vertices. Flipping this path extends the matching.

One 11-interval involution of size 173 plus 191 short words certifies
all sizes 173..364. No long JSON certificate and no matching search
algorithm is needed by this independent checker.
"""
from pathlib import Path

BASE = [
    (1, 7, 8),
    (8, 12, 27),
    (13, 14, 125),
    (15, 19, 27),
    (20, 21, 125),
    (22, 42, 64),
    (43, 103, 216),
    (104, 105, 125),
    (106, 110, 216),
    (111, 112, 125),
    (113, 173, 216),
]
PATH = Path(__file__).resolve().parent / "certificates" / "augmenting_cube_words.txt"


def certify(p):
    n = len(p) - 1
    assert sorted(p[1:]) == list(range(1, n + 1)), f"permutation failure n={n}"
    cubes = {k*k*k for k in range(2, 10) if k*k*k <= 2*n}
    assert all(i+p[i] in cubes for i in range(1, n+1)), \
        f"cube-sum failure n={n}"


def seed_173():
    p = [0] * 174
    covered = [False] * 174
    for a, b, c in BASE:
        assert 1 <= a <= b <= 173 and c in {2**3, 3**3, 4**3, 5**3, 6**3}
        for i in range(a, b+1):
            assert not covered[i], f"repeated seed vertex {i}"
            covered[i] = True
            p[i] = c-i
    assert all(covered[1:])
    certify(p)
    assert all(p[p[i]] == i for i in range(1, 174)), "seed not involutive"
    return p


def flip_augmenting_word(p, n, word):
    assert len(p) == n and 174 <= n <= 364
    assert word and all(k in "2345678" for k in word)
    inverse = [0] * (n + 1)
    for i in range(1, n):
        inverse[p[i]] = i
    u = n
    visited_left = {n}
    visited_right = set()
    edges = []
    for j, digit in enumerate(word):
        root = int(digit)
        v = root**3 - u
        assert 1 <= v <= n, (n, j, u, root, v)
        assert v not in visited_right, (n, j, v)
        visited_right.add(v)
        edges.append((u, v))
        if v == n:
            assert j == len(word)-1, (n, j, "premature termination")
            break
        assert j < len(word)-1, (n, j, "did not reach free right")
        w = inverse[v]
        assert 1 <= w < n and w not in visited_left, (n, j, w)
        visited_left.add(w)
        u = w
    else:
        raise AssertionError(f"no terminal right vertex for n={n}")
    new = p + [0]
    for u, v in edges:
        new[u] = v
    certify(new)
    return new, len(edges)


def main():
    p = seed_173()
    lines = []
    for raw in PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            number, word = line.split()
            lines.append((int(number), word))
    assert [n for n, _ in lines] == list(range(174, 365))
    total = 0
    for n, word in lines:
        p, path_len = flip_augmenting_word(p, n, word)
        total += path_len
    assert total == 1844, total
    print(f"PASS: one explicit interval involution of n=173, "
          f"{len(lines)} alternating augmenting words, "
          f"{total} cube-root digits, all 192 matchings valid.")
    print("PASS: no matching solver, floating point or long witness JSON used.")


if __name__ == "__main__":
    main()
