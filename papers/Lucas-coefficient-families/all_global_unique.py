"""Complete global uniqueness decision for all integer q and all three forms.

The paper proves a finite collision certificate for S_q and,
unless T_q has a stationary collision, a 13t index bound for
all collisions in T_q and P_q, t being the first index with
L_t>200*(q+1)**4.
"""
from argparse import ArgumentParser
from explicit_infinite import infinite_T
from global_collisions import index_cutoff,complete_collisions

L=[2,1]
def ensure(n):
    while len(L)<=n:L.append(L[-1]+L[-2])

def bounded_collision(q,form,N):
    """First repeated positive value and its two witnesses, or None."""
    ensure(N)
    first={}
    for i in range(1,N+1):
        for j in range(1,N+1):
            val = q*L[i] + (L[j] if form=='P' else -L[j])
            if val<=0:continue
            if val in first:
                return val,first[val],(i,j)
            first[val]=(i,j)
    return None

def global_status(q,form):
    """Return 'empty', 'unique', 'finite_collisions' or 'infinite_collisions'."""
    if form not in ('S','T','P'):raise ValueError("invalid form")
    if q==0:
        return 'empty' if form=='T' else 'infinite_collisions'
    if q==1: return 'infinite_collisions'
    if q<=-1:
        if form=='T':return 'empty'
        return global_status(-q, 'P' if form=='S' else 'S')
    if form=='S':
        return 'finite_collisions' if complete_collisions(q) else 'unique'
    if infinite_T(q):return 'infinite_collisions'
    six_t,t=index_cutoff(q)
    return 'finite_collisions' if bounded_collision(q,form,13*t) else 'unique'

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument("q",type=int)
    p.add_argument("form",choices=('S','T','P'))
    a=p.parse_args()
    print(global_status(a.q,a.form))
