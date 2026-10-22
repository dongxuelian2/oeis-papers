#!/usr/bin/env python3
"""A077187: all r=11*3**b*2**a*5**c, 0<=b<=2, a,c>=0.

Odd-u branch: exact nonzero invariant, no resultant sieve.
Even-u branch: explicit quadratic obstruction; reuse the ten existing
v=11 norm integers and exhaust all admissible indices under their bounds.
No new cyclotomic field degrees, target-prime enumeration, or order cutoff.
"""
from math import gcd
from sympy import Poly, QQ, Rational, Symbol, cyclotomic_poly, resultant
from certify_fixed_v7 import algebra, drift_resultant
from certify_fixed_v11 import EXPECTED

x = Symbol("x")
EVEN_NORMS = {gamma: N for g, gamma, N in EXPECTED if g == 22}


def explicit_coordinates(g, gamma):
    phi, red, mul, add, scal, neg, sub, inv, powers = algebra(g)
    if g == 11:
        a = 10 * gamma % 11  # 2a=9 gamma mod 11.
        z, zi = powers[a], powers[-a % g]
        d = 11 - 2 * a
        U = [scal(add(red(1), zi), Rational(99, 200)),
             scal(sub(red(1), zi), Rational(9*d, 20)), red(0)]
        V = [scal(add(red(1), z), Rational(-81, 200)),
             scal(sub(red(1), z), Rational(-11*d, 20)), red(0)]
    elif g == 22:
        a = 9 * gamma % 11
        z, zi = powers[a], powers[-a % g]
        d = 11 - 2 * a
        U = [red(Rational(99, 200)),
             scal(sub(red(d), scal(zi, 11)), Rational(9, 20)), red(0)]
        V = [red(Rational(-81, 200)),
             scal(sub(red(d), scal(z, 11)), Rational(-11, 20)), red(0)]
    else:
        raise ValueError(g)
    return a, d, z, U, V


def verify_explicit_identities():
    for g in (11, 22):
        phi, red, mul, add, scal, neg, sub, inv, powers = algebra(g)
        for gamma in range(1, 11):
            a, d, z, U, V = explicit_coordinates(g, gamma)
            _, generic_U, generic_V = drift_resultant(
                g, gamma, return_coordinates=True, v=11, ell=22)
            assert U == generic_U and V == generic_V, (g, gamma)
            if g == 11:
                target = scal(add(z, red(1)), Rational(909, 100))
                for j in range(3):
                    invariant = sub(scal(mul(z, U[j]), 11), scal(V[j], 9))
                    assert invariant == (target if j == 0 else red(0))
            else:
                linear = sub(mul(U[1], V[0]), mul(U[0], V[1]))
                obstruction = add(add(red(891), scal(z, 40*d)),
                                  scal(mul(z, z), -1331))
                # Multiplication by z does not change the absolute norm.
                assert scal(mul(z, linear), 4000) == scal(obstruction, 9)
                # z is primitive 22 when a is odd, primitive 11 otherwise.
                z_order = 22 if a % 2 else 11
                quadratic = 9 * (891 + 40*d*x - 1331*x*x)
                norm = abs(int(resultant(quadratic,
                                        cyclotomic_poly(z_order, x), x)))
                assert norm == EVEN_NORMS[gamma], (gamma, norm)
    assert pow(10, 2, 101) == 100 and pow(10, 4, 101) == 1
    print("PASS all 20 explicit linear formulas; odd-u nonzero invariant")
    print("PASS all 10 existing even-u norms from a degree-two obstruction")


def base_polynomial(b_positive, c_positive):
    index = 22 * (3 if b_positive else 1) * (5 if c_positive else 1)
    return [int(c) for c in Poly(cyclotomic_poly(index, x), x).all_coeffs()]


def phi_mod(a, b, c, modulus, bases):
    assert a >= 1 and b in (0, 1, 2) and c >= 0
    exponent = 2**(a-1) * 3**max(b-1, 0) * 5**max(c-1, 0)
    value_at = pow(10, exponent, modulus)
    out = 0
    for coeff in bases[b > 0, c > 0]:
        out = (out * value_at + coeff) % modulus
    return out


def certify_even_branch():
    bases = {(b, c): base_polynomial(b, c)
             for b in (False, True) for c in (False, True)}
    maximum = max(EVEN_NORMS.values())
    counts = [0, 0, 0]
    for b in (0, 1, 2):
        a = 1
        while 11 * 3**b * 2**a <= maximum:
            c = 0
            while (r := 11 * 3**b * 2**a * 5**c) <= maximum:
                w = 3**b * 2**a * 5**c
                gamma = pow(w % 11, -1, 11)
                norm = EVEN_NORMS[gamma]
                if r <= norm:
                    common = gcd(norm, phi_mod(a, b, c, norm, bases))
                    assert common == 1, (a, b, c, r, gamma, common)
                    counts[b] += 1
                c += 1
            a += 1
    assert counts == [3887, 3796, 3702], counts
    print("PASS exhaustive even-u cyclotomic sieve, counts by b=0,1,2:", counts)
    print("Every raw cyclotomic gcd is 1; no candidate factors remain.")
    print("PASS all ord_p(10)=11*3^b*2^a*5^c, b<=2, a,c>=0")
    print("Odd a=0 branch is algebraic; even a>=1 branch is computation-certified.")
    print("Together with the elementary v|9 theorem: all coprime parts v|99.")
    print("The unrestricted all-primes A077187 conjecture remains OPEN.")
    return counts


if __name__ == "__main__":
    verify_explicit_identities()
    certify_even_branch()
