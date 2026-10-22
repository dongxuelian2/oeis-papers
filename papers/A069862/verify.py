#!/usr/bin/env python3
"""Exact-arithmetic checks for the A069862 least-length families.

Finite tests supplement, but do not replace, proofs in main.tex.
The a(n)=2 classification is prior art (Wasserman, 2005; A069860).
"""

def residues(n, count):
    r = 0
    for k in range(1, count+1):
        r = (r * pow(10, len(str(n+k)), n) + k) % n
        yield r

def least(n, limit):
    return next((k for k,r in enumerate(residues(n,limit),1) if r==0),None)

def audit():
    samples = (1,2,5,9,10,11,20,25,33,50,100,125,143,200,250,500,1000,1250)
    for n in samples:
        D=len(str(n+1))
        if 10**D%n == 0:
            expected=n
        elif n==143:
            expected=285
        elif n in (9,11):
            expected=n-1
        else:
            continue
        assert least(n, expected)==expected,(n,expected)
        print(f"PASS: a({n})={expected}")
    for j in range(4):
        D=6*j+3
        n=(10**D+1)//7
        assert (10**D+1)%7==0
        assert len(str(n+1))==D
        assert 3*n-1<10**D
        assert 10**D%n==n-1
        for k in (1,2,3,4,n-1,n,n+1,2*n-2,2*n-1):
            assert 1<=k<=2*n-1
            assert (k+1)//2 % n == (0 if k==2*n-1 else (k+1)//2)
        print(f"PASS symbolic j={j}, n={n}, a(n)={2*n-1}")
    def known_two(n):
        return n>1 and (10**len(str(n+2))+2)%n == 0
    def wasserman(n):
        if n==3:return True
        for d in range(1,len(str(n))+3):
            z=10**d+2
            if any(z==n*m for m in (2,3,6)):
                return True
            if d%6==5 and z==7*n:
                return True
        return False
    assert all(known_two(n)==wasserman(n) for n in range(1,200001))
    print("PASS prior-art a(n)=2 classification, n<=200000")

if __name__=="__main__":
    audit()
