"""Exact certificates for the A191980/A191982 intersection theorem.

Each fixed-shift gap obeys the Lucas recurrence. Checking
positivity at c=8 and c=9 proves it for all c >= 8.
"""
from bisect import bisect_right
from collections import defaultdict
from sum_difference_overlap import EXCEPTIONS,count,contains,large,small,nth

N=240
L=[2,1]
for i in range(2,N+20): L.append(L[-1]+L[-2])

def inequalities(c):
    r={h:5*(L[c]-L[c-h]) for h in range(1,5)}
    gaps={
        "a_bound":5*L[c]-L[c+3]-L[c-3]-5*L[c-5],
        "top_exclusion":L[c+3]+L[c+1]-5*L[c],
        "max_v1":L[c+3]+L[c-3]-L[c+2]-L[c],
        "max_v2":L[c+3]+L[c-3]-L[c+1]-L[c-1],
        "h1_lo":r[1]-2*L[c-1],
        "h1_hi":L[c+2]-r[1],
        "h1_at_c":r[1]-L[c]-L[c-2],
        "h1_at_c1_lo":r[1]-L[c+1]-L[c-5],
        "h1_at_c1_hi":L[c-1]+L[c+1]-r[1],
        "h2_lo":r[2]-2*L[c],
        "h2_hi":L[c+3]-r[2],
        "h2_at_c1":r[2]-L[c+1]-L[c-1],
        "h2_at_c2_lo":r[2]-L[c+2]-L[c-4],
        "h2_at_c2_hi":L[c]+L[c+2]-r[2],
        "h3_lo":r[3]-2*L[c+1],
        "h3_hi":L[c+3]-r[3],
        "h3_at_c2":r[3]-L[c+2]-L[c],
        "h4_lo":r[4]-L[c+2]-L[c]
    }
    assert len(gaps)==18
    assert r[4]==L[c+3]+L[c-7]
    return gaps

for c in (8,9):
    gaps=inequalities(c)
    assert all(v>0 for v in gaps.values()),(c,gaps)
for c in range(10,N):
    assert all(v>0 for v in inequalities(c).values()),c

small_solutions=[]
for c in range(1,8):
    for a in range(1,c):
        for b in range(1,c+4):
            for d in range(1,c+4):
                if 5*L[a]+L[b]==5*L[c]-L[d]:
                    small_solutions.append((5*L[a]+L[b],a,b,c,d))
assert len(small_solutions)==16
assert sorted({x for x,*_ in small_solutions})==list(EXCEPTIONS)

P=defaultdict(list)
for a in range(1,N):
    for b in range(1,N+4):
        P[5*L[a]+L[b]].append((a,b))
T=set()
for c in range(1,N+1):
    for d in range(1,c+4):
        x=5*L[c]-L[d]
        if x>0: T.add(x)
actual=set(P)&T
A={large(n) for n in range(4,N-3)}
B={small(n) for n in range(4,N-3)}
assert A.isdisjoint(B) and A.isdisjoint(EXCEPTIONS) and B.isdisjoint(EXCEPTIONS)
expected=set(EXCEPTIONS)|A|B
assert actual==expected
assert len(actual)==14+2*(N-7)

ordered=sorted(actual)
for x in list(range(-2,15000))+[L[i] for i in range(3,150)]:
    assert count(x)==bisect_right(ordered,x),x
    assert contains(x)==(x in actual),x
cutoff=small(N-3)
for n in range(1,bisect_right(ordered,cutoff-1)+1):
    assert nth(n)==ordered[n-1],n
print("PASS: 18 positive Lucas-recursive gaps (c=8,9), audit through c=239")
print("PASS: 14 exceptions and 16 witnesses with c<=7")
print("PASS: independent intersection through c=240:",len(actual),"values")
print("PASS: exact counting, membership, and rank inversion")
