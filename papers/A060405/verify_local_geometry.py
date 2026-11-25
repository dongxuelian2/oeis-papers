#!/usr/bin/env python3
"""Exact certificates for local square classes on the -1 mod 720720 branch."""
M = 720720
A, B, I = (0,1,1,1), (0,1,1,2), (1,0,0,1)
# matrix depth, value depth, leading unit modulo p (modulo 8 for p=2)
EXPECTED = {2:(4,4,7),3:(3,4,2),5:(1,5,4),7:(2,2,3),11:(2,2,7),13:(2,2,5)}

def mul(a,b,q):
    x,y,z,w=a; u,v,s,t=b
    return ((x*u+y*s)%q,(x*v+y*t)%q,(z*u+w*s)%q,(z*v+w*t)%q)

def power(a,n,q):
    assert n>=0
    b=I
    while n:
        if n&1: b=mul(b,a,q)
        a=mul(a,a,q); n//=2
    return b

def valuation(x,p):
    assert x != 0
    k=0
    while x%p==0: x//=p; k+=1
    return k

def value(t,q):
    a,b=power(A,M*t,q),power(B,M*t,q)
    return (-a[0]+2*a[1]+b[0])%q

def depth(a,p):
    return min(valuation(x-y,p) for x,y in zip(a,I) if x!=y)

def check_constants():
    for p,(d,e,u) in EXPECTED.items():
        q=p**12; a,b=power(A,M,q),power(B,M,q)
        z=value(1,q)
        assert (min(depth(a,p),depth(b,p)),valuation(z,p),z//p**e%(8 if p==2 else p))==(d,e,u)
    q=5**8
    c,e=[tuple((x-y)%q for x,y in zip(power(a,M,q),I)) for a in (A,B)]
    a,b=power(c,2,q),power(e,2,q)
    z=(-a[0]+2*a[1]+b[0])%q
    assert z%625==500
    a,b=power(c,3,q),power(e,3,q)
    assert (-a[0]+2*a[1]+b[0])%625==0
    print('Matrix depths and leading units verified.')

def lift_root(digits):
    r=1
    for k in range(1,digits):
        roots=[r+j*5**k for j in range(5) if value(r+j*5**k,5**(k+4))==0]
        assert len(roots)==1
        r=roots[0]
    assert value(r,5**(digits+3))==0
    return r

def check_samples(root,digits):
    ts=set(range(1,501))|{j*p**k for p in EXPECTED for k in range(1,7) for j in (1,2,3)}
    ts|={root+j*5**k for k in range(1,8) for j in (1,2,3)}
    for t in sorted(ts):
        for p,(d,e,u) in EXPECTED.items():
            if p==5:
                if t%5 not in (0,1):
                    v=3; unit=2*t*(t-1)%5
                else:
                    x=t if t%5==0 else t-root
                    if x%5**digits==0: continue
                    j=valuation(x,5); v=3+j
                    unit=(3 if t%5==0 else 2)*(x//5**j)%5
            else:
                j=valuation(t,p); v=e+j; unit=u*(t//p**j)%(8 if p==2 else p)
            z=value(t,p**(v+(3 if p==2 else 1)))
            assert z!=0 and valuation(z,p)==v,(p,t,v,z)
            assert z//p**v%(8 if p==2 else p)==unit,(p,t,v,unit,z)
    print('Exact valuation/unit formulas checked for',len(ts),'sample indices.')

if __name__=='__main__':
    check_constants()
    digits=24
    root=lift_root(digits)
    assert root==9500531834602826
    print('Nonzero 5-adic root modulo 5**24:',root)
    check_samples(root,digits)
