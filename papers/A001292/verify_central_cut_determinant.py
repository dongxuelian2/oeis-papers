#!/usr/bin/env python3
"""Finite exact audits for the all-cut theorem; this is not a search proof."""

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


def determinant(rows):
    (a, b, c), (d, e, f), (g, h, i) = rows
    return a * (e*i-f*h) - b * (d*i-f*g) + c * (d*h-e*g)


def exact_rotations():
    counts = {"width2_pairs": 0, "width2_central_pairs": 0,
              "width2_square_pairs": 0, "width3_samples": 0}
    samples = []
    for d in (2, 3):
        B, L = 10**d, 10**(d-1)
        C = B-1
        W = [0]
        for m in range(1, B):
            W.append(W[-1] * 10**len(str(m)) + m)
        t = sum(len(str(m)) for m in range(1, L))
        assert t == ((9*d-10)*L+1)//9
        G = 10**t
        A = C*C*W[L-1]+L*C+1
        assert 0 < 8*A < G*B*B
        pairs = []
        if d == 2:
            pairs = [(m, K) for m in range(2*L, B)
                     for K in range(8, m-L+1)]
        else:
            for m in (2*L, 2*L+1, 3*L, 5*L, B-1):
                N = m-L+1
                H = t+d*N
                middle = (H//(2*d) + N-1-H//(2*d))//2
                cuts = {8, 9, N-1, N//2, middle,
                        H//(2*d), H//(2*d)-1,
                        N-1-H//(2*d), N-H//(2*d)}
                pairs += [(m, K) for K in sorted(cuts) if 8 <= K < N]
        for m, K in pairs:
            N, k = m-L+1, K+L-1
            J, M = k*C+B, m*C+B
            q, e = divmod(t+d*N, 2)
            Q = 10**q
            T = (G*M-A)*B**K+J
            R = 10**(t+d*K)*W[m] - (10**(t+d*N)-1)*W[k]
            assert C*C*R == G*J*B**N-T
            assert C*C*R % B**K == -J % B**K
            assert 0 < T < 2*G*B**(K+2)
            assert B*B < 10*J and J < B*B
            assert 10**e * Q*Q == G*B**N
            # Stronger denominator bound implies the approximation inequality.
            bound = Fraction(20, B**(N-K-1))
            assert Fraction(T*T, Q**4 * 10**e * J) < bound*bound
            # Radicand positivity and sufficient concavity condition.
            assert 5*T < G*J*B**N
            a0 = G*C*B**K
            assert 20*T > B*a0
            assert B >= 100 and B*B*20 < 3*B*8*C
            for p, multiplier in ((2, 7), (5, 3)):
                assert valuation(J, p) < multiplier*d < d*K
            y = isqrt(R)
            is_square = y*y == R
            central = (2*d*(N-K-1) < t+d*N
                       and 2*d*K < t+d*N)
            if d == 2:
                counts["width2_pairs"] += 1
                counts["width2_central_pairs"] += central
                counts["width2_square_pairs"] += is_square
            else:
                counts["width3_samples"] += 1
                samples.append([m, K])
    assert counts["width2_pairs"] == 3400
    assert 3400 < 32*100*((36).bit_length())
    return {**counts, "width3_sample_m_K": samples,
            "warning": "The theorem does not depend on these square searches."}


def compressed_root_branches():
    local_checks = decimal_checks = root_checks = 0
    for p, top in ((2, 10), (5, 6)):
        for n in range(1, top+1):
            modulus = p**n
            roots_by_value = {}
            for x in range(modulus):
                roots_by_value.setdefault(x*x % modulus, []).append(x)
            for J in range(1, min(modulus, 501)):
                v = valuation(J, p)
                assert v < n
                roots = roots_by_value.get(-J % modulus, [])
                if v % 2:
                    assert not roots
                else:
                    a = v//2
                    reduced_modulus = p**(n-a)
                    branches = {x % reduced_modulus for x in roots}
                    assert len(branches) <= (4 if p == 2 else 2)
                    assert len(roots) == len(branches)*p**a
                    for x in roots:
                        assert x > 0 and valuation(x, p) == a
                        root_checks += 1
                local_checks += 1
    for n in (1, 2, 3, 4):
        modulus = 10**n
        roots_by_value = {}
        for x in range(modulus):
            roots_by_value.setdefault(x*x % modulus, []).append(x)
        for J in range(1, min(modulus, 501)):
            v2, v5 = valuation(J, 2), valuation(J, 5)
            if max(v2, v5) >= n:
                continue
            roots = roots_by_value.get(-J % modulus, [])
            if v2 % 2 or v5 % 2:
                assert not roots
            else:
                z = 2**(v2//2)*5**(v5//2)
                r = modulus//z
                branches = {x % r for x in roots}
                assert len(branches) <= 8
                assert len(roots) == z*len(branches)
            decimal_checks += 1
    return {"prime_power_compressed_branch_checks": local_checks,
            "decimal_crt_compressed_branch_checks": decimal_checks,
            "individual_root_valuation_checks": root_checks}


# Sparse polynomials in (A,Q,lambda,T), with integer exponents, including
# negative Q powers. This verifies the derivative identity symbolically.
def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0)+coefficient
    return {m: c for m, c in out.items() if c}


def scale(poly, scalar):
    return {m: scalar*c for m, c in poly.items() if scalar*c}


def multiply(left, right):
    out = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            m = tuple(a+b for a, b in zip(ml, mr))
            out[m] = out.get(m, 0)+cl*cr
    return {m: c for m, c in out.items() if c}


def symbolic_concavity_identity():
    f = {(1, 2, 0, 0): 1, (0, 0, 0, 1): -1}
    fprime = {(1, 1, 0, 0): 2, (0, -1, 1, 0): -1}
    fsecond = {(1, 0, 0, 0): 2, (0, -2, 1, 0): 1}
    numerator = add(scale(multiply(f, fsecond), 2),
                    scale(multiply(fprime, fprime), -1))
    expected = {(1, 0, 1, 0): 6, (1, 0, 0, 1): -4,
                (0, -2, 1, 1): -2, (0, -2, 2, 0): -1}
    assert numerator == expected
    return {"symbolic_identity": "2 f f''-(f')^2 = A(6lambda-4T)-lambda(2T+lambda)/Q^2",
            "checked_by": "Exact sparse-polynomial expansion, not numerical samples."}


def synthetic_determinants():
    divisibility_checks = error_checks = nonzero = 0
    for r in (1, 2, 5, 10, 125, 1000, 10**16):
        for q in range(6):
            Qs = [10**q, 10**(q+1), 10**(q+3)]
            for beta in (0, 1, 7, r-1):
                for hs in ((1, 2, 3), (1, 11, 1001), (4, 25, 31)):
                    xs = [beta+r*h for h in hs]
                    D = determinant([(x, Q, 1) for x, Q in zip(xs, Qs)])
                    assert D % (r*Qs[0]) == 0
                    if D:
                        assert abs(D) >= r*Qs[0]
                        nonzero += 1
                    divisibility_checks += 1
    for Qs in ((1, 10, 100), (100, 1000, 100000), (3, 6, 12)):
        alpha = Fraction(11, 7)
        E = Fraction(9, 13)
        for ds in ((1, 2, 3), (1, 5, 2), (5, 1, 4), (5, 5, 5)):
            deltas = [E*Fraction(d, 6) for d in ds]
            xs = [alpha*Q-delta for Q, delta in zip(Qs, deltas)]
            D = determinant([(x, Q, 1) for x, Q in zip(xs, Qs)])
            assert abs(D) < 2*E*Qs[2]
            error_checks += 1
    return {"synthetic_divisibility_checks": divisibility_checks,
            "synthetic_nonzero_determinants": nonzero,
            "synthetic_error_column_bound_checks": error_checks,
            "warning": "Synthetic determinant examples are not rotation-square solutions."}


def centered_width_constants():
    rows = []
    for d in range(2, 1001):
        B, L = 10**d, 10**(d-1)
        t = ((9*d-10)*L+1)//9
        hmin = Fraction(10*L-1, 9*d)-5
        assert hmin == L+1-Fraction(t, d)-6
        assert L >= 5*d
        assert 91*L >= 450*d+10
        assert hmin >= Fraction(L, 10*d) > 0
        assert 40**2 < B**2  # Exact sufficiency for the relaxed triple gap.
        if d >= 3:
            assert 11*L >= 90*d+2
            assert hmin >= Fraction(L, 2*d)
        # bit_length(n) = 1+floor(log2 n) for positive integer n.
        count_factor = (18*d).bit_length()
        assert 2**(count_factor-1) <= 18*d < 2**count_factor
        uniform_factor = (90*d-1).bit_length()  # ceil(log2(90d))
        assert 2**(uniform_factor-1) < 90*d <= 2**uniform_factor
        assert 90*d < 2**(4*d)
        if d in (2, 3, 4, 10, 100, 1000):
            rows.append({"d": d, "theorem_coefficient_of_B": 32*count_factor,
                         "uniform_alternative_coefficient_of_B": 32*uniform_factor})
    return {"widths_audited": [2, 1000], "width_count": 999,
            "sample_bound_coefficients": rows}


def main():
    results = {
        "scope": "Finite component audits. The infinite theorem is established by the written proof.",
        "rotations": exact_rotations(),
        "compressed_roots": compressed_root_branches(),
        "concavity": symbolic_concavity_identity(),
        "determinants": synthetic_determinants(),
        "centered_constants": centered_width_constants(),
        "claims_not_made": ["All-width nonexistence", "All rotations covered",
                            "Earlier-width cuts covered", "Integer-power conjecture solved"],
    }
    target = Path(__file__).with_name("central-cut-determinant-certificate.json")
    target.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps(results, indent=2))
    print("PASS. Finite audits support, but do not replace, the theorem proof.")


if __name__ == "__main__":
    main()
