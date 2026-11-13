#!/usr/bin/env python3
"""Finite identity audits, not enumeration of the ineffective exceptional set."""
import math,json
from fractions import Fraction as F
from pathlib import Path

def smooth25(n):
    z=1
    for p in (2,5):
        while n%p==0:z*=p;n//=p
    return z

def run():
    identities=0;cut_samples=[]
    for d in (2,3):
        B=10**d;L=B//10;C=B-1
        W=[0]
        for n in range(1,B):W.append(W[-1]*10**len(str(n))+n)
        t=sum(len(str(n)) for n in range(1,L));G=10**t
        A=C*C*W[L-1]+L*C+1
        assert 8*A<G*B*B and t<d*L
        for m in (5*L//2,5*L,B-1):
            N=m-L+1
            for K in sorted({8,9,N//2,N-1}):
                if not 8<=K<N:continue
                k=L+K-1;J=k*C+B;M=m*C+B
                R=10**(t+d*K)*W[m]-(10**(t+d*N)-1)*W[k]
                T=(G*M-A)*B**K+J
                coeff=G*J*B**(N-K)+A-G*M
                assert C*C*R==G*J*B**N-T
                assert C*C*R+J==coeff*B**K and coeff>0
                assert 0<T<2*G*B**(K+2)
                assert B*B<10*J and J<B*B
                # Exact cancellation estimate behind the limiting direction.
                assert T*B<20*G*J*B**N
                q,e=divmod(t+d*N,2);Q=10**q
                assert 10**e*Q*Q==G*B**N
                assert F(G*B**(K+3),B**K*Q)==F(G*B**3,Q)
                identities+=1;cut_samples.append([d,m,K])
    primitive=0
    for x in range(1,101):
        for a in range(1,31):
            for Q in (10,100):
                g=math.gcd(x,a)
                assert g==math.gcd(math.gcd(x,a*Q),a)
                assert F(smooth25(g),g)**3<=1
                assert max(x//g,a*Q//g,a//g)>=Q
                primitive+=1
    margins=0
    for delta in (F(1,10),F(1,2),F(1),F(2),F(5)):
        for d in range(4,201):
            L=10**(d-1)
            product_log_upper=-delta*d*L/2+3*d+2
            norm_log_upper=5*d*L+d+1
            assert product_log_upper+delta*norm_log_upper/20<0
            margins+=1
    out=dict(exact_rotation_product_checks=identities,cut_samples=cut_samples,
             primitive_scaling_checks=primitive,rational_margin_checks=margins)
    Path(__file__).with_name('subspace-cuts-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Exact rotation/product checks:',identities)
    print('Primitive-vector scaling checks:',primitive)
    print('Rational decay-margin checks:',margins)
    print('PASS. No ineffective exceptional subspaces or square solutions are computed.')
if __name__=='__main__':run()
