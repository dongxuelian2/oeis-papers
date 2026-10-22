#!/usr/bin/env python3
"""Independent prime-field audit of the new GMP single-period certificates.

These checks do not import the composite-ring C++ routine or its
geometric-sum implementation; instead use the standard field rational
formulas, with a separate q=1 case.
"""
def isprime(p):
    return p>1 and all(p%d for d in range(2,int(p**0.5)+1))

def n_order(a,p):
    assert isprime(p) and p not in (2,5)
    x=a%p
    n=1
    while x!=1:
        n+=1
        x=x*a%p
        assert n<=p
    return n

CASES = [
    # prime, actual multiplicative order, stable period, U, V
    (857, 856, 45368, 789, 388),
    (937, 936, 936, 61, 281),
]

def direct_field(p, r, T):
    assert isprime(p) and int(n_order(10, p)) == r
    C=Y=0
    L=1
    q=10%p
    Lr=1
    for d in range(1,2*T+1):
        n=9*L%p
        A=pow(10,(9*d*Lr)%r,p)
        if q==1:
            S=n
            J=n*(n-1)*pow(2,-1,p)%p
        else:
            inv=pow(q-1,-1,p)
            S=(A-1)*inv%p
            J=(q-n*A+(n-1)*A*q)*inv*inv%p
        C=(A*C+(q-1)*S-J)%p
        Y=pow(A,-1,p)*(Y+L*S+J)%p
        if d==T:
            C1,Y1=C,Y
        L,q,Lr=q,q*10%p,Lr*10%r
    return (C-C1)%p,(Y-Y1)%p,(C1,Y1)

if __name__ == "__main__":
    for p,r,T,U,V in CASES:
        u,v,(C,Y)=direct_field(p,r,T)
        assert (u,v)==(U,V),(p,r,u,v)
        assert u or v
        a=(10*u+v)%p
        offset=0 if a else 1
        slope=a if a else (1000*u+v)%p
        constant=(10*C+Y+1 if offset==0 else 1000*C+Y+121)%p
        j=1+(-constant*pow(slope,-1,p))%p
        assert 1<=j<=p and (constant+(j-1)*slope)%p==0
        print(f"PASS p={p}, r={r}, (U,V)=({u},{v}), witness k=10^({j}*{T})+{offset}")
    print("PASS independent prime-field checks; conjecture still OPEN in unbounded order.")
