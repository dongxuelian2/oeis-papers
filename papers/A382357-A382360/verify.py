#!/usr/bin/env python3
"""Exact audits of greedy valuation permutations; Python standard library only."""
from collections import defaultdict
from pathlib import Path
import json


def valuation(n, b):
    k = 0
    while n % b == 0:
        n //= b
        k += 1
    return k


def core(t, b):
    """The t-th positive integer not divisible by b (1-based)."""
    return t+(t-1)//(b-1)


def queue_walk(b=2, jump=1, seed=(1,)):
    """Smallest unused label in each of the two eligible queues."""
    assert b >= 2 and jump >= 1 and len(set(seed)) == len(seed)
    assert all(n > 0 for n in seed)
    assert all(abs(valuation(x,b)-valuation(y,b)) == jump
               for x,y in zip(seed,seed[1:]))
    used = set(seed)
    pointers = defaultdict(lambda: 1)

    def candidate(k):
        scale = b**k
        t = pointers[k]
        while (value := scale*core(t,b)) in used:
            t += 1
        pointers[k] = t
        return value

    yield from seed
    k = valuation(seed[-1],b)
    while True:
        levels = (k+jump,) if k < jump else (k-jump,k+jump)
        value,k = min((candidate(j),j) for j in levels)
        used.add(value)
        pointers[k] += 1
        yield value


def direct_walk(b, jump, seed, count):
    """Independent scan of integer labels; no queue or core formula."""
    out = list(seed)
    used = set(seed)
    while len(out) < count:
        current = valuation(out[-1],b)
        n = 1
        while n in used or abs(valuation(n,b)-current) != jump:
            n += 1
        out.append(n)
        used.add(n)
    return out


def take(iterator, count):
    return [next(iterator) for _ in range(count)]


def audit_generators():
    comparisons = 0
    for b in range(2,9):
        for jump in (1,2):
            for r in range(jump):
                seeds = [(b**r,),
                         ((b+1)*b**r,(b+1)*b**(r+jump),b**(r+2*jump)),
                         ((2*b+1)*b**(r+3*jump),b**(r+2*jump),(b+1)*b**(r+jump))]
                for seed in seeds:
                    actual = take(queue_walk(b,jump,seed),160)
                    expected = direct_walk(b,jump,seed,160)
                    assert actual == expected, (b,jump,seed)
                    assert len(set(actual)) == len(actual)
                    assert all(valuation(n,b) % jump == r for n in actual)
                    assert all(abs(valuation(x,b)-valuation(y,b)) == jump
                               for x,y in zip(actual,actual[1:]))
                    comparisons += len(actual)
    return comparisons


def audit_contraction():
    comparisons = 0
    for b in range(2,31):
        # Independent enumeration of the core classes.
        expected = [n for n in range(1,1001) if n % b]
        assert [core(t,b) for t in range(1,len(expected)+1)] == expected
        for jump in range(1,5):
            scale = b**jump
            C = scale*scale-scale*scale//b-1
            for c in range(100):
                for u in range(1,100):
                    if scale*scale*core(u,b) < core(c+1,b):
                        assert scale*scale*u <= c+scale*scale-scale*scale//b
                    comparisons += 1
            for M in range(1,1001):
                assert (2*M+C)//(scale*scale) <= M-1
            # All possible next counts consistent with the recurrence contract
            # in pairs. Values 0 are retained as the contradiction boundary.
            for u in range(1,40):
                for v in range(1,40):
                    M = max(u,v)
                    w = (u+v+C)//(scale*scale)
                    z = (v+w+C)//(scale*scale)
                    assert max(w,z) <= M-1
    return comparisons


def audit_binary():
    published = json.loads(Path(__file__).with_name('published.json').read_text())
    length = 500000
    iterator = queue_walk()
    prefix = []
    positions = {}
    counts, ups, downs = defaultdict(int),defaultdict(int),defaultdict(int)
    coverage = bytearray(10001)
    current = None
    records = 0
    local_blocks = []
    pending = []
    for index in range(1,length+1):
        value = next(iterator)
        k = valuation(value,2)
        if current is not None:
            if k == current+1:
                ups[current] += 1
            else:
                assert k == current-1
                downs[k] += 1
        counts[k] += 1
        current = k
        if value <= 10000:
            coverage[value] = 1
        if index <= len(published['prefix']):
            prefix.append(value)

        for due,expected in list(pending):
            if due == index:
                assert value == expected, (index,value,expected)
                pending.remove((due,expected))
        if value == 2**k:
            assert k not in positions
            positions[k] = index
            # Last exits of a finite path ending at a newly reached level.
            for j in range(k):
                assert ups[j]-downs[j] == 1
            for j in range(1,k):
                assert counts[j] == ups[j-1]+ups[j]-1
            for j in range(2,k):
                assert 4*ups[j] <= ups[j-2]+ups[j-1]+1
            records += 1
            if k % 2 == 0:
                pending.extend([(index+1,2*value),(index+2,3*value)])
                if k:
                    assert previous == 3*value//2
                    pending.append((index+3,5*value//2))
                    local_blocks.append(index)
        previous = value

    assert prefix == published['prefix']
    assert [positions[k] for k in range(len(published['positions']))] == published['positions']
    for k in range(0,max(positions),2):
        if k+1 in positions:
            assert positions[k+1] == positions[k]+1
    assert all(coverage[1:])
    return len(prefix),len(published['positions']),records,len(local_blocks)


def main():
    comparisons = audit_generators()
    contraction = audit_contraction()
    prefix,positions,records,blocks = audit_binary()
    print(f"PASS: {comparisons} terms matched independent integer scans across "
          "63 base/jump/seed cases; "
          f"{contraction} exact rounding controls and 116000 contraction bounds; "
          f"500000 binary terms, {prefix} published terms, {positions} published inverse positions; "
          f"{records} finite last-exit audits and {blocks} five-term blocks; "
          "all labels 1..10000 occur in the checked prefix.")


if __name__ == '__main__':
    main()
