#!/usr/bin/env python3
"""Shortest accepted palindrome in a finite automaton, exact integer arithmetic."""
from functools import lru_cache
from heapq import heappush, heappop

def automaton(n):
    pattern = str(n)
    d = len(pattern)
    count = n*(d+2)
    start, dead = count, count+1
    transitions = []
    for r in range(n):
        for k in range(d+2):
            row = []
            for x in range(10):
                if k >= d:
                    j = d+1
                else:
                    text = pattern[:k]+str(x)
                    j = max(j for j in range(d+1) if text.endswith(pattern[:j]))
                row.append(((10*r+x)%n)*(d+2)+j)
            transitions.append(row)
    transitions += [[dead]+[(x%n)*(d+2) for x in range(1,10)], [dead]*10]
    return transitions, start, d+1

def least(n):
    if n < 1:
        raise ValueError('positive index required')
    if n % 10 == 0:
        return 0
    delta, start, accept = automaton(n)
    size = len(delta)
    pre = [[[] for _ in range(size)] for _ in range(10)]
    for p,row in enumerate(delta):
        for x,q in enumerate(row):
            pre[x][q].append(p)
    infinity = 2*size*size+1
    distance = [infinity]*(size*size)
    heap = []
    def offer(p,q,d):
        i = p*size+q
        if d < distance[i]:
            distance[i] = d
            heappush(heap,(d,p,q))
    for p,row in enumerate(delta):
        offer(p,p,0)
        for q in row:
            offer(p,q,1)
    while heap:
        d,u,v = heappop(heap)
        if d != distance[u*size+v]:
            continue
        for x in range(10):
            q = delta[v][x]
            for p in pre[x][u]:
                offer(p,q,d+2)
    @lru_cache(None)
    def word(p,q):
        d = distance[p*size+q]
        if d == 0:
            return ''
        if d == 1:
            return str(next(x for x in range(10) if delta[p][x] == q))
        for x in range(10):
            u = delta[p][x]
            choices = [word(u,v) for v in pre[x][q] if distance[u*size+v] == d-2]
            if choices:
                return str(x)+min(choices)+str(x)
        raise AssertionError('unreachable accepting palindrome')
    assert distance[start*size+accept] < infinity
    return int(word(start,accept))

def witness(n):
    if n % 10 == 0:
        return None
    core, a = 1, 0
    for p in (2,5):
        while n % (core*p) == 0:
            core *= p
            a += 1
    # n has at most one of 2,5; a decimal suffix of a digits fixes divisibility by core.
    suffix = str(core).zfill(max(a,1))
    block = suffix[::-1]+str(n)+str(n)[::-1]+suffix
    m = n//core
    b = pow(10,len(block),m) if m != 1 else 0
    h,r = 1,b
    while m != 1 and r != 1:
        h += 1
        r = r*b % m
    return block,m*h

def audit():
    published = [111,222,333,444,555,666,777,888,999,0,1111,82128,41314,414414,55155,61616,317713,41814,41914,0,912219,2222,52325,2324232,52525,82628,82728,828828,52925,0,2131312,23232,3333,2243422,535535,2136312,43734,88388]
    assert [least(n) for n in range(1,39)] == published
    # Enumerate ordinary palindrome halves directly, independently of the DFA.
    found = {}
    for length in range(3,8):
        half = (length+1)//2
        for h in range(10**(half-1),10**half):
            t = str(h)
            s = t+(t[:-1] if length%2 else t)[::-1]
            k = int(s)
            for n in range(1,101):
                if n not in found and k%n == 0 and str(n) in s[1:-1]:
                    found[n] = k
    for n,k in found.items():
        assert least(n) == k,(n,k,least(n))
    for n in range(1,501):
        w = witness(n)
        if w is None:
            assert n%10 == 0
            continue
        block,copies = w
        assert block == block[::-1] and block[0] != '0' and str(n) in block[1:-1]
        r = 0
        for _ in range(copies):
            for x in block:
                r = (10*r+int(x)) % n
        assert r == 0,n
    from pathlib import Path
    table = Path(__file__).with_name('b084043.txt')
    for line in table.read_text().splitlines():
        if line and not line.startswith('#'):
            n, k = map(int, line.split())
            assert least(n) == k, (n, k)
    print(f'PASS 38 official terms; {len(found)} independent palindrome minima through 7 digits; 450 witnesses through n=500')

if __name__ == '__main__':
    import sys
    if len(sys.argv)==1:
        audit()
    else:
        for n in map(int,sys.argv[1:]):
            print(n,least(n))
