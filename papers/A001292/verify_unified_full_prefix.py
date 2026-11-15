#!/usr/bin/env python3
"""Finite audit, not an enumeration proof of unbounded perfect-power claims."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
checks=defaultdict(int)

def vp(a,p):
    assert a>0
    v=0
    while a%p==0:
        a//=p; v+=1
    return v

def det(rows):
    (a,b,c),(d,e,f),(g,h,i)=rows
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

# Prefix smooth parts and all explicit small-width cases.
W=[0]; digits=[0]
for k in range(1,5001):
    w=len(str(k)); W.append(W[-1]*10**w+k); digits.append(digits[-1]+w)
    if k<10: continue
    B=10**w; L=B//10; C=B-1; K=k-L+1
    J=k*C+B
    assert all(vp(W[k],p)==vp(J,p)<w*K for p in (2,5))
    assert all(vp(W[k],p)<digits[k] for p in (2,5))
    smooth=2**vp(W[k],2)*5**vp(W[k],5)
    assert smooth<=J<B*B
    checks['prefix_smooth_and_unsaturated']+=1
    if K<=7 and w in (2,3): checks['fourteen_small_cases']+=1
assert checks['fourteen_small_cases']==14

# Exact rotation identity, leading coefficient and signed correction bounds.
endpoints=list(range(10,150))+[199,200,299,999,1000,1001,1099,1199]
for m in endpoints:
    d=len(str(m)); B=10**d; L=B//10; C=B-1; t=digits[L-1]
    G=10**t; A=C*C*W[L-1]+L*C+1; N=m-L+1; M=m*C+B
    ks=list(range(1,m)) if m<150 else sorted({1,9,10,L-2,L-1,L,L+6,L+7,m-1} & set(range(1,m)))
    for k in ks:
        s=digits[k]; V=10**s; U=W[k]; coefficient=V*A-G*C*C*U; T=V*M-C*C*U
        R=(W[m]-U*10**(digits[m]-s))*V+U
        assert C*C*R==coefficient*B**N-T
        assert coefficient*10>=C*C*G
        assert abs(T)<B*B*V
        assert 0<U*8<V
        assert R>0 and len(str(R))==digits[m]
        assert R%V==U
        if k>=L: assert coefficient==G*(k*C+B)
        else:
            suffix=W[L-1]-U*10**(t-s)
            assert coefficient==V*(C*C*suffix+L*C+1)
        # At the domain's first endpoint, exponential-minus-linear curve has positive derivative.
        n0=max(1,k-L+2)
        assert coefficient*B**n0 > C*V # log(B)>1
        checks['exact_rotation_and_bounds']+=1
        checks['earlier_width_identity' if k<L else 'same_width_identity']+=1
        if T<0: checks['negative_corrections']+=1

# Root compression for arbitrary targets with unsaturated valuations.
for p in (2,5):
 for n in range(1,6):
  modulus=p**n
  for ell in (2,3,5,7):
   fibers=defaultdict(list)
   for x in range(modulus): fibers[pow(x,ell,modulus)].append(x)
   for u in range(1,min(modulus,101)):
    v=vp(u,p)
    if v>=n: continue
    roots=fibers[u]
    if v%ell:
        assert not roots
    else:
        a=v//ell; D=p**(n-(ell-1)*a)
        branches={x%D for x in roots}
        cap=(4 if p==2 else 2) if ell==2 else (5 if p==5 and ell==5 else 1)
        assert len(branches)<=cap
        assert all(vp(x,p)==a for x in roots if x)
    checks['prime_power_root_compression']+=1

for n in range(1,4):
 modulus=10**n
 for ell in (2,3,5,7):
  fibers=defaultdict(list)
  for x in range(modulus): fibers[pow(x,ell,modulus)].append(x)
  for k in range(10,80):
   v2,v5=vp(W[k],2),vp(W[k],5)
   if max(v2,v5)>=n: continue
   roots=fibers[W[k]%modulus]
   if v2%ell or v5%ell:
    assert not roots
   else:
    z=2**(v2//ell)*5**(v5//ell); D=modulus//z**(ell-1)
    cap=8 if ell==2 else (5 if ell==5 else 1)
    assert len({x%D for x in roots})<=cap
   checks['decimal_crt_compression']+=1

# Rational evaluations of the exact differentiation identity and H derivative.
for ell in range(2,20):
 for q in (F(1),F(3,2),F(2),F(7)):
  for a in (F(1),F(3),F(11)):
   for b in (F(1,3),F(2),F(5)):
    for T in (F(-13),F(-1),F(0),F(1),F(17)):
     g=a*q**ell-T
     gp=ell*a*q**(ell-1)-b/q
     gpp=ell*(ell-1)*a*q**(ell-2)+b/q**2
     expanded=ell*g*gpp-(ell-1)*gp*gp
     claimed=ell*a*q**(ell-2)*((2*ell-1)*b-ell*(ell-1)*T)-(ell*b*T+(ell-1)*b*b)/q**2
     assert expanded==claimed
     hdirect=-ell*(ell-1)*b-b/(ell*a*q**ell)*(ell*b-ell*(ell*T+(ell-1)*b))
     hclaim=-ell*(ell-1)*b+ell*b*T/(a*q**ell)+(ell-2)*b*b/(a*q**ell)
     assert hdirect==hclaim
     if g>0 and gp>0: assert hclaim<0
     checks['derivative_identity_samples']+=1

# Synthetic determinants are not actual perfect-power rotations.
for D in (1,3,8,25,100):
 for residue in (0,1,2):
  for exps in ((0,1,2),(1,2,4),(2,4,6)):
   qs=[10**e for e in exps]
   for cs in ((1,2,5),(1,10,100),(3,7,21)):
    xs=[residue+D*c for c in cs]
    delta=det([[x,q,1] for x,q in zip(xs,qs)])
    if delta:
     assert delta%(D*qs[0])==0 and abs(delta)>=D*qs[0]
     checks['synthetic_determinant_divisibility']+=1
   alpha=F(7,3); errors=[F(1),F(-1,2),F(1,4)]
   xs=[alpha*q-error for q,error in zip(qs,errors)]
   delta=det([[x,q,1] for x,q in zip(xs,qs)])
   assert abs(delta)<2*qs[-1]
   checks['synthetic_error_bound']+=1

# Centered bounds: rational checks over many widths; full proof is in note.
for d in range(3,1001):
 L=10**(d-1); t=F((9*d-10)*L+1,9)
 assert t/d-7>=F(L,2) and t/d<L
 for ell in (2,3,5,7,19,101):
  hmin=1+t/d-F(4*ell,ell-1)
  hmax=9*L+t/d-F(4*ell,ell-1)
  assert hmin>=F(L,2) and hmax<10*L
 checks['centered_width_checks']+=1
assert sum(m-1 for m in range(10,100))==4815
assert 2**4<20<2**5 and 3**2<20<3**3
checks['counting_constants']=3

certificate={
 'status':'PASS',
 'scope':'Finite audit only; global theorems rely on the written proof. Synthetic points are not claimed to be perfect-power rotations.',
 'checks':dict(sorted(checks.items())),
 'note_sha256':hashlib.sha256((ROOT/'UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'unified-full-prefix-certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(certificate,indent=2))
