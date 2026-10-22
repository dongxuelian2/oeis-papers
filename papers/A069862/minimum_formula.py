#!/usr/bin/env python3
"""A069862 by a finite arithmetic formula over quadratic residue classes.

No orbit search, prefix-length cutoff, or calls to least.py are used to
evaluate a term. See minimum_formula.tex for the formula and completeness
proof. The only minimum is over explicit arithmetic-progression candidates.
"""
import argparse
from itertools import product
from math import gcd

from verify_existence import factor, order10


def ceildiv(a, b):
    return -((-a) // b)


def sqrt_prime(a, p):
    """One square root modulo an odd prime, or None (Tonelli--Shanks)."""
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    c, x, t, r = pow(z, q, p), pow(a, (q + 1) // 2, p), pow(a, q, p), s
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (r - i - 1), p)
        x, t, c, r = x * b % p, t * b * b % p, b * b % p, i
    return x


def sqrt_unit(a, p, e):
    """One root of a unit modulo p**e; the other is its negative."""
    x = sqrt_prime(a, p)
    if x is None:
        return None
    modulus = p
    inverse = pow(2 * x, -1, p)
    for _ in range(1, e):
        x += ((a - x * x) // modulus * inverse % p) * modulus
        modulus *= p
    return x


def quadratic_prime_classes(a, b, c, p, e):
    """Disjoint classes (residue, modulus) of all quadratic roots mod p**e.

    Each returned modulus divides p**e. Singular roots are compressed into
    classes rather than enumerating all their free higher digits.
    """
    modulus = p ** e
    a, b, c = a % modulus, b % modulus, c % modulus
    while e and a % p == b % p == c % p == 0:
        a, b, c = a // p, b // p, c // p
        e -= 1
        modulus //= p
    if not e:
        return [(0, 1)]
    if a % p == 0:
        if b % p == 0:
            return []
        # The square root congruent to b mod p yields the unique root.
        y = sqrt_unit(b * b - 4 * a * c, p, e)
        assert y is not None
        if y % p != b % p:
            y = -y
        return [((-2 * c * pow(b + y, -1, modulus)) % modulus, modulus)]
    delta = (b * b - 4 * a * c) % modulus
    if delta == 0:
        root_modulus = p ** ((e + 1) // 2)
        return [((-b * pow(2 * a, -1, root_modulus)) % root_modulus,
                 root_modulus)]
    valuation, unit = 0, delta
    while unit % p == 0:
        valuation += 1
        unit //= p
    if valuation % 2:
        return []
    s = valuation // 2
    y = sqrt_unit(unit, p, e - 2 * s)
    if y is None:
        return []
    root_modulus = p ** (e - s)
    inverse = pow(2 * a, -1, root_modulus)
    return [(((-b + sign * p ** s * y) * inverse) % root_modulus,
             root_modulus) for sign in (-1, 1)]


def crt_pair(r, q, s, v):
    """Merge two classes with coprime positive moduli, including modulus 1."""
    return (r + q * ((s - r) * pow(q, -1, v) % v), q * v)


def quadratic_classes(a, b, c, factors):
    classes = [(0, 1)]
    for p, e in factors.items():
        local = quadratic_prime_classes(a, b, c, p, e)
        classes = [crt_pair(r, q, s, v)
                   for (r, q), (s, v) in product(classes, local)]
        if not classes:
            break
    return classes


def geometric_terms(base, length, modulus):
    """B**length, S_length, T_length modulo modulus, with exact division."""
    denominator = (base - 1) ** 2
    extended = modulus * denominator
    power = pow(base, length, extended)
    s = (power - 1) // (base - 1) % modulus
    numerator = (base * power - (length + 1) * base + length) % extended
    assert numerator % denominator == 0
    return power % modulus, s, numerator // denominator


def block_value(value, endpoint, length, width, modulus):
    power, s, t = geometric_terms(10 ** width, length, modulus)
    return (power * value + endpoint * s + t) % modulus


def boundary_value(n, width):
    """Finite sum for the prefix preceding a width; no prefix recurrence."""
    first_width = len(str(n + 1))
    value, trailing_digits = 0, 0
    for d in range(width - 1, first_width - 1, -1):
        first, last = max(n + 1, 10 ** (d - 1)), 10 ** d - 1
        length = last - first + 1
        word = block_value(0, first - 1, length, d, n)
        value = (value + word * pow(10, trailing_digits, n)) % n
        trailing_digits += d * length
    return value


def interval_classes(n, width, value, endpoint, factors=None):
    """Return (transient endpoints, stable endpoint classes, stable lower bound).

    The classes characterize *every* zero of the fixed-width continuation
    after stabilization, including beyond the actual decimal interval.
    The caller intersects them with that interval using a ceiling formula.
    """
    factors = factor(n) if factors is None else factors
    alpha, beta = factors.get(2, 0), factors.get(5, 0)
    smooth = 2 ** alpha * 5 ** beta
    odd = n // smooth
    odd_factors = {p: e for p, e in factors.items() if p not in (2, 5)}
    base = 10 ** width
    burn = max(1, ceildiv(alpha, width), ceildiv(beta, width))
    early = [endpoint + j for j in range(1, burn)
             if block_value(value, endpoint, j, width, n) == 0]
    order = order10(odd) if odd > 1 else 1
    h = order // gcd(order, width)
    _, s_h, t_h = geometric_terms(base, h, odd)
    quadratic = h * s_h % odd
    target = -base * pow(base - 1, -1, smooth) % smooth
    g = gcd(h, smooth)
    reduced = smooth // g
    inverse_h = pow(h // g, -1, reduced)
    stable = []
    for j in range(h):
        difference = target - endpoint - j
        if difference % g:
            continue
        smooth_class = difference // g * inverse_h % reduced
        linear = (2 * ((endpoint + j) * s_h + t_h) - h * s_h) % odd
        constant = 2 * block_value(value, endpoint, j, width, odd) % odd
        for r, q in quadratic_classes(quadratic, linear, constant, odd_factors):
            z, modulus = crt_pair(r, q, smooth_class, reduced)
            period = h * modulus
            stable.append(((endpoint + j + h * z) % period, period))
    return early, stable, endpoint + burn


def least_formula(n, explain=False):
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return (1, []) if explain else 1
    factors = factor(n)
    trace = []
    for width in range(len(str(n + 1)), n + 1):
        endpoint, upper = max(n, 10 ** (width - 1) - 1), 10 ** width - 1
        value = boundary_value(n, width)
        early, classes, lower = interval_classes(n, width, value, endpoint, factors)
        candidates = [x for x in early if x <= upper]
        for r, period in classes:
            candidate = r + period * ceildiv(lower - r, period)
            if candidate <= upper:
                candidates.append(candidate)
        if explain:
            trace.append({"width": width, "prefix_residue": value,
                          "transient_roots": early, "stable_lower": lower,
                          "classes": classes, "first_endpoints": sorted(candidates)})
        if candidates:
            result = min(candidates) - n
            return (result, trace) if explain else result
    raise AssertionError("Universal existence bound violated")


def audit():
    from random import Random
    from least import least
    from verify import least as direct_least

    polynomials = 0
    for modulus in range(1, 32, 2):
        factors = factor(modulus)
        for a, b, c in product(range(modulus), repeat=3):
            classes = quadratic_classes(a, b, c, factors)
            obtained = {x for r, q in classes for x in range(r, modulus, q)}
            expected = {x for x in range(modulus) if (a*x*x + b*x + c) % modulus == 0}
            assert obtained == expected, (modulus, a, b, c, classes, expected)
            polynomials += 1
    print(f"PASS {polynomials} exhaustive quadratic congruences modulo odd m<=31", flush=True)
    rng = Random(69862)
    singular_checks = 0
    for modulus in (81, 125, 243, 625, 729, 2401, 6561, 675, 3675):
        factors = factor(modulus)
        polynomials = [(1, 0, 0), (0, 0, 0), (0, 0, 1)]
        for _ in range(64):
            a, b, c = (rng.randrange(modulus) for _ in range(3))
            polynomials.append((a, b, c))
            # Force zero discriminant, nontrivial content, or a linear reduction.
            p = next(iter(factors))
            polynomials.extend(((a*a, 2*a*b, b*b), (p*a, p*b, p*c), (p*a, 1, c)))
        for a, b, c in polynomials:
            classes = quadratic_classes(a, b, c, factors)
            obtained = [x for r, q in classes for x in range(r, modulus, q)]
            expected = {x for x in range(modulus) if (a*x*x + b*x + c) % modulus == 0}
            assert len(obtained) == len(set(obtained))
            assert set(obtained) == expected, (modulus, a, b, c)
            assert len(classes) <= 2 ** len(factors)
            singular_checks += 1
    print(f"PASS {singular_checks} higher-power and mixed-modulus quadratic checks", flush=True)
    # Arbitrary starting states test the classification, not just A069862 outputs.
    checks = 0
    for n in range(1, 181):
        for width in range(1, 5):
            value, endpoint = rng.randrange(n), rng.randrange(4*n + 1)
            early, classes, lower = interval_classes(n, width, value, endpoint)
            residue = value
            for length in range(1, 2*n + 20):
                x = endpoint + length
                residue = (10 ** width * residue + x) % n
                classified = x in early or (x >= lower and any((x-r) % q == 0 for r, q in classes))
                assert classified == (residue == 0), (n, width, endpoint, value, length)
                checks += 1
    print(f"PASS {checks} arbitrary-state classifications, including nilpotent transients", flush=True)
    for n in range(1, 1001):
        result = least_formula(n)
        assert result == least(n) == direct_least(n, result), (n, result)
    print("PASS minima n=1..1000 against state-orbit and direct enumeration", flush=True)
    from verify_existence import residue
    boundary_checks = 0
    for n in (1, 2, 7, 8, 9, 10, 37, 99, 100, 451, 999, 1000, 8192, 5**10, 3**8 * 7 * 11):
        first_width = len(str(n + 1))
        for width in range(first_width, first_width + 5):
            endpoint = max(n, 10 ** (width - 1) - 1)
            assert boundary_value(n, width) == residue(n, endpoint)
            boundary_checks += 1
    print(f"PASS {boundary_checks} boundary sums versus independent binary affine composition", flush=True)


def audit_reference(path):
    import hashlib
    from pathlib import Path
    raw = Path(path).read_bytes()
    rows = [tuple(map(int, line.split())) for line in raw.decode().splitlines()
            if line.strip() and not line.lstrip().startswith('#')]
    assert rows and all(n > 0 for n, _ in rows)
    assert all(rows[i][0] < rows[i+1][0] for i in range(len(rows) - 1))
    for n, expected in rows:
        obtained = least_formula(n)
        assert obtained == expected, (n, obtained, expected)
    print(f"PASS all {len(rows)} reference terms; SHA-256 {hashlib.sha256(raw).hexdigest()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("indices", type=int, nargs="*")
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--reference", help="OEIS b-file to compare independently")
    parser.add_argument("--explain", action="store_true")
    args = parser.parse_args()
    if args.audit:
        audit()
    if args.reference:
        audit_reference(args.reference)
    for n in args.indices:
        print(n, least_formula(n, args.explain))
    if not (args.audit or args.reference or args.indices):
        parser.error("supply positive indices, --audit, or --reference")
