"""Check every exact norm and GMP gcd row, and exclude true-phase candidates."""
from pathlib import Path
from math import gcd
import json,sys
import sympy as sp
sys.set_int_max_str_digits(0)
D=Path(__file__).parent; rows=[]
for line in (D/'all_486_gmp.tsv').read_text().splitlines():
    g,a,c,G=map(int,line.split())
    assert gcd(g,729)==1
    n=int((D/f'norm_gamma_{g}.txt').read_text())
    assert n>1 and gcd(n,30)==1 and n%G==0
    w=(n-1)//6561
    assert 2**a<=w<2**(a+1)
    assert 5**c<=w<5**(c+1)
    rows.append((g,a,c,G,len(str(n))))
assert len(rows)==486
assert sorted(x[0] for x in rows)==[g for g in range(1,729) if g%3]
expected={202:328051,247:52489,266:52489,346:52489,458:52489,698:328051*839809}
nontrivial={g:G for g,a,c,G,_ in rows if G!=1}
assert nontrivial==expected,nontrivial
candidate={}
for phase,G in nontrivial.items():
    factors=sp.factorint(G)
    for p in factors:
        assert sp.isprime(p)
        order=int(sp.n_order(10,p))
        assert order%6561==0
        s=order//6561;tmp=s
        for q in (2,5):
            while tmp%q==0:tmp//=q
        assert tmp==1
        truephase=pow(s,-1,729)
        candidate[p]={'order':order,'s':s,'true_phase':truephase}
        assert truephase!=phase
phases={g:G for g,_,_,G,_ in rows}
for p,rec in candidate.items():assert phases[rec['true_phase']]==1
assert set(candidate)=={52489,328051,839809}
out={
 'theorem':'all primes with ord_p(10)=6561*2^a*5^c have a mountain-concatenation witness',
 'phases':486,
 'norm_digits_min':min(row[4] for row in rows),
 'norm_digits_max':max(row[4] for row in rows),
 'nontrivial':{str(k):str(v) for k,v in sorted(nontrivial.items())},
 'factors_and_true_phase':{str(p):v for p,v in sorted(candidate.items())},
 'status':'exact class-specific finite certificate passed; unrestricted conjecture open'
}
(D/'verified_summary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
