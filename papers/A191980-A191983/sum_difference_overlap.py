"""Exact positive intersection of OEIS A191980 and A191982."""
from argparse import ArgumentParser
from bisect import bisect_right
EXCEPTIONS = (6,8,9,12,16,19,22,24,26,31,34,44,52,138)
L = [2,1]
def lucas(n):
    if n < 0: raise ValueError("Lucas index must be nonnegative")
    while len(L)<=n: L.append(L[-1]+L[-2])
    return L[n]
def large(n):
    if n<4: raise ValueError("n >= 4 required")
    return 5*lucas(n)+lucas(n+7)
def small(n):
    if n<4: raise ValueError("n >= 4 required")
    return 5*lucas(n)+lucas(n-3)
def count(x):
    result=bisect_right(EXCEPTIONS,x)
    for f in (large,small):
        n=4
        while f(n)<=x:
            result+=1
            n+=1
    return result
def contains(x):
    if x in EXCEPTIONS: return True
    for f in (large,small):
        n=4
        while f(n)<=x:
            if f(n)==x: return True
            n+=1
    return False
def nth(n):
    if n<1: raise ValueError("1-based index required")
    hi=1
    while count(hi)<n: hi*=2
    lo=0
    while lo<hi:
        mid=(lo+hi)//2
        if count(mid)>=n: hi=mid
        else: lo=mid+1
    return lo
if __name__=="__main__":
    p=ArgumentParser(description=__doc__)
    p.add_argument("operation",choices=("count","nth","member"))
    p.add_argument("value",type=int)
    a=p.parse_args()
    print({"count":count,"nth":nth,"member":contains}[a.operation](a.value))
