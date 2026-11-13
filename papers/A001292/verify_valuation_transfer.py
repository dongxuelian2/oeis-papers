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
    e,p,r=5,412031,41203
    assert prime(p) and pow(10,r,p)==1 and all(pow(10,r//ell,p)!=1 for ell in factors(r))
    assert math.gcd(r,222)==1 and p%37==36 and p%3==2 and (p-1)%(e*r)==0
    assert pow(10,(p-1)//e,p)==1 and math.gcd(e,37*36)==1
    valuation_checks=0
    for b in (5,25,125):
        q=37**b;mod=37*q;residues=[]
        for v in range(1,37):
            for m in (q*v,q*v-1):
                t=m*(m+1)//2
                assert t%q==0 and (t//q)%37!=0
                residues.append(m%mod);valuation_checks+=1
        assert len(set(residues))==72
    for m in range(1,30001,3):assert (m*(m+1)//2)%9==1
    tailchecks=0
    for a in range(6,301):
        B=5
        while 5*B<=a-1:B*=5
        assert 5*B>=a
        assert F(2,37**(5*B))<=F(2,37**a)
        assert 3*p*r*37**(B+1)<=3*p*r*37**a;tailchecks+=1
    recurrence_checks=0
    for d in (3,6,111,222):
        assert math.gcd(d,r)==1
        B=pow(10,d,p);alpha=pow(1-B,-1,p)
        for m,w in ((0,0),(17,123)):
            z=w
            for i in range(1,r+1):z=(B*z+m+i)%p
            assert z==(w+r*alpha)%p;recurrence_checks+=1
    data=dict(e=e,p=p,exact_order=r,valuation_class_checks=valuation_checks,q3_unit_checks=10000,tail_period_checks=tailchecks,scalar_order_step_checks=recurrence_checks)
    Path(__file__).with_name('valuation-transfer-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Fifth-power witness and exact order: PASS')
    print('Selected valuation-class checks:',valuation_checks)
    print('Q3 unit residues:',10000)
    print('Exact tail/period inequalities:',tailchecks)
    print('Scalar order-step identities:',recurrence_checks)
    print('PASS. No enormous-width prefixes or full blocks were enumerated.')
if __name__=='__main__':run()
