#!/usr/bin/env python3
"""Exact modular certificates for prime-power index descent."""
from math import isqrt, lcm

A, B, I = (0, 1, 1, 1), (0, 1, 1, 2), (1, 0, 0, 1)
SIGNS = ((1, 1), (1, -1), (-1, 1), (-1, -1))
PAIRS = ((0, -1), (1, -1), (2, -1), (3, -1), (0, 1), (0, 2), (0, 3))
CLASSES = (1, 2, 5, 10)
WITNESSES = {
    3: ((1453,11,7,7),(1823,11,7,7),(1453,11,7,7),(1453,11,7,7),
        (1453,11,7,7),(1753,11,7,7),(1753,11,7,7)),
   -3: ((1753,11,7,7),(1753,11,7,7),(1453,11,7,7),(1933,11,7,7),
        (1823,11,7,7),(1453,11,7,7),(1753,11,7,7)),
   -2: ((1213,11,7,7),(1213,11,7,7),(1621,11,7,7),(1621,11,7,7),
        (1823,11,7,7),(1213,11,7,7),(1213,11,7,7)),
   -1: ((1453,1993,1753,1453),(1993,1453,1453,1753),
        (1753,1453,1453,1993),(1453,1753,1993,1453),
        (1453,2341,1753,1453),(1453,1753,2207,1453),(1753,1453,1453,2207)),
}


def mul(a,b,p):
    x,y,z,w=a; i,j,k,l=b
    return ((x*i+y*k)%p,(x*j+y*l)%p,(z*i+w*k)%p,(z*j+w*l)%p)


def mp(a,n,p):
    assert n>=0
    z=I
    while n:
        if n&1: z=mul(z,a,p)
        a=mul(a,a,p); n//=2
    return z


def leg(x,p):
    z=pow(x%p,(p-1)//2,p)
    return -1 if z==p-1 else z


def isprime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))


def mixed(r,k,s,p):
    """L_(r+s[0]*k)+P_(r+s[1]*k) mod p."""
    h=p*p-1
    a=mp(A,(r+s[0]*k)%h,p); b=mp(B,(r+s[1]*k)%h,p)
    return (2*a[0]+a[1]+b[1])%p


def descent(r,k,p,e):
    """Full formula, including odd k."""
    h=p*p-1
    s5,s2=leg(5,p)**e,leg(2,p)**e
    a=mp(A,(r+s5*k)%h,p); b=mp(B,(r+s2*k)%h,p)
    return ((-1)**(k*((1-s5)//2))*(2*a[0]+a[1])
            +(-1)**(k*((1-s2)//2))*b[1])%p


def check_descent():
    count=0
    for r in WITNESSES:
        for p in range(7,100):
            if not isprime(p): continue
            for k in (1,2,3,4,5,6,720720):
                for e in range(1,7):
                    assert descent(r,k,p,e)==mixed(r,k*p**e,(1,1),p)
                    count+=1
    print('Frobenius identity sample checks:',count)


def check_witnesses(D):
    assert {r:len(str(k)) for r,k in D.items()}=={3:429,-3:439,-2:342,-1:3483}
    count=0
    for r,rows in WITNESSES.items():
        assert D[r]%720720==0
        for (i,j),qs in zip(PAIRS,rows):
            for d,q in zip(CLASSES,qs):
                assert isprime(q) and q>5
                z=d*mixed(r,D[r],SIGNS[i],q)
                if j>=0: z*=mixed(r,D[r],SIGNS[j],q)
                assert leg(z,q)==-1,(r,i,j,d,q)
                count+=1
    print('Independent square-class witnesses:',count)


if __name__=='__main__':
    from verify_composite_lifting import certificate
    check_descent()
    from verify_extension import forced_divisor
    D=certificate()
    D[-1]=lcm(D[-1],forced_divisor())
    check_witnesses(D)
