#!/usr/bin/env python3
"""Independent finite-field audit of the fixed-v=7 spectral compression.

No SymPy, no import from the symbolic certifier, no algebraic norms.
Direct digit-layer recursion is independently compared to a 42-coset
closed formula for selected primes of large and small exact orders.
"""
from math import gcd, lcm

CASES = [
    # prime, exact order, drift U, drift V
    (29,28,8,26),
    (71,35,56,60),
    (113,112,112,56),
    (239,7,8,100),
    (421,140,332,262),
    (701,700,495,692),
    (7841,56,7833,1704),
    (17921,8960,12584,7191),
]

def prime_factors(n):
    answer=[]
    d=2
    while d*d<=n:
        if n%d==0:
            answer.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:answer.append(n)
    return answer

def isprime(n):
    return n>=2 and all(n%d for d in range(2,int(n**0.5)+1))

def direct(p,r,T):
    C=Y=0
    L=1
    q=10%p
    power=1
    for d in range(1,2*T+1):
        n=9*L%p
        A=pow(10,9*d*power%r,p)
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
            C0,Y0=C,Y
        L=q
        q=q*10%p
        power=power*10%r
    return (C-C0)%p,(Y-Y0)%p

def spectral(p,r):
    u=r//7
    g=7 if u%2 else 14
    ell=42
    m=r//g
    T=m*ell
    assert T==lcm(r,6)
    zeta=pow(10,m,p)
    assert pow(zeta,g,p)==1
    assert all(pow(zeta,g//q,p)!=1 for q in prime_factors(g))
    gamma=pow(u,-1,7)
    inv10=pow(10,-1,p)
    inv200=pow(200,-1,p)
    inv2=pow(2,-1,p)
    inv12=pow(12,-1,p)
    P=1
    U=V=0
    for a in range(1,ell+1):
        A=pow(zeta,(g//7)*gamma*9*a*pow(10,a-1,7),p)
        Pnext=P*A%p
        Pinv=pow(P,-1,p)
        alpha=Pinv*(1-pow(A,-1,p))%p
        beta=P*(A-1)%p
        c=pow(zeta,a,p)
        if c==1:
            nreg=m-1
            F1=(m-1)*inv2%p
            F2=-(m*m-1)*inv12%p
            singular=True
        else:
            nreg=m
            ic=pow(c-1,-1,p)
            F1=m*c*ic%p
            F2=m*m*c*ic*ic%p
            singular=False
        U+=(alpha*(nreg+F2)-9*Pinv*inv10*F1
            + (9*Pinv*inv200 if singular else 0))%p
        V+=(beta*(inv10*F1-F2)+9*Pnext*inv10*F1
            + (9*P*inv200 if singular else 0))%p
        P=Pnext
    assert P==1
    return (U%p,V%p,T,g,m,gamma)

def main():
    for p,r,U,V in CASES:
        assert isprime(p) and (p-1)%r==0
        assert pow(10,r,p)==1
        assert all(pow(10,r//q,p)!=1 for q in prime_factors(r))
        us,vs,T,g,m,gamma=spectral(p,r)
        ud,vd=direct(p,r,T)
        assert (us,vs)==(ud,vd)==(U,V),(p,(us,vs),(ud,vd),(U,V))
        print("PASS p",p,"r",r,"g",g,"m",m,
              "gamma",gamma,"drift",(U,V))
    print("PASS 8 independent symbolic-free finite-field comparisons")
    print("The infinite theorem requires the separate exact symbolic certificate.")

if __name__=="__main__":
    main()
