#!/usr/bin/env python3
"""Odd-order prime exclusions cover even widths and odd endpoints."""
import json,math
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).parent
I=((1,0,0),(0,1,0),(0,0,1))
def mul(A,B,M):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%M for j in range(3)) for i in range(3))
def power(A,n,M):
 R=I
 while n:
  if n&1:R=mul(R,A,M)
  A=mul(A,A,M);n//=2
 return R
def append_closed(v,a,n,d,M):
 B=pow(10,d,M)
 if B==1:return (v+n*a+n*(n-1)//2)%M
 c=B-1;lift=M*c*c;U=pow(B,n,lift)
 s0=(U-1)//c%M;s1=((B-(n%lift)*U+((n-1)%lift)*B*U)%lift)//(c*c)
 return (U*v+(a+n-1)*s0-s1)%M
rows=[(31,465,168,155,91,28,17,-6,868),(41,205,38,205,126,5,27,5,861)]
cert=[]
for p,r,s,L,b,C,H,J,macro in rows:
 M=p*p;E=p*r
 K=88 if p==31 else 133
 W=D=0;X={0}
 for k in range(1,K+1):
  width=len(str(k));W=(W*10**width+k)%p;D+=width;X.add(W*pow(10,-D,p)%p)
 assert X==set(range(p))
 def A(d):return ((pow(10,d,M),1,0),(0,1,1),(0,0,1))
 def F(d):
  x=pow(10,d-1,E);Q=power(A(d),9*x%E,M)
  return Q[0][0],(Q[0][1]*x+Q[0][2])%M
 # Exact order, append matrix period, and affine-period identities.
 assert pow(10,r,M)==1
 assert all(pow(10,q,M)!=1 for q in range(1,r) if r%q==0)
 assert all(power(A(d),E,M)==I for d in range(1,r+1))
 assert power(A(s),p*L,M)==I
 unitpart=E
 while unitpart%2==0:unitpart//=2
 while unitpart%5==0:unitpart//=5
 assert pow(10,r,unitpart)==1
 A0,B0=1,0
 for d in range(2,r+2):
  a0,b0=F(d);A0,B0=a0*A0%M,(a0*B0+b0)%M
 assert (A0,B0)==(1,macro) and p*macro%M==0
 # Check digit count exactly over a full residue period.
 S=(pow(10,s,9*r)-1)//9
 assert {m for m in range(r) if (s*(m+1)-S)%r==0}=={m for m in range(r) if (m-b)%L==0}
 repunit=9*r
 while repunit%2==0:repunit//=2
 while repunit%5==0:repunit//=5
 assert pow(10,r,repunit)==1
 # Every possible lift a modp, not just the first two examples.
 V=append_closed(0,1,9,1,M);checks=0
 for d in range(2,E+2):
  if d%r==s:
   a=(d-s)//r;start=pow(10,d-1,p*L)
   for t in range(p):
    m=b+L*t;n=(m-start)%(p*L)+1;Q=power(A(d),n,M)
    W=(Q[0][0]*V+Q[0][1]*start+Q[0][2])%M
    assert W==p*((C+H*t+J*a)%p),(p,d,t,W)
    checks+=1
  aa,bb=F(d);V=(aa*V+bb)%M
 assert checks==p*p
 cert.append({'p':p,'order':r,'full_width_period':E,'append_period':E,'macro_translation':macro,'s':s,'L':L,'b':b,'prefix_coefficients':[C,H,J]})
 print('PASS:',p,'all',r,'append phases, full affine identity and',checks,'parameter residue pairs')
 # Independent full actual-width prefixes, without period reduction of widths.
 targets={s,s+r,s+2*r};V=0;start=1;ind=0
 for d in range(1,max(targets)+1):
  if d in targets:
   a=(d-s)//r
   for t in range(p):
    n=(b+L*t-start)%(p*L)+1
    W=append_closed(V,start,n,d,M)
    assert W==p*((C+H*t+J*a)%p)
    ind+=1
  V=append_closed(V,start,9*start,d,M);start*=10
 print('PASS:',ind,'independent arithmetic-geometric prefix checks at widths',sorted(targets))
# Simple subfamilies lie outside BOTH previous parity/3-adic methods.
for j in range(31):
 d=168+28830*j;a=(d-168)//465
 for k in range(31):
  m=91+28830*k;t=(m-91)//155
  assert d%2==0 and m%2==1 and m%3==1 and (t-2-4*a)%31!=0
for j in range(41):
 d=38+16810*j;a=(d-38)//205
 for k in range(41):
  m=331+50430*k;t=(m-126)//205
  assert d%2==0 and m%2==1 and m%3==1 and (t-15-15*a)%41!=0
# Conditional CRT for the joint width progression d=9468 mod19065.
assert (9468-168)%465==0 and (9468-38)%205==0
assert math.lcm(465,205)==19065
# Both endpoint families require m=1 mod5; conditional moduli31^2,41^2 coprime.
u=(1-Fraction(931,961)*Fraction(1641,1681))/5
assert u==Fraction(17534,1615441)
# For d=9468, the excluded t-lifts are20 at31 and8 at41.
N=961*1681;count=0
for z in range(N):
 m=1+5*z
 f31=(m-91)%155==0 and ((m-91)//155)%31!=20
 f41=(m-126)%205==0 and ((m-126)//205)%41!=8
 count+=bool(f31 or f41)
assert Fraction(count,5*N)==u
print('PASS: simple double-blind subfamilies and',N,'conditional CRT checks; union',u,float(u))
(ROOT/'odd_order_families_certificate.json').write_text(json.dumps({'families':cert,'joint_digit_progression':[9468,19065],'joint_endpoint_density':str(u)},indent=2)+'\n')

# Optional combination with the verified7/11/13 progression.
D0=4200162423;period=5458042590
assert D0%858858==346803 and D0%19065==9468
assert period==math.lcm(858858,19065)
assert math.gcd(2*49*121*169,5*961*1681)==1
ue=Fraction(126320,1002001);u5=1-(1-ue)*(1-u)
assert u5==Fraction(219416697774,1618673497441)
print('PASS: five-prime CRT progression',D0,period,'union',u5,float(u5))
