#!/usr/bin/env python3
"""Exact elementary Tutte witness for the four-cube n=581 fixed-108 graph.

No matching algorithm, third-party packages, numerical search, or
archived permutation data. This script checks a 31-interval cut set
and computes connected components by the definition of a graph.
"""
from collections import Counter

N=581
FIXED=108
CUBES=(343,512,729,1000)
INTERVALS=(
    (148,151),(156,156),(161,162),(165,167),(170,170),
    (174,175),(179,180),(184,186),(203,204),(209,210),
    (215,217),(263,271),(276,277),(281,282),(286,287),
    (298,301),(305,306),(311,320),(324,325),(329,330),
    (334,336),(432,441),(445,446),(450,451),(455,457),
    (467,470),(474,475),(480,489),(493,494),(498,499),
    (503,505),
)
EXPECTED={1:60,3:18,5:13,7:2,11:7,17:3,63:1,93:1}


def component(start, available):
    """Close under the four exact cubic reflections, staying in T."""
    q=[start]
    reached={start}
    for x in q:
        for cube in CUBES:
            y=cube-x
            if y!=x and y in available and y not in reached:
                reached.add(y)
                q.append(y)
    return reached


def main():
    assert len(INTERVALS)==31
    assert all(1<=a<=b<=N for a,b in INTERVALS)
    assert all(INTERVALS[i][1]<INTERVALS[i+1][0]
               for i in range(len(INTERVALS)-1))
    S={i for a,b in INTERVALS for i in range(a,b+1)}
    assert FIXED not in S and len(S)==103
    T=set(range(1,N+1))-{FIXED}-S
    assert len(T)==477
    sizes=[]
    while T:
        c=component(min(T),T)
        assert c<=T
        sizes.append(len(c))
        T-=c
    table=Counter(sizes)
    assert table==EXPECTED, (table,EXPECTED)
    assert sum(size*num for size,num in table.items())==477
    odd_components=sum(num for size,num in table.items() if size%2)
    assert odd_components==105 and odd_components>len(S)
    print("PASS: 31 disjoint integer intervals form a 103-vertex Tutte set")
    print("PASS: 477 remaining vertices split into 105 odd components")
    print("PASS: component sizes",dict(sorted(table.items())))
    print("PROVED: 105 > 103, so no perfect matching is possible")
    print("CONSEQUENCE: no four-cube involution with sole fixed point 108 at n=581")


if __name__=="__main__":
    main()
