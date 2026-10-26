#!/usr/bin/env python3
from fractions import Fraction as Q
from math import comb
from pathlib import Path


def coefficients(length):
    b=[Q(1)]
    for n in range(1,length):
        b.append(-sum(comb(n,k)*4**k*b[n-k] for k in range(1,n+1))/2)
    a=[Q(1)]
    for n in range(1,length):
        a.append(sum(b[j]*a[n-j] for j in range(1,n+1))/n)
    return a


def gamma_recurrence(length):
    # G(x/(1+8x))=(1+4x)^2/(1+8x)*G(x).
    # At degree m+1, a_(m+1) cancels and the coefficient of a_m
    # on the left is -8m; no Euler or Bernoulli numbers are used.
    a=[Q(1)]
    for m in range(1,length):
        left=sum(a[j]*(-8)**(m+1-j)*comb(m,m+1-j) for j in range(1,m))
        right=sum(a[j]*16*(-8)**(m-1-j) for j in range(m))
        a.append((left-right)/(8*m))
    return a


def mul(a,b,length):
    return [sum(a[j]*b[n-j] for j in range(n+1)) for n in range(length)]


def compose_mobius(h,sign,c):
    # H(sign*x/(1+c*x)) through its known degree.
    out=[Q(0)]*len(h)
    for n in range(1,len(h)):
        out[n]=sum(h[j]*sign**j*(-c)**(n-j)*comb(n-1,n-j)
                   for j in range(1,n+1))
    return out


def main():
    pairs=[tuple(map(int,line.split())) for line in
           Path(__file__).with_name('b092635-published.txt').read_text().splitlines()
           if line.strip() and not line.startswith('#')]
    assert [n for n,_ in pairs]==list(range(301))
    a=coefficients(301)
    assert a==gamma_recurrence(301)==[Q(v) for _,v in pairs]
    assert all(v.denominator==1 for v in a)
    print('PASS all301official coefficients, independently from Euler exponential and exact gamma shift')
    h=[Q(0)]+a[:100]
    minus=[v*(-1)**n for n,v in enumerate(h)]
    target=[Q(0)]*len(h);target[2]=-1
    assert mul(h,minus,len(h))==target
    assert h==[-v for v in compose_mobius(h,-1,4)]
    target[2]=1
    assert mul(h,compose_mobius(h,1,-4),len(h))==target
    print('PASS all3formal reciprocal/substitution identities through degree100')


if __name__=='__main__':main()
