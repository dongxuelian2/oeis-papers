"""Exact finite-defect transfer, independent of the pT forward iteration."""
from math import lcm
import sympy as sp
from independent_digit_layers import order,state_at_e

def parameters(p):
    r=order(10,p);f=sp.factorint(r)
    a=f.get(2,0);c=f.get(5,0)
    u=2**a*5**c;v=r//u
    T=lcm(r,order(10,v) if v>1 else 1)
    return r,u,v,T,max(a,c)+1

def layer_map(p,r,d,exponent_d=None):
    if exponent_d is None:exponent_d=d
    L=pow(10,d-1,p);q=pow(10,d,p)
    N=9*L%p;B=(10*L-1)%p
    a=pow(10,(9*exponent_d*pow(10,exponent_d-1,r))%r,p)
    if q==1:
        S=N;J=N*(N-1)*pow(2,-1,p)%p
    else:
        S=(a-1)*pow(q-1,-1,p)%p
        J=(q-N*a+(N-1)*a*q)*pow((q-1)**2,-1,p)%p
    return a,(B*S-J)%p,(L*S+J)*pow(a,-1,p)%p

def transfer_state(p):
    r,u,v,T,E=parameters(p)
    C=Y=0
    for d in range(1,E):
        a,c,y=layer_map(p,r,d)
        C=(a*C+c)%p;Y=(pow(a,-1,p)*Y+y)%p
    early=(C,Y)
    for d in range(E-1,0,-1):
        a,c,y=layer_map(p,r,d,T+d)
        C=((C-c)*pow(a,-1,p))%p;Y=(a*(Y-y))%p
    return (C,Y),early,(r,u,v,T,E)

if __name__=="__main__":
    for p in (7,11,13,17,29,37,43,53,73,97,109,113,137,151,193,257,281):
        (C,Y),early,(r,u,v,T,E)=transfer_state(p)
        assert (C,Y)==state_at_e(p,p*T,r),p
        print("PASS",p,r,u,v,T,E,(C,Y))
