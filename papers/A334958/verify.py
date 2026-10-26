#!/usr/bin/env python3
"""Independent Fraction summation, integer recurrence, and valuation product."""
from fractions import Fraction as Q
from math import gcd, factorial, lcm

def factor(n):
    result={};p=2
    while p*p<=n:
        while n%p==0: result[p]=result.get(p,0)+1;n//=p
        p+=1
    if n>1:result[n]=result.get(n,0)+1
    return result

def valuation(n,p):
    v=0
    while n%p==0:n//=p;v+=1
    return v

def terms(bound):
    a=0
    for n in range(1,bound+1):
        a=n*a+(-1)**(n+1)*factorial(n-1)
        following=(n+1)*a+(-1)**(n+2)*factorial(n)
        yield gcd(a,following)

def audit():
    published=[1,1,1,2,2,12,12,48,144,1440,1440,17280,17280,241920,18144000,145152000,145152000,2612736000,2612736000,10450944000,219469824000,4828336128000,4828336128000,115880067072000,579400335360000,15064408719360000,135579678474240000,26573616980951040000,26573616980951040000]
    assert list(terms(29))==published
    h=Q(0);common=1
    for n,expected in enumerate(terms(500),1):
        h+=Q((-1)**(n+1),n)
        f=factorial(n)
        assert expected==f//h.denominator
        value=Q(f)
        for p in factor(f):
            value*=Q(p)**min(0,valuation(h.numerator,p)-valuation(h.denominator,p))
        assert value==expected
        common=lcm(common,n)
        assert expected%(f//common)==0
        b=f-int(f*h);bnext=factorial(n+1)-int(factorial(n+1)*(h+Q((-1)**(n+2),n+1)))
        assert gcd(b,bnext)==gcd(b,f)==gcd(int(f*h),b)==expected
    from pathlib import Path
    for line,k in zip((x for x in Path(__file__).with_name('b334958.txt').read_text().splitlines() if not x.startswith('#')),terms(100)):
        n,expected=map(int,line.split());assert k==expected
    print('PASS 29 official terms; 500 independent exact rational/valuation/divisibility controls; 100-row table')

if __name__=='__main__': audit()
