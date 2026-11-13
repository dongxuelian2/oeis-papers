#!/usr/bin/env python3
import math,json
from pathlib import Path
ROWS=[(1,5,1031,103),(2,5,1031,103),(5,5,1031,103),(25,5,1031,103),(103,5,14831,1483),(7,7,207719,14837),(35,7,207719,14837),(77,7,836879,59777),(13,13,808679,31103)]
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

def crt(mods,rs):
    a=0;M=1
    for n,b in zip(mods,rs):
        a+=M*((b-a)*pow(M,-1,n)%n);M*=n;a%=M
    return a,M

def run():
    out=[];coprimes=0
    for u,e,p,r in ROWS:
        assert math.gcd(u,3)==1 and prime(e) and prime(p)
        S=sorted(({3,5}|set(factors(u)))-{2,e})
        mods=[8,e*e]+S;rs=[7,1+e]+[ell-1 for ell in S]
        a,M=crt(mods,rs);assert math.gcd(a,M)==1 and M%40==0 and M%e==0
        assert a%8==7 and a%e==1 and a%5 in(1,4)
        assert p%M==a and p%8==7 and p%3==2
        assert (p-1)%e==0 and (p-1)%(e*e)!=0
        assert pow(10,(p-1)//2,p)==1 and pow(10,(p-1)//e,p)==1
        assert pow(10,r,p)==1 and all(pow(10,r//ell,p)!=1 for ell in factors(r))
        assert math.gcd(r,6*u)==1 and (p-1)%(e*r)==0
        for h in range(1,101):assert math.gcd(u*3**h,r)==1;coprimes+=1
        phi=M
        for ell in factors(M):phi=phi//ell*(ell-1)
        out.append(dict(multiplier=u,exponent=e,modulus=M,residue=a,prime=p,exact_order=r,extension_degree=e*phi))
    assert math.gcd(103,103)>1 and math.gcd(1483,103)==1
    data=dict(witnesses=out,width_coprimality_checks=coprimes)
    Path(__file__).with_name('multiplier-witnesses-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Nine CRT/prime/exact-order witnesses: PASS')
    print('Quadratic compatibility and exponent-dividing-multiplier cases: PASS')
    print('Fixed-multiplier width coprimality checks:',coprimes)
    print('PASS. Arbitrary fixed multiplier existence follows from proof, not nine samples.')
if __name__=='__main__':run()
