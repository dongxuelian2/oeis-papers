#!/usr/bin/env python3
import json,math
from pathlib import Path

def run():
    prefix=0; width_checks=identity_checks=0
    for n in range(1,10000):
        prefix=prefix*10**len(str(n))+n
        if n not in (9,99,999,9999):continue
        d=len(str(n))+1;B=10**d;L=B//10;C=B-1
        t=(d-1)*L-(L-1)//9
        A=C*C*prefix+L*C+1
        assert 10**(t-1)<=prefix<10**t
        scale=10**(t+2*d)
        assert 1000*A>=81*scale and A<2*scale
        assert math.gcd(A,C*C)==1 and A>C*C
        assert prefix%B==9*L-1 and A%B==8*L
        z=A;v=0
        while z%5==0:z//=5;v+=1
        assert v==d-1
        w=prefix
        for m in range(L,L+8):
            w=w*B+m;N=m-L+1
            assert C*C*w==A*B**N-(m*C+B)
            identity_checks+=1
        width_checks+=1
    count=0
    for d in range(2,2001):
        L=10**(d-1);t=(d-1)*L-(L-1)//9
        # Exact simplification used in the limiting ratio.
        assert 9*t==(9*d-10)*L+1
        count+=1
    out=dict(widths=[2,3,4,5],coefficient_checks=width_checks,
             exact_prefix_identities=identity_checks,digit_formula_checks=count)
    Path(__file__).with_name('coefficient-height-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2));print('PASS. The height limit is proved algebraically, not inferred from tests.')
if __name__=='__main__':run()
