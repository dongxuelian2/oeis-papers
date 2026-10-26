#!/usr/bin/env python3
"""Exact all-index evaluator; no third-party dependencies."""
from collections import deque
from math import prod

PRIMES = (2, 3, 5, 7)

def exponents(n):
    if n < 1:
        raise ValueError('positive index required')
    rest, e = n, []
    for p in PRIMES:
        a = 0
        while rest % p == 0:
            rest //= p
            a += 1
        e.append(a)
    return tuple(e) if rest == 1 and n % 10 else None

DIGITS = {d: tuple(next(a for a in range(4) if d % (p ** (a + 1))) for p in PRIMES) for d in range(1, 10)}

def least(n):
    target = exponents(n)
    if target is None:
        return 0
    # The extra start vertex is necessary for n=1: the empty word is invalid.
    parent = {}
    queue = deque()
    def add(state, previous, digit):
        if state not in parent:
            parent[state] = previous, digit
            queue.append(state)
    for d in range(1, 10):
        add((d % n, tuple(min(a, b) for a, b in zip(target, DIGITS[d]))), None, d)
    while queue:
        state = queue.popleft()
        r, e = state
        if r == 0 and e == target:
            digits = []
            while state is not None:
                state, d = parent[state]
                digits.append(str(d))
            return int(''.join(reversed(digits)))
        for d in range(1, 10):
            add(((10*r+d) % n, tuple(min(a, b+c) for a,b,c in zip(target,e,DIGITS[d]))), state, d)
    raise AssertionError('existence theorem violated')

def suffix(p, a):
    s = 0
    for j in range(1, a+1):
        s = next(s+d*10**(j-1) for d in range(1,p+1) if (s+d*10**(j-1)) % p**j == 0)
    return str(s).zfill(a)

def witness(n):
    e = exponents(n)
    if e is None:
        return None
    a,b,c,d = e
    tail = suffix(2,a) if a else suffix(5,c) if c else '1'
    block = '2'*a + '3'*b + '5'*c + '7'*d + tail
    core = 2**a * 5**c
    m = n // core
    h, r = 1, 10**len(block) % m if m != 1 else 0
    while m != 1 and r != 1:
        h += 1
        r = r * pow(10,len(block),m) % m
    return block, m*h

def word_mod(word, n):
    r = 0
    for c in word:
        r = (10*r + int(c)) % n
    return r

def audit():
    published = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 168, 0, 378, 135, 48, 0, 36, 0, 0, 273, 0, 0, 168, 525, 0, 999, 476, 0, 0, 0, 288, 0, 0, 175, 1296, 0, 0, 0, 0, 0, 378, 0, 0, 495, 0, 0, 384, 3577, 0]
    assert [least(n) for n in range(1,len(published)+1)] == published
    # Independent direct integer scan: capture every n<=200 whose minimum is <=200000.
    found = {}
    for k in range(1,200001):
        p = prod(map(int,str(k)))
        if not p:
            continue
        for n in range(1,201):
            if n not in found and k % n == 0 and p % n == 0:
                found[n] = k
    for n,k in found.items():
        assert least(n) == k, (n,k,least(n))
    count = 0
    for n in range(1,501):
        w = witness(n)
        if w is None:
            assert least(n) == 0
            continue
        block, copies = w
        # Check repeated construction without materializing giant integers.
        r = 0
        for _ in range(copies):
            for c in block:
                r = (10*r+int(c)) % n
        assert r == 0 and '0' not in block
        assert pow(prod(map(int,block)),copies,n) == 0
        count += 1
    from pathlib import Path
    table = Path(__file__).with_name('b085124.txt')
    for line in table.read_text().splitlines():
        if line and not line.startswith('#'):
            n, k = map(int, line.split())
            assert least(n) == k, (n, k)
    print(f'PASS {len(published)} official terms; {len(found)} independent minima; {count} constructive witnesses through n=500')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        audit()
    else:
        for n in map(int,sys.argv[1:]):
            print(n,least(n))
