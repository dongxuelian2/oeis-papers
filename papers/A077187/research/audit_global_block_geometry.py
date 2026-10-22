#!/usr/bin/env python3
"""Small, independent algebra audits for the A077187 global-structure note.

No external packages, large-order enumeration or repunit factorization.
Checks exact digit-window conjugacy, invariant/normalized mountain,
full-layer reflection, and many-witness theorem on five primes.
"""
from math import gcd, lcm

def order10(n):
    if n == 1: return 1
    assert gcd(10,n)==1
    x=10%n; k=1
    while x!=1: x=x*10%n; k+=1
    return k

def state(p,r,e):
    """Standalone field-layer recurrence, independent of GMP certificates."""
    C=Y=0; L=1; q=10%p; t=1
    for d in range(1,e+1):
        n=9*L%p
        A=pow(10,9*d*t%r,p)
        if q==1:
            S=n; J=n*(n-1)*pow(2,-1,p)%p
        else:
            iv=pow(q-1,-1,p)
            S=(A-1)*iv%p
            J=(q-n*A+(n-1)*A*q)*iv*iv%p
        C=(A*C+(q-1)*S-J)%p
        Y=pow(A,-1,p)*(Y+L*S+J)%p
        L,q,t=q,q*10%p,t*10%r
    return C,Y

def coords(p,q,k,C,Y):
    a=q-1
    return ((a*a*C+k*a+q)%p,(a*a*Y-k*a+1)%p)

def local_checks():
    count=0
    for p in (7,13,37,73,101,239,313):
        for d in range(1,6):
            q=pow(10,d,p)
            L=pow(10,d-1,p)
            C,Y=31%p,47%p
            k=(L-1)%p
            x0,z0=coords(p,q,k,C,Y)
            for _ in range(min(12,9*10**(d-1))):
                x,z=coords(p,q,k,C,Y)
                assert x*z%p==x0*z0%p
                mountain=(q*C+Y+k+1)%p
                assert ((q-1)**2*mountain-q*x-z+2*q)%p==0
                C1=(q*C+k+1)%p
                Y1=pow(q,-1,p)*(Y+k+1)%p
                x1,z1=coords(p,q,(k+1)%p,C1,Y1)
                assert x1==q*x%p and z1==pow(q,-1,p)*z%p
                # Check the interface homothety in the nonsingular case.
                if q!=1:
                    qp=q*10%p; aa=q-1; bb=qp-1
                    lam=bb*bb*pow(aa,-2,p)%p
                    xx,zz=coords(p,qp,k,C,Y)
                    assert xx==(lam*x+k*(bb-lam*aa)+qp-lam*q)%p
                    assert zz==(lam*z-k*(bb-lam*aa)+1-lam)%p
                C,Y,k=C1,Y1,(k+1)%p
                count+=1
    print('PASS local first integrals, mountain line, and interfaces:',count)

def reflected_layer_checks():
    for L in (1,10): # first two decimal digit widths
        q=10*L; m=9*L
        S=sum(q**j for j in range(m))
        fwd=sum((L+j)*q**(m-1-j) for j in range(m))
        rev=sum((L+j)*q**j for j in range(m))
        assert fwd+rev==(L+q-1)*S
    print('PASS exact two-way reflection identity at digit widths 1 and 2')

def abundance_checks():
    for p in (37,73,101,239,313):
        r=order10(p)
        assert r>=3
        v=r
        while v%2==0:v//=2
        while v%5==0:v//=5
        T=lcm(r,order10(v))
        C1,Y1=state(p,r,T);C2,Y2=state(p,r,2*T)
        U,V=(C2-C1)%p,(Y2-Y1)%p
        assert U or V
        exceptional=[];good=0
        for n in range(r):
            slope=(pow(10,n+1,p)*U+pow(10,-n,p)*V)%p
            if slope==0:
                exceptional.append(n);continue
            # Calculate F_n(1) by literal per-integer steps in the new layer.
            C,Y=C1,Y1
            for offset in range(n):
                C=(10*C+1+offset)%p
                Y=pow(10,-1,p)*(Y+1+offset)%p
            const=(10*C+Y+1+n)%p
            j=1+(-const*pow(slope,-1,p))%p
            C,Y=(C1+(j-1)*U)%p,(Y1+(j-1)*V)%p
            for offset in range(n):
                C=(10*C+1+offset)%p
                Y=pow(10,-1,p)*(Y+1+offset)%p
            assert (10*C+Y+1+n)%p==0
            good+=1
        assert len(exceptional)<=gcd(r,2)
        assert good>=r-gcd(r,2)
        print('PASS p=',p,'order=',r,'nonzero-offsets=',good,
              'exceptional=',exceptional)
    print('PASS structural nonzero-drift offset multiplicity checks')

if __name__ == '__main__':
    local_checks()
    reflected_layer_checks()
    abundance_checks()
