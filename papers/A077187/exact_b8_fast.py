"""Exact 3^8 cyclotomic group ring; zero floating point operations."""
import sys,time
from math import gcd
from functools import lru_cache
from pathlib import Path
import numpy as np
import sympy as sp
from scalar_reference import primitive_root_of_order,polyforms
sys.set_int_max_str_digits(0)
T=729; DEG=486; D=200*T*T
x=sp.Symbol('x'); PHI=sp.Poly(x**486+x**243+1,x)

@lru_cache(None)
def cyc_conv_base(n):
    arr=np.arange(n,dtype=np.int64)
    raw=np.convolve(arr,arr)
    ans=np.zeros(n,dtype=np.int64)
    ans[:n]+=raw[:n]
    ans[:n-1]+=raw[n:]
    return ans

@lru_cache(None)
def sums(j):
    g=gcd(j,T); n=T//g
    k=np.arange(n,dtype=np.int64)
    h=np.zeros(T,dtype=np.int64)
    h[(j*(k+1))%T]=g*k
    h2=np.zeros(T,dtype=np.int64)
    h2[(j*(k+1))%T]=g*g*cyc_conv_base(n)
    return h,h2

def shift(a,i):return np.roll(a,i)

def red(a):
    a=np.array(a,dtype=object)
    for i in range(DEG,T):
        v=a[i]; a[i-243]-=v; a[i-486]-=v
    return [int(v) for v in a[:DEG]]

def mon(e):
    v=np.zeros(T,dtype=np.int64); v[e%T]=1
    return v

def coefficients(gamma):
    assert gamma%3
    U=np.zeros((3,T),dtype=np.int64); V=np.zeros((3,T),dtype=np.int64)
    U[0,0]=99*T*T; V[0,0]=-81*T*T
    U[1,0]=-90*T*T; V[1,0]=90*T*T
    Ej=0; power=1
    for j in range(1,T):
        prev=Ej; Ej=(Ej+j*power)%T
        alphaexp=gamma*j*power%T
        eu=-gamma*Ej%T; ev=gamma*prev%T
        H,H2=sums(j)
        one=mon(0); alpha=mon(alphaexp); am1=alpha-one
        U[1]+=shift(D*am1-180*T*shift(H,alphaexp),eu)
        U[2]+=shift(200*(shift(H2,alphaexp)-H2),eu)
        V[1]+=shift(200*T*shift(H,alphaexp)-20*T*H,ev)
        V[2]+=shift(200*(H2-shift(H2,alphaexp)),ev)
        power=power*10%T
    return [red(row) for row in U],[red(row) for row in V]

def ring_mul(a,b):
    aa=np.array(a,dtype=object);bb=np.array(b,dtype=object)
    out=np.convolve(aa,bb)
    out=np.concatenate((out,np.array([0],dtype=object)))
    for i in range(T,len(out)):out[i-T]+=out[i]
    return red(out[:T])

def sub(a,b):return [x-y for x,y in zip(a,b)]

def resultant_poly(U,V):
    A=sub(ring_mul(U[2],V[0]),ring_mul(U[0],V[2]))
    B=sub(ring_mul(U[2],V[1]),ring_mul(U[1],V[2]))
    C=sub(ring_mul(U[1],V[0]),ring_mul(U[0],V[1]))
    return sub(ring_mul(A,A),ring_mul(B,C))

def crosscheck(gamma,p=1459,z=9):
    if pow(z,T,p)!=1 or pow(z,T//3,p)==1:
        z=primitive_root_of_order(p,T)
    U,V=coefficients(gamma)
    refu,refv=polyforms(T,gamma,p,z)
    def ev(a):return sum(c*pow(z,i,p) for i,c in enumerate(a))%p
    for i in range(3):
        assert ev(U[i])==refu[i]*D%p,(gamma,'U',i)
        assert ev(V[i])==refv[i]*D%p,(gamma,'V',i)
    R=resultant_poly(U,V)
    a,b,c=refu;d,e,f=refv
    rr=((c*d-a*f)**2-(c*e-b*f)*(b*d-a*e))%p
    assert ev(R)==rr*pow(D,4,p)%p
    return R

if __name__=='__main__':
    g=int(sys.argv[1]) if len(sys.argv)>1 else 1
    R=crosscheck(g)
    print('phase',g,'nonzero',any(R),'maxcoefficient',max(map(abs,R)))
