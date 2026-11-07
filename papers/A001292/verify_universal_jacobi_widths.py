#!/usr/bin/env python3
"""Finite audits; no inference of infinite coverage from sample frequencies."""
import json,math
from pathlib import Path
from fractions import Fraction
from verify_cyclic_jacobi_certificate import jacobi,v3
from verify_cyclotomic_jacobi_family import prefix

def Q(j):
    x=10**(3**(j-1));return (x*x+x+1)//3

def run():
    assert [m for m in range(27) if m*(m+1)//2%27==9]==[8,18]
    phases=[]
    for a in range(37):
        delta=(1-88*a)%37
        signs=[jacobi((b*(b+1)//2+11*a)%37,37) for b in range(37)]
        expected=0 if delta==0 else (18 if jacobi(delta,37)==1 else 19)
        assert signs.count(1)==expected
        assert (delta==0)==(a==8)
        phases.append(dict(width_mod37=a,discriminant=delta,positive=expected,zero=signs.count(0),negative=signs.count(-1)))
    rational_checks=0
    for h in range(5,101):
        for J in range(5,h+1):
            lhs=math.prod(Fraction(j+4,2*j) for j in range(J,h+1))
            rhs=Fraction(math.prod(range(h+1,h+5)),2**(h-J+1)*math.prod(range(J,J+4)))
            assert lhs==rhs;rational_checks+=1
    rows=[];direct=0
    for d in (9,18,27,36,45,81,108,333):
        h=v3(d)[0];q=3**h;B=10**d;L=B//10;mods=[Q(j) for j in range(2,h+1)];M=math.prod(mods)
        assert 27*M==(10**q-1)//(37*3**(h-1))
        c=(prefix(L-1,M)-L*(L-1)//2)%M
        for residue in (8,18):
            first=L+(residue-L)%27;good=[];success=0
            for i in range(100):
                m=first+27*i
                if any(jacobi((m*(m+1)//2+c)%n,n)==-1 for n in mods):
                    success+=1
                    if len(good)<3:good.append(m)
            for m in good:
                W=prefix(m,M);assert W==(m*(m+1)//2+c)%M
                assert any(jacobi(W,n)==-1 for n in mods)
                assert prefix(m,27)==9
                assert prefix(m,37)==(m*(m+1)//2+11*d)%37
                D=d*(m+1)-(B-1)//9
                assert D%q==0 and pow(10,D,M)==1
                direct+=1
            rows.append(dict(width=d,residue_mod27=residue,sample_size=100,certified_in_sample=success,selected_exact_prefixes=good))
    data=dict(mod27_roots=[8,18],complete_mod37_phase_counts=phases,rational_product_checks=rational_checks,samples=rows,selected_exact_prefix_checks=direct)
    Path(__file__).with_name('universal-jacobi-widths-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Complete mod27 root and 37*37 character checks passed.')
    print('Exact rational product identities:',rational_checks)
    print('Sampled endpoints:',sum(r['sample_size'] for r in rows))
    print('Selected exact prefixes:',direct)
    print('PASS. Samples do not establish the infinite bounds or individually test all rotations.')
if __name__=='__main__':run()
