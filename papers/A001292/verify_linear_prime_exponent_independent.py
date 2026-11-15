import json
from fractions import Fraction
from pathlib import Path

p,q,e=1031,103,5
bad={a for a in range(1,p) if pow(a,(p-1)//e,p)!=1}
assert len(bad)==824

def aggregates(n,B,M):
    # P=B^n, S=sum B^(n-1-i), F=sum i*B^(n-1-i).
    N,P,S,F=0,1,0,0
    for bit in bin(n)[2:]:
        P,S,F=P*P%M,S*(P+1)%M,(F*(P+1)+N*S)%M
        N*=2
        if bit=='1':
            P,S,F=P*B%M,(S*B+1)%M,(F*B+N)%M
            N+=1
    return P,S,F

def independent_prefix(m,M):
    w,u,d=0,1,1
    while u<=m:
        n=min(m,10*u-1)-u+1
        P,S,F=aggregates(n,pow(10,d,M),M)
        w=(P*w+u*S+F)%M
        u*=10;d+=1
    return w

def v3(n):
    v=0
    while n and n%3==0:n//=3;v+=1
    return v

def D(m):
    if not m:return 0
    d=len(str(m))
    return d*(m+1)-(10**d-1)//9

# Independent prefix implementation agrees with direct recurrence.
w=0
small_checks=0
for m in range(1,10001):
    w=(w*10**len(str(m))+m)%752139
    if m<100 or m%97==0:
        assert independent_prefix(m,752139)==w
        small_checks+=1

# Check all q-residue phases and p lifts, rather than sampled affine m.
phases=counts=0
for d in range(1,q):
    B=pow(10,d,p);alpha=pow(1-B,-1,p)
    a=(((pow(10,d,q)-1)*pow(9,-1,q)%q)*pow(d,-1,q)-1)%q
    residues=[(a+q*j)%(p*q) for j in range(p)]
    assert len(set(residues))==p
    for c in (0,1,489,1030):
        assert sum((alpha*m+c)%p in bad for m in residues)==824
        counts+=1
    phases+=1

# The four classes are exactly the prescribed triangular valuation.
valuation_checks=0
for b in range(1,9):
    M=3**(b+1);expected={3**b,2*3**b,3**b-1,2*3**b-1}
    actual={m for m in range(M) if m*(m+1)//2 and v3(m*(m+1)//2)==b}
    assert actual==expected
    valuation_checks+=M

# Validate supplied rows independently and test cuts at digit boundaries and near m.
rows=json.loads(Path(__file__).with_name('linear-prime-exponent-certificate.json').read_text())['selected_prefixes']
cut_checks=0
for row in rows:
    d,m=row['width'],row['endpoint'];h=v3(d);M3=3**(h+2);M=p*M3
    w=independent_prefix(m,M)
    assert w%729==row['prefix_mod729'] and w%p==row['prefix_mod1031']
    assert w%p in bad and D(m)%q==0
    assert w%M3==m*(m+1)//2%M3 and v3(w%M3)==5
    cuts={0,1,9,10,99,100,10**(d-1)-1,10**(d-1),m//2,m-1}
    for k in cuts:
        assert 0<=k<m
        wk=independent_prefix(k,M)
        r=(pow(10,D(k),M)*w-(pow(10,D(m),M)-1)*wk)%M
        norm=r*pow(pow(10,D(k),M3),-1,M3)%M3
        assert norm==m*(m+1)//2%M3
        assert v3(r%M3)==5 and r%p in bad
        assert pow(pow(10,D(k),p),(p-1)//5,p)==1
        cut_checks+=1

eta=Fraction(824,p*q)
for h in range(4,1001):
    b=5
    while 5*b<=h+1:b*=5
    assert 5*b>=h+2 and b+1<=h+2
    # The geometric comparison is exact, before using h.
    tail_geometric=Fraction(2,3**(5*b))
    assert tail_geometric<=Fraction(2,3**(h+2))

print('Independent direct-prefix comparisons:',small_checks)
print('Complete p-lift affine counts:',counts,'across',phases,'B phases')
print('Exhaustive triangular valuation residues:',valuation_checks)
print('Independent supplied-prefix checks:',len(rows))
print('Digit-boundary, midpoint, and late rotation-cut checks:',cut_checks)
print('Tail/period exponent checks: 997')
print('PASS: independent arithmetic checks passed.')
