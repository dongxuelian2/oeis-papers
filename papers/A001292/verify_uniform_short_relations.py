#!/usr/bin/env python3
"""Finite exact audits of the short-relation lemma; not a search for squares."""
from fractions import Fraction
from functools import lru_cache
from math import factorial, gcd, isqrt
from itertools import product
from pathlib import Path
import json


def iroot4(n):
    return isqrt(isqrt(n))


@lru_cache(None)
def squareclass(n):
    a, s, p = 1, 1, 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        a *= p**(e//2)
        s *= p**(e % 2)
        p += 1
    return a, s*n


def valuation2(n):
    return (n & -n).bit_length()-1


def run():
    counts = dict(identity_samples=0, early_bound_samples=0,
                  late_bound_samples=0, vacuous_radius_samples=0,
                  rational_root_local_samples=0, synthetic_local_samples=0,
                  eta_threshold_samples=0, moving_counterexample_samples=0,
                  denominator_clearing_samples=0)
    for d in (2, 3):
        B, L = 10**d, 10**(d-1)
        C = B-1
        words = [0]
        for n in range(1, B):
            words.append(words[-1]*10**len(str(n))+n)
        t = sum(len(str(n)) for n in range(1, L))
        G = 10**t
        A = C*C*words[L-1]+L*C+1
        assert t >= 9 and t < d*L and 8*A < G*B*B
        endpoints = range(2*L, B) if d == 2 else (2*L, 2*L+1, 5*L//2, 5*L, B-1)
        for m in endpoints:
            N, M = m-L+1, m*C+B
            assert N >= L+1 and 5*M > B*B
            q, e = divmod(t+d*N, 2)
            Q = 10**q
            assert 2*q >= d*N and q <= d*N
            assert 10**e*Q*Q == G*B**N
            cuts = range(8, N) if d == 2 else sorted({8, 9, N//2-1, N//2, N//2+1, N-1})
            for K in cuts:
                if not 8 <= K < N:
                    continue
                k, J = L+K-1, (L+K-1)*C+B
                a, s = squareclass(J)
                assert a*a*s == J < B*B
                T = (G*M-A)*B**K+J
                F = G*J*B**(N-K)+A-G*M
                R = 10**(t+d*K)*words[m]-(10**(t+d*N)-1)*words[k]
                assert C*C*R == G*J*B**N-T
                assert C*C*R+J == F*B**K
                assert 0 < T < 2*G*B**(K+2) and F > 0
                counts['identity_samples'] += 1
                if isqrt(10**e*s)**2 == 10**e*s:
                    assert (s,e) in ((1,0),(10,1))
                    r = valuation2(J)
                    assert r < 7*d < d*K
                    if s == 10:
                        assert r % 2 == 1
                    else:
                        assert r == 2*valuation2(a) and d*K-r >= 3
                        assert all((u*u+v*v) % 8 != 0 for u in (1,3,5,7) for v in (1,3,5,7))
                    counts['rational_root_local_samples'] += 1
                if N < 12:
                    counts['vacuous_radius_samples'] += 1
                    continue
                # Largest integer W <= B^(N/4-3), with no floating-point arithmetic.
                W = iroot4(B**(N-12))
                assert W**4 <= B**(N-12) < (W+1)**4
                assert W < Q
                assert W*W*B**6 <= Q
                assert 2*(2*W*W*Q+W*W) < Q*Q
                if 2*K <= N:
                    assert 2*W*W*T < Q*Q
                    assert 40 < B**4
                    counts['early_bound_samples'] += 1
                else:
                    D = gcd(B**K, Q)
                    assert D*D >= B**N
                    assert 2*B**4*W*W < D
                    # The congruence used in the proof is exact for all b_i;
                    # small test coefficients audit its implementation.
                    for b1,b2,b3 in ((1,2,3),(-2,1,-3),(3,-2,0)):
                        remainder = a*a*((b2*Q+b3)**2+s*b1*b1)-a*a*(b3*b3+s*b1*b1)
                        assert remainder % D == 0
                    counts['late_bound_samples'] += 1
    # Actual cut samples need not include either exceptional squareclass.
    # Audit the local contradiction ingredients independently for all small a.
    for d in (2,3):
        B, K = 10**d, 8
        for s,e in ((1,0),(10,1)):
            for a in range(1,isqrt((B*B-1)//s)+1):
                J = a*a*s
                r = valuation2(J)
                assert J < B*B and r < 7*d < d*K
                assert isqrt(10**e*s)**2 == 10**e*s
                if s == 10:
                    assert r % 2 == 1
                else:
                    assert r == 2*valuation2(a) and d*K-r >= 3
                    assert all((u*u+v*v) % 8 != 0 for u in (1,3,5,7) for v in (1,3,5,7))
                counts['synthetic_local_samples'] += 1
    for eta in (Fraction(1,100),Fraction(1,10),Fraction(1,5),Fraction(6,25)):
        for N in range(13, 2001):
            if (Fraction(1,4)-eta)*N >= 3+Fraction(3,2)*eta:
                assert eta*(N+Fraction(3,2)) <= Fraction(N,4)-3
                counts['eta_threshold_samples'] += 1
    for r in range(3,8):
        n, Q = 10**r, 10**factorial(r)
        x,y,z = n*Q+1,Q,n
        assert gcd(gcd(x,y),z) == 1
        assert x-n*y == 1 and x-Fraction(z,n) == n*Q
        assert x-n*y-Fraction(z,n) == 0
        arch = (x-n*y)*y*z
        local_both = Fraction(1,(x-Fraction(z,n))*y*z)
        combined = arch*local_both
        assert combined == Fraction(1,n*Q)
        assert combined*combined*x <= 1
        counts['moving_counterexample_samples'] += 1
    rationals = (Fraction(0),Fraction(1),Fraction(-2,3),Fraction(7,5),Fraction(-11,13))
    for coeffs in product(rationals,repeat=3):
        if not any(coeffs):
            continue
        M = max(max(abs(c.numerator),c.denominator) for c in coeffs)
        denominator = coeffs[0].denominator*coeffs[1].denominator*coeffs[2].denominator
        integers = [c*denominator for c in coeffs]
        assert all(c.denominator == 1 for c in integers)
        assert 0 < max(abs(c) for c in integers) <= M**3
        counts['denominator_clearing_samples'] += 1
    target = Path(__file__).with_name('uniform-short-relations-certificate.json')
    target.write_text(json.dumps(counts,indent=2)+'\n')
    print(json.dumps(counts,indent=2))
    print('PASS. Finite ingredient checks only; no square solutions or exceptional subspaces computed.')


if __name__ == '__main__':
    run()
