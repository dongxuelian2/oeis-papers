"""Explicit exhaustive infinite-collision classification for weighted Lucas sums.

The coefficient theorem in main.tex replaces the large stationary-pattern
search with three necessary-and-sufficient arithmetic families. The earlier
12t stationary certificate supplies a finite index bound for testing family
membership: m <= floor(7t/2), r < 3t/2, with
t = min{n>=1: Lucas(n)>200*(q+1)^4}.
"""
from argparse import ArgumentParser
from global_collisions import index_cutoff

L = [2, 1]
F = [0, 1]


def ensure(n):
    while len(L) <= n:
        L.append(L[-1] + L[-2])
        F.append(F[-1] + F[-2])


def coefficient_witnesses(q):
    """Complete finite list of quotient/half-Lucas witnesses for q>=2.

    Each witness is ('Lucas quotient', m, r),
    ('Fibonacci quotient', m, r), or ('half Lucas', m, None).
    """
    if q < 2:
        raise ValueError("q must be >=2")
    _, t = index_cutoff(q)
    max_m = (7*t)//2
    max_r = (3*t-1)//2
    ensure(max_m)
    witnesses = []
    for m in range(2, max_m+1):
        if m % 6 == 3 and L[m] == 2*q:
            witnesses.append(("half Lucas", m, None))
        sequence = L if m % 2 else F
        for r in range(1, min(m-1, max_r)+1):
            if r % 2 != m % 2:
                continue
            if sequence[m] == q*sequence[r]:
                witnesses.append(("Lucas quotient" if m % 2 else
                                  "Fibonacci quotient", m, r))
    return witnesses


def infinite_T(q):
    """True precisely if T_q or P_q has infinite collisions, q>=2."""
    return bool(coefficient_witnesses(q))


def infinite_collision(q, form):
    """Exact all-integer q infinity decision for S/T/P."""
    if form not in ("S", "T", "P"):
        raise ValueError("form must be S, T, or P")
    if q == 0:
        return form != "T"
    if q == 1:
        return True
    if q >= 2:
        return False if form == "S" else infinite_T(q)
    if form == "T":
        return False
    if q == -1:
        return True
    return infinite_T(-q) if form == "S" else False


if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("q", type=int)
    p.add_argument("form", choices=("S", "T", "P"))
    a = p.parse_args()
    print(f"q={a.q}, {a.form}: infinite collisions = "
          f"{infinite_collision(a.q, a.form)}")
    if a.q >= 2 and a.form in ("T", "P"):
        print("explicit coefficient witnesses:", coefficient_witnesses(a.q))
