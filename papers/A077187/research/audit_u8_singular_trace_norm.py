#!/usr/bin/env python3
"""A077187: exact uniform u=8 defect trace and nonsquare norm.

Uses Fraction polynomial arithmetic modulo x^4+1, and independent
modular digit-layer recurrences. Standard library; no order-bound scan.
"""
from fractions import Fraction as Q
from math import gcd,lcm

D=120758121; P=10**189
a=Q(10,81)-Q(219804400,D*P)
b=Q(1,81)+Q(217557800*P,D)
c=Q(-11,81)
EXAMPLES={73:(8,22,27,1),137:(8,96,36,1),233:(232,97,38,1),
          313:(312,5,248,-1),617:(88,435,598,1),
          2393:(184,58,2087,1),7841:(56,2725,1339,-1)}

def const(z): return [Q(z),Q(0),Q(0),Q(0)]
def add(x,y): return [i+j for i,j in zip(x,y)]
def mul(x,z): return [i*z for i in x]
def rotate(x,k):
    out=const(0)
    for i,z in enumerate(x):
        q,r=divmod(i+k,4)
        out[r]+=(-z if q%2 else z)
    return out

def terms(d,A):
    q=10**d; L=10**(d-1); n=9*L
    S=Q(A-1,q-1)
    J=Q(q-n*A+(n-1)*q*A,(q-1)**2)
    return (q-1)*S-J,L*S+J

def symbolic():
    C=Y=Q(0)
    for d in (1,2,3):
        A=10**(9*d*10**(d-1))
        B,R=terms(d,A)
        C,Y=A*C+B,(Y+R)/A
    C,Y=const(C),const(Y)
    for d in (3,2,1):
        A=10**(9*d*10**(d-1))
        B0,R0=terms(d,0);B1,R1=terms(d,1)
        shift=1 if d==1 else 0
        sign=1 if d==1 else -1
        Bhat=add(const(B0),rotate(const(sign*A*(B1-B0)),shift))
        Rhat=add(const(R0),rotate(const(sign*A*(R1-R0)),shift))
        C=rotate(mul(add(C,mul(Bhat,-1)),Q(1,sign*A)),-shift)
        Y=add(rotate(mul(Y,sign*A),shift),mul(Rhat,-1))
    assert C==add(const(-Q(10,81)),rotate(const(a),-1))
    assert Y==add(const(-Q(1,81)),rotate(const(b),1))
    print("PASS: exact finite-defect map in Q[x]/(x^4+1)")

def mod(z,p): return z.numerator*pow(z.denominator,-1,p)%p
def order(p):
    x=10%p; r=1
    while x!=1:
        x=x*10%p;r+=1
    return r

def layer(p,r,d,C,Y,inverse=False):
    q=pow(10,d,p); L=pow(10,d-1,p); n=9*L%p
    A=pow(10,9*d*pow(10,d-1,r)%r,p)
    if q==1: S=n;J=n*(n-1)*pow(2,-1,p)%p
    else:
        iq=pow(q-1,-1,p);S=(A-1)*iq%p
        J=(q-n*A+(n-1)*q*A)*iq*iq%p
    B=((q-1)*S-J)%p;R=(L*S+J)%p
    if inverse: return (C-B)*pow(A,-1,p)%p,(A*Y-R)%p
    return (A*C+B)%p,(Y+R)*pow(A,-1,p)%p

def audit():
    prime=23
    aa,bb,cc=(mod(x,prime) for x in (a,b,c))
    norm=((aa*aa-bb*bb)**2+(2*aa*bb-cc*cc)**2)%prime
    assert (aa,bb,cc,norm)==(10,22,1,7)
    assert pow(norm,(prime-1)//2,prime)==prime-1
    print("PASS: field norm nonsquare modulo 23 (residue 7)")
    for p,(r0,rho0,K0,chi0) in EXAMPLES.items():
        r=order(p);v=r//8
        assert r==r0 and gcd(v,10)==1
        T=lcm(r,order(v) if v>1 else 1)
        rho=pow(10,9*(pow(10,T,r)-1),p)
        assert rho==rho0 and pow(rho,4,p)==p-1
        C=Y=0
        for d in (1,2,3): C,Y=layer(p,r,d,C,Y)
        for d in (3,2,1): C,Y=layer(p,r,T+d,C,Y,True)
        assert C==(-10*pow(81,-1,p)+mod(a,p)*pow(rho,-1,p))%p
        assert Y==(-pow(81,-1,p)+mod(b,p)*rho)%p
        K=(C+Y)%p
        chi=0 if K==0 else (1 if pow(-K%p,(p-1)//2,p)==1 else -1)
        assert (K,chi)==(K0,chi0)
        print(f"PASS p={p}, ord={r}, Wsum={K}, singular character={chi}")
    print("PASS both singular outcomes; unrestricted mountain problem OPEN.")

if __name__=="__main__":
    symbolic()
    audit()
