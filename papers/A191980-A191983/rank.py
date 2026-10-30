"""Exact A191981 counting, unranking and membership. Python 3.10+, no dependencies."""
from argparse import ArgumentParser
from bisect import bisect_left, bisect_right
from math import isqrt

LUCAS = [2, 1]
BASE = [2, 3, 6, 9]
FIRST_INDEX = {1: 5, 2: 4, 3: 6, 4: 7}

def ensure_index(i: int) -> None:
    while len(LUCAS) <= i:
        LUCAS.append(LUCAS[-1] + LUCAS[-2])

def ensure_above(x: int) -> None:
    while LUCAS[-1] <= x:
        ensure_index(len(LUCAS))

def positive_count(x: int) -> int:
    """Number of positive A191981 values at most x; three partial blocks."""
    if x < 11:
        return bisect_right(BASE, x)
    ensure_above(x)
    m = bisect_right(LUCAS, x, lo=1) - 1
    ensure_index(m + 3)
    total = 1 + (m - 4) * (m - 3) // 2
    for i in range(m + 1, m + 4):
        q = (LUCAS[i] - x - 1) // 5
        below = bisect_right(LUCAS, q, lo=1) - 1
        total += max(0, i - 4 - below)
    return total

def published_count(x: int) -> int:
    return (1 if x >= 0 else 0) + positive_count(x)

def nth_positive(n: int) -> int:
    if n < 1:
        raise ValueError("positive index must be >= 1")
    N = max(4, (7 + isqrt(8 * n - 7)) // 2)
    def prefix(i: int) -> int:
        return 1 + (i - 4) * (i - 3) // 2
    while prefix(N) < n:
        N += 1
    while N > 4 and prefix(N - 1) >= n:
        N -= 1
    ensure_index(N)
    lo, hi = 0, LUCAS[N]
    while lo < hi:
        mid = (lo + hi) // 2
        if positive_count(mid) < n:
            lo = mid + 1
        else:
            hi = mid
    return lo

def nth_published(n: int) -> int:
    if n < 1:
        raise ValueError("OEIS offset is 1")
    return 0 if n == 1 else nth_positive(n - 1)

def residue_cumulative(r: int, k: int) -> int:
    if k < 0:
        return 0
    if r == 1:
        return (k + 1) * (2 * k + 1)
    if r == 2:
        return 1 + 2 * k * (k + 1)
    if r == 3:
        return 2 * (k + 1) ** 2
    if r == 4:
        return (k + 1) * (2 * k + 3)
    raise ValueError("residue must be 1, 2, 3, or 4")

def nth_residue(r: int, n: int) -> int:
    """1-based rank within the values congruent to r modulo 5."""
    if r not in FIRST_INDEX or n < 1:
        raise ValueError("residue must be 1..4 and index >= 1")
    lo, hi = 0, 1
    while residue_cumulative(r, hi) < n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if residue_cumulative(r, mid) < n:
            lo = mid + 1
        else:
            hi = mid
    k = lo
    i = FIRST_INDEX[r] + 4 * k
    t = n - residue_cumulative(r, k - 1)
    j = 1 if (r == 2 and k == 0) else i - 3 - t
    ensure_index(i)
    return LUCAS[i] - 5 * LUCAS[j]

def representation(x: int) -> tuple[int, int] | None:
    """Unique (i,j) for x=L_i-5*L_j; None for nonmembers."""
    if x <= 0 or x % 5 == 0:
        return None
    i = FIRST_INDEX[x % 5]
    ensure_index(i)
    while LUCAS[i] - 5 < x:
        i += 4
        ensure_index(i)
    target = LUCAS[i] - x
    if target % 5:
        return None
    q = target // 5
    if i == 4:
        return (4, 1) if q == 1 else None
    j = bisect_left(LUCAS, q, lo=1, hi=i - 3)
    return (i, j) if j <= i - 4 and LUCAS[j] == q else None

if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("operation", choices=["count", "nth", "member", "residue"])
    p.add_argument("value", type=int)
    p.add_argument("--mod5", type=int, choices=[1,2,3,4], default=1)
    a = p.parse_args()
    if a.operation == "count":
        print(published_count(a.value))
    elif a.operation == "nth":
        print(nth_published(a.value))
    elif a.operation == "member":
        print(representation(a.value))
    else:
        print(nth_residue(a.mod5, a.value))
