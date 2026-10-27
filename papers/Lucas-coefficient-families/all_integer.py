"""Exact distinct-value and representation algorithms for all integer q.

Lucas indices i,j >= 1. Forms S=L_i-qL_j, T=qL_i-L_j,
P=qL_i+L_j. Values and thresholds are positive integers.
"""
from argparse import ArgumentParser
from bisect import bisect_right
L = [2, 1]

def ensure_value(bound):
    while L[-1] <= bound:
        L.append(L[-1] + L[-2])

def max_index(bound):
    if bound < 1: return 0
    ensure_value(bound)
    return bisect_right(L, bound, lo=1) - 1

def _collect_s_positive(q, X):
    B = (q + 1) * (X + q + 1) + 1
    J = max_index(B)
    I = max_index(X + q * B)
    result = {}
    for i in range(1, I + 1):
        for j in range(1, min(i, J + 1)):
            v = L[i] - q * L[j]
            if 0 < v <= X:
                result.setdefault(v, []).append((i, j))
    return result

def _collect_t_positive(q, X):
    if q == 1: return _collect_s_positive(1, X)
    B = (q + 1) * (X + q + 1) + 1
    I_bound = max(B, X // (q - 1))
    I = max_index(I_bound)
    J = max_index(q * I_bound)
    result = {}
    for i in range(1, I + 1):
        for j in range(1, J + 1):
            v = q * L[i] - L[j]
            if 0 < v <= X:
                result.setdefault(v, []).append((i, j))
    return result

def _collect_p_positive(q, X):
    I = max_index((X - 1) // q)
    J = max_index(X - q)
    result = {}
    for i in range(1, I + 1):
        for j in range(1, J + 1):
            v = q * L[i] + L[j]
            if v <= X:
                result.setdefault(v, []).append((i, j))
    return result

def values(q, form, X):
    """Return value->list of all index pairs; None denotes infinite witnesses."""
    if not isinstance(q, int) or not isinstance(X, int):
        raise TypeError("q and X must be integers")
    if form not in ('S', 'T', 'P'): raise ValueError("form must be S, T, P")
    if X <= 0: return {}
    if q == 0:
        if form == 'T': return {}
        return {L[i]: None for i in range(1, max_index(X) + 1)}
    if q > 0:
        return {'S': _collect_s_positive, 'T': _collect_t_positive,
                'P': _collect_p_positive}[form](q, X)
    m = -q
    if form == 'T': return {}
    if form == 'S':
        return {x: [(j, i) for i, j in reps]
                for x, reps in _collect_p_positive(m, X).items()}
    return {x: [(j, i) for i, j in reps]
            for x, reps in _collect_s_positive(m, X).items()}

def count(q, form, X):
    return len(values(q, form, X))

def nth(q, form, n):
    if n < 1: raise ValueError("n must be >=1")
    if form == 'T' and q <= 0: raise ValueError("T_q is empty for q <= 0")
    hi = 1
    while count(q, form, hi) < n: hi *= 2
    lo = 1
    while lo < hi:
        mid = (lo + hi) // 2
        if count(q, form, mid) >= n: hi = mid
        else: lo = mid + 1
    return lo

if __name__ == '__main__':
    p = ArgumentParser(description=__doc__)
    p.add_argument('form', choices=['S','T','P'])
    p.add_argument('q', type=int)
    p.add_argument('operation', choices=['count','nth','member','witnesses'])
    p.add_argument('value', type=int)
    a = p.parse_args()
    if a.operation == 'count': print(count(a.q, a.form, a.value))
    elif a.operation == 'nth': print(nth(a.q, a.form, a.value))
    elif a.operation == 'member':
        print(a.value in values(a.q, a.form, a.value))
    else: print(values(a.q, a.form, a.value).get(a.value, []))
