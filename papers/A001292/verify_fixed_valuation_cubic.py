#!/usr/bin/env python3
import json
from pathlib import Path
from verify_antiperiodic_thirteen import power,append,prefix

def run():
    M=243;I=[[1,0,0],[0,1,0],[0,0,1]];V=0;Vone=1;table={};prior={}
    for d in range(1,28):
        prior[d%27]=V;L=pow(10,d-1,M)
        A=[[pow(10,d,M),1,0],[0,1,1],[0,0,1]]
        assert power(A,243,M)==I
        allowed=[];R=(pow(10,d,M)-1)//9
        for m in range(M):
            w=append(V,L,(m-L+1)%M,d,M)
            if w in (27,216) and (d*(m+1)-R)%27==0:allowed.append(m)
        table[d%27]=allowed
        V=append(V,L,9*L%M,d,M);Vone=append(Vone,L,9*L%M,d,M)
    assert V==0 and Vone==1
    expected={r:[] for r in range(27)}
    for ds,ms in [([0],[53,54,188,189]),([1,10,19],[27,216]),([3,12,21],[108,216]),([4,13,22],[54,108]),([6,15,24],[27,135]),([7,16,25],[135,189]),([9,18],[54,189])]:
        for d in ds:expected[d]=ms
    assert table==expected
    cubes={pow(x,3,37) for x in range(1,37)}
    w=D=0;direct=0
    for m in range(1,100000):
        d=len(str(m));D+=d;w=(pow(10,d,243)*w+m)%243
        assert ((w in(27,216) and D%27==0)==(m%243 in table[d%27]));direct+=1
    rows=[];rotations=0
    for d in (3,4,6):
        L=10**(d-1);m=L
        while True:
            if m%243 in table[d%27] and prefix(m,37) not in cubes|{0}:break
            m+=1
        mod=243*37;w=0;D=0;ws=[0];ds=[0]
        for i in range(1,m+1):
            j=len(str(i));D+=j;w=(pow(10,j,mod)*w+i)%mod;ws.append(w);ds.append(D)
        assert D%27==0
        for k in range(m):
            r=(pow(10,ds[k],mod)*w-(pow(10,D,mod)-1)*ws[k])%mod
            assert r%243 in (27,216) and r%37 not in cubes|{0};rotations+=1
        rows.append(dict(width=d,endpoint=m,prefix_mod243=w%243,prefix_mod37=w%37))
    data=dict(complete_table={str(k):table[k] for k in range(27)},matrix_phases=27,table_cells=6561,direct_endpoint_checks=direct,selected_global_certificates=rows,individual_modular_rotation_checks=rotations)
    Path(__file__).with_name('fixed-valuation-cubic-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('27 matrix phases, full boundary cycle and6561 local table cells: PASS')
    print('Direct endpoint/length checks:',direct)
    print('Selected global endpoints:',rows)
    print('Individual modular rotation checks:',rotations)
    print('PASS. Complete classification is restricted to exact valuation3 Q3-cube blocks.')
if __name__=='__main__':run()
