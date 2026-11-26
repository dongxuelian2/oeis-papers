#!/usr/bin/env python3
"""Independent h=3 polynomial/rotation residue audit (no matrix routines)."""
from verify_h2_local_equivalence import power
from verify_three_adic_sufficient_extension import excluded_residue
from verify_a001292 import direct_prefix_mod,digits_total
q=3**8
X=[direct_prefix_mod(k,q)*pow(10,-digits_total(k),q)%q for k in range(9)]
for u in (1,2,4,5,7,8):
    d=27*u
    bad=[]
    for m in range(q):
        W=(m*(m+1)//2+d*(135-21*(m**3-m))*pow(4,-1,q))%q
        # The exact length polynomial is evaluated modulo the unit-group period;
        # negative formal lengths are legitimate modular exponents here.
        D=d*(m+1)-(10**d-1)//9
        delta=(pow(10,D,q)-1)%q
        vals=[(W-delta*x)%q for x in X]
        pred=(m%9 in (2,3,5,6) or m%27 in (9,17)
              or m%243 in (26,27,81,107,108,134,135,161,215,216)
              or m%q==(-729*(u+2))%q)
        if pred:
            assert all(excluded_residue(x,8) for x in vals),(u,m,vals)
            bad.append(m)
        else:
            assert any(power(x,8) for x in vals[:2]),(u,m,vals)
    assert len(bad)==3673
    print('PASS: u =',u,', 3673 excluded classes, all other classes have cut-0/1 witnesses')
print('PASS: 354294 normalized rotation residues')
