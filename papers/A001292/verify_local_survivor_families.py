#!/usr/bin/env python3
"""Infinite simultaneous local power families: an obstruction, not counterexamples."""
from pathlib import Path
from math import gcd,lcm
import json
ROOT=Path(__file__).parent
I=((1,0,0),(0,1,0),(0,0,1))
def mul(A,B,p):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%p for j in range(3)) for i in range(3))
def power(A,n,p):
 R=I
 while n:
  if n&1:R=mul(R,A,p)
  A=mul(A,A,p);n//=2
 return R
def append(v,a,n,d,p):
 B=pow(10,d,p)
 if B==1:return (v+n*a+n*(n-1)//2)%p
 c=B-1;lift=p*c*c;U=pow(B,n,lift)
 s0=(U-1)//c%p;s1=((B-(n%lift)*U+((n-1)%lift)*B*U)%lift)//(c*c)
 return (U*v+(a+n-1)*s0-s1)%p
T=38168130;M=152672520
families=[(31,53392081,'square'),(32,95797681,'seventeenth')]
cert=[]
for p,r in[(7,6),(11,2),(13,6),(31,15),(41,5)]:
 E=p*r
 def A(d):return ((pow(10,d,p),1,0),(0,1,1),(0,0,1))
 def F(d):
  L=pow(10,d-1,E);Q=power(A(d),9*L%E,p)
  return Q[0][0],(Q[0][1]*L+Q[0][2])%p
 assert pow(10,r,p)==1
 assert all(power(A(d),E,p)==I for d in range(1,r+1))
 s=E
 while s%2==0:s//=2
 while s%5==0:s//=5
 assert pow(10,r,s)==1
 # Nonunit part divides10, so positive powers have already saturated it.
 assert 10%(E//s)==0
 aa,bb=1,0
 for d in range(2,r+2):
  a,b=F(d);aa,bb=a*aa%p,(a*bb+b)%p
 assert aa==1
 # Repeat the affine translation p times: full boundary periodE.
 assert p*bb%p==0 and T%E==0 and M%E==0
 item={'p':p,'order':r,'append_period':E,'boundary_period':E,'macro_translation':bb,'residues':{}}
 for d0,m0,kind in families:
  V=0;L=1
  for d in range(1,d0):V=append(V,L,9*L,d,p);L*=10
  n=(m0-L)%E+1
  # Matrix and independent geometric closed formula agree.
  Q=power(A(d0),n,p);W=(Q[0][0]*V+Q[0][1]*(L%p)+Q[0][2])%p
  assert W==append(V,L,n,d0,p)
  expected=8 if p==11 and kind=='seventeenth' else 1
  assert W==expected
  # Check several later full periods via independent actual-width sums.
  for shift in(1,2):
   d1=d0+shift*E;v=0;l=1
   for d in range(1,d1):v=append(v,l,9*l,d,p);l*=10
   assert append(v,l,(m0-l)%E+1,d1,p)==expected
  item['residues'][kind]=W
 cert.append(item)
for d,m,kind in families:
 assert m%120==1 and M%120==0
 assert T%2==0 and T%3==0
 # W_m is1 mod3,1 mod5,1 mod8, by the digit sum and final block.
 assert (m*(m+1)//2)%3==1 and m%5==1 and m%8==1
assert families[1][0]%2==0 and families[1][1]%2==1
for p in(2,3,5,7,11,13,31,41):assert gcd(17,p*(p-1))==1
assert T==lcm(42,22,78,465,205)
assert M==lcm(T,120)
# Direct actual-digit modular audit at32-digit endpoints; no period reduction ofm.
for p,r in[(7,6),(11,2),(13,6),(31,15),(41,5)]:
 for d,mres,kind in families:
  lower=10**(d-1);m=lower+(mres-lower)%M
  v=0;L=1
  for width in range(1,d):v=append(v,L,9*L,width,p);L*=10
  value=append(v,L,m-L+1,d,p)
  assert value==(8 if p==11 and kind=='seventeenth' else 1)
(ROOT/'local_survivor_certificate.json').write_text(json.dumps({'width_period':T,'endpoint_period':M,'families':families,'prime_certificates':cert},indent=2)+'\n')
print('PASS:34 append phases, five affine-period certificates, all selected residues')
print('PASS:20 independent later-width checks and10 actual31/32-digit endpoint checks')
print('PASS: exact2/3/5 conditions and17th-power Hensel hypotheses at all eight primes')
print(json.dumps(cert,indent=2))
