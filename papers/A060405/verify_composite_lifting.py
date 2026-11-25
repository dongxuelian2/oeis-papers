#!/usr/bin/env python3
"""Composite-period CRT propagation, and exact scalar-period modulus checks."""
from collections import defaultdict
from math import gcd
from verify_anchor_forcing import A, B, M, ANCHORS, mp, val, primes, order, factors, four_anchors

EXPECTED = {
    3: ((60,132),(96,379),(17,426),(1,429),(0,429)),
    -3: ((56,121),(97,373),(21,436),(1,439),(0,439)),
    -2: ((53,113),(77,303),(14,342),(0,342)),
    -1: ((59,129),(92,366),(24,436),(0,436)),
}


def check_period_formula(N=1000):
    F,P,L,Q = [0,1],[0,1],[2,1],[1,1]
    for _ in range(N+3):
        F.append(F[-1]+F[-2])
        P.append(2*P[-1]+P[-2])
        L.append(L[-1]+L[-2])
        Q.append(2*Q[-1]+Q[-2])
    a=[x+y for x,y in zip(L,P)]
    for h in range(1,N+1):
        k=h//2
        expected=(1 if h%2 else gcd(5*F[k],2*P[k]) if k%2==0
                  else gcd(L[k],2*Q[k]))
        assert gcd(*(a[h+j]-a[j] for j in range(4)))==expected
        assert gcd(L[h]-2,L[h+1]-1,P[h],P[h+1]-1)==expected
    print('Exact scalar-period modulus:',N,'checks passed')


def initial(q,h,r):
    a,b=mp(A,r%h,q),mp(B,r%h,q)
    return ((2*a[0]+a[1])%q,(2*a[2]+a[3])%q,b[1],b[3])


def flags(r,D,q,h,f):
    a,b,c,d=initial(q,h,r)
    x,y,z,w=mp(A,D%h,q)
    i,j,k,l=mp(B,D%h,q)
    sq=bytearray(q)
    for t in range((q+1)//2):
        sq[t*t%q]=1
    result=[]
    for t in range(f):
        if sq[(a+c)%q]:
            result.append(t)
        a,b,c,d=(x*a+y*b)%q,(z*a+w*b)%q,(i*c+j*d)%q,(k*c+l*d)%q
    assert 0 in result
    return result


def factor_powers(n):
    out=[]
    for p in factors(n):
        s=1
        while n%p==0:
            n//=p
            s*=p
        out.append((p,s))
    assert n==1
    return out


def generalized_round(r,D,orders,cap=2000):
    groups=defaultdict(list)
    for q,h in orders:
        f=h//gcd(D,h)
        if 1<f<=cap:
            groups[f].append((q,h))
    constraints={}
    for f,qs in groups.items():
        # Resource filter: omitting constraints cannot invalidate a deduction.
        if len(qs)==1 and f>128:
            continue
        ts=None
        for q,h in qs:
            if ts is None or len(ts)>f//8:
                new=set(flags(r,D,q,h,f))
                ts=new if ts is None else ts&new
            else:
                ts={t for t in ts if pow(val((r+(D%h)*t)%h,q),(q-1)//2,q)!=q-1}
            if ts=={0}:
                break
        assert 0 in ts
        if len(ts)<f:
            constraints[f]=ts

    # Necessary domains modulo the largest available power of each prime.
    facts={f:factor_powers(f) for f in constraints}
    maxs={}
    for pp in facts.values():
        for p,s in pp:
            maxs[p]=max(maxs.get(p,1),s)
    domains={p:set(range(s)) for p,s in maxs.items()}
    change=True
    while change:
        change=False
        for f,ts in constraints.items():
            pp=facts[f]
            proj={p:{t%s for t in ts} for p,s in pp}
            for p,s in pp:
                dom=domains[p]
                new={v for v in dom if v%s in proj[p]}
                if len(new)<len(dom):
                    domains[p]=new
                    change=True
            proj2={p:{v%s for v in domains[p]} for p,s in pp}
            new={t for t in ts if all(t%s in proj2[p] for p,s in pp)}
            assert 0 in new
            if len(new)<len(ts):
                constraints[f]=new
                change=True

    mult=1
    forced=[]
    for p,s in sorted(maxs.items()):
        v=gcd(s,*domains[p])
        if v>1:
            forced.append((p,v))
            mult*=v
    return mult,forced


def certificate():
    assert four_anchors()==sorted(r%M for r in ANCHORS)
    orders=[(q,order(q)) for q in primes(100000) if q>5]
    assert len(orders)==9589
    result={}
    for r in ANCHORS:
        D=M
        for j,(count,digits) in enumerate(EXPECTED[r],1):
            mult,forced=generalized_round(r,D,orders)
            D*=mult
            assert (len(forced),len(str(D)))==(count,digits)
            print('anchor',r,'round',j,'forced prime powers',count,'digits',digits,flush=True)
        assert mult==1
        result[r]=D
        print('D',r,D,flush=True)
    assert min(result.values())>10**341+3
    print('Only square index in [0, 10^341] is 3.')
    return result


if __name__=='__main__':
    check_period_formula()
    certificate()
