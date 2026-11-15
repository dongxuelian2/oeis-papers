#!/usr/bin/env python3
import math,json
from fractions import Fraction as F
from pathlib import Path

def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def factors(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out

def run():
    e,p,r=37,90947,1229
    assert prime(757) and pow(10,27,757)==1 and pow(10,9,757)!=1
    assert pow(10,27,243)==1 and pow(10,3,27)==1
    assert prime(37) and pow(10,3,37)==1 and pow(10,1,37)!=1
    assert prime(p) and pow(10,r,p)==1 and all(pow(10,r//ell,p)!=1 for ell in factors(r))
    assert math.gcd(r,6*757)==1 and p%3==2 and (p-1)%(e*r)==0
    assert pow(10,(p-1)//e,p)==1 and math.gcd(e,757*756)==1
    admissible_checks=0
    for q0 in range(7,2001):
        if not prime(q0):continue
        t=q0-1
        for f in factors(t):
            while t%f==0 and pow(10,t//f,q0)==1:t//=f
        if math.gcd(t,10)!=1:continue
        phi=9*t
        for f in factors(phi):phi=phi//f*(f-1)
        P=3*t*phi
        assert P%3==0 and P%t==0 and P%q0!=0 and pow(10,P,9*t)==1
        admissible_checks+=1
    valuation_checks=0
    for b in (37,74,1369):
        q=757**b;mod=757*q;residues=[]
        for v in range(1,757):
            for m in (q*v,q*v-1):
                t=m*(m+1)//2
                assert t%q==0 and (t//q)%757!=0
                residues.append(m%mod);valuation_checks+=1
        assert len(set(residues))==1512
    for m in range(1,30001,3):assert (m*(m+1)//2)%9==1
    tailchecks=0
    for a in list(range(38,301))+[1369,1370,50653,50654]:
        B=37
        while 37*B<=a-1:B*=37
        assert 37*B>=a
        # Beyond the small range, compare exponents exactly rather than
        # constructing a multi-million-digit denominator. Base 757 > 1.
        if a<=300:assert F(2,757**(37*B))<=F(2,757**a)
        assert B+1<=a
        assert 3*p*r*757**(B+1)<=3*p*r*757**a;tailchecks+=1
    recurrence_checks=0
    for d in (27,54,27*757,54*757):
        assert math.gcd(d,r)==1
        B=pow(10,d,p);alpha=pow(1-B,-1,p)
        for m,w in ((0,0),(17,123)):
            z=w
            for i in range(1,r+1):z=(B*z+m+i)%p
            assert z==(w+r*alpha)%p;recurrence_checks+=1
    data=dict(admissible_prime_checks=admissible_checks,valuation_sample_b=[37,74,1369],q=757,P=27,e=e,p=p,exact_order=r,valuation_class_checks=valuation_checks,q3_unit_checks=10000,tail_period_checks=tailchecks,scalar_order_step_checks=recurrence_checks)
    Path(__file__).with_name('general-valuation-transfer-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Exponent-37 witness and exact order: PASS')
    print('Admissible prime/P checks through 2000:',admissible_checks)
    print('Selected valuation-class checks:',valuation_checks)
    print('Q3 unit residues:',10000)
    print('Exact tail/period inequalities:',tailchecks)
    print('Scalar order-step identities:',recurrence_checks)
    print('PASS. No enormous-width prefixes or full blocks were enumerated.')
if __name__=='__main__':run()
