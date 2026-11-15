#!/usr/bin/env python3
"""Finite audits, not a proof of the integer perfect-power conjecture."""
import json, math, random
from fractions import Fraction
from pathlib import Path

def primes(n):
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for p in range(2,math.isqrt(n)+1):
        if a[p]:a[p*p:n+1:p]=b'\0'*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if a[p]]

def width(n,g):
    d=0
    while n:n//=g;d+=1
    return d

def direct_arrays(g,n,p):
    w=[0];ds=[0]
    for m in range(1,n+1):
        d=width(m,g);w.append((w[-1]*pow(g,d,p)+m)%p);ds.append(ds[-1]+d)
    return w,ds

def audit_joint():
    records=[]
    cases=[(2,(3,7,13)),(2,(5,11,23)),(3,(7,13,19)),(5,(11,31))]
    for ell,ps in cases:
        T=math.lcm(*(p*(p-1) for p in ps))
        expected=math.prod(Fraction(p+ell-1,ell*p) for p in ps)
        # Deliberately vary coefficients across primes; second trial has zero alpha.
        for trial in range(2):
            allowed=[]
            for p in ps:
                B=2;alpha=(p+trial*7+3)%p if trial==0 else 0
                beta=(3*trial+1)%(p-1)+1;gamma=(p*p+11*trial+2)%p
                roots={pow(x,ell,p) for x in range(p)}
                allowed.append([((alpha*pow(B,n,p)+beta*n+gamma)%p) in roots for n in range(p*(p-1))])
            good=sum(all(a[n%len(a)] for a in allowed) for n in range(T))
            assert Fraction(good,T)==expected,(ell,ps,trial,good,T,expected)
            records.append(dict(exponent=ell,primes=ps,trial=trial,period=T,survivors=good,density=str(expected)))
    return records

def audit_rotations():
    rng=random.Random(1292);checks=0
    for g in (2,3,10):
        for p in primes(47):
            if g%p==0:continue
            w,ds=direct_arrays(g,600,p)
            for _ in range(400):
                m=rng.randrange(2,601);k=rng.randrange(m);d=width(m,g)
                B=g**d;L=g**(d-1);C=B-1
                if C%p==0:continue
                inv=pow(C,-1,p);u=pow(g,ds[k],p)
                A=(C*C*w[L-1]+L*C+1)%p
                alpha=((u*A*inv*inv-pow(g,ds[L-1],p)*w[k])*pow(B,1-L,p))%p
                beta=-u*inv%p;gamma=(w[k]-u*B*inv*inv)%p
                affine=(alpha*pow(B,m,p)+beta*m+gamma)%p
                rotation=(u*w[m]-(pow(g,ds[m],p)-1)*w[k])%p
                assert beta and affine==rotation,(g,p,m,k)
                checks+=1
    return checks

def audit_selection():
    records=[]
    for g in (2,3,10):
        for ell in (2,3,5,7):
            a=math.log(g)/4
            A0=math.ceil(1+(ell-1)*(math.log(g)+a+2))
            for d in (100,300,1000):
                eligible=[p for p in primes(A0*d) if p>=d and p%ell==1 and g%p and pow(g,d,p)!=1]
                t=math.floor(a*d/math.log(d));assert len(eligible)>=t
                chosen=eligible[:t];T=math.lcm(*(p*(p-1) for p in chosen)) if chosen else 1
                prod=math.prod(p*(p-1) for p in chosen)
                assert T<=prod<=(A0*d)**(2*t)
                density=math.prod(Fraction(p+ell-1,ell*p) for p in chosen)
                records.append(dict(base=g,exponent=ell,width=d,A0=A0,eligible=len(eligible),selected=t,period_bits=T.bit_length(),density=str(density)))
    return records

if __name__=='__main__':
    data=dict(joint_densities=audit_joint(),direct_rotation_checks=audit_rotations(),prime_selections=audit_selection())
    out=Path(__file__).with_name('growing-prime-sieve-certificate.json')
    out.write_text(json.dumps(data,indent=2)+'\n')
    print('Exact joint-density checks:',len(data['joint_densities']))
    print('Direct affine-rotation checks:',data['direct_rotation_checks'])
    print('Growing-prime selection and period checks:',len(data['prime_selections']))
    print('PASS. Asymptotic theorem is proved in GROWING_PRIME_SIEVE.md; integer conjecture remains open.')
