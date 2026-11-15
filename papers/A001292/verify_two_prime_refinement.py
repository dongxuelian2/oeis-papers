#!/usr/bin/env python3
"""Exact finite audits of the two-prime periodic bound."""
import json,math,random
from fractions import Fraction
from pathlib import Path

def run():
    rng=random.Random(1292);records=[];intervals=0
    for ell,p,q in ((2,3,7),(2,11,23),(3,7,13),(3,13,19),(5,11,31),(7,29,43)):
        assert (p-1)%ell==(q-1)%ell==0
        T=math.lcm(p*(p-1),q*(q-1))
        assert T*ell<=p*(p-1)*q*(q-1)
        rho=Fraction(p+ell-1,ell*p)*Fraction(q+ell-1,ell*q)
        assert rho<Fraction(4,ell*ell)
        for trial in range(2):
            masks=[]
            for z in (p,q):
                roots={pow(x,ell,z) for x in range(z)}
                alpha=3 if not trial else 0;beta=2;gamma=z//2+trial
                masks.append([((alpha*pow(2,n,z)+beta*n+gamma)%z) in roots for n in range(z*(z-1))])
            allowed=[all(mask[n%len(mask)] for mask in masks) for n in range(T)]
            prefix=[0]
            for v in allowed:prefix.append(prefix[-1]+v)
            A=prefix[-1];assert Fraction(A,T)==rho
            assert A<=Fraction(4*max(p,q)**4,ell**3)
            def upto(n):
                z,r=divmod(n,T);return z*A+prefix[r]
            for _ in range(300):
                start=rng.randrange(5*T);H=rng.randrange(4*T)
                count=upto(start+H)-upto(start)
                assert count<=H*rho+A
                intervals+=1
            records.append(dict(exponent=ell,primes=[p,q],trial=trial,period=T,allowed=A,density=str(rho)))
    Path(__file__).with_name('two-prime-refinement-certificate.json').write_text(json.dumps(dict(cases=records,intervals_checked=intervals),indent=2)+'\n')
    print('Exact joint-period cases checked:',len(records))
    print('Sharpened interval bounds checked:',intervals)
    print('PASS. Infinite theorem uses the proved Linnik prime supply; conjecture remains open.')

if __name__=='__main__':run()
