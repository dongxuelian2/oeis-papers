#!/usr/bin/env python3
"""Finite arithmetic check of the 26 cyclic-color planar-face templates.

Reads only the explicit four-color reflection formulas. No matching
solver, planarity-finding library, external face embeddings or images.
"""
from collections import Counter
from verify_three_rotation_planarity import CASES, adjacency

# (canonical face-color word, closed integer intervals of minimum vertices)
PATTERNS = {
    560: (
        ("ABCDCABCDC",((1,38),(40,59),(61,83))),
        ("BCDBCD",((1,62),)),
        ("ABCDDABCDD",((1,23),)),
        ("ABCDDBCDCABCDDBCDCDD",((47,47),)),
        ("ABCDCABDC",((39,39),)),
        ("ABCDC",((84,84),)),
        ("ABCDCBCDC",((60,60),)),
        ("BCD",((63,63),)),
    ),
    579: (
        ("ABCBABCBCDBABCBABCBCDB",((13,28),(30,41))),
        ("ABCBCDCABCBCDC",((1,13),(15,26))),
        ("ABCBCDBABCDC",((1,11),)),
        ("ABCBCDBABCBCDB",((71,80),)),
        ("ABCBABCBCDBABCBBCBCDB",((29,29),)),
        ("ABCBCDCABCCDC",((14,14),)),
        ("ABCBCDCBCDCABCBCDCBCDC",((53,53),)),
        ("ABCBCBABCDC",((12,12),)),
        ("ABCBCDB",((81,81),)),
    ),
    665: (
        ("ACDCBACDCB",((72,86),(88,144))),
        ("ACBACB",((1,62),)),
        ("BDCBDC",((64,120),)),
        ("ABDCBABDCB",((9,11),(13,35))),
        ("ABDCBACD",((1,8),)),
        ("ACDCACDCB",((87,87),)),
        ("ACB",((63,63),)),
        ("ABCBABDCB",((12,12),)),
        ("ABDCB",((36,36),)),
    ),
}


def cyclic_normal(word):
    return min(word[i:]+word[:i] for i in range(len(word)))


def face_words(n,colors,order):
    N=adjacency(n,colors)
    label={c:chr(ord("A")+i) for i,c in enumerate(sorted(colors))}
    unseen={(u,v) for u,row in N.items() for v in row.values()}
    result=Counter()
    while unseen:
        u,v=start=next(iter(unseen))
        word=[]
        vertices=[]
        while (u,v) in unseen:
            unseen.remove((u,v))
            word.append(label[u+v])
            vertices.append(u)
            avail=[c for c in order if c in N[v]]
            incoming=u+v
            w=N[v][avail[(avail.index(incoming)+1)%len(avail)]]
            u,v=v,w
        assert (u,v)==start
        result[(cyclic_normal("".join(word)),min(vertices))]+=1
    assert all(m==1 for m in result.values())
    return result


def main():
    for n,colors,order,_,face_lengths in CASES:
        expected=Counter()
        for word,ranges in PATTERNS[n]:
            for a,b in ranges:
                for v in range(a,b+1):
                    expected[(word,v)]+=1
        assert all(v==1 for v in expected.values())
        actual=face_words(n,colors,order)
        assert actual==expected, (
            n,"missing",list((expected-actual).items())[:5],
            "extra",list((actual-expected).items())[:5])
        assert sum(actual.values())==sum(face_lengths.values())
        assert Counter({k:sum(1 for (w,v) in actual if len(w)==k)
                        for k in face_lengths})==face_lengths
        print(f"PASS: n={n}, {len(PATTERNS[n])} color-word families "
              f"enumerate all {len(actual)} faces")
    print("PASS: exactly 26 face templates certify the three planar rotations")
    print("NO matching solver and NO planarity-search implementation used")


if __name__=="__main__":
    main()
