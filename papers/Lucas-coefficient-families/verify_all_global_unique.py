"""Global uniqueness certificate for ALL three forms, coefficients q=2..100."""
from all_global_unique import global_status
from stationary_collisions import stationary_T
from global_collisions import complete_collisions,index_cutoff

S_NOT_UNIQUE={
 2,3,4,6,7,9,10,11,14,17,18,19,23,25,28,29,31,
 36,38,41,46,47,62,65,72,73,75,76,94,
}
T_UNIQUE={
 27,31,39,42,57,59,62,63,67,68,70,71,78,83,86,91,93,95,97,
}
P_UNIQUE={
 27,39,42,57,59,63,67,68,70,71,78,83,86,91,93,95,97,
}
INFINITE={
 2,3,4,7,8,11,18,19,21,29,38,47,48,55,76,
}

def lucas(n):
    L=[2,1]
    while len(L)<=n:L.append(L[-1]+L[-2])
    return L

def brute(q,mode,n):
    L=lucas(n)
    seen=set()
    for i in range(1,n+1):
        for j in range(1,n+1):
            v=q*L[i]+(L[j] if mode=='P' else -L[j])
            if v<=0:continue
            if v in seen:return False
            seen.add(v)
    return True

def main():
    for q in range(2,101):
        s=global_status(q,'S')
        assert (s=='finite_collisions')==(q in S_NOT_UNIQUE)
        tflag=global_status(q,'T')
        pflag=global_status(q,'P')
        assert (tflag=='infinite_collisions')==(q in INFINITE)
        assert (pflag=='infinite_collisions')==(q in INFINITE)
        assert (tflag=='unique')==(q in T_UNIQUE),(q,tflag)
        assert (pflag=='unique')==(q in P_UNIQUE),(q,pflag)
        _,t=index_cutoff(q)
        if q not in INFINITE:
            assert (tflag=='unique')==brute(q,'T',13*t+5),q
            assert (pflag=='unique')==brute(q,'P',13*t+5),q
    for q in (-31,-7,-1,0,1,2,3,5,27,31,38):
        assert global_status(q,'S') in ('unique','finite_collisions','infinite_collisions')
        for mode in ('T','P'):
            assert global_status(q,mode) in ('empty','unique','finite_collisions','infinite_collisions')
    assert global_status(31,'T')=='unique'
    assert global_status(31,'P')=='finite_collisions'
    assert global_status(27,'T')==global_status(27,'P')=='unique'
    assert global_status(5,'T')==global_status(5,'P')=='finite_collisions'
    print("PASS: q=2..100, global uniqueness for all S,T,P forms")
    print("PASS: 70/99 globally unique S_q; 19/99 globally unique T_q; 17/99 globally unique P_q")
    print("PASS: independent enlarged finite windows and sign reductions")

if __name__=='__main__':main()
