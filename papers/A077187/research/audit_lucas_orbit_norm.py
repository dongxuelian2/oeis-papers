#!/usr/bin/env python3
"""Independent audit of Lucas cyclic norms for decimal mountain windows.

No imports from research code and no SymPy. Compares O(log h) matrix
transfer norms to direct root enumeration in 49 small field windows.
This proves no universal nonzero-drift or zero-drift-witness claim.
"""
from math import gcd,lcm

def ord10(p):
    n,x=1,10%p
    while x!=1:
        x=x*10%p
        n+=1
    return n

def full_layer(p,r,d,C,Y):
    q,L=pow(10,d,p),pow(10,d-1,p)
    n=9*L%p
    a=pow(10,9*d*pow(10,d-1,r)%r,p)
    if q==1:
        S,J=n,n*(n-1)*pow(2,-1,p)%p
    else:
        iv=pow(q-1,-1,p)
        S=(a-1)*iv%p
        J=(q-n*a+(n-1)*a*q)*iv*iv%p
    return (a*C+(q-1)*S-J)%p,(Y+L*S+J)*pow(a,-1,p)%p

def lucas_norm(A,H,B,n,p):
    """Res(z^n-1, A*z^2+H*z+B), using O(log n) 2x2 powering."""
    def mul(X,Y):
        return ((X[0]*Y[0]+X[1]*Y[2])%p,
                (X[0]*Y[1]+X[1]*Y[3])%p,
                (X[2]*Y[0]+X[3]*Y[2])%p,
                (X[2]*Y[1]+X[3]*Y[3])%p)
    result=(1,0,0,1)
    power=(-H%p,-A*B%p,1,0)
    e=n
    while e:
        if e&1:result=mul(result,power)
        power=mul(power,power)
        e>>=1
    return (pow(A,n,p)+pow(B,n,p)-result[0]-result[3])%p

def window_norm(p,r,d,C,Y):
    q,L=pow(10,d,p),pow(10,d-1,p)
    if q==1:
        K=(C+Y+L-L*L)%p
        N=2*K*(1-pow(-K%p,(p-1)//2,p))%p
        brute=1
        for n in range(p):
            brute=brute*((L+n)**2+K)%p
        assert N==brute,(p,d,'singular')
        return N,p
    iv=pow(q-1,-1,p)
    A=q*(C+L*iv+iv*iv)%p
    B=(Y-L*iv+q*iv*iv)%p
    H=-2*q*iv*iv%p
    h=r//gcd(r,d)
    N=lucas_norm(A,H,B,h,p)
    brute=1
    for n in range(h):
        z=pow(q,n,p)
        brute=brute*(A*z*z+H*z+B)%p
    assert N==brute,(p,d,'resultant')
    for s in (0,1,3):
        As=A*pow(q,s,p)%p
        Bs=B*pow(q,-s,p)%p
        assert lucas_norm(As,H,Bs,h,p)==N,(p,d,s,'gauge')
    return N,h

def literal_zeros(p,r,d,C,Y,period):
    q,L=pow(10,d,p),pow(10,d-1,p)
    nzeros=0
    for n in range(period):
        if (q*C+Y+L+n)%p==0:nzeros+=1
        k=(L+n)%p
        C=(q*C+k)%p
        Y=(Y+k)*pow(q,-1,p)%p
    return nzeros

def audit():
    checked=0
    for p in (7,17,23,29,37,43,73,101,137,211,313,617):
        r=ord10(p)
        v=r
        for factor in (2,5):
            while v%factor==0:v//=factor
        t=v//gcd(v,9)
        T=lcm(r,ord10(t) if t>1 else 1)
        C=Y=0
        for d in range(1,T+1):C,Y=full_layer(p,r,d,C,Y)
        picks=set([T+1,T+2,T+3,2*T,T+r])
        for d in range(T+1,2*T+1):
            if d in picks:
                norm,period=window_norm(p,r,d,C,Y)
                count=literal_zeros(p,r,d,C,Y,period)
                assert (norm==0)==(count>0),(p,d,'zero-criterion',norm,count)
                assert count<=2,(p,d,'too-many-roots',count)
                checked+=1
            C,Y=full_layer(p,r,d,C,Y)
    assert checked==49,checked
    print('PASS 49 independent field windows with exact Lucas determinant norms')
    print('PASS subgroup-root equivalence, singular products, phase gauge invariance')
    print('No claim of a universal zero-drift witness.')

if __name__=='__main__':audit()
