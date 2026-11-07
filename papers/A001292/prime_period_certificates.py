import sys,math
from collections import Counter

def order(a,m):
 x=a%m;k=1
 while x!=1:x=x*a%m;k+=1
 return k

def run(p):
 M=p*p;I=((1,0,0),(0,1,0),(0,0,1))
 def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%M for j in range(3)) for i in range(3))
 def power(a,n):
  r=I
  while n:
   if n&1:r=mul(r,a)
   a=mul(a,a);n//=2
  return r
 def A(d):return ((pow(10,d,M),1,0),(0,1,1),(0,0,1))
 r=order(10,M);E=math.lcm(r,M);s=E
 while s%2==0:s//=2
 while s%5==0:s//=5
 T=math.lcm(r,order(10,s));offset=1
 while pow(10,offset)% (E//s):offset+=1
 start=offset+1
 def F(d):
  L=pow(10,d-1,E);N=9*L%E;Q=power(A(d),N)
  return Q[0][0],(Q[0][1]*L+Q[0][2])%M
 assert all(power(A(d),E)==I for d in range(1,r+1))
 a,b=1,0
 for d in range(start,start+T):
  x,y=F(d);a,b=x*a%M,(x*b+y)%M
 print('p',p,'r',r,'E',E,'T',T,'start',start,'macro',a,b)
 assert a==1
 if b:T*=p
 V=0
 for d in range(1,start):
  L=10**(d-1);Q=power(A(d),9*L);V=(Q[0][0]*V+Q[0][1]*L+Q[0][2])%M
 counts={};classes={}
 for d in range(start,start+T):
  L=pow(10,d-1,E);W=V;B=pow(10,d,M)
  S=(pow(10,d,9*r)-1)//9
  good=[]
  for j in range(E):
   m=L+j;W=(B*W+m)%M
   if (d*(m+1)-S)%r==0 and W%p==0 and W:good.append(m%E)
  if good:counts[d%T]=len(good);classes[d%T]=sorted(good)
  a,b=F(d);V=(a*V+b)%M
 print('nonempty phases',len(counts),'counts',Counter(counts.values()),'total',sum(counts.values()),'first',list(classes.items())[:3])
 import json
 from pathlib import Path
 Path(__file__).with_name('prime_'+str(p)+'_classes.json').write_text(json.dumps({'p':p,'r':r,'E':E,'T':T,'classes':classes}))
 return r,E,T,classes
if __name__=='__main__':
 for p in (11,13):run(p)
