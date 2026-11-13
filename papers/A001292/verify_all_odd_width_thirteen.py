#!/usr/bin/env python3
import json
from pathlib import Path
from verify_antiperiodic_thirteen import prefix
N={2,5,6,7,8,11}
def coeff(d):
    s=d%6;a=(d-s)//6
    return {1:(10,5*a),3:(7,5*a+5),5:(4,5*a+11)}[s]
def condition(m,d):
    alpha,c=coeff(d)
    return m%27==18 and m%2==0 and (alpha*m+c)%13 in N

def run():
    phases=[]
    for d in range(1,78,2):
        alpha,c=coeff(d);cs=[m for m in range(702) if condition(m,d)]
        assert len(cs)==6
        phases.append(dict(width_mod78=d,alpha=alpha,constant=c%13,classes_mod702=cs))
    w13=w27=D=0;P13=[0];P27=[0];Ds=[0];direct=0;chosen3=[];chosen5=[]
    for m in range(1,100000):
        d=len(str(m));D+=d
        w13=(pow(10,d,13)*w13+m)%13;w27=(pow(10,d,27)*w27+m)%27
        P13.append(w13);P27.append(w27);Ds.append(D)
        assert w27==(m*(m+1)//2+9*d*((m+1)//3))%27
        if d%2 and m%6==0:
            alpha,c=coeff(d);assert w13==(alpha*m+c)%13;direct+=1
        if d==3 and condition(m,d):chosen3.append(m)
        if d==5 and condition(m,d) and len(chosen5)<3:chosen5.append(m)
    rotations=0
    for m in chosen3+chosen5:
        assert Ds[m]%6==0
        for k in range(m):
            r13=(pow(10,Ds[k],13)*P13[m]-(pow(10,Ds[m],13)-1)*P13[k])%13
            r27=(pow(10,Ds[k],27)*P27[m]-(pow(10,Ds[m],27)-1)*P27[k])%27
            assert r13 in N and r27==9;rotations+=1
    selected=0
    for d in (7,9,11,13,15,17,25,27,29,75,77,79):
        L=10**(d-1);first=L+(-L)%6;alpha,c=coeff(d)
        for i in range(4):
            m=first+6*i;assert prefix(m,13)==(alpha*m+c)%13;selected+=1
    data=dict(width_phases=phases,general_mod27_checks=99999,direct_linear_prefix_checks=direct,selected_larger_prefix_checks=selected,certified_three_digit_endpoints=chosen3,selected_five_digit_endpoints=chosen5,individual_modular_rotation_checks=rotations)
    Path(__file__).with_name('all-odd-width-thirteen-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('39 width phases and six endpoint classes per phase: PASS')
    print('General mod27 prefix checks:',99999)
    print('Direct linear prefix checks:',direct)
    print('Selected larger-width prefixes:',selected)
    print('Three-digit endpoints:',chosen3)
    print('Selected five-digit endpoints:',chosen5)
    print('Individual modular rotation checks:',rotations)
    print('PASS. Infinite-width and whole-block claims follow from the proof.')
if __name__=='__main__':run()
