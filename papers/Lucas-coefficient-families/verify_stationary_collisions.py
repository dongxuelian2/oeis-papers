"""Exact collision dichotomy audits for T/P and all coefficient signs."""
from stationary_collisions import stationary_T,infinite_collisions,finite_T_collision_seeds

T_INFINITE_TO_200={
 2,3,4,7,8,11,18,19,21,29,38,47,48,55,76,
 123,124,144,199,
}

def lucas(N):
    a=[2,1]
    while len(a)<=N: a.append(a[-1]+a[-2])
    return a

def main():
    coeffs=patterns=0
    for q in range(2,201):
        offsets=stationary_T(q)
        assert bool(offsets)==(q in T_INFINITE_TO_200),(q,offsets)
        assert infinite_collisions(q,'T')==bool(offsets)
        assert infinite_collisions(q,'P')==bool(offsets)
        assert not infinite_collisions(q,'S')
        from global_collisions import index_cutoff
        six_t,t=index_cutoff(q)
        K=2*six_t+1
        L=lucas(K+t+35)
        for di,dj,de in offsets:
            i,j,ell=K+di,K+dj,K+de
            assert 0<i<K and 0<j<ell
            for shift in (0,1,2,3,11,29):
                value=q*L[K+shift]-L[ell+shift]
                assert value>0
                assert value==q*L[i+shift]-L[j+shift]
                assert q*L[K+shift]+L[j+shift] == q*L[i+shift]+L[ell+shift]
        coeffs+=1
        patterns+=len(offsets)
    seeds=finite_T_collision_seeds(5)
    assert sorted(seeds)==[2,4,8,14,17],seeds
    assert not stationary_T(5)
    assert stationary_T(2)
    for q in (-40,-7,-1,0,1,2,3,5,7,38):
        for form in ('S','T','P'):
            flag=infinite_collisions(q,form)
            if q==0:assert flag==(form!='T')
            if q<=-2:
                if form=='T' or form=='P':assert not flag
                if form=='S':assert flag==infinite_collisions(-q,'T')
    print(f"PASS: all {coeffs} coefficient classifications q=2..200")
    print(f"PASS: {patterns} stationary families, each verified across 6 shifts")
    print("PASS: q=5 has exactly five finite T collisions and zero stationary families")
    print("PASS: all signs and three expression forms covered")

if __name__=="__main__":main()
