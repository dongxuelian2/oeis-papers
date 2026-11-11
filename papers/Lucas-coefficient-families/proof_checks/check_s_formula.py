#!/usr/bin/env python3
"""Independent exact-arithmetic check for the new closed formula for A191981.
No source manuscript algorithms are imported. Python 3 standard library only.
"""
from math import isqrt
import argparse

PREFIX = [0,2,3,6,9,12,13,14,21,24,27,32,33,41,42,54,56,61,68,71,87,88,103,108,109,118]

def lucas(n):
    out=[2,1]
    for _ in range(n-1): out.append(out[-1]+out[-2])
    return out

def term(n,L):
    assert n>=1
    if n<=26: return PREFIX[n-1]
    k=(1+isqrt(8*n-41))//2
    r=n-5-k*(k-1)//2
    assert k>=7 and 1<=r<=k
    if r==1: return 3*L[k+1]
    if r in (2,3): return L[k+4]-5*L[k-r]
    if r==4: return L[k+5]-5*L[k]
    return L[k+4]-5*L[k+1-r]

def mod5term(c,n,L):
    """c=1,2,3,4 corresponds to residues 1,3,4,2 modulo 5."""
    assert c in (1,2,3,4) and n>=1
    if c==4:
        if n==1: return 2
        n-=1
    # t satisfies Q(t)<n<=Q(t+1), Q(t)=2t^2+(c-2)t.
    # Using floor of the lower-bound inverse with n-1 avoids ceil issues.
    t=(isqrt((c-2)**2+8*(n-1))-(c-2))//4
    r=n-(2*t*t+(c-2)*t)
    i=4+c+4*t
    j=c+4*t-r+1
    assert 1<=j<=i-4
    return L[i]-5*L[j]

def main(M):
    assert M>=12
    L=lucas(M+6)
    cutoff=L[M]
    # Completeness: i>=M+3 implies min positive value 3L_{i-5}>=3L_{M-2}>L_M.
    pairs=[(2,4,1)] + [(L[i]-5*L[j],i,j) for i in range(5,M+3) for j in range(1,i-3)]
    vals=[0]+sorted({v for v,i,j in pairs if 0<v<cutoff})
    for n,v in enumerate(vals,1):
        assert term(n,L)==v,(n,term(n,L),v)
    assert len(vals)==5+(M-4)*(M-3)//2,(M,len(vals))
    assert len(vals)==len([v for v,i,j in pairs if v<cutoff])+1
    for m in range(11,M+1):
        actual=sorted((v,i,j) for v,i,j in pairs if L[m-1]<=v<L[m])
        order=[(m+2,m-2),(m,m-6),(m,m-7),(m+1,m-4)]+[(m,j) for j in range(m-8,0,-1)]
        assert [(i,j) for _,i,j in actual]==order,m
        assert len(actual)==m-4
    residues=(1,3,4,2)
    for c,residue in enumerate(residues,1):
        sub=[v for v in vals if v%5==residue]
        for n,v in enumerate(sub,1):
            assert mod5term(c,n,L)==v,(c,n,v,mod5term(c,n,L))
    # Bare definition cross-check, including all index pairs and no admissibility theorem,
    # for a comfortably smaller finite range; cutoff makes missing large indices impossible.
    small=35
    Ls=lucas(small+8)
    brute=sorted({0}|{Ls[i]-5*Ls[j] for i in range(1,small+3) for j in range(1,small+3) if 0<Ls[i]-5*Ls[j]<Ls[small]})
    assert brute==[term(n,Ls) for n in range(1,len(brute)+1)]
    print(f'PASS: A191981 all {len(vals)} terms below L_{M}; {M-10} complete stable shells; all four mod-5 subsequence formulas.')
    print(f'PASS: direct unrestricted double-index definition check: {len(brute)} terms below L_{small}.')
    print('Maximum tested value:', vals[-1])

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-shell',type=int,default=500)
    main(parser.parse_args().max_shell)
