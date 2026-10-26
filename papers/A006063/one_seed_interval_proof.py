#!/usr/bin/env python3
"""Independent interval-algebra certificate of seven-round reflection closure.

This checker never iterates through all individual reachable lengths.
It stores unions of integer intervals and applies the exact mapping

  [a,b] -> [c-h-1, c-l-1],
  l=max(a,c-CAP-1), h=min(b,(c-2)//2),

where c is a cube <= 2*CAP. The truncation expresses
m < c-m-1 <= CAP. Adjacent intervals are merged after each round.

A single seed [7,7] yields all [8915,10975] in seven rounds.
The infinite induction is given in main.tex and one_seed_eventual.py.
"""
CAP=10975
SEED=(7,7)
EXPECTED_SIZES=(1,21,189,995,3280,6588,8533,8924)
EXPECTED_INTERVALS=(1,21,186,870,2077,2037,1031,770)


def merge(intervals):
    result=[]
    for a,b in sorted(intervals):
        assert a<=b
        if result and a<=result[-1][1]+1:
            x,y=result[-1]
            result[-1]=(x,max(b,y))
        else:
            result.append((a,b))
    return result


def apply_round(intervals,cubes):
    derived=list(intervals)
    for a,b in intervals:
        for c in cubes:
            lo=max(a,c-CAP-1)
            hi=min(b,(c-2)//2)
            if lo<=hi:
                derived.append((c-hi-1,c-lo-1))
    return merge(derived)


def main():
    cubes=[]
    k=2
    while k**3<=2*CAP:
        cubes.append(k**3)
        k+=1
    intervals=[SEED]
    for depth in range(8):
        total=sum(b-a+1 for a,b in intervals)
        assert total==EXPECTED_SIZES[depth], (depth,total)
        assert len(intervals)==EXPECTED_INTERVALS[depth]
        if depth:
            print(f"PASS round {depth}: {total} lengths "
                  f"in {len(intervals)} disjoint intervals")
        if depth<7:
            intervals=apply_round(intervals,cubes)
    assert (8915,10975) in intervals
    assert all(a>8914 or b<8914 for a,b in intervals)
    print("PASS: [8915,10975] is a single proven interval in round 7.")
    print("PASS: exact symbolic interval reflection, no matching search.")


if __name__=="__main__":
    main()
