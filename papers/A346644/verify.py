#!/usr/bin/env python3
"""Independent arithmetic checks of denominator witnesses and exact minima."""
from functools import lru_cache
from math import gcd, isqrt, prod


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def factor(n):
    fs, p = [], 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            fs.append((p, e))
        p += 1
    if n > 1:
        fs.append((n, 1))
    return fs


def denominator_from_factors(fs):
    sigma = prod((p**(e+1)-1)//(p-1) for p, e in fs)
    tau = prod(e+1 for _, e in fs)
    return tau // gcd(sigma, tau)


def geometric_mod(p, h, modulus):
    # Binary composition, independent of the alternating-sum proof.
    power, total = 1, 0
    block_power, block_sum = p % modulus, 1 % modulus
    while h:
        if h & 1:
            total = (total + power*block_sum) % modulus
            power = power*block_power % modulus
        block_sum = block_sum*(1+block_power) % modulus
        block_power = block_power*block_power % modulus
        h //= 2
    return total


def partitions(s, ceiling=None):
    if s == 0:
        yield ()
    else:
        for b in range(min(s, s if ceiling is None else ceiling), 0, -1):
            for tail in partitions(s-b, b):
                yield (b,)+tail


@lru_cache(None)
def partition_minimum(q, s):
    assert is_prime(q) and s >= 0
    if s == 0:
        return 1
    if q == 2:
        return 2**(2**s-1)
    ps, p = [], 2
    while len(ps) < s:
        if p % q != 1 and is_prime(p):
            ps.append(p)
        p += 1
    return min(prod(ps[i]**(q**b-1) for i, b in enumerate(part))
               for part in partitions(s))


def audit():
    exact_constructive = 0
    for n in range(1, 501):
        m, u = n, 1
        while m % 2 == 0:
            m //= 2
            u *= 2
        A, p = 2**u-1, 3
        while p % n != (n-1) % n or not is_prime(p):
            p += 2
        h, D = m*A, n*A
        S = geometric_mod(p, h, D)
        assert gcd((A*S) % D, D) == A
        assert S % n == 1 % n
        if h <= 1000:
            fs = [(2, u-1), (p, h-1)]
            assert denominator_from_factors(fs) == n
            exact_constructive += 1

    published = [1, 2, 4, 8, 16, 450, 64, 128, 36, 162, 1024, 1800,
                 4096, 1458, 144, 32768, 65536, 54450, 262144, 405000,
                 576, 118098, 4194304, 28800, 1296, 1062882, 900,
                 5832, 268435456, 115200, 1073741824, 2147483648,
                 9216, 86093442, 5184, 217800, 68719476736,
                 774840978, 102400]
    for n, K in enumerate(published, 1):
        assert denominator_from_factors(factor(K)) == n
        fs = factor(n)
        if len(fs) == 1:
            q, s = fs[0]
            assert partition_minimum(q, s) == K, (n, K)

    # Sieve sigma and tau by actual divisors, independent of factor formulas.
    limit = 100000
    sigmas, taus = [0]*(limit+1), [0]*(limit+1)
    for d in range(1, limit+1):
        for K in range(d, limit+1, d):
            sigmas[K] += d
            taus[K] += 1
    minima = {}
    for K in range(1, limit+1):
        den = taus[K]//gcd(sigmas[K], taus[K])
        minima.setdefault(den, K)
    comparisons = 0
    for n, K in enumerate(published, 1):
        if K <= limit:
            assert minima[n] == K
            comparisons += 1
    prime_power_checks = 0
    for n, K in minima.items():
        fs = factor(n)
        if len(fs) == 1:
            assert partition_minimum(*fs[0]) == K, (n, K)
            prime_power_checks += 1
    assert partition_minimum(3, 4) == 57600 == minima[81]
    assert partition_minimum(5, 2) == 1296
    print(f"PASS: 500 denominator constructions ({exact_constructive} expanded); "
          f"39 published entries; {comparisons} published minima and "
          f"{prime_power_checks} prime-power minima checked below {limit}; "
          "a(81)=57600.")


if __name__ == '__main__':
    audit()
