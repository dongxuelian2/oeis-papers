#!/usr/bin/env python3
"""Direct all-index formulas for OEIS A191980-A191983; direct all-index evaluator.
No rank oracle, minimization, candidate search, or previous-term dependency.
Usage: python evaluate.py 191981 27
The standard Lucas function uses exact fast doubling, rather than floating Binet.
"""
from math import isqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def _fib_pair(n):
    if n==0:return 0,1
    a,b=_fib_pair(n//2)
    c,d=a*(2*b-a),a*a+b*b
    return (d,c+d) if n%2 else (c,d)

def L(n):
    assert n>=0
    a,b=_fib_pair(n)
    return 2*b-a

S_PREFIX=(0,2,3,6,9,12,13,14,21,24,27,32,33,41,42,54,56,61,68,71,87,88,103,108,109,118)
T_PREFIX=(0,1,2,4,6,8,9,11,12,13,14,16,17,19)
P_PREFIX=(6,8,9,12,16,18,19,21,22,23,24,26,27,31,33,34,36,38,39,42,44,46,49,52,53,56,58,59,62,64,66,67,73,81,82,84,91,93,94,96,97,101,102,108,111,119,128,131,137,138,143,146,148,149,152,156,158,163,166,174,178,192,204,213,214,219,221,234,236,238,239,242,246,253,254,264,268,282,289,311)
U_PREFIX=(0,1,2,3,4,6,8,9,11,12,13,14,16,17,19,21,22,24,26,27,28,31,32,33,34,36,37,41,42,43,44,48,51,52,54,56,58,61,68,69,71,72,79,83,86,87,88,89,94,98,103,108,109,112,116,118)

def a191981(n):
    if n<1:raise ValueError('OEIS offset is 1')
    if n<=26:return S_PREFIX[n-1]
    k=(1+isqrt(8*n-41))//2
    r=n-5-k*(k-1)//2
    if r==1:return 3*L(k+1)
    if r in (2,3):return L(k+4)-5*L(k-r)
    if r==4:return L(k+5)-5*L(k)
    return L(k+4)-5*L(k+1-r)

def a191982(n):
    if n<1:raise ValueError('OEIS offset is 1')
    if n<=14:return T_PREFIX[n-1]
    m=(isqrt(8*n+49)-5)//2
    r=n-(m*m+5*m-8)//2
    if r==1:return 2*L(m+1)
    if r==2:return 5*L(m)-L(m+1)
    if r==3:return 5*L(m+1)-L(m+3)
    return 5*L(m)-L(m+4-r)

def a191980(n):
    if n<1:raise ValueError('OEIS offset is 1')
    if n<=80:return P_PREFIX[n-1]
    m=(5+isqrt(4*n+37))//2
    r=n-m*m+5*m+4
    if r<=m-9:return 5*L(r)+L(m)
    if r==m-8:return 5*L(m-5)+L(m-1)
    if r==m-7:return 5*L(m-8)+L(m)
    if r==m-6:return 5*L(m-4)+L(m-2)
    if r==m-5:return 5*L(m-7)+L(m)
    if r<=2*m-10:return 5*L(m-3)+L(r-m+5)
    i,j={2*m-9:(m-6,m),2*m-8:(m-3,m-4),2*m-7:(m-4,m-1),2*m-6:(m-3,m-3),2*m-5:(m-5,m),2*m-4:(m-3,m-2)}[r]
    return 5*L(i)+L(j)

def a191983(n):
    if n<1:raise ValueError('OEIS offset is 1')
    if n<=56:return U_PREFIX[n-1]
    m=3+isqrt(n-8)
    r=n-((m-3)**2+7)
    if r<=m-4:return 5*L(m-3)-L(m-3-r)
    if r==m-3:return 2*L(m-1)
    if r==m-2:return 5*L(m-2)-L(m-1)
    if r==m-1:return L(m+1)-5*L(m-6)
    if r==m:return L(m+2)-5*L(m-3)
    if r==m+1:return L(m+1)-5*L(m-7)
    if r==m+2:return 5*L(m-1)-L(m+1)
    if r==m+3:return L(m+1)-5*L(m-8)
    if r==m+4:return 4*L(m-2)
    return L(m+1)-5*L(2*m-4-r)

if __name__=='__main__':
    import sys
    seq,n=map(int,sys.argv[1:3])
    print({191980:a191980,191981:a191981,191982:a191982,191983:a191983}[seq](n))
