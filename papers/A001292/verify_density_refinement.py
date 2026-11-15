from fractions import Fraction as F
Q=440334654777631
rho=F(2865982022164616687973223130,2999999999999999999999999997)
def success(p,e): return F((p-1)*p**(e-1), e*(p**e-1))
def improvement(p,e,h):
    return F(2,3**(h+1))*(1-success(p,e)-F((e-1)*(p-1),e*p))
delta=improvement(Q,5,3)+improvement(757,7,5)
tail=F(0)
rows=[]
for h in range(6,101):
    n=h+2;a=b=0
    while n%2==0: a+=1;n//=2
    while n%3==0: b+=1;n//=3
    if n!=1: continue
    x=F(1,3**(h+1)) if b==0 else F(4 if a==0 else 2,3**(h+2))
    tail+=x;rows.append((h,str(x),float(x)))
print('old',float(rho))
print('positive_valuation_gain',float(delta))
print('tail_rows',rows)
print('tail_gain',float(tail))
print('new_lower_bound',float(rho+delta+tail))
# Finite modular enumeration: counts valuations < K; residual ball has mass p^-K.
for p,e in [(7,3),(11,5),(757,7)]:
    K=4 if p<12 else 2
    mod=p**K
    count=0
    for x in range(1,mod):
        a=0;y=x
        while y%p==0: y//=p;a+=1
        if a%e==0 and pow(y%p,(p-1)//e,p)==1: count+=1
    exact=success(p,e)
    assert F(count,mod)<=exact<=F(count+1,mod)
    print('enumerated',p,e,K,count,mod,'pass')
print('finite h<=16 lower bound',float(rho+delta+sum(F(x) for h,x,_ in rows if h<=16)))
alpha=F(19,37)*F(166834,333667)*F(379,757)*F(Q+1,2*Q)
beta=F(13,37)*F(111223,333667)
base=1-(10*alpha+2*beta+1)/27
old5=F(2,81)*F(4*(Q-1),5*Q)
old7=F(2,729)*F(6*756,7*757)
assert base+old5+old7+F(2,729)==rho
finite=sum(F(x) for h,x,_ in rows if h<=16)
new=base+F(2,81)*(1-success(Q,5))+F(2,729)*(1-success(757,7))+F(2,729)+finite
assert new==rho+delta+finite
assert new>F(95599527150,10**11)
# An independent sum of valuation shells approximates s from below.
for p,e in [(Q,5),(757,7),(7,3),(11,5)]:
    truncated=sum(F(p-1,e*p**(e*j+1)) for j in range(5))
    assert 0<success(p,e)-truncated<F(1,p**(5*e))
print('baseline reconstruction, rational lower-bound comparison, and shell checks: PASS')
print('exact finite bound:',new)
