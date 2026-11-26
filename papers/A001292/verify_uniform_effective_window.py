#!/usr/bin/env python3
import json,math
from pathlib import Path
A=24*12577

def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def run():
    assert A==301848
    disc_constant=40**4*144**2;assert disc_constant<10**16
    h0=32;left=3**h0;right=2*h0+4+3*A*h0*(h0+1)**2
    assert left>=right and 10*(h0+1)<=3**h0
    induction_checks=0
    for h in range(2,10001):
        assert (h+2)**2<3*h*(h+1)
        assert 2*(h+1)+4<3*(2*h+4)
        induction_checks+=1
    cases=[];pairs=0
    for h in (32,33,40,64,100,128,256,512,1000):
        assert 10*(h+1)<=3**h
        rhs_exp=2*h+5+3*A*h*(h+1)**2
        assert 3**h+1>=rhs_exp
        es=[e for e in range(5,h+2) if prime(e)]
        for e in es:
            assert e<=h+1 and e*e<=(h+1)**2
            # Since 10e<=3^h, log_3 P_e <= A*h*e^2.
            exact_upper_exp=2*e+3+3*A*h*e*e
            assert exact_upper_exp<=rhs_exp<=3**h+1;pairs+=1
        cases.append(dict(h=h,prime_exponents=len(es),largest_prime=es[-1],sufficient_power3_exponent=rhs_exp))
    data=dict(A=A,discriminant_constant=disc_constant,h0=h0,base_left=left,base_right=right,induction_cases=induction_checks,growing_window_cases=cases,prime_window_pairs=pairs)
    Path(__file__).with_name('uniform-effective-window-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Discriminant constants and A=301848: PASS')
    print('h=32 exact base:',left,'>=',right)
    print('Finite induction audits:',induction_checks)
    print('Prime/window exponent comparisons:',pairs)
    print('PASS. Unbounded conclusions use the proof and cited unconditional theorem, not finite extrapolation.')
if __name__=='__main__':run()
