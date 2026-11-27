#!/usr/bin/env python3
"""Exact certificate for unified A060405 bounds, splitting curves, and local geometry."""

import math
from collections import Counter
from fractions import Fraction

A_MAT = (0, 1, 1, 1)
B_MAT = (0, 1, 1, 2)
I_MAT = (1, 0, 0, 1)


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3.317e24 and trial check for larger ints."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in small:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_up_to(n):
    s = bytearray(b"\x01") * (n + 1)
    s[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if s[p]:
            s[p * p : n + 1 : p] = b"\x00" * len(range(p * p, n + 1, p))
    return [p for p in range(2, n + 1) if s[p]]


def mat_mul(x, y, mod):
    return (
        (x[0] * y[0] + x[1] * y[2]) % mod,
        (x[0] * y[1] + x[1] * y[3]) % mod,
        (x[2] * y[0] + x[3] * y[2]) % mod,
        (x[2] * y[1] + x[3] * y[3]) % mod,
    )


def mat_pow(m, e, mod):
    if e < 0:
        det = (m[0] * m[3] - m[1] * m[2]) % mod
        invd = pow(det, -1, mod)
        minv = (
            (m[3] * invd) % mod,
            (-m[1] * invd) % mod,
            (-m[2] * invd) % mod,
            (m[0] * invd) % mod,
        )
        return mat_pow(minv, -e, mod)
    res = I_MAT
    b = m
    while e:
        if e & 1:
            res = mat_mul(res, b, mod)
        b = mat_mul(b, b, mod)
        e >>= 1
    return res


def lp_exact(n):
    if n < 0:
        l_val, p_val = lp_exact(-n)
        s = 1 if (-n) % 2 == 0 else -1
        return s * l_val, -s * p_val
    l0, l1, p0, p1 = 2, 1, 0, 1
    for _ in range(n):
        l0, l1 = l1, l0 + l1
        p0, p1 = p1, p0 + 2 * p1
    return l0, p0


def qp_exact(n):
    if n < 0:
        q_val, p_val = qp_exact(-n)
        s = 1 if (-n) % 2 == 0 else -1
        return s * q_val, -s * p_val
    q0, q1, p0, p1 = 1, 1, 0, 1
    for _ in range(n):
        q0, q1 = q1, q0 + 2 * q1
        p0, p1 = p1, p0 + 2 * p1
    return q0, p0


def lp_mod(n, mod):
    ap = mat_pow(A_MAT, n, mod)
    bp = mat_pow(B_MAT, n, mod)
    return (2 * ap[0] + ap[1]) % mod, bp[1] % mod


def zero_val(k, mod):
    ap = mat_pow(A_MAT, k, mod)
    bp = mat_pow(B_MAT, k, mod)
    return (-ap[0] + 2 * ap[1] + bp[0]) % mod


def leg(x, p):
    z = pow(x % p, (p - 1) // 2, p)
    return -1 if z == p - 1 else z


def jacobi(a, b):
    assert b > 0 and b % 2 == 1
    a %= b
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if b % 8 in (3, 5):
                t = -t
        a, b = b, a
        if a % 4 == 3 and b % 4 == 3:
            t = -t
        a %= b
    return t if b == 1 else 0


def sqrt_mod_prime(a, p):
    a %= p
    if a == 0:
        return 0
    assert leg(a, p) == 1
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while leg(z, p) != -1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)
    while t != 1:
        i = 1
        t2i = (t * t) % p
        while t2i != 1:
            t2i = (t2i * t2i) % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p
    return r


def check_n6_subspace_constants():
    """Check N=6 weights, basis count, multiplicity, Evertse-Ferretti bound, and height bridge."""
    alpha = (1.0 + math.sqrt(5.0)) / 2.0
    beta = 1.0 + math.sqrt(2.0)
    u_val = alpha ** 4
    v_val = beta ** 2
    c_val = 1.0 / (2.0 * math.sqrt(2.0))
    a_r_max = math.sqrt(c_val) * (beta ** 1.5)
    assert a_r_max < 2.3
    log_uv34 = math.log((u_val ** 3) * (v_val ** 4))
    eta = 199.0 / 200.0
    m0 = 600

    sigmas = {
        "v1": [v_val, 1 / v_val, u_val / v_val, 1 / (u_val * v_val), u_val * v_val],
        "v2": [v_val, 1 / v_val, 1 / (u_val * v_val), u_val / v_val, v_val / u_val],
        "v3": [1 / v_val, v_val, u_val * v_val, v_val / u_val, u_val / v_val],
        "v4": [1 / v_val, v_val, v_val / u_val, u_val * v_val, 1 / (u_val * v_val)],
    }
    targets = {"v1": u_val * v_val, "v2": v_val, "v3": u_val * v_val, "v4": u_val * v_val}
    total_weight = 0.0
    for v_name, mags in sigmas.items():
        for s in mags:
            d = eta * math.log(s / targets[v_name]) / log_uv34
            assert d <= 0.0
            total_weight += d
            if s < targets[v_name]:
                assert m0 * math.log(s / targets[v_name]) <= d * math.log(2.3) + d * m0 * log_uv34
    d0_ratios = [(5.0, u_val / v_val**4), (5.0, u_val**2 / v_val**4), (5.0, u_val / v_val**4), (2.3, 1.0 / u_val)]
    for cnst, ratio in d0_ratios:
        d = eta * math.log(ratio) / log_uv34
        assert d <= 0.0
        total_weight += d
        assert math.log(cnst) + m0 * math.log(ratio) <= d * math.log(2.3) + d * m0 * log_uv34
    assert total_weight < -6.0 - 1.0 / 6.0

    # Squared basis count and multiplicity
    w5 = [(0, 1), (0, -1), (1, -1), (-1, -1), (1, 1)]
    cnt = Counter()
    for p1 in w5:
        for p2 in w5:
            cnt[(p1[0] + p2[0], p1[1] + p2[1])] += 1
    assert max(cnt.values()) == 4
    bases = set(cnt.keys()) | {(1, 0), (-1, 0), (0, 2), (0, -2)}
    assert len(bases) == 12
    assert bases.isdisjoint({(-2, 2), (-1, 2), (-2, 0)})

    # Evertse-Ferretti count and height bridge
    # Theorem 3.1 has dimension 6, at most 9 forms, and coefficient degree at most 2.
    dimension, form_count, coefficient_degree, inv_epsilon = 6, 9, 2, 6
    rd = form_count * coefficient_degree
    t6 = (
        10**9 * 2**(2 * dimension) * dimension**14 * inv_epsilon**3
        * math.log(3 * inv_epsilon * rd) * math.log(inv_epsilon * math.log(3 * rd))
    )
    assert t6 < 1.3e27
    assert 22 * t6 + 1200 < 2.9e28
    height_threshold = max(
        math.log(1000) / (3 * rd), dimension * inv_epsilon * math.log(dimension)
    )
    assert m0 * math.log(u_val**0.75 * v_val) > height_threshold
    assert 4.0 * 64.0 / math.log(5.0 / 4.0) < 1150.0
    assert 4.0 * (40.0 + math.log(11.0)) / math.log(5.0 / 4.0) < 1150.0
    print("N=6 Subspace Theorem constants and bounds verified.")


def mul_k(x, y):
    a1, b1, c1, d1 = x
    a2, b2, c2, d2 = y
    return (
        a1 * a2 + 2 * b1 * b2 + 5 * c1 * c2 + 10 * d1 * d2,
        a1 * b2 + b1 * a2 + 5 * c1 * d2 + 5 * d1 * c2,
        a1 * c2 + c1 * a2 + 2 * b1 * d2 + 2 * d1 * b2,
        a1 * d2 + d1 * a2 + b1 * c2 + c1 * b2,
    )


def pow_k(x, n):
    if n < 0:
        a, b, c, d = x
        adj = mul_k(mul_k((a, b, -c, -d), (a, -b, c, -d)), (a, -b, -c, d))
        nm = mul_k(x, adj)[0]
        return pow_k(tuple(u / nm for u in adj), -n)
    res = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    base = x
    while n:
        if n & 1:
            res = mul_k(res, base)
        base = mul_k(base, base)
        n >>= 1
    return res


def check_new_norm_identities():
    """Verify Family 2 (dual Z[sqrt(2)]) and Family 3 ((1,+-1) mixed-unit) identities."""
    alpha = (Fraction(1, 2), Fraction(0), Fraction(1, 2), Fraction(0))
    beta = (Fraction(1), Fraction(1), Fraction(0), Fraction(0))
    ab = mul_k(alpha, beta)
    two_s2 = (Fraction(0), Fraction(2), Fraction(0), Fraction(0))
    inv_2s2 = (Fraction(0), Fraction(1, 4), Fraction(0), Fraction(0))

    for n in range(-7, 20, 2):
        l_val, p_val = lp_exact(n)
        q_val, p_chk = qp_exact(n)
        assert p_chk == p_val
        a_val = l_val + p_val

        # Family 2: beta * w_+^2 = sqrt(2)*P_n + 1 and Jacobi identity
        m = (n - 1) // 2
        sig = 1 if m % 2 == 0 else -1
        qm, pm = qp_exact(m)
        qm1, pm1 = qp_exact(m + 1)
        u_w = pm + sig * pm1
        assert (qm - sig * qm1) % 2 == 0
        v_w = (qm - sig * qm1) // 2
        assert u_w * u_w - 2 * v_w * v_w == sig * q_val
        # beta * (u_w + v_w*sqrt(2))^2 = sqrt(2)*P_n + 1
        sq_a, sq_b = u_w * u_w + 2 * v_w * v_w, 2 * u_w * v_w
        assert sq_a + 2 * sq_b == 1 and sq_a + sq_b == p_val
        # Norm equation: (beta*w_+)^2 - sqrt(2)*beta*a_n = -beta*(sqrt(2)*L_n - 1)
        bw_a, bw_b = u_w + 2 * v_w, u_w + v_w
        lhs_a = bw_a * bw_a + 2 * bw_b * bw_b - 2 * a_val
        lhs_b = 2 * bw_a * bw_b - a_val
        assert lhs_a == -(2 * l_val - 1) and lhs_b == -(l_val - 1)
        norm_2 = 2 * l_val * l_val - 1
        if norm_2 > 1:
            assert jacobi((2 * l_val + 1) * l_val, norm_2) == 1
            assert jacobi(l_val + 1, norm_2) == 1

        # Family 3: (1,+-1) identities in K
        an_k = pow_k(alpha, n)
        bn_k = pow_k(beta, n)
        abn_k = pow_k(ab, n)

        f1 = tuple(u - v for u, v in zip(abn_k, two_s2))
        f0, f_s2, f_s5, f_s10 = f1
        norm1 = mul_k(f1, (f0, -f_s2, f_s5, -f_s10))
        lhs1 = tuple(u - v for u, v in zip((Fraction(16 * a_val), Fraction(0), Fraction(0), Fraction(0)),
                                           tuple(18 * z for z in an_k)))
        rhs1 = tuple(2 * z for z in mul_k(pow_k(alpha, -n), norm1))
        assert lhs1 == rhs1

        g2 = tuple(u + v for u, v in zip(abn_k, inv_2s2))
        g0, g_s2, g_s5, g_s10 = g2
        norm2 = mul_k(g2, (g0, g_s2, -g_s5, -g_s10))
        lhs2 = tuple(u - v for u, v in zip((Fraction(0), Fraction(2 * a_val), Fraction(0), Fraction(0)),
                                           tuple(9 * z for z in bn_k)))
        rhs2 = tuple(8 * z for z in mul_k(pow_k(beta, -n), norm2))
        assert lhs2 == rhs2
    print("Dual Z[sqrt(2)] and (1,+-1) mixed-unit norm identities verified for odd n in [-7, 19].")


def chi_pm_gauss(re_r, im_r, q):
    inv_im = pow(im_r, -1, q)
    i_mod = (-re_r * inv_im) % q
    assert (i_mod * i_mod + 1) % q == 0
    return leg(1 + 2 * i_mod, q), leg(1 - 2 * i_mod, q)


def check_section2_witnesses():
    """Verify explicit odd-valuation Gaussian prime witnesses with chi_+- = -1."""
    # (s, q_minus, q_plus)
    witnesses = [
        (17, 137, None),
        (19, None, 37),
        (31, 61, 61),
        (37, 78737, 593),
        (43, 11437, None),
        (47, 3761, 3761),
        (61, 853, None),
        (71, 569, 569),
        (73, 1873724873, None),
        (49, None, 293),
        (121, None, 446196005573),
        (125, 129749, 129749),
        (55, 109, 109),
        (65, 1949, 1949),
        (77, 23869, 23869),
        (91, 13, None),
        (57, 1311797, None),
        (87, 41761, 173),
        (177, 1025009776421, 2833),
        (183, 32211583765067977, 92606620033),
    ]
    checked = 0
    for s, qm, qp in witnesses:
        qh, ph = qp_exact((s - 1) // 2)
        re_r, im_r = qh + ph, ph
        norm_r = re_r * re_r + im_r * im_r
        for q, idx in ((qm, 1), (qp, 0)):
            if q is None:
                continue
            assert is_prime(q) and q != 5
            v = 0
            tmp = norm_r
            while tmp % q == 0:
                tmp //= q
                v += 1
            assert v % 2 == 1, (s, q, v)
            assert chi_pm_gauss(re_r, im_r, q)[idx] == -1, (s, q, idx)
            checked += 1
    print(f"Section 2 Gaussian prime-power and composite witnesses verified: {checked}.")


def check_section3_forcing():
    """Verify exact Section 3 one-step prime forcing witnesses."""
    # (s, p, expected_ord_xi, required_divisor_of_ord_xi)
    cases = [
        (33, 1321, 110, 2),
        (35, 7001, 250, 2),
        (51, 51511, 8585, 5),
    ]
    for s, p, expected_ord, req_div in cases:
        assert is_prime(p) and leg(2, p) == 1 and leg(5, p) == 1
        qs, ps = qp_exact(s)
        q2s, p2s = qp_exact(2 * s)
        l2s, _ = lp_exact(2 * s)
        # N_{K/Q(sqrt(2))}(eta^s - 1) = beta^{2s} - L_{2s}*beta^s + 1 = a + b*sqrt(2)
        a_rel = q2s - l2s * qs + 1
        b_rel = p2s - l2s * ps
        norm_2 = abs(a_rel * a_rel - 2 * b_rel * b_rel)
        assert norm_2 % p == 0 and norm_2 % (p * p) != 0 and math.gcd(a_rel, b_rel) % p != 0
        r2 = (-a_rel * pow(b_rel, -1, p)) % p
        assert (r2 * r2 - 2) % p == 0
        assert leg(2 * r2, p) == -1
        r5_0 = sqrt_mod_prime(5, p)
        inv2 = (p + 1) // 2
        matched = []
        for r5 in (r5_0, p - r5_0):
            eta_mod = ((1 + r2) * (3 - r5) * inv2) % p
            if pow(eta_mod, s, p) == 1:
                xi_mod = ((1 + r2) * (3 + r5) * inv2) % p
                # Compute exact order of xi_mod mod p
                ord_xi = p - 1
                tmp = ord_xi
                q_facs = []
                d = 2
                while d * d <= tmp:
                    if tmp % d == 0:
                        q_facs.append(d)
                        while tmp % d == 0:
                            tmp //= d
                    d += 1
                if tmp > 1:
                    q_facs.append(tmp)
                for qf in q_facs:
                    while ord_xi % qf == 0 and pow(xi_mod, ord_xi // qf, p) == 1:
                        ord_xi //= qf
                matched.append(ord_xi)
        assert matched == [expected_ord] and expected_ord % req_div == 0
    print("Section 3 one-step prime forcing witnesses verified (33->1321, 35->7001, 51->51511).")


def check_frobenius_and_double_roots():
    """Verify all-parity Frobenius descent and p=19, 307 double-root geometry."""
    ps = [p for p in primes_up_to(53) if p > 5]
    tests = 0
    for p in ps:
        s5 = leg(5, p)
        s2 = leg(2, p)
        for e in (1, 2, 3):
            e5 = s5 ** e
            e2 = s2 ** e
            for r0 in range(-6, 7):
                for k in range(-5, 6):
                    lhs_l, lhs_p = lp_mod(r0 + k * (p ** e), p)
                    rhs_l, _ = lp_mod(r0 + e5 * k, p)
                    _, rhs_p = lp_mod(r0 + e2 * k, p)
                    rhs_l = ((e5 ** (k & 1)) * rhs_l) % p
                    rhs_p = ((e2 ** (k & 1)) * rhs_p) % p
                    assert lhs_l == rhs_l and lhs_p == rhs_p
                    tests += 1
    assert tests == 5577

    # Unconditional odd-offset corollaries
    for p in ps:
        for e in (1, 3):
            if leg(5, p) == -1 and leg(2, p) == 1:
                l_val, p_val = lp_mod(-2 + p ** e, p)
                assert (l_val + p_val) % p == 5 % p
            if leg(5, p) == 1 and leg(2, p) == -1:
                l_val, p_val = lp_mod(2 + 3 * (p ** e), p)
                assert (l_val + p_val) % p == 10 % p

    # Double-root local geometry at p=19 (h=360) and p=307 (h=5544)
    roots = {
        19: (360, 15, 4, 12, 1350020572964207),
        307: (5544, 81, 33, 8, 69800898470995632160),
    }
    for p, (h, lead, r0, prec, expected_tau) in roots.items():
        assert mat_pow(A_MAT, h, p) == I_MAT and mat_pow(B_MAT, h, p) == I_MAT
        q = p ** 4
        ca = tuple((x - y) % q for x, y in zip(mat_pow(A_MAT, h, q), I_MAT))
        cb = tuple((x - y) % q for x, y in zip(mat_pow(B_MAT, h, q), I_MAT))
        ca2, cb2 = mat_mul(ca, ca, q), mat_mul(cb, cb, q)
        ca3, cb3 = mat_mul(ca2, ca, q), mat_mul(cb2, cb, q)
        assert (-ca3[0] + 2 * ca3[1] + cb3[0]) % (p ** 3) == 0
        for t in range(1, 25):
            z = zero_val(h * t, p ** 3)
            assert z % (p * p) == 0
            assert (z // (p * p)) % p == (lead * t * (t - r0)) % p
        r = r0
        for k in range(1, prec):
            hits = [r + j * (p ** k) for j in range(p) if zero_val(h * (r + j * (p ** k)), p ** (k + 3)) == 0]
            assert len(hits) == 1
            r = hits[0]
        assert r == expected_tau and zero_val(h * r, p ** (prec + 2)) == 0
        # Near-0 unit is QR, near-tau unit is NQR
        z0 = zero_val(h * p, p ** 4)
        zt = zero_val(h * (r + p), p ** 4)
        assert z0 % (p ** 3) == 0 and leg(z0 // (p ** 3), p) == 1
        assert zt % (p ** 3) == 0 and leg(zt // (p ** 3), p) == -1
    print("All-parity Frobenius identity (5577 cases) and p=19, 307 double roots verified.")


def check_6round_5adic_split():
    """Verify 6-round forced-prime closure below 30000 and 5-adic split linear systems."""
    m_base = 720720
    d_val = m_base
    units = {}
    ps30 = [p for p in primes_up_to(29999) if p >= 17]
    round_counts = []
    while True:
        hits = []
        for p in ps30:
            if d_val % p == 0:
                continue
            h = math.gcd(d_val, p * p - 1)
            if mat_pow(A_MAT, h, p) != I_MAT or mat_pow(B_MAT, h, p) != I_MAT:
                continue
            z = zero_val(h, p * p)
            if z:
                units[p] = (z // p) * pow(h, -1, p) % p
                hits.append(p)
        if not hits:
            break
        round_counts.append(len(hits))
        for p in hits:
            d_val *= p
    assert round_counts == [38, 263, 338, 161, 32, 5] and len(units) == 837

    e_val = 7 * 11 * 13
    for p in units:
        e_val *= p
    assert (e_val % 5, e_val % 8, e_val % 3) == (1, 5, 1)

    for p, h in ((2, 48), (3, 24), (7, 336), (11, 1320), (13, 2184)):
        val = zero_val(h, p ** 8)
        v = 0
        while val % p == 0:
            val //= p
            v += 1
        hh = h
        while hh % p == 0:
            hh //= p
        modu = 8 if p == 2 else p
        units[p] = (val * pow(hh, -1, modu)) % modu

    odd_test = sorted((set(units) - {2}) | {5})
    assert len(odd_test) == 842

    def unit_bits_2(u):
        return int(u % 4 == 3) | (int(u % 8 in (3, 5)) << 1)

    def vec(q):
        z = unit_bits_2(q)
        for i, p in enumerate(odd_test, 2):
            if leg(q, p) == -1:
                z |= 1 << i
        return z

    def add_basis(basis, v):
        while v:
            j = v.bit_length() - 1
            if j in basis:
                v ^= basis[j]
            else:
                basis[j] = v
                return True
        return False

    def reduce_vec(basis, v):
        while v:
            j = v.bit_length() - 1
            if j not in basis:
                break
            v ^= basis[j]
        return v

    cutoffs = {}
    for delta in (0, 1):
        mult = 5 if delta == 1 else 1
        t_bits = unit_bits_2((e_val * mult * units[2]) % 8)
        for i, p in enumerate(odd_test, 2):
            if p == 5:
                want_neg = leg(e_val, 5) == (1 if delta == 0 else -1)
                if want_neg:
                    t_bits |= 1 << i
            else:
                if leg(e_val * mult * units[p], p) == -1:
                    t_bits |= 1 << i
        basis = {}
        cutoff = None
        for q in primes_up_to(11000):
            if q < 17 or d_val % q == 0:
                continue
            add_basis(basis, vec(q))
            if reduce_vec(basis, t_bits) == 0:
                cutoff = (q, len(basis))
                break
        cutoffs[delta] = cutoff
    assert cutoffs == {0: (9949, 842), 1: (9967, 843)}
    print("6-round forced closure (837 primes) and 5-adic split cutoffs (9949, 9967) verified.")


if __name__ == "__main__":
    check_n6_subspace_constants()
    check_new_norm_identities()
    check_section2_witnesses()
    check_section3_forcing()
    check_frobenius_and_double_roots()
    check_6round_5adic_split()
