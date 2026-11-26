#!/usr/bin/env python3
"""Exact whole-block hypotheses plus selected-cut tests, without factoring."""
import json,math
from pathlib import Path

ENDPOINTS=(5040,5067,5094,5121,5175,5202,5229,5283,5337,5391)

def jacobi(a,n):
    assert n>0 and n%2
    a%=n;sign=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5):sign=-sign
        a,n=n,a
        if a%4==n%4==3:sign=-sign
        a%=n
    return sign if n==1 else 0

def v3(n):
    assert n
    a=0
    while n%3==0:n//=3;a+=1
    return a,n

def run():
    try:
        from sympy import jacobi_symbol
    except ImportError:
        jacobi_symbol=None
    W=[0];D=[0]
    for m in range(1,max(ENDPOINTS)+1):
        d=len(str(m));W.append(W[-1]*10**d+m);D.append(D[-1]+d)
    records=[];cuts_checked=0;library_checks=0
    for m in ENDPOINTS:
        a=2+v3(D[m])[0];Delta=10**D[m]-1;M=Delta//3**a
        v,z=v3(W[m]);J=jacobi(z,M)
        assert a>=3 and v==2 and z%3==1 and J==-1
        assert Delta%3**a==0 and M%3 and math.gcd(W[m],Delta)==9
        assert jacobi(10,M)==1
        if jacobi_symbol is not None:
            assert int(jacobi_symbol(z,M))==J;library_checks+=1
        tested=sorted(set((0,1,2,m//2,m-1)))
        for k in tested:
            R=10**D[k]*W[m]-Delta*W[k]
            b,u=v3(R)
            assert b==2 and u%3==1
            assert jacobi(u,M)==-1
            cuts_checked+=1
        records.append(dict(endpoint=m,digits=D[m],v3_delta=a,v3_prefix=v,normalized_unit_mod9=z%9,jacobi=J,common_gcd=9,selected_cuts=tested))
    data=dict(certificates=records,rotations_covered_by_theorem=sum(ENDPOINTS),selected_cuts_checked=cuts_checked,sympy_jacobi_cross_checks=library_checks)
    Path(__file__).with_name('cyclic-jacobi-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Exact endpoint certificates:',len(records))
    print('Rotations covered by the theorem:',sum(ENDPOINTS))
    print('Selected cuts checked:',cuts_checked)
    print('Optional SymPy Jacobi cross-checks:',library_checks)
    print('PASS. A sufficient whole-block certificate, not a proof for every endpoint.')

if __name__=='__main__':run()
