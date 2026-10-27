#!/usr/bin/env python3
"""Exact recurrence, crossing-count formula, and independent Hamilton-path DP."""
from functools import lru_cache
from math import comb, factorial
from pathlib import Path


def sequences(bound):
    opposite, same = [0,1], [1,0]
    for n in range(2,bound+1):
        opposite.append((n-1)*opposite[-1]+opposite[-2])
        same.append((n-1)*same[-1]+same[-2])
    return opposite[:bound+1],same[:bound+1]


def crossing_counts(n):
    """Directed tours with exactly r horizontal (between-column) moves."""
    result={}
    for r in range(1,n+1):
        if r%2:
            k=(r-1)//2
            normalized=factorial(n-r)*comb(n-k-1,k)**2
        else:
            j=r//2
            normalized=factorial(n-r)*comb(n-j,j)*comb(n-j-1,j-1)
        result[r]=2*factorial(n)*normalized
    return result


def direct_paths(n):
    """Literal rook graph, fixed start, subset DP; no crossing formulas."""
    size=2*n
    full=(1<<size)-1
    neighbors=[]
    for v in range(size):
        row,col=v%n,v//n
        neighbors.append([u for u in range(size) if u!=v and (u%n==row or u//n==col)])
    @lru_cache(None)
    def visit(mask,last):
        if mask==full:
            return (1,0) if last//n==0 else (0,1)
        same=opposite=0
        for nxt in neighbors[last]:
            if not mask>>nxt&1:
                a,b=visit(mask|1<<nxt,nxt)
                same+=a;opposite+=b
        return same,opposite
    same,opposite=visit(1,0)
    return 2*n*same,2*n*opposite


def write_tables():
    opposite,same=sequences(100)
    for ident,values in [('A001040',opposite),('A001053',same)]:
        path=Path(__file__).with_name('b'+ident[1:]+'.txt')
        path.write_text('# Exact recurrence values, n=0..100.\n'+''.join(f'{n} {v}\n' for n,v in enumerate(values)))


def audit():
    opposite,same=sequences(200)
    published_opposite=[0,1,1,3,10,43,225,1393,9976,81201,740785,7489051,83120346,1004933203,13147251985,185066460993,2789144166880,44811373131073,764582487395121,13807296146243251,263103209266016890,5275871481466581051,111056404320064218961,2448516766522879398193]
    published_same=[1,0,1,2,7,30,157,972,6961,56660,516901,5225670,57999271,701216922,9173819257,129134686520,1946194117057,31268240559432,533506283627401,9634381345852650,183586751854827751,3681369418442407670,77492344539145388821,1708512949279640961732]
    assert opposite[:24]==published_opposite and same[:24]==published_same
    print('PASS all 24 displayed official values for each sequence',flush=True)
    for n in range(1,201):
        counts=crossing_counts(n)
        assert sum(v for r,v in counts.items() if r%2)==2*factorial(n)*opposite[n]
        assert sum(v for r,v in counts.items() if not r%2)==2*factorial(n)*same[n]
    print('PASS exact crossing sums versus defining recurrences for n=1..200',flush=True)
    for n in range(1,9):
        actual_same,actual_opposite=direct_paths(n)
        assert actual_same==2*factorial(n)*same[n],(n,actual_same)
        assert actual_opposite==2*factorial(n)*opposite[n],(n,actual_opposite)
    print('PASS independent literal Hamilton-path subset DP for every board n=1..8',flush=True)
    for ident,values in [('A001040',opposite),('A001053',same)]:
        rows=[tuple(map(int,line.split())) for line in Path(__file__).with_name('b'+ident[1:]+'.txt').read_text().splitlines() if line and not line.startswith('#')]
        assert rows==list(enumerate(values[:101]))
    print('PASS both 101-row tables, including correct n=0 recurrence offsets',flush=True)

if __name__=='__main__':
    import sys
    if sys.argv[1:]==['--write-tables']:write_tables()
    elif not sys.argv[1:]:audit()
    else:raise SystemExit('usage: verify.py [--write-tables]')
