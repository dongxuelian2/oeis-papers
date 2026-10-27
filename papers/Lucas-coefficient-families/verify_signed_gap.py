"""Independent certificate checks for the signed-gap collision spectra."""
from signed_gap import signed_gap_witnesses, L, ensure

S_NONUNIQUE = {
  2,3,4,6,7,9,10,11,14,17,18,19,23,25,28,29,31,
  36,38,41,46,47,62,65,72,73,75,76,94
}
T_UNIQUE = {
  27,31,39,42,57,59,62,63,67,68,70,71,78,83,86,91,93,95,97
}
P_UNIQUE = {
  27,39,42,57,59,63,67,68,70,71,78,83,86,91,93,95,97
}

F = [0,1]


def ensure_f(n):
    while len(F) <= n:
        F.append(F[-1]+F[-2])


def main():
    # These certified coefficient sets were established independently
    # in verify_all_global_unique.py, before this signed-gap routine.
    for q in range(2,101):
        signs = signed_gap_witnesses(q)
        assert (1 in signs) == (q in S_NONUNIQUE), (q,signs)
        assert (-1 not in signs) == (q in T_UNIQUE), (q,signs)
        assert (not signs) == (q in P_UNIQUE), (q,signs)
        for sign,(a,b,c,d,delta) in signs.items():
            assert 1 <= a < b and 1 <= c < d
            assert L[b]-L[a] == q*(L[d]-L[c])
            assert sign == (delta>0)-(delta<0)
            # A sum collision always follows.
            assert q*L[c]+L[b] == q*L[d]+L[a] > 0
            if sign == 1:
                assert L[a]-q*L[c] == L[b]-q*L[d] > 0
            elif sign == -1:
                assert q*L[c]-L[a] == q*L[d]-L[b] > 0
            else:
                assert q*L[c] == L[a] and q*L[d] == L[b]
    print("PASS: complete S,T,P signed spectra q=2..100 agree with prior global results")

    ensure(100)
    ensure_f(100)
    audits=0
    for h in range(1,17):
        for a in range(2,61):
            for c in range(1,a):
                delta=L[a]*L[c+h]-L[c]*L[a+h]
                assert delta == 5*((-1)**(c+1))*F[a-c]*F[h], (a,c,h)
                audits+=1
    print(f"PASS: {audits} independent equal-gap determinant identities")

    families=set()
    for r in range(1,9):
        coefficients=[
          (L[3*r]//2, 1, 3*r+1, L[3*r]%2),
          (L[4*r+2]//3, 2, 4*r+1, L[4*r+2]%3),
          (F[3*(r+1)]//2, 4, 3*(r+1)-2, F[3*(r+1)]%2)
        ]
        for q,h,a,remainder in coefficients:
            assert remainder==0 and q>=2
            assert L[a+h]-L[a] == q*(L[1+h]-L[1])
            assert L[a]-q*L[1] == L[a+h]-q*L[1+h] > 0
            families.add(q)
    print(f"PASS: 24 explicit positive S collision certificates in "
          f"{len(families)} different coefficients")

    # Distinct finite exceptional behavior between T and P is
    # detected without equating the three sets.
    for q in (27,31,39,62,97):
        signs = signed_gap_witnesses(q)
        assert (1 in signs) == (q in {31,62})
        assert -1 not in signs
    print("PASS: P-only versus S/T sign separation at q=27,31,39,62,97")


if __name__ == "__main__":
    main()
