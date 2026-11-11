"""Independent exact-integer audits for every coefficient sign."""
from collections import defaultdict
from all_integer import values, count, nth

def lucas(N):
    L=[2,1]
    for _ in range(2,N+1): L.append(L[-1]+L[-2])
    return L

def direct(q, form, X, N=62):
    L=lucas(N)
    result=defaultdict(list)
    for i in range(1,N+1):
        for j in range(1,N+1):
            v=(L[i]-q*L[j] if form=='S' else
               q*L[i]-L[j] if form=='T' else q*L[i]+L[j])
            if 0<v<=X: result[v].append((i,j))
    return result

def main():
    tests=0
    for q in range(-40,41):
        for form in ('S','T','P'):
            for X in (0,1,2,3,5,9,15,32,100,333,1000):
                result=values(q,form,X)
                expected=direct(q,form,X,N=42)
                assert set(result)==set(expected),(q,form,X)
                if q:
                    for x in result:
                        assert sorted(result[x])==sorted(expected[x]),(q,form,X,x)
                else:
                    assert all(reps is None for reps in result.values())
                assert count(q,form,X)==len(expected)
                tests+=1
    for q in (-23,-7,-1,0,1,2,3,4,5,6,7,8,15,18,40,55,99):
        for form in ('S','T','P'):
            if q<=0 and form=='T': continue
            expected=sorted(direct(q,form,10**12,N=62))
            for n in (1,2,3,5,10,20,50):
                assert nth(q,form,n)==expected[n-1],(q,form,n)
    print(f'PASS: {tests} threshold audits for all signs and all three forms')
    print('PASS: exact witnesses, collision multiplicities and nth values')

if __name__=='__main__': main()
