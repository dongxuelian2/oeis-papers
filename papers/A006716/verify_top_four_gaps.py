#!/usr/bin/env python3
"""Independent exact-rational audit of highest FOUR nonzero root positions.

For an A006716 root with >=6 nonzero digits, the square has >=11 decimal
digits, so its first ten decimal digits must be in {1,4,9}^10.

The top-four gap data and mask counts are derived by intersecting exact
integer-scaled square intervals with the 3^10 admissible prefix intervals.
No floating point. A separate finite sweep deals with shorter squares.
"""
from bisect import bisect_left
from itertools import product

PREFIX10=sorted(int("".join(d)) for d in product("149",repeat=10))
PAIRS=((1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1))
EXPECTED={
 (1,1):(129,32,6,4,0),
 (1,2):(65,20,0,0,0,0),
 (1,3):(34,5,3,0,0,0,0),
 (2,1):(119,48,18,0,0,0),
 (2,2):(22,13,4,5,0,7,9),
 (2,3):(17,3,0,0,0,0,0,0),
 (2,4):(12,2,4,0,0,0,0,0,0),
 (3,1):(12,10,0,0,0,0,0)
}

def intersects(prefixes,K,D,z):
    """Does [(z/D)^2,((z+1)/D)^2) meet any admissible K-digit prefix?"""
    lower=z*z*10**K
    upper=(z+1)*(z+1)*10**K
    den=D*D
    for j in (1,2):
        scale=den*10**j
        pos=bisect_left(prefixes, lower//scale)
        for i in (pos-1,pos):
            if 0<=i<len(prefixes):
                p=prefixes[i]
                if lower<(p+1)*scale and upper>p*scale:
                    return True
    return False

def possible(g,h,t,a,b,c,d):
    D=10**(g+h+t)
    z=a*D+b*10**(h+t)+c*10**t+d
    return intersects(PREFIX10,10,D,z)

def check_masks():
    checked=0
    for g,h in PAIRS:
        counts=[]
        for t in range(1,g+h+4):
            count=sum(possible(g,h,t,a,b,c,d)
                for a,b,c,d in product(range(1,10),repeat=4))
            counts.append(count)
            checked+=9**4
        assert tuple(counts)==EXPECTED[g,h], (g,h,counts)
        print(f"PASS gaps ({g},{h}): {counts}")
    assert all(ct==0 for (g,h),row in EXPECTED.items()
                         for i,ct in enumerate(row,1) if i>=8)
    print(f"PASS {checked} exact top-four interval tests: fourth gap <= 7")

def check_short():
    # If x*x has fewer than ten digits then x<=31622. Exhaust that
    # entire finite exceptional range, independently of any OEIS list.
    short=[]
    for x in range(1,31623):
        if sum(ch!='0' for ch in str(x))<4:
            continue
        if not set(str(x*x))<=set("149"):
            continue
        short.append(x)
        exps=[i for i,ch in enumerate(reversed(str(x))) if ch!='0']
        e,p,q,s=exps[-1],exps[-2],exps[-3],exps[-4]
        assert q-s<=7
    assert short==[31488],short
    print("PASS all 31,622 short-square roots; sole qualifying support>=4 is 31488")


if __name__=="__main__":
    check_masks()
    check_short()
