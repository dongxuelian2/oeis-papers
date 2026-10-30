#!/usr/bin/env python3
"""Bare-definition comparison of all four standalone direct formulas.
Exact comparison with the complete double-index definitions.
"""
from direct_terms import *
import sys
M=int(sys.argv[1]) if len(sys.argv)>1 else 500
ell=[L(i) for i in range(M+10)]
X=ell[M]
# Safe enclosing rectangles, deliberately independent of admissible-pair lists.
S={ell[i]-5*ell[j] for i in range(1,M+3) for j in range(1,M+3) if 0<ell[i]-5*ell[j]<X}
T={5*ell[i]-ell[j] for i in range(1,M+1) for j in range(1,M+4) if 0<5*ell[i]-ell[j]<X}
P={5*ell[i]+ell[j] for i in range(1,M) for j in range(1,M) if 5*ell[i]+ell[j]<X}
for seq,fun,values in [(191981,a191981,{0}|S),(191982,a191982,{0}|T),(191980,a191980,P),(191983,a191983,{0}|S|T)]:
    raw=sorted(values)
    for n,v in enumerate(raw,1):assert fun(n)==v,(seq,n,fun(n),v)
    print(f'PASS A{seq}: all {len(raw)} terms below L_{M}; bare double-index definition vs independent standalone direct evaluator')
