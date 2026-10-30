#!/usr/bin/env python3
"""Exact, finite certificate plus extended checks. Research only; no repo mutation."""
from math import isqrt
from pathlib import Path
NMAX=1000
L=[2,1]
for _ in range(NMAX+10): L.append(L[-1]+L[-2])

def ceil_sqrt(n):
    s=isqrt(n)
    return s+(s*s<n)

def ceil_div(a,b):return -(-a//b)

Tprefix=[0,1,2,4,6,8,9,11,12,13,14,16,17,19]
Pprefix=[6,8,9,12,16,18,19,21,22,23,24,26,27,31,33,34,36,38,39,42,44,46,49,52,53,56,58,59,62,64,66,67,73,81,82,84,91,93,94,96,97,101,102,108,111,119,128,131,137,138,143,146,148,149,152,156,158,163,166,174,178,192,204,213,214,219,221,234,236,238,239,242,246,253,254,264,268,282,289,311]

def a982(n):
    if n<=14:return Tprefix[n-1]
    m=ceil_div(ceil_sqrt(8*n+57)-7,2)
    r=n-(m*m+5*m-8)//2
    assert 1<=r<=m+3
    if r==1:return 2*L[m+1]
    if r==2:return 5*L[m]-L[m+1]
    if r==3:return 5*L[m+1]-L[m+3]
    return 5*L[m]-L[m+4-r]

def a980(n):
    if n<=80:return Pprefix[n-1]
    m=ceil_div(3+ceil_sqrt(4*n+41),2)
    r=n-m*m+5*m+4
    assert 1<=r<=2*m-4
    if r<=m-9:return 5*L[r]+L[m]
    if r==m-8:return 5*L[m-5]+L[m-1]
    if r==m-7:return 5*L[m-8]+L[m]
    if r==m-6:return 5*L[m-4]+L[m-2]
    if r==m-5:return 5*L[m-7]+L[m]
    if r<=2*m-10:return 5*L[m-3]+L[r-m+5]
    i,j={2*m-9:(m-6,m),2*m-8:(m-3,m-4),2*m-7:(m-4,m-1),2*m-6:(m-3,m-3),2*m-5:(m-5,m),2*m-4:(m-3,m-2)}[r]
    return 5*L[i]+L[j]

# Each dictionary value is a homogeneous fixed-shift Lucas expression.
# Hence it satisfies h(m+2)=h(m+1)+h(m), so positive at two consecutive
# bases proves positive at ALL later m, independently of the extended tests.
def t_certificate(m):
    A=2*L[m+1]; B=5*L[m]-L[m+1]; C=5*L[m+1]-L[m+3]
    return {
      'exclude i>=m+4':2*L[m+2]-5*L[m],
      'i=m next j below lower':5*L[m-1]-(5*L[m]-L[m+2]),
      'i=m+1 higher j below lower':5*L[m-1]-(5*L[m+1]-L[m+4]),
      'i=m+1 lower j above upper':5*L[m+1]-L[m+2]-5*L[m],
      'i=m+2 maximum j below lower':5*L[m-1]-(5*L[m+2]-L[m+5]),
      'i=m+2 next j above upper':5*L[m+2]-L[m+4]-5*L[m],
      'i=m+3 next j above upper':5*L[m+3]-L[m+5]-5*L[m],
      'first > lower':A-5*L[m-1],
      'second > first':B-A,
      'third > second':C-B,
      'row tail > third':4*L[m]-C,
    }

def p_certificate(m):
    p=lambda i,j:5*L[m+i]+L[m+j]
    return {
      'exclude i>=m-2':5*L[m-2]-L[m+1],
      'j=m last i in':L[m-1]-5*L[m-5],
      'j=m next i out':5*L[m-4]-L[m-1],
      'i=m-3 lower':5*L[m-3]-L[m],
      'i=m-3 last j in':L[m+1]-p(-3,-2),
      'i=m-3 next j out':p(-3,-1)-L[m+1],
      'interior i<=m-6 out':L[m]-p(-6,-1),
      'i=m-5 lower j out':L[m]-p(-5,-2),
      'i=m-5 j=m-1 lower':p(-5,-1)-L[m],
      'i=m-5 j=m-1 upper':L[m+1]-p(-5,-1),
      'i=m-4 lower j out':L[m]-p(-4,-3),
      'i=m-4 j=m-2 lower':p(-4,-2)-L[m],
      'i=m-4 j=m-1 upper':L[m+1]-p(-4,-1),
      'order 1':p(-5,-1)-p(-9,0),
      'order 2':p(-8,0)-p(-5,-1),
      'order 3':p(-4,-2)-p(-8,0),
      'order 4':p(-7,0)-p(-4,-2),
      'order 5 homogeneous':5*L[m-3]-p(-7,0),
      'order 6':p(-6,0)-p(-3,-5),
      'order 7':p(-3,-4)-p(-6,0),
      'order 8':p(-4,-1)-p(-3,-4),
      'order 9':p(-3,-3)-p(-4,-1),
      'order 10':p(-5,0)-p(-3,-3),
      'order 11':p(-3,-2)-p(-5,0),
    }

def t_template(m):
    return [(m+3,m+6),(m,m+1),(m+1,m+3)]+[(m,j) for j in range(m,0,-1)]
def p_template(m):
    return ([(i,m) for i in range(1,m-8)]
       +[(m-5,m-1),(m-8,m),(m-4,m-2),(m-7,m)]
       +[(m-3,j) for j in range(1,m-4)]
       +[(m-6,m),(m-3,m-4),(m-4,m-1),(m-3,m-3),(m-5,m),(m-3,m-2)])

lines=[]
def report(s):print(s);lines.append(s)
for name,cert,base in [('T',t_certificate,4),('P',p_certificate,12)]:
    a,b=cert(base),cert(base+1)
    assert all(v>0 for v in a.values()) and all(v>0 for v in b.values())
    report(f'{name} fixed-shift recurrence certificate (bases {base},{base+1}):')
    for key in a: report(f'  {key}: {a[key]}, {b[key]}')
    # Supplemental coding check; theorem uses only bases and recurrence.
    for m in range(base,NMAX):
        c,d,e=cert(m),cert(m+1),cert(m+2)
        assert all(e[k]==c[k]+d[k] for k in c)
        assert all(v>0 for v in c.values())

# Admissible T-row endpoints: two initial identities/strict inequalities
# propagate by recurrence and prove the positive index region.
for i in (2,3):
    assert 5*L[i]-L[i+3]==2*L[i-2]>0
    assert L[i+4]-5*L[i]==3*L[i-1]>0
assert [j for j in range(1,6) if 5*L[1]-L[j]>0]==[1,2,3]

# Prefix searches have proved finite enclosing rectangles:
# T<=20: i<=6, j<=i+3; P<322: i<=8,j<=11.
assert Tprefix==[0]+sorted({5*L[i]-L[j] for i in range(1,7) for j in range(1,i+4) if 0<5*L[i]-L[j]<=20})
assert Pprefix==sorted({5*L[i]+L[j] for i in range(1,9) for j in range(1,12) if 5*L[i]+L[j]<322})
report('Finite prefixes verified: T 14 entries including zero; P 80 entries.')

# Brute-force comparison, not the proof of completeness.
M=300
rawT=sorted({5*L[i]-L[j] for i in range(1,M+4) for j in range(1,i+4) if 0<5*L[i]-L[j]<=5*L[M]})
rawP=sorted({5*L[i]+L[j] for i in range(1,M-2) for j in range(1,M+1) if 5*L[i]+L[j]<L[M+1]})
assert [0]+rawT==[a982(n) for n in range(1,len(rawT)+2)]
assert rawP==[a980(n) for n in range(1,len(rawP)+1)]
report(f'Exact brute-force matched A191982 first {len(rawT)+1} entries through 5L_{M}.')
report(f'Exact brute-force matched A191980 first {len(rawP)} entries below L_{M+1}.')
for m in range(4,NMAX):
    v=[5*L[i]-L[j] for i,j in t_template(m)]
    assert len(v)==m+3 and v==sorted(set(v))
    assert 5*L[m-1]<v[0]<v[-1]<=5*L[m]
for m in range(12,NMAX):
    v=[5*L[i]+L[j] for i,j in p_template(m)]
    assert len(v)==2*m-4 and v==sorted(set(v))
    assert L[m]<=v[0]<v[-1]<L[m+1]
report(f'T/P ordered templates and enclosing shells checked through m={NMAX-1}.')
# Results printed above.
