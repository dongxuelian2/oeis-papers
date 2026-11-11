"""Independent exact-integer verification of OEIS A191980."""
from collections import defaultdict
from bisect import bisect_right
from sums import COLLISIONS, count_pairs, count, nth, representations

OEIS_PREFIX = [
    6,8,9,12,16,18,19,21,22,23,24,26,27,31,33,34,36,38,39,42,
    44,46,49,52,53,56,58,59,62,64,66,67,73,81,82,84,91,93,94,
    96,97,101,102,108,111,119,128,131,137,138,143,146,148,149,
    152,156,158,163,166,174,
]
def lucas(n):
    L = [2,1]
    for i in range(2,n+1):
        L.append(L[i-1]+L[i-2])
    return L

def main():
    N = 120
    L = lucas(N)
    witnesses = defaultdict(list)
    for i in range(1,N+1):
        for j in range(1,N+1):
            witnesses[5*L[i]+L[j]].append((i,j))
    values = sorted(witnesses)
    assert values[:len(OEIS_PREFIX)] == OEIS_PREFIX
    repeated = {x:ps for x,ps in witnesses.items() if len(ps)>1}
    expected = {
        16:[(1,5),(2,1)], 23:[(1,6),(3,2)],
        38:[(3,6),(4,2)], 62:[(2,8),(5,4)],
        91:[(2,9),(6,1)],
    }
    assert repeated == expected, repeated
    sums_with_repetition = sorted(x for x,ps in witnesses.items() for _ in ps)
    for x in list(range(-2,10000)) + [L[i] for i in range(2,N+1)]:
        assert count_pairs(x) == bisect_right(sums_with_repetition, x),x
        assert count(x) == bisect_right(values,x),x
    for n in list(range(1,501)) + [1000,3000,8000,12000]:
        assert nth(n) == values[n-1],n
    for x in range(0,10000):
        assert sorted(representations(x)) == sorted(witnesses.get(x,[])),x
    for x in (5*L[90]+L[45],5*L[100]+L[120],5*L[5]+L[111]):
        assert sorted(representations(x)) == sorted(witnesses[x]),x

    # Identity yields two infinite A191980/A191982 overlap families.
    for n in range(4,N-7):
        assert 5*(L[n+4]-L[n]) == L[n+7]+L[n-3]
        assert 5*L[n]+L[n+7] == 5*L[n+4]-L[n-3] > 0
        assert 5*L[n]+L[n-3] == 5*L[n+4]-L[n+7] > 0
    family_u = {5*L[n]+L[n+7] for n in range(4,N-7)}
    family_v = {5*L[n]+L[n-3] for n in range(4,N-7)}
    assert family_u.isdisjoint(family_v)
    assert len(family_u)==N-11 and len(family_v)==N-11
    print('PASS: 60 OEIS A191980 terms and five collisions among 120^2 representations')
    print('PASS: exact counting, nth terms and membership witnesses')
    print('PASS: two infinite overlap identities, tested through n=112')

if __name__ == '__main__':
    main()
