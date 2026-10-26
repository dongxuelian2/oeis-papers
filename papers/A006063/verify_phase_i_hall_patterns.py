#!/usr/bin/env python3
"""Optional computational Hall audit of four fixed Phase I correction patterns.

It uses only Python standard library but DOES perform 94 bipartite
augmenting-path searches, so its result is NOT a uniform case-free proof.
The near-bipartite reduction and charge balance are independently
proved in SMALL_BIPARTITE_CORE.md and PHASE_I_FOUR_HALL_PATTERNS.md.
"""
from collections import Counter, deque
from verify_small_bipartite_core import CASES, adjacency

LOW,HIGH,PALETTE,ORDER,EXCEPTIONS,_ = CASES[0]


def two_coloring(graph):
    color={1:0}
    q=deque([1])
    while q:
        i=q.popleft()
        for j in sorted(graph[i]):
            if j not in color:
                color[j]=1-color[i]
                q.append(j)
            else:
                assert color[j]!=color[i],(i,j)
    assert len(color)==len(graph)
    return color


def perfect_bipartite_matching(graph, color):
    left=sorted(i for i in graph if color[i]==0)
    right={i for i in graph if color[i]==1}
    if len(left)!=len(right):
        return False

    used_right={}
    def augment(i,seen):
        for j in sorted(graph[i]):
            if j in seen:
                continue
            assert j in right
            seen.add(j)
            if j not in used_right or augment(used_right[j],seen):
                used_right[j]=i
                return True
        return False
    for i in left:
        if not augment(i,set()):
            return False
    return len(used_right)==len(left)


def main():
    full=adjacency(HIGH,PALETTE)
    deletion={tuple(sorted(edge)) for edge in EXCEPTIONS}
    for a,b in deletion:
        full[a].remove(b)
        full[b].remove(a)
    chi=two_coloring(full)
    # Orientation fixed by vertex 1 in the positive class.
    assert chi[1]==0
    hist=Counter()
    patterns=Counter()
    for n in range(LOW,HIGH+1):
        fixed=108 if n%2 else None
        remaining=set(range(1,n+1))
        if fixed is not None:
            remaining.remove(fixed)
        delta=sum(1 if chi[i]==0 else -1 for i in remaining)
        assert delta in (0,2,4), (n,delta)
        hist[delta]+=1
        if delta==4:
            q=((70,146),(84,132))
            label="two-edge"
        elif delta==2 and n==559:
            q=((101,115),)
            label="559-switch"
        elif delta==2:
            q=((84,132),)
            label="one-edge"
        else:
            q=()
            label="no-edge"
        patterns[label]+=1
        assert all(tuple(sorted(e)) in deletion for e in q)
        assert len({i for e in q for i in e})==2*len(q)
        assert all(i in remaining for e in q for i in e)
        assert 2*sum(1 if chi[e[0]]==0 else -1 for e in q)==delta
        for e in q:
            assert chi[e[0]]==chi[e[1]]
        rem=remaining-{x for e in q for x in e}
        G={i:{j for j in full[i] if j in rem} for i in rem}
        assert perfect_bipartite_matching(G,chi),(n,label)
    assert hist==Counter({0:8,2:54,4:32})
    assert patterns==Counter({"no-edge":8,"one-edge":53,
                              "559-switch":1,"two-edge":32})
    print("PASS (EXPERIMENT): all 94 balanced bipartite remainders have perfect matchings")
    print("PASS: correction patterns",dict(patterns))
    print("PASS: imbalances",dict(sorted(hist.items())))
    print("UNPROVED: one uniform Hall theorem replacing these 94 computations")


if __name__ == "__main__":
    main()
