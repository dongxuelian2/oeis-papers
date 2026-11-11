"""Complete positive intersection of OEIS A191981 and A191982."""
from argparse import ArgumentParser
from bisect import bisect_left, bisect_right

from rank import LUCAS, ensure_above, ensure_index

EXCEPTIONS = (2, 6, 9, 12, 13, 14, 24, 32, 61)

def _index_of_lucas(value: int) -> int | None:
    if value < 1:
        return None
    ensure_above(value)
    i = bisect_left(LUCAS, value, lo=1)
    return i if i < len(LUCAS) and LUCAS[i] == value else None

def contains(x: int) -> bool:
    """Whether x belongs to the positive intersection (not the artificial zero)."""
    if x in EXCEPTIONS:
        return True
    for factor in (3, 8):
        if x > 0 and x % factor == 0:
            i = _index_of_lucas(x // factor)
            if i is not None and i >= 6:
                return True
    return False

def count(x: int) -> int:
    """Exact number of positive intersection values <= x."""
    if x < 0:
        return 0
    ensure_index(6)
    ensure_above(x // 3)
    return (bisect_right(EXCEPTIONS, x)
            + max(0, bisect_right(LUCAS, x // 3, lo=6) - 6)
            + max(0, bisect_right(LUCAS, x // 8, lo=6) - 6))

def nth(n: int) -> int:
    """n-th positive intersection value, indexed from 1."""
    if n < 1:
        raise ValueError("index must be >= 1")
    hi = 1
    while count(hi) < n:
        hi *= 2
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if count(mid) < n:
            lo = mid + 1
        else:
            hi = mid
    return lo

if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("operation", choices=("count", "nth", "member"))
    p.add_argument("value", type=int)
    a = p.parse_args()
    print({"count": count, "nth": nth, "member": contains}[a.operation](a.value))
