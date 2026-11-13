#!/usr/bin/env python3
"""Finite audits of exact ingredients, not a perfect-power exclusion search."""
import json, math
from collections import Counter
from pathlib import Path

def squarefree_part(n):
    s=1;p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e^=1
        if e:s*=p
        p=3 if p==2 else p+2
    return s*n

def valuation(n,p):
    v=0
    while n%p==0:n//=p;v+=1
    return v

def run():
    checks=0; classes=[]
    for d in (2,3):
        B=10**d;L=B//10;C=B-1
        W=[0]
        for n in range(1,B):W.append(W[-1]*10**len(str(n))+n)
        t=sum(len(str(n)) for n in range(1,L));G=10**t
        A=C*C*W[L-1]+L*C+1
        assert 8*A<G*B*B
        for m in (2*L,5*L,B-1):
            N=m-L+1
            for K in sorted({8,N//2,N-1}):
                k=L+K-1
                if k>=m:continue
                J=k*C+B;M=m*C+B
                Dk=t+d*K;Dm=t+d*N
                R=10**Dk*W[m]-(10**Dm-1)*W[k]
                T=(G*M-A)*B**K+J
                assert C*C*R==G*J*B**N-T and R>0
                assert 16*T>G*B*B*B**K and T<2*G*B*B*B**K
                assert 10*J>B*B and J<B*B
                for p in (2,5):assert valuation(C*C*R,p)==valuation(J,p)
                checks+=1
        counts=Counter(squarefree_part((L+K-1)*C+B) for K in range(8,3*L+1))
        n=C;omega=0;p=3
        while p*p<=n:
            if n%p==0:
                omega+=1
                while n%p==0:n//=p
            p+=2
        if n>1:omega+=1
        assert max(counts.values())<=2**omega
        assert len(counts)*2**omega>=3*L-7
        assert len(counts)**2>B/100
        classes.append(dict(d=d,cuts=3*L-7,squareclasses=len(counts),omega_C=omega,max_multiplicity=max(counts.values())))
    out=dict(exact_rotation_checks=checks,squareclass_checks=classes)
    Path(__file__).with_name('irrational-target-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2));print('PASS: finite audit only; unbounded assertions are proved in the note.')
if __name__=='__main__':run()
