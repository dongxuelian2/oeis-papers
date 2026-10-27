"""Exact-integer audit of the A191982 collision and A191983 counting claims."""
from bisect import bisect_right
from collections import defaultdict

def lucas_up_to(n):
    terms = [2, 1]
    while len(terms) <= n:
        terms.append(terms[-1]+terms[-2])
    return terms
from count_union import (
    COLLISIONS, positive_pair_count, count_A191982_positive,
    count_A191982, count_A191983, nth_A191982, nth_A191983,
)
from intersection import count as intersection_count

OEIS_T = [
    0,1,2,4,6,8,9,11,12,13,14,16,17,19,22,24,26,28,31,32,34,
    36,37,43,44,48,51,52,54,58,61,69,72,79,83,86,87,89,94,98,
    112,116,127,134,138,141,142,144,152,159,181,188,206,217,224,
    228,231,232,234,246,257,
]
OEIS_U = [
    0,1,2,3,4,6,8,9,11,12,13,14,16,17,19,21,22,24,26,27,28,
    31,32,33,34,36,37,41,42,43,44,48,51,52,54,56,58,61,68,69,
    71,72,79,83,86,87,88,89,94,98,103,108,109,112,116,118,
    127,134,138,141,142,144,152,
]

def main():
    N = 160
    L = lucas_up_to(N+3)
    pairs = defaultdict(list)
    for k in range(1,N+1):
        for ell in range(1,(3 if k==1 else k+3)+1):
            v = 5*L[k]-L[ell]
            assert v > 0
            pairs[v].append((k,ell))
    D = {v: ps for v,ps in pairs.items() if len(ps)>1}
    expected = {
        4:[(1,1),(2,5)], 2:[(1,2),(3,6)],
        8:[(2,4),(5,8)], 14:[(2,1),(6,9)],
        17:[(3,2),(4,6)],
    }
    assert D == expected
    # Check the comparison identities used to eliminate all k >= 4.
    for k in range(4,N-6):
        assert 2*L[k+2] > 5*L[k]-1
        assert L[k+2] < 5*L[k-1] < L[k+4]
        assert 3*L[k-2] > L[k-1]
        assert L[k+4]-5*L[k-1] > L[k]
        assert L[k+4] < 5*L[k+1]
        assert L[k+5]-5*L[k+1] == 3*L[k] > L[k+1]
        assert L[k+5] < 10*L[k+1]
        R = L[k+6]-10*L[k+1]
        assert L[k-2] < R < L[k+2]
    S = {L[i]-5*L[j] for i in range(1,N+1)
         for j in range(1,N+1) if L[i]-5*L[j]>0}
    T = sorted(pairs)
    U = sorted(S | set(T))
    assert [0]+T[:len(OEIS_T)-1] == OEIS_T
    assert [0]+U[:len(OEIS_U)-1] == OEIS_U
    # x up to L_110 has all contributing first indices <= N.
    for x in list(range(-3,9001)) + [L[i] for i in range(4,111)]:
        assert positive_pair_count(x) == sum(
            len(ps) for v,ps in pairs.items() if v<=x), x
        assert count_A191982_positive(x) == bisect_right(T,x),x
        assert count_A191982(x) == int(x>=0)+bisect_right(T,x),x
        assert count_A191983(x) == int(x>=0)+bisect_right(U,x),x
    for n in range(1,900):
        assert nth_A191982(n) == ([0]+T)[n-1],n
        assert nth_A191983(n) == ([0]+U)[n-1],n
    assert all(len(ps)==2 for ps in D.values())
    print("PASS: complete five-collision classification, 160 index blocks")
    print("PASS: OEIS A191982 (61) and A191983 (63) terms")
    print("PASS: exact positive pair/unique count and union rank inversion")

if __name__ == "__main__":
    main()
