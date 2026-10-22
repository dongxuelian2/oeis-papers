from math import lcm
import sympy as sp

def order(b,p): return int(sp.n_order(b,p))

def state_at_e(p,e,r=None):
    if r is None:r=order(10,p)
    C=Y=0; l=1; q=10%p; lr=1
    inv2=pow(2,-1,p)
    for d in range(1,e+1):
        N=9*l%p;B=(10*l-1)%p
        A=pow(10,9*d*lr%r,p)
        if q==1:
            S=N;J=N*(N-1)*inv2%p
        else:
            S=(A-1)*pow(q-1,-1,p)%p
            J=(q-N*A+(N-1)*A*q)*pow((1-q)**2,-1,p)%p
        c=(B*S-J)%p;y=(l*S+J)*pow(A,-1,p)%p
        C=(A*C+c)%p;Y=(pow(A,-1,p)*Y+y)%p
        l=q;q=q*10%p;lr=lr*10%r
    return C,Y

def mountain_window(p,e,C,Y,n):
    q=pow(10,e+1,p);L=pow(10,e,p)
    for j in range(n):
        k=(L+j)%p
        C=(q*C+k)%p
        Y=(pow(q,-1,p)*(Y+k))%p
    return (q*C+Y+L+n)%p

def test(limit=200):
    seen=[]
    for p in sp.primerange(7,limit):
        r=order(10,p);f=sp.factorint(r)
        u=2**f.get(2,0)*5**f.get(5,0);v=r//u
        if 20%u:continue
        T=lcm(r,order(10,v) if v>1 else 1)
        e=p*T;n=(9*pow(10,T,r)-10)%r
        C,Y=state_at_e(p,e,r)
        assert mountain_window(p,e,C,Y,n)==0,p
        seen.append(p)
    print("PASS direct witness:",len(seen),"primes")
if __name__=="__main__":test()
