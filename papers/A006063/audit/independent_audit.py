"""AI-assisted independent audit; no repository verifier is imported or executed.
Optional dependency: SymPy (tested 1.14.0). Run without -O.
Ported from the frozen-base audit; reads the current adjacent certificate files.
"""
import json, hashlib
from pathlib import Path
from collections import deque
from functools import lru_cache
import sympy as sp
P=Path(__file__).resolve().parent.parent; C=P/'certificates'
CUBES={k**3 for k in range(2,100)}
def valid(p):
 n=len(p); assert sorted(p)==list(range(1,n+1)); assert all(i+x in CUBES for i,x in enumerate(p,1)); return p
def read(name): return json.loads((C/name).read_text())
seeds={}; blocks=0
for line in (C/'finite_56_cubic_order_shapes.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'): continue
 n,k,o=line.split('|'); n=int(n); k=list(map(int,k.split(','))); o=list(map(int,o.split(',')))
 assert sorted(o)==list(range(1,len(k)+1))
 M=sp.Matrix([[int(i<j)+int(o.index(i+1)<o.index(j+1))+int(i==j) for i in range(len(k))] for j in range(len(k))])
 assert M.det(method='domain-ge')==1
 L=list(M.inv(method='DM')*sp.Matrix([r**3-1 for r in k])); assert all(x.is_Integer and x>0 for x in L); assert sum(L)==n
 p=[]
 for l,r in zip(L,k): p += [r**3-i for i in range(len(p)+1,len(p)+int(l)+1)]
 seeds[n]=valid(p); blocks+=len(L)
assert len(seeds)==56 and blocks==784
print('PASS 56 determinants independently using SymPy domain-ge determinant / DM inverse; 784 positive integral lengths and full bijections')
# Direct recomputation of prefix sums from each family's lengths and order;
# notably, do not assume the supplied nominal sums.
templates={}
def family(L,O):
 assert min(L)>=0 and sorted(O)==list(range(1,len(L)+1))
 p=[]
 for j,l in enumerate(L):
  c=1+sum(L[:j])+sum(L[i-1] for i in O[:O.index(j+1)])+l
  p += [c-i for i in range(len(p)+1,len(p)+l+1)]
 valid(p); assert len(p) not in templates; templates[len(p)]=p
for U,V in [(64,125),(125,216),(216,343)]:
 a,b=2*U-V-1,2*V-3*U+1; family([a,b,a,b],[3,4,1,2])
for X in [27,8]:
 Y,Z=64,125; a,b,c=2*Y-Z-1,X+2*Z-4*Y+1,Y-X; family([a,b,c,a,c],[4,2,5,1,3])
for X,W in [(8,64),(27,64),(8,27)]:
 Y,Z=64,125; a=2*Y-Z-1; b=X-2*a-1; c=W+2*a-2*X+1; d=Y+X-W-2*a-1; family([a,b,c,d,a,d],[5,2,3,6,1,4])
for X in [7,8]:
 for T in [2*X-7,27]:
  for Q in [121-2*T+2*X,125]:
   u,v,w,z,h=X-7,T-2*X+7,X+27-T,Q+2*T-2*X-121,X+152-T-Q
   family([3,u,v,w,3,w,z,h,3,27,3,h],[11,2,3,6,9,4,7,12,5,10,1,8])
for a,b in [(0,0),(0,1),(1,1)]:
 for t in [0,7+4*b+2*a]:
  family([2*b,7-a-4*b-a*b,a,a*b,13+4*b,a,23-4*b-a,13+4*b,48-a-45*b+a*b,2*b,b*(39-a),t,30+a-t,13+4*b,91+a-t],[10,4,6,2,8,3,11,1,9,14,7,12,15,5,13])
for a,b in [(0,0),(1,0),(1,1)]:
 family([7,12*a,159-24*a-99*b,14*b,28*b,63*b,10+24*a-6*b,8*b,159-24*a-107*b,10+24*a+93*b],[1,2,8,5,6,9,4,10,3,7])
assert len(templates)==25 and not templates.keys()&seeds.keys(); seeds.update(templates)
print('PASS six templates yield exactly 25 disjoint seed lengths via direct prefix sums')
def peel(n):
 V=set(range(1,n+1)); assignments={}
 while V:
  for i in sorted(V):
   N={j for j in V if i+j in CUBES}
   if len(N)==1:
    j=N.pop(); assignments[i]=j; assignments[j]=i; V-={i,j}; break
  else: break
 return assignments,V
