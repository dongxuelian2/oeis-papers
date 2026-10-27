"""Exact norm-pruned stationary-collision search for weighted Lucas differences.

For q>=2, the existing proof bounds every nonstationary T_q collision
and locates stationary patterns in a finite 12t window.  The gap norm
C(n)=L_n-1-(-1)^n gives the necessary identity q*q*C(h)=C(e),
where h=k-i, e=ell-j are the two index gaps.  This leaves at most
one e for each h.  A binary search recovers the other starting index.
"""
from argparse import ArgumentParser
from global_collisions import index_cutoff

L = [2, 1]


def ensure(n):
    while len(L) <= n:
        L.append(L[-1] + L[-2])


def gap_norm(n):
    """Positive absolute algebraic norm of phi**n-1, n>=1."""
    if n < 1:
        raise ValueError("gap length must be positive")
    ensure(n)
    return L[n] - 1 - (-1 if n % 2 else 1)


def norm_candidates(q):
    """Gap pairs (h,e) compatible with the proved stationary window."""
    if q < 2:
        raise ValueError("q must be at least 2")
    _, t = index_cutoff(q)
    ensure(7 * t)
    # C(1)=C(2)=1, but the target q^2*C(h)>=4.
    # C(e) is strictly increasing for e>=3.
    inverse = {gap_norm(e): e for e in range(3, 7*t + 1)}
    return t, [(h, inverse[q*q*gap_norm(h)])
               for h in range(1, 3*t)
               if q*q*gap_norm(h) in inverse]


def stationary_T_norm(q):
    """All (i-K,j-K,ell-K) stationary T_q patterns; exact integer test.

    Equivalent to stationary_collisions.stationary_T, using O(t log t)
    index comparisons after Lucas-number generation rather than
    enumerating all triples of indices.
    """
    t, candidates = norm_candidates(q)
    K = 12*t + 1
    ensure(K + t + 2)
    result = []
    for h, e in candidates:
        i = K - h
        target = q * (L[K] - L[i])
        # ell=j+e; K-t<=ell<=K+t; K-6t<=j<ell.
        lo = max(1, K-6*t, K-t-e)
        hi = K+t-e
        if lo > hi:
            continue
        # For e>=3, L[j+e]-L[j] strictly increases with j>=1.
        left, right = lo, hi+1
        while left < right:
            mid = (left+right)//2
            if L[mid+e]-L[mid] < target:
                left = mid+1
            else:
                right = mid
        j = left
        if j > hi or L[j+e]-L[j] != target:
            continue
        ell = j+e
        if (j-i) % 2:
            continue
        if q*(L[K+1]-L[i+1]) != L[ell+1]-L[j+1]:
            continue
        if q*L[K]-L[ell] <= 0:
            continue
        result.append((i-K, j-K, ell-K))
    return sorted(result)


if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("q", type=int)
    args = p.parse_args()
    t, pairs = norm_candidates(args.q)
    print(f"q={args.q}, t={t}, norm candidates={len(pairs)}")
    print("candidate gap pairs:", pairs)
    print("stationary patterns:", stationary_T_norm(args.q))
