#!/usr/bin/env python3
"""Independent low-cost coverage/local-obstruction audit, not root enumeration."""
import bisect,json,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
start=time.monotonic(); cap=10000;D=[0]
for m in range(1,2*cap+1):D.append(D[-1]+len(str(m)))
def vp(n,p):
    a=0
    while n%p==0:n//=p;a+=1
    return a
counts={'max_cut':cap,'valuation_identity_and_smooth_bound_checks':0,'guaranteed_pairs_all_cuts':0,'guaranteed_pairs_local_survivor_cuts':0,'odd_valuation_cuts':0,'unit_obstructed_cuts':0,'local_survivor_cuts':0,'implied_root_branches':0,'width_crossing_survivor_cuts':0}
U=0
for k in range(1,cap+1):
    w=len(str(k));U=U*10**w+k
    if k<10:continue
    s=D[k];a=vp(U,2);b=vp(U,5);J=k*(10**w-1)+10**w
    assert (a,b)==(vp(J,2),vp(J,5)),k
    smooth=2**a*5**b
    assert smooth<=J<10**(2*w) and max(a,b)<s,k
    counts['valuation_identity_and_smooth_bound_checks']+=1
    E=2*s-2*w;end=bisect.bisect_right(D,E)-1
    assert D[end]<=E<D[end+1]
    n=max(0,end-k);counts['guaranteed_pairs_all_cuts']+=n
    if a%2 or b%2:counts['odd_valuation_cuts']+=1
    elif U//2**a%8!=1 or U//5**b%5 not in (1,4):counts['unit_obstructed_cuts']+=1
    else:
        assert s-a>=3 and s-b>=1
        counts['local_survivor_cuts']+=1
        counts['implied_root_branches']+=8
        counts['guaranteed_pairs_local_survivor_cuts']+=n
        counts['width_crossing_survivor_cuts']+=len(str(end))>w
        H=10**s//(2**(a//2)*5**(b//2))
        assert 10**E<H*H
counts['elapsed_seconds']=round(time.monotonic()-start,3)
counts['scope']='Independent local-obstruction and guaranteed-coverage counts only. No claim to have independently rerun cut-10000 root enumeration.'
Path(__file__).with_name('late-prefix-independent-coverage-10000-results.json').write_text(json.dumps(counts,indent=2)+'\n')
print(json.dumps(counts,indent=2))
