"""Independent whole-sequence collision certificates for q=2..100."""
from collections import defaultdict
from global_collisions import complete_collisions,index_cutoff

NONUNIQUE_2_TO_100 = {
    2,3,4,6,7,9,10,11,14,17,18,19,23,25,28,29,31,36,38,
    41,46,47,62,65,72,73,75,76,94,
}
def lucas(n):
    v=[2,1]
    for k in range(2,n+1):
        v.append(v[-1]+v[-2])
    return v

def independent(q,N):
    L=lucas(N)
    pairs=defaultdict(list)
    for i in range(2,N+1):
        for j in range(1,i):
            value=L[i]-q*L[j]
            if value>0:
                pairs[value].append((i,j))
    return {v:ps for v,ps in pairs.items() if len(ps)>1}

def main():
    entries=counts=0
    for q in range(2,101):
        cutoff,t=index_cutoff(q)
        assert cutoff==6*t and lucas(t)[t]>200*(q+1)**4
        actual=complete_collisions(q)
        assert bool(actual)==(q in NONUNIQUE_2_TO_100),q
        extra=independent(q,cutoff+8)
        assert actual==extra,(q,actual,extra)
        entries+=1
        counts+=len(actual)
    assert len(NONUNIQUE_2_TO_100)==29
    assert entries-len(NONUNIQUE_2_TO_100)==70
    assert complete_collisions(5)=={}
    assert sorted(complete_collisions(2))==[1,5]
    assert sorted(complete_collisions(3))==[8,26]
    assert sorted(complete_collisions(4))==[3,7]
    assert sorted(complete_collisions(6))==[5,23,105]
    print(f"PASS: {entries} complete finite coefficient certificates q=2..100")
    print("PASS: 70 globally unique coefficients, 29 with finite collisions")
    print(f"PASS: {counts} distinct duplicate values across q=2..100")
    print("PASS: all certificates agree with independent extended enumeration")

if __name__ == "__main__":
    main()
