#!/usr/bin/env python3
"""Certify that three primes are terminal in the single-prime norm-order graph."""
from math import gcd, isqrt, prod

# q, norm prime p, complete prime factorization of p-1,
# primitive root witness, roots x^2=2, y^2=2*x, z^2=5 modulo p.
ROWS=(
    (17,152278105612081,((2,4),(3,1),(5,1),(7,1),(17,1),(41,1),(193,1),(673811,1)),
     19,1745782824757,22803992262977,75895411019931),
    (19,7288288224767761,((2,4),(3,1),(5,1),(7,1),(19,1),(41,2),(227,1),(598369,1)),
     22,1133425683383699,3582029197855130,3083684573490331),
    (23,16454995746349728961,((2,6),(3,2),(5,1),(7,2),(23,1),(41,1),(113,1),(251,1),(4359587,1)),
     22,7623309455290880278,7494070251204616725,6982634978947343705),
)

def prime_small(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))

def verify():
    F=[0,1]
    Q=[1,1]
    for _ in range(46):
        F.append(F[-1]+F[-2])
        Q.append(2*Q[-1]+Q[-2])
    for q,p,fac,a,x,y,z in ROWS:
        assert prime_small(q) and p==5*F[2*q]**2-4*Q[q]**2
        assert prod(l**e for l,e in fac)==p-1
        assert all(prime_small(l) for l,e in fac)
        # At every prime divisor of p, a must have order p-1.
        # This proves p prime, using the complete factorization above.
        assert pow(a,p-1,p)==1
        assert all(gcd(pow(a,(p-1)//l,p)-1,p)==1 for l,e in fac)
        # Complete splitting and both norm characters trivial.
        assert p%4==1 and x*x%p==2 and z*z%p==5 and y*y%p==2*x%p
        print(q,'terminal; unique norm prime',p)

if __name__=='__main__':
    verify()
