"""Independent exact certificate for A191983 shell/nth formula; no repository edits.
Python 3, standard library. Call: python verify_union.py [last_shell=300].
The nth formula has fixed case count; the verifier itself enumerates for checking only.
"""
from math import isqrt
import sys
M=int(sys.argv[1]) if len(sys.argv)>1 else 300
L=[2,1]
for _ in range(M+15):L.append(L[-1]+L[-2])
PREFIX=(0,1,2,3,4,6,8,9,11,12,13,14,16,17,19,21,22,24,26,27,28,31,32,33,34,36,37,41,42,43,44,48,51,52,54,56,58,61,68,69,71,72,79,83,86,87,88,89,94,98,103,108,109,112,116,118)
def S(i,j):return L[i]-5*L[j]
def T(i,j):return 5*L[i]-L[j]
def fixed(m):
 return (T(m+1,m+4),T(m-2,m-1),S(m+1,m-6),S(m+2,m-3),S(m+1,m-7),T(m-1,m+1),S(m+1,m-8),T(m-2,m-2))
def a983(n):
 assert n>=1
 if n<=56:return PREFIX[n-1]
 m=3+isqrt(n-8)
 r=n-((m-3)**2+7)
 if r<=m-4:return T(m-3,m-3-r)
 if r<=m+4:return fixed(m)[r-(m-4)-1]
 return S(m+1,2*m-4-r)
# Endpoint certificate: every expression below is a fixed-shift Lucas-linear
# combination. Its positivity at both 10 and11 proves positivity for every m>=10.
def cert(m):
 lo,hi=L[m],L[m+1]
 d={
 'exclude lower i':lo-5*L[m-4],
 'exclude higher i':2*L[m]-hi,
 'row m-3 lower':T(m-3,m-4)-lo,
 'row m-3 next below':lo-T(m-3,m-3),
 'row m-3 upper (stronger)':hi-5*L[m-3],
 'row m-2 lower':T(m-2,m-1)-lo,
 'row m-2 upper':hi-T(m-2,m-2),
 'row m-2 prior above':T(m-2,m-3)-hi,
 'row m-2 next below':lo-T(m-2,m),
 'row m-1 lower':T(m-1,m+1)-lo,
 'row m-1 upper':hi-T(m-1,m+1),
 'row m-1 prior above':T(m-1,m)-hi,
 'row m-1 next below':lo-T(m-1,m+2),
 'row m gap above':T(m,m+2)-hi,
 'row m gap below':lo-T(m,m+3),
 'row m+1 lower':T(m+1,m+4)-lo,
 'row m+1 upper':hi-T(m+1,m+4),
 'row m+1 prior above':T(m+1,m+3)-hi,
 'row m+1 next below':lo-T(m+1,m+5),
 'run to fixed stronger':fixed(m)[0]-5*L[m-3],
 'fixed to final run':S(m+1,m-9)-fixed(m)[-1],
 }
 for k,(a,b) in enumerate(zip(fixed(m),fixed(m)[1:]),1):d[f'fixed order {k}']=b-a
 return d
print('Frozen source head: e6f972cd61e73c25e0b965e5fa8c43ae6f950edd')
c10,c11=cert(10),cert(11)
for k in c10:
 print('CERT',k,c10[k],c11[k]); assert min(c10[k],c11[k])>0
for m in range(10,M+1):
 assert S(m+3,m-1)==T(m-3,m-7)
 assert S(m+1,m-5)==T(m-3,m-9)
 assert all(v>0 for v in cert(m).values())
# Exhaustive representations below L_(M+1); known row minima give completeness.
cut=L[M+1]
s={S(4,1)}
for i in range(5,M+4):
 for j in range(1,i-3):
  x=S(i,j)
  if x<cut:s.add(x)
t=set()
for i in range(1,M+2):
 for j in range(1,(3 if i==1 else i+3)+1):
  x=T(i,j)
  if x<cut:t.add(x)
u=sorted({0}|s|t)
assert tuple(u[:56])==PREFIX
assert len([x for x in u if x<L[10]])==56
assert len(u)==(M-2)**2+7,(M,len(u))
for n,x in enumerate(u,1):
 assert a983(n)==x,(n,x,a983(n))
print('PASS all',len(u),'terms below L_'+str(M+1),'exact arithmetic; shells 10..'+str(M))
