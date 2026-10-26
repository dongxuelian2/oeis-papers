#!/usr/bin/env python3
"""Parity-optimal cube-sum involutions from one odd-cube reflection seed per parity.

A strict interval reflection of sum c=k^3 adds no fixed point whenever
k is odd (since c/2 is not an integer), and it preserves length parity.

Seed odd: n=7, p(i)=8-i, one fixed point at i=4.
Seed even: n=26, p(i)=27-i, zero fixed points.

Exact finite reachability with ONLY odd cubes:
  every odd n in [70001,100001] is reached from 7;
  every even n in [230000,302000] is reached from 26.

Strong induction via the *least odd cube* c=k^3>=n+M+1 then gives
  every odd n>=70001: one fixed point (4)
  every even n>=230000: no fixed points.
The final gap bounds:
  for k>=57,  2*(k-2)^3-k^3-2*70001 >= 7555 >0;
  for k>=83,  2*(k-2)^3-k^3-2*230000 >=31095 >0.

No matching solvers, old 173 threshold, or old large certificates.
"""
from __future__ import annotations

ODD_SEED, ODD_LO, ODD_HI = 7, 70001, 100001
EVEN_SEED, EVEN_LO, EVEN_HI = 26, 230000, 302000


def odd_cubes(cap: int):
    result=[]
    k=3
    while k**3<=2*cap:
        result.append((k,k**3))
        k+=2
    return result


def reachability(seed: int, cap: int):
    assert seed in (ODD_SEED,EVEN_SEED)
    cubes=odd_cubes(cap)
    reachable=bytearray(cap+1)
    parent=[0]*(cap+1)  # stores predecessor length, 0 means unreachable
    roots=bytearray(cap+1)  # cube root, bounded by 100 for our caps
    reachable[seed]=1
    for n in range(seed+2, cap+1, 2):
        for k,c in cubes:
            if c>2*n:
                break
            m=c-n-1
            if seed<=m<n and reachable[m]:
                reachable[n]=1
                parent[n]=m
                roots[n]=k
                break
    return reachable,parent,roots


def integer_cube_ceiling(x: int, odd: bool = True):
    lo,hi=0,1
    while hi**3<x:
        hi*=2
    while lo+1<hi:
        m=(lo+hi)//2
        if m**3<x:
            lo=m
        else:
            hi=m
    k=hi
    if odd and not k%2:
        k+=1
    return k


def predecessor(n: int, seed: int, lower: int):
    k=integer_cube_ceiling(n+lower+1)
    m=k**3-n-1
    assert m>=lower and m<n and (m-n)%2==0
    if seed==ODD_SEED:
        assert n>=ODD_HI+2 and k>=57
        poly=2*(k-2)**3-k**3-2*ODD_LO
        assert poly>=7555
    else:
        assert n>=EVEN_HI+2 and k>=83
        poly=2*(k-2)**3-k**3-2*EVEN_LO
        assert poly>=31095
    return m,k


def history(n: int, seed: int, lo: int, hi: int, parent, roots):
    assert n>=lo and n%2==seed%2
    steps=[]
    cur=n
    while cur>hi:
        m,k=predecessor(cur,seed,lo)
        steps.append((m,cur,k))
        cur=m
    while cur!=seed:
        m,k=parent[cur],roots[cur]
        assert m>=seed and m<cur and k%2==1 and k**3==m+cur+1
        steps.append((m,cur,k))
        cur=m
    return steps


def actual_permutation(n: int,seed: int,lo:int,hi:int,parent,roots):
    chain=history(n,seed,lo,hi,parent,roots)
    p=[0]*(n+1)
    c=8 if seed==7 else 27
    for i in range(1,seed+1):
        p[i]=c-i
    for m,b,k in reversed(chain):
        c=k**3
        for i in range(m+1,b+1):
            p[i]=c-i
    assert sorted(p[1:])==list(range(1,n+1))
    assert all(p[p[i]]==i for i in range(1,n+1))
    assert all(i+p[i]==(8 if seed==7 else 27)
               or any(i+p[i]==k**3 for _,_,k in chain)
               for i in (1,seed,n//2,n))
    fixed=[i for i in range(1,n+1) if p[i]==i]
    assert fixed==([4] if seed==7 else [])
    for i in range(1,n+1):
        j=p[i]
        if i!=j:
            assert (i+j) == int(round((i+j)**(1/3)))**3 or any(
                i+j==k**3 for _,_,k in chain) or i+j==(8 if seed==7 else 27)
    return len(chain),fixed


def check_parity_tail(seed:int,lo:int,hi:int):
    found,parent,roots=reachability(seed,hi)
    assert all(found[n] for n in range(lo,hi+1,2))
    last_missing=max((n for n in range(seed,hi+1,2) if not found[n]),default=0)
    expected=69601 if seed==ODD_SEED else 228026
    assert last_missing==expected,(seed,last_missing)
    assert integer_cube_ceiling(hi+2+lo+1)%2==1
    for n in (lo,hi,hi+2,hi+10,2*hi):
        if n%2!=seed%2:n+=1
        depth,fixed=actual_permutation(n,seed,lo,hi,parent,roots)
        print(f"PASS seed={seed}, n={n}, depth={depth}, fixed={fixed}")
    length=(hi-lo)//2+1
    print(f"PASS seed={seed}: all {length} same-parity lengths "
          f"{lo}..{hi} reachable; last gap={last_missing}.")
    return parent,roots


def main():
    check_parity_tail(ODD_SEED,ODD_LO,ODD_HI)
    check_parity_tail(EVEN_SEED,EVEN_LO,EVEN_HI)
    assert 2*(57-2)**3-57**3-2*ODD_LO==7555
    assert 2*(83-2)**3-83**3-2*EVEN_LO==31095
    print("CERTIFIED by odd-cube induction: odd n>=70001 has an "
          "involution fixing exactly 4; even n>=230000 has a "
          "fixed-point-free cube-sum involution.")


if __name__=="__main__":
    main()
