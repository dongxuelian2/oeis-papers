"""Collision families for quotient coefficients of Lucas and Fibonacci numbers."""
from argparse import ArgumentParser
L=[2,1]; F=[0,1]
def ensure(n):
    while len(L)<=n:
        L.append(L[-1]+L[-2])
        F.append(F[-1]+F[-2])

def quotient(m,h):
    """Coefficient q for m>h>=1 with the same parity, or None."""
    if not (m>h>=1 and (m-h)%2==0):
        raise ValueError("m>h>=1 with equal parity required")
    ensure(m)
    a=L if m%2 else F
    return a[m]//a[h] if a[m]%a[h]==0 else None

def collision(m,h,n):
    """Return (q, positive T value, two T index pairs)."""
    if n<1: raise ValueError("n>=1 required")
    q=quotient(m,h)
    if q is None: raise ValueError("quotient is nonintegral")
    ensure(n+2*m)
    v=q*L[n+m-h]-L[n]
    assert v==q*L[n+m+h]-L[n+2*m]>0
    return q,v,(n+m-h,n),(n+m+h,n+2*m)

def special_two(n):
    """Additional infinite T_2 collision."""
    if n<1: raise ValueError("n>=1 required")
    ensure(n+3)
    v=L[n+3]
    assert v==2*L[n+2]-L[n]
    return 2,v,(n+2,n),(n+3,n+3)


def half_lucas_collision(r, n):
    """Return q, positive T value, two distinct witnesses, for q=L_(6r+3)/2."""
    if r < 0:
        raise ValueError("r must be >=0")
    M = 6*r+3
    if n < M:
        raise ValueError("n must be >=6r+3")
    ensure(n+M+1)
    assert L[M] % 2 == 0
    q = L[M]//2
    val = q*L[n] - L[n-M+1]
    assert val > 0 and val == q*L[n+3]-L[n+M+1]
    return q, val, (n,n-M+1), (n+3,n+M+1)

if __name__=="__main__":
    p=ArgumentParser(description=__doc__)
    p.add_argument("m",type=int)
    p.add_argument("h",type=int)
    p.add_argument("n",type=int,nargs="?",default=1)
    a=p.parse_args()
    print(collision(a.m,a.h,a.n))
