#!/usr/bin/env python3
import json,math
from pathlib import Path
from fractions import Fraction as F
ROWS=[(5,1031,103),(7,6203,443),(11,3191,29),(13,7151,275),(17,239,7),(19,43283,1139),(23,106031,2305),(29,36947,637),(31,49787,803)]
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
    result=[];recurrences=0;counts=0;coprimes=0
    for e,p,r in ROWS:
        assert prime(e) and prime(p) and p%12==11 and (p-1)%e==0
        assert pow(10,r,p)==1 and all(pow(10,r//ell,p)!=1 for ell in factors(r))
        assert math.gcd(r,6)==1 and r>1 and (p-1)%(e*r)==0
        assert pow(10,(p-1)//2,p)==1 and pow(10,(p-1)//e,p)==1
        nonpowers=sum(pow(x,(p-1)//e,p)!=1 for x in range(1,p))
        assert nonpowers==(p-1)*(e-1)//e;counts+=1
        for d in (1,2,3,6,9):
            if math.gcd(d,r)!=1:continue
            B=pow(10,d,p);alpha=pow(1-B,-1,p)
            for m,w in ((0,0),(7,11),(123,42)):
                z=w
                for i in range(1,r+1):z=(B*z+m+i)%p
                assert z==(w+r*alpha)%p;recurrences+=1
            for parity in (1,2):
                for h in range(1,31):assert math.gcd(parity*3**h,r)==1;coprimes+=1
        for h in range(e-1,e+50):
            b=e
            while e*b<=h+1:b*=e
            assert e*b>=h+2 and F(2,3**(e*b))<=F(2,3**(h+2))
        result.append(dict(e=e,p=p,exact_order=r,nonzero_nonpowers=nonpowers,witness_prime_density=str(F(1,8*e*(e-1))),endpoint_density_factor=str(F((p-1)*(e-1),e*p*r))))
    data=dict(witnesses=result,exact_nonpower_counts=counts,scalar_recurrence_checks=recurrences,width_coprimality_checks=coprimes)
    Path(__file__).with_name('chebotarev-exponent-witnesses-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Nine explicit prime/order/quadratic/e-th-power witnesses: PASS')
    print('Exact complete nonpower counts:',counts)
    print('Scalar composite-order recurrence checks:',recurrences)
    print('Width coprimality checks:',coprimes)
    print('PASS. All-exponent witness existence follows from the field/Chebotarev proof, not the nine examples.')
if __name__=='__main__':run()
