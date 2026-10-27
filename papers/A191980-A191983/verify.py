"""Exact-integer checks for the A191981 note. Run: python verify.py"""
from collections import defaultdict

OEIS_FIRST_57 = [
    0, 2, 3, 6, 9, 12, 13, 14, 21, 24, 27, 32, 33, 41, 42,
    54, 56, 61, 68, 71, 87, 88, 103, 108, 109, 118, 141,
    144, 164, 177, 179, 184, 194, 228, 232, 267, 286,
    287, 302, 307, 317, 369, 376, 431, 463, 466, 486,
    501, 506, 516, 597, 608, 698, 749, 753, 788, 808,
]

def lucas_up_to(n: int) -> list[int]:
    terms = [2, 1]
    while len(terms) <= n:
        terms.append(terms[-1] + terms[-2])
    return terms

def main() -> None:
    N = 80
    L = lucas_up_to(N)
    witnesses: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            d = L[i] - 5 * L[j]
            expected_positive = (i == 4 and j == 1) or (i >= 5 and j <= i - 4)
            assert (d > 0) == expected_positive, (i, j, d)
            if d > 0:
                witnesses[d].append((i, j))
    assert all(len(w) == 1 for w in witnesses.values())
    assert all(k % 5 for k in witnesses)
    actual = [0] + sorted(witnesses)
    assert actual[:len(OEIS_FIRST_57)] == OEIS_FIRST_57
    for n in range(4, N + 1):
        restricted = {d for d, [(i, j)] in witnesses.items() if i <= n}
        assert len(restricted) == 1 + (n - 4) * (n - 3) // 2
    for i in range(5, N + 1):
        assert L[i] - 5 * L[i - 4] == 3 * L[i - 5]
        assert L[i - 1] * 3 > L[i]
    for i in range(4, N - 3):
        lo_next = L[i + 4] - 5 * L[i]
        hi_this = L[i] - 5
        assert lo_next > hi_this

    # Exact rank, unranking, membership and adjacent sequence prefixes.
    from bisect import bisect_right
    from rank import (positive_count, published_count, nth_positive,
                      nth_published, nth_residue, residue_cumulative,
                      representation)
    observed = sorted(witnesses)
    for x in range(-2, 4000):
        assert positive_count(x) == bisect_right(observed, x), x
        assert published_count(x) == (x >= 0) + bisect_right(observed, x), x
    for n in range(1, 450):
        assert nth_published(n) == ([0] + observed)[n - 1], n
        assert nth_positive(n) == observed[n - 1], n
    for residue in (1, 2, 3, 4):
        part = [a for a in observed if a % 5 == residue]
        for n in range(1, 150):
            assert nth_residue(residue, n) == part[n - 1], (residue, n)
        initial = {1: 5, 2: 4, 3: 6, 4: 7}[residue]
        for k in range(12):
            direct = sum(1 for a, [(i, j)] in witnesses.items()
                         if a % 5 == residue and i <= initial + 4 * k)
            assert residue_cumulative(residue, k) == direct
    for x in range(1, 10000):
        assert (representation(x) is not None) == (x in witnesses), x
    for x, pairs in list(witnesses.items())[:750]:
        assert representation(x) == pairs[0]
    for n in (1, 2, 10, 100, 1000, 10000):
        a = nth_positive(n)
        assert positive_count(a) == n and positive_count(a - 1) == n - 1

    B_PREFIX = [
        0,1,2,4,6,8,9,11,12,13,14,16,17,19,22,24,26,28,31,32,34,
        36,37,43,44,48,51,52,54,58,61,69,72,79,83,86,87,89,94,98,
        112,116,127,134,138,141,142,144,152,159,181,188,206,217,
        224,228,231,232,234,246,257,
    ]
    U_PREFIX = [
        0,1,2,3,4,6,8,9,11,12,13,14,16,17,19,21,22,24,26,27,28,
        31,32,33,34,36,37,41,42,43,44,48,51,52,54,56,58,61,68,
        69,71,72,79,83,86,87,88,89,94,98,103,108,109,112,116,
        118,127,134,138,141,142,144,152,
    ]
    B = {5 * L[i] - L[j] for i in range(1, N + 1)
         for j in range(1, N + 1) if 5 * L[i] > L[j]}
    assert [0] + sorted(B)[:len(B_PREFIX)-1] == B_PREFIX
    assert sorted({0} | set(witnesses) | B)[:len(U_PREFIX)] == U_PREFIX
    assert 5 * L[1] - L[2] == 5 * L[3] - L[6] == 2
    assert 5 * L[1] - L[1] == 5 * L[2] - L[5] == 4
    for n in range(6, N - 5):
        v = 3 * L[n]
        assert v == L[n + 5] - 5 * L[n + 1] == 5 * L[n - 1] - L[n - 5]
        assert v in witnesses and v in B
    for n in range(5, N - 6):
        v = L[n + 6] - 5 * L[n]
        assert v == 5 * L[n + 2] - L[n - 4]
        assert v in witnesses and v in B
    print("PASS: exact three-block rank and four quadratic residue streams")
    print("PASS: exact nth terms, membership and A191982/A191983 published prefixes")
    print("PASS: two proved infinite intersection identities; finite samples checked")
    print(f"PASS: first {len(OEIS_FIRST_57)} OEIS terms match")
    print(f"PASS: positivity, uniqueness, residue and finite count for 1 <= i,j <= {N}")
    print(f"PASS: {len(witnesses)} distinct positive differences")

if __name__ == "__main__":
    main()
