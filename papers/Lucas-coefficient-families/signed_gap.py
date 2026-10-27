"""Complete signed Lucas-gap collision spectra for all q>=2.

For D(a,b)=L_b-L_a, a<b, suppose D(a,b)=q D(c,d).
Let Delta=L_a L_d-L_b L_c. Then:
  Delta>0: an S_q positive collision;
  Delta<0: a T_q positive collision;
  any Delta: a P_q positive collision.
Every collision in the corresponding form arises this way.

The existing global collision and stationary theorems guarantee a
representative with all four indices <= N=13*t+1, where t is the
least positive index with L_t>200*(q+1)**4. This includes coefficients
with infinite T/P collision families, through their finite stationary
witness at k=12*t+1. The default routine is consequently exhaustive.
"""
from argparse import ArgumentParser
from global_collisions import index_cutoff

L = [2, 1]


def ensure(n):
    while len(L) <= n:
        L.append(L[-1] + L[-2])


def signed_gap_witnesses(q, limit=None):
    """One (a,b,c,d,Delta) witness for each available sign +1,-1,0.

    A custom 'limit' permits truncated experiments; omit it for the
    proved whole-infinite-sequence decision.
    """
    if q < 2:
        raise ValueError("q must be >= 2")
    _, t = index_cutoff(q)
    N = 13*t+1 if limit is None else limit
    ensure(N)
    gaps = {}
    for b in range(2, N+1):
        for a in range(1, b):
            gaps.setdefault(L[b]-L[a], []).append((a,b))
    witnesses = {}
    for small, denominator_pairs in gaps.items():
        numerator_pairs = gaps.get(q*small)
        if numerator_pairs is None:
            continue
        for a,b in numerator_pairs:
            for c,d in denominator_pairs:
                delta = L[a]*L[d]-L[b]*L[c]
                sign = (delta > 0) - (delta < 0)
                if sign not in witnesses:
                    witnesses[sign] = (a,b,c,d,delta)
                if len(witnesses) == 3:
                    return witnesses
    return witnesses


def collision_flags(q):
    """Presence of at least one positive collision of each form."""
    signs = signed_gap_witnesses(q)
    return {"S": 1 in signs, "T": -1 in signs, "P": bool(signs)}


if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("q", type=int)
    args = p.parse_args()
    t = index_cutoff(args.q)[1]
    print(f"q={args.q}, complete index cutoff={13*t+1}")
    witnesses = signed_gap_witnesses(args.q)
    for sign, pair in sorted(witnesses.items()):
        print(f"Delta sign {sign:+d}: {pair}")
    print("collision flags:", {"S": 1 in witnesses,
                              "T": -1 in witnesses, "P": bool(witnesses)})
