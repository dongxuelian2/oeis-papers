#!/usr/bin/env python3
import json,math
from fractions import Fraction as F
from pathlib import Path
from verify_antiperiodic_thirteen import prefix

def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def run():
    p,q,e=1031,103,5
    assert prime(p) and prime(q) and pow(10,q,p)==1 and 10%p!=1 and (p-1)//q%e==0
    powers={pow(x,e,p) for x in range(1,p)};bad=set(range(1,p))-powers
    assert len(powers)==206 and len(bad)==824 and 10 in powers
    identities=0
    for d in range(1,q):
        B=pow(10,d,p);alpha=pow(1-B,-1,p)
        for m,w in ((0,0),(1,123),(37,800)):
            z=w
            for i in range(1,q+1):z=(B*z+m+i)%p
            assert z==(w+q*alpha)%p;identities+=1
    tails=0
    for h in range(4,151):
        b=5
        while b*5<=h+1:b*=5
        assert 5*b>=h+2
        assert F(2,3**(5*b))<=F(2,3**(h+2))
        assert p*q*3**(b+1)<=p*q*3**(h+2);tails+=1
    rows=[];cuts=0
    for d in (81,162,243):
        L=10**(d-1);R=(pow(10,d,q)-1)*pow(9,-1,q)%q
        a=(R*pow(d,-1,q)-1)%q;A=3**6
        B=pow(10,d,p);alpha=pow(1-B,-1,p)
        first=L+(a-L)%q;c=(prefix(first,p)-alpha*first)%p
        for residue in (3**5,2*3**5,3**5-1,2*3**5-1):
            # Solve the two endpoint congruences, then search only p possible lifts.
            base=residue+A*((a-residue)*pow(A,-1,q)%q);mod=A*q
            m=L+(base-L)%mod
            for _ in range(p):
                if (alpha*m+c)%p in bad:break
                m+=mod
            else:raise AssertionError('No finite-field nonpower lift')
            w=prefix(m,A*p)
            assert w%A in(3**5,2*3**5)
            assert w%p==(alpha*m+c)%p and w%p in bad
            D=d*(m+1)-(10**d-1)//9;assert D%q==0
            for k in (0,1,2,9):
                Dk=sum(len(str(i)) for i in range(1,k+1))
                wk=prefix(k,A*p)
                r=(pow(10,Dk,A*p)*w-(pow(10,D,A*p)-1)*wk)%(A*p)
                assert r%A in(3**5,2*3**5) and r%p in bad;cuts+=1
            rows.append(dict(width=d,endpoint=m,endpoint_mod103=a,prefix_mod729=w%A,prefix_mod1031=w%p))
    data=dict(e=e,p=p,q=q,nonzero_fifth_powers=len(powers),nonpowers=len(bad),scalar_q_step_checks=identities,tail_period_checks=tails,selected_prefixes=rows,selected_cut_checks=cuts)
    Path(__file__).with_name('linear-prime-exponent-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Prime/order/fifth-power data and824 nonpowers: PASS')
    print('Exact q-step checks across102 phases:',identities)
    print('Exact tail/period inequalities:',tails)
    print('Selected actual prefixes:',len(rows))
    print('Selected modular cuts:',cuts)
    print('PASS. Infinite-family statements follow from proof; no claim for every exponent.')
if __name__=='__main__':run()
