#!/usr/bin/env python3
"""Exact witness for A077187 when arbitrary-order drift is nonzero.
Does NOT prove the drift is nonzero for every prime.
"""
from math import lcm
from sympy import n_order, factorint, isprime

def witness(p):
    if p in (2,5): return None
    if p==3: return "3"
    if p==11: return "2"
    assert p>=7 and isprime(p)
    r=int(n_order(10,p)); f=factorint(r)
    u=2**f.get(2,0)*5**f.get(5,0); v=r//u
    T=lcm(r,int(n_order(10,v)) if v>1 else 1)
    C=Y=0; L=1; q=10%p; lr=1
    for d in range(1,2*T+1):
        N=9*L%p; B=(10*L-1)%p
        A=pow(10,9*d*lr%r,p)
        if q==1:
            G=N; J=N*(N-1)*pow(2,-1,p)%p
        else:
            inv=pow(q-1,-1,p)
            G=(A-1)*inv%p
            J=(q-N*A+(N-1)*A*q)*inv*inv%p
        C=(A*C+B*G-J)%p
        Y=(pow(A,-1,p)*(Y+L*G+J))%p
        if d==T: C1,Y1=C,Y
        L=q; q=q*10%p; lr=lr*10%r
    U=(C-C1)%p; V=(Y-Y1)%p
    if U==V==0:
        return {"p":p,"T":T,"drift":(U,V),
                "status":"ZERO_DRIFT: use quadratic window decision"}
    s0=(10*U+V)%p; s1=(1000*U+V)%p
    if s0:
        j=1+(-(10*C1+Y1+1)*pow(s0,-1,p))%p
        offset=0
        assert (10*(C1+(j-1)*U)+Y1+(j-1)*V+1)%p==0
    else:
        j=1+(-(1000*C1+Y1+121)*pow(s1,-1,p))%p
        offset=1
        assert (1000*(C1+(j-1)*U)+Y1+(j-1)*V+121)%p==0
    return {"p":p,"r":r,"T":T,"drift":(U,V),
            "k":f"10^{j*T}"+("+1" if offset else "")}

if __name__=="__main__":
    from sys import argv
    for p in map(int,argv[1:] or ["73","113","233","313","1489"]):
        print(witness(p))
