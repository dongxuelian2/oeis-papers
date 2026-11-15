#!/usr/bin/env python3
"""Finite structural audit. No numerical Linnik exponent/constant is asserted."""
import json, math
from fractions import Fraction
from pathlib import Path
from verify_growing_prime_sieve import primes

def prime(n):
    return n>=2 and all(n%p for p in range(2,math.isqrt(n)+1))

def least_in_class(a,q):
    n=a
    while not prime(n):n+=q
    return n

def run():
    records=[]
    for g in (2,10):
        for d in (6,12,24):
            for ell in (2,3,7,23,101):
                candidates=[p for p in primes(8*d) if 2*d<p<8*d and p!=ell]
                r=candidates[0];ps=[]
                for b in range((r+1)//2,r):
                    a=(1+ell*((b-1)*pow(ell,-1,r)%r))%(ell*r)
                    assert a%ell==1 and a%r==b and math.gcd(a,ell*r)==1
                    p=least_in_class(a,ell*r)
                    assert p>=b>d and p%ell==1 and p%r==b
                    ps.append(p)
                assert len(ps)==len(set(ps)) and len(ps)>=d
                bad=[p for p in ps if pow(g,d,p)==1]
                assert math.prod(bad)<=g**d-1
                good=[p for p in ps if g%p and pow(g,d,p)!=1]
                assert good
                selected=good[:min(3,len(good))]
                density=math.prod(Fraction(p+ell-1,ell*p) for p in selected)
                assert density < Fraction(2,ell)**len(selected)
                T=math.lcm(*(p*(p-1) for p in selected))
                assert T <= max(selected)**(2*len(selected))
                records.append(dict(base=g,width=d,exponent=ell,auxiliary_prime=r,constructed=len(ps),ineligible=len(ps)-len(good),largest_prime=max(ps),selected=selected,density=str(density),period=T))
    tails=[]
    for Q in (3,10,50):
        for s in (2,3,8):
            partial=sum((Fraction(2,n)**s for n in range(Q+1,Q+501)),Fraction(0))
            bound=Fraction(2,Q)**s*(1+Fraction(Q,s-1))
            assert partial<=bound
            tails.append(dict(cutoff=Q,power=s,terms=500,bound=str(bound)))
    data=dict(crt_constructions=records,tail_checks=tails)
    Path(__file__).with_name('linnik-exponent-window-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('CRT prime constructions checked:',len(records))
    print('Exact finite density-tail checks:',len(tails))
    print('PASS. No numerical admissible Linnik constants or resolution of the integer conjecture is claimed.')

if __name__=='__main__':run()
