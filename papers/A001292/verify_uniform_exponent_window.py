#!/usr/bin/env python3
"""Finite audits of the uniform window, not an effective asymptotic threshold."""
import json, math
from fractions import Fraction
from pathlib import Path
from verify_growing_prime_sieve import primes

def run():
    records=[];total=0
    for g in (2,3,10):
        a=math.log(g)/4;C=math.ceil(math.log(g)+a+2)
        for d in (100,300,1000):
            cap=math.floor(math.log(d)**2)
            es=primes(cap);ps=primes(2*C*max(es)*d)
            t=math.floor(a*d/math.log(d))
            assert t>1
            densities=[];details=[]
            for ell in es:
                Y=C*ell*d
                chosen=[p for p in ps if Y<=p<=2*Y and p%ell==1 and g%p and pow(g,d,p)!=1][:t]
                assert len(chosen)==t,(g,d,ell)
                T=math.lcm(*(p*(p-1) for p in chosen))
                assert T <= (2*C*ell*d)**(2*t)
                delta=math.prod(Fraction(p+ell-1,ell*p) for p in chosen)
                rational_upper=Fraction(1,ell**t)*Fraction(C*d+1,C*d)**t
                assert delta<=rational_upper
                densities.append(delta)
                details.append(dict(exponent=ell,selected=t,min_prime=min(chosen),max_prime=max(chosen),period_bits=T.bit_length()))
                total+=1
            summed=sum(densities,Fraction(0))
            bound=Fraction(C*d+1,C*d)**t * Fraction(1,2**t)*Fraction(t+1,t-1)
            assert summed<=bound
            records.append(dict(base=g,width=d,window_exponent=2,exponent_cap=cap,C=C,primes_per_exponent=t,exponents_checked=len(es),sum_density_upper=str(bound),details=details))
    data=dict(window_cases=records,total_exponent_selections=total)
    Path(__file__).with_name('uniform-exponent-window-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Growing exponent windows checked:',len(records))
    print('Uniform prime selections, density and period bounds checked:',total)
    print('Exact rational union-density bounds checked:',len(records))
    print('PASS. No effective Siegel-Walfisz threshold or full conjecture resolution is claimed.')

if __name__=='__main__':run()