for n in [173,174,175]:
 a,V=peel(n)
 if n<175:
  assert not V; p=valid([a[i] for i in range(1,n+1)]); seeds[n]=p
 else:
  v=sorted(V); assert v==[4,11,16,23,41,48,102,114,168,175]
  @lru_cache(None)
  def permanent(mask):
   i=mask.bit_count()
   if i==len(v): return 1
   return sum(permanent(mask|1<<j) for j in range(len(v)) if not mask>>j&1 and v[i]+v[j] in CUBES)
  assert permanent(0)==3
print('PASS independent greedy forced-neighbor peeling: P173=P174=1, residual exact permanent P175=3')
known={0:[]}; direct=set(seeds)
for n in range(1,365):
 if n in seeds: known[n]=seeds[n]; continue
 for m,p in list(known.items()):
  if m<n and m+n+1 in CUBES:
   known[n]=valid(p+[m+n+1-i for i in range(m+1,n+1)]); break
assert all(n in known for n in range(173,365)); assert len([n for n in known if 0<n<173])==48
print('PASS independent constructive reflection closure: 48 below173 and all192 lengths173..364')
data=read('exact_classification_below_173.json'); yes={r['n']:valid(r['p']) for r in data['positive']}; no={r['n']:r['S'] for r in data['negative']}
assert len(yes)==48 and len(no)==124 and set(yes).isdisjoint(no) and set(yes)|set(no)==set(range(1,173)); assert set(yes)=={n for n in known if 0<n<173}
for n,S in no.items():
 assert len(set(S))==len(S) and set(S)<=set(range(1,n+1))
 N={j for j in range(1,n+1) if any(i+j in CUBES for i in S)}; assert len(N)<len(S)
print('PASS all48 positive and124 Hall-negative records, with exhaustive neighbor scans')
def acyclic(p):
 n=len(p); adj=[[j for j in range(n) if i!=j and i+1+p[j] in CUBES] for i in range(n)]; deg=[0]*n
 for row in adj:
  for j in row: deg[j]+=1
 todo=deque(i for i in range(n) if deg[i]==0); removed=0
 while todo:
  i=todo.popleft(); removed+=1
  for j in adj[i]:
   deg[j]-=1
   if deg[j]==0: todo.append(j)
 return removed==n
second=read('second_solutions.json'); third=read('third_solutions.json'); archive=read('base_permutations.json')
E={112,115,116,117,119,124,125,126,127,128,129,130,133}
assert {n for n,p in yes.items() if not acyclic(p)}==E
assert all(acyclic(valid(archive[i])) for i in [0,1])
def switched(p,cy):
 assert len(cy)>1 and len(set(cy))==len(cy) and set(cy)<=set(range(1,len(p)+1))
 q=p.copy()
 for i,j in zip(cy,cy[1:]+cy[:1]): q[i-1]=p[j-1]
 valid(q); assert q!=p; return q
assert {r['n'] for r in second['small']}==E
for r in second['small']: switched(yes[r['n']],r['cycle'])
for category,expected in [('tail',set(range(175,365))),('exceptional',{554,555})]:
 s={r['n']:r['cycle'] for r in second[category]}; t={r['n']:r['cycle'] for r in third[category]}; assert set(s)==set(t)==expected
 for n in s:
  if category=='tail': p=valid(archive[n-173])
  else:
   m=728-n; p=valid(archive[m-173]+[729-i for i in range(m+1,n+1)])
  assert switched(p,s[n])!=switched(p,t[n])
print('PASS multiplicity: independent Kahn DAG test, 13 small alternating cycles, two distinct alternatives at all190 base sizes plus554,555')
# Independent finite parity closure using pointwise shortest-path DP, no interval machinery.
for seed,cap,target,depth,count in [(7,100001,69603,13,2961),(26,303412,228028,12,7047)]:
 parity=seed%2; T=(cap-parity)//2; ds=[(k**3-1-2*parity)//2 for k in range(3,100,2) if k**3<=2*cap]; dist=[10**9]*(T+1); dist[(seed-parity)//2]=0
 for t in range((seed-parity)//2,T+1):
  if dist[t]>=depth: continue
  for d in ds:
   u=d-t
   if t<u<=T: dist[u]=min(dist[u],dist[t]+1)
 assert all(dist[t]<=depth for t in range((target-parity)//2,T+1))
 starts=[t for t in range(T+1) if dist[t]<=depth and (t==0 or dist[t-1]>depth)]
 assert len(starts)==count and 2*starts[-1]+parity==target
 print(f'PASS independent pointwise parity shortest-path DP seed{seed}: {count} intervals at depth{depth}, final [{target},{cap}]')
print('ALL INDEPENDENT FINITE CHECKS PASS')
