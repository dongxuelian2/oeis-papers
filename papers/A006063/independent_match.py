#!/usr/bin/env python3
"""Second implementation: independent DFS augmenting-path existence check.

This implementation does not consume the archived witnesses. It computes new
matchings from the cube-sum graph for all 192 base cases and verifies them.
No third-party packages are needed.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify import check


def independent_matching(n):
    cubes = []
    k = 2
    while k**3 <= 2*n:
        cubes.append(k**3)
        k += 1
    neighbors = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        neighbors[i] = [c-i for c in cubes if 1 <= c-i <= n]

    right_partner = [0]*(n + 1)

    def augment(left, visited):
        for right in neighbors[left]:
            if right in visited:
                continue
            visited.add(right)
            previous = right_partner[right]
            if previous == 0 or augment(previous, visited):
                right_partner[right] = left
                return True
        return False

    for left in range(1, n + 1):
        if not augment(left, set()):
            raise AssertionError(f"no matching found for n={n}")
    permutation = [0]*(n + 1)
    for right in range(1, n + 1):
        permutation[right_partner[right]] = right
    return permutation[1:]


def main():
    for n in range(173, 365):
        check(n, independent_matching(n))
    print("PASS: independent augmenting-path matching for all n=173..364.")


if __name__ == "__main__":
    main()
