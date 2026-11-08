#!/usr/bin/env python3
"""Exact, standard-library late-prefix square-candidate enumeration.

No floats, external packages, network calls, or fixed-width root scanning.
For every k audited, enumerate all squares R_(m,k)<H_k^2, m>k,
where H_k=10^D(k)/sqrt(W_k's 2,5-smooth part).
"""
import argparse, hashlib, json, math, sys, time
from pathlib import Path
sys.set_int_max_str_digits(0)


def vp(n, p):
    a=0
    while n%p==0:
        n//=p; a+=1
    return a


def unit_roots(u,p,n):
    """All roots of a p-adic unit modulo p^n, by precision doubling."""
    assert n>0 and u%p
    modulus=p**n; u%=modulus
    if p==2:
        if n<=3:
            return [r for r in range(1,modulus,2) if r*r%modulus==u]
        if u%8!=1: return []
        r=1; e=3
        while e<n:
            target=min(n,2*e-2); q=1<<target
            r=(r+((u-r*r)//2)*pow(r,-1,q))%q
            assert (r*r-u)%q==0
            e=target
        return sorted({r,(-r)%modulus,(r+modulus//2)%modulus,(-r+modulus//2)%modulus})
    assert p==5
    starts=[r for r in (1,2) if r*r%5==u%5]
    if not starts: return []
    r=starts[0]; e=1
    while e<n:
        target=min(n,2*e); q=5**target
        r=(r+(u-r*r)*pow(2*r,-1,q))%q
        assert (r*r-u)%q==0
        e=target
    return sorted({r,(-r)%modulus})


def compressed_roots(U,s):
    """Return all root classes modulo H; empty means a local obstruction."""
    v2,v5=vp(U,2),vp(U,5)
    assert max(v2,v5)<s
    if v2%2 or v5%2: return None,[],(v2,v5)
    a,b=v2//2,v5//2
    mod2,mod5=2**(s-a),5**(s-b)
    root2=[2**a*r for r in unit_roots(U//2**v2,2,s-v2)]
    root5=[5**b*r for r in unit_roots(U//5**v5,5,s-v5)]
    H=mod2*mod5
    if not root2 or not root5: return H,[],(v2,v5)
    inverse=pow(mod2,-1,mod5)
    roots=sorted({(r2+mod2*((r5-r2)*inverse%mod5))%H for r2 in root2 for r5 in root5})
    assert len(roots)<=8 and H==10**s//(2**a*5**b)
    for r in roots: assert (r*r-U)%10**s==0
    return H,roots,(v2,v5)


def digits_before_width(d):
    L=10**(d-1)
    return ((9*d-10)*L+1)//9


def D(m):
    if m==0:return 0
    d=len(str(m)); L=10**(d-1)
    return digits_before_width(d)+d*(m-L+1)


def endpoint_from_digit_count(E):
    """Unique m with D(m)=E, or None. D has gaps at width >=2."""
    if E<=0:return None
    d=1; L=1; t=0
    while E>t+9*d*L:
        t+=9*d*L; d+=1; L*=10
    q,r=divmod(E-t,d)
    return L+q-1 if r==0 and 1<=q<=9*L else None


def endpoint_at_most_digits(E):
    d=1; L=1; t=0
    while E>=t+9*d*L:
        t+=9*d*L; d+=1; L*=10
    return L-1+max(0,(E-t)//d)


def prefix(m):
    """Construct W_m by one exact arithmetic-geometric identity per width."""
    if not m:return 0
    W=0; L=1; B=10
    while L<=m:
        j=min(m,B-1); n=j-L+1; C=B-1
        numerator=(C*C*W+L*C+1)*pow(B,n)-(j*C+B)
        W,remainder=divmod(numerator,C*C)
        assert remainder==0
        L=B; B*=10
    return W


def rotation(m,k,U=None,s=None):
    U=prefix(k) if U is None else U
    s=D(k) if s is None else s
    E=D(m)
    return 10**s*prefix(m)-(10**E-1)*U


def local_root_audit():
    count=0
    for p,limit in ((2,10),(5,5)):
        for n in range(1,limit+1):
            q=p**n
            for u in range(1,min(q,200)):
                if u%p:
                    actual=unit_roots(u,p,n)
                    expected=[r for r in range(q) if r*r%q==u%q]
                    assert actual==expected,(p,n,u)
                    count+=1
    return count


def enumerate_cut(k,U,s):
    H,roots,valuations=compressed_roots(U,s)
    witnesses=[]; survivors=[]
    for index,r in enumerate(roots):
        square=r*r; E=len(str(square)); m=endpoint_from_digit_count(E)
        if m is None:
            witnesses.append({'branch':index,'kind':'digit_gap','square_digits':E})
        elif m<=k:
            witnesses.append({'branch':index,'kind':'endpoint_not_after_cut','m':m})
        else:
            R=rotation(m,k,U,s)
            sign=(square>R)-(square<R)
            witnesses.append({'branch':index,'kind':'exact_comparison','m':m,'square_minus_rotation_sign':sign})
            if sign==0:survivors.append(m)
    return H,roots,valuations,witnesses,survivors


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--max-cut',type=int,default=1000); ap.add_argument('--output',default='late-prefix-certificate.json'); args=ap.parse_args()
    start=time.monotonic()
    root_audit=local_root_audit()
    summary={'max_cut':args.max_cut,'cut_range_start':10,'unit_root_exhaustive_cases':root_audit,'cuts':0,'odd_valuation_cuts':0,'unit_obstructed_cuts':0,'local_survivor_cuts':0,'root_branches':0,'digit_gap_rejections':0,'not_after_cut_rejections':0,'exact_candidate_comparisons':0,'guaranteed_pairs_all_cuts':0,'guaranteed_pairs_local_survivor_cuts':0,'square_survivors':[],'width_crossing_survivor_cuts':0,'naive_crosscheck_pairs':0}
    records=[]; U=0;s=0
    for k in range(1,args.max_cut+1):
        w=len(str(k)); U=U*10**w+k;s+=w
        if k<10:continue
        assert s==D(k)
        H,roots,valuations,witnesses,survivors=enumerate_cut(k,U,s)
        summary['cuts']+=1
        guaranteed_end=endpoint_at_most_digits(2*s-2*w)
        guaranteed_count=max(0,guaranteed_end-k)
        summary['guaranteed_pairs_all_cuts']+=guaranteed_count
        if any(v%2 for v in valuations):summary['odd_valuation_cuts']+=1
        elif not roots:summary['unit_obstructed_cuts']+=1
        else:
            summary['local_survivor_cuts']+=1
            summary['guaranteed_pairs_local_survivor_cuts']+=guaranteed_count
            if len(str(guaranteed_end))>w:summary['width_crossing_survivor_cuts']+=1
        summary['root_branches']+=len(roots)
        for witness in witnesses:
            if witness['kind']=='digit_gap':summary['digit_gap_rejections']+=1
            elif witness['kind']=='endpoint_not_after_cut':summary['not_after_cut_rejections']+=1
            else:summary['exact_candidate_comparisons']+=1
        summary['square_survivors'] += [[m,k] for m in survivors]
        # Store concise reproducible branch dispositions. Roots are reconstructed,
        # not copied as giant decimal strings into the report.
        if roots:
            records.append({'k':k,'prefix_digits':s,'valuations':valuations,'guaranteed_endpoint':guaranteed_end,'branches':witnesses})
        # Independent brute-force pair audit over a small domain.
        if k<=99:
            for m in range(k+1,guaranteed_end+1):
                R=rotation(m,k,U,s); y=math.isqrt(R)
                assert (y*y==R)==(m in survivors)
                summary['naive_crosscheck_pairs']+=1
        if k%1000==0:
            print(json.dumps({'progress_cut':k,'elapsed_seconds':round(time.monotonic()-start,3),'root_branches':summary['root_branches'],'comparisons':summary['exact_candidate_comparisons']}),flush=True)
    summary['elapsed_seconds']=round(time.monotonic()-start,3)
    summary['algorithm']='precision-doubling prime-power roots; CRT; exact square-digit-length endpoint inversion; exact rotation comparison'
    summary['scope']='Complete for each audited k and every m>k with R_(m,k)<H_k^2. Guaranteed subregion D(m)<=2D(k)-2digits(k). Finite audit, not proof of infinite absence.'
    source=Path(__file__).read_bytes(); summary['script_sha256']=hashlib.sha256(source).hexdigest()
    out={'summary':summary,'local_survivor_branch_certificates':records}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
