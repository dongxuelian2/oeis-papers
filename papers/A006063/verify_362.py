#!/usr/bin/env python3
"""Solver-free, exact certificate that P(362) >= 2**40.

Reads 43 constant-cube interval rows and 40 pairwise disjoint
alternating directed cycles. Reconstructs the permutation by exact
integer operations and checks every altered edge directly.
"""
import json
from pathlib import Path

FILE = Path(__file__).resolve().parent / "certificates" / "forty_cycles_362.json"


def read_and_verify():
    data = json.loads(FILE.read_text(encoding="utf-8"))
    n = data["n"]
    assert n == 362
    p = [0] * (n + 1)
    for lo, hi, cube in data["blocks"]:
        assert 1 <= lo <= hi <= n
        assert any(k**3 == cube for k in range(2, 10))
        for i in range(lo, hi + 1):
            assert p[i] == 0, ("overlapping intervals", i)
            p[i] = cube - i
    assert sorted(p[1:]) == list(range(1, n + 1))
    assert all(any(k**3 == i+p[i] for k in range(2, 10))
               for i in range(1, n+1))

    cycles = data["cycles"]
    assert len(cycles) == 40
    seen = set()
    for cycle in cycles:
        assert 2 <= len(cycle) <= n
        assert len(set(cycle)) == len(cycle)
        for j, u in enumerate(cycle):
            v = cycle[(j+1) % len(cycle)]
            assert 1 <= u <= n and u not in seen
            seen.add(u)
            assert any(k**3 == u+p[v] for k in range(2,10)), (u,v)

    # Optional spot-check: flip all cycles simultaneously.
    q = p.copy()
    for cycle in cycles:
        for j, u in enumerate(cycle):
            q[u] = p[cycle[(j+1) % len(cycle)]]
    assert sorted(q[1:]) == list(range(1, n+1))
    assert all(any(k**3 == i+q[i] for k in range(2, 10))
               for i in range(1, n+1))
    assert q != p
    print(f"PASS: {len(data['blocks'])} cube-reflection rows, "
          f"{len(cycles)} vertex-disjoint alternating cycles, "
          f"{len(seen)} vertices switched.")
    print("CERTIFIED: P(362) >= 2**40.")
    return p, cycles


if __name__ == "__main__":
    read_and_verify()
