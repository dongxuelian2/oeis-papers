#!/usr/bin/env python3
"""Independent tests of stable candidate verifier; no network or uploads."""
import bisect, hashlib, importlib.util, json, math, random, sys, time
from pathlib import Path
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('target',HERE/'verify_late_prefix_candidates.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
summary={}; start=time.monotonic()
def note(k,value):
    summary[k]=value
    print(json.dumps({k:value}),flush=True)

# A single residue-square table per modulus independently gives every root set.
cases=0
for p,limit in ((2,14),(5,7)):
    for n in range(1,limit+1):
        q=p**n; expected={}
        for r in range(q):
            if r%p:expected.setdefault(r*r%q,[]).append(r)
        for u in range(1,q):
            if u%p:
                assert v.unit_roots(u,p,n)==expected.get(u,[]),(p,n,u)
                cases+=1
note('exhaustive_unit_residue_cases',cases)

# Large exponent tests know a square root before invoking the target solver.
rng=random.Random(20261107);cases=0
for p in (2,5):
    for n in (1,2,3,4,5,7,8,9,15,16,17,31,32,33,63,64,65,127,128,129,257,513,1025,4097,40001):
        q=p**n
        for _ in range(3):
            r=rng.randrange(1,q)
            while r%p==0:r=rng.randrange(1,q)
            u=r*r%q
            expected=sorted({r,-r%q}) if p==5 or n<=2 else sorted({r,(-r)%q,(r+q//2)%q,(-r+q//2)%q})
            assert v.unit_roots(u,p,n)==expected,(p,n)
            assert v.unit_roots(u+q*rng.randrange(1,100),p,n)==expected
            cases+=2
note('known_square_high_precision_cases',cases)

# Complete decimal congruences, with all roots independently tabulated.
cases=0
for s in range(1,5):
    modulus=10**s; expected={}
    for y in range(modulus):expected.setdefault(y*y%modulus,[]).append(y)
    for U in range(1,modulus):
        def val(n,p):
            e=0
            while not n%p:n//=p;e+=1
            return e
        v2,v5=val(U,2),val(U,5)
        if max(v2,v5)>=s:continue
        H,roots,vals=v.compressed_roots(U,s)
        full=expected.get(U,[])
        assert vals==(v2,v5)
        if v2%2 or v5%2:
            assert H is None and roots==[] and full==[]
        else:
            correct_H=2**(s-v2//2)*5**(s-v5//2)
            assert H==correct_H
            assert roots==sorted({y%H for y in full})
            assert sorted(r+j*H for r in roots for j in range(modulus//H))==full
        cases+=1
note('exhaustive_compressed_decimal_cases',cases)

# Prefixes and digit counts come from decimal string concatenation / a recurrence,
# not the arithmetic-geometric formula or digit-width inversion.
prefix_text=['']; D=[0]
for m in range(1,20001):
    D.append(D[-1]+len(str(m)))
    if m<=2100:prefix_text.append(prefix_text[-1]+str(m))
for m,text in enumerate(prefix_text):
    assert v.prefix(m)==(int(text) if text else 0)
    assert v.D(m)==len(text)
note('direct_string_prefix_cases',len(prefix_text))
by_digits={d:m for m,d in enumerate(D)}
for E in range(D[-1]+1):
    assert v.endpoint_from_digit_count(E)==(by_digits.get(E) if E else None),E
    assert v.endpoint_at_most_digits(E)==bisect.bisect_right(D,E)-1,E
note('exhaustive_digit_inversion_lengths',D[-1]+1)

certificate=json.loads((HERE/'late-prefix-1000-certificate.json').read_text())
cert_records={r['k']:r for r in certificate['local_survivor_branch_certificates']}
count=0;local_count=0;branches=0;comparisons=0;gaps=0;early=0;local_cuts=0;crossing=0;naive=0
for k in range(10,1001):
    text=prefix_text[k];U=int(text);s=len(text);w=len(str(k))
    H,roots,vals=v.compressed_roots(U,s)
    J=k*(10**w-1)+10**w
    assert vals==(val(J,2),val(J,5))
    assert 2**vals[0]*5**vals[1]<=J<10**(2*w)
    Emax=2*s-2*w
    end=bisect.bisect_right(D,Emax)-1
    # In a second implementation, enumerate/count every covered endpoint.
    independent_count=sum(1 for m in range(k+1,2101) if D[m]<=Emax)
    assert independent_count==max(0,end-k)
    count+=independent_count
    # Independent local-square existence test plus number of classes.
    exists=not any(e%2 for e in vals)
    if exists:
        n2=s-vals[0];n5=s-vals[1]
        u2=U//2**vals[0];u5=U//5**vals[1]
        exists=(u2%min(8,2**n2)==1 and u5%5 in (1,4))
    assert bool(roots)==exists
    if roots:
        assert len(roots)==8 and len(set(roots))==8
        assert 0<min(roots)<=max(roots)<H
        assert all((r*r-U)%10**s==0 for r in roots)
        assert 10**Emax<H*H
        local_cuts+=1;local_count+=independent_count;branches+=len(roots)
        crossing+=len(str(end))>w
        expected=[]
        for i,r in enumerate(roots):
            square=r*r;E=len(str(square));m=by_digits.get(E)
            if m is None:
                expected.append({'branch':i,'kind':'digit_gap','square_digits':E});gaps+=1
            elif m<=k:
                expected.append({'branch':i,'kind':'endpoint_not_after_cut','m':m});early+=1
            else:
                # Construct rotation by a literal string splice, independently
                # of both target prefix() and target rotation().
                direct_R=int(prefix_text[m][s:]+text)
                assert len(str(direct_R))==D[m]
                sign=(square>direct_R)-(square<direct_R)
                assert sign!=0,(m,k)
                expected.append({'branch':i,'kind':'exact_comparison','m':m,'square_minus_rotation_sign':sign});comparisons+=1
        record=cert_records[k]
        assert record['branches']==expected,(k,record,expected)
        assert record['guaranteed_endpoint']==end
        assert record['prefix_digits']==s and record['valuations']==list(vals)
    else:assert k not in cert_records
    if k<=99:
        for m in range(k+1,end+1):
            R=int(prefix_text[m][s:]+text);root=math.isqrt(R)
            assert root*root!=R,(m,k)
            naive+=1
checks={'guaranteed_pairs_all_cuts':count,'guaranteed_pairs_local_survivor_cuts':local_count,'local_survivor_cuts':local_cuts,'root_branches':branches,'exact_candidate_comparisons':comparisons,'digit_gap_rejections':gaps,'not_after_cut_rejections':early,'width_crossing_survivor_cuts':crossing,'naive_crosscheck_pairs':naive}
for key,value in checks.items():assert certificate['summary'][key]==value,(key,value)
note('independently_reproduced_1000_counts',checks)
assert hashlib.sha256((HERE/'verify_late_prefix_candidates.py').read_bytes()).hexdigest()==certificate['summary']['script_sha256']
summary['target_script_sha256']=certificate['summary']['script_sha256']
summary['elapsed_seconds']=round(time.monotonic()-start,3)
summary['result']='All independent mathematical and program checks passed. Finite audit only.'
(HERE/'late-prefix-independent-audit-results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
