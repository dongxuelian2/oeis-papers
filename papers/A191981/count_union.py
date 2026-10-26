"""Exact A191982 and A191983 rank/count via five collision corrections."""
from argparse import ArgumentParser
from bisect import bisect_left, bisect_right
from rank import LUCAS, ensure_above, ensure_index, positive_count
from intersection import count as intersection_count

COLLISIONS = (2, 4, 8, 14, 17)

def positive_pair_count(x: int) -> int:
    """Count positive pairs (k, ell) with 5*L_k-L_ell <= x."""
    if x < 1:
        return 0
    total = 0
    k = 1
    while True:
        ensure_index(k+3)
        if k >= 3 and 2*LUCAS[k-2] > x:
            break
        b = 3 if k == 1 else k+3
        threshold = 5*LUCAS[k]-x-1
        excluded = bisect_right(LUCAS, threshold, lo=1, hi=b+1)-1
        total += b-excluded
        k += 1
    return total

def count_A191982_positive(x: int) -> int:
    return positive_pair_count(x) - bisect_right(COLLISIONS, x)

def count_A191982(x: int) -> int:
    return int(x >= 0) + count_A191982_positive(x)

def count_A191983(x: int) -> int:
    """Number of nonnegative union terms <= x."""
    return (int(x >= 0) + positive_count(x)
            + count_A191982_positive(x) - intersection_count(x))

def _unrank(count, n):
    if n < 1:
        raise ValueError("OEIS indexing begins at 1")
    hi = 1
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

def nth_A191982(n: int) -> int:
    return _unrank(count_A191982, n)

def nth_A191983(n: int) -> int:
    return _unrank(count_A191983, n)

if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("t-count","t-nth","union-count","union-nth"))
    parser.add_argument("value", type=int)
    a = parser.parse_args()
    print({
        "t-count":count_A191982,
        "t-nth":nth_A191982,
        "union-count":count_A191983,
        "union-nth":nth_A191983,
    }[a.operation](a.value))
