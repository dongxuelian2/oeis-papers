#!/usr/bin/env python3
"""Exact audits supporting the general finite-prime local-square theorem.
The theorem for arbitrary finite S is proved in FINITE_PRIME_LIMIT.md.
"""
from fractions import Fraction
from math import gcd,lcm
from pathlib import Path
import json,random,sys
# The same-directory baseline verifier is already in the repository.
from verify_a001292 import append_block

def order(a,p):
 x=a%p;r=1
 while x!=1:x=x*a%p;r+=1
 return r

def classes(coefficients):
 residues=[1];T=120;expected=Fraction(1,120)
 for p,(B,alpha,beta,gamma) in sorted(coefficients.items()):
  assert p>5 and B%p and beta%p
  H=lcm(T,p-1);assert gcd(H,p)==1
  squares={x*x%p for x in range(1,p)};new=[]
  for r in residues:
   for j in range(H//T):
    a=r+T*j;constant=(alpha*pow(B,a,p)+gamma)%p
    hits=0
    for t in range(p):
     m=a+H*t
     if (constant+beta*m)%p in squares:new.append(m);hits+=1
    assert hits==(p-1)//2
  residues=new;T=H*p;expected*=Fraction(p-1,2*p)
  assert Fraction(len(residues),T)==expected
 assert len(set(residues))==len(residues)
 return T,residues,expected

def closed(v,a,n,d,p):
 B=pow(10,d,p)
 if B==1:return (v+n*a+n*(n-1)//2)%p
 c=B-1;lift=p*c*c;U=pow(B,n,lift)
 s0=(U-1)//c%p;s1=((B-(n%lift)*U+((n-1)%lift)*B*U)%lift)//(c*c)
 return (U*v+(a+n-1)*s0-s1)%p

def coefficients(d,primes):
 lower=10**(d-1);ans={};boundaries={}
 for p in primes:
  B=pow(10,d,p);c=(B-1)%p;assert c
  v=0;a=1
  for w in range(1,d):v=append_block(v,a,9*a,w,p);a*=10
  inv=pow(c,-1,p);A=(c*c*v+lower*c+1)%p
  ans[p]=(B,A*pow(B,1-lower,p)*inv*inv%p,-inv%p,-B*inv*inv%p)
  boundaries[p]=v
 return ans,boundaries

# Exhaustive checks of the joint-count lemma, including overlapping periods.
rng=random.Random(1292);lemma=[]
for ps in [(7,11),(7,13,43),(11,23,47),(7,11,13,17)]:
 cf={p:(rng.randrange(1,p),rng.randrange(p),rng.randrange(1,p),rng.randrange(p)) for p in ps}
 T,rs,sigma=classes(cf)
 # Exhaust all m=1 mod120 in one full common period.
 direct=[]
 for m in range(1,T,120):
  if all(pow((a*pow(B,m,p)+b*m+c)%p,(p-1)//2,p)==1 for p,(B,a,b,c) in cf.items()):direct.append(m)
 assert set(direct)==set(rs)
 lemma.append({'primes':ps,'period':T,'classes':len(rs),'density':str(sigma)})
 print('PASS: joint-count lemma',ps,'period',T,'classes',len(rs))

# Actual concatenation coefficients, independent arithmetic-geometric audit.
primes=(7,11,13,31,41);audits=[]
for d in (9,11,31):
 cf,boundaries=coefficients(d,primes);T,rs,sigma=classes(cf)
 assert T==152672520 and len(rs)==27000
 lower=10**(d-1);tested=0
 # Every survivor class at d=9; 1000 deterministic classes at later widths.
 chosen=rs if d==9 else rs[:1000]
 for r in chosen:
  m=lower+(r-lower)%T;assert len(str(m))==d and m%120==1
  for p in primes:
   W=closed(boundaries[p],lower,m-lower+1,d,p)
   B,a,b,c=cf[p]
   assert W==(a*pow(B,m,p)+b*m+c)%p
   assert W and pow(W,(p-1)//2,p)==1
   tested+=1
  assert m%8==m%5==(m*(m+1)//2)%3==1
 audits.append({'digits':d,'period':T,'survivor_classes':len(rs),'independent_prime_checks':tested})
 print('PASS: actual digit width',d,'survivor classes',len(rs),'independent prime checks',tested)

# Qualifying widths and exact geometric lower-density formula.
sigma=Fraction(27000,152672520)
assert sigma==Fraction(1,120)*Fraction(3,7)*Fraction(5,11)*Fraction(6,13)*Fraction(15,31)*Fraction(20,41)
L=lcm(*(order(10,p) for p in primes));assert L==30
lower=sigma*Fraction(9,10**L-1)
for period in (1,2,3,5):
 expected_min=Fraction(9,10**period-1)
 expected_max=Fraction(9*10**(period-1),10**period-1)
 weights=[]
 for residue in range(period):
  s=sum(10**(period-1-j) for j in range(period) if (residue-j-1)%period==0)
  weights.append(Fraction(9*s,10**period-1))
 assert min(weights)==expected_min and max(weights)==expected_max
# For these particular primes, all odd widths not divisible by5 qualify.
for d in range(1,301):assert all(d%order(10,p) for p in primes)==(d%2==1 and d%5!=0)
result={'general_statement':'Any finite prime set admits a positive-lower-density subset of endpoints whose unrotated concatenations are simultaneous local squares.','joint_count_tests':lemma,'actual_prefix_audits':audits,'eight_prime_example':{'base_endpoint_congruence':'m=1 mod120','qualifying_widths':'d odd and5 does not divide d','density_per_qualifying_width':str(sigma),'classes_per_period':27000,'endpoint_period':152672520,'simple_width_progression':'d=1 mod30','lower_density_bound_from_simple_progression':str(lower)},'proof_required':'The arbitrary-finite-set theorem and all-precision conclusions use the argument and Hensel lifting in FINITE_PRIME_LIMIT.md, not finite extrapolation.'}
Path(__file__).with_name('finite-prime-limit-certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: exact product density',sigma,'and positive geometric lower-density bound',lower)
# Stronger eight-prime bound using every qualifying width phase.
allowed={1,3,7,9}
weights={r:Fraction(9*sum(10**(9-j) for j in range(10) if (r-j)%10 in allowed),10**10-1) for r in range(10)}
assert min(weights,key=weights.get)==6
assert min(weights.values())==Fraction(1010101,1111111111)
full_lower=sigma*min(weights.values())
assert full_lower==Fraction(227272725,1413634444303081)
result['eight_prime_example']['lower_density_bound_using_all_qualifying_widths']=str(full_lower)
Path(__file__).with_name('finite-prime-limit-certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: all eligible width phases give lower-density bound',full_lower,float(full_lower))
