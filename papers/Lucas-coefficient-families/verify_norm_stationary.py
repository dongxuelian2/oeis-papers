"""Independent regression audit for the norm-pruned stationary criterion."""
from collections import defaultdict
from norm_stationary import stationary_T_norm, norm_candidates, gap_norm, ensure, L
from global_collisions import index_cutoff


def original_stationary(q):
    """Independent direct two-consecutive-shift dictionary enumeration."""
    _, t = index_cutoff(q)
    K = 12*t + 1
    ensure(K+t+2)
    lookup = defaultdict(list)
    for i in range(K-3*t, K):
        for j in range(K-6*t, K+t+1):
            lookup[(q*L[i]-L[j], q*L[i+1]-L[j+1])].append((i-K,j-K,j))
    found = set()
    for ell in range(K-t, K+t+1):
        value = q*L[K]-L[ell]
        if value <= 0:
            continue
        for di,dj,j in lookup[(value, q*L[K+1]-L[ell+1])]:
            if j < ell:
                found.add((di,dj,ell-K))
    return sorted(found)


def main():
    assert [gap_norm(n) for n in range(1,10)] == [1,1,4,5,11,16,29,45,76]
    infinite = {2,3,4,7,8,11,18,19,21,29,38,47,48,55,76,123,124,144,199}
    found = set()
    candidates_total = 0
    for q in range(2,201):
        t, pairs = norm_candidates(q)
        candidates_total += len(pairs)
        fast = stationary_T_norm(q)
        baseline = original_stationary(q)
        assert fast == baseline, (q, fast, baseline)
        if fast:
            found.add(q)
        K = 12*t+1
        for di,dj,de in fast:
            i,j,ell = K+di,K+dj,K+de
            h,e = K-i,ell-j
            assert q*q*gap_norm(h) == gap_norm(e)
            assert (j-i)%2 == 0
            ensure(max(K, i, j, ell)+6)
            for n in range(5):
                a = q*L[K+n]-L[ell+n]
                b = q*L[i+n]-L[j+n]
                assert a == b > 0, (q,di,dj,de,n)
    assert found == infinite, (found,infinite)
    print("PASS: norm identity and parity for all stationary witnesses")
    print("PASS: exact patterns agree with independent direct search, q=2..200")
    print("PASS: five further shifts of every stationary identity")
    print("PASS: all 19 infinite-collision coefficients in q=2..200")
    print(f"Norm-compatible gap pairs inspected: {candidates_total}")


if __name__ == "__main__":
    main()
