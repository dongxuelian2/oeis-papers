"""Exact ingredients of IRRATIONAL_TARGET_ASSESSMENT.md Section 3.1.

For even necessary root valuations, g is computed as it would be under
an integer-square hypothesis. No sampled rotation is asserted square.
"""
from math import gcd


def valuation(n, p):
    assert n != 0
    n = abs(n)
    answer = 0
    while n % p == 0:
        n //= p
        answer += 1
    return answer


counts = {'early': 0, 'balanced': 0, 'ordinary': 0, 'even_root_valuations': 0}
for d in (2, 3):
    B, L = 10**d, 10**(d-1)
    C = B-1
    W = [0]
    for n in range(1, B):
        W.append(W[-1]*10**len(str(n))+n)
    t = sum(len(str(n)) for n in range(1, L))
    G = 10**t
    A = C*C*W[L-1]+L*C+1
    assert valuation(A, 5) == d-1 and t > d
    balanced_floor = (A-B*G)//(C*G)
    balanced = {m for m in (balanced_floor, balanced_floor+1) if L+8 <= m < B}
    endpoints = {L+8, 2*L-1, 2*L, 5*L, B-1} | balanced
    for m in sorted(endpoints):
        N = m-L+1
        for K in sorted({8, max(8, N//2), N-1}):
            if K >= N:
                continue
            k = L+K-1
            J, M = k*C+B, m*C+B
            q, e = divmod(t+d*N, 2)
            Q = 10**q
            R = 10**(t+d*K)*W[m]-(10**(t+d*N)-1)*W[k]
            tail = (G*M-A)*B**K+J
            assert C*C*R == 10**e*J*Q*Q-tail and R > 0
            assert G*M-A != 0 and abs(tail) > B**K-B*B
            assert B**K-B*B > 7*B**3
            assert 4*(10**e*J) < 49*B*B
            assert 4*C*C*R < 49*B*B*Q*Q
            vp = [valuation(J, p) for p in (2, 5)]
            for p, v in zip((2, 5), vp):
                assert valuation(C*C*R, p) == v < d*K
            if all(v % 2 == 0 for v in vp):
                smooth_root = 2**(vp[0]//2)*5**(vp[1]//2)
                g = gcd(smooth_root, Q)
                assert g*g <= J < B*B
                assert abs(tail) > 7*B*g*g
                counts['even_root_valuations'] += 1
            counts['early' if m < 2*L else 'ordinary'] += 1
            if m in balanced:
                counts['balanced'] += 1
assert counts['early'] and counts['balanced'] and counts['even_root_valuations']
print('PASS: full-word identities, valuations and exact gap bounds:', counts)
print('The square-root valuation condition is necessary only; no square rotation is inferred.')
