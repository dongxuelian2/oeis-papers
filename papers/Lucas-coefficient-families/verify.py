"""Independent exhaustive integer audit of Lucas coefficient-family theorems."""
from bisect import bisect_right
from collections import defaultdict
from family import (unique_coefficient,repeated_coefficient,permitted,
                    bounded_index_count,positive_count,nth_positive,
                    repeat_witness,fibonacci)

L=[2,1]; F=[0,1]
def ensure(n):
    while len(L)<=n:
        L.append(L[-1]+L[-2])
        F.append(F[-1]+F[-2])
def signed_fib(n):
    ensure(abs(n))
    return F[n] if n>=0 else (-1)**(-n+1)*F[-n]

def run():
    signs=values=gaps=0
    for r in range(1,31):
        ensure(2*r)
        q=5*F[2*r]
        assert q==unique_coefficient(r)
        N=max(120,2*r+85)
        ensure(N+8)
        seen={}
        for i in range(1,N+1):
            for j in range(1,N+1):
                s=L[i]-q*L[j]
                assert (s>0)==permitted(r,i,j),(r,i,j,s)
                signs+=1
                if s>0:
                    assert s not in seen,(r,s,seen.get(s),(i,j))
                    seen[s]=(i,j)
                    values+=1
        for i in range(2*r+2,N-3):
            left=L[i+4]-q*L[i-2*r+2]-(L[i]-q)
            right=q+5*signed_fib(i-4*r+2)
            assert left==right and right>0,(r,i,left,right)
            gaps+=1
        for n in (2*r+2,2*r+3,2*r+8,N):
            assert sum(i<=n for i,j in seen.values())==bounded_index_count(r,n)
        ordered=sorted(seen)
        for x in list(range(0,120))+ordered[:20]:
            assert positive_count(r,x)==bisect_right(ordered,x),(r,x)
        for n in range(1,51):
            assert nth_positive(r,n)==ordered[n-1],(r,n)
    collisions=0
    for r in range(1,21):
        ensure(250+8*r)
        q=L[2*r]
        assert q==repeated_coefficient(r)
        for n in range(1,81):
            value=L[n+4*r]
            assert q*L[n+2*r]-L[n]==value
            assert q*L[n+6*r]-L[n+8*r]==value>0
            assert q*L[n+2*r]+L[n+8*r]==q*L[n+6*r]+L[n]
            assert repeat_witness(r,n)==(value,(n+2*r,n),(n+6*r,n+8*r))
            collisions+=1
    print("PASS: 30 collision-free coefficients q=5F_(2r), exact index regions")
    print(f"PASS: {signs} signs, {values} unique values, {gaps} strictly positive four-block gaps")
    print("PASS: bounded-index triangular count, exact threshold counts and nth terms")
    print(f"PASS: {collisions} repeated witnesses for 20 coefficients q=L_(2r)")
if __name__=="__main__":
    run()
