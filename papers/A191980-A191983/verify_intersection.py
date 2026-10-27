"""Finite certificate for the positive A191981/A191982 intersection.

The main proof reduces infinite inequalities to consecutive
initial indices i=16,17, because fixed-shift Lucas-linear
expressions satisfy the same second-order recurrence.
"""
from bisect import bisect_right
from intersection import EXCEPTIONS, contains, count, nth

def lucas(n):
    a = [2, 1]
    for _ in range(2, n + 1):
        a.append(a[-1] + a[-2])
    return a

L = lucas(210)

def check_fixed(i):
    R = lambda d, ell: L[i] + L[ell] - 5 * L[i-d]
    for d, ell, lo, hi in ((1,i+2,5,4), (3,i-2,7,6),
                           (4,i-2,5,4), (4,i-6,6,5),
                           (4,i-14,7,6), (5,i-6,5,4),
                           (6,i-14,5,4)):
        assert 5*L[i-lo] < R(d,ell) < 5*L[i-hi], (i,d,ell)
    assert R(3,i-6) < 0
    assert R(5,i-2) > 5*L[i-4]
    assert R(6,i-6) > 5*L[i-4]
    assert R(4,i-10) == 5*L[i-6]
    assert R(6,i-10) == 5*L[i-4]
    # Lower envelopes for ell <= its indicated bound.
    assert L[i] - 5*L[i-4] > 5*L[i-7]
    assert L[i] - 5*L[i-5] > 5*L[i-5]
    assert L[i] - 5*L[i-6] > 5*L[i-5]

def main():
    for i in (16,17):
        check_fixed(i)
    # Additional finite audit; the general proof uses the recurrence.
    for i in range(18,200):
        check_fixed(i)
    N = 180
    S = {}
    for i in range(4,N+1):
        for j in ((1,) if i==4 else range(1,i-3)):
            value = L[i]-5*L[j]
            if value > 0:
                assert value not in S
                S[value] = (i,j)
    T = set()
    for k in range(1,N):
        for ell in range(1,k+4):
            value = 5*L[k]-L[ell]
            if value > 0:
                T.add(value)
    actual = set(S) & T
    expected = set(EXCEPTIONS)
    for n in range(6,N-4):
        expected.add(3*L[n])
        expected.add(8*L[n])
        assert 3*L[n] == L[n+5]-5*L[n+1] == 5*L[n-1]-L[n-5]
        assert 8*L[n] == L[n+5]-5*L[n-1] == 5*L[n+1]-L[n-5]
    assert actual == expected & set(S)
    assert len(actual) == 9+2*(N-10)
    ordered = sorted(actual)
    for x in list(range(-2,10001)) + [L[i] for i in range(6,100)]:
        assert count(x) == bisect_right(ordered,x), x
        assert contains(x) == (x in actual), x
    for n in range(1,160):
        assert nth(n) == ordered[n-1]
    print("PASS: recurrence comparison seeds i=16,17 and audit to i=199")
    print(f"PASS: complete intersection classification through index {N}: {len(actual)} values")
    print("PASS: exact membership, counting and indexing against brute force")

if __name__ == "__main__":
    main()
