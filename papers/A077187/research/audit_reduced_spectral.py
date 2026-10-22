#!/usr/bin/env python3
"""Independent field audit of removing gcd(v,9) from spectral phases.

These finite identity checks supplement the algebraic proof. They do not
assert universal nonzero drift or enumerate primes as an existence proof.
"""
from math import gcd, lcm
from audit_fixed_v7 import direct, isprime, prime_factors


def order10(n):
    if n == 1:
        return 1
    assert gcd(n, 10) == 1
    z, r = 10 % n, 1
    while z != 1:
        z = 10 * z % n
        r += 1
    return r


def reduced_spectral(p, r):
    v = r
    for q in (2, 5):
        while v % q == 0:
            v //= q
    u = r // v
    delta = gcd(v, 9)
    t = v // delta
    beta = 9 // delta
    ell = lcm(t, order10(t))
    g = gcd(r, ell)
    m = r // g
    T = m * ell
    assert T == lcm(r, order10(v))
    zeta = pow(10, m, p)
    assert pow(zeta, g, p) == 1
    assert all(pow(zeta, g // q, p) != 1 for q in prime_factors(g))
    gamma = pow(u, -1, t) if t > 1 else 0
    U = V = 0
    P = 1
    for j in range(1, ell + 1):
        exp = (g // t) * beta * gamma * j * pow(10, j - 1, t)
        A = pow(zeta, exp, p)
        actual = pow(10, 9 * (T + j) * pow(10, T + j - 1, r), p)
        assert A == actual, (p, r, j, 'phase')
        c = pow(zeta, j, p)
        roots = [pow(10, T + j + k * ell, p) for k in range(m)]
        assert len(set(roots)) == m
        assert all(pow(q, m, p) == c for q in roots)
        regular = [q for q in roots if q != 1]
        F1 = sum(q * pow(q - 1, -1, p) for q in regular) % p
        F2 = sum(q * pow(q - 1, -2, p) for q in regular) % p
        if c == 1:
            assert A == 1
            assert F1 == (m - 1) * pow(2, -1, p) % p
            assert F2 == -(m * m - 1) * pow(12, -1, p) % p
        else:
            assert F1 == m * c * pow(c - 1, -1, p) % p
            assert F2 == m * m * c * pow(c - 1, -2, p) % p
        Pinv = pow(P, -1, p)
        alpha = Pinv * (1 - pow(A, -1, p)) % p
        phase_diff = P * (A - 1) % p
        U += alpha * (len(regular) + F2) - 9 * Pinv * pow(10, -1, p) * F1
        V += phase_diff * (F1 * pow(10, -1, p) - F2)
        V += 9 * P * A * pow(10, -1, p) * F1
        if c == 1:
            U += 9 * Pinv * pow(200, -1, p)
            V += 9 * P * pow(200, -1, p)
        P = P * A % p
    assert P == 1
    return (U % p, V % p), (v, t, ell, T)


def main():
    cases = (7, 11, 19, 23, 29, 43, 67, 71, 89, 109, 127,
             163, 199, 331, 397, 463, 487, 617, 1321, 1459)
    for p in cases:
        assert isprime(p)
        r = order10(p)
        observed, (v, t, ell, T) = reduced_spectral(p, r)
        assert observed == direct(p, r, T), (p, r, observed)
        print('PASS', 'p=', p, 'r=', r, 'v=', v, 't=', t,
              'ell=', ell, 'drift=', observed)
    print('PASS 20 independent reduced-phase, coset, and direct-layer identities')


if __name__ == '__main__':
    main()
