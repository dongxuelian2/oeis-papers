#!/usr/bin/env python3
import json
from pathlib import Path
from verify_antiperiodic_thirteen import prefix,power,append

def char(x,p):
    t=pow(x%p,(p-1)//2,p);return -1 if t==p-1 else t

def f37(m,d):
    s=d%3;a=(d-s)//3
    return ((4*m+33*a) if s==1 else (34*m+26+33*a) if s==2 else m*(m+1)//2+11*d)%37

def f13(m,d):
    s=d%6;a=(d-s)//6
    alpha,c={1:(10,5*a),3:(7,5*a+5),5:(4,5*a+11)}[s]
    return (alpha*m+c)%13

def run():
    I=[[1,0,0],[0,1,0],[0,0,1]];trans=[]
    for j in (2,3,4):
        A=[[pow(10,j,37),1,0],[0,1,1],[0,0,1]]
        assert power(A,111,37)==I
        u=10**(j-1);z=append(0,u,9*u,j,37)
        assert (append(1,u,9*u,j,37)-z)%37==1;trans.append(z)
    assert trans==[26,8,36] and sum(trans)%37==33
    phases=[]
    for d in range(1,112):
        n=sum(char(f37(m,d),37)==-1 for m in range(37))
        delta=(1-88*d)%37
        expected=18 if d%3 else (36 if not delta else 17 if char(delta,37)==1 else 18)
        assert n==expected
        cs=[m for m in range(999) if m%27==18 and char(f37(m,d),37)==-1]
        assert len(cs)==n
        phases.append(dict(width_mod111=d%111,classes_mod999=cs,negative_residues=n))
    unions=[]
    for d in range(1,223,2):
        n=sum(char(f37(m,d),37)==-1 for m in range(37))
        count=sum(m%27==18 and (char(f37(m,d),37)==-1 or (m%2==0 and char(f13(m,d),13)==-1)) for m in range(25974))
        assert count==20*n+222
        unions.append(dict(width_mod222=d%222,union_count=count))
    w37=w27=D=0;P37=[0];P27=[0];Ds=[0];direct=0;chosen=[]
    for m in range(1,100000):
        d=len(str(m));D+=d
        w37=(pow(10,d,37)*w37+m)%37;w27=(pow(10,d,27)*w27+m)%27
        P37.append(w37);P27.append(w27);Ds.append(D)
        if m%3==0:assert w37==f37(m,d);direct+=1
        if m%27==18 and char(w37,37)==-1 and (d==2 or (d==4 and len(chosen)<5)):chosen.append(m)
    rotations=0
    for m in chosen:
        assert Ds[m]%3==0
        for k in range(m):
            r37=(pow(10,Ds[k],37)*P37[m]-(pow(10,Ds[m],37)-1)*P37[k])%37
            r27=(pow(10,Ds[k],27)*P27[m]-(pow(10,Ds[m],27)-1)*P27[k])%27
            assert char(r37,37)==-1 and r27==9;rotations+=1
    selected=0
    for d in (6,7,8,9,10,11,36,37,38,110,111,112):
        L=10**(d-1);first=L+(-L)%3
        for i in range(4):
            m=first+3*i;assert prefix(m,37)==f37(m,d);selected+=1
    data=dict(matrix_translations=trans,width_phases=phases,odd_width_unions=unions,direct_prefix_checks=direct,selected_larger_prefix_checks=selected,selected_certified_endpoints=chosen,individual_modular_rotation_checks=rotations)
    Path(__file__).with_name('all-width-thirty-seven-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Three matrix phases,111 width phases and111 odd-width CRT unions: PASS')
    print('Direct multiple-of3 prefix checks:',direct)
    print('Selected larger-width prefixes:',selected)
    print('Selected certified endpoints:',chosen)
    print('Individual modular rotation checks:',rotations)
    print('PASS. All-width conclusions follow from the proof, not finite extrapolation.')
if __name__=='__main__':run()
