#!/usr/bin/env python3
"""Short exact audit of the universal twisted-reflection identity.

No searches, large-order scans, or third-party libraries.
Compares the one-period reflected-block decomposition with the
independently accumulated two-endpoint drift for five formal orders.
"""
from math import gcd, lcm
from certify_orders_le500 import geom, order_class_drift, split_order, multiplicative_order_10_mod_v

def check(r):
    T,N,G,U,V=order_class_drift(r)
    P=1
    upward=downward=base=error1=error10=0
    for d in range(T+1,2*T+1):
        q=pow(10,d,N)
        L=pow(10,d-1,N)
        h=r//gcd(r,d)
        nmod=9*pow(10,d-1,h*N)%(h*N)
        t,b=divmod(nmod,h)
        ph,Sh,Jh=geom(q,h,N)
        A,Sb,Jb=geom(q,b,N)
        assert ph==1
        S=(t*Sh+Sb)%N
        J=(t*Jh+h*Sh*(t*(t-1)//2)+t*h*Sb+Jb)%N
        B=((q-1)*S-J)%N
        R=(L*S+J)%N
        assert (B+R-(L+q-1)*S)%N==0
        theta=P*P*A%N
        invtheta=pow(theta,-1,N)
        upward=(upward+P*invtheta*B)%N
        downward=(downward+P*R)%N
        base=(base+P*(L+q-1)*S)%N
        error1=(error1+P*(invtheta-1)*B)%N
        error10=(error10+P*(10*invtheta-1)*B)%N
        P=P*A%N
    assert P==1
    assert (upward,downward)==(U,V),(r,'word-vectors')
    assert (base+error1-U-V)%N==0,(r,'lambda=1')
    assert (base+error10-10*U-V)%N==0,(r,'lambda=10')
    return (base,error1,error10)

def digit_profile(s,r):
    # s is a literal decimal word; digits indexed from right to left.
    coeffs=[0]*r
    for i,c in enumerate(reversed(s)):
        coeffs[i%r]+=int(c)
    return sum(c*10**i for i,c in enumerate(coeffs))%(10**r-1)

if __name__=='__main__':
    for r in (4,7,11,13,17):
        baseline,mismatch1,mismatch10=check(r)
        print('PASS twisted scalar lambda=1,10 and both block words for r=',r,
              'mismatch1=',mismatch1)
    for r in (2,3,7):
        s='1234567890123456789029384756'
        assert digit_profile(s,r)==int(s)%(10**r-1)
    print('PASS group-ring cyclic digit profile identity (three formal orders)')
