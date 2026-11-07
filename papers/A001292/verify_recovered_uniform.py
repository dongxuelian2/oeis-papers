#!/usr/bin/env python3
"""New recovery audit, not a byte-for-byte copy of the lost four verifiers.
Checks the exact recovered manuscript's18-cut theorem, all-h test andh4 set.
Run beside the published baseline verifier files, or its recovery subdirectory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent/'published-baseline'))
from verify_a001292 import append_block,digits_total,direct_prefix_mod
from verify_boundary_valuations import valuation
from verify_h3_local_equivalence import G
K0=(0,2,3,5,8,9,11,15,30)
K1=(1,4,19,22,100,106,109,1000,10006)
K=tuple(sorted(K0+K1))
def large(n):
 if n==0:return False
 for p in(2,3):
  while n%p==0:n//=p
 return n>1
def witness(w,P):
 w%=3**P
 if not w:return False
 b=valuation(w);u=w//3**b
 return b==0 or large(b) or b%2==0 and u%3==1 or b%3==0 and P-b>=2 and u%9 in(1,8)
def test_units(b,U):return b==0 or large(b) or b%2==0 and any(w%3==1 for w in U) or b%3==0 and any(w%9 in(1,8) for w in U)
def local_test(W,delta,P):
 if not delta:
  assert W and valuation(W)<=P-2
  return witness(W,P)
 n=valuation(delta)
 if W%3**n==0:return True
 b=valuation(W);g=W//3**b%9;c=delta//3**n%3
 return test_units(b,{g} if n-b>=2 else {g,(g-3*c)%9})
def polynomial_test(m,d):
 h=valuation(d);assert h>=2
 u=d//3**h;P=h+5;g=G(m%3**P,d,P)
 if m%27 not in(0,26):return not(m%9 in(2,3,5,6) or m%27 in(9,17))
 n=h+4 if m%27==0 else h+2
 if g%3**n==0:return True
 b=valuation(g);w=g//3**b%9
 return test_units(b,{w} if n-b>=2 else {w,(w+3*u)%9})
def lifting():
 X={k:direct_prefix_mod(k,81)*pow(10,-digits_total(k),81)%81 for k in K}
 assert {X[k]%27 for k in K0}==set(range(0,27,3))
 assert {X[k] for k in K1}==set(range(1,81,9))
 sig=lambda n:(n%2==0,n%3==0,large(n))
 signatures={tuple(sig(n+t) for t in range(3)):n for n in range(2,10001)}
 for ss,n in signatures.items():
  for c in range(81):
   if not c%3:continue
   for z in range(81):
    good=False
    for x in X.values():
     r=(z-c*x)%81
     if not r:continue
     t=valuation(r)
     if t>2:continue
     w=r//3**t;two,three,big=ss[t]
     if big or two and w%3==1 or three and w%9 in(1,8):good=True;break
    assert good,(n,c,z)
 assert len(signatures)==24
 print('PASS: exact18-prefix coverage;24 valuation signatures through n=10000, all z,c mod81')
def literal():
 P=18;M=3**P;W=D=0;count=0
 X={k:direct_prefix_mod(k,M)*pow(10,-digits_total(k),M)%M for k in K}
 for m in range(1,100001):
  d=len(str(m));W=(W*10**d+m)%M;D+=d
  if m<10007:continue
  delta=(pow(10,D,M)-1)%M
  assert delta and valuation(delta)+4<=P
  assert local_test(W,delta,P)==any(witness((W-delta*x)%M,P) for x in X.values())
  count+=len(K)
 print('PASS:',count,'literal-prefix fixed-cut comparisons')
def h4():
 extra={26,27,81,107,108,134,135,161,215,216}
 for u in range(27):
  if u%3==0:continue
  count=0
  for m in range(6561):
   excluded=m%9 in(2,3,5,6) or m%27 in(9,17) or m%243 in extra or m%6561 in {729*(4-3*u)%6561,729*(1-3*u)%6561}
   assert excluded== (not polynomial_test(m,81*u)),(m,u)
   count+=excluded
  assert count==3674
 print('PASS:18 exacth4 sets, each3674 classes mod6561')
def matrix():
 count=0
 for d in(9,18,27,54,81,162,243,486):
  h=valuation(d);P=h+8;M=3**P
  X={k:direct_prefix_mod(k,M)*pow(10,-digits_total(k),M)%M for k in K}
  lower=1;prefix=0
  for width in range(1,d):
   prefix=append_block(prefix,lower,9*lower,width,M);lower*=10
  W=append_block(prefix,lower,1,d,M);B=pow(10,d,M)
  D=d*(lower+1)-(10**d-1)//9;A=pow(10,D,M)
  for off in range(6561):
   m=lower+off
   if off:W=(W*B+m)%M;A=A*B%M
   assert W%3**(h+5)==G(m,d,h+5)
   delta=(A-1)%M
   actual=any(witness((W-delta*x)%M,P) for x in X.values())
   assert actual==local_test(W,delta,P)==polynomial_test(m,d),(d,off)
   count+=len(K)
  print('PASS: independent matrix-prefix audit at digit length',d)
 print('PASS:',count,'independent matrix rotation comparisons')
if __name__=='__main__':
 lifting();literal();h4();matrix()
