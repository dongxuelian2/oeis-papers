#!/usr/bin/env python3
"""A077187: independent finite-field audit of the Möbius phase involution.

Standard library only. Compares exact successful-phase counts from
polynomial-GCD degrees against direct enumeration for 360 synthetic
situations plus genuine decimal-concatenation drift vectors.
Includes common-root, degeneracy, anti-diagonal and zero-drift cases.
This is an audit of universal identities, NOT an all-primes proof.
"""
from math import comb, gcd, lcm

def norm_poly(a):
    a = list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def minus(a,b,p):
    return norm_poly([((a[i] if i<len(a) else 0)
                       -(b[i] if i<len(b) else 0))%p
                      for i in range(max(len(a),len(b)))])

def linpow(a,b,n,p):
    return norm_poly([comb(n,i)*pow(a,i,p)*pow(b,n-i,p)%p
                      for i in range(n+1)])

def poly_rem(a,b,p):
    a,b=norm_poly(a),norm_poly(b)
    assert b!=[0]
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b) and a!=[0]:
        off=len(a)-len(b); scale=a[-1]*inv%p
        for i in range(len(b)):
            a[off+i]=(a[off+i]-scale*b[i])%p
        a=norm_poly(a)
    return a

def poly_gcd(a,b,p):
    a,b=norm_poly(a),norm_poly(b)
    while b!=[0]:
        a,b=b,poly_rem(a,b,p)
    return a

def gcd_degree(p,*polys):
    g=polys[0]
    for poly in polys[1:]:
        g=poly_gcd(g,poly,p)
    return len(g)-1

def order10(p):
    assert p not in (2,5)
    x=10%p;r=1
    while x!=1:
        x=x*10%p
        r+=1
    return r

def phase_counts(p,r,A,B,H,U,V):
    """Returns (direct_count, projective_count) over order-r group."""
    alpha,beta=10*U%p,V%p
    mu=[pow(10,n,p) for n in range(r)]
    assert len(set(mu))==r
    a=lambda z:(A*z*z+H*z+B)%p
    b=lambda z:(alpha*z*z+beta)%p
    universal=any(a(z)==0 and b(z)==0 for z in mu)
    if universal:
        direct=p
    else:
        direct=len({(-a(z)*pow(b(z),-1,p))%p
                    for z in mu if b(z)!=0})
    if U%p==0 and V%p==0:
        expected=p if universal else 0
        assert direct==expected
        return direct, expected
    if universal:
        return direct,p
    P=[p-1]+[0]*(r-1)+[1]
    bp=[beta,0,alpha]
    n0=gcd_degree(p,P,bp)
    m=r-n0
    D=(A*beta-B*alpha)%p
    lam=(D*D+H*H*alpha*beta)%p
    if lam==0:
        predicted=m
    else:
        F=minus(linpow(-D%p,-H*beta%p,r,p),
                linpow(-H*alpha%p,D,r,p),p)
        J=[H*beta%p,2*D%p,-H*alpha%p]
        e=gcd_degree(p,P,F)-gcd_degree(p,P,F,bp)
        f=gcd_degree(p,P,J)-gcd_degree(p,P,J,bp)
        assert (e-f)%2==0 and e>=f,(p,r,e,f)
        predicted=m-(e-f)//2
        assert (m+1)//2 <=predicted<=m
        # Independently test the involution equation on eligible roots.
        for z in mu:
            if b(z)==0:continue
            den=(D-H*alpha*z)%p
            if den==0:
                # A pole, hence no finite partner.
                assert (-D*z-H*beta)%p!=0
                continue
            w=-(D*z+H*beta)*pow(den,-1,p)%p
            if w in mu and w!=z and b(w)!=0:
                assert a(z)*b(w)%p==a(w)*b(z)%p
                # The deck map has order two.
                den2=(D-H*alpha*w)%p
                assert den2!=0
                zz=-(D*w+H*beta)*pow(den2,-1,p)%p
                assert zz==z
    assert direct==predicted,(p,r,A,B,H,U,V,direct,predicted)
    return direct,predicted

def full_layer(p,r,d,C,Y):
    q,L=pow(10,d,p),pow(10,d-1,p)
    n=9*L%p
    phase=9*d*pow(10,d-1,r)%r
    aa=pow(10,phase,p)
    if q==1:
        S=n;J=n*(n-1)*pow(2,-1,p)%p
    else:
        iv=pow(q-1,-1,p)
        S=(aa-1)*iv%p
        J=(q-n*aa+(n-1)*aa*q)*iv*iv%p
    return ((aa*C+(q-1)*S-J)%p,
            (Y+L*S+J)*pow(aa,-1,p)%p)

def decimal_drift(p):
    r=order10(p);v=r
    while v%2==0:v//=2
    while v%5==0:v//=5
    t=v//gcd(v,9)
    T=lcm(r,order10(t) if t>1 else 1)
    C=Y=0; midpoint=None
    for d in range(1,2*T+1):
        C,Y=full_layer(p,r,d,C,Y)
        if d==T:midpoint=(C,Y)
    U,V=(C-midpoint[0])%p,(Y-midpoint[1])%p
    q=10%p;inv=pow(q-1,-1,p)
    A=q*(midpoint[0]+inv+inv*inv)%p
    B=(midpoint[1]-inv+q*inv*inv)%p
    H=-2*q*inv*inv%p
    return r,T,A,B,H,U,V

def audit():
    primes=(7,13,17,23,29,37,43,73,101,137,211,313)
    n=0
    for p in primes:
        r=order10(p)
        H=-20*pow(81,-1,p)%p
        for A,B in ((19%p,29%p),(0,0),(1,0),(0,1),(5,8)):
            for U,V in ((0,0),(1,0),(0,1),(1,p-1),(1,1),(3,4)):
                phase_counts(p,r,A,B,H,U,V)
                n+=1
    assert n==360
    print("PASS 360 synthetic Möbius phase-count and GCD identities")
    for p in primes:
        r,T,A,B,H,U,V=decimal_drift(p)
        a,b=phase_counts(p,r,A,B,H,U,V)
        assert a==b
        print(f"PASS genuine decimal drift p={p}, r={r}, T={T}, phases={a}")
    print("PASS 12 genuine decimal concatenation recurrences")
    print("General zero-drift mountain existence remains OPEN.")

if __name__=="__main__":
    audit()
