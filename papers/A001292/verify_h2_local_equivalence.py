#!/usr/bin/env python3
"""Finite certificates and independent matrix audits for the h=2 equivalence.
The infinite argument is in main.tex (Theorem thm:h2-complete).
"""
from verify_a001292 import append_block,digits_total,direct_prefix_mod
from verify_three_adic_sufficient_extension import class133,excluded_residue,cubic
from verify_boundary_valuations import valuation
CUTS=(0,1,2,3,4,19,22)
def power(n,P):
    n%=3**P
    if not n:return None
    b=valuation(n);w=n//3**b
    if b==0:return 5
    for e in (2,3,5,7):
        if b%e:continue
        if e==2 and w%3!=1:continue
        if e==3 and (P-b<2 or w%9 not in (1,8)):continue
        return e
    return None

def finite_audit():
    for u in (1,2,4,5,7,8):
        undecided=[]
        for m in range(243):
            vals=[cubic(m,k,9*u,243) for k in range(9)]
            if class133(m,u):
                assert all(excluded_residue(x,5) for x in vals)
            elif not any(power(vals[k],5) for k in range(4)):
                undecided.append(m)
        assert undecided==[0,161 if u%3==1 else 242],(u,undecided)
    X={k:direct_prefix_mod(k,81)*pow(10,-digits_total(k),81)%81 for k in CUTS}
    assert [X[k]%9 for k in (0,2,3)]==[0,3,6]
    assert [((X[k]-X[1])%81)//9 for k in (4,19,22)]==[8,2,5]
    for z in range(9):
        for c in (1,2,4,5,7,8):
            assert any(power(3**6*(z-c*t),8) for t in (0,3,6))
            assert any(power(3**6*(z-c*t),8) for t in (8,2,5))
    print('PASS: six complete residue tables, exact prefix constants, full-coset lemma')

def matrix_audit():
    P=9;mod=3**P;checks=0
    X={k:direct_prefix_mod(k,mod)*pow(10,-digits_total(k),mod)%mod for k in CUTS}
    # Representatives of every m modulo 3^8 test all boundary branches,
    # independently of the cubic formula, at several digit lengths.
    for d in (9,18,36,45):
        lower=1;prefix=0
        for width in range(1,d):
            prefix=append_block(prefix,lower,9*lower,width,mod);lower*=10
        W=append_block(prefix,lower,1,d,mod)
        D=digits_total(lower)
        A=pow(10,D,mod);B=pow(10,d,mod)
        for offset in range(3**8):
            m=lower+offset
            if offset:
                W=(B*W+m)%mod;A=A*B%mod
            ys=[(W-(A-1)*X[k])%mod for k in CUTS]
            positive=any(power(y,P) for y in ys)
            if class133(m,d//9):
                assert not positive,(d,m,ys)
                assert all(excluded_residue(y,P) for y in ys),(d,m,ys)
            else:assert positive,(d,m,ys)
            checks+=len(CUTS)
        print('PASS: matrix-initialized consecutive prefixes, d =',d)
    print('PASS:',checks,'independent bounded-cut checks')
if __name__=='__main__':finite_audit();matrix_audit()
