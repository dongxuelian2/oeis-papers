#!/usr/bin/env python3
"""Verify inverse-paired tensor fibers form legal cube-sum involutions.

For any odd cube L=t**3 and arbitrary valid p_r on [M], the shifted
fiber construction Q(i,r)=(p_r(i),L+1-r) is an involution precisely
when p_(L+1-r)=p_r**(-1). Therefore its exact count is
I(M)*P(M)**((L-1)//2).

This test uses a 316-element involution p with cube sums 27 and 343,
and a different valid permutation q obtained by switching one
alternating five-cycle. No large matching certificate is used.
"""


def cube_set(n):
    return {k**3 for k in range(2,int((2*n)**(1/3))+4)
            if k**3<=2*n}


def check(p):
    n=len(p)-1
    assert sorted(p[1:])==list(range(1,n+1))
    cubes=cube_set(n)
    assert all(i+p[i] in cubes for i in range(1,n+1))


def seed_316():
    p=[0]*317
    for i in range(1,27):p[i]=27-i
    for i in range(27,317):p[i]=343-i
    check(p)
    assert all(p[p[i]]==i for i in range(1,317))
    return p


def alternative(p):
    q=p[:]
    cycle=(1,219,50,268,99)
    for j,i in enumerate(cycle):
        q[i]=p[cycle[(j+1)%len(cycle)]]
    check(q)
    assert q!=p
    assert any(q[q[i]]!=i for i in range(1,317))
    return q


def inverse(p):
    inv=[0]*len(p)
    for i in range(1,len(p)):inv[p[i]]=i
    check(inv)
    return inv


def lift(t):
    assert t%2
    L=t**3
    M=316
    A=(L-1)//2
    p=seed_316()
    q=alternative(p)
    qi=inverse(q)
    fibers={}
    for r in range(1,L+1):
        if r==(L+1)//2:
            fibers[r]=p
        elif r<(L+1)//2:
            fibers[r]=q if r%2 else p
        else:
            fibers[r]=inverse(fibers[L+1-r])
    Q=[0]*(A+M*L+1)
    for r in range(1,L+1):
        for i in range(1,M+1):
            u=A+(i-1)*L+r
            j=fibers[r][i]
            Q[u]=A+(j-1)*L+L+1-r
            assert u+Q[u]==L*(i+j)
    lo=A+1
    assert sorted(Q[lo:])==list(range(lo,A+M*L+1))
    assert all(Q[Q[x]]==x for x in range(lo,A+M*L+1))
    assert all(u+Q[u] in cube_set(A+M*L) for u in range(lo,A+M*L+1))
    print(f"PASS t={t}, L={L}, M={M}, "
          f"paired fiber choices={(L-1)//2}, "
          f"legal involution on shifted interval.")


if __name__=="__main__":
    for t in (3,5):lift(t)
