#!/usr/bin/env python3
import json,math
from fractions import Fraction as F
from pathlib import Path
from verify_antiperiodic_thirteen import prefix

def run():
    cubes={pow(x,3,37) for x in range(1,37)};assert 10 in cubes and len(cubes)==12
    counts=[sum((m*(m+1)//2+11*a)%37 not in cubes|{0} for m in range(37)) for a in range(37)]
    assert counts==[20,25,20,23,25,25,27,28,24,28,27,25,25,23,20,25,20,21,28,28,21,23,20,27,21,27,23,23,27,21,27,20,23,21,28,28,21]
    roots=[]
    for b in (3,9):
        q=3**b;A=9*q;expected=sorted([2*q,7*q,2*q-1,7*q-1])
        found=[m for m in range(A) if m*(m+1)//2%A in (q,8*q)]
        assert found==expected;roots.append(dict(valuation=b,modulus=A,roots=found))
    tails=0
    for h in range(3,101):
        B=3
        while B*3<=h:B*=3
        assert 3*B>=h+1
        assert F(2,3)*F(1,3**(3*B))<=F(2,3**(h+2))
        assert 37*3**(B+2)<=333*3**h;tails+=1
    rows=[];checks=0
    for d in (27,54,81):
        b=3;q=3**b;A=9*q;L=10**(d-1)
        for residue in (2*q,7*q,2*q-1,7*q-1):
            m=L+(residue-L)%A
            while (m*(m+1)//2+11*d)%37 in cubes|{0}:m+=A
            w=prefix(m,A*37)
            assert w%A in (q,8*q)
            assert w%37==(m*(m+1)//2+11*d)%37 and w%37 not in cubes|{0}
            D=d*(m+1)-(10**d-1)//9;assert D%3==0
            rows.append(dict(width=d,valuation=b,endpoint=m,residue_mod243=w%A,residue_mod37=w%37));checks+=1
    data=dict(cube_subgroup=sorted(cubes),phase_noncube_counts=counts,exhaustive_roots=roots,tail_and_period_checks=tails,selected_prefixes=rows)
    Path(__file__).with_name('cubic-local-survivors-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('All37 cubic-character phases and cube subgroup: PASS')
    print('Exhaustive valuation roots: b=3 and9')
    print('Exact tail/period inequalities:',tails)
    print('Selected exact prefixes:',checks)
    print('PASS. Infinite valuation union and all-rotation assertions follow from proof.')
if __name__=='__main__':run()
