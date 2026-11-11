"""Exact A191980 counting, membership and unranking; Lucas L_1=1.

Run: python sums.py count 10000
     python sums.py nth 500
     python sums.py representations 62
"""
from argparse import ArgumentParser
from bisect import bisect_left, bisect_right

LUCAS = [2, 1]
COLLISIONS = (16, 23, 38, 62, 91)

def ensure_above(x: int) -> None:
    while LUCAS[-1] <= x:
        LUCAS.append(LUCAS[-2] + LUCAS[-1])

def count_pairs(x: int) -> int:
    """Number of ordered pairs (i,j)>=1 satisfying 5 L_i + L_j <= x."""
    if x < 6:
        return 0
    ensure_above(x)
    k_max = bisect_right(LUCAS, (x - 1) // 5, lo=1) - 1
    return sum(bisect_right(LUCAS, x-5*LUCAS[i], lo=1) - 1
               for i in range(1, k_max+1))

def count(x: int) -> int:
    """Number of DISTINCT A191980 terms <= x."""
    return count_pairs(x) - bisect_right(COLLISIONS, x)

def nth(n: int) -> int:
    """OEIS A191980 term with index n>=1."""
    if n < 1:
        raise ValueError("OEIS index must be >= 1")
    hi = 6
    while count(hi) < n:
        hi *= 2
    lo = 0
    while lo < hi:
        mid = (lo+hi)//2
        if count(mid) >= n:
            hi = mid
        else:
            lo = mid+1
    return lo

def representations(x: int) -> list[tuple[int,int]]:
    """Every exact witness (i,j) for x=5L_i+L_j; at most two."""
    if x < 6 or x % 5 == 0:
        return []
    ensure_above(x)
    j_max = bisect_right(LUCAS, x-5, lo=1) - 1
    answer = []
    for j in range(1, j_max+1):
        if LUCAS[j] % 5 != x % 5:
            continue
        q = (x-LUCAS[j]) // 5
        i = bisect_left(LUCAS, q, lo=1)
        if i < len(LUCAS) and LUCAS[i] == q:
            answer.append((i,j))
    return answer

if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("operation", choices=("count", "pairs", "nth", "representations"))
    p.add_argument("value", type=int)
    a = p.parse_args()
    print({"count":count, "pairs":count_pairs,
           "nth":nth, "representations":representations}[a.operation](a.value))
