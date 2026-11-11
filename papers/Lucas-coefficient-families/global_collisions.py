"""Complete positive collision decision for S_q={L_i-q L_j>0}, q>=2.

The proof in main.tex shows that all collision indices are <=6t,
where t is the least index with L_t > 200*(q+1)^4.
The algorithm terminates and is globally exhaustive.
"""
from argparse import ArgumentParser
from collections import defaultdict

L = [2, 1]
def ensure_index(i):
    while len(L) <= i:
        L.append(L[-1]+L[-2])

def index_cutoff(q):
    """Return (6t, t) for any q>=2, with a rigorous universal cutoff."""
    if q < 2:
        raise ValueError("global finite-collision certificate requires q >= 2")
    t = 1
    while True:
        ensure_index(t)
        if L[t] > 200*(q+1)**4:
            return 6*t, t
        t += 1

def complete_collisions(q):
    """Mapping duplicate value -> every pair (i,j); no missing larger indices."""
    limit, _ = index_cutoff(q)
    ensure_index(limit)
    first = {}
    dup = {}
    for i in range(2, limit+1):
        for j in range(1, i):
            v = L[i]-q*L[j]
            if v <= 0:
                break
            if v in dup:
                dup[v].append((i,j))
            elif v in first:
                dup[v] = [first.pop(v),(i,j)]
            else:
                first[v] = (i,j)
    return dict(sorted(dup.items()))

def is_globally_unique(q):
    return not complete_collisions(q)

if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("q", type=int)
    args = p.parse_args()
    cutoff, t = index_cutoff(args.q)
    results = complete_collisions(args.q)
    print(f"q={args.q}; complete upper first-index bound={cutoff} (t={t})")
    print(f"Globally unique: {not bool(results)}; duplicate values: {len(results)}")
    for v, pairs in results.items():
        print(v, pairs)
