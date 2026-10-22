#!/usr/bin/env python3
"""A077187 fixed-v=7 infinite-family certificate.

PROVES (conditional on audit of exact code):
  ord_p(10)=7*2^a*5^c (a,c>=0) => nonzero drift => a mountain witness.

Algebra: full-period drift is quadratic in m=r/g over Q(zeta_g),
where g=7 if a=0 else 14. Compute quadratic resultants for ALL
gamma=u^{-1} mod 7, take exact cyclotomic norms and exclude primitive
order factors using modular Phi_r(10), without factoring the norms.

Dependencies: sympy. No enumeration of target primes, no large
repunit integer, and no arbitrary multiplicative-order cutoff.
"""
from math import gcd, lcm
from sympy import Poly, QQ, Rational, Symbol, cyclotomic_poly, resultant
from sympy import n_order

x = Symbol("x")
V = 7
ELL = 42  # lcm(7,ord_7(10)) = lcm(7,6)
SCALE = 40000
NORMS = {
    7: 33476324853960868807109434619064591936,
    14: 114974543608404744933251944861980458578855689,
}

def algebra(g):
    phi = Poly(cyclotomic_poly(g,x),x,domain=QQ)
    def red(a): return Poly(a,x,domain=QQ).rem(phi)
    def mul(a,b): return a.mul(b).rem(phi)
    def add(a,b): return (a+b).rem(phi)
    def scal(a,k): return a.mul_ground(Rational(k)).rem(phi)
    def neg(a):return scal(a,-1)
    def sub(a,b):return add(a,neg(b))
    def inv(a):return a.invert(phi)
    powers=[red(1)]
    for _ in range(g):powers.append(mul(powers[-1],red(x)))
    return phi,red,mul,add,scal,neg,sub,inv,powers

def drift_resultant(g,gamma,return_coordinates=False,v=7,ell=None):
    """Quadratic polynomials U(m), V(m) in Q(zeta_g)[m].

    The only input phases are gamma in (Z/7)^*, and g in {7,14}.
    All 42 full-digit-layer phase multipliers are represented in
    the fixed-degree cyclotomic algebra Q[x]/Phi_g(x).
    """
    if ell is None:
        ell=lcm(v,int(n_order(10,v)) if v>1 else 1)
    assert v>=1 and gcd(v,10)==1 and ell%g==0 and g%v==0
    assert 1<=gamma<v and gcd(gamma,v)==1
    phi,red,mul,add,scal,neg,sub,inv,zpow=algebra(g)
    coeff=[[red(0) for _ in range(3)] for _ in range(2)]
    P=red(1)
    for a in range(1,ell+1):
        exp=(g//v)*gamma*9*a*pow(10,a-1,v)
        A=zpow[exp%g]
        invA=zpow[(-exp)%g]
        Pinv=inv(P)
        alpha=mul(Pinv,sub(red(1),invA))
        beta=mul(P,sub(A,red(1)))
        PA=mul(P,A)
        if a%g==0:
            # One singular q=1 phase in this coset.
            # sum_nonzero q/(q-1)=(m-1)/2
            # sum_nonzero q/(q-1)^2=-(m^2-1)/12.
            cu=[
                add(scal(alpha,Rational(-11,12)),scal(Pinv,Rational(99,200))),
                sub(alpha,scal(Pinv,Rational(9,20))),
                scal(alpha,Rational(-1,12)),
            ]
            cv=[
                add(add(scal(beta,Rational(-2,15)),scal(PA,Rational(-9,20))),
                    scal(P,Rational(9,200))),
                add(scal(beta,Rational(1,20)),scal(PA,Rational(9,20))),
                scal(beta,Rational(1,12)),
            ]
        else:
            c=zpow[a%g]
            denominator=inv(sub(c,red(1)))
            Q=mul(c,denominator)
            R=mul(Q,denominator)
            cu=[
                red(0),
                sub(alpha,scal(mul(Pinv,Q),Rational(9,10))),
                mul(alpha,R),
            ]
            cv=[
                red(0),
                add(scal(mul(beta,Q),Rational(1,10)),
                    scal(mul(PA,Q),Rational(9,10))),
                neg(mul(beta,R)),
            ]
        for j in range(3):
            coeff[0][j]=add(coeff[0][j],cu[j])
            coeff[1][j]=add(coeff[1][j],cv[j])
        P=PA
    assert P==red(1), ("stable monodromy",g,gamma)
    U,W=coeff
    aa=sub(mul(U[2],W[0]),mul(U[0],W[2]))
    bb=sub(mul(U[2],W[1]),mul(U[1],W[2]))
    cc=sub(mul(U[1],W[0]),mul(U[0],W[1]))
    R=sub(mul(aa,aa),mul(bb,cc))  # Res_m(U,W)
    if return_coordinates:
        return R,U,W
    return R

def exact_norms():
    for g,want in NORMS.items():
        for gamma in range(1,7):
            R,U,W=drift_resultant(g,gamma,return_coordinates=True)
            # Reduction of the coefficients modulo a true-order prime
            # is legitimate: their denominators divide 200.
            assert all(200%int(z.q)==0
                       for row in (U,W) for term in row
                       for z in term.all_coeffs())
            poly=Poly(SCALE*R.as_expr(),x,domain=QQ)
            assert all(z.q==1 for z in poly.all_coeffs()),(g,gamma)
            norm=abs(int(resultant(poly.as_expr(),cyclotomic_poly(g,x),x)))
            assert norm==want,(g,gamma,norm,want)
        print("PASS 6 exact primitive phases, g =",g,
              "norm(40000*Res_m) =",want,flush=True)

def mobius(n):
    ans=1
    d=2
    while d*d<=n:
        if n%d==0:
            n//=d
            if n%d==0:return 0
            ans=-ans
        d+=1
    if n>1:ans=-ans
    return ans

def base_polynomial(a_positive,c_positive):
    n=7*(2 if a_positive else 1)*(5 if c_positive else 1)
    return [int(z) for z in reversed(Poly(cyclotomic_poly(n,x),x).all_coeffs())]

def phi_mod_norm(a,c,norm,bases):
    # Phi_{7*2^a*5^c}(X) = Phi_{7*2^[a>0]*5^[c>0]}(X^E)
    # where E=2^max(a-1,0)*5^max(c-1,0).
    E=2**max(a-1,0)*5**max(c-1,0)
    t=pow(10,E,norm)
    value=0
    for z in reversed(bases[(a>0,c>0)]):
        value=(value*t+z)%norm
    return value

def strip_index_factors(h,index):
    while True:
        q=gcd(h,index)
        if q==1:return h
        h//=q

def exclusion_sieve():
    bases={(a,c):base_polynomial(a,c)
           for a in (False,True) for c in (False,True)}
    count={7:0,14:0}
    for a_start in (0,1):
        g=7 if a_start==0 else 14
        bound=NORMS[g]
        a=a_start
        while 7*2**a<=bound:
            c=0
            while (r:=7*2**a*5**c)<=bound:
                h=gcd(bound,phi_mod_norm(a,c,bound,bases))
                residual=strip_index_factors(h,r)
                assert residual==1,(a,c,r,h,residual)
                count[g]+=1
                c+=1
            a+=1
            if a_start==0:break
    assert count=={7:53,14:4479},count
    print("PASS exact cyclotomic exclusion: all",sum(count.values()),
          "smooth-order indices below the resultant-norm bound",count)
    print("PASS unlimited-exponent v=7 theorem; unrestricted A077187 OPEN.")

if __name__=="__main__":
    exact_norms()
    exclusion_sieve()
