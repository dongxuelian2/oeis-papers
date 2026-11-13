#!/usr/bin/env python3
"""Recovered from original tool-call text; dependency paths made portable."""
from pathlib import Path
import json,sys,math
from fractions import Fraction
from prime_period_certificates import run
from verify_a001292 import direct_prefix_mod,digits_total
ROOT=Path(__file__).parent
rows13={1:(78,0,0,1),15:(26,22,10,8),17:(78,24,2,9),25:(78,24,0,1),29:(78,54,11,9),45:(26,24,0,8)}
def predicted(p,d,m):
 if p==11:
  s=d%22
  if s not in(1,17):return False
  a=(d-s)//22;b=0 if s==1 else 12;alpha=0 if s==1 else 2
  return (m-b)%22==0 and (m-b)//22%11!=(alpha-2*a)%11
 s=d%78
 if s not in rows13:return False
 L,b,alpha,beta=rows13[s];a=(d-s)//78
 return (m-b)%L==0 and (m-b)//L%13!=(alpha+beta*a)%13
for p in(11,13):
 r,E,T,classes=run(p)
 s=9*r
 while s%2==0:s//=2
 while s%5==0:s//=5
 assert pow(10,T,s)==1
 for d in range(2,T+2):
  wanted=set(classes.get(d%T,[]))
  assert {m for m in range(E) if predicted(p,d,m)}==wanted
 K=103 if p==11 else 27
 assert {direct_prefix_mod(k,p)*pow(10,-digits_total(k),p)%p for k in range(K+1)}==set(range(p))
 print('PASS: full compact classification and normalized-prefix cover at',p)
def append_closed(v,a,n,d,M):
 B=pow(10,d,M)
 if B==1:return (v+n*a+n*(n-1)//2)%M
 c=B-1;lift=M*c*c;U=pow(B,n,lift)
 S0=((U-1)//c)%M
 S1=((B-(n%lift)*U+((n-1)%lift)*B*U)%lift)//(c*c)
 return (U*v+(a+n-1)*S0-S1)%M
for p in(11,13):
 for d in range(1,79):
  for a in(0,1,16,73):
   for n in(0,1,2,13,78,169):
    w=0;B=pow(10,d,p*p)
    for x in range(a,a+n):w=(B*w+x)%(p*p)
    assert append_closed(0,a,n,d,p*p)==w
print('PASS:3744 independent closed-form/literal comparisons')
for p,targets in ((11,{17,259,501}),(13,{15,1029,2043})):
 M=p*p;V=0;L=1;r=22 if p==11 else 78;E=242 if p==11 else 1014;checks=0
 for d in range(1,max(targets)+1):
  if d in targets:
   W=V;B=pow(10,d,M);S=(pow(10,d,9*r)-1)//9
   for j in range(E):
    m=L+j;W=(B*W+m)%M
    actual=(d*(m+1)-S)%r==0 and W%p==0 and W!=0
    assert actual==predicted(p,d,m),(p,d,m%E,W)
    checks+=1
  V=append_closed(V,L,9*L,d,M);L*=10
 print('PASS:',checks,'independent closed-form endpoint checks at',p,'widths',sorted(targets))
for p in(11,13):
 M=p*p;W=D=0;prefix=[0];length=[0]
 for m in range(1,1000):
  d=len(str(m));W=(W*10**d+m)%M;D+=d;prefix.append(W);length.append(D)
  delta=(pow(10,D,M)-1)%M
  actual=all((r:=(pow(10,length[k],M)*W-delta*prefix[k])%M)%p==0 and r!=0 for k in range(m))
  assert actual==predicted(p,d,m)
print('PASS:999000 literal rotation checks for11 and13')
D0=346803;period=858858
assert (D0%42,D0%242,D0%1014)==(9,17,15)
assert period==math.lcm(42,242,1014)
assert math.gcd(49,121)==math.gcd(49,169)==math.gcd(121,169)==1
N=49*121*169;count=0
for t in range(N):
 m=2*t
 seven=m%14==2 and m%98!=30
 eleven=m%22==12 and m%242!=56
 thirteen=m%26==22 and m%338!=282
 count+=bool(seven or eleven or thirteen)
union=Fraction(count,2*N)
assert union==Fraction(126320,1002001)
assert union==(1-Fraction(43,49)*Fraction(111,121)*Fraction(157,169))/2
coverage={}
for h,a,b in[(1,131,243),(2,133,243),(3,3673,6561),(4,3674,6561)]:
 q=Fraction(a,b);z=q+(1-q)*union
 coverage[h]={'fraction':str(z),'decimal':float(z),'increment':str(z-q)}
(ROOT/'eleven_thirteen_certificate.json').write_text(json.dumps({'prime13_rows':rows13,'digit_progression':[D0,period],'three_prime_union':str(union),'coverage':coverage},indent=2)+'\n')
print('PASS:1002001 exact CRT combinations; union',union)
print(json.dumps(coverage,indent=2))
