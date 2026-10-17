"""Exact norm in Q(zeta_(3^n)) via cubic relative norm tower."""
from pathlib import Path
from time import monotonic
import sys,numpy as np
sys.set_int_max_str_digits(0)
def reduce_poly(poly,n):
    m=3**(n-1);t=3*m;d=2*m
    c=list(map(int,poly))
    if len(c)<t:c.extend([0]*(t-len(c)))
    for i in range(len(c)-1,d-1,-1):
        val=c[i]
        if val:
            if i>=t:c[i-t]+=val
            else:c[i-m]-=val;c[i-2*m]-=val
    return c[:d]
def mul_poly(a,b,n):
    return reduce_poly(np.convolve(np.array(a,dtype=object),np.array(b,dtype=object)),n)
def relative(coeff,n):
    assert n>=2 and len(coeff)==2*3**(n-1)
    target=n-1
    A=coeff[0::3];B=coeff[1::3];C=coeff[2::3]
    def mul(a,b):return mul_poly(a,b,target)
    def shift(a,i):return reduce_poly([0]*i+a,target)
    aa=mul(A,A);bb=mul(B,B);cc=mul(C,C)
    a3=mul(aa,A);b3=mul(bb,B);c3=mul(cc,C)
    abc=mul(mul(A,B),C)
    return [v+u+w-3*z for v,u,w,z in zip(a3,shift(b3,1),shift(c3,2),shift(abc,1))]
def full_norm(R,n=6,logs=False):
    t=monotonic();coeff=list(map(int,R))
    for step in range(n,1,-1):
        coeff=relative(coeff,step)
        if logs:print('level',step,'to',step-1,'degree',len(coeff),'elapsed',monotonic()-t,flush=True)
    assert len(coeff)==2
    a,b=coeff;ans=a*a-a*b+b*b
    return ans
if __name__=='__main__':
    from exact_b8_fast import crosscheck
    g=int(sys.argv[1]) if len(sys.argv)>1 else 1
    n=full_norm(crosscheck(g),6,logs=True)
    for q in (2,3,5):
        while n%q==0:n//=q
    (Path(__file__).parent/f'norm_gamma_{g}.txt').write_text(str(n)+'\n')
    print('PHASE',g,'Ndigits',len(str(n)))
