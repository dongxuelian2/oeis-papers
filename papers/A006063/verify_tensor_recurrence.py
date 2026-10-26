#!/usr/bin/env python3
"""Exact tests for generalized tensorized power-divisor reflection.

No matching solver or permanent routine is used. Tests 2 independent
tensor fibers, 2 distinct suffix cubes, and the 362-cycle amplification.
"""
import json
from pathlib import Path
from construct_linear import make
from verify_362 import read_and_verify

HERE=Path(__file__).resolve().parent
EARLY=HERE/"certificates"/"exact_classification_below_173.json"


def known_perm(n, seed362):
    if n==0:
        return []
    if n==362:
        return seed362[1:]
    if n>=173:
        return make(n)
    data=json.loads(EARLY.read_text(encoding="utf-8"))
    for row in data["positive"]:
        if row["n"]==n:
            return row["p"]
    raise AssertionError(f"not a certified early length: {n}")


def build(t,q,b,mode=0,precomputed=None):
    assert t>=1 and t%2==1 and q>0 and q%2==1
    L=t**3
    n=(q*L-1)//2
    A=(L-1)//2
    M=b**3-(q+1)//2
    assert M>=0 and b**3<q
    B=A+M*L
    C=(b*t)**3
    assert B+n+1==C and n-B==(q-b**3)*L>0

    seed362=precomputed
    if seed362 is None:
        seed362,_=read_and_verify()
    prefix=known_perm(A,seed362)
    sample=known_perm(M,seed362)

    alternative=sample.copy()
    if M==362 and mode:
        _,cycles=read_and_verify()
        cycle=cycles[0]
        for j,u in enumerate(cycle):
            alternative[u-1]=sample[cycle[(j+1)%len(cycle)]-1]
        assert alternative!=sample

    p=[0]*(n+1)
    p[1:A+1]=prefix
    for i in range(1,M+1):
        for r in range(1,L+1):
            base=alternative if (mode and r%2==0) else sample
            x=A+(i-1)*L+r
            p[x]=A+(base[i-1]-1)*L+L+1-r
            assert x+p[x]==L*(i+base[i-1])
    for x in range(B+1,n+1):
        p[x]=C-x
    assert sorted(p[1:])==list(range(1,n+1)), (t,q,b,"not bijective")
    cubes=set()
    k=2
    while k**3<=2*n:
        cubes.add(k**3)
        k+=1
    assert all(i+p[i] in cubes for i in range(1,n+1)),(t,q,b,"non-cube")
    assert p[n]==C-n
    return p


def main():
    seed362,cycles=read_and_verify()
    assert len(cycles)==40

    # Stronger explicit 362-base family; t=7 uses the early witness n=171.
    for t in (7,9):
        L=t**3
        n=(733*L-1)//2
        base=build(t,733,9,mode=0,precomputed=seed362)
        varied=build(t,733,9,mode=1,precomputed=seed362)
        assert varied!=base
        assert len(base)==len(varied)==n+1
        print(f"PASS 362 gadget: t={t}, n={n}, independent base cycles={40*L}.")

    # Two distinct summands in the power-divisor recurrence for one n:
    # q=1001: b=9 gives M=228; b=10 gives M=499.
    a=build(7,1001,9,precomputed=seed362)
    b=build(7,1001,10,precomputed=seed362)
    assert len(a)==len(b)==(1001*7**3+1)//2
    assert a[-1]!=b[-1]
    print("PASS divisor recurrence: q=1001, t=7, 2 distinct cube-suffix families.")


if __name__ == "__main__":
    main()
