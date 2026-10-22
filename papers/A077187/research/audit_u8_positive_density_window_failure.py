#!/usr/bin/env python3
"""A077187: independent, exact u=8 first post-defect window audit.

The main theorem is analytic, not a finite search: on a natural-density
1/32 set of primes, ord_p(10) has smooth part exactly 8 and a fixed
rational quadratic is irreducible mod p, so the entire first q=10
window AFTER the pT boundary has no divisible mountain.

This script checks the rational discriminant at a split prime 401;
then checks the original digit-layer affine prefix, the corrected
long-window group equation, and the subgroup-root distinctions at
eight illustrative primes. Stdlib only, no large-order enumeration.
"""
from fractions import Fraction
from math import gcd, lcm

BIGNUM=10**189
DEN=120758121
aa=Fraction(10,81)-Fraction(219804400,DEN*BIGNUM)
bb=Fraction(1,81)+Fraction(217557800*BIGNUM,DEN)
disc=Fraction(20,81)**2-40*aa*bb
SAMPLES={
  # prime: (order, Legendre(disc), number of subgroup roots)
  73:(8,1,0), 137:(8,1,0), 233:(232,1,2),
  313:(312,-1,0), 457:(152,-1,0), 617:(88,-1,0),
  857:(856,1,2), 1993:(664,1,0),
}

def as_field(x,p):
    assert x.denominator%p
    return x.numerator*pow(x.denominator,-1,p)%p

def ord10(n):
    if n==1:return 1
    assert gcd(n,10)==1
    z=10%n; t=1
    while z!=1:
        z=z*10%n;t+=1
        assert t<=n
    return t

def layer(p,r,d,C,Y,backwards=False):
    q=pow(10,d,p); L=pow(10,d-1,p); n=9*L%p
    mult=pow(10,9*d*pow(10,d-1,r)%r,p)
    if q==1:
        S=n; J=n*(n-1)*pow(2,-1,p)%p
    else:
        iv=pow(q-1,-1,p)
        S=(mult-1)*iv%p
        J=(q-n*mult+(n-1)*q*mult)*iv*iv%p
    up=((q-1)*S-J)%p
    down=(L*S+J)%p
    if backwards:
        return ((C-up)*pow(mult,-1,p)%p,(mult*Y-down)%p)
    return ((mult*C+up)%p,(Y+down)*pow(mult,-1,p)%p)

def audit_rational_discriminant():
    p=401
    assert p%80==1 and p%8==1
    assert (as_field(aa,p),as_field(bb,p),as_field(disc,p))==(146,228,24)
    assert pow(24,(p-1)//2,p)==p-1
    print("PASS split-prime certificate p=401, disc=24, Legendre=-1")
    for rem in (57,73):
        assert rem%16==9 and rem%5 in (2,3)
    print("PASS CRT residues 57/73 mod 80 force v2(ord)=3 and v5(ord)=0")

def audit_actual_primes():
    for p,(want_r,want_leg,want_count) in SAMPLES.items():
        assert p%80 in (57,73)
        r=ord10(p)
        assert r==want_r
        v=r//8
        assert r%8==0 and gcd(v,10)==1
        T=lcm(r,ord10(v))
        rho=pow(10,9*(pow(10,T,r)-1),p)
        assert pow(rho,4,p)==p-1
        C=Y=0
        for d in range(1,4):
            C,Y=layer(p,r,d,C,Y)
        for d in range(3,0,-1):
            C,Y=layer(p,r,T+d,C,Y,backwards=True)
        assert (C+10*pow(81,-1,p))%p==as_field(aa,p)*pow(rho,-1,p)%p
        assert (Y+pow(81,-1,p))%p==as_field(bb,p)*rho%p
        D=as_field(disc,p)
        leg=0 if not D else (1 if pow(D,(p-1)//2,p)==1 else -1)
        assert leg==want_leg
        # Original local mountain polynomial in the q=10 window.
        # q=10^(pT+1)=10, L=10^(pT)=1 mod p.
        zlist=[pow(10,n,p) for n in range(r)]
        original=[z for z in zlist if (
              (10*(C+10*pow(81,-1,p))*z*z
               -20*pow(81,-1,p)*z
               +Y+pow(81,-1,p))%p==0)]
        reduced=[y for y in zlist if (
              (10*as_field(aa,p)*y*y
               -20*pow(81,-1,p)*y+as_field(bb,p))%p==0)]
        # Gauge z=rho*y preserves the subgroup.
        assert set(original)=={rho*y%p for y in reduced}
        assert len(reduced)==want_count,(p,len(reduced),want_count)
        print(f"PASS actual p={p} r={r} v={v} leg={leg} subgroup_roots={len(reduced)}")
    print("PASS original affine defect + phase-gauge comparison")
    print("The density-1/32 theorem follows from CRT and Chebotarev, NOT this sample.")

if __name__=="__main__":
    audit_rational_discriminant()
    audit_actual_primes()
