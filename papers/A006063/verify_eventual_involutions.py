#!/usr/bin/env python3
"""Independent exact interval certificate for eventual minimal-fixed-point cube-sum involutions.

The source seed at length 7 is p(i)=8-i (fixes 4 only), and at length
26 it is p(i)=27-i (no fixed point). Only odd-cube suffix reflections
are allowed, so each new block is fixed-point-free and parity is preserved.

This program operates on unions of integer intervals in the parity
coordinate t=(n-parity)/2, not a matching solver or permutation archive.
"""

CASES = [
    # (seed, max checked length, target start, required rounds, length of final union)
    (7, 100001, 69603, 13, None),
    (26, 303412, 228028, 12, 7047),
]


def merge(intervals):
    result = []
    for a, b in sorted(intervals):
        assert 0 <= a <= b
        if result and a <= result[-1][1] + 1:
            result[-1][1] = max(result[-1][1], b)
        else:
            result.append([a, b])
    return result


def closure(seed, cap, rounds):
    parity = seed & 1
    cap_t = (cap - parity) // 2
    constants = []
    for k in range(3, 300, 2):
        if k**3 > 2 * cap:
            break
        constants.append((k**3 - 1 - 2*parity)//2)
    intervals = [[(seed-parity)//2]*2]
    for _ in range(rounds):
        additional = intervals.copy()
        for a,b in intervals:
            for d in constants:
                source_lo = max(a, d-cap_t)
                source_hi = min(b, (d-1)//2)
                if source_lo <= source_hi:
                    additional.append([d-source_hi, d-source_lo])
        intervals = merge(additional)
    return intervals


def main():
    for seed, cap, target, depth, num_intervals in CASES:
        p = seed & 1
        intervals = closure(seed, cap, depth)
        if num_intervals is not None:
            assert len(intervals) == num_intervals, (seed, len(intervals))
        target_t, cap_t = (target-p)//2, (cap-p)//2
        assert any(a <= target_t and cap_t <= b for a,b in intervals)
        trailing = next((2*a+p,2*b+p) for a,b in intervals if a <= target_t <= b)
        print(f'PASS seed={seed}, {depth} rounds, {len(intervals)} intervals; '
              f'last interval={trailing}, covers target [{target},{cap}] in its parity')

    # The least odd cube k^3 >= n + start + 1 gives m=k^3-n-1.
    # For n>cap, k is at least 57 (odd) or 83 (even). The exact
    # sharp endpoint lower bounds follow by comparing to (k-2)^3.
    for minimum_root, minimum_start, checked_cap in ((57,69603,100001),(83,228028,303412)):
        k = minimum_root
        assert checked_cap + 2 + minimum_start + 1 > (k-2)**3
        value = 2*(k-2)**3-k**3-2*minimum_start
        assert value > 0
        # For k>=57, f(k)=2(k-2)^3-k^3-2M increases.
        assert 6*k*k-36*k+8 > 0  # f(k+2)-f(k)
        print(f'PASS lower bound at k={k}: 2*(k-2)^3-k^3-2*M={value}>0')
    print('THEOREM: odd n>=69603: exactly one fixed point (4); '
          'even n>=228028: fixed-point-free involution.')


if __name__ == '__main__':
    main()