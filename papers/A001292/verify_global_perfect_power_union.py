#!/usr/bin/env python3
"""Finite audits for GLOBAL_PERFECT_POWER_UNION.md, not a proof by search."""
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def valuation(n, p):
    assert n > 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def prime_flags(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p*p
            sieve[start:n+1:p] = b"\x00" * ((n-start)//p+1)
    return sieve


def main():
    checks = {}

    # Direct full-prefix smooth parts and unsaturated valuations.
    W = 0
    s = 0
    minimum_slack = None
    for k in range(1, 10001):
        w = len(str(k))
        W = W * (10**w) + k
        s += w
        if k >= 10:
            a, b = valuation(W, 2), valuation(W, 5)
            assert (2**a)*(5**b) < 10**(2*w), (k, a, b)
            assert a < s and b < s, (k, a, b, s)
            if k >= 12:
                assert s > 7*w
            minimum_slack = min(minimum_slack or s, s-max(a,b))
    checks["prefixes"] = {"k_from": 10, "k_through": 10000,
                           "smooth_part_and_unsaturated_valuations": True,
                           "minimum_precision_minus_local_valuation": minimum_slack}

    # Exact finite local root-compression checks for all right sides attained.
    groups_checked = 0
    root_values_checked = 0
    for p, n_max in ((2, 10), (5, 6)):
        for n in range(1, n_max+1):
            modulus = p**n
            for e in (3, 5, 7, 11):
                groups = defaultdict(list)
                for y in range(modulus):
                    groups[pow(y, e, modulus)].append(y)
                    root_values_checked += 1
                for c, roots in groups.items():
                    if c == 0:
                        continue  # The theorem excludes saturated valuations.
                    v = valuation(c, p)
                    assert v < n and v % e == 0
                    a = v//e
                    compressed = p**(n-(e-1)*a)
                    branches = {y % compressed for y in roots}
                    bound = 5 if p == 5 and e == 5 else 1
                    assert len(branches) <= bound, (p,n,e,c,len(branches))
                    groups_checked += 1
    checks["compressed_roots"] = {"primes": [2,5], "exponents": [3,5,7,11],
                                  "right_side_groups": groups_checked,
                                  "root_values": root_values_checked,
                                  "all_branch_bounds_pass": True}

    # Rotation length, fixed-width cut recovery, and value multiplicity.
    digits = ""
    lengths = [0]
    rotations_checked = 0
    max_multiplicity = 0
    for m in range(1, 301):
        digits += str(m)
        lengths.append(len(digits))
        value_widths = defaultdict(set)
        value_counts = defaultdict(int)
        for k in range(1, m):
            s = lengths[k]
            w = len(str(k))
            rotated = digits[s:] + digits[:s]
            assert rotated[0] != "0" and len(rotated) == lengths[m]
            assert int(rotated[-w:]) == k
            assert rotated[-s:] == digits[:s]
            assert w not in value_widths[rotated]
            value_widths[rotated].add(w)
            value_counts[rotated] += 1
            assert value_counts[rotated] <= len(str(m))
            max_multiplicity = max(max_multiplicity, value_counts[rotated])
            rotations_checked += 1
    checks["rotation_injection"] = {"m_through": 300, "pairs": rotations_checked,
                                    "maximum_observed_same_value_multiplicity": max_multiplicity,
                                    "length_and_cut_recovery_pass": True}

    # All coefficient inequalities are checked by exact integer arithmetic.
    for d in range(2, 2001):
        B = 10**d
        correction = 40 if d >= 3 else 0
        assert 5*d*(d**4+d*d+correction) <= 2*B
        assert 25*d**4 <= 4*B       # (d^2/sqrt(B))^2 <= (2/5)^2.
        assert 50*d <= B
        assert 25*(2*d*d+14*d) <= 9*B
        assert d*d < 2*B
    log10_lower = Fraction(23, 10)
    odd_constant = (Fraction(12,5) + 1 + Fraction(9,25)
                    + (8+Fraction(32,5))/log10_lower)
    perfect_constant = odd_constant + Fraction(320,50)
    assert odd_constant < 11
    assert perfect_constant < 17
    assert sum(range(10,100)) == 4905
    checks["constants"] = {"widths_from": 2, "widths_through": 2000,
                            "all_exact_width_inequalities_pass": True,
                            "odd_coefficient_upper_rational": str(odd_constant),
                            "perfect_coefficient_upper_rational": str(perfect_constant),
                            "claimed_odd_constant": 11,
                            "claimed_perfect_constant": 17,
                            "claimed_square_constant": 330,
                            "d2_total_pairs": 4905}

    # Finite sanity check of the elementary prime estimate and low-prime sum.
    flags = prime_flags(200000)
    count = 0
    for n in range(2, len(flags)):
        count += flags[n]
        assert count < 4*n/math.log(n)
    for d in range(2, 101):
        P = d*d
        total = sum(p*(5 if p == 5 else 1)
                    for p in range(3, P+1) if flags[p])
        bound = P*(P+1)//2 + (20 if d >= 3 else 0)
        assert total <= bound
    checks["prime_counts"] = {"integer_arguments_through": 200000,
                               "pi_u_lt_4u_over_log_u_pass": True,
                               "low_prime_sum_widths_through": 100}

    certificate = {"status": "PASS", "scope": "Finite corroboration only; the general theorem uses the written proofs and companion all-cut determinant input.", "checks": checks}
    output = json.dumps(certificate, indent=2, sort_keys=True)
    (HERE / "global-perfect-power-union-certificate.json").write_text(output+"\n")
    print(output)


if __name__ == "__main__":
    main()
