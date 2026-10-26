#!/usr/bin/env python3
"""Structural, solver-free audit: P(236)=512, with no cube-sum involution.

A 15-interval permutation produces an alternating directed graph with
exactly nine independent directed 5-cycle SCCs and 191 singleton SCCs.
All equalities are verified with exact integers; no matching solver.
"""
N=236
BLOCKS=[
 (1,7,8),(8,9,216),(10,18,64),(19,43,125),
 (44,45,216),(46,70,125),(71,81,216),(82,106,125),
 (107,134,343),(135,136,216),(137,170,343),
 (171,172,216),(173,197,343),(198,208,216),(209,236,343)]
CUBES={k**3 for k in range(2,9) if k**3<=2*N}

def template():
    p=[0]*(N+1)
    for a,b,c in BLOCKS:
        assert c in CUBES and 1<=a<=b<=N
        for i in range(a,b+1):
            assert p[i]==0
            p[i]=c-i
    assert sorted(p[1:])==list(range(1,N+1))
    assert all(i+p[i] in CUBES for i in range(1,N+1))
    return p

def components(E):
    order=[];seen=set()
    def visit(u):
        seen.add(u)
        for v in sorted(E[u]):
            if v not in seen:visit(v)
        order.append(u)
    for u in E:
        if u not in seen:visit(u)
    reverse={u:set() for u in E}
    for u in E:
        for v in E[u]:reverse[v].add(u)
    seen.clear();scc=[]
    def visit_reverse(u,c):
        seen.add(u);c.add(u)
        for v in sorted(reverse[u]):
            if v not in seen:visit_reverse(v,c)
    for u in reversed(order):
        if u not in seen:
            c=set();visit_reverse(u,c);scc.append(c)
    return scc

def main():
    p=template()
    E={i:{j for j in range(1,N+1) if i!=j and i+p[j] in CUBES}
       for i in range(1,N+1)}
    scc=components(E)
    expected=[{10+j,46+j,71+j,137+j,198+j} for j in range(9)]
    assert len(scc)==200 and sum(len(c)==1 for c in scc)==191
    assert {frozenset(c) for c in scc if len(c)>1}=={
        frozenset(c) for c in expected}
    for C in expected:
        local={i:E[i]&C for i in C}
        assert all(len(local[i])==1 for i in C)
        successors={i:next(iter(local[i])) for i in C}
        assert set(successors.values())==C
        start=min(C);cur=start;cycle=[]
        while cur not in cycle:
            cycle.append(cur);cur=successors[cur]
        assert cur==start and len(cycle)==5

    # For any solution q, f=p^{-1} o q is a permutation whose directed
    # arcs are among the edges of E plus loops. Each f-cycle lies in an
    # SCC, thus singletons contribute 1 and 5-cycles each contribute 2.
    assert 2**len(expected)==512

    # The middle 5-block is invariant under p; its only choices
    # are p and its inverse, both genuine odd 5-cycles.
    S={14,50,75,141,202}
    assert [p[i] for i in (14,50,75,141,202)]==[50,75,141,202,14]
    inverse={p[i]:i for i in S}
    f={i:next(iter(E[i]&S)) for i in S}
    assert all(p[f[i]]==inverse[i] for i in S)
    assert all(p[p[i]]!=i and inverse[inverse[i]]!=i for i in S)
    print("PASS: fifteen-interval valid permutation, nine independent 5-cycles.")
    print("PROVED: P(236)=512 and no cube-sum involution for n=236.")

if __name__=="__main__":
    main()
