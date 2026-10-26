#!/usr/bin/env python3
from itertools import groupby
from math import comb


def exact(n):
    q=sum(comb(n-3*i,2*i-1) for i in range(1,(n+1)//5+1))
    r=sum(comb(n-3*i+2,2*i-2)+comb((n-5*i+4)//2+i-1,i-1)
          for i in range(1,(n+4)//5+1))
    s=sum(comb(n-3*i-2,2*i)+comb((n-5*i-2)//2+i,i)
          for i in range(1,(n-2)//5+1))
    assert (r+s)%2==0
    return 1+q+(r+s)//2


def main():
    values=[0]+[exact(n) for n in range(1,1001)]
    published=[2,2,2,3,4,6,9,13,19,28,42,63,95,143,216,327,496,
               754,1147,1747,2662,4059,6192,9450,14428,22034,33658,
               51422,78573,120073,183510,280485,428733,655371,1001854,
               1531567,2341417,3579571,5472565,8366756]
    assert values[1:41]==published
    denominator=[1,-2,0,2,-1,-2,2,0,0,0,1]
    numerator=[0,2,-2,-2,3,0,-4,1,0,-1,0,1]
    for n in range(1001):
        got=sum(v*values[n-i] for i,v in enumerate(denominator) if i<=n)
        assert got==(numerator[n] if n<len(numerator) else 0),(n,got)
    assert values[11]-(2*values[10]-2*values[8]+values[7]+2*values[6]-2*values[5]-values[1])==1
    print('PASS exact established binomial formula, all40official terms and rational GF through n=1000')
    print('PASS recurrence from n=12 and explicit n=11 defect1')
    for n in range(1,19):
        representatives=set()
        for mask in range(1<<n):
            word=format(mask,f'0{n}b')
            runs=[(bit,len(list(g))) for bit,g in groupby(word)]
            if len(runs)>1:
                valid=all(length >= (2 if bit=='0' or i in (0,len(runs)-1) else 3)
                          for i,(bit,length) in enumerate(runs))
                if not valid:
                    continue
            representatives.add(min(word,word[::-1]))
        assert len(representatives)==values[n],(n,len(representatives),values[n])
    print('PASS independent binary-state/reflection-orbit enumeration for all n<=18')


if __name__=='__main__':main()
