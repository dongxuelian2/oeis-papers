#!/usr/bin/env python3
"""Audit involution-preserving reflection closure from the 7-point seed.

Every strict suffix reflection extends a legal involution by another
disjoint involution, leaving p(4)=4. Theorems in main.tex therefore show
I_4(n)>=F(n)>0 for every n>=8915 and
liminf log I_4(n)/(2*n)**(1/3)>=log(2)/2.

This checker tests actual constructed permutations at representative
lengths; the infinite result follows from the induction and the
reflection-tree entropy theorem, not from extrapolating these tests.
"""
from one_seed_eventual import finite_reflection_closure, construct, plan


def check_involution(n, parents):
    p=[0]+construct(n,parents)
    assert len(p)==n+1
    assert p[4]==4
    assert all(p[p[i]]==i for i in range(1,n+1))
    block_count=len(plan(n,parents))
    # Every cycle is a fixed point or a transposition.
    visited=bytearray(n+1)
    fixed=0
    pairs=0
    for i in range(1,n+1):
        if visited[i]:continue
        j=p[i]
        if i==j:
            visited[i]=1
            fixed+=1
        else:
            assert i!=j and p[j]==i
            visited[i]=visited[j]=1
            pairs+=1
    assert fixed+2*pairs==n
    assert fixed>=1 and fixed%2==n%2
    print(f"PASS n={n}: involution fixing 4, "
          f"{fixed} fixed points, {pairs} transpositions, "
          f"{block_count} reflection layers.")


def main():
    parents,_=finite_reflection_closure()
    for n in (8915,8916,9841,10975,10976,20000,100000):
        check_involution(n,parents)
    print("PASS: involution preservation verified on explicit constructions.")


if __name__=="__main__":
    main()
