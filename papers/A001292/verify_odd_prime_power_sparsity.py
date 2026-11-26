#!/usr/bin/env python3
"""Independent finite checks for the odd-prime-power sparsity proof.
These checks corroborate finite instances; they do not replace the proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import log
import json
from pathlib import Path

def vp(n,p):
    a=0
    while n and n%p==0:
        a+=1; n//=p
    return a

counts=defaultdict(int)
# Compressed local root branches, including nonunit right sides.
for p,ns in ((2,range(1,13)),(5,range(1,6))):
    for n in ns:
        mod=p**n
        for ell in (3,5,7,11,13):
            buckets=defaultdict(list)
            for x in range(mod):
                c=pow(x,ell,mod)
                if c: buckets[c].append(x)
            for c,xs in buckets.items():
                v=vp(c,p)
                assert v%ell==0
                a=v//ell
                assert all(vp(x,p)==a for x in xs)
                r=p**(n-(ell-1)*a)
                bound=5 if p==5 and ell==5 else 1
                assert len({x%r for x in xs})<=bound
                counts['nonzero_local_target_classes']+=1

# Exact derivative algebra after substituting arbitrary rational parameters.
# f=a*Q^ell-T, T'=lambda/Q, T''=-lambda/Q^2.
for ell in range(2,32):
    for Q in (F(1),F(3,2),F(7),F(29)):
        for a,lam,T in ((F(17),F(2),F(9)),(F(53,7),F(11,5),F(24,7)),(F(100),F(1),F(1))):
            f=a*Q**ell-T
            fp=ell*a*Q**(ell-1)-lam/Q
            fpp=ell*(ell-1)*a*Q**(ell-2)+lam/Q**2
            lhs=f*fpp-F(ell-1,ell)*fp*fp
            rhs=a*Q**(ell-2)*((2*ell-1)*lam-ell*(ell-1)*T)-lam*T/Q**2-F(ell-1,ell)*lam**2/Q**2
            assert lhs==rhs
            counts['exact_derivative_instances']+=1

# Width constants checked with integer/rational arithmetic, not large floats.
for d in range(2,1001):
    B=10**d; L=B//10
    t=((9*d-10)*L+1)//9
    assert 9*t==(9*d-10)*L+1
    h=F(L+1)-F(t,2*d)-F(11,2)
    assert h>=F(L,4)
    assert h>0
    P=max(5,d)
    assert d*(3*d+4)*P*(P+1)<=6*B
    assert 25*28*d<=14*B
    assert 25*d*d<=B
    counts['width_constant_instances']+=1

# The proof's final coefficient, plus the extra 24B all-cube cover.
coef=3+14/25+1+(32+16/5)/log(10)
assert coef<20

# Direct sieve corroboration of the elementary prime-counting inequality.
limit=200000
sieve=bytearray(b'\x01')*(limit+1); sieve[:2]=b'\x00\x00'
for p in range(2,int(limit**.5)+1):
    if sieve[p]: sieve[p*p:limit+1:p]=b'\x00'*((limit-p*p)//p+1)
pi=0
for n in range(2,limit+1):
    pi+=sieve[n]
    assert pi<4*n/log(n)
    counts['prime_count_integer_instances']+=1

# Decimal-length / final-block injection on every admissible width-2 pair.
W=''; seen={}
for m in range(1,100):
    W+=str(m)
    if m<20: continue
    for k in range(17,m):
        cut=sum(len(str(j)) for j in range(1,k+1))
        R=int(W[cut:]+W[:cut])
        H=len(str(R)); key=(R%100,H)
        d=2; B=100; L=10; C=99; t=9; G=10**t
        N=m-L+1; K=k-L+1; J=k*C+B; M=m*C+B
        A=C*C*int(''.join(str(j) for j in range(1,L)))+L*C+1
        T=(G*M-A)*B**K+J
        assert C*C*R==G*J*B**N-T
        assert 0<T<2*G*B**(K+2)
        assert (C*C*R+J)%B**K==0
        counts['width_two_exact_rotation_instances']+=1
        assert key==(k,9+2*(m-10+1))
        assert key not in seen
        seen[key]=(m,k)
        counts['width_two_injection_instances']+=1

report={'status':'PASS','scope':'Finite independent corroboration only; general theorem requires the written proof.', 'counts':dict(counts),'full_odd_union_coefficient':coef}
print(json.dumps(report,indent=2))
Path(__file__).with_name('odd-prime-power-certificate.json').write_text(json.dumps(report,indent=2)+'\n')
