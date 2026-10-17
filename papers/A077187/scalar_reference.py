"""Independent scalar finite-field formulas for decimal digit-layer drift."""
from math import gcd

def primitive_root_of_order(p,t):
    assert (p-1)%t==0
    fac=[]; tmp=t; f=2
    while f*f<=tmp:
        if tmp%f==0:
            fac.append(f)
            while tmp%f==0:tmp//=f
        f+=1
    if tmp>1:fac.append(tmp)
    for a in range(2,p):
        z=pow(a,(p-1)//t,p)
        if pow(z,t,p)==1 and all(pow(z,t//f,p)!=1 for f in fac):
            return z
    raise RuntimeError((p,t))

def polyforms(t,gamma,p,z):
    inv10=pow(10,-1,p); inv20=pow(20,-1,p); inv200=pow(200,-1,p)
    U=[9*inv20+9*inv200,-9*inv20,0]
    V=[-9*inv20+9*inv200,9*inv20,0]
    Eprev=0
    for j in range(1,t):
        e10=pow(10,j-1,t)
        E=(Eprev+j*e10)%t
        zz=pow(z,j,p)
        invz=pow(zz-1,-1,p)
        X=zz*invz%p
        Z=zz*invz*invz%p
        alpha=pow(z,gamma*j*e10%t,p)
        U[1]=(U[1]+pow(z,-gamma*E%t,p)*((alpha-1)-9*inv10*alpha*X))%p
        U[2]=(U[2]+pow(z,-gamma*E%t,p)*((alpha-1)*Z))%p
        V[1]=(V[1]+pow(z,gamma*Eprev%t,p)*((alpha-inv10)*X))%p
        V[2]=(V[2]+pow(z,gamma*Eprev%t,p)*((1-alpha)*Z))%p
        Eprev=E
    return [u%p for u in U],[v%p for v in V]
