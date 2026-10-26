#!/usr/bin/env python3
"""Two transverse cubic-reflection path partitions in high Phase III.

Standard-library integer arithmetic only. Reconstructs the exact 245
even-sum paths and both 193/194 odd-sum normalized path decompositions.
Does NOT search for any perfect matching.
"""
from collections import Counter

ODD = (343, 729)
EVEN = (512, 1000)


def component_sizes(n, sums, fixed=None):
    remaining = set(range(1,n+1))
    if fixed is not None:
        remaining.remove(fixed)
    sizes = []
    while remaining:
        start = min(remaining)
        visited = {start}
        queue = [start]
        for v in queue:
            for c in sums:
                w = c-v
                if w in remaining and w != v and w not in visited:
                    visited.add(w)
                    queue.append(w)
        sizes.append(len(visited))
        remaining -= visited
    return Counter(sizes)


def positive_counts(**kw):
    return Counter({int(k):v for k,v in kw.items() if v})


def main():
    count = 0
    for n in range(580,666):
        raw = component_sizes(n,EVEN)
        assert raw == Counter({1:1,2:744-n,3:n-511,4:11}), (n,raw)
        assert sum(raw.values()) == 245
        if n%2 == 0:
            count += 1
            continue
        for fixed in (256,500):
            assert 2*fixed in EVEN
            even = component_sizes(n,EVEN,fixed)
            if fixed == 256:
                wanted_even=Counter({2:744-n,3:n-511,4:11})
                wanted_odd=(Counter({1:2,2:22,3:727-n,4:n-557})
                            if n<=641 else
                            Counter({1:1,2:23,3:728-n,4:n-558}))
            else:
                wanted_even=Counter({1:2,2:743-n,3:n-511,4:11})
                wanted_odd=(Counter({2:23,3:727-n,4:n-557})
                            if n<=613 else
                            Counter({2:22,3:729-n,4:n-558}))
            assert even == wanted_even, (n,fixed,even,wanted_even)
            odd = component_sizes(n,ODD,fixed)
            assert odd == wanted_odd, (n,fixed,odd,wanted_odd)
            assert sum(even.values())+sum(odd.values()) == 438
            assert all(size <= 4 for size in odd),odd
            assert all(size <= 4 for size in even),even
            count += 1
    assert count == 129 # 43 even n + (43 odd n)*2
    print("PASS: exact even-cube 245-path counts at 86 lengths")
    print("PASS: fixed 256 gives 244 even / 194 odd components")
    print("PASS: fixed 500 gives 245 even / 193 odd components")
    print("PASS: all 86 odd fixed-point graphs have size <=4 paths")
    print("PASS: two quotient component counts sum to exactly 438")
    print("NOT PROVED: perfect matching of the four-cube union")


if __name__=="__main__":
    main()
