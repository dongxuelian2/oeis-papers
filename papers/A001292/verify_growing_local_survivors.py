#!/usr/bin/env python3
"""Exact finite checks; local squares are not asserted to be integer squares."""
import math,json
from fractions import Fraction as F
from pathlib import Path
from verify_a001292 import append_block

def primes(n):return [p for p in range(2,n+1) if all(p%q for q in range(2,math.isqrt(p)+1))]
def prefix(m,mod):
    z=0;lo=1;d=1
    while lo<=m:
        count=min(m,10*lo-1)-lo+1
        z=append_block(z,lo,count,d,mod);lo*=10;d+=1
    return z

def coefficients(d,p):
    B=pow(10,d,p);lo=10**(d-1);C=(B-1)%p;inv=pow(C,-1,p)
    A=(C*C*prefix(lo-1,p)+lo*C+1)%p
    return A*pow(B,1-lo,p)*inv*inv%p,-inv%p,-B*inv*inv%p

def count_class(a,T,lo,hi):return (hi-a)//T-(lo-1-a)//T

def run():
    records=[];checks=0
    for d in (5,7,11):
        ps=[p for p in primes(2*d) if p>5];T=120;classes=[1];density=F(1,120)
        for p in ps:
            assert pow(10,d,p)!=1
            alpha,beta,gamma=coefficients(d,p);B=pow(10,d,p)
            H=math.lcm(T,p-1);newT=H*p;roots={x*x%p for x in range(1,p)};out=[]
            for a in classes:
                for j in range(H//T):
                    b=a+j*T;exp=pow(B,b,p)
                    for t in range(p):
                        n=b+t*H
                        if (alpha*exp+beta*n+gamma)%p in roots:out.append(n)
            density*=F(p-1,2*p);T=newT;classes=out
            assert len(classes)==len(set(classes)) and F(len(classes),T)==density
        assert math.lcm(*range(1,2*d+1))%T==0
        lo,hi=10**(d-1),10**d-1
        count=sum(count_class(a,T,lo,hi) for a in classes)
        assert abs(F(count)-F(hi-lo+1)*density)<=T
        for a in classes[:100]:
            m=a+max(0,(lo-a+T-1)//T)*T
            if m>hi:continue
            assert m%120==1
            assert prefix(m,8)==1 and prefix(m,3)==1 and prefix(m,5)==1
            for p in ps:
                v=prefix(m,p)
                assert v and pow(v,(p-1)//2,p)==1
                checks+=1
        records.append(dict(width=d,prime_cutoff=2*d,period=T,allowed_classes=len(classes),density=str(density),actual_endpoints=count))
    Path(__file__).with_name('growing-local-survivors-certificate.json').write_text(json.dumps(dict(cases=records,independent_prefix_checks=checks),indent=2)+'\n')
    for r in records:print(r)
    print('Independent candidate prefix checks:',checks)
    print('PASS. All candidates are local squares; no integer-square assertion is made.')

if __name__=='__main__':run()
