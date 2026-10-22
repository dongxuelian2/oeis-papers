"""Exact tail-gauge algebra. No unbounded prime-scan claims."""
from fractions import Fraction as Q
from math import isqrt
import argparse
import json


def constants(d):
    q = 10 ** d
    L = 10 ** (d - 1)
    c = Q(L, q-1) + Q(1, (q-1)**2)
    b = -Q(L, q-1) + Q(q, (q-1)**2)
    f = Q(q, q-1) - Q(q, (q-1)**2)
    delta = -Q(q, q-1) - Q(1, (q-1)**2)
    alpha = 10 ** (9*d*L)
    return q, c, b, delta, f, alpha


def apply(d, state, rho=Q(1), inverse=False):
    q, c, b, delta, f, alpha = constants(d)
    a = alpha*rho
    C, Y = state
    if inverse:
        return (C-delta)/a-c, (Y-f)*a-b
    return a*(C+c)+delta, (Y+b)/a+f


def square_rational(x):
    if x < 0:
        return False
    return isqrt(x.numerator)**2 == x.numerator and isqrt(x.denominator)**2 == x.denominator


def u8_window_coefficients():
    state = (Q(0), Q(0))
    for d in (1, 2, 3):
        state = apply(d, state)
    result = {}
    for d in (3, 2, 1):
        q, c, b, delta, f, alpha = constants(d)
        U, V = state[0]-delta, state[1]-f
        result[d] = (q*U, -Q(2*q, (q-1)**2), V)
        if d > 1:
            state = apply(d, state, Q(-1), inverse=True)
    return result


def u8_window_discriminants():
    return {d: b*b-4*a*c
            for d, (a, b, c) in u8_window_coefficients().items()}


def rational_mod(x, p):
    x = Q(x)
    return x.numerator % p * pow(x.denominator, -1, p) % p


def full_layer(p, e, r, state, inverse=False):
    L = pow(10, e-1, p)
    q = 10*L % p
    N = 9*L % p
    alpha = pow(10, 9*e*pow(10, e-1, r) % r, p)
    if q == 1:
        s0 = N
        s1 = N*(N-1)*pow(2, -1, p) % p
    else:
        iv = pow(q-1, -1, p)
        s0 = (alpha-1)*iv % p
        s1 = (q-N*alpha+(N-1)*q*alpha)*iv*iv % p
    R = (L*s0+s1) % p
    B = ((q-1)*s0-s1) % p
    C, Y = state
    if inverse:
        return (C-B)*pow(alpha, -1, p) % p, (alpha*Y-R) % p
    return (alpha*C+B) % p, (Y+R)*pow(alpha, -1, p) % p


def subgroup(q, p):
    vals = [1]
    x = q % p
    while x != 1:
        vals.append(x)
        x = x*q % p
    return vals


def order10(n):
    if n == 1:
        return 1
    return len(subgroup(10, n))


def verify_examples():
    from math import lcm
    examples = (73, 137, 7841, 617, 233, 313, 2393)
    q2, c2, b2, d2, f2, a2 = constants(2)
    q3, c3, b3, d3, f3, a3 = constants(3)
    K = 10**189
    aa = Q(10, 81)+2*(d2+c3)/K
    bb = Q(1, 81)+2*K*(f2+b3)
    assert aa == Q(10, 81)-Q(219804400, 120758121*K)
    assert bb == Q(1, 81)+Q(217557800*K, 120758121)
    rows = []
    coefficients = u8_window_coefficients()
    for p in examples:
        r = order10(p)
        v = r//8
        assert r % 8 == 0 and v % 2 and v % 5
        T = lcm(r, order10(v))
        actual = (0, 0)
        for d in (1, 2, 3):
            actual = full_layer(p, d, r, actual)
        W = actual
        for d in (3, 2, 1):
            W = full_layer(p, T+d, r, W, inverse=True)
        rho1 = pow(10, 9*(pow(10, T, r)-1), p)
        inv9 = pow(9, -1, p)
        A = (W[0]+10*inv9*inv9) % p
        B = (W[1]+inv9*inv9) % p
        assert A*rho1 % p == rational_mod(aa, p)
        assert B*pow(rho1, -1, p) % p == rational_mod(bb, p)
        H = subgroup(10, p)
        roots_old = [z for z in H if (10*A*z*z-20*inv9*inv9*z+B) % p == 0]
        am, bm = rational_mod(aa,p), rational_mod(bb,p)
        roots_new = [t for t in H if (10*am*t*t-20*inv9*inv9*t+bm) % p == 0]
        assert sorted(roots_old) == sorted(rho1*t % p for t in roots_new)
        # Independently form each target end state with the modular layer
        # recurrence, then remove its current multiplier from the window.
        X = actual
        characters = {}
        for d in (3, 2, 1):
            qd, _, _, delta, f, _ = constants(d)
            field_coefficients = (
                qd*(X[0]-rational_mod(delta, p)) % p,
                -2*qd*pow(qd-1, -2, p) % p,
                (X[1]-rational_mod(f, p)) % p)
            assert field_coefficients == tuple(
                rational_mod(value, p) for value in coefficients[d])
            ac, bc, cc = field_coefficients
            dd = (bc*bc-4*ac*cc) % p
            characters[d] = 0 if not dd else (
                1 if pow(dd, (p-1)//2, p) == 1 else -1)
            if d > 1:
                X = full_layer(p, T+d, r, X, inverse=True)
        if p == 617:
            assert characters == {1: -1, 2: -1, 3: -1}
        disc = (400*pow(81,-2,p)-40*am*bm) % p
        rows.append(dict(p=p, r=r, rho1=rho1, first_roots=roots_new,
                         three_window_characters=characters,
                         discriminant_character=0 if not disc else (1 if pow(disc,(p-1)//2,p)==1 else -1)))
    print(json.dumps(rows, indent=2))


def symbolic_report():
    ds = u8_window_discriminants()
    print('u8 discriminant rational sizes:',
          {d:(len(str(v.numerator)),len(str(v.denominator)),v>0) for d,v in ds.items()})
    for mask in range(1, 8):
        value = Q(1)
        chosen = []
        for d in range(1,4):
            if mask & (1 << (d-1)):
                chosen.append(d)
                value *= ds[d]
        relations = [c for c in (1,-1,2,-2,5,-5,10,-10)
                     if square_rational(value/c)]
        assert not relations, (chosen, relations)
        print('PASS squareclass independence for product', chosen)
    assert all(value != 0 for value in ds.values())
    print('PASS rank six for squareclasses -1, 2, 5, Delta_1, Delta_2, Delta_3')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--examples', action='store_true')
    parser.add_argument('--symbolic', action='store_true')
    args = parser.parse_args()
    if args.examples:
        verify_examples()
    if args.symbolic:
        symbolic_report()
