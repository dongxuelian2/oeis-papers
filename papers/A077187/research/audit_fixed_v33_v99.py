#!/usr/bin/env python3
"""Independent field audit of the 22-phase lift for v=33 and v=99.

Stdlib only. Does NOT import spectral/norm scripts or the cyclotomic
exclusion routine. Compares a closed 22-coset formula with the full
direct 2T-layer recurrence, and checks exact multiplicative orders.
Finite unit tests, not the infinity proof.
"""
from math import gcd,lcm

# s, prime, r, T, U, V : independently frozen exact field vectors
CASES=[
    (3,67,33,66,9,32),
    (3,2113,2112,2112,638,373),
    (3,2377,264,264,2051,844),
    (3,3301,3300,3300,415,1340),
    (3,5281,2640,2640,4219,5129),
    (3,16369,264,264,1340,592),
    (3,18481,1320,1320,14781,4029),
    (3,21121,10560,10560,16550,11004),
    (9,199,99,198,36,138),
    (9,397,99,198,278,189),
    (9,991,495,990,87,471),
    (9,4951,2475,4950,2243,94),
    (9,6337,6336,6336,1654,6086),
    (9,14851,990,990,7481,3274),
    (9,19801,9900,9900,3922,3935),
]

def factor(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out

def isprime(n):
    return n>=2 and all(n%d for d in range(2,int(n**0.5)+1))

def direct(p,r,T):
    C=Y=0
    L=1;q=10%p; t=1
    for d in range(1,2*T+1):
        n=9*L%p
        A=pow(10,9*d*t%r,p)
        if q==1:
            S=n; J=n*(n-1)*pow(2,-1,p)%p
        else:
            iq=pow(q-1,-1,p)
            S=(A-1)*iq%p
            J=(q-n*A+(n-1)*A*q)*iq*iq%p
        C=(A*C+(q-1)*S-J)%p
        Y=pow(A,-1,p)*(Y+L*S+J)%p
        if d==T:C1,Y1=C,Y
        L=q;q=q*10%p;t=t*10%r
    return (C-C1)%p,(Y-Y1)%p

def folded_spectral(p,r,s):
    u=r//(11*s)
    g0=11 if u%2 else 22
    m=r//g0  # = (s*u)/(g0/11)
    assert m*22==lcm(r,2)
    xi=pow(10,m,p)
    assert pow(xi,g0,p)==1
    assert all(pow(xi,g0//q,p)!=1 for q in factor(g0))
    gamma=pow((s*u)%11,-1,11)
    P=1
    U=V=0
    inv10=pow(10,-1,p); inv200=pow(200,-1,p)
    inv2=pow(2,-1,p); inv12=pow(12,-1,p)
    for j in range(1,23):
        A=pow(xi,(g0//11)*gamma*9*j*pow(10,j-1,11),p)
        PA=P*A%p
        Pinv=pow(P,-1,p)
        alpha=Pinv*(1-pow(A,-1,p))%p
        beta=P*(A-1)%p
        c=pow(xi,j,p)
        if c==1:
            nr=m-1
            F1=(m-1)*inv2%p
            F2=-(m*m-1)*inv12%p
            singular=True
        else:
            nr=m
            ic=pow(c-1,-1,p)
            F1=m*c*ic%p
            F2=m*m*c*ic*ic%p
            singular=False
        U+=(alpha*(nr+F2)-9*Pinv*inv10*F1
           +(9*Pinv*inv200 if singular else 0))%p
        V+=(beta*(inv10*F1-F2)+9*PA*inv10*F1
           +(9*P*inv200 if singular else 0))%p
        P=PA
    assert P==1
    return (U%p,V%p)

def audit_3adic_phase_depth():
    count=0
    for b in range(1,8):
        for a in (0,1,3):
            for c in (0,1):
                r=11*3**b*2**a*5**c
                d=2+max(a,c)  # safely in the stable range
                for t in range(6):
                    L=22*3**t
                    exp0=(9*d*pow(10,d-1,r))%r
                    exp1=(9*(d+L)*pow(10,d+L-1,r))%r
                    order=r//gcd(r,(exp1-exp0)%r)
                    assert order==3**max(b-2-t,0),(a,b,c,t,order)
                    count+=1
    print(f"PASS sharp 3-adic phase defect in {count} independent exponent checks")

if __name__=="__main__":
    for s,p,r,T,wU,wV in CASES:
        assert isprime(p) and r%(11*s)==0
        assert (p-1)%r==0 and pow(10,r,p)==1
        assert all(pow(10,r//q,p)!=1 for q in factor(r))
        assert T==lcm(r,2)
        spect=folded_spectral(p,r,s)
        full=direct(p,r,T)
        assert spect==full==(wU,wV),(p,s,r,spect,full,(wU,wV))
        print(f"PASS s={s}, p={p}, r={r}, T={T}, drift={spect}")
    print("PASS 15 fully independent original-digit-layer vs 22-phase checks")
    audit_3adic_phase_depth()
    print("The unbounded theorem additionally requires the v11 exact norms and cyclotomic index sieve.")
