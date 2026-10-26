#!/usr/bin/env python3
"""Audit exact initial leaves in all 199 high-band four-color graphs.

Uses integer arithmetic only. NO matching, optimization, NetworkX,
SciPy, archived permutation arrays, or endpoint certificates.
"""
PHASES=(
    (467,560,(216,343,512,729)),
    (561,579,(216,512,729,1000)),
    (580,665,(343,512,729,1000)),
)


def expected_leaves(n):
    if n<=560:
        if n<512:
            return None
        return set(range(512,n+1)) | ({404} if n%2 else set())
    if n<=579:
        return {256,404} if n%2 else {108,256}
    if n%2==0:
        return set()
    return {87} if n<=641 else set()


def main():
    checked=0
    for low,high,cubes in PHASES:
        for n in range(low,high+1):
            fixed = (108 if n<=579 else 256) if n%2 else None
            V=set(range(1,n+1))
            if fixed is not None:
                assert 2*fixed in cubes
                V.remove(fixed)
            nbrs={i:{c-i for c in cubes
                     if c-i in V and c-i!=i}
                  for i in V}
            assert all(len(q)>=1 for q in nbrs.values())
            E={i for i,q in nbrs.items() if len(q)==1}
            want=expected_leaves(n)
            if want is not None:
                assert E==want,(n,sorted(E),sorted(want))
            if 512<=n<=560:
                for i in range(512,n+1):
                    assert nbrs[i]=={729-i}
                if n%2:
                    assert nbrs[404]=={325}
            if 561<=n<=579:
                assert nbrs[256]=={473}
                assert nbrs[404 if n%2 else 108]=={
                    325 if n%2 else 404}
            if n>=581 and n%2:
                if n<=641:
                    assert nbrs[87]=={425}
                else:
                    assert nbrs[87]=={425,642}
            checked+=1
    assert checked==199
    print("PASS: 199/199 exact high-window initial leaf sets")
    print("PASS: phase I forced suffix [512,n], and extra odd 404")
    print("PASS: phase II exactly two forced leaves per length")
    print("PASS: phase III even no leaves; odd fixed256 threshold 642")
    print("PASS: all odd n=581..641 fixed256 force 87<->425")
    print("NOTE: this proves necessary forced edges, not matching existence")


if __name__=="__main__":
    main()
