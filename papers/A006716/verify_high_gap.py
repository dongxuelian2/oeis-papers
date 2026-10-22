#!/usr/bin/env python3
"""Auxiliary integer checks for the universal high-to-low root gap lemma.

The symbolic proof in GLOBAL_HIGH_GAP.md is independent of this finite test.
"""
from itertools import product

KNOWN = [
    1,2,3,7,12,21,38,107,212,31488,70107,387288,
    95610729,446653271,3148717107,21081079479,
    648070211589107021
]

def support(x):
    return [(i,int(c)) for i,c in enumerate(reversed(str(x))) if c!="0"]

def check_root(x):
    positions=support(x)
    desc=list(reversed(positions))
    for i in range(1,len(desc)-1):
        high, q, lower = desc[0][0], desc[i][0], desc[i+1][0]
        assert q-lower <= high-q+3, (x,high,q,lower)
        if desc[0][1] <= 3:
            assert q-lower <= high-q+2, (x,high,q,lower)

def check_contradiction():
    count=0
    for q in range(5,14):
        for e in range(q+1, q+4):
            for s in range(0,q):
                if s > q-(e-q+4):
                    continue
                for a,c,d in product((1,3,7,9),repeat=3):
                    H = a*10**e + c*10**q
                    L = d*10**s + (1 if s else 0)
                    digit=((H+L)**2 // 10**(2*q-1)) % 10
                    assert digit==0,(e,q,s,a,c,d,digit)
                    count+=1
    assert count>1000
    print(f"PASS: {count} forbidden-gap integer square identities")
    refined=0
    for q in range(4,14):
        for e in range(q+1,q+4):
            for s in range(q):
                if s > q-(e-q+3):
                    continue
                for a,c,d in product((1,2,3), (1,3,7,9),(1,3,7,9)):
                    H=a*10**e+c*10**q
                    L=d*10**s+(1 if s else 0)
                    assert ((H+L)**2//10**(2*q-1))%10==0
                    refined+=1
    assert refined>1000
    print(f"PASS: {refined} stronger low-leading-digit identities")

def main():
    for x in KNOWN:
        assert set(str(x*x)) <= set("149")
        check_root(x)
    print(f"PASS: all {len(KNOWN)} recorded roots satisfy both proven bounds")
    check_contradiction()

if __name__=="__main__":
    main()
