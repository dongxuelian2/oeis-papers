#!/usr/bin/env python3
"""Exact Hamming-isometry audit for cube-sum permutation binary codes.

No search is used. Nine disjoint directed 5-cycles inside an explicit
n=236 interval permutation encode nine independent bits. Block lifting
creates 9*t**3 bits, and changing one bit changes precisely 5 entries.
"""
from count_236 import template

M = 236
CYCLES = [
    (10+j,137+j,46+j,198+j,71+j) for j in range(9)
]


def fiber(base, mask):
    output = base[:]
    for j, cycle in enumerate(CYCLES):
        if mask & (1<<j):
            for z, i in enumerate(cycle):
                output[i] = base[cycle[(z+1)%5]]
    return output


def interval(t, masks):
    L=t**3
    assert t%2 and len(masks)==L
    A=(L-1)//2
    base=template()
    p=[0]*(A+M*L+1)
    fibers={k:fiber(base,k) for k in set(masks)}
    for r,mask in enumerate(masks,1):
        q=fibers[mask]
        for i in range(1,M+1):
            u=A+(i-1)*L+r
            p[u]=A+(q[i]-1)*L+(L+1-r)
            assert u+p[u]==L*(i+q[i])
    assert sorted(p[A+1:])==list(range(A+1,A+M*L+1))
    return p,A,L


def audit(t):
    L=t**3
    base=template()
    seqs=set()
    for mask in range(512):
        p=fiber(base,mask)
        assert all(i+p[i] in {8,27,64,125,216,343} for i in range(1,M+1))
        assert sorted(p[1:])==list(range(1,M+1))
        word=tuple(p[1:])
        assert word not in seqs
        seqs.add(word)
        assert sum(p[i]!=base[i] for i in range(1,M+1))==5*mask.bit_count()
    assert len(seqs)==512

    first=[(73*r+19)%512 for r in range(L)]
    second=[((113*r+207)^341)%512 for r in range(L)]
    p,A,L=interval(t,first)
    q,B,_=interval(t,second)
    assert A==B
    hd=sum(p[i]!=q[i] for i in range(A+1,A+M*L+1))
    bits=sum((u^v).bit_count() for u,v in zip(first,second))
    assert hd==5*bits
    print(f"PASS odd t={t}: {9*L} bits, "
          f"permutation Hamming distance={hd} = 5*{bits}.")


if __name__=="__main__":
    for t in (3,5,9):
        audit(t)
