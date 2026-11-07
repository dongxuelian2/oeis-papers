#!/usr/bin/env python3
"""Independent scalar audit: does not import the primary verifier/helpers."""
from math import gcd
from pathlib import Path
import json


def step_state(state, q, modulus, n):
    w, u, v = state
    for _ in range(n):
        w, u = (q*w+u)%modulus, (u+v)%modulus
    return w,u,v


def append(w,u,n,d,modulus):
    return step_state((w,u,1), pow(10,d,modulus), modulus, n)[0]

# Direct state recurrence, on all basis states, independently proves the
# matrix identities and hence permits reducing each append count.
period_tests=0
for modulus, period, widths in ((243,243,range(1,28)), (37,111,range(1,4))):
    for d in widths:
        for basis in ((1,0,0),(0,1,0),(0,0,1)):
            assert step_state(basis,pow(10,d,modulus),modulus,period)==basis
            period_tests+=1
assert pow(10,27,243)==1 and pow(10,9,243)!=1

# Independent prefix-boundary recurrence, maintaining two starting values
# to certify the complete affine cycle rather than one orbit alone.
table={}; v0=0; v1=1; boundary=[]
for d in range(1,28):
    L=pow(10,d-1,243)
    residues=[]
    for m in range(243):
        w=append(v0,L,(m-L+1)%243,d,243)
        D=(d*(m+1)-(pow(10,d,243)-1)//9)%27
        if w in (27,216) and D==0: residues.append(m)
    table[d%27]=residues
    v0=append(v0,L,(9*L)%243,d,243)
    v1=append(v1,L,(9*L)%243,d,243)
    boundary.append((d,v0,v1))
assert (v0,v1)==(0,1)
certificate=json.loads(Path(__file__).with_name('fixed-valuation-cubic-certificate.json').read_text())
assert {str(k):v for k,v in table.items()}==certificate['complete_table']
assert table[0]==sorted([2*27,7*27,2*27-1,7*27-1])

# Exact cubic-character counts, without using either source verifier.
cubes={x**3%37 for x in range(1,37)}
noncubes=set(range(1,37))-cubes
assert len(cubes)==12 and len(noncubes)==24 and 10 in cubes
counts=[sum((x*(x+1)//2+11*a)%37 in noncubes for x in range(37)) for a in range(37)]
assert counts==[20,25,20,23,25,25,27,28,24,28,27,25,25,23,20,25,20,21,28,28,21,23,20,27,21,27,23,23,27,21,27,20,23,21,28,28,21]

# Complete combined phase check: lcm(27,111)=999 widths. The modulo-37
# formula is checked at all compatible endpoint phases modulo 111.
v=0; formula_checks=0; class_checks=0
for d in range(1,1000):
    L=pow(10,d-1,111)
    for m in range(111):
        if d%3==1 and m%3!=0: continue
        if d%3==2: continue
        w=append(v,L,(m-L+1)%111,d,37)
        formula=(4*m+33*((d-1)//3))%37 if d%3==1 else (m*(m+1)//2+11*d)%37
        assert w==formula,(d,m,w,formula)
        formula_checks+=1
    local=table[d%27]
    crt_count=0
    for r in local:
        for x in range(37):
            # Unique CRT representative modulo 243*37.
            m=r+243*((x-r)*pow(243,-1,37)%37)
            assert m%243==r and m%37==x and 0<=m<8991
            value=(4*m+33*((d-1)//3))%37 if d%3==1 else (m*(m+1)//2+11*d)%37
            crt_count+=value in noncubes
    wanted=48 if d%3==1 else len(local)*counts[d%37]
    if d%3==2: wanted=0
    assert crt_count==wanted,(d,crt_count,wanted)
    class_checks+=1
    v=append(v,L,9*L%111,d,37)

# Once v3(Delta)>=b, the two unit tests force Delta/3^b = 0 mod9.
# This is independent of b, and proves the normalized finite part of the
# general three-cut argument; v3(Delta)<b is excluded by cut 1.
for u in (1,8):
    good=[a for a in range(9) if (u-a)%9 in (1,8) and (u-3*a)%9 in (1,8)]
    assert good==[0]

print('PASS: independent scalar period checks:',period_tests)
print('PASS: all 6561 local cells and complete width-27 affine boundary cycle')
print('PASS: general-b normalized three-cut congruence and old b=3 overlap')
print('PASS: all 37 character counts and all 999 combined width count phases')
print('PASS: independent modulo-37 prefix phase checks:',formula_checks)
