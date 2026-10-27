#!/usr/bin/env python3
"""Independent exact checks for every-modulus periodicity of A006154."""
from math import comb, factorial, gcd, lcm
from pathlib import Path


def terms(limit):
    a=[1]
    for n in range(1,limit+1):
        a.append(sum(comb(n,j)*a[n-j] for j in range(1,n+1,2)))
    return a


def literal(size):
    def visit(left,blocks):
        if not left:
            return factorial(len(blocks)) if all(k%2 for k in blocks) else 0
        count=visit(left-1,blocks+[1])
        for j in range(len(blocks)):
            blocks[j]+=1
            count+=visit(left-1,blocks)
            blocks[j]-=1
        return count
    return visit(size,[])


def step(v,m):
    # D=c*d/ds+s*d/dc on R[s,c]/(s^m,c^m-1).
    w=[0]*(m*m)
    for i in range(m):
        for j in range(m):
            x=v[i*m+j]
            if i:
                w[(i-1)*m+(j+1)%m]+=i*x
            if i+1<m and j:
                w[(i+1)*m+j-1]+=j*x
    return tuple(x%m for x in w)


def period(m):
    remaining=m;answer=1;p=2
    while p*p<=remaining:
        q=1
        while remaining%p==0:
            remaining//=p;q*=p
        if q>1:
            answer=lcm(answer,q if p==2 else q//p*(p-1))
        p+=1
    if remaining>1:
        answer=lcm(answer,remaining if remaining==2 else remaining-1)
    return answer


def main():
    a=terms(600)
    rows=[tuple(map(int,line.split())) for line in
          Path(__file__).with_name('b006154-published.txt').read_text().splitlines()
          if line.strip() and not line.startswith('#')]
    assert [n for n,_ in rows]==list(range(201))
    assert [a[n] for n,_ in rows]==[v for _,v in rows]
    assert [literal(n) for n in range(9)]==a[:9]
    print('PASS all201official terms and literal ordered odd-block partitions through8elements')
    for m in range(2,33):
        u=tuple(int(j==0) for i in range(m) for j in range(m))
        v=u;states=[]
        for n in range(251):
            states.append(v)
            assert sum(v[:m])%m==a[n]%m,(m,n)
            v=step(v,m)
        phi=sum(gcd(j,m)==1 for j in range(1,m+1))
        p=period(m)
        assert (2*phi)%p==0 and (m%2==0 or phi%p==0)
        assert all((a[n+p]-a[n])%m==0 for n in range(m,601-p))
        if m in (2,3,5,7,11,13,17,19,23,29,31):
            if m==2:
                assert states[4]==states[2]
                assert states[3]==states[1]
            else:
                assert states[m]==states[1]
    assert all(a[n]%10==[1,2,7,2][(n-1)%4] for n in range(1,601))
    print('PASS finite differential quotients modulo2..32 through index250')
    print('PASS explicit period bounds modulo2..32 through600; whole-polynomial prime certificates')
    print('PASS period4modulo10from index1')


if __name__=='__main__':main()
