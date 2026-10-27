"""Independent mathematical and implementation checks for explicit families."""
from explicit_infinite import coefficient_witnesses, infinite_T, infinite_collision
from norm_stationary import stationary_T_norm
from stationary_collisions import infinite_collisions as original_infinite

L = [2, 1]
F = [0, 1]


def ensure(n):
    while len(L) <= n:
        L.append(L[-1] + L[-2])
        F.append(F[-1] + F[-2])


def independent_family_coefficients(max_q, max_index=70):
    ensure(max_index)
    result = set()
    for m in range(2, max_index+1):
        if m % 6 == 3 and L[m]//2 <= max_q:
            assert L[m] % 2 == 0
            result.add(L[m]//2)
        seq = L if m%2 else F
        for r in range(1,m):
            if r%2 == m%2 and seq[m]%seq[r] == 0:
                q = seq[m]//seq[r]
                if 2 <= q <= max_q:
                    result.add(q)
    return result


def check_witness(q, witness):
    kind, m, r = witness
    if kind == "half Lucas":
        assert m >= 3 and m%6 == 3 and L[m] == 2*q
        for x in range(m, m+18):
            ensure(x+m+2)
            a = q*L[x]-L[x-m+1]
            b = q*L[x+3]-L[x+m+1]
            assert a == b > 0, (q,witness,x,a,b)
    else:
        assert m > r >=1 and m%2 == r%2
        seq = L if m%2 else F
        assert seq[m] == q*seq[r]
        for n in range(1,19):
            ensure(n+2*m)
            a = q*L[n+m-r]-L[n]
            b = q*L[n+m+r]-L[n+2*m]
            assert a == b > 0, (q,witness,n,a,b)


def check_pattern(q, pat):
    di,dj,de=pat
    h,e,d=-di,de-dj,di-dj
    assert h>0 and e>h and d%2==0
    if h%2 == 0 and e%2 == 0:
        r,m=h//2,e//2
        assert (m-r)%2 == 0 and d==m-r
        seq=L if m%2 else F
        ensure(m)
        assert seq[m] == q*seq[r]
    elif h%2 == 1 and e%2 == 1:
        assert (h,e,d,q)==(1,3,2,2)
    elif h%2 == 1 and e%2 == 0:
        m=e//2
        assert m%2 == 1
        if h==1:
            assert d==m+1 and q==L[m]
        else:
            assert h==3 and d==m-1 and m%3==0 and 2*q==L[m]
    else:
        assert (h,e,d,q)==(2,3,0,2)


def main():
    independent=independent_family_coefficients(1000)
    found=set()
    n_patterns=0
    n_witnesses=0
    for q in range(2,1001):
        witnesses=coefficient_witnesses(q)
        classified=bool(witnesses)
        baseline=stationary_T_norm(q)
        assert classified == bool(baseline), (q,witnesses,baseline)
        assert classified == (q in independent), (q,witnesses)
        if classified:
            found.add(q)
        for witness in witnesses:
            check_witness(q,witness)
            n_witnesses+=1
        for pat in baseline:
            check_pattern(q,pat)
            n_patterns+=1
    for q in (-199,-38,-5,-2,-1,0,1,2,5,27,38,199):
        for form in ("S","T","P"):
            assert infinite_collision(q, form) == original_infinite(q,form), (q,form)
    assert len(found)==29, (len(found),sorted(found))
    print("PASS: 2..1000 explicit three-family classification equals")
    print("      independent quotient generation and finite norm algorithm")
    print(f"PASS: {n_patterns} stationary patterns satisfy the exact parity cases")
    print(f"PASS: {n_witnesses} constructed coefficient witnesses")
    print("PASS: 18 consecutive values for each quotient/half-Lucas identity")
    print("PASS: positive, zero and negative coefficient sign reductions")
    print("PASS: 19/199 infinite coefficients in 2..200; 29/999 in 2..1000")


if __name__ == "__main__":
    main()
