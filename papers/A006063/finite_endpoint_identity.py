#!/usr/bin/env python3
"""Optional exact arithmetic audit of the paper's finite algebraic atlas.

Proof itself: Lemma "Boundary cancellation criterion" in main.tex.
For each n the finite table lists (b_j,k_j) and asserts
  {1} + {k_j**3-b_(j-1)} = {n+1} + {k_j**3-b_j}
as MULTISETS, with all image endpoints between 1 and n+1.

This is a mathematical assertion of explicit integer equality,
not a matching algorithm. A human can verify each row by sorting
two short lists; this small script is an optional cross-check.

All 109 rows cover 173..255 and 339..364; the remaining 256..338
follow by reflection through 8**3=512, and n>=365 follows
from the polynomial cube-gap lemma.
"""
from collections import Counter
from pathlib import Path

ATLAS = Path(__file__).resolve().parent / "certificates" / "finite_block_atlas.txt"


def verify_atlas():
    expected = list(range(173,256))+list(range(339,365))
    seen = []
    total_segments = 0
    max_segments = 0
    for raw in ATLAS.read_text(encoding="utf-8").splitlines():
        line=raw.strip()
        if not line or line.startswith("#"):
            continue
        items=line.split()
        n=int(items[0])
        b0=0
        L=[]
        R=[]
        for item in items[1:]:
            b,k=map(int,item.split(":"))
            assert b0<b<=n and 2<=k<=8,(n,item)
            c=k**3
            lo,hi=c-b,c-b0
            assert 1<=lo<hi<=n+1,(n,item,lo,hi)
            L.append(lo)
            R.append(hi)
            b0=b
        assert b0==n
        assert Counter([n+1,*L])==Counter([1,*R]), n
        assert sorted([n+1,*L])==sorted([1,*R])
        seen.append(n)
        total_segments+=len(L)
        max_segments=max(max_segments,len(L))
    assert seen==expected,(len(seen),seen)
    assert total_segments==1123
    assert max_segments==53
    print("PASS: 109 explicit integer multiset identities.")
    print("PASS: every table row defines a permutation via the")
    print("      boundary-cancellation lemma, no matching computation.")
    print("PASS: 1,123 image intervals; all image endpoints inside [1,n+1].")


if __name__=="__main__":
    verify_atlas()
