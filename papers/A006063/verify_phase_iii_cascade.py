#!/usr/bin/env python3
"""Exact arithmetic audit: Phase III fixed-point duality and full leaf cascades.

Only Python standard library, no networkx, matching solver, numerical
optimization, previous cube-sum permutations or endpoint atlases.
"""
from collections import Counter

CUBES = (343, 512, 729, 1000)
ODD = (343, 729)

BOUNDARY_CHECKS = {
    (500, 581): (162, 277, 446),
    (500, 603): (181, 229, 398),
    (256, 581): (189, 208, 310),
    (256, 589): (141, 189, 304, 473),
    (256, 629): (141, 189, 243, 304, 412, 473),
    (256, 643): (87, 473),
}


def odd_components(n, fixed):
    parts = []
    for x in range(1, 172):
        v = {x, 343-x}
        if 386+x <= n:
            v.add(386+x)
        if 729-x <= n:
            v.add(729-x)
        parts.append(v)
    parts += [{j, 729-j} for j in range(343, 365)]
    assert len(parts) == 193 and sum(map(len, parts)) == n
    q = 0
    profile = Counter()
    for part in parts:
        remaining = part - {fixed}
        while remaining:
            start = min(remaining)
            queue = [start]
            reached = {start}
            for v in queue:
                for c in ODD:
                    w = c - v
                    if w in remaining and w not in reached:
                        reached.add(w)
                        queue.append(w)
            q += len(reached)%2
            profile[len(reached)] += 1
            remaining -= reached
    return q, profile


def expected_pairs(n, fixed):
    if fixed == 500:
        pairs = [(12,331,343)]
        if n<=601:
            pairs += [(398,114,512),(229,283,512),
                      (60,452,512),(548,181,729)]
        return pairs
    if n >= 643:
        return []
    pairs = [(87,425,512),(575,154,729),(358,371,729)]
    if n <= 587:
        pairs += [(141,202,343),(527,473,1000),(39,304,343)]
    if n >= 629:
        pairs += [(629,100,729)]
    return pairs


def neighbors(v, remaining):
    return {c-v for c in CUBES if c-v in remaining and c-v != v}


def complete_peeling(n, fixed):
    remaining = set(range(1,n+1)) - {fixed}
    pairs = []
    while True:
        leaves = [(v,next(iter(neighbors(v,remaining))))
                  for v in sorted(remaining)
                  if len(neighbors(v,remaining)) == 1]
        if not leaves:
            break
        v,w = leaves[0]
        assert v+w in CUBES
        pairs.append((v,w,v+w))
        remaining -= {v,w}
    return pairs,remaining


def check_boundary(n, fixed, pairs, remaining):
    removed = {fixed} | {v for a,b,_ in pairs for v in (a,b)}
    affected = {c-v for v in removed for c in CUBES
                if 1<=c-v<=n and c-v not in removed}
    assert affected == set(BOUNDARY_CHECKS[fixed,n]),(n,fixed,affected)
    assert {len(neighbors(v,remaining)) for v in affected} == {2}
    assert min(len(neighbors(v,remaining)) for v in remaining) >= 2


def main():
    checked = 0
    for fixed in (256,500):
        for n in range(581,666,2):
            q, profile = odd_components(n,fixed)
            if fixed == 500:
                expected_profile = ({2:23,3:727-n,4:n-557} if n<=613
                                    else {2:22,3:729-n,4:n-558})
            else:
                expected_profile = ({1:2,2:22,3:727-n,4:n-557} if n<=641
                                    else {1:1,2:23,3:728-n,4:n-558})
            assert profile == Counter(expected_profile), (n,fixed,profile)
            assert sum(profile.values()) == (193 if fixed==500 else 194)
            expected_q = 729-n if fixed==256 or n>=615 else 727-n
            assert q == expected_q, (n,fixed,q,expected_q)
            assert q%2 == 0
            pairs, remaining = complete_peeling(n,fixed)
            expected = expected_pairs(n,fixed)
            assert pairs == expected, (n,fixed,pairs,expected)
            if (fixed,n) in BOUNDARY_CHECKS:
                check_boundary(n,fixed,pairs,remaining)
            assert min(len(neighbors(v,remaining)) for v in remaining) >= 2
            checked += 1
    assert checked==86
    print("PASS: fixed-500 keeps 193 paths; fixed-256 splits into 194 at 86 cases")
    print("PASS: exact 1/2/3/4-component-size profiles and odd defects")
    print("PASS: exact 6/3/4/0 and 5/1 forced-edge cascades")
    print("PASS: six small boundary checks, each surviving affected vertex degree 2")
    print("NOT PROVED: perfect matching existence in the leaf-free cores")


if __name__=="__main__":
    main()
