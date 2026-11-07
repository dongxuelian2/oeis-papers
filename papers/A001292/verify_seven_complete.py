#!/usr/bin/env python3
"""Complete classification of uniform valuation-one at7, plus CRT coverage."""
import sys,json
from pathlib import Path
from fractions import Fraction
from verify_a001292 import append_block,digits_total,direct_prefix_mod
import verify_seven_family
X={direct_prefix_mod(k,7)*pow(10,-digits_total(k),7)%7 for k in range(13)}
assert X==set(range(7))
expected={1:{42,84,126,168,210,252},5:{12,54,96,138,180,222},9:{x for x in range(294) if x%14==2 and x%98!=30}}
v=0;l=1;table={}
for d in range(1,85):
 if d>=43:
  good=[];w=v;B=pow(10,d,49)
  for j in range(294):
   m=l+j;w=(B*w+m)%49
   if digits_total(m)%42==0 and w%7==0 and w:good.append(m%294)
  assert set(good)==expected.get(d%42,set()),(d,good)
  if good:table[d%42]=sorted(good)
 v=append_block(v,l,9*l,d,49);l*=10
w=D=0;prefix=[0];length=[0];checked=0
for m in range(1,1000):
 d=len(str(m));w=(w*10**d+m)%49;D+=d;prefix.append(w);length.append(D)
 delta=(pow(10,D,49)-1)%49
 actual=all((r:=(pow(10,length[k],49)*w-delta*prefix[k])%49)%7==0 and r!=0 for k in range(m))
 predicted=m%294 in expected.get(d%42,set())
 assert actual==predicted,(m,actual,predicted)
 checked+=m
coverage={}
for h,a,b in [(1,131,243),(2,133,243),(3,3673,6561),(4,3674,6561)]:
 q=Fraction(a,b);combined=1-(1-q)*Fraction(46,49)
 count=a*98+(b-a)*6
 assert Fraction(count,b*98)==combined
 coverage[h]={'three_adic':str(q),'combined':str(combined),'increment':str(combined-q),'combined_decimal':float(combined)}
Path(__file__).with_name('seven_complete_certificate.json').write_text(json.dumps({'classes_mod294':table,'coverage':coverage},indent=2)+'\n')
print('PASS: complete42-phase table, all7 normalized-prefix residues,',checked,'literal rotations')
print(json.dumps(coverage,indent=2))
