#!/usr/bin/env python3
import json
from fractions import Fraction as F
from pathlib import Path

def run():
    checks=earlier=later=0;samples=[]
    for w in (2,3):
        B=10**w;L=B//10;C=B-1;V=B-L
        W=[0];D=[0]
        for n in range(1,3*B//2+1):
            ell=len(str(n));W.append(W[-1]*10**ell+n);D.append(D[-1]+ell)
        t=D[L-1];G=10**t;P=D[B-1];A=C*C*W[L-1]+L*C+1
        assert P==t+w*V
        for m in (2*L,5*L,B-1,B,5*B//4,3*B//2):
            E=D[m]
            H=G*C*C*W[m]-A*(10**E-1)
            if m<B:
                N=m-L+1
                assert E==t+w*N and H==A-G*(m*C+B)
                assert abs(H)<2*G*B*B
            else:
                U=W[m]-W[B-1]*10**(E-P);Jend=C*C+B
                assert 0<=U<10**(E-P)
                assert H==A+G*(C*C*U-Jend*10**(E-P))
                assert H<0 and abs(H)<2*B*B*10**(E-w*V)
            Ms=max(t,E-w*V)
            for k in sorted({L+7,(L+B)//2,B-2,m-1}):
                if not L+7<=k<=B-2 or k>=m:continue
                K=k-L+1;J=k*C+B
                R=10**D[k]*W[m]-(10**E-1)*W[k]
                assert C*C*R==J*10**E+H*B**K-J
                assert (C*C*R+J)%B**K==0
                assert abs(H*B**K-J)<3*B**(K+2)*10**Ms
                assert abs(H*B**K-J)*B<=30*J*10**E
                assert R>0
                checks+=1;earlier+=m<B;later+=m>=B;samples.append([w,m,k])
    windows=0
    eps=F(1,10)
    for w in range(4,201):
        B=10**w;L=B//10;V=B-L;t=(w-1)*L-(L-1)//9
        for m in (B,3*B//2):
            E=(w+1)*(m+1)-(10*B-1)//9
            assert 2*t+eps*w*B<=E<=2*w*V-eps*w*B
            assert max(F(t)-F(E,2),F(E,2)-w*V)<=-eps*w*B/2
            windows+=1
    out=dict(exact_rotation_tail_checks=checks,same_width_checks=earlier,
             crossed_boundary_checks=later,rational_window_checks=windows,samples=samples)
    Path(__file__).with_name('cross-width-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Exact rotation/tail checks:',checks,'(same width:',earlier,'crossed boundary:',later,')')
    print('Rational window checks:',windows)
    print('PASS. Finite ingredients only; no ineffective exceptional sets are computed.')
if __name__=='__main__':run()
