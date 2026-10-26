#!/usr/bin/env python3
"""Exact all-index A346644 minima using the proved reduced-factor normal form.

The evaluator searches prime-power factorizations, not successive integers.
Every exponent plus one is n-smooth, and each local divisor mean is reduced.
An elementary construction supplies a finite upper bound. See minimum.tex.
"""
import argparse
from functools import lru_cache
from itertools import permutations
from math import gcd

from verify import denominator_from_factors, factor, is_prime, partition_minimum


def valuation(n, p):
    assert n > 0
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def prime_stream(start=2):
    if start <= 2:
        yield 2
    p = max(3, start | 1)
    while True:
        if is_prime(p):
            yield p
        p += 2


def capped_power(p, e, limit):
    """p**e if <=limit, else None; intermediate integers stay bounded."""
    if limit < 1:
        return None
    value = 1
    while e:
        if e & 1:
            if p > limit // value:
                return None
            value *= p
        e //= 2
        if e:
            p = limit + 1 if p > limit // p else p*p
    return value


def floor_root(n, e):
    assert n >= 1 and e >= 1
    if e == 1:
        return n
    lo, hi = 1, 1 << ((n.bit_length()+e-1)//e)
    while lo < hi:
        mid = (lo+hi+1)//2
        if capped_power(mid, e, n) is None:
            hi = mid-1
        else:
            lo = mid
    return lo


def floor_log(n, p):
    e, power = 0, 1
    while power <= n//p:
        power *= p
        e += 1
    return e


@lru_cache(None)
def smooth_numbers(primes, limit):
    values = [1]
    for p in primes:
        expanded = []
        for v in values:
            while v <= limit:
                expanded.append(v)
                v *= p
        values = expanded
    return tuple(sorted((v for v in values if v >= 2), reverse=True))


def normalize(fs):
    """Construct a divisor with the same denominator and reduced local means."""
    target = denominator_from_factors(fs)
    ps, ms = [p for p, _ in fs], [e+1 for _, e in fs]
    tau_primes = sorted({q for m in ms for q, _ in factor(m)})
    for q in tau_primes:
        capacities = [valuation(m, q) for m in ms]
        ms = [m//q**b for m, b in zip(ms, capacities)]
        if target % q:
            continue
        sums = [(p**m-1)//(p-1) for p, m in zip(ps, ms)]
        need = valuation(target, q) + sum(valuation(s, q) for s in sums)
        for i, (p, s, capacity) in enumerate(zip(ps, sums, capacities)):
            if p % q == 1 or s % q == 0:
                continue
            take = min(need, capacity)
            ms[i] *= q**take
            need -= take
        assert need == 0, (fs, q, target)
    return [(p, m-1) for p, m in zip(ps, ms) if m > 1]


def order_mod_prime(a, q):
    assert a % q
    h = q-1
    for r, _ in factor(h):
        while h % r == 0 and pow(a, h//r, q) == 1:
            h //= r
    return h


def weak_compositions(total, length):
    if length == 0:
        if total == 0:
            yield ()
    elif length == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in weak_compositions(total-first, length-1):
                yield (first,)+rest


def triangular_candidates(n, primes, ceiling=None):
    """The formula's allocations for a fixed distinct-prime tuple.

    This generator is independent of the branch-and-bound minimum search.
    Its outputs automatically have denominator n; no denominator filter is
    used. A ceiling, if supplied, only prunes products already exceeding it.
    """
    assert len(primes) == len(set(primes)) and all(is_prime(p) for p in primes)
    qs = factor(n)

    def allocate(stage, ms):
        if stage == len(qs):
            yield [(p, m-1) for p, m in zip(primes, ms) if m > 1]
            return
        q, s = qs[stage]
        good, budget = [], s
        for i, (p, m) in enumerate(zip(primes, ms)):
            if p == q:
                good.append(i)
            elif p % q != 1:
                h = order_mod_prime(p, q)
                if m % h:
                    good.append(i)
                else:
                    budget += valuation(p**h-1, q)
        for allocation in weak_compositions(budget, len(good)):
            updated = ms.copy()
            for i, b in zip(good, allocation):
                updated[i] *= q**b
            if ceiling is not None:
                partial = 1
                for p, m in zip(primes, updated):
                    power = capped_power(p, m-1, ceiling//partial)
                    if power is None:
                        break
                    partial *= power
                else:
                    yield from allocate(stage+1, updated)
            else:
                yield from allocate(stage+1, updated)

    yield from allocate(0, [1]*len(primes))


def elementary_witness(n):
    """The fixed, non-Dirichlet construction used to bound the formula."""
    primes = prime_stream()
    sigma, value, fs = 1, 1, []
    for q, s in factor(n):
        p = next(primes)  # the i-th prime is <= the i-th divisor prime q
        b = s + valuation(sigma, q)
        m = q**b
        power = p**(m-1)
        value *= power
        sigma *= (p*power-1)//(p-1)
        fs.append((p, m-1))
    return value, fs


def small_witness(n):
    """A cheaper proved witness; singleton allocations and a few base choices."""
    qs = factor(n)
    sigma, upper, fs, used = 1, 1, [], set()
    for q, s in qs:
        budget = s + valuation(sigma, q)
        choices = []
        for p in prime_stream():
            if p not in used and p % q != 1:
                choices.append(p)
                if len(choices) == (1 if q == 2 else budget):
                    break
        for p in choices:
            m = q**budget if q == 2 else q
            power = p**(m-1)
            upper *= power
            sigma *= (p*power-1)//(p-1)
            used.add(p)
            fs.append((p, m-1))
    # This is an optional improvement to the valid bound, not a completeness
    # assumption. Exhaustive minimum search below is independent of its success.
    if len(qs) <= 3:
        stream = prime_stream()
        pool = [next(stream) for _ in range(len(qs)+2)]
        for assignment in permutations(pool, len(qs)):
            if any(p % q == 1 for p, (q, _) in zip(assignment, qs)):
                continue
            candidate, sigma, trial = 1, 1, []
            for p, (q, s) in zip(assignment, qs):
                m = q**(s + valuation(sigma, q))
                power = capped_power(p, m-1, (upper-1)//candidate)
                if power is None:
                    break
                candidate *= power
                sigma *= (p*power-1)//(p-1)
                trial.append((p, m-1))
            else:
                upper, fs = candidate, trial
    assert denominator_from_factors(fs) == n
    return upper, sorted(fs)


def least(n, statistics=False):
    if n < 1:
        raise ValueError('n must be positive')
    qs = factor(n)
    if not qs:
        return (1, {'nodes': 0, 'factors': []}) if statistics else 1
    if len(qs) == 1:
        result = partition_minimum(*qs[0])
        return (result, {'nodes': 0, 'prime_power_formula': True}) if statistics else result
    best, best_fs = small_witness(n)
    support = tuple(q for q, _ in qs)
    targets = tuple(s for _, s in qs)
    nodes = 0

    def visit(value, previous, net, fs):
        nonlocal best, best_fs, nodes
        nodes += 1
        if net == targets:
            if value < best:
                best, best_fs = value, fs
            return
        needed = max(1, sum(max(0, s-c)*(q-1) for (q, s), c in zip(qs, net)))
        maximum_prime = floor_root((best-1)//value, needed)
        for p in prime_stream(previous+1):
            if p > maximum_prime or (not fs and n % 2 == 0 and p != 2):
                break
            if capped_power(p, needed, (best-1)//value) is None:
                break
            limit = floor_log((best-1)//value, p)+1
            for m in smooth_numbers(support, limit):
                if p == 2 and valuation(m, 2) != (targets[0] if support[0] == 2 else 0):
                    continue
                power = capped_power(p, m-1, (best-1)//value)
                if power is None:
                    continue
                sigma = (p*power-1)//(p-1)
                if gcd(m, sigma) != 1:
                    continue
                new_net = tuple(c + valuation(m, q)-valuation(sigma, q)
                                for c, q in zip(net, support))
                visit(value*power, p, new_net, fs+[(p, m-1)])

    visit(1, 1, (0,)*len(qs), [])
    assert denominator_from_factors(best_fs) == n
    return (best, {'nodes': nodes, 'factors': best_fs}) if statistics else best


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('indices', nargs='*', type=int)
    parser.add_argument('--table', type=int, metavar='N', help='print terms 1 through N')
    parser.add_argument('--statistics', action='store_true')
    args = parser.parse_args()
    if args.table is not None and args.table < 1:
        parser.error('--table must be positive')
    if not args.indices and args.table is None:
        parser.error('supply indices or --table N')
    for n in list(range(1, args.table+1)) if args.table is not None else args.indices:
        print(n, least(n, args.statistics), flush=True)
