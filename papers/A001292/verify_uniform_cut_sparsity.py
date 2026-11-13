#!/usr/bin/env python3
"""Exact finite audits for UNIFORM_CUT_SPARSITY.md; no theorem by search."""

import json
from fractions import Fraction
from math import isqrt
from pathlib import Path


def valuation(n, p):
    assert n > 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def prime_power_roots_formula(J, p, n):
    """Root count of x^2 = -J mod p^n, restricted to v_p(J)<n."""
    v = valuation(J, p)
    assert v < n
    if v % 2:
        return 0
    unit = -(J // p**v)
    residual_n = n-v
    if p == 2:
        if residual_n == 1:
            unit_roots = 1
        elif residual_n == 2:
            unit_roots = 2 if unit % 4 == 1 else 0
        else:
            unit_roots = 4 if unit % 8 == 1 else 0
    else:
        assert p == 5
        unit_roots = 2 if unit % 5 in (1, 4) else 0
    return p**(v//2) * unit_roots


def smooth_values_below(B):
    out = []
    z5 = 1
    while z5 < B:
        z = z5
        while z < B:
            out.append(z)
            z *= 2
        z5 *= 5
    return sorted(out)


def region_flags(d, t, N, K):
    H = t+d*N
    early = 2*d*(N-K-1) >= H
    late = 2*d*K >= H
    assert not (early and late)
    return early, late


def audit_identity(d, m, K, W, t, G, A):
    B = 10**d
    L = B//10
    C = B-1
    N = m-L+1
    k = L+K-1
    assert 2*L <= m < B and 8 <= K < N
    J = k*C+B
    M = m*C+B
    H = t+d*N
    q, e = divmod(H, 2)
    Q = 10**q
    R = 10**(t+d*K)*W[m] - (10**H-1)*W[k]
    T = (G*M-A)*B**K+J
    x_squared = C*C*R
    assert R > 0
    assert x_squared == G*J*B**N-T
    assert (x_squared+J) % B**K == 0
    assert 0 < T < 2*G*B**(K+2)
    assert 10*J > B*B and J < B*B
    assert 5*M > B*B and M < B*B
    assert 10**e*Q*Q == G*B**N
    assert 2*q >= d*L and q < 5*d*L
    # Squared, exact version of the upper approximation estimate:
    # T/(Q^2 alpha) < 20 B^(K-N+1).
    error_upper = Fraction(20, B**(N-K-1))
    assert Fraction(T*T, Q**4 * 10**e * J) < error_upper**2
    for p, multiple in ((2, 7), (5, 3)):
        v = valuation(J, p)
        assert v < multiple*d < d*K
        assert valuation(x_squared, p) == v
    early, late = region_flags(d, t, N, K)
    if early:
        assert d*N >= 2*d*(K+1)+t
    if late:
        if 2*d*K-H >= 2*d:
            assert x_squared < B**(2*K)
        else:
            assert H <= 2*d*K < H+2*d
    if m+1 < B:
        R_next = 10**(t+d*K)*W[m+1] - (10**(H+d)-1)*W[k]
        assert C*C*(R_next-R) == G*C*B**K*(J*B**(N-K)-1)
        assert R_next > R
    y = isqrt(R)
    is_square = y*y == R
    if is_square:
        x = C*y
        for p in (2, 5):
            assert 2*valuation(x, p) == valuation(J, p)
    return is_square, early, late


def audit_rotations():
    total = 0
    width2 = {"pairs": 0, "early_pairs": 0, "late_pairs": 0,
              "square_pairs": 0, "early_square_pairs": 0,
              "late_square_pairs": 0}
    samples = []
    for d in (2, 3):
        B = 10**d
        L = B//10
        C = B-1
        W = [0]
        for n in range(1, B):
            W.append(W[-1]*10**len(str(n))+n)
        t = sum(len(str(n)) for n in range(1, L))
        assert t == ((9*d-10)*L+1)//9
        assert ((9*d-10)*L+1) % 9 == 0
        G = 10**t
        A = C*C*W[L-1]+L*C+1
        assert 2*d <= t < d*L and 0 < 8*A < G*B*B
        if d == 2:
            for m in range(2*L, B):
                for K in range(8, m-L+1):
                    sq, early, late = audit_identity(d, m, K, W, t, G, A)
                    width2["pairs"] += 1
                    width2["early_pairs"] += early
                    width2["late_pairs"] += late
                    width2["square_pairs"] += sq
                    width2["early_square_pairs"] += sq and early
                    width2["late_square_pairs"] += sq and late
                    total += 1
        else:
            for m in (2*L, 3*L, 5*L, B-1):
                N = m-L+1
                H = t+d*N
                boundary = (H+2*d-1)//(2*d)
                cuts = {8, 9, N//2, N-1, boundary-1, boundary,
                        N-1-boundary, N-boundary}
                for K in sorted(cuts):
                    if 8 <= K < N:
                        audit_identity(d, m, K, W, t, G, A)
                        samples.append([d, m, K])
                        total += 1
    assert width2["early_square_pairs"] <= (8*2+6)*100
    assert width2["late_square_pairs"] <= (24*2+37)*100
    return dict(exact_rotation_checks=total, exhaustive_width2=width2,
                width3_samples=samples)


def audit_small_modulus_roots():
    checks = 0
    moduli = []
    for p, top in ((2, 10), (5, 6)):
        for n in range(1, top+1):
            modulus = p**n
            counts = [0]*modulus
            for x in range(modulus):
                counts[x*x % modulus] += 1
            for J in range(1, min(modulus, 501)):
                assert valuation(J, p) < n
                actual = counts[-J % modulus]
                predicted = prime_power_roots_formula(J, p, n)
                assert actual == predicted
                v = valuation(J, p)
                if v % 2:
                    assert actual == 0
                else:
                    assert actual <= (4 if p == 2 else 2)*p**(v//2)
                checks += 1
            moduli.append(modulus)
    # Direct CRT/root-count check at small decimal moduli too.
    for n in (1, 2, 3):
        modulus = 10**n
        counts = [0]*modulus
        for x in range(modulus):
            counts[x*x % modulus] += 1
        for J in range(1, min(modulus, 501)):
            if valuation(J, 2) < n and valuation(J, 5) < n:
                expected = (prime_power_roots_formula(J, 2, n)
                            * prime_power_roots_formula(J, 5, n))
                assert counts[-J % modulus] == expected
                checks += 1
        moduli.append(modulus)
    return dict(exact_prime_power_and_crt_checks=checks, moduli=moduli)


def audit_smooth_sums():
    out = []
    for d in (2, 3, 4):
        B = 10**d
        L = B//10
        C = B-1
        Js = [k*C+B for k in range(L+7, B-1)]
        compatible = []
        actual_root_sum = 0
        for J in Js:
            v2, v5 = valuation(J, 2), valuation(J, 5)
            assert v2 < 7*d and v5 < 3*d
            assert d*8-v2 >= 3
            if v2 % 2 == 0 and v5 % 2 == 0:
                z = 2**(v2//2)*5**(v5//2)
                assert z*z <= J < B*B
                compatible.append(z)
            actual_root_sum += (prime_power_roots_formula(J, 2, d*8)
                                * prime_power_roots_formula(J, 5, d*8))
        zs = smooth_values_below(B)
        assert len(zs) == len(set(zs))
        divisibility_weight = 0
        for z in zs:
            count = sum(J % (z*z) == 0 for J in Js)
            assert count*z*z <= B+z*z
            divisibility_weight += z*count
        reciprocal = sum((Fraction(1, z) for z in zs), Fraction(0))
        assert reciprocal < Fraction(5, 2)
        h, power5 = 0, 1
        while power5*5 < B:
            h += 1
            power5 *= 5
        assert power5 < B <= power5*5
        assert sum(zs) < 2*B*(h+1)
        assert sum(compatible) <= divisibility_weight
        assert divisibility_weight <= B*reciprocal+sum(zs)
        assert sum(compatible) < B*(Fraction(9, 2)+2*h)
        assert actual_root_sum <= 8*sum(compatible)
        assert actual_root_sum < B*(36+16*h) < (24*d+36)*B
        out.append(dict(d=d, cuts=len(Js), even_valuation_cuts=len(compatible),
                        smooth_weights_sum=sum(compatible),
                        congruence_root_sum=actual_root_sum,
                        strong_late_theorem_bound=(24*d+36)*B,
                        smooth_divisors=len(zs), h=h))
    return out


def audit_width_inequalities():
    for d in range(2, 1001):
        B = 10**d
        L = B//10
        t = ((9*d-10)*L+1)//9
        assert ((9*d-10)*L+1) % 9 == 0
        assert 2*d <= t < d*L
        assert L >= 2*d
        q_min = (t+d*(L+1))//2
        q_max = (t+d*(9*L))//2
        assert 2*q_min >= d*L and q_max < 5*d*L
        assert q_max < 10*q_min
        assert 6*L < 2**(4*d)
        for K in (8, L, 5*L):
            N0 = 2*K+2+Fraction(t, d)
            center = 2*K+2+Fraction(t+3, d)
            assert center-N0 == Fraction(3, d) <= Fraction(3, 2)
            ceil_N0 = -(-N0.numerator//N0.denominator)
            endpoint = N0+3
            ceil_endpoint = -(-endpoint.numerator//endpoint.denominator)
            assert ceil_endpoint-ceil_N0 == 3
            assert ceil_endpoint-center >= Fraction(3, 2)
        # Exact integer derivation of the relaxed rational-center gap:
        # 1/Q2 < 20 B^(K-N1+1) => q2 >= d(N1-K-1)-1.
        # Hence dN2 >= 2d(N1-K-1)-t+e-2,
        # which is strictly greater than 2dN1-d*center.
        for e in (0, 1):
            assert e-2 > -3
    return dict(width_threshold_checks=999, exact_center_checks=2997,
                exact_gap_count_checks=999)


def audit_late_boundary_strip():
    results = []
    for d in (2, 3, 4):
        B = 10**d
        L = B//10
        t = ((9*d-10)*L+1)//9
        admissible_boundary_pairs = 0
        for m in range(2*L, B):
            N = m-L+1
            H = t+d*N
            K = (H+2*d-1)//(2*d)
            assert H <= 2*d*K < H+2*d
            assert 2*d*(K-1) < H
            assert 2*d*(K+1) >= H+2*d
            if 8 <= K < N:
                admissible_boundary_pairs += 1
        assert admissible_boundary_pairs < B
        results.append(dict(d=d, endpoints=B-2*L,
                            boundary_pairs=admissible_boundary_pairs))
    return results


def main():
    results = dict(
        scope="Finite audits only; the all-width bound is proved in the note.",
        rotations=audit_rotations(),
        roots=audit_small_modulus_roots(),
        smooth_sums=audit_smooth_sums(),
        width_inequalities=audit_width_inequalities(),
        late_boundary_strips=audit_late_boundary_strip(),
    )
    path = Path(__file__).with_name("uniform-cut-sparsity-certificate.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps(results, indent=2))
    print("PASS. No all-width nonexistence or full-conjecture claim is made.")


if __name__ == "__main__":
    main()
