#!/usr/bin/env python3
"""Pure integer audit of the forced cube-reflection peeling proof.

No archived permutations, MILP, matching or determinant atlas.
Reconstructs the three parametrized forced bands for 173..181,
the exact leaf-stripping rounds for 173..175, their residual cores,
and the count of the ten-vertex residual cube graph.
"""
from collections import Counter

CUBES = {k**3 for k in range(2, 10)}


def neighbors(i, remaining):
    return [j for j in remaining if i+j in CUBES]


def peel_batch(remaining, firsts):
    """firsts: [(i,c),...] with requested unique neighbor c-i."""
    expected = []
    paired = set()
    for i, c in firsts:
        j = c-i
        assert i in remaining and j in remaining
        assert neighbors(i, remaining) == [j], (i, c, neighbors(i, remaining))
        assert i not in paired and j not in paired
        paired.update((i, j))
        expected.append((i, j, c))
    assert all(i+j in CUBES for i,j,_ in expected)
    remaining.difference_update(paired)
    return expected


def first_three(n):
    return [
        [(i,216) for i in range(125,343-n)],
        [(i,64) for i in range(34,216-n)],
        [(i,216) for i in range(95,277-n)],
    ]


SINGLETONS = [
    (113,216),(22,27),(3,125),(94,125),(33,125),
    (124,125),(7,27),(105,216),(14,27),(112,216),
    (21,27),(2,125),(93,125),
]


def batches(n):
    out = first_three(n)
    if n == 173:
        out += [
            [(4,8),(5,8)] + [(i,27) for i in range(8,13)],
            [(i,216) for i in (45,46,106,107,108,122)],
            [(31,64),(172,216),(173,216)],
        ]
        out += [[a] for a in [
            (92,216),(1,8),(20,125),(111,125),
            (13,125),(104,125),(6,8),(123,216),(32,64),
        ]]
    else:
        out += [
            ([(4,8)] if n == 174 else []) +
            [(i,27) for i in range(8, 12 if n==174 else 11)],
            [(i,216) for i in (45,46,47,106,107,108)],
            [(15,27)] + [(i,216) for i in (172,173,174)],
        ]
        out += [[v] for v in SINGLETONS]
    return out


def peel(n):
    rem=set(range(1,n+1))
    forced={}
    records=[]
    for batch in batches(n):
        pairs=peel_batch(rem,batch)
        for i,j,c in pairs:
            assert i not in forced and j not in forced
            forced[i]=j
            forced[j]=i
        records.append(pairs)
    return forced, rem, records


def count_core(core):
    core=tuple(sorted(core))
    def go(rows,used_cols):
        if not rows:
            return 1
        i=rows[0]
        return sum(go(rows[1:],used_cols|{j}) for j in core
                   if j not in used_cols and i+j in CUBES)
    return go(core,frozenset())


def main():
    # Three symbolic bands; after each prescribed removal, every
    # first endpoint has exactly one legal neighbor.
    for n in range(173,182):
        rem=set(range(1,n+1))
        counts=[]
        for b in first_three(n):
            counts.append(len(peel_batch(rem,b)))
        assert counts == [218-n,182-n,182-n]
        assert sum(counts) == 582-3*n

    p173,r173,z173=peel(173)
    p174,r174,z174=peel(174)
    p175,r175,z175=peel(175)
    assert not r173 and not r174
    assert len(p173)==173 and len(p174)==174
    assert [len(x) for x in z173]==[45,9,9,7,6,3]+[1]*9
    assert [len(x) for x in z174]==[44,8,8,5,6,4]+[1]*13
    assert [len(x) for x in z175]==[43,7,7,3,6,4]+[1]*13
    assert {i for i,j in p173.items() if i==j}=={4,32,108}
    assert {i for i,j in p174.items() if i==j}=={4,108}

    expected={4,11,16,23,41,48,102,114,168,175}
    assert r175==expected
    assert len(p175)==165
    cycle=[23,41,175,168,48,16,11,114,102]
    edges={(min(i,j),max(i,j)) for i in expected for j in expected
           if i+j in CUBES and i<=j}
    cycle_edges={(min(a,b),max(a,b)) for a,b in zip(cycle,cycle[1:]+cycle[:1])}
    assert edges==cycle_edges|{(4,4),(4,23)}
    assert count_core(expected)==3

    changed={i for i in range(1,174) if p173[i]!=p174[i]}
    target=set(sum((list(range(a,b+1)) for a,b in [
        (1,3),(5,7),(13,14),(20,22),(31,33),(42,42),
        (92,94),(104,105),(111,112),(122,124)]),[]))
    assert changed==target and len(changed)==25
    print("PASS: symbolic three-band peeling for all 173<=n<=181")
    print("PASS: forced matching unique at n=173 (3 fixed points)")
    print("PASS: forced matching unique at n=174 (2 fixed points)")
    print("PASS: n=175 has 10-vertex loop+9-cycle core, exactly 3 permutations")
    print("PASS: any 173->174 extension rewires exactly 25 old rows")


if __name__=="__main__":
    main()
