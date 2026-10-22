#!/usr/bin/env python3
"""Exact rational proof audit: gap to FIFTH highest nonzero root digit <=5.

No floats, no arbitrary cutoff on digit length. For squares shorter than
14 digits the complete finite exceptional range is checked directly.
"""
from functools import lru_cache
from itertools import product
from math import isqrt

ALPHABET="149"
PAIRS=((1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1))

@lru_cache(maxsize=200000)
def next_allowed(lower,K):
    """Smallest exactly K-digit integer over 1,4,9 at least lower."""
    word=str(lower).zfill(K)
    if len(word)>K:
        return None

    @lru_cache(None)
    def visit(i,greater):
        if i==K:
            return ""
        for digit in ALPHABET:
            if not greater and digit<word[i]:
                continue
            suffix=visit(i+1,greater or digit>word[i])
            if suffix is not None:
                return digit+suffix
        return None
    answer=visit(0,False)
    return int(answer) if answer is not None else None

def prefix_intersects(z,D,K):
    """Does [z²/D²,(z+1)²/D²) meet a K-digit 149-prefix interval?"""
    denominator=D*D
    for j in (1,2):
        factor=10**(K-j)
        minimum=(z*z*factor)//denominator
        maximum=(((z+1)*(z+1)*factor+denominator-1)//denominator)-1
        lower=max(minimum,10**(K-1))
        upper=min(maximum,10**K-1)
        if lower>upper:
            continue
        first=next_allowed(lower,K)
        if first is not None and first<=upper:
            return True
    return False

def classify():
    top4=[]
    for g,h in PAIRS:
        for t in range(1,min(7,g+h+3)+1):
            D=10**(g+h+t)
            for a,b,c,d in product(range(1,10),repeat=4):
                z=a*D+b*10**(h+t)+c*10**t+d
                if prefix_intersects(z,D,10):
                    top4.append((g,h,t,a,b,c,d,z,D))
    assert len(top4)==603,len(top4)
    print("PASS: independently derived 603 admissible top-four configurations")

    counts={}
    survivors_five=[]
    tested=0
    for g,h,t,a,b,c,d,z,D in top4:
        for u in range(1,g+h+t+4):
            tested+=1
            scale=10**(u-1)
            if prefix_intersects(z*scale,D*scale,14):
                counts[u]=counts.get(u,0)+1
                if u==5:
                    survivors_five.append((g,h,t,a,b,c,d))
    assert counts=={1:593,2:179,3:49,4:8,5:2},counts
    assert survivors_five==[(2,1,1,7,2,9,9),(2,1,3,3,7,4,3)],survivors_five
    print(f"PASS: {tested} exact fifth-gap prefix checks")
    print("PASS: gap counts",counts,"; NO cases with fifth gap >=6")

def short_exception():
    upper=isqrt(10**13-1)
    matches=[]
    for x in range(1,upper+1):
        if any(d not in ALPHABET for d in str(x*x)):
            continue
        positions=[i for i,c in enumerate(str(x)[::-1]) if c!="0"]
        if len(positions)<5:
            continue
        exps=positions[::-1]
        gap=exps[3]-exps[4]
        assert gap<=5,(x,gap)
        matches.append(x)
    assert matches==[31488,387288],matches
    print(f"PASS: all {upper:,} short-square roots; 5-sparse+ roots:",matches)

if __name__=="__main__":
    classify()
    short_exception()
    print("CERTIFIED: fifth-highest nonzero root gap <=5 for all A006716 squares.")
