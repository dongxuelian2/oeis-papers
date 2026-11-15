#!/usr/bin/env python3
"""Verify new sufficient exclusions; deliberately does NOT assert completeness.
Uses the pre-existing proved cubic congruence, independently checks it with
matrix concatenation, and checks all possible prime divisors of valuations.
"""
from verify_a001292 import append_block, direct_prefix_mod, digits_total
from verify_boundary_valuations import valuation
from verify_three_adic_intervals import cubic

EXTRA = {1: {26,27,81,108,134,135,216},
         2: {27,81,107,108,135,215,216}}

def excluded_residue(n, precision):
    n %= 3**precision
    if not n:
        return False
    b = valuation(n)
    if not b:
        return False
    remainder = b
    for p in (2,3):
        while remainder % p == 0:
            remainder //= p
    if remainder != 1:
        return False
    unit = n//3**b
    return ((b%2 != 0 or unit%3 == 2) and
            (b%3 != 0 or (precision-b >= 2 and unit%9 not in (1,8))))

def class133(m,u):
    return (m%9 in (2,3,5,6) or m%27 in (9,17)
            or m%243 in EXTRA[u%3])

def residue_audit():
    for u in (1,2,4,5,7,8):
        found = {m for m in range(243)
                 if all(excluded_residue(cubic(m,k,9*u,243),5)
                        for k in range(9))}
        expected = {m for m in range(243) if class133(m,u)}
        assert found == expected and len(found) == 133
    # Exercise general-h criterion and period, with zero-residue safety.
    cases = 0
    for h in range(2,9):
        mod = 3**(h+4)
        for u in (1,2,4,5,7,8):
            d = 3**h*u
            for m in range(243):
                for k in range(9):
                    assert cubic(m,k,d,mod) == cubic(m,k+9,d,mod)
                    n=cubic(m,k,d,mod)
                    if excluded_residue(n,h+4):
                        # Independent enumeration of every possible exponent.
                        b=valuation(n); unit=n//3**b
                        primes=[p for p in range(2,b+1)
                                if all(p%q for q in range(2,int(p**0.5)+1))]
                        for p in primes:
                            if b%p == 0:
                                assert (p==2 and unit%3==2) or (p==3 and unit%9 not in (1,8))
                    cases += 1
    assert not excluded_residue(0,10)
    print('PASS: six 133-class sets; general-h residue and prime-divisor checks:',cases)

def matrix_audit():
    checks=certificates=0
    for d in (9,18,27,81,243):
        h=valuation(d); precision=h+6; mod=3**precision
        prefix=0; lower=1
        for width in range(1,d):
            prefix=append_block(prefix,lower,9*lower,width,mod)
            lower*=10
        samples={lower,10*lower-1,(11*lower-1)//2}
        residues=range(243) if h==2 else (0,1,2,26,27,80,81,134,242)
        for r in residues:
            samples.add(lower+(r-lower)%243)
        for m in sorted(samples):
            W=append_block(prefix,lower,m-lower+1,d,mod)
            shift=(pow(10,digits_total(m),mod)-1)%mod
            sufficient=all(excluded_residue(cubic(m,j,d,3**(h+4)),h+4)
                           for j in range(9))
            cuts=set(range(12))|{lower-1,m-1}
            for k in cuts:
                if k==lower-1: Wk=prefix
                elif k==m-1: Wk=append_block(prefix,lower,m-lower,d,mod)
                else: Wk=direct_prefix_mod(k,mod)
                Dk=digits_total(k)
                R=(pow(10,Dk,mod)*W-shift*Wk)%mod
                assert R*pow(10,-Dk,3**(h+4))%3**(h+4)==cubic(m,k,d,3**(h+4))
                if sufficient or (h==2 and class133(m,d//9)):
                    assert excluded_residue(R,precision),(d,m,k,R)
                    certificates+=1
                checks+=1
        print('PASS: independent matrix interval d =',d,'prefixes =',len(samples))
    print('PASS: independent rotation checks:',checks,'certified exclusions:',certificates)

if __name__=='__main__':
    residue_audit()
    matrix_audit()
