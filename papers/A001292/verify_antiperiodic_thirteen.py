#!/usr/bin/env python3
import json
from pathlib import Path

def mul(a,b,mod):
    return [[sum(a[i][k]*b[k][j] for k in range(3))%mod for j in range(3)] for i in range(3)]
def power(a,n,mod):
    r=[[1,0,0],[0,1,0],[0,0,1]]
    while n:
        if n&1:r=mul(r,a,mod)
        a=mul(a,a,mod);n//=2
    return r
def append(w,u,n,d,mod):
    p=power([[pow(10,d,mod),1,0],[0,1,1],[0,0,1]],n,mod)
    return (p[0][0]*w+p[0][1]*u+p[0][2])%mod

def prefix(m,mod):
    w=0;u=1;d=1
    while u<=m:
        w=append(w,u,min(m,10*u-1)-u+1,d,mod);u*=10;d+=1
    return w

def run():
    I=[[1,0,0],[0,1,0],[0,0,1]];translations=[]
    for j in range(2,8):
        A=[[pow(10,j,13),1,0],[0,1,1],[0,0,1]]
        assert power(A,78,13)==I
        u=10**(j-1);n=9*u
        f0=append(0,u,n,j,13);f1=append(1,u,n,j,13)
        assert (f1-f0)%13==1
        assert pow(10,j-1,78)==pow(10,j+5,78)
        translations.append(f0)
    assert translations==[5,8,11,4,7,12]
    assert sum(translations)%13==8
    assert (-prefix(99,13)+100*7)%13==5
    N={x for x in range(13) if pow(x,6,13)==12};assert N=={2,5,6,7,8,11}
    classes=[]
    for a in range(13):
        cs=[m for m in range(702) if m%27 in (8,18) and m%2==0 and (m//2+5*(a+1))%13 in N]
        assert len(cs)==12;classes.append(dict(width_mod78=3+6*a,endpoint_classes_mod702=cs))
    w13=w27=0;D=0;prefixes13=[0];prefixes27=[0];lengths=[0];certified=[];direct=0
    for m in range(1,1000):
        d=len(str(m));D+=d
        w13=(pow(10,d,13)*w13+m)%13;w27=(pow(10,d,27)*w27+m)%27
        if m<1000:
            prefixes13.append(w13);prefixes27.append(w27);lengths.append(D)
        if d==3 and m%2==0:
            assert w13==(m//2+5)%13;direct+=1
        if d==3 and m%27 in (8,18) and m%2==0 and (m//2+5)%13 in N:certified.append(m)
    rotations=0
    for m in certified:
        for k in range(m):
            r13=(pow(10,lengths[k],13)*prefixes13[m]-(pow(10,lengths[m],13)-1)*prefixes13[k])%13
            r27=(pow(10,lengths[k],27)*prefixes27[m]-(pow(10,lengths[m],27)-1)*prefixes27[k])%27
            assert r13 in N and r27==9;rotations+=1
    selected=0
    for d in (9,15,21,27,33,75,81):
        a=(d-3)//6;L=10**(d-1)
        for i in range(6):
            m=L+2*i
            assert prefix(m,13)==(m//2+5*(a+1))%13;selected+=1
    data=dict(matrix_translations=translations,width_phases=classes,three_digit_certified_endpoints=certified,direct_three_digit_even_prefix_checks=direct,selected_larger_prefix_checks=selected,individual_rotation_modular_checks=rotations)
    Path(__file__).with_name('antiperiodic-thirteen-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Six exact matrix phases/translations and13 width-class counts: PASS')
    print('Direct three-digit even prefix checks:',direct)
    print('Selected larger-width prefix checks:',selected)
    print('Certified three-digit endpoints:',len(certified))
    print('Individual rotation checks modulo27 and13:',rotations)
    print('PASS. Infinite-width claims follow from the proof, not extrapolation.')
if __name__=='__main__':run()
