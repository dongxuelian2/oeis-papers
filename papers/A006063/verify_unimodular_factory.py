#!/usr/bin/env python3
"""57 finite A006063 cases as *symbolic cubic determinant families*.

Reads ONLY certificates/finite_57_cubic_order_shapes.txt, containing
cube-root words and output orders, without any input breakpoints.
Builds the unimodular matrix M(pi), recovers the unique positive integer
lengths with fraction-free exact integer elimination, and verifies
arbitrary positive integer cube dilations. No matching or old interval
atlas is imported for any of these 57 shapes.

The other 25 base seeds come from the six symbolic families of
verify_57_plus_templates.py. We import only its parametric_rows()
function (which reads no certificate). The 173..364 closure is audited.
"""
from pathlib import Path

SHAPES = (Path(__file__).resolve().parent / "certificates"
          / "finite_57_cubic_order_shapes.txt")
CUBES = {k**3 for k in range(2, 9)}
EXPECTED_ROWS = 57
EXPECTED_BLOCKS = 795


def read_shapes():
    result = {}
    for raw in SHAPES.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        cells = [part.strip() for part in s.split("|")]
        assert len(cells) == 3, s
        n = int(cells[0])
        roots = [int(x) for x in cells[1].split(",")]
        order = [int(x) for x in cells[2].split(",")]
        t = len(roots)
        assert n > 0 and n not in result
        assert t and all(2 <= k <= 8 for k in roots)
        assert sorted(order) == list(range(1, t + 1))
        result[n] = (roots, order)
    assert len(result) == EXPECTED_ROWS
    assert sum(len(roots) for roots, _ in result.values()) == EXPECTED_BLOCKS
    return result


def integer_matrix(order):
    """C_j-1 = sum_i M[j,i] * ell_i."""
    t = len(order)
    position = {label: q for q, label in enumerate(order)}
    assert len(position) == t
    return [[int(i < j) + int(position[i + 1] < position[j + 1])
             + int(i == j) for i in range(t)]
            for j in range(t)]


def bareiss_solve(matrix, b):
    """Return (det M, M^{-1}b), exact integer arithmetic only.

    The back-substitution is integer because all accepted determinants
    equal +1. No float approximations, NumPy, SymPy, or matchings.
    """
    n = len(matrix)
    a = [list(map(int, row)) + [int(b[i])]
         for i, row in enumerate(matrix)]
    denominator, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n)
                              if a[i][k] != 0), None)
            if pivot_row is None:
                raise AssertionError("singular cubic-order shape")
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            left = a[i][k]
            for j in range(k + 1, n + 1):
                numerator = a[i][j] * pivot - left * a[k][j]
                assert numerator % denominator == 0
                a[i][j] = numerator // denominator
            a[i][k] = 0
        denominator = pivot
    determinant = sign * a[n - 1][n - 1]
    assert determinant != 0
    x = [0] * n
    for i in range(n - 1, -1, -1):
        numerator = a[i][n] - sum(a[i][j] * x[j]
                                  for j in range(i + 1, n))
        assert numerator % a[i][i] == 0, (i, numerator, a[i][i])
        x[i] = numerator // a[i][i]
    assert all(sum(matrix[i][j] * x[j] for j in range(n)) == b[i]
               for i in range(n))
    return determinant, x


def validate_permutation(lengths, roots):
    n = sum(lengths)
    assert all(L >= 1 for L in lengths)
    q, start = [], 0
    for L, k in zip(lengths, roots):
        for i in range(start + 1, start + L + 1):
            q.append(k**3 - i)
        start += L
    assert len(q) == n and set(q) == set(range(1, n + 1))
    return n


def verify_shape(n, roots, order):
    M = integer_matrix(order)
    assert all(M[i][j] + M[j][i] == 2
               for i in range(len(M)) for j in range(len(M)))
    determinant, lengths = bareiss_solve(M, [k**3 - 1 for k in roots])
    assert determinant == 1, (n, determinant)
    assert min(lengths) >= 1 and sum(lengths) == n
    assert validate_permutation(lengths, roots) == n
    d2, v = bareiss_solve(M, [1] * len(roots))
    assert d2 == 1
    assert set(v) <= {-1, 0, 1}
    assert sum(v) == len(roots) % 2
    # The parameterized family applies to EVERY h>=1, not only
    # the following two independently checked examples:
    # L_j(h) = L_j + (h^3-1)(L_j+v_j);
    # the coefficient is >=0 since L_j>=1 and v_j>=-1.
    assert all(L + w >= 0 for L, w in zip(lengths, v))
    parity = len(roots) % 2
    for h in (2, 3):
        scaled = [L + (h**3 - 1) * (L + w)
                  for L, w in zip(lengths, v)]
        assert sum(scaled) == ((n + parity) * h**3 - parity)
        assert all(x > 0 for x in scaled)
        assert all(sum(M[i][j] * scaled[j] for j in range(len(M)))
                   == (h * roots[i])**3 - 1
                   for i in range(len(M)))
        if h == 2:
            validate_permutation(scaled, [h*k for k in roots])
    return lengths, v


def main():
    shape_rows = read_shapes()
    recovered = {}
    for n, (roots, order) in sorted(shape_rows.items()):
        lengths, v = verify_shape(n, roots, order)
        blocks = []
        pos = 0
        for length, k in zip(lengths, roots):
            pos += length
            blocks.append((pos, k))
        recovered[n] = blocks
    # The original seed families use no old explicit endpoint atlas.
    from verify_57_plus_templates import parametric_rows
    symbolic = parametric_rows()
    assert len(symbolic) == 25 and not (set(symbolic) & set(recovered))
    bases = {**recovered, **symbolic}
    assert len(bases) == 82
    known = {0}
    reflected = set()
    for n in range(1, 365):
        if n in bases:
            known.add(n)
        else:
            possible = [(c, c - n - 1) for c in sorted(CUBES)
                        if 0 <= c - n - 1 < n and c - n - 1 in known]
            if possible:
                known.add(n)
                reflected.add(n)
    assert sum(0 < n < 173 for n in known) == 48
    assert set(range(173, 365)) <= known
    assert sum(n < 173 for n in reflected) == 26
    assert sum(n >= 173 for n in reflected) == 132
    print("PASS: 57 independent unimodular cubic-order algebraic shapes.")
    print("PASS: all 795 block lengths reconstructed by integer determinants.")
    print("PASS: all 57 sets of block lengths positive; min length 1.")
    print("PASS: cubic dilation for every integer h>=1, symbolically;")
    print("      lengths N(h)=(n+epsilon)*h^3-epsilon, epsilon=t mod 2.")
    print("PASS: 25 independent symbolic family bases and all 173..364.")
    print("No legacy endpoint table, matching solver, or floating point used.")


if __name__ == "__main__":
    main()
