"""Exact integer algorithms for two Lucas coefficient families."""
from argparse import ArgumentParser
from bisect import bisect_left

L=[2,1]
F=[0,1]
def ensure(n):
    while len(L)<=n:
        L.append(L[-1]+L[-2])
        F.append(F[-1]+F[-2])
def lucas(n):
    if n<0: raise ValueError("Lucas index must be >= 0")
    ensure(n); return L[n]
def fibonacci(n):
    ensure(abs(n))
    return F[n] if n>=0 else (-1)**(-n+1)*F[-n]
def unique_coefficient(r):
    if r<1: raise ValueError("r must be >=1")
    return 5*fibonacci(2*r)
def repeated_coefficient(r):
    if r<1: raise ValueError("r must be >=1")
    return lucas(2*r)
def permitted(r,i,j):
    unique_coefficient(r)
    return (i==2*r+2 and j==1) or (i>=2*r+3 and 1<=j<=i-2*r-2)
def bounded_index_count(r,n):
    unique_coefficient(r)
    d=n-2*r-2
    return 0 if d<0 else 1+d*(d+1)//2
def positive_count(r,x):
    """Number of distinct positive values L_i - 5F_(2r)L_j <= x."""
    if x<=0: return 0
    q=unique_coefficient(r)
    i=2*r+2
    total=0
    while True:
        ensure(i+5)
        # For i >= 2r+7 the block minimum is at least L_(i-2r-4).
        if i>=2*r+7 and L[i-2*r-4]>x:
            break
        maxj=1 if i==2*r+2 else i-2*r-2
        first_j=bisect_left(L,(L[i]-x+q-1)//q,1,maxj+1)
        total+=max(0,maxj-first_j+1)
        i+=1
    return total
def nth_positive(r,n):
    if n<1: raise ValueError("positive rank must be >=1")
    unique_coefficient(r)
    upper=2*r+2
    while bounded_index_count(r,upper)<n: upper+=1
    lo,hi=0,lucas(upper)
    while lo<hi:
        mid=(lo+hi)//2
        if positive_count(r,mid)<n: lo=mid+1
        else: hi=mid
    return lo
def repeat_witness(r,n):
    """Value and two witnesses in q L_k - L_l for q=L_(2r)."""
    if n<1: raise ValueError("n must be >=1")
    repeated_coefficient(r)
    return lucas(n+4*r),(n+2*r,n),(n+6*r,n+8*r)

if __name__=="__main__":
    p=ArgumentParser(description=__doc__)
    p.add_argument("operation",choices=("coefficient","count","nth","repeat"))
    p.add_argument("r",type=int)
    p.add_argument("value",type=int,nargs="?",default=1)
    a=p.parse_args()
    if a.operation=="coefficient": print(unique_coefficient(a.r))
    elif a.operation=="count": print(positive_count(a.r,a.value))
    elif a.operation=="nth": print(nth_positive(a.r,a.value))
    else: print(repeat_witness(a.r,a.value))
