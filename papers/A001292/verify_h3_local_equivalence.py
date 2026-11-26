#!/usr/bin/env python3
"""Exact finite audits for the explicit h=3 local equivalence.
Infinite proofs are in main.tex, Lemma strong-prefix and Theorem h3-complete.
"""
from fractions import Fraction as F
from verify_a001292 import append_block,digits_total,direct_prefix_mod
from verify_boundary_valuations import valuation,rational_mod
from verify_h2_local_equivalence import power
from verify_three_adic_sufficient_extension import excluded_residue
EXTRA={26,27,81,107,108,134,135,161,215,216}
def low(m):return m%9 in (2,3,5,6) or m%27 in (9,17) or m%243 in EXTRA
def excluded(m,u):return low(m) or (m+729*(u+2))%6561==0
def G(m,d,P=8):
    mod=3**P
    return (m*(m+1)//2+d*pow(4,-1,mod)*(135-21*(m**3-m)))%mod

def finite_audit():
    ell=sum((F((-1)**(j+1)*9**j,j) for j in range(1,9)),F(0))
    c0=F(1,200);c1=F(169,3000)*ell+ell**2/1800
    c2=F(671,80000)*ell**2+F(353,54000)*ell**3+ell**4/32400
    assert [rational_mod(x,27) for x in (c0,c1,c2/3)]==[5,12,9]
    assert rational_mod(c0+c1/2+c2/6,27)==2
    assert sum(low(m) for m in range(243))==136
    for m in range(243):
        n=m*(m+1)//2%243
        if n:assert low(m)==excluded_residue(n,5)
        else:assert not low(m)
    for u in range(27):
        if not u%3:continue
        assert sum(excluded(m,u) for m in range(6561))==3673
        for m in range(6561):
            w=G(m,27*u)
            if w%243:
                actual=excluded_residue(w,8)
            else:
                actual=(m%243==0 and w%729==0 and
                        w//729%9==(3*u-1)%9)
            assert actual==excluded(m,u),(m,u,w)
    print('PASS: strengthened boundary constants, 136 low classes, 18 full 3673-class sets')

def matrix_audit():
    # Check strengthened congruence beyond h=3 as well.
    for d in (9,18,27,36,45,54,81,108,135,189,216):
        h=valuation(d);P=h+5;mod=3**P
        lower=1;prefix=0
        for width in range(1,d):
            prefix=append_block(prefix,lower,9*lower,width,mod);lower*=10
        W=append_block(prefix,lower,1,d,mod);B=pow(10,d,mod)
        for offset in range(mod):
            m=lower+offset
            if offset:W=(W*B+m)%mod
            assert W==G(m,d,P),(d,m,W,G(m,d,P))
        print('PASS: strengthened prefix polynomial, d =',d)
    P=10;mod=3**P;count=0
    cuts=(0,1,2,3,4,19,22,99,100,243,1000)
    X={k:direct_prefix_mod(k,mod)*pow(10,-digits_total(k),mod)%mod for k in cuts}
    for d in (27,54,108,135,189,216):
        lower=1;prefix=0
        for width in range(1,d):
            prefix=append_block(prefix,lower,9*lower,width,mod);lower*=10
        W=append_block(prefix,lower,1,d,mod);B=pow(10,d,mod)
        A=pow(10,digits_total(lower),mod)
        for offset in range(6561):
            m=lower+offset
            if offset:W=(W*B+m)%mod;A=A*B%mod
            ys=[(W-(A-1)*X[k])%mod for k in cuts]
            if excluded(m,d//27):
                assert all(excluded_residue(y,P) for y in ys),(d,m,ys)
            else:assert any(power(y,P) for y in ys[:2]),(d,m,ys[:2])
            count+=len(cuts)
        print('PASS: exact h=3 classification, d =',d)
    print('PASS:',count,'independent rotation checks, including first-two-cut witnesses')
if __name__=='__main__':finite_audit();matrix_audit()
