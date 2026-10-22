"""Independent checks for general_dynamics.md; no project formula imports.

Finite tests verify identities, and are not an all-primes existence proof.
"""
from math import gcd, lcm


def order10(n):
    if n == 1:
        return 1
    assert gcd(n, 10) == 1
    x, d = 10 % n, 1
    while x != 1:
        x = x * 10 % n
        d += 1
    return d


def general_period(p):
    r = order10(p)
    v = r
    for ell in (2, 5):
        while v % ell == 0:
            v //= ell
    return r, lcm(r, order10(v))


def moments(q, n, p):
    """Binary concatenation: return q**n, sum q**j, sum j*q**j."""
    def join(a, b):
        na, pa, sa, ta = a
        nb, pb, sb, tb = b
        return ((na + nb) % p, pa * pb % p,
                (sa + pa * sb) % p,
                (ta + pa * (na * sb + tb)) % p)
    out = (0, 1, 0, 0)
    block = (1, q, 1, 0)
    while n:
        if n & 1:
            out = join(out, block)
        block = join(block, block)
        n >>= 1
    return out[1:]


def states(p, upto):
    """Full layers from independent geometric-moment binary composition."""
    r = order10(p)
    c = y = 0
    yield c, y
    for e in range(1, upto + 1):
        q = pow(10, e, p)
        L = pow(10, e - 1, p)
        # All three moments are periodic with period p*r in their length.
        N = 9 * pow(10, e - 1, p * r) % (p * r)
        alpha, s0, s1 = moments(q, N, p)
        A = (L * s0 + s1) % p
        B = ((L + N - 1) * s0 - s1) % p
        c = (alpha * c + B) % p
        y = (y + A) * pow(alpha, -1, p) % p
        yield c, y


def smooth_drift_formula(p):
    r = order10(p)
    v, b = r, 0
    while v % 3 == 0:
        v //= 3
        b += 1
    s = v
    for ell in (2, 5):
        while v % ell == 0:
            v //= ell
    assert v == 1 and b >= 2
    t = 3 ** (b - 2)
    m = r // t
    z = pow(10, m, p)
    gamma = pow(s, -1, t) if t > 1 else 0
    i10, i20, i200 = [pow(x, -1, p) for x in (10, 20, 200)]
    U = (99 * i200 - 9 * i20 * m) % p
    V = (-81 * i200 + 9 * i20 * m) % p
    E = 0
    for j in range(1, t):
        prior = E
        e = j * pow(10, j - 1, t) % t
        E = (E + e) % t
        a, w = pow(z, gamma * e, p), pow(z, j, p)
        iv = pow(w - 1, -1, p)
        X, Z = w * iv % p, w * iv * iv % p
        U += pow(z, -gamma * E, p) * (
            m * ((a - 1) - 9 * i10 * a * X) + m * m * (a - 1) * Z)
        V += pow(z, gamma * prior, p) * (
            m * (a - i10) * X + m * m * (1 - a) * Z)
    return U % p, V % p


def window_formula(p, c, y, L, q, n):
    if q == 1:
        return ((L + n) ** 2 + c + y + L - L * L) % p
    iv = pow(q - 1, -1, p)
    a = q * (c + L * iv + iv * iv) % p
    b = (y - L * iv + q * iv * iv) % p
    return (a * pow(q, n, p) + b * pow(q, -n, p)
            - 2 * q * iv * iv) % p


def check():
    primes = [p for p in range(3, 251)
              if p != 5 and all(p % d for d in range(2, int(p ** .5) + 1))]
    for p in primes:
        r, T = general_period(p)
        ss = list(states(p, 3 * T))
        assert tuple((ss[2*T][i] - ss[T][i]) % p for i in range(2)) == tuple(
            (ss[3*T][i] - ss[2*T][i]) % p for i in range(2)), (p, r, T)
        c = y = 0
        for k in range(1, 301):
            q = pow(10, len(str(k)), p)
            L = 10 ** (len(str(k)) - 1)
            if k == L:
                c0, y0 = c, y
            f = (q * c + k + y) % p
            assert f == window_formula(p, c0, y0, L, q, k-L), (p, k)
            c = (q * c + k) % p
            y = (y + k) * pow(q, -1, p) % p
    print('PASS general affine period and all within-layer formulas:', len(primes), 'primes')
    for p in (19, 109, 163, 487, 1459, 2917, 17497, 52489):
        r = order10(p)
        ss = list(states(p, 2*r))
        observed = tuple((ss[2*r][i] - ss[r][i]) % p for i in range(2))
        assert smooth_drift_formula(p) == observed, (p, r)
    print('PASS independent smooth drift identities through b=8')
    p = 43
    ss = list(states(p, 84))
    print('r-period counterexample p=43,r=21:', [ss[j*21] for j in range(1,5)])
    print('correct T=', general_period(p)[1])


if __name__ == '__main__':
    check()
