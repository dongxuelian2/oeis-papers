#!/usr/bin/env python3
"""A077187 terminal-defect gauge: original early window = late full orbit.

No symbolic packages. Checks fixed rational h=2 quadratic, split-prime
41 witness, and nine genuine smooth-u=4 primes, directly comparing
original layer maps and shifted inverse dynamics with subgroup roots.
This is a local-window theorem, not an all-primes existence theorem.
"""
from fractions import Fraction as Q
from math import gcd,lcm

SAMPLES={
    # p: (ord_p(10), chi(discriminant), number of subgroup roots)
    109:(108,1,1),149:(148,1,1),229:(228,-1,0),
    269:(268,-1,0),349:(116,-1,0),389:(388,1,0),
    509:(508,1,2),709:(708,-1,0),829:(276,-1,0),
}
C1=123456789
Y1=Q(987654321,10**9)
q=100
L=10
c=Q(L,q-1)+Q(1,(q-1)**2)
b=-Q(L,q-1)+Q(q,(q-1)**2)
A=100*(Q(C1)+c)
B=Y1+b
H=-Q(200,9801)
D=H*H-4*A*B

def red(f,p):
    assert f.denominator%p
    return f.numerator*pow(f.denominator,-1,p)%p

def ord10(n):
    if n==1:return 1
    assert gcd(n,10)==1
    x=10%n; r=1
    while x!=1:
        r+=1;x=x*10%n
        assert r<=n
    return r

def layer(p,r,d,C,Y,inverse=False):
    q=pow(10,d,p);L=pow(10,d-1,p);n=9*L%p
    alpha=pow(10,9*d*pow(10,d-1,r)%r,p)
    if q==1:
        S=n;J=n*(n-1)*pow(2,-1,p)%p
    else:
        inv=pow(q-1,-1,p)
        S=(alpha-1)*inv%p
        J=(q-n*alpha+(n-1)*q*alpha)*inv*inv%p
    BC=((q-1)*S-J)%p
    BY=(L*S+J)%p
    if inverse:
        return ((C-BC)*pow(alpha,-1,p)%p,(alpha*Y-BY)%p)
    return ((alpha*C+BC)%p,(Y+BY)*pow(alpha,-1,p)%p)

def run():
    assert A==Q(120999998998000,9801)
    assert B==Q(8790000000121,9801000000000)
    assert D==Q(-669867392724508459,15125000)
    assert red(D,41)==12
    assert pow(12,20,41)==40
    print("PASS exact rational terminal h=2 polynomial and split p=41")
    for p,(want_r,chi,want_roots) in SAMPLES.items():
        assert p%40==29
        r=ord10(p)
        assert r==want_r and r%4==0 and (r//4)%2==1 and r%5!=0
        v=r//4
        T=lcm(r,ord10(v))
        # Initial complete actual digit blocks:
        C,Y=0,0
        C,Y=layer(p,r,1,C,Y)
        assert C==C1%p and Y==red(Y1,p)
        C2,Y2=layer(p,r,2,C,Y)
        # State immediately before shifted full length-(pT+2) window:
        x,y=layer(p,r,T+2,C2,Y2,inverse=True)
        mult=pow(10,9*2*10%r,p)
        hat=pow(10,9*(T+2)*pow(10,T+1,r)%r,p)
        rho=hat*pow(mult,-1,p)%p
        # In the original/late quadratic formulas only:
        ic=red(c,p);ib=red(b,p)
        assert (x+ic)%p==(C+ic)*pow(rho,-1,p)%p
        assert (y+ib)%p==(Y+ib)*rho%p
        # Explicit proof that the phase belongs to the q=100 subgroup:
        n=r//gcd(r,2)
        subgroup={pow(100,j,p) for j in range(n)}
        assert rho in subgroup
        roots=[z for z in subgroup if (red(A,p)*z*z+red(H,p)*z+red(B,p))%p==0]
        late=[z for z in subgroup if (
            100*(x+ic)*z*z+red(H,p)*z+y+ib)%p==0]
        assert set(late)=={rho*z%p for z in roots}
        delta=red(D,p)
        symbol=0 if delta==0 else (1 if pow(delta,(p-1)//2,p)==1 else -1)
        assert (symbol,len(roots))==(chi,want_roots),(p,symbol,len(roots))
        print(f"PASS p={p} ord={r} disc_symbol={symbol} subgroup_roots={len(roots)}")
    print("PASS terminal-defect phase gauge and actual u=4 orbit comparison")
    print("A077187 unrestricted still OPEN; u=4 is already solved via a different window.")

if __name__=="__main__":run()
