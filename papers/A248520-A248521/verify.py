#!/usr/bin/env python3
"""Certified rational evaluation of cotangent-floor sequences."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path


def floor(x):
    return x.numerator//x.denominator


def ceil(x):
    return -floor(-x)


def atan_recip(n, digits):
    assert n >= 2
    total, power, j = Q(0), Q(1, n), 0
    tolerance = Q(1, 10**digits)
    while True:
        total += (-1)**j*power/(2*j+1)
        power /= n*n
        j += 1
        next_term = (-1)**j*power/(2*j+1)
        if abs(next_term) < tolerance:
            return min(total, total+next_term), max(total, total+next_term)


@lru_cache(None)
def pi_bounds(digits):
    a, b = atan_recip(5, digits+5)
    c, d = atan_recip(239, digits+5)
    low, high = 16*a-4*d, 16*b-4*c
    scale = 10**digits
    return Q(floor(low*scale), scale), Q(ceil(high*scale), scale)


def trig_bounds(x, sine, digits):
    """Alternating Taylor bounds, here only 0<x<1 is used."""
    assert 0 < x < 1
    term, total, j = (x if sine else Q(1)), Q(0), 0
    tolerance = Q(1, 10**digits)
    while True:
        total += term
        a = 2*j+(2 if sine else 1)
        term *= -x*x/(a*(a+1))
        j += 1
        if abs(term) < tolerance:
            return min(total, total+term), max(total, total+term)


@lru_cache(None)
def cot_floor(k):
    if k <= 2:
        assert k >= 1
        return k-1
    digits = 12
    while True:
        pl, ph = pi_bounds(digits)
        xl, xh = pl/(2*k), ph/(2*k)
        sl, _ = trig_bounds(xl, True, digits+6)
        _, sh = trig_bounds(xh, True, digits+6)
        cl, _ = trig_bounds(xh, False, digits+6)
        _, ch = trig_bounds(xl, False, digits+6)
        if sl > 0 and floor(cl/sh) == floor(ch/sl):
            return floor(cl/sh)
        digits *= 2


@lru_cache(None)
def one(n):
    assert n >= 1
    if n == 1:
        return 1
    digits = 12
    while True:
        pl, ph = pi_bounds(digits)
        al, ah = atan_recip(n, digits+6)
        low, high = pl/(2*ah), ph/(2*al)
        if ceil(low) == ceil(high):
            return ceil(low)-1
        digits *= 2


def beta_ratio_floor(n):
    if n == 0:
        return 0
    digits = 12
    while True:
        pl, ph = pi_bounds(digits)
        low, high = n*ph/(ph-2), n*pl/(pl-2)
        if floor(low) == floor(high):
            return floor(low)
        digits *= 2


def zero(n):
    low, high = beta_ratio_floor(n-1)+1, beta_ratio_floor(n)
    assert high-low+1 in (2, 3)
    for k in range(low, high+1):
        if k-cot_floor(k+1) == n:
            return k
    raise AssertionError((n, low, high))


def audit():
    for name, formula in [('A248520', zero), ('A248521', one)]:
        rows = [tuple(map(int, line.split())) for line in
                Path(__file__).with_name(f'published-{name}.txt').read_text().splitlines()
                if line and not line.startswith('#')]
        for n, expected in rows:
            assert formula(n) == expected, (name, n)
        print(f'PASS {len(rows)} official b-file prefix terms for {name}', flush=True)
    outputs = [[], []]
    previous = 0
    for k in range(1, 3001):
        current = cot_floor(k+1)
        difference = current-previous
        assert difference in (0, 1)
        outputs[difference].append(k)
        assert len(outputs[1]) == current
        assert len(outputs[0]) == k-current
        previous = current
    for values, formula in zip(outputs, [zero, one]):
        for n, expected in enumerate(values, 1):
            assert formula(n) == expected, (n, expected)
    print('PASS direct certified cotangent differences for k=1..3000, both exact formulas and counts')
    for n in (10**6+3, 10**12+39, 10**30+57):
        k = one(n)
        assert cot_floor(k) == n-1 and cot_floor(k+1) == n
        k = zero(n)
        assert k-cot_floor(k+1) == n
        assert k-1-cot_floor(k) == n-1
    print('PASS exact large-index boundary checks through n=10^30+57')


if __name__ == '__main__':
    audit()
