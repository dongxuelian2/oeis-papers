#!/usr/bin/env python3
"""A077187: independent finite-defect Duhamel flux and phase-squareclass audit.

Checks a universal algebraic identity in 16 genuine prime fields, with
three independent constructions of W where the period is short.
Also verifies a split prime (41) witnessing that the rational norm of
the u=8 defect trace is not a square in Q(zeta_8).
Standard library only. Not a proof of the unrestricted conjecture.
"""
from fractions import Fraction
from math import gcd, lcm

PRIMES=(7,11,17,23,37,43,73,101,137,149,211,233,313,617,2393,7841)
DEN=120758121
TEN=10**189
COEFFICIENTS=(
    Fraction(10,81)-Fraction(219804400,DEN*TEN),
    Fraction(1,81)+Fraction(217557800*TEN,DEN),
    Fraction(-11,81),
)

def multiplicative_order(n):
    if n==1: return 1
    assert gcd(n,10)==1
    t=10%n
    k=1
    while t!=1:
        t=t*10%n
        k+=1
        assert k<=n
    return k

def factor_smooth(r):
    u=1
    v=r
    a=c=0
    while v%2==0:
        a+=1;u*=2;v//=2
    while v%5==0:
        c+=1;u*=5;v//=5
    return u,v,max(a,c)

def full_map(p,r,d,state,inverse=False):
    C,Y=state
    q=pow(10,d,p)
    L=pow(10,d-1,p)
    m=9*L%p
    A=pow(10,(9*d*pow(10,d-1,r))%r,p)
    if q==1:
        S=m
        J=m*(m-1)*pow(2,-1,p)%p
    else:
        iq=pow(q-1,-1,p)
        S=(A-1)*iq%p
        J=(q-m*A+(m-1)*A*q)*iq*iq%p
    B=((q-1)*S-J)%p
    R=(L*S+J)%p
    if inverse:
        return ((C-B)*pow(A,-1,p)%p,(A*Y-R)%p)
    return ((A*C+B)%p,(Y+R)*pow(A,-1,p)%p)

def verify_prime(p):
    r=multiplicative_order(p)
    u,v,h=factor_smooth(r)
    T=lcm(r,multiplicative_order(v))
    actual=stable=(0,0)
    prod=1
    flux_C=flux_Y=0
    for d in range(1,h+1):
        q=pow(10,d,p)
        assert q!=1
        L=pow(10,d-1,p)
        inv=pow(q-1,-1,p)
        cent_C=(L*inv+inv*inv)%p
        cent_Y=(-L*inv+q*inv*inv)%p
        A=pow(10,9*d*pow(10,d-1,r)%r,p)
        Ahat=pow(10,9*(T+d)*pow(10,T+d-1,r)%r,p)
        rho=Ahat*pow(A,-1,p)%p
        term_C=pow(prod,-1,p)*(pow(rho,-1,p)-1)*(actual[0]+cent_C)%p
        term_Y=prod*(rho-1)*(actual[1]+cent_Y)%p
        # The scalar flux is exactly (rho-1)(Z-X/rho).
        X=(actual[0]+cent_C)*pow(prod,-1,p)%p
        Z=(actual[1]+cent_Y)*prod%p
        assert (term_C+term_Y-(rho-1)*(Z-X*pow(rho,-1,p)))%p==0
        flux_C=(flux_C+term_C)%p
        flux_Y=(flux_Y+term_Y)%p
        actual=full_map(p,r,d,actual)
        stable=full_map(p,r,T+d,stable)
        prod=prod*Ahat%p
    W=((actual[0]-stable[0])*pow(prod,-1,p)%p,
       (actual[1]-stable[1])*prod%p)
    assert (flux_C,flux_Y)==W,(p,"Duhamel",W,(flux_C,flux_Y))
    reverse=actual
    for d in range(h,0,-1):
        reverse=full_map(p,r,T+d,reverse,inverse=True)
    assert reverse==W,(p,"inverse",reverse,W)
    # When the period is modest, compare with original two-block
    # states, not with the affine-prefix formula.
    if T<=500:
        S=(0,0)
        ST=None
        for d in range(1,2*T+1):
            S=full_map(p,r,d,S)
            if d==T: ST=S
        reconstructed=((2*ST[0]-S[0])%p,(2*ST[1]-S[1])%p)
        assert reconstructed==W,(p,"global block",reconstructed,W)
    if u==8:
        a,b,c=COEFFICIENTS
        rho=pow(10,9*(pow(10,T,r)-1),p)
        assert pow(rho,4,p)==p-1
        def evaluate(fr):
            return fr.numerator*pow(fr.denominator,-1,p)%p
        assert W==((-10*pow(81,-1,p)+evaluate(a)*pow(rho,-1,p))%p,
                   (-pow(81,-1,p)+evaluate(b)*rho)%p)
        # New hyperbola invariant; independent of the chosen root.
        assert ((W[0]+10*pow(81,-1,p))*(W[1]+pow(81,-1,p))
                -evaluate(a)*evaluate(b))%p==0
    if u>0 and 20%u==0:
        rho=pow(10,9*(pow(10,T,r)-1),p) if h else 1
        assert W==((pow(rho,-1,p)-1)*10*pow(81,-1,p)%p,
                   (rho-1)*pow(81,-1,p)%p)
    print(f"PASS p={p} r={r} smooth_u={u} T={T} h={h} W={W}")

def norm_phase_audit():
    a,b,c=COEFFICIENTS
    for p in (41,73,97,137):
        assert p%8==1
        def ev(fr):
            return fr.numerator*pow(fr.denominator,-1,p)%p
        aa,bb,cc=ev(a),ev(b),ev(c)
        norm=((aa*aa-bb*bb)**2+(2*aa*bb-cc*cc)**2)%p
        assert norm and pow(norm,(p-1)//2,p)==p-1
        primitive=[x for x in range(1,p) if pow(x,8,p)==1 and pow(x,4,p)==p-1]
        assert len(primitive)==4
        signs=[]
        conjugate_product=1
        for x in primitive:
            E=(cc+aa*pow(x,-1,p)+bb*x)%p
            assert E
            conjugate_product=conjugate_product*E%p
            signs.append(1 if pow(-E%p,(p-1)//2,p)==1 else -1)
        assert conjugate_product==norm
        assert signs.count(-1)%2==1
        assert 1 in signs and -1 in signs
        print(f"PASS split p={p} Norm={norm} four formal phase signs={signs}")
    print("PASS nonsquare norm at split p=41 => sqrt(Norm) not in Q(zeta8)")
    print("No claim that each formal phase occurs as the actual digit defect at a fixed prime.")

if __name__=="__main__":
    for p in PRIMES:verify_prime(p)
    norm_phase_audit()
    print("PASS exact Duhamel trace and conjugate-phase tests; A077187 OPEN")
