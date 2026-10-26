#!/usr/bin/env python3
"""General structural facts for cube-sum permutations, without a search cutoff.

(a) P(n) = permanent of the symmetric zero-one cube-sum matrix H_n.
(b) Modulo 2, P(n) = determinant(H_n) over F_2 (binary elimination).
(c) Any legal permutation p gives directed graph i->j when i+p(j) is a
    cube, and P(n) factors exactly over the graph's strong components.
(d) A four-block n=171 witness and the n=236 nine-component example
    demonstrate (b) and (c) independently of the original certificates.
"""
from itertools import permutations

def cubes(n):
    k=2
    result=[]
    while k**3<=2*n:
        result.append(k**3)
        k+=1
    return set(result)

def parity_via_binary_determinant(n):
    cs=cubes(n)
    rows=[]
    for i in range(1,n+1):
        value=0
        for c in cs:
            j=c-i
            if 1<=j<=n:value|=1<<(j-1)
        rows.append(value)
    rank=0
    for col in range(n):
        pivot=next((u for u in range(rank,n) if (rows[u]>>col)&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for u in range(rank+1,n):
            if (rows[u]>>col)&1:
                rows[u]^=rows[rank]
        rank+=1
    return int(rank==n)

def four_block_171():
    seg=[(1,7,8),(8,19,27),(20,44,64),(45,171,216)]
    p=[0]*172
    for a,b,c in seg:
        for i in range(a,b+1):
            assert p[i]==0
            p[i]=c-i
    return p

def fourteen_plus_one_block_236():
    blocks=[
        (1,7,8),(8,9,216),(10,18,64),(19,43,125),
        (44,45,216),(46,70,125),(71,81,216),(82,106,125),
        (107,134,343),(135,136,216),(137,170,343),
        (171,172,216),(173,197,343),(198,208,216),(209,236,343)]
    p=[0]*237
    for a,b,c in blocks:
        for i in range(a,b+1):
            assert p[i]==0
            p[i]=c-i
    return p

def strongly_connected_groups(p):
    n=len(p)-1
    cs=cubes(n)
    edges=[[] for _ in range(n+1)]
    reverse=[[] for _ in range(n+1)]
    for u in range(1,n+1):
        for v in range(1,n+1):
            if u!=v and u+p[v] in cs:
                edges[u].append(v)
                reverse[v].append(u)
    order=[]
    seen=[False]*(n+1)
    def go(u):
        seen[u]=True
        for v in edges[u]:
            if not seen[v]:go(v)
        order.append(u)
    for u in range(1,n+1):
        if not seen[u]:go(u)
    seen=[False]*(n+1)
    groups=[]
    def back(u,group):
        seen[u]=True
        group.append(u)
        for v in reverse[u]:
            if not seen[v]:back(v,group)
    for u in reversed(order):
        if not seen[u]:
            group=[]
            back(u,group)
            groups.append(sorted(group))
    return groups

def internal_permanent(group,p,cs):
    # Exhaustive for SCC sizes <=5 only. General theorem is proved in tex.
    assert len(group)<=5
    return sum(
        all(i+p[j] in cs for i,j in zip(group,perm))
        for perm in permutations(group)
    )

def check(p):
    n=len(p)-1
    cs=cubes(n)
    assert sorted(p[1:])==list(range(1,n+1))
    assert all(i+p[i] in cs for i in range(1,n+1))

def test_uniform_gap_bounds():
    """Exact smoke tests of two purely algebraic global theorems."""
    for n in (7,10,26,172,173,236,1000,10000,100000):
        k=2
        while (k+1)**3<=n+1:
            k+=1
        c=min((k**3,(k+1)**3),key=lambda x:abs(x-(n+1)))
        gap=(k+1)**3-k**3
        assert 2<=c<=2*n
        delta=abs(c-(n+1))
        assert delta<=gap//2
        lo=max(1,c-n)
        hi=min(n,c-1)
        assert hi-lo+1==n-delta
        assert all(lo<=c-i<=hi for i in (lo,hi))
        K=2
        while (K+1)**3<=2*n:
            K+=1
        G=(K+1)**3-K**3
        if n>=G:
            for a in (1,n//3,n//2):
                b=min(n,a+n-G)
                if b<a:continue
                lo2=b+1
                hi2=a+n
                cs=[z**3 for z in range(2,K+2) if lo2<=z**3<=hi2]
                assert cs, (n,a,b,lo2,hi2)
        print(f"PASS global cube gap n={n}: "
              f"matching defect <= {delta}, maximum gap {G}.")


def main():
    test_uniform_gap_bounds()
    cases={7:[0]+[8-i for i in range(1,8)],
           171:four_block_171(),
           236:fourteen_plus_one_block_236()}
    for n,p in cases.items():
        check(p)
        groups=strongly_connected_groups(p)
        if n==171:
            assert len(groups)==171
        if n==236:
            nonsingletons=[g for g in groups if len(g)>1]
            assert len(groups)==200 and len(nonsingletons)==9
            expected=[{10+t,46+t,71+t,137+t,198+t} for t in range(9)]
            assert {frozenset(g) for g in nonsingletons} == {
                frozenset(g) for g in expected}
            product=1
            for group in groups:
                val=internal_permanent(group,p,cubes(n))
                if len(group)>1:assert val==2
                product*=val
            assert product==512
        expected_parity={7:1,171:1,236:0}[n]
        got=parity_via_binary_determinant(n)
        assert got==expected_parity
        print(f"PASS n={n}: SCCs={len(groups)}, parity={got}.")
    print("PASS P(236)=2^9 exact via 9 five-vertex permanent factors.")
    print("PASS parity checked independently through GF(2) elimination.")

if __name__ == "__main__":
    main()
