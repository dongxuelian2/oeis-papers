"""Complete effective infinite-collision decision for ALL integer q and S/T/P.

For q>=2, T_q collisions whose larger first index k > 12t
are stationary; t is least with L_t > 200*(q+1)**4.
Every infinite T/P collision family has a representative in
the finite window around K=12t+1. The paper proves necessity.
"""
from argparse import ArgumentParser
from collections import defaultdict
from global_collisions import index_cutoff,complete_collisions
L=[2,1]
def ensure(n):
    while len(L)<=n: L.append(L[-1]+L[-2])

def stationary_T(q):
    """Return all normalised (i-K,j-K,ell-K) simultaneous-shift patterns."""
    if q<2: raise ValueError("q must be >= 2")
    six_t,t=index_cutoff(q)
    K=2*six_t+1
    ensure(K+t+2)
    lookup=defaultdict(list)
    for i in range(K-3*t,K):
        for j in range(K-6*t,K+t+1):
            key=(q*L[i]-L[j],q*L[i+1]-L[j+1])
            lookup[key].append((i-K,j-K,j))
    found=set()
    for ell in range(K-t,K+t+1):
        x=q*L[K]-L[ell]
        if x<=0: continue
        key=(x,q*L[K+1]-L[ell+1])
        for di,dj,j in lookup.get(key,()):
            if j<ell: found.add((di,dj,ell-K))
    return sorted(found)

def infinite_collisions(q,form):
    """Exact boolean for infinite repeated positive VALUES in S_q/T_q/P_q."""
    if form not in ('S','T','P'): raise ValueError("form must be S/T/P")
    if q==0: return form!='T'
    if q==1: return True
    if q>=2:
        return False if form=='S' else bool(stationary_T(q))
    # q = -m < 0
    if form=='T': return False
    m=-q
    if form=='P': return m==1
    return True if m==1 else bool(stationary_T(m))

def finite_T_collision_seeds(q):
    """All T_q collisions with the larger first index <=12t."""
    if q<2: raise ValueError("q must be >=2")
    six_t,t=index_cutoff(q)
    K=2*six_t
    ensure(K+t+2)
    first={}
    dup={}
    for k in range(1,K+1):
        for ell in range(1,K+t+1):
            value=q*L[k]-L[ell]
            if value<=0: break
            if value in dup:
                dup[value].append((k,ell))
            elif value in first:
                dup[value]=[first.pop(value),(k,ell)]
            else:
                first[value]=(k,ell)
    return dict(sorted(dup.items()))

if __name__=="__main__":
    p=ArgumentParser(description=__doc__)
    p.add_argument("form",choices=('S','T','P'))
    p.add_argument("q",type=int)
    a=p.parse_args()
    flag=infinite_collisions(a.q,a.form)
    print(f"q={a.q} form={a.form}: infinitely many repeated positive values = {flag}")
    if a.q>=2 and a.form in ('T','P'):
        print("stationary T patterns:", stationary_T(a.q))
    if a.q>=2 and a.form=='S':
        print("complete finite S collision list:",complete_collisions(a.q))
