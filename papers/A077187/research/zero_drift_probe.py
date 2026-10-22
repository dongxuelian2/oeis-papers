"""Independent exploratory layer dynamics. No numerical scan proves universality."""
from math import gcd, lcm
import argparse
def primes(bound):
    sieve = bytearray(b'\x01') * (bound + 1)
    sieve[:2] = b'\x00\x00'
    for a in range(2, bound + 1):
        if sieve[a]:
            yield a
            for b in range(a * a, bound + 1, a):
                sieve[b] = 0


def order10(m):
    a = 10 % m
    result = 1
    while a != 1:
        a = a * 10 % m
        result += 1
    return result


def period(p):
    r = order10(p)
    t = r
    for f in (2, 5):
        while t % f == 0:
            t //= f
    s = order10(9 * t)
    return r, lcm(r, s)


def step(p, e, r, C, Y):
    L = pow(10, e - 1, p)
    q = 10 * L % p
    N = 9 * L % p
    alpha = pow(q, 9 * pow(10, e - 1, r) % r, p)
    if q == 1:
        s0 = N
        s1 = N * (N - 1) * pow(2, -1, p) % p
    else:
        iv = pow(q - 1, -1, p)
        s0 = (alpha - 1) * iv % p
        s1 = (q - N * alpha + (N - 1) * q * alpha) * iv**2 % p
    A = (L * s0 + s1) % p
    B = ((q - 1) * s0 - s1) % p
    return (alpha * C + B) % p, (Y + A) * pow(alpha, -1, p) % p


def scan(bound):
    zero = []
    for p in primes(bound):
        if p < 7:
            continue
        r, T = period(p)
        # Since r < p and p >= 7, e=T is beyond the 2/5-power transient.
        C = Y = 0
        first = None
        squares = []
        for e in range(1, 2 * T + 1):
            C, Y = step(p, e, r, C, Y)
            if e == T:
                first = C, Y
            if e > T and e % r == 0:
                squares.append(pow((-C - Y) % p, (p - 1) // 2, p) != p - 1)
        drift = ((C - first[0]) % p, (Y - first[1]) % p)
        if drift == (0, 0):
            zero.append((p, r, T, first, any(squares)))
            print('ZERO', zero[-1], flush=True)
    print('Completed bound', bound, 'zero drift cases', zero, flush=True)


def selftest():
    # Verify formulas against literal concatenation through all first 3 layers.
    for p in (7, 11, 13, 17, 19, 23, 31, 37):
        C = Y = 0
        layer_start = {}
        for k in range(1, 1000):
            e = len(str(k))
            L = 10 ** (e - 1)
            q = pow(10, e, p)
            if k == L:
                layer_start[e] = C, Y
            C0, Y0 = layer_start[e]
            n = k - L
            if q == 1:
                predicted = (k * k + C0 + Y0 + L - L * L) % p
            else:
                iv = pow(q - 1, -1, p)
                A = (C0 + L * iv + iv * iv) % p
                B = (Y0 - L * iv + q * iv * iv) % p
                predicted = (pow(q, n + 1, p) * A
                             + pow(q, -n, p) * B - 2*q*iv*iv) % p
            actual = (q * C + k + Y) % p
            assert predicted == actual, (p, k, predicted, actual)
            C, Y = (q*C+k) % p, (Y+k)*pow(q, -1, p) % p

    # Verify the theorem's explicit witness with full digit-layer recurrence,
    # without using the defect or square formulas to compute the state.
    examples = (7, 11, 13, 23, 31, 37, 41, 43, 53, 67, 71, 79, 83)
    for p in examples:
        r, T = period(p)
        t = r
        for f in (2, 5):
            while t % f == 0:
                t //= f
        u = r // t
        assert 10 % u == 0
        C = Y = 0
        for e in range(1, p*T + 1):
            C, Y = step(p, e, r, C, Y)
        lam = pow(10, T, r)
        n = (9*lam-10) % r
        for j in range(n):
            C, Y = (10*C+1+j) % p, (Y+1+j)*pow(10, -1, p) % p
        assert (10*C+1+n+Y) % p == 0, (p, r, T, n)
    print('PASS exact window identities and explicit witnesses:', examples)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bound', type=int)
    parser.add_argument('--selftest', action='store_true')
    args = parser.parse_args()
    if args.selftest:
        selftest()
    if args.bound is not None:
        scan(args.bound)
