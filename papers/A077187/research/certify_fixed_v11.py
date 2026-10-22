#!/usr/bin/env python3
"""A077187: exact algebraic certificate for ALL ord_p(10)=11*2^a*5^c.

Uses the fixed-v spectral compressor from certify_fixed_v7.py; for v=11
the two drift polynomials are always linear in m. Computes all 20 exact
linear resultants over Q(zeta_11)/Q(zeta_22), and eliminates every
possible true-order prime without factoring their norms.

SymPy dependency; no target-prime enumeration, no order cutoff.
The unrestricted A077187 conjecture remains open.
"""
from hashlib import sha256
from math import gcd
from sympy import Poly,QQ,cyclotomic_poly,resultant,Symbol
from certify_fixed_v7 import algebra,drift_resultant
x=Symbol("x")

V=11
SCALE=4000
# (g,gamma,norm) over the full set gamma in (Z/11)^*
EXPECTED=[
(11,1,15127131018612774155981272140023529449278464),
(11,2,1225495932559745042375384507489056346459136),
(11,3,42367371154715789557360879894110000000000),
(11,4,256179292089836816135434505919211662336),
(11,5,4338418806242896850673754101156864),
(11,6,4338418806242896850673754101156864),
(11,7,256179292089836816135434505919211662336),
(11,8,42367371154715789557360879894110000000000),
(11,9,1225495932559745042375384507489056346459136),
(11,10,15127131018612774155981272140023529449278464),
(22,1,285516851271280164572961034632619303414011),
(22,2,214182411409509503494503647303624144662011),
(22,3,174217810946540745462448546732625758006011),
(22,4,158087601681258150675757566429843100246011),
(22,5,166212164989478356770043568530151430262011),
(22,6,166212164989478356770043568530151430262011),
(22,7,158087601681258150675757566429843100246011),
(22,8,174217810946540745462448546732625758006011),
(22,9,214182411409509503494503647303624144662011),
(22,10,285516851271280164572961034632619303414011),
]
EXPECTED_HASH="513c1bc27609c811d838d00f6248f61f1f349c9b3e1fa6f54472e37597ab76e7"

def exact_norms():
    norms={}
    for g,gamma,want in EXPECTED:
        _,red,mul,add,scal,neg,sub,inv,zpow=algebra(g)
        _R,U,W=drift_resultant(g,gamma,return_coordinates=True,v=V,ell=22)
        assert U[2].is_zero and W[2].is_zero,(g,gamma,"degree>1")
        # Linear resultant, NOT padded-quadratic resultant (which
        # would vanish identically when both leading coefficients are 0).
        linear=sub(mul(U[1],W[0]),mul(U[0],W[1]))
        poly=Poly(SCALE*linear.as_expr(),x,domain=QQ)
        assert all(z.q==1 for z in poly.all_coeffs()),(g,gamma)
        norm=abs(int(resultant(poly.as_expr(),cyclotomic_poly(g,x),x)))
        assert norm==want,(g,gamma,norm,want)
        assert norm>0
        assert all(200%int(z.q)==0
                   for row in (U,W) for term in row
                   for z in term.all_coeffs())
        norms[g,gamma]=norm
    blob="".join(f"{g},{gamma},{N}\n" for g,gamma,N in EXPECTED).encode()
    assert sha256(blob).hexdigest()==EXPECTED_HASH
    print("PASS 20 fixed-degree linear resultant norms (two degenerate quadratic terms)")
    print("SHA256",EXPECTED_HASH)
    return norms

def base_poly(a_positive,c_positive):
    index=11*(2 if a_positive else 1)*(5 if c_positive else 1)
    return [int(z) for z in Poly(cyclotomic_poly(index,x),x).all_coeffs()]

def phi_at_ten_mod(a,c,N,bases):
    e=2**max(0,a-1)*5**max(0,c-1)
    y=pow(10,e,N)
    value=0
    for z in bases[(a>0,c>0)]:
        value=(value*y+z)%N
    return value

def strip_divisors_of_index(n,r):
    while True:
        q=gcd(n,r)
        if q==1:return n
        n//=q

def eliminate(norms):
    bases={(a,c):base_poly(a,c)
           for a in (False,True) for c in (False,True)}
    maximum=max(norms.values())
    count=0
    a=0
    while 11*2**a<=maximum:
        c=0
        while 11*2**a*5**c<=maximum:
            r=11*2**a*5**c
            u=2**a*5**c
            gamma=pow(u%11,-1,11)
            g=11 if a==0 else 22
            N=norms[g,gamma]
            if r<=N:
                h=gcd(N,phi_at_ten_mod(a,c,N,bases))
                residual=strip_divisors_of_index(h,r)
                assert residual==1,(a,c,r,g,gamma,h,residual)
                count+=1
            c+=1
        a+=1
    assert count==3943,count
    print("PASS all",count,"admissible phase-aware smooth indices: zero primitive residue")
    print("PASS ALL ord_p(10)=11*2^a*5^c have nonzero drift")
    print("Unrestricted A077187 remains OPEN.")

if __name__=="__main__":
    eliminate(exact_norms())
