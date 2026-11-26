#!/usr/bin/env python3
import json,math
from fractions import Fraction as F
from pathlib import Path
from verify_cyclic_jacobi_certificate import jacobi,v3
from verify_cyclotomic_jacobi_family import prefix

def Q(j):
    x=10**(3**(j-1));return (x*x+x+1)//3

def run():
    roots=[]
    for b in (2,4,8):
        mod=3**(b+1)
        found=[m for m in range(mod) if (m*(m+1)//2)%mod==3**b]
        assert found==[3**b-1,2*3**b]
        roots.append(dict(valuation=b,modulus=mod,roots=found))
    periods=0
    for h in range(6,51):
        B=2**((h+1).bit_length()-1)
        S=sum((F(2,3**(b+1)) for b in (2**r for r in range(1,B.bit_length()))),F(0))
        assert S>=F(2,27) and 2*B>=h+2
        # Rational prefactor identity and a bound without constructing 10^(3^h).
        ratio=F(3**(B+1),999*3**(h-2))
        assert ratio==F(3)**(B-h+3)/999 and ratio<=F(81,999)
        E=math.prod(F(j+4,2*j) for j in range(5,h))
        assert E==F(h*(h+1)*(h+2)*(h+3),2**(h-5)*5*6*7*8)
        periods+=1
    countermodels=[]
    for ell in (5,7,11):
        x=10**ell;N=sum(x**i for i in range(ell));c=pow(8,-1,N)
        assert N%8==1 and jacobi(2,N)==1
        for t in range(100):
            f=(t*(t+1)//2+c)%N
            assert f==((2*t+1)**2*pow(8,-1,N))%N
            assert jacobi(f,N)>=0
        countermodels.append(dict(prime=ell,level=2,modulus=N,selected_residues=100))
    rows=[];checks=0
    for d in (27,81,243,729):
        h=v3(d)[0];B=10**d;L=B//10;mods=[Q(j) for j in range(2,h)];M=math.prod(mods)
        c=(prefix(L-1,M)-L*(L-1)//2)%M
        for b in (2,4):
            if b>h+1:continue
            for residue in (3**b-1,2*3**b):
                A=3**(b+1);first=L+(residue-L)%A;selected=[];success=0
                for i in range(50):
                    m=first+A*i
                    if any(jacobi((m*(m+1)//2+c)%n,n)==-1 for n in mods):
                        success+=1
                        if len(selected)<2:selected.append(m)
                for m in selected:
                    W=prefix(m,M);assert W==(m*(m+1)//2+c)%M
                    assert any(jacobi(W,n)==-1 for n in mods)
                    assert prefix(m,A)==3**b
                    D=d*(m+1)-(B-1)//9
                    assert pow(10,D,M)==1
                    checks+=1
                rows.append(dict(width=d,valuation=b,residue=residue,samples=50,certified=success,selected_prefixes=selected))
    data=dict(uniform_character_countermodels=countermodels,exhaustive_valuation_roots=roots,rational_period_and_error_checks=periods,endpoint_samples=rows,selected_exact_prefix_checks=checks)
    Path(__file__).with_name('jacobi-valuation-union-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Exhaustive residue root checks at valuations 2,4,8 passed.')
    print('Uniform-character countermodels: 3 moduli, 100 selected residues each.')
    print('Rational period/error checks:',periods)
    print('Sampled endpoints:',sum(x['samples'] for x in rows))
    print('Selected exact prefixes:',checks)
    print('PASS. Infinite counts and all-rotation conclusions are proved, not inferred from samples.')
if __name__=='__main__':run()
