#!/usr/bin/env python3
"""Independent exact-integer audit of arithmetic cube-sum graph expansion.

For i!=j, a common neighbor v implies
  |i-j| = a**3-b**3 = (a-b)*(a*a+a*b+b*b).
Hence the codegree is at most tau(|i-j|), the divisor count.
Cauchy-Schwarz then yields, for S with s vertices,
  |N(S)| >= s*minimum_degree**2/(maximum_degree+(s-1)*D),
where D=max_{1<=d<n}tau(d).

The published theorem combines this inequality with tau(d)=d**o(1)
to prove every Hall deficient set has size n**(2/3-o(1)).
This script verifies the finite identities without treating
finite computation as the mathematical asymptotic proof.
"""


def cubes(n):
    k=2
    vals=[]
    while k**3<=2*n:
        vals.append(k**3)
        k+=1
    return vals


def degree_matrix(n):
    cs=cubes(n)
    neighbors=[
        {c-i for c in cs if 1<=c-i<=n}
        for i in range(1,n+1)
    ]
    return neighbors


def divisor_counts(n):
    tau=[0]*n
    for d in range(1,n):
        for m in range(d,n,d):
            tau[m]+=1
    return tau


def cubert_floor(x):
    lo,hi=0,1
    while hi**3<=x:
        hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if m**3<=x:lo=m
        else:hi=m
    return lo


def verify(n):
    neighbors=degree_matrix(n)
    cs=cubes(n)
    tau=divisor_counts(n)
    dmin=min(map(len,neighbors))
    dmax=max(map(len,neighbors))
    D=max(tau[1:])
    assert all(
        len(neighbors[i-1]) == cubert_floor(i+n)-cubert_floor(i)
        for i in range(1,n+1)
    )
    # Integer cross-multiplication checks the second-moment bound exactly.
    subsets=[
        set(range(1,n+1)),
        set(range(1,n+1,2)),
        set(range(1,n+1,3)),
        set(range(1,min(n+1,26))),
        {1,n},
        {max(1,n//3),max(1,n//2),n},
    ]
    for S in subsets:
        if not S:continue
        used=set().union(*(neighbors[i-1] for i in S))
        s=len(S)
        assert len(used)*(dmax+(s-1)*D)>=s*dmin*dmin,(n,S)

    # Verify common-neighbor bound for all pairs in small graphs;
    # deterministic arithmetically-spaced sample for large graphs.
    if n<=236:
        pairs=((i,j) for i in range(1,n+1) for j in range(i+1,n+1))
    else:
        ix=sorted({1,2,3,n//4,n//2,3*n//4,n,
                   *range(1,n+1,max(1,n//40))})
        pairs=((i,j) for i in ix for j in ix if i<j)
    tested=0
    for i,j in pairs:
        common=len(neighbors[i-1]&neighbors[j-1])
        assert common<=tau[j-i],(n,i,j,common,tau[j-i])
        tested+=1

    # Compute exact difference-of-cubes multiplicity; stronger than tau
    # and independent of the choice of endpoints i,j.
    differences={}
    roots=[cubert_floor(c) for c in cs]
    for a in roots:
        for b in roots:
            d=a**3-b**3
            if 1<=d<n:
                differences[d]=differences.get(d,0)+1
    assert all(count<=tau[d] for d,count in differences.items())
    print(f"PASS n={n}: degree=[{dmin},{dmax}], "
          f"max_tau={D}, max_cube_diff_multiplicity="
          f"{max(differences.values(), default=0)}, "
          f"checked_pairs={tested}")


def main():
    for n in (172,236,1000,10000):
        verify(n)
    print("PASS: exact degree, divisor-codegree and "
          "Cauchy-Schwarz expansion identities.")


if __name__=="__main__":
    main()
