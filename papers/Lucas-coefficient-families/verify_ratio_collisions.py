"""Independent integer check of quotient-collision identities."""
from ratio_collisions import quotient,collision,special_two

def lucas_fibonacci(N):
    L=[2,1];F=[0,1]
    for _ in range(2,N+1):
        L.append(L[-1]+L[-2]);F.append(F[-1]+F[-2])
    return L,F

def main():
    L,F=lucas_fibonacci(250)
    families=identities=0;qs=set()
    for h in range(1,21):
        for m in range(h+1,45):
            if (m-h)%2: continue
            A=L if m%2 else F
            if A[m]%A[h]:continue
            q=A[m]//A[h]
            assert quotient(m,h)==q and q>1
            qs.add(q);families+=1
            for n in range(1,121):
                v=q*L[n+m-h]-L[n]
                assert v==q*L[n+m+h]-L[n+2*m]>0
                assert q*L[n+m-h]+L[n+2*m]==q*L[n+m+h]+L[n]
                assert collision(m,h,n)==(q,v,(n+m-h,n),(n+m+h,n+2*m))
                identities+=1
    for k in range(1,31):
        q=L[k]
        if k==1:continue
        if k%2: assert q in qs
        else: assert q==quotient(2*k,k)
    for n in range(1,121):
        q,v,p1,p2=special_two(n)
        assert v==2*L[n+2]-L[n]==2*L[n+3]-L[n+3]
    print(f"PASS: {families} quotient families, {len(qs)} distinct coefficients")
    print(f"PASS: {identities} exact repeated T/P values and 120 special q=2 witnesses")
if __name__=="__main__":main()
