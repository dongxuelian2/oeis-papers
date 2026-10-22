#!/usr/bin/env python3
"""A077187 exact reference checks for the scalar-GCD conjecture.

FINITE DATA ONLY. Verifies all 179 formal orders 2 <= r <= 180, by the
existing full-2T geometric-sum evaluator (not the single-period GMP
shortcut). Also tests the PROVED order-inflation identity using exact
composite-ring states reduced independently modulo their true primes.

No external packages. Does not claim global scalar-gcd identity.
Run: python3 research/audit_scalar_gcd_and_inflation.py
"""
from math import gcd
from certify_orders_le500 import order_class_drift

# actual order, formal order, actual prime
INFLATION = [
    (6,174,7), (6,258,7), (6,696,7),
    (16,272,17), (2,88,11), (4,808,101),
    (3,888,37), (6,936,13)
]

def exact_order(a,p):
    x = a%p
    k = 1
    while x != 1:
        k += 1
        x = x*a%p
        assert k <= p
    return k

def main():
    cached={}
    for r in range(2,181):
        T,N,G,U,V=order_class_drift(r)
        cached[r]=(T,N,G,U,V)
        expected=gcd(N,9*T)
        assert gcd(N,U+V)==expected,(r,T,'scalar')
        assert gcd(N,10*U+V)==expected,(r,T,'single-offset slope')
        assert G==expected,(r,T,'vector')
    print('PASS vector/scalar/single-offset-slope gcd equality for all 179 orders 2<=r<=180')

    for s,r,p in INFLATION:
        assert exact_order(10,p)==s,(s,r,p,'wrong true order')
        assert r%s==0
        Ts,Ns,Gs,Us,Vs=cached.get(s) or order_class_drift(s)
        Tr,Nr,Gr,Ur,Vr=cached.get(r) or order_class_drift(r)
        assert Tr%Ts==0,(r,s,Tr,Ts)
        m=Tr//Ts
        assert (Ur%p,Vr%p)==((m*Us)%p,(m*Vs)%p),(r,s,p,'inflation')
        assert m%p==0,(r,s,p,m)
        assert (Ur%p,Vr%p)==(0,0),(r,s,p,'contamination')
        print('PASS order inflation',{'r':r,'s':s,'p':p,'ratio':m})
    print('PASS all 8 independent modular order-inflation examples')
    print('UNPROVED: scalar gcd identity for all r, A077187 for all primes.')

if __name__=='__main__':
    main()
