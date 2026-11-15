#!/usr/bin/env python3
"""Finite audits of an infinite theorem; no extrapolation from samples."""
import json,math
from fractions import Fraction as F
from pathlib import Path
from verify_a001292 import append_block
from verify_cyclic_jacobi_certificate import jacobi

def prefix(m,mod):
    z=0;lo=1;d=1
    while lo<=m:
        z=append_block(z,lo,min(m,10*lo-1)-lo+1,d,mod)
        lo*=10;d+=1
    return z

def prime_factors(n):
    ps=[];p=2
    while p*p<=n:
        if n%p==0:
            ps.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:ps.append(n)
    return ps

def run():
    lemma=[]
    for Q in (11,19,43,91,187,539,1331):
        assert Q%8==3
        ps=prime_factors(Q);S=sum((F(1,p) for p in ps),F(0));bound=F(1,2)-F(3,2*min(ps))-2*S
        for c in sorted({0,1,2,13%Q,100%Q,pow(8,-1,Q)}):
            negative=sum(jacobi((t*(t+1)//2+c)%Q,Q)==-1 for t in range(Q))
            assert F(negative,Q)>=bound
            lemma.append(dict(modulus=Q,constant=c,negative_classes=negative,lower_fraction=str(bound)))
    widths=[];checks=0
    for h in (2,3,4):
        d=3**h;B=10**d;L=B//10;x=10**(d//3);Q=(x*x+x+1)//3
        assert (x*x+x+1)%3==0 and math.gcd(Q,999)==1 and Q%8==3
        assert jacobi(2,Q)==-1 and jacobi(10,Q)==1
        c=(prefix(L-1,Q)-L*(L-1)//2)%Q
        start=666+max(0,(L-666+998)//999)*999
        samples=[];row=dict(h=h,width=d,modulus=Q,constant=c)
        if h==2:
            mask=[jacobi((m*(m+1)//2+c)%Q,Q)==-1 for m in range(Q)]
            neg=sum(mask);actual=0;candidate_count=0
            for m in range(start,B,999):
                candidate_count+=1
                if mask[m%Q]:
                    actual+=1
                    if len(samples)<10:samples.append(m)
            row.update(negative_residue_classes=neg,endpoint_candidates=candidate_count,certified_endpoints=actual)
        else:
            for j in range(1000):
                m=start+999*j
                if jacobi((m*(m+1)//2+c)%Q,Q)==-1:samples.append(m)
                if len(samples)==10:break
            assert len(samples)==10
        for m in samples:
            assert L<=m<B and m%999==666
            D=d*(m+1)-(B-1)//9
            assert D%d==0 and pow(10,D,Q)==1
            w=prefix(m,Q);assert w==(m*(m+1)//2+c)%Q and jacobi(w,Q)==-1
            assert prefix(m,27)==9
            w37=prefix(m,37);assert w37==(33*pow(3,h-1,37))%37 and pow(w37,18,37)==1
            checks+=1
        row['selected_endpoint_samples']=samples;widths.append(row)
    out=dict(character_lemma_cases=lemma,width_checks=widths,selected_exact_prefix_checks=checks)
    Path(__file__).with_name('cyclotomic-jacobi-family-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Exact quadratic-character lemma cases:',len(lemma))
    print('h=2 full finite scan:',{k:v for k,v in widths[0].items() if k not in ('constant','selected_endpoint_samples')})
    print('Selected exact prefix checks across widths 9,27,81:',checks)
    print('PASS. Infinite lower bound follows from the proof, not the finite samples.')

if __name__=='__main__':run()
