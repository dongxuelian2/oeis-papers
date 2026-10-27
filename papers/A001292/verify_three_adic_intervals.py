#!/usr/bin/env python3
"""Exact checks of the cubic 3-adic law and complete v_3(d)=1 classification.

Literal rotations and matrix appending are independent of the cubic formula.
Local witnesses are also checked by constructing roots modulo powers of 3.
"""
from verify_a001292 import append_block, direct_prefix_mod, digits_total
from verify_boundary_valuations import valuation


EXTRA = {1: {0, 27, 54, 135, 189}, 2: {54, 108, 162, 189, 216}}


def excluded(m, d):
    assert valuation(d) == 1
    return (m % 9 in (2, 3, 5, 6) or m % 27 in (9, 17)
            or m % 243 in EXTRA[(d//3) % 3])


def cubic(m, k, d, mod):
    m %= mod
    return (m*(m+1)//2+3*d*pow(2, -1, mod)*(m**3-m+9)
            -9*d*m*(k*(k+1)//2)) % mod


def local_power(n, precision):
    """Return a certified exponent in {2,3,5}; zero means unknown at precision."""
    n %= 3**precision
    if not n:
        return 0
    b = valuation(n)
    unit = n//3**b
    if b % 2 == 0 and unit % 3 == 1:
        return 2
    if b % 3 == 0 and precision-b >= 2 and unit % 9 in (1, 8):
        return 3
    if b % 5 == 0:
        return 5
    return 0


def root_certificate(n, e, precision):
    """Construct an actual root of the witnessed residue modulo 3**precision."""
    mod = 3**precision
    n %= mod
    assert n
    b = valuation(n)
    assert b % e == 0
    unit, count = n//3**b, precision-b
    roots = [x for x in (1, 2) if pow(x, e, 3) == unit % 3]
    step = 3
    for _ in range(1, count):
        lifted = 3*step
        roots = [x+t*step for x in roots for t in range(3)
                 if pow(x+t*step, e, lifted) == unit % lifted]
        assert roots, (e, b, unit, lifted)
        step = lifted
    root = 3**(b//e)*roots[0]
    assert pow(root, e, mod) == n


def literal_audit():
    precision, mod = 8, 3**8
    low = 243
    words, lengths = [0], [0]
    W = D = rotations = witnesses = 0
    inv10 = {j: pow(10, -j, low) for j in (1, 2, 3)}
    for m in range(1, 1000):
        width = len(str(m))
        W = (W*10**width+m) % mod
        D += width
        words.append(W)
        lengths.append(D)
        if m < 100:
            continue
        whole_excluded = excluded(m, 3)
        shift = (pow(10, D, mod)-1) % mod
        R, inverse_cut = W, 1
        witness = None
        for k in range(m):
            assert R*inverse_cut % low == cubic(m, k, 3, low), (m, k)
            e = local_power(R, precision)
            if whole_excluded:
                assert R and valuation(R) <= 4 and not e, (m, k)
            elif k < 4 and e and witness is None:
                witness = R, e
            j = len(str(k+1))
            R = (R*10**j-shift*(k+1)) % mod
            inverse_cut = inverse_cut*inv10[j] % low
            rotations += 1
        assert R == W
        if not whole_excluded:
            assert witness is not None, m
            root_certificate(*witness, precision)
            witnesses += 1
    print(f'PASS: {rotations} rotation residues for all m=100..999; '
          f'{witnesses} first-four-cut witnesses with constructed roots mod 3**8', flush=True)

    count = 0
    for m in (135, 189, 243, 486, 729, 972):
        text = ''.join(str(j) for j in range(1, m+1))
        cut = 0
        for k in range(m):
            R = int(text[cut:]+text[:cut])
            assert R % mod == (pow(10, lengths[k], mod)*words[m]
                               -(pow(10, lengths[m], mod)-1)*words[k]) % mod
            assert excluded(m, 3) and not local_power(R, precision)
            assert valuation(R) in (3, 4)
            cut += len(str(k+1))
            count += 1
    print(f'PASS: {count} complete integer rotations of six new explicit examples', flush=True)


def classification_grid():
    count = 0
    for d in (3, 6, 12, 15, 21, 24):
        found = set()
        for m in range(243):
            fails = []
            for k in range(9):
                n = cubic(m, k, d, 243)
                fails.append(bool(n) and not local_power(n, 5))
                count += 1
            if all(fails):
                found.add(m)
        expected = {m for m in range(243) if excluded(m, d)}
        assert found == expected and len(found) == 131, d
        old = {m for m in range(243)
               if m % 9 in (2, 3, 5, 6) or m % 27 in (9, 17)}
        assert len(old) == 126 and found-old == EXTRA[(d//3) % 3]
    # The negative critical branch is handled without a zero-residue escape.
    for u in (1, 2, 4, 5, 7, 8):
        for z in range(9):
            q = (3*u-z)*pow(2, -1, 9) % 9
            values = {(q+u*t) % 9 for t in (0, 3, 6)}
            assert len(values) == 3 and values & {1, 3, 8}
    print(f'PASS: all {count} cubic class/cut combinations; six exact '
          '131-class sets; all 54 negative-branch cosets', flush=True)


def first_in_class(lower, residue, period):
    return lower+(residue-lower) % period


def matrix_audit():
    rotations = endpoints = witnesses = 0
    for d in (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 81, 243):
        h = valuation(d)
        precision = max(8, h+4)
        mod, theorem_mod = 3**precision, 3**(h+4)
        prefix, lower, before_length = 0, 1, 0
        for width in range(1, d):
            prefix = append_block(prefix, lower, 9*lower, width, mod)
            before_length += 9*width*lower
            lower *= 10
        upper = 10*lower-1
        samples = {lower, upper, (lower+upper)//2}
        if h == 1:
            samples.update(lower+j for j in range(243))
        for r, period in ((0, 3**(h+2)), (0, theorem_mod),
                          (-27*d, theorem_mod), (-1, 3**(h+2))):
            samples.add(first_in_class(lower, r, period))
        samples = sorted(m for m in samples if lower <= m <= upper)
        for m in samples:
            count = m-lower+1
            W = append_block(prefix, lower, count, d, mod)
            D = before_length+d*count
            assert D == digits_total(m)
            shift = (pow(10, D, mod)-1) % mod
            assert W % theorem_mod == cubic(m, 0, d, theorem_mod), (d, m % 10000)
            cuts = {0: (0, 0), lower-1: (prefix, before_length)}
            for k in (1, 2, 3, 8, 9, 41, 99, 100):
                if k < m:
                    cuts[k] = direct_prefix_mod(k, mod), digits_total(k)
            cuts[m-1] = append_block(prefix, lower, count-1, d, mod), D-d
            candidate = None
            for k, (Wk, Dk) in cuts.items():
                R = (pow(10, Dk, mod)*W-shift*Wk) % mod
                assert R*pow(10, -Dk, theorem_mod) % theorem_mod == cubic(m, k, d, theorem_mod)
                if m % 3**(h+2) == 0:
                    assert R % theorem_mod == (m+27*d)*pow(2, -1, theorem_mod) % theorem_mod
                if m % theorem_mod == 0:
                    assert valuation(R) == h+3
                    assert R//3**(h+3) % 3 == (d//3**h)*2 % 3
                if h == 1:
                    e = local_power(R, precision)
                    if excluded(m, d):
                        assert R and valuation(R) <= 4 and not e
                    elif k < 4 and e and candidate is None:
                        candidate = R, e
                rotations += 1
            if h == 1 and not excluded(m, d):
                assert candidate is not None, (d, m % 243)
                root_certificate(*candidate, precision)
                witnesses += 1
            endpoints += 1
        print(f'PASS: independent matrix interval d={d}, h={h}, '
              f'{len(samples)} full prefixes', flush=True)
    print(f'PASS: {endpoints} matrix prefixes, {rotations} cubic/rotation checks, '
          f'{witnesses} constructed local root witnesses', flush=True)


def main():
    classification_grid()
    literal_audit()
    matrix_audit()


if __name__ == '__main__':
    main()
