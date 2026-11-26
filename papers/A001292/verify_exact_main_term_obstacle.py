#!/usr/bin/env python3
"""Finite exact audits of a method limitation, not a conjecture proof."""
import math,json
from pathlib import Path

def valuation(n,p):
    assert n
    v=0
    while n%p==0:n//=p;v+=1
    return v,n

def run():
    records=[];tested=0;mod=2**64
    for d in (2,3,4,5):
        B=10**d;L=B//10;C=B-1
        ws=[0];ds=[0]
        for m in range(1,B):
            length=len(str(m));ws.append((ws[-1]*pow(10,length,mod)+m)%mod);ds.append(ds[-1]+length)
        G=pow(10,ds[L-1],mod);A=(C*C*ws[L-1]+L*C+1)%mod
        for k in range(L+7,B-1):
            J=k*C+B;K=k-L+1
            assert C*C*ws[k]%mod==(A*pow(B,K,mod)-J)%mod
            tested+=1
            choices=[]
            t=math.isqrt(J)
            if t*t==J:choices.append((0,t))
            if J%10==0:
                t=math.isqrt(J//10)
                if 10*t*t==J:choices.append((1,t))
            for e,t in choices:
                m=k+1
                if (ds[L-1]+d*(m-L+1)+e)%2:m+=1
                if m>=B or (ds[L-1]+d*(m-L+1)+e)%2:continue
                R=(pow(10,ds[k],mod)*ws[m]-(pow(10,ds[m],mod)-1)*ws[k])%mod
                v,u=valuation(R,2)
                assert v<61 and (v%2 or u%8!=1)
                assert R%2**(v+3)==ws[k]%2**(v+3)
                N=m-L+1
                rhs=(G*J*pow(B,N,mod)+(A-G*(m*C+B))*pow(B,K,mod)-J)%mod
                assert C*C*R%mod==rhs
                records.append(dict(width=d,cut=k,endpoint=m,J=J,squarefree_part=10**e,root=t,v2=v,unit_mod8=u%8))
    data=dict(exact_prefix_identity_checks=tested,leading_square_cases=records)
    Path(__file__).with_name('exact-main-term-obstacle-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Exact prefix identity checks:',tested)
    print('Rational-square main term cases checked:',len(records))
    print('PASS. Each selected rotation has a 2-adic obstruction; this is a method limitation only.')

if __name__=='__main__':run()
