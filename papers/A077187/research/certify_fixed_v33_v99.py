#!/usr/bin/env python3
"""Prove the 33*2^a*5^c and 99*2^a*5^c A077187 order families.

This is a new EXACT NORM-REUSE theorem, not a prime search. A formal
22-phase folding lemma reduces the stable drift for v=11*s (s=3,9)
to the same fixed v=11 linear polynomial, evaluated at m'=s*u/t
and phase gamma'=(s*u)^(-1) mod 11, t=gcd(2,u). Therefore every
hypothetical zero drift prime divides one of the 20 EXACT integer
resultant norms already certified in certify_fixed_v11.py.

We independently exhaust ALL 2^a*5^c indices below the corresponding
phase-dependent norm and verify gcd(N, Phi_{11*s*2^a*5^c}(10))==1,
without factoring N or enumerating candidate target primes.

Requires SymPy only for four tiny *base* cyclotomic polynomials per s.
Resultant algebra and norm proof are independently verified by
certify_fixed_v11.py and its own GitHub Actions workflow.
"""
from hashlib import sha256
from math import gcd
from sympy import Symbol,Poly,cyclotomic_poly

# Frozen exact norms from the independently CI-certified 20 linear
# resultants. Duplicated, not imported, to protect against accidental
# changes to the earlier certificate table.
NORMS = {
 11: {
  1:15127131018612774155981272140023529449278464,
  2:1225495932559745042375384507489056346459136,
  3:42367371154715789557360879894110000000000,
  4:256179292089836816135434505919211662336,
  5:4338418806242896850673754101156864,
  6:4338418806242896850673754101156864,
  7:256179292089836816135434505919211662336,
  8:42367371154715789557360879894110000000000,
  9:1225495932559745042375384507489056346459136,
 10:15127131018612774155981272140023529449278464},
 22: {
  1:285516851271280164572961034632619303414011,
  2:214182411409509503494503647303624144662011,
  3:174217810946540745462448546732625758006011,
  4:158087601681258150675757566429843100246011,
  5:166212164989478356770043568530151430262011,
  6:166212164989478356770043568530151430262011,
  7:158087601681258150675757566429843100246011,
  8:174217810946540745462448546732625758006011,
  9:214182411409509503494503647303624144662011,
 10:285516851271280164572961034632619303414011}
}
EXPECTED_V11_NORM_SHA256 = (
    "513c1bc27609c811d838d00f6248f61f1f349c9b3e1fa6f54472e37597ab76e7"
)
EXPECTED_COUNTS = {3:3850, 9:3757}

def audit_norm_table():
    table = "".join(f"{g},{gamma},{NORMS[g][gamma]}\n"
        for g in (11,22) for gamma in range(1,11)).encode()
    assert sha256(table).hexdigest()==EXPECTED_V11_NORM_SHA256
    assert all(N>0 for d in NORMS.values() for N in d.values())

def base_polynomials(s):
    x=Symbol("x")
    return {
        (aa,cc): [int(z) for z in Poly(
            cyclotomic_poly(11*s*(2 if aa else 1)*(5 if cc else 1),x),x
        ).all_coeffs()]
        for aa in (False,True) for cc in (False,True)
    }

def phi_mod_norm(s,a,c,N,bases):
    # Since 11*s is coprime to 10, the standard cyclotomic
    # prime-power substitution identity applies to 2^a and 5^c.
    e=2**max(a-1,0)*5**max(c-1,0)
    y=pow(10,e,N)
    result=0
    for coeff in bases[(a>0,c>0)]:
        result=(result*y+coeff)%N
    return result

def exhaustive_exclusion(s):
    assert s in (3,9)
    bases=base_polynomials(s)
    max_norm=max(max(d.values()) for d in NORMS.values())
    a=0
    checked=0
    phase_counts={}
    while 11*s*2**a<=max_norm:
        c=0
        while (r:=11*s*2**a*5**c)<=max_norm:
            u=2**a*5**c
            gamma=pow((s*u)%11,-1,11)
            g=11 if a==0 else 22
            N=NORMS[g][gamma]
            # Phase-sensitive bounds are NOT monotone in a or c.
            # Each admissible r must be tested separately.
            if r<=N:
                h=gcd(N,phi_mod_norm(s,a,c,N,bases))
                assert h==1,(s,a,c,r,g,gamma,h)
                checked+=1
                phase_counts[(g,gamma)]=phase_counts.get((g,gamma),0)+1
            c+=1
        a+=1
    assert checked==EXPECTED_COUNTS[s],(s,checked,EXPECTED_COUNTS[s])
    return checked,phase_counts

def main():
    audit_norm_table()
    print("PASS verified same pinned 20 exact v=11 elimination norms")
    for s in (3,9):
        n,_=exhaustive_exclusion(s)
        print(f"PASS s={s}, v={11*s}: {n} phase-aware infinite-exponent index exclusions; all gcd=1")
    print("THEOREM: ord_p(10)=33*2^a*5^c or 99*2^a*5^c => nonzero stable drift")
    print("Unrestricted A077187 all-primes conjecture remains OPEN.")

if __name__=="__main__":
    main()
