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


def classify_sixth():
    top4=[]
    for g,h in PAIRS:
        for t in range(1,min(7,g+h+3)+1):
            D=10**(g+h+t)
            for a,b,c,d in product(range(1,10),repeat=4):
                z=a*D+b*10**(h+t)+c*10**t+d
                if prefix_intersects(z,D,10):
                    top4.append((g,h,t,a,b,c,d,z,D))
    assert len(top4)==603
    top5=[]
    for g,h,t,a,b,c,d,z,D in top4:
        for u in range(1,min(5,g+h+t+3)+1):
            D5=D*10**u
            for f in range(1,10):
                z5=z*10**u+f
                if prefix_intersects(z5,D5,14):
                    top5.append((g,h,t,u,a,b,c,d,f,z5,D5))
    assert len(top5)==2322,len(top5)
    print("PASS: exactly 2322 five-highest-digit configurations")

    counts={}
    survivors=[]
    for g,h,t,u,a,b,c,d,f,z,D in top5:
        for v in range(1,min(21,g+h+t+u+3)+1):
            scale=10**(v-1)
            if prefix_intersects(z*scale,D*scale,16):
                counts[v]=counts.get(v,0)+1
                if v==6:
                    survivors.append((g,h,t,u,a,b,c,d,f))
    assert counts=={1:2322,2:702,3:200,4:56,5:19,6:3},counts
    assert survivors==[
        (1,1,1,1,3,1,4,8,8),
        (1,1,3,2,2,1,2,1,6),
        (2,3,1,1,7,1,9,9,5)
    ],survivors
    print("PASS: sixth-highest gap counts",counts)
    print("CERTIFIED: no 16-digit-prefix-compatible gap >=7")

def short_exception_sixth():
    # Covers all integer squares with at most 15 decimal digits.
    upper=isqrt(10**15-1)
    matches=[]
    for x in range(1,upper+1):
        y=x*x
        while y and y%10 in (1,4,9):
            y//=10
        if y:
            continue
        positions=[i for i,c in enumerate(str(x)[::-1]) if c!="0"]
        if len(positions)<6:
            continue
        exps=positions[::-1]
        assert exps[4]-exps[5]<=6,(x,exps)
        matches.append(x)
    assert matches==[387288],matches
    print(f"PASS: all {upper:,} possible short-square roots; support>=6: {matches}")

if __name__=="__main__":
    classify_sixth()
    short_exception_sixth()
    print("CERTIFIED: sixth-highest root gap <=6 for all A006716 squares.")
