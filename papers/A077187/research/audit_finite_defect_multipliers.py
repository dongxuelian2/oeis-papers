#!/usr/bin/env python3
"""Independent exact finite-defect multiplier audit for A077187.

PROVED formula (not merely a conjecture):
  rho_d = (10^v)^(-v^(-1) * 9*d*10^(d-1) mod u) mod p,
where r=ord_p(10)=u*v, u is 2,5-smooth and gcd(v,10)=1.

All checks use direct modular exponents of the *original* and the
*T+d*-layer multipliers, not the symbolic transfer-state formula.
No SymPy, no GMP, no numerical approximations.
"""
from math import gcd, lcm

PRIMES = [
    73, 137, 7841, 617, 233, 313, 2393,
    17, 113, 337, 193, 577,
    151, 1151, 251, 1051, 601, 701, 751, 4751,
]

def order(a, n):
    assert gcd(a, n) == 1
    x = a % n
    k = 1
    while x != 1:
        k += 1
        x = x*a % n
        assert k <= n
    return k

def factor_smooth(r):
    v = r
    u = 1
    for q in (2, 5):
        while v % q == 0:
            v //= q
            u *= q
    return u, v

def check(p):
    r=order(10,p)
    u,v=factor_smooth(r)
    T=lcm(r,order(10,v) if v>1 else 1)
    a=c=0
    n=u
    while n%2==0: n//=2; a+=1
    while n%5==0: n//=5; c+=1
    E=1+max(a,c)
    zeta=pow(10,v,p)
    gamma=pow(v,-1,u) if u>1 else 0
    assert pow(zeta,u,p)==1
    if u>1:
        assert all(pow(zeta,u//q,p)!=1 for q in (2,5) if u%q==0)

    for d in range(1,E+5):
        e=(9*d*pow(10,d-1,r))%r
        ehat=(9*(T+d)*pow(10,T+d-1,r))%r
        orig=pow(10,e,p)
        continued=pow(10,ehat,p)
        rho=(continued*pow(orig,-1,p))%p
        predicted=(
            pow(zeta,(-gamma*9*d*pow(10,d-1,u))%u,p)
            if u>1 else 1
        )
        assert rho==predicted,(p,r,u,v,d,rho,predicted)
        if d>=E:
            assert rho==1,(p,r,d,E)
        if u==8 and d in (2,3):
            assert rho==p-1,(p,r,d,rho)
    return p,r,u,v,T,E

if __name__=='__main__':
    for p in PRIMES:
        print('PASS',check(p))
    print('PASS exact continuation/primitive-smooth-root ratio for',
          len(PRIMES),'primes; full A077187 conjecture remains OPEN')
