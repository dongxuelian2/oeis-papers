#!/usr/bin/env python3
"""Exact finite certificate audit, not actual huge-width prefix enumeration."""
import json,math
from fractions import Fraction as F
from pathlib import Path

def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def leg(a,p):
    x=pow(a%p,(p-1)//2,p);return -1 if x==p-1 else x

def run():
    data=json.loads(Path(__file__).with_name('bounded-valuation-crt-certificate.json').read_text())
    rows=data['prime_data'];assert len(rows)==324
    ps=[x['p'] for x in rows];assert len(set(ps))==324
    L=111;epsilon=F(1)
    for x in rows:
        p,r,s=x['p'],x['r'],x['s']
        assert prime(p) and p<20000 and math.gcd(p,999)==1
        assert r>0 and s>0 and r%2 and math.gcd(r,10)==1
        assert pow(10,r,p)==1 and pow(10,s,9*r)==1
        assert leg(2,p)==-1
        ell=math.lcm(3,r,s);assert ell%3==0 and ell%9!=0
        L=math.lcm(L,r,s);epsilon*=F(p+3,2*p)
    T=999*math.prod(ps)
    assert L==data['width_period'] and T==data['endpoint_period']
    assert L%3==0 and L%9 and L%37==0
    assert len(str(L))==612 and len(str(T))==1233 and L>=1233+200
    assert epsilon<F(1,2**323)
    assert F(111,36*10**199)<F(1,2**640)
    assert F(1,2**323)+F(1,2**640)<F(1,2**322)
    good37=[b for b in range(37) if leg(b*(b+1)//2,37)==1]
    classes=[m for m in range(999) if m%27 in (8,18) and m%37 in good37]
    assert len(good37)==18 and len(classes)==36
    models=0
    for p in ps[:5]:
        for c in range(p):
            neg=sum(leg(t*(t+1)//2+c,p)==-1 for t in range(p))
            assert 2*neg>=p-3;models+=1
    crtchecks=0
    for mods in (ps[:2],ps[:3]):
        M=math.prod(mods)
        for shift in range(3):
            masks=[[leg(t*(t+1)//2+shift+i,p)!=-1 for t in range(p)] for i,p in enumerate(mods)]
            expected=math.prod(sum(mask) for mask in masks)
            actual=sum(all(mask[(classes[0]+999*t)%p] for mask,p in zip(masks,mods)) for t in range(M))
            assert actual==expected;crtchecks+=1
    print('324 distinct primes and all eligibility conditions: PASS')
    print('Exact width period digits:',len(str(L)))
    print('Exact endpoint period digits:',len(str(T)))
    print('Exact rational epsilon < 2^(-323) and interval error < 2^(-640): PASS')
    print('Endpoint classes modulo999:',len(classes))
    print('Exhaustive quadratic-constant models:',models)
    print('Exact complete CRT models:',crtchecks)
    print('PASS. No actual huge-width prefixes or endpoint intervals were enumerated.')
if __name__=='__main__':run()
