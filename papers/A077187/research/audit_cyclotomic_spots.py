#!/usr/bin/env python3
"""Independent cyclotomic-modulus stress test for A077187.

The proposed 'rad(G_r)|rad(990*r)' for FULL REPUNIT G_r is FALSE:
r=174 and r=258 have G_r=189, including prime 7 of order 6.
This test removes that lower-order contamination using Phi_r(10).

Standard library only. Finite spot checks, NOT an all-order proof.
Run: python3 papers/A077187/research/audit_cyclotomic_spots.py
"""
from math import gcd,lcm
from certify_orders_le500 import (
    geom, split_order, multiplicative_order_10_mod_v,
    order_class_drift, remove_allowed_factors
)

EXPECT = {
    56:1, 88:1, 104:1, 112:1, 168:1,
    174:1, 258:1, 272:17, 312:1, 336:1,
}

def mobius(n):
    ans=1
    q=2
    while q*q<=n:
        if n%q==0:
            n//=q
            if n%q==0:
                return 0
            ans=-ans
        q+=1
    if n>1:ans=-ans
    return ans

def cyclotomic_at_ten(r):
    num=den=1
    for d in range(1,r+1):
        if r%d:continue
        m=mobius(r//d)
        if m==1:num*=10**d-1
        elif m==-1:den*=10**d-1
    assert num%den==0
    result=num//den
    assert result>1 and (10**r-1)%result==0
    return result

def cyclotomic_drift(r):
    _,v=split_order(r)
    T=lcm(r,multiplicative_order_10_mod_v(v))
    modulus=cyclotomic_at_ten(r)
    inv2=(modulus+1)//2
    assert modulus%2
    C=Y=0
    L=1;q=10%modulus
    for d in range(1,2*T+1):
        h=r//gcd(r,d)
        nmod=9*pow(10,d-1,h*modulus)%(h*modulus)
        t,b=divmod(nmod,h)
        ph,Sh,Jh=geom(q,h,modulus)
        pb,Sb,Jb=geom(q,b,modulus)
        assert ph==1
        S=(t*Sh+Sb)%modulus
        J=(t*Jh+h*Sh*t*(t-1)*inv2+t*h*Sb+Jb)%modulus
        invA=pow(pb,-1,modulus)
        C=(pb*C+(q-1)*S-J)%modulus
        Y=invA*(Y+L*S+J)%modulus
        if d==T:C1,Y1=C,Y
        L,q=q,q*10%modulus
    U=(C-C1)%modulus
    V=(Y-Y1)%modulus
    return (T,modulus,gcd(modulus,U,V),U,V)

def main():
    for r, expected in EXPECT.items():
        T,phi,H,U,V=cyclotomic_drift(r)
        Tr,N,G,Ur,Vr=order_class_drift(r)
        assert T==Tr and N%phi==0
        assert (Ur%phi,Vr%phi)==(U,V),(r,'crossmod')
        assert H==expected,(r,H,expected)
        assert remove_allowed_factors(H,r)==1,(r,H)
        if r in (174,258):
            assert G==189 and G%7==0
            assert phi%7!=0 and H==1
    print("PASS 10 cyclotomic spot checks, including r=174,258 negative controls")
    print("PASS all cyclotomic gcds supported on factors of r")
    print("No all-primes proof asserted")

if __name__=="__main__":
    main()
