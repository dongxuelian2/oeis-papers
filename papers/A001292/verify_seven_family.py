#!/usr/bin/env python3
"""Exact finite certificates for a new global 7-adic whole-block exclusion."""
import json
from pathlib import Path
M=49
I=((1,0,0),(0,1,0),(0,0,1))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%M for j in range(3)) for i in range(3))
def power(a,n):
 r=I
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n//=2
 return r
def A(d):return ((pow(10,d,M),1,0),(0,1,1),(0,0,1))
def block(v,d):
 l=10**(d-1);q=power(A(d),9*l)
 return (q[0][0]*v+q[0][1]*l+q[0][2])%M
# All append matrices have period dividing294. Width and block endpoints
# repeat every42: 10^42=1 mod147, while positive powers are0 mod2.
assert pow(10,42,147)==1
for d in range(1,43):assert power(A(d),294)==I
pairs=[]
for d in range(2,44):
 b=block(0,d);a=(block(1,d)-b)%M;pairs.append((a,b))
for initial in (0,1):
 v=initial
 for a,b in pairs:v=(a*v+b)%M
 assert v==initial
# Hence V_(d+42)=V_d for all d>=1. Recover the eight-digit boundary.
v=0
for d in range(1,9):v=block(v,d)
assert v==2 and pow(10,8,294)==16 and pow(10,9,49)==13
# Recurrence on d=9 mod42: W(next)=13W+next mod49.
# W is periodic98 within this interval; start m=16 mod294 at V=2.
assert power(A(9),98)==I
w=v;res={}
for m in range(16,16+98):
 w=(13*w+m)%49;res[m%98]=w
for t in range(7):assert res[2+14*t]==7*((t+5)%7)
# Digit count D=d(m+1)-(10^d-1)/9; d=9 mod42 gives D=9m-18 mod42.
assert (10**9-1)//9%42==27
assert pow(10,42,189)==1 # repunit periodic42 mod42, using parity separately
# Output the explicit finite affine certificate.
certificate={'modulus':49,'append_matrix_period':294,'digit_width_period':42,
 'affine_maps_d_2_through_43':pairs,'macro_map':[1,0],
 'V_8':2,'start_m_mod_294':16,'B':13,
 'prefix_values_m_2_plus_14t':[res[2+14*t] for t in range(7)]}
Path(__file__).with_name('seven_family_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
# Independent literal appending, using no matrix, checks the finite maps.
for d in range(1,43):
 b=pow(10,d,M)
 for start in (0,1,16,48):
  for length in (1,13,42,98,294,295):
   w=0
   for x in range(start,start+length):w=(b*w+x)%M
   q=power(A(d),length)
   assert w==(q[0][1]*start+q[0][2])%M
print('PASS: 42 append matrices, complete affine period certificate, 7 prefix classes, 1008 independent literal checks')
# Independent existing matrix algorithm at six widths, 294 endpoints each.
import sys
from verify_a001292 import append_block,digits_total
v=0;l=1;count=0
for d in range(1,220):
 if d%42==9:
  for off in range(294):
   m=l+off;w=append_block(v,l,off+1,d,49)
   if m%14==2:
    t=((m-2)//14)%7
    assert w==7*((t+5)%7)
    assert digits_total(m)%42==0
    if t!=2:
     for k in (0,1,2,7,19,10006,m-1):
      # Shift vanishes, so every normalized rotation is the same nonzero multiple of7.
      assert pow(10,digits_total(k),49)*w%7==0
      assert pow(10,digits_total(k),49)*w%49!=0
     count+=1
 v=append_block(v,l,9*l,d,49);l*=10
print('PASS:',count,'global-excluded endpoints over six independent digit widths')
