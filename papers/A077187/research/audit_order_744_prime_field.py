#!/usr/bin/env python3
"""Independent prime-field cross-check for the 744 bound certificate.

This script NEVER imports the repunit-ring geometric-sum routine.
It derives the affine full-layer map directly from rational geometric sums
in F_p (q=1 handled separately). Checks order, endpoints, drift and a
two-offset witness congruence against frozen test vectors.
"""
from math import gcd, lcm

CASES = [
    # p, r, T, U mod p, V mod p
    (1753, 584, 584, 1438, 1332),
    (1993, 664, 27224, 1889, 1956),
    (13921, 696, 4872, 13258, 9689),
]

def factors(n):
    result=[];t=2
    while t*t<=n:
        if n%t==0:
            result.append(t)
            while n%t==0:n//=t
        t+=1
    if n>1:result.append(n)
    return result

def prime(p):
    return p>1 and all(p%i for i in range(2,int(p**0.5)+1))

def check(p,r,T,wantU,wantV):
    assert prime(p) and (p-1)%r==0
    assert pow(10,r,p)==1
    assert all(pow(10,r//q,p)!=1 for q in factors(r))
    C=Y=0
    L=1
    q=10%p
    Lr=1
    inv2=pow(2,-1,p)
    midpoint=None
    for d in range(1,2*T+1):
        N=9*L%p
        A=pow(10,(9*d*Lr)%r,p)
        if q==1:
            S=N
            J=N*(N-1)*inv2%p
        else:
            inv=pow(q-1,-1,p)
            S=(A-1)*inv%p
            J=(q-N*A+(N-1)*A*q)*inv*inv%p
        C=(A*C+(q-1)*S-J)%p
        Y=pow(A,-1,p)*(Y+L*S+J)%p
        if d==T:midpoint=(C,Y)
        L,q,Lr=q,q*10%p,Lr*10%r
    U,V=(C-midpoint[0])%p,(Y-midpoint[1])%p
    assert (U,V)==(wantU,wantV),(p,r,T,U,V)
    assert (U,V)!=(0,0)
    slope0=(10*U+V)%p
    joffset=0 if slope0 else 1
    slope=slope0 if slope0 else (1000*U+V)%p
    const=(
        (10*midpoint[0]+midpoint[1]+1) if joffset==0
        else (1000*midpoint[0]+midpoint[1]+121)
    )%p
    j=1+(-const*pow(slope,-1,p))%p
    assert 1<=j<=p
    assert (const+(j-1)*slope)%p==0
    return j,joffset

if __name__=='__main__':
    for p,r,T,U,V in CASES:
        j,offset=check(p,r,T,U,V)
        print(f"PASS independent F_{p} drift for order {r}; k=10^({j}*{T})+{offset}")
    print("PASS all three independent field checks; unrestricted problem open.")
