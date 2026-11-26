#!/usr/bin/env python3
"""Complete certificate-condition scan, not an exhaustive perfect-power search."""
import json,math
from pathlib import Path
from verify_cyclic_jacobi_certificate import jacobi,v3
LOW,HIGH=5001,10000

def run():
    try:
        from sympy import jacobi_symbol
    except ImportError:jacobi_symbol=None
    W=0;D=0;records=[];eligible=0;cross=0;cuts=0;symbols={-1:0,0:0,1:0}
    for m in range(1,HIGH+1):
        prevW,prevD=W,D;d=len(str(m));W=W*10**d+m;D+=d
        if m<LOW:continue
        b,z=v3(W);a=2+v3(D)[0]
        if b<2 or b&(b-1) or a<=b or z%3!=1:continue
        eligible+=1;Delta=10**D-1;M=Delta//3**a;J=jacobi(z,M);symbols[J]+=1
        if jacobi_symbol is not None:
            assert J==int(jacobi_symbol(z,M));cross+=1
        if J!=-1:continue
        assert math.gcd(W,Delta)==3**b and jacobi(10,M)==1
        for k,Wk,Dk in ((1,1,1),(m-1,prevW,prevD)):
            R=10**Dk*W-Delta*Wk;v,u=v3(R)
            assert v==b and u%3==1
            assert u%M==(pow(10,Dk,M)*z)%M
            cuts+=1
        records.append(dict(endpoint=m,digits=D,v3_delta=a,v3_prefix=b,unit_mod9=z%9,jacobi=-1,common_gcd=3**b))
    by_b={str(b):sum(r['v3_prefix']==b for r in records) for b in sorted({r['v3_prefix'] for r in records})}
    data=dict(endpoint_interval=[LOW,HIGH],endpoints_scanned=HIGH-LOW+1,valuation_eligible=eligible,jacobi_counts={str(k):v for k,v in symbols.items()},certified_blocks=len(records),by_valuation=by_b,rotations_covered_by_theorem=sum(r['endpoint'] for r in records),selected_cut_checks=cuts,optional_sympy_cross_checks=cross,certificates=records)
    Path(__file__).with_name('jacobi-endpoint-range-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    for key in data:
        if key!='certificates':print(key+':',data[key])
    print('PASS. Every block conclusion is by theorem; no perfect-power conclusion is drawn for uncertified endpoints.')

if __name__=='__main__':run()
