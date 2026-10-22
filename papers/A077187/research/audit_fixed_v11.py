#!/usr/bin/env python3
"""Independent field-recursion and 22-coset audit for v=11.

Uses no SymPy, no symbolic resultant code and no previous certificate.
"""
from math import lcm
from audit_fixed_v7 import isprime,prime_factors,direct

CASES=[
    (23,22,18,9),
    (89,44,57,29),
    (331,110,57,302),
    (617,88,405,356),
    (1321,55,712,15),
    (5501,5500,501,3175),
    (13751,6875,435,9997),
    (21649,11,3181,20235),
]

def spectral(p,r):
    u=r//11
    g=11 if u%2 else 22
    ell=22
    m=r//g
    T=ell*m
    assert T==lcm(r,2)
    zeta=pow(10,m,p)
    assert pow(zeta,g,p)==1
    assert all(pow(zeta,g//q,p)!=1 for q in prime_factors(g))
    gamma=pow(u,-1,11)
    inv10=pow(10,-1,p)
    inv200=pow(200,-1,p)
    inv2=pow(2,-1,p)
    inv12=pow(12,-1,p)
    P=1
    U=V=0
    for a in range(1,ell+1):
        A=pow(zeta,(g//11)*gamma*9*a*pow(10,a-1,11),p)
        PA=P*A%p
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
           +(9*Pinv*inv200 if singular else 0))%p
        V+=(beta*(inv10*F1-F2)+9*PA*inv10*F1
           +(9*P*inv200 if singular else 0))%p
        P=PA
    assert P==1
    return U%p,V%p,T

if __name__=="__main__":
    for p,r,U,V in CASES:
        assert isprime(p) and (p-1)%r==0
        assert pow(10,r,p)==1
        assert all(pow(10,r//q,p)!=1 for q in prime_factors(r))
        us,vs,T=spectral(p,r)
        ud,vd=direct(p,r,T)
        assert (us,vs)==(ud,vd)==(U,V),(p,r,(us,vs),(ud,vd),(U,V))
        print("PASS p",p,"r",r,"T",T,"drift",(U,V))
    print("PASS 8 independent v=11 field-recurrence / spectral checks")
    print("The infinite-family conclusion uses the separate exact norm certificate.")
