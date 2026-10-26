#!/usr/bin/env python3
"""Construct witnesses and compute exact minima by an independently checked DFA."""
from collections import deque
from math import prod


def digits(n, b=10):
    out = []
    while n:
        n, d = divmod(n, b)
        out.append(d)
    return tuple(reversed(out))


def nonzero_product(n, b=10):
    return prod(d for d in digits(n, b) if d)


def is_shift(m, n, b=10):
    if m % n:
        return False
    q = m // n
    while q > 1 and q % b == 0:
        q //= b
    return q == 1


def witness(n, b=10, j=1):
    m, q = n, 1
    # Remove exactly the primes supported by the base, without factoring n.
    from math import gcd
    while (g := gcd(m, b)) > 1:
        m //= g
        q *= g
    s, power = 0, 1
    while power % q:
        power *= b
        s += 1
    t, r = 1, 1 % m
    while r:
        r = (r*b+1) % m
        t += 1
    assert t <= m
    repunit = (b**(j*t)-1)//(b-1)
    return (n*b**(j*t)+repunit)*b**s, s, t, m


def minimum(n):
    """The lexicographically first shortest accepting word of the finite DFA."""
    target = str(n)
    d, P = len(target), nonzero_product(n)

    def transition(state, a):
        r, q, h = state
        w = max(1, a)
        if q % w:
            return None
        if h < d:
            h = h+1 if a == int(target[h]) else d+1
        elif h == d and a != 0:
            h = d+1
        return ((10*r+a) % n, q//w, h)

    initial = (0, P, 0)
    seen, queue = set(), deque()
    for a in range(1, 10):
        state = transition(initial, a)
        if state is not None and state not in seen:
            seen.add(state)
            queue.append((state, a, 1))
    while queue:
        state, value, length = queue.popleft()
        r, q, h = state
        if r == 0 and q == 1 and h != d:
            return value, length, len(seen)
        for a in range(10):
            next_state = transition(state, a)
            if next_state is not None and next_state not in seen:
                seen.add(next_state)
                queue.append((next_state, 10*value+a, length+1))
    raise AssertionError(f"No accepting word at n={n}")


def tau(n):
    out, p = 1, 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out *= e+1
        p += 1
    return out*2 if n > 1 else out


def brute(n, stop):
    P = nonzero_product(n)
    for m in range(2*n, stop+1, n):
        if not is_shift(m, n) and nonzero_product(m) == P:
            return m
    raise AssertionError((n, stop))


def audit():
    count = 0
    for b in range(2, 17):
        for n in range(1, 201):
            for j in (1, 2, 3):
                M, s, t, m = witness(n, b, j)
                assert M % n == 0 and not is_shift(M, n, b)
                assert nonzero_product(M, b) == nonzero_product(n, b)
                assert len(digits(M, b)) == len(digits(n, b))+s+j*t
                assert t <= m
                count += 1
    published = [11, 12, 1113, 104, 15, 132, 1071, 24, 11133, 110,
                 1001, 1020, 1131, 1022, 105, 32, 1071, 108, 133, 120,
                 100002, 1122, 161, 1008, 125, 1430, 702, 224, 3016,
                 11130, 10013, 160, 3003, 612, 315, 1332, 703, 342,
                 11193, 1040, 10004, 1008, 602, 1144, 225]
    for n, expected in enumerate(published, 1):
        actual, length, _ = minimum(n)
        assert actual == expected == brute(n, expected), (n, actual)
        assert length <= n*tau(nonzero_product(n))*(len(str(n))+2)
    for n in range(1, 301):
        a, length, _ = minimum(n)
        assert a % n == 0 and not is_shift(a, n)
        assert nonzero_product(a) == nonzero_product(n)
        assert length <= n*tau(nonzero_product(n))*(len(str(n))+2)
    for n in range(1, 101):
        assert minimum(10*n)[0] == 10*minimum(n)[0]
    print(f"PASS: {count} constructive witnesses in bases 2..16; "
          "45 published minima checked by direct enumeration; "
          "DFA minima n=1..300; 100 decimal-shift identities.")


if __name__ == '__main__':
    audit()
