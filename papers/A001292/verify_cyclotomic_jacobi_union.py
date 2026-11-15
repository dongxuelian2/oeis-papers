#!/usr/bin/env python3
"""Finite CRT and prefix audits, not an empirical asymptotic claim."""
import json,math
from pathlib import Path
from verify_cyclic_jacobi_certificate import jacobi,v3
from verify_cyclotomic_jacobi_family import prefix

def Q(j):
    x=10**(3**(j-1));return (x*x+x+1)//3

def run():
    models=[]
    for mods in ((11,19),(11,19,43),(19,43,59)):
        T=math.prod(mods)
        for shift in range(3):
            allowed=[]
            for i,n in enumerate(mods):
                c=3*i+shift
                allowed.append([jacobi((m*(m+1)//2+c)%n,n)!=-1 for m in range(n)])
            count=sum(all(mask[(666+999*t)%n] for mask,n in zip(allowed,mods)) for t in range(T))
            expected=math.prod(sum(mask) for mask in allowed)
            assert count==expected
            models.append(dict(moduli=mods,shift=shift,period=T,joint_survivors=count,product_count=expected))
    rows=[];prefix_checks=0
    for d in (9,27,36,81,108):
        h=v3(d)[0];q=3**h
        assert pow(d%37,18,37)==1
        allmods=[Q(j) for j in range(2,h+1)]
        for i,a in enumerate(allmods):
            assert math.gcd(a,999)==1 and jacobi(10,a)==1
            for b in allmods[:i]:assert math.gcd(a,b)==1
        period=999*math.prod(allmods)
        assert period==3*(10**q-1)//q
        B=10**d;L=B//10;J=max(2,(h+1)//2);mods=[Q(j) for j in range(J,h+1)]
        modulus=math.prod(mods);c=(prefix(L-1,modulus)-L*(L-1)//2)%modulus
        first=666+max(0,(L-666+998)//999)*999
        unions=top=0;selected=[];added=[]
        for i in range(200):
            m=first+999*i;assert m<B
            signs=[jacobi((m*(m+1)//2+c)%a,a) for a in mods]
            success=-1 in signs;unions+=success;top+=signs[-1]==-1
            if success and len(selected)<3:selected.append(m)
            if success and signs[-1]!=-1 and len(added)<3:added.append(m)
        for m in sorted(set(selected+added)):
            W=prefix(m,modulus)
            assert W==(m*(m+1)//2+c)%modulus
            assert any(jacobi(W,a)==-1 for a in mods)
            assert prefix(m,27)==9 and pow(prefix(m,37),18,37)==1
            D=d*(m+1)-(B-1)//9
            assert D%q==0 and pow(10,D,modulus)==1
            prefix_checks+=1
        rows.append(dict(width=d,v3_width=h,three_part=q,first_index=J,joint_period=period,sample_endpoints=200,sample_union_certificates=unions,sample_top_only_certificates=top,selected_prefix_checks=sorted(set(selected+added))))
    data=dict(exact_crt_models=models,actual_width_samples=rows,selected_prefix_checks=prefix_checks)
    Path(__file__).with_name('cyclotomic-jacobi-union-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Exact CRT model counts:',len(models))
    for r in rows:print('Width',r['width'],'sample union/top:',r['sample_union_certificates'],r['sample_top_only_certificates'],'out of',r['sample_endpoints'])
    print('Selected exact prefix checks:',prefix_checks)
    print('PASS. Sample rates are not used to prove or estimate the infinite coverage bound.')

if __name__=='__main__':run()
