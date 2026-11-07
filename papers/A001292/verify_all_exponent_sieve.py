#!/usr/bin/env python3
"""Exact finite audits of the all-exponent quadratic sieve."""
import math,json
from fractions import Fraction as F
from pathlib import Path

def primes(n):
    return [p for p in range(2,n+1) if all(p%q for q in range(2,math.isqrt(p)+1))]

def support(ps,z):
    a={1:()}
    for p in ps:
        a.update({q*p:fs+(p,) for q,fs in list(a.items()) if q*p<=z})
    return dict(sorted(a.items()))

def rho(fs):return math.prod(F(p-1,p*p) for p in fs)
def w(fs):return math.prod(F(p-1,p*p-p+1) for p in fs)

def run():
    records=[]
    for N in (6,30,210,9990):
        for z in (8,20,40):
            qs=support([p for p in primes(z) if N%p],z)
            G=sum((w(fs) for fs in qs.values()),F(0));lam={}
            for q,fs in qs.items():
                Gq=sum((w(rs) for r,rs in qs.items() if q*r<=z and math.gcd(q,r)==1),F(0))
                lam[q]=(-1)**len(fs)*math.prod(1/(1-F(p-1,p*p)) for p in fs)*Gq/G
                assert abs(lam[q])<=q
            assert lam[1]==1
            form=sum((lam[q]*lam[r]*rho(set(qs[q])|set(qs[r])) for q in qs for r in qs),F(0))
            assert form==1/G
            for s,fs in qs.items():
                Y=sum((lam[q]*rho(rs) for q,rs in qs.items() if q%s==0),F(0))
                assert Y==(-1)**len(fs)*w(fs)/G
            records.append(dict(N=N,z=z,support=len(qs),G=str(G),quadratic_form=str(form)))
    local=[]
    for ps in ((3,7),(3,5,7),(5,11)):
        T=math.lcm(*(p*p*(p-1) for p in ps))
        masks=[]
        for p in ps:
            M=p*p
            masks.append([((pow(2,n,M)+n+3)%M)%p==0 and (pow(2,n,M)+n+3)%M!=0 for n in range(M*(p-1))])
        count=sum(all(a[n%len(a)] for a in masks) for n in range(T))
        assert F(count,T)==rho(ps)
        local.append(dict(primes=ps,period=T,intersection=count,density=str(rho(ps))))
    # Exact finite Euler-distribution normalization and weighted first moment.
    euler=[]
    for ps in ((2,3,5),(3,7,11),(5,11,13)):
        a=support(ps,math.prod(ps));P=sum((w(fs) for fs in a.values()),F(0))
        assert P==math.prod(1/(1-F(p-1,p*p)) for p in ps)
        for p in ps:
            mass=sum((w(fs) for q,fs in a.items() if q%p==0),F(0))/P
            assert mass==F(p-1,p*p)
        euler.append(dict(primes=ps,products=len(a),total_mass=str(P)))
    out=dict(weight_identity_checks=records,local_intersections=local,euler_distribution_checks=euler)
    Path(__file__).with_name('all-exponent-sieve-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Exact quadratic-weight cases:',len(records))
    print('Exact local-intersection periods:',len(local))
    print('Exact Euler distributions:',len(euler))
    print('PASS. This audits identities, not the absence of individual perfect powers.')

if __name__=='__main__':run()
