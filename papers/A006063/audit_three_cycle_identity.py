#!/usr/bin/env python3
"""Pure integer audit for two-reflection, triple-cycle cube identities.

The mathematical proof uses no computation. These checks independently
validate its closed interval formulas and all 148877*T-1 translated
three-cycles for a modest T=u^3.

    53^3 + 2*(94^3) = 2*(87^3) + 79^3

For each positive integer u, the two-block reversal on
n=(94^3-53^3)*u^3 supports 53^3*u^3-1 pairwise disjoint
switchable directed three-cycles. Therefore
P(681707*u^3) >= 2^(148877*u^3-1).
"""
import argparse

A,B,X,Y=53**3,94**3,87**3,79**3
D1,D2=B-X,X-A

def verify_identity():
    assert (A,B,X,Y)==(148877,830584,658503,493039)
    assert A+2*B==2*X+Y
    assert A+B/2<=X<=B-A
    assert D1==172081 and D2==509626
    assert A<=D1 and D2-D1>=A and D2+A<=B-A


def audit(u,materialize):
    T=u**3
    n=(B-A)*T
    number=A*T-1
    assert number>0
    first=(1,A*T-1)
    second=(A*T,n)
    offsets=(0,D1*T,D2*T)
    for off in offsets:
        assert first[0]+off<=first[1]+off<=n
    for h in range(2):
        assert first[1]+offsets[h] < first[0]+offsets[h+1]
    assert first[0]+offsets[1]>=second[0]
    assert first[1]+offsets[-1]<=second[1]

    # The alternative sums are cube scalings:
    assert X*T==(87*u)**3
    assert Y*T==(79*u)**3
    assert A*T==(53*u)**3
    assert B*T==(94*u)**3

    if materialize:
        p=[0]*(n+1)
        for i in range(1,A*T):
            p[i]=A*T-i
        for i in range(A*T,n+1):
            p[i]=B*T-i
        assert sorted(p[1:])==list(range(1,n+1))
        visited=bytearray(n+1)
        for s in range(1,A*T):
            v=(s,s+D1*T,s+D2*T)
            for i in v:
                assert not visited[i]
                visited[i]=1
            sums=(v[0]+p[v[1]],v[1]+p[v[2]],v[2]+p[v[0]])
            assert sums==(X*T,Y*T,X*T)
        assert sum(visited)==3*number
    else:
        for s in (1,2,A*T//2,A*T-1):
            v=(s,s+D1*T,s+D2*T)
            def p(i):
                return (A if i<A*T else B)*T-i
            assert (v[0]+p(v[1]),v[1]+p(v[2]),v[2]+p(v[0]))==(X*T,Y*T,X*T)
    print(f"PASS u={u}, n={n}, disjoint 3-cycles={number}; "
          f"certified >=2**{number} legal permutations.")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--u",type=int,nargs="*",default=[1,2,3])
    args=parser.parse_args()
    verify_identity()
    for u in args.u:
        audit(u,materialize=(u==1))
