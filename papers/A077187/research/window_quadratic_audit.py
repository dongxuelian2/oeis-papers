#!/usr/bin/env python3
"""A077187: independent quadratic-window audit and no-DLP finite root test.

Requires SymPy. The complete unrestricted conjecture is NOT proved here.
"""
from math import gcd, lcm
from sympy import isprime, n_order, primerange, sqrt_mod

def layer(p, r, d, C, Y):
    L = pow(10, d-1, p); q = pow(10, d, p)
    N = (9*L) % p; A = pow(10, 9*d*pow(10, d-1, r) % r, p)
    if q == 1:
        S = N; J = N*(N-1)*pow(2, -1, p) % p
    else:
        inv = pow(q-1, -1, p)
        S = (A-1)*inv % p
        J = (q-N*A+(N-1)*A*q)*inv*inv % p
    return ((A*C+(q-1)*S-J) % p,
            pow(A, -1, p)*(Y+L*S+J) % p)

def window_residue_formula(p, d, C, Y, n):
    L = pow(10, d-1, p); q = pow(10, d, p)
    if q == 1:
        return ((L+n)**2+C+Y+L-L*L) % p
    inv = pow(q-1, -1, p)
    b = q*inv*inv % p
    A = (q*C+L*q*inv+b) % p
    B = (Y-L*inv+b) % p
    z = pow(q, n, p)
    return (A*z+B*pow(z, -1, p)-2*b) % p

def window_residue_direct(p, d, C, Y, n):
    L = pow(10, d-1, p); q = pow(10, d, p)
    iq = pow(q, -1, p)
    for j in range(n):
        k = (L+j) % p
        C = (q*C+k) % p
        Y = iq*(Y+k) % p
    return (q*C+Y+L+n) % p

def subgroup_root_exists(p, r, d, C, Y):
    """Test roots assuming a full residue period of offsets is allowed.

    Apply on reference windows d>T, or interpret as an unrestricted-offset
    test. Uses modular square roots and subgroup powering, not discrete logs.
    """
    L = pow(10, d-1, p); q = pow(10, d, p)
    if q == 1:
        target = (L*L-L-C-Y) % p
        return target == 0 or pow(target, (p-1)//2, p) == 1
    inv = pow(q-1, -1, p)
    b = q*inv*inv % p
    A = (q*C+L*q*inv+b) % p
    B = (Y-L*inv+b) % p
    H = (-2*b) % p
    h = r//gcd(r, d)
    if A == 0:
        roots = [(-B*pow(H,-1,p)) % p]
    else:
        discriminant = (H*H-4*A*B) % p
        roots = [(-H+s)*pow(2*A,-1,p) % p
                 for s in sqrt_mod(discriminant, p, all_roots=True)]
    return any(z != 0 and pow(z,h,p) == 1 for z in roots)

def drift_or_zero_test(p):
    """Deterministic prime-specific witness or zero-drift reference test.

    Nonzero drift returns k=10^(j*T)+offset. In zero drift, test the short
    transient and one whole stable period by subgroup roots.
    """
    assert p >= 7 and p != 11 and isprime(p)
    r = int(n_order(10,p)); v = r
    while v % 2 == 0: v //= 2
    while v % 5 == 0: v //= 5
    T = lcm(r, int(n_order(10,v)) if v > 1 else 1)
    a = 0; c = 0; temp = r
    while temp % 2 == 0: a += 1; temp //= 2
    while temp % 5 == 0: c += 1; temp //= 5
    E = max(a,c)+1
    C = Y = 0
    early = []
    for d in range(1,T+1):
        if d<E: early.append((d,C,Y))
        C,Y=layer(p,r,d,C,Y)
    C1,Y1=C,Y
    for d in range(T+1,2*T+1): C,Y=layer(p,r,d,C,Y)
    U,V=(C-C1)%p,(Y-Y1)%p
    if U or V:
        slope0=(10*U+V)%p
        offset=0 if slope0 else 1
        slope = slope0 if slope0 else (1000*U+V)%p
        constant = (10*C1+Y1+1) if offset==0 else (1000*C1+Y1+121)
        j = 1+(-constant*pow(slope,-1,p))%p
        assert (constant+(j-1)*slope)%p == 0
        return ('WITNESS',p,r,T,j,offset)
    for d,C,Y in early:
        for n in range(9*10**(d-1)):
            if window_residue_formula(p,d,C,Y,n)==0:
                return ('EARLY_WITNESS',p,d,n)
    C,Y=C1,Y1
    for d in range(T+1,2*T+1):
        if subgroup_root_exists(p,r,d,C,Y):
            return ('LATE_SUBGROUP_ROOT',p,d)
        C,Y=layer(p,r,d,C,Y)
    return ('COUNTEREXAMPLE_CERTIFICATE',p,T)

def audit():
    checked=0; root_checks=0
    for p in primerange(7,250):
        r=int(n_order(10,p)); C=Y=0
        for d in range(1,16):
            for n in (0,1,2,3,5,11,29):
                x=window_residue_formula(p,d,C,Y,n)
                y=window_residue_direct(p,d,C,Y,n)
                assert x==y,(p,d,n,x,y)
                checked+=1
            brute=any(window_residue_formula(p,d,C,Y,n)==0
                      for n in range(r if pow(10,d,p)!=1 else p))
            assert subgroup_root_exists(p,r,d,C,Y)==brute,(p,d)
            root_checks+=1
            C,Y=layer(p,r,d,C,Y)
    for p in (7,13,17,29,73,113,233,313,701):
        assert drift_or_zero_test(p)[0]=='WITNESS',p
    print('PASS',checked,'exact window comparisons;',root_checks,
          'subgroup tests; 9 cross-checked prime witnesses')

if __name__=='__main__':
    import sys
    if len(sys.argv)>1:
        print(drift_or_zero_test(int(sys.argv[1])))
    else: audit()
