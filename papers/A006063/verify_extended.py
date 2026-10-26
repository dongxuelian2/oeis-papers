#!/usr/bin/env python3
"""Independent certificate audit for exact A006063/A096680 classifications.

Finite certificates are verified by direct integer/set computations:
- A006063 below 173: explicit positive permutations or explicit Hall obstructions.
- A006063 >=173: 109 irreducible-to-reflection starting witnesses suffice.
- A096680: explicit alternating cycles for every base case with >=2 solutions;
  uniqueness of the remaining finite positives is certified by DAG acyclicity.
The infinite conclusions rest on the accompanying mathematical induction.
"""
import json
from pathlib import Path
from verify import check, cubes_through

HERE = Path(__file__).resolve().parent / "certificates"


def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def reflect(perm, cube, n):
    m = len(perm)
    if not (m < n and cube == m + n + 1):
        raise AssertionError("invalid reflection parameters")
    result = list(perm) + [cube - i for i in range(m + 1, n + 1)]
    check(n, result)
    return result


def directed_edges(perm):
    n = len(perm)
    inverse = [0] * (n + 1)
    for i, v in enumerate(perm, 1):
        inverse[v] = i
    cubes = cubes_through(2 * n)
    return [
        [inverse[c-i] for c in sorted(cubes)
         if 1 <= c-i <= n and perm[i-1] != c-i]
        for i in range(1, n + 1)
    ]


def check_unique(perm):
    """Two perfect matchings differ iff an alternating directed cycle exists."""
    n = len(perm)
    edges = directed_edges(perm)
    color = [0] * (n+1)

    def dfs(i):
        color[i] = 1
        for j in edges[i-1]:
            if color[j] == 1:
                return False
            if color[j] == 0 and not dfs(j):
                return False
        color[i] = 2
        return True

    for i in range(1, n+1):
        if color[i] == 0 and not dfs(i):
            raise AssertionError(f"alternating cycle exists at n={n}")


def check_cycle(perm, cycle):
    n = len(perm)
    if (not isinstance(cycle, list) or len(cycle) < 2
            or any(type(i) is not int or i < 1 or i > n for i in cycle)
            or len(set(cycle)) != len(cycle)):
        raise AssertionError(f"invalid cycle at n={n}")
    edges = directed_edges(perm)
    other = list(perm)
    for j, i in enumerate(cycle):
        nxt = cycle[(j+1) % len(cycle)]
        if nxt not in edges[i-1]:
            raise AssertionError(f"invalid alternating edge at n={n}")
        other[i-1] = perm[nxt-1]
    check(n, other)
    if other == perm:
        raise AssertionError(f"cycle failed to change permutation n={n}")
    return other


def check_small():
    data = read("exact_classification_below_173.json")
    yes = {row["n"]: row["p"] for row in data["positive"]}
    no = {row["n"]: row["S"] for row in data["negative"]}
    if set(yes) & set(no) or set(yes) | set(no) != set(range(1, 173)):
        raise AssertionError("classification does not partition 1..172")
    for n, perm in yes.items():
        check(n, perm)
    for n, S in no.items():
        if (not S or len(S) != len(set(S))
                or any(type(i) is not int or i < 1 or i > n for i in S)):
            raise AssertionError(f"malformed Hall set, n={n}")
        cubes = cubes_through(2*n)
        neighbors = {c-i for i in S for c in cubes if 1 <= c-i <= n}
        if len(neighbors) >= len(S):
            raise AssertionError(f"not a Hall deficiency, n={n}")
        if neighbors.intersection(S):
            raise AssertionError(f"negative Hall set is not independent, n={n}")
    expected = [
        7,19,26,37,44,56,63,66,68,80,82,85,87,98,100,103,105,
        110,112,115,116,117,118,119,120,121,122,123,124,125,126,
        127,128,129,130,131,132,133,135,147,149,150,151,152,155,
        156,159,171,
    ]
    if sorted(yes) != expected:
        raise AssertionError("small-index OEIS membership mismatch")
    print("PASS: exact small classification (48 positive, 124 Hall-negative).")
    return yes


def check_compact():
    core = read("core_109.json")
    expected = set(range(173, 256)) | set(range(339, 365))
    if set(map(int, core)) != expected:
        raise AssertionError("incorrect compact base index set")
    constructed = {}
    for n in range(173, 365):
        if str(n) in core:
            constructed[n] = core[str(n)]
            check(n, constructed[n])
        else:
            constructed[n] = reflect(constructed[511-n], 512, n)
    if len(constructed) != 192:
        raise AssertionError("bad reconstructed base count")
    # Legacy full certificate is a separate 192-row cross-check, not
    # assumed to match the newly generated witness permutation termwise.
    archive = read("base_permutations.json")
    if len(archive) != 192:
        raise AssertionError("bad archive size")
    for n in range(173, 365):
        check(n, archive[n-173])
    print("PASS: 109 compact witnesses imply all 192 base cases.")
    return constructed, archive



def check_reused_small_compression(yes):
    """Optimal reflection-only basis: empty seed + 48 early + 60 new."""
    core = read("core_60_with_empty.json")
    if len(core) != 60:
        raise AssertionError("expected exactly 60 additional seed lengths")
    known = {0: []}  # Full interval reflection when c=n+1 is a cube.
    known.update(yes)
    witnessed = 0
    reflected = 0
    for n in range(173, 365):
        options = []
        for c in sorted(cubes_through(2*n)):
            m = c-n-1
            if 0 <= m < n and m in known:
                options.append((m, c))
        if options:
            if str(n) in core:
                raise AssertionError(f"unnecessary core-60 witness n={n}")
            m, c = options[0]
            known[n] = reflect(known[m], c, n)
            reflected += 1
        else:
            if str(n) not in core:
                raise AssertionError(f"missing irreducible seed n={n}")
            known[n] = core[str(n)]
            check(n, known[n])
            witnessed += 1
    if (witnessed, reflected) != (60, 132):
        raise AssertionError("unexpected compression totals")
    assert known[342] == [343-i for i in range(1,343)]
    print("PASS: empty matching + 48 early positives + 60 new seeds "
          "cover all 192 sizes n=173..364.")

def check_multiplicity(yes, archive):
    data = read("second_solutions.json")
    multiple_small = {}
    for row in data["small"]:
        n = row["n"]
        if n in multiple_small or n not in yes:
            raise AssertionError("bad small multi-index")
        check_cycle(yes[n], row["cycle"])
        multiple_small[n] = row["cycle"]
    expected_small = {112,115,116,117,119,124,125,126,127,128,129,130,133}
    if set(multiple_small) != expected_small:
        raise AssertionError("unexpected small multiple-permutation cases")
    for n, perm in yes.items():
        if n not in multiple_small:
            check_unique(perm)
    check_unique(archive[0])
    check_unique(archive[1])

    tail = data["tail"]
    if [row["n"] for row in tail] != list(range(175, 365)):
        raise AssertionError("tail multiplicity base indices incorrect")
    for row in tail:
        check_cycle(archive[row["n"]-173], row["cycle"])

    exceptional = data["exceptional"]
    if {row["n"] for row in exceptional} != {554, 555}:
        raise AssertionError("missing multiplicity exceptions")
    for row in exceptional:
        n = row["n"]
        m = 728 - n
        perm = reflect(archive[m-173], 729, n)
        check_cycle(perm, row["cycle"])
    third = read("third_solutions.json")
    if [row["n"] for row in third["tail"]] != list(range(175, 365)):
        raise AssertionError("third-solution base index mismatch")
    first_tail = {row["n"]: row["cycle"] for row in tail}
    for row in third["tail"]:
        n = row["n"]
        perm = archive[n-173]
        first = check_cycle(perm, first_tail[n])
        second = check_cycle(perm, row["cycle"])
        if first == second:
            raise AssertionError(f"two cycles gave same extra matching n={n}")
    if {row["n"] for row in third["exceptional"]} != {554, 555}:
        raise AssertionError("third-solution exception index mismatch")
    first_exc = {row["n"]: row["cycle"] for row in exceptional}
    for row in third["exceptional"]:
        n = row["n"]
        perm = reflect(archive[728-n-173], 729, n)
        first = check_cycle(perm, first_exc[n])
        second = check_cycle(perm, row["cycle"])
        if first == second:
            raise AssertionError(f"duplicate third matching n={n}")
    print("PASS: complete A096680 classification and THREE "
          "distinct solutions for all n>=175 by induction.")


def integer_cuberoot(x):
    lo, hi = 0, 1
    while hi**3 <= x:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**3 <= x:
            lo = mid
        else:
            hi = mid
    return lo



def count_at_175_exact(permutation):
    """Exact permanent using directed SCCs; only nontrivial SCC has size 10."""
    n = len(permutation)
    edges = directed_edges(permutation)
    rev = [[] for _ in range(n+1)]
    for u in range(1, n+1):
        for v in edges[u-1]:
            rev[v].append(u)
    seen, order = set(), []

    def forward(u):
        seen.add(u)
        for v in edges[u-1]:
            if v not in seen:
                forward(v)
        order.append(u)

    for u in range(1, n+1):
        if u not in seen:
            forward(u)
    seen.clear()
    components = []

    def backwards(u, comp):
        seen.add(u)
        comp.append(u)
        for v in rev[u]:
            if v not in seen:
                backwards(v, comp)

    for u in reversed(order):
        if u not in seen:
            comp = []
            backwards(u, comp)
            components.append(comp)
    nonsingletons = [sorted(c) for c in components if len(c)>1]
    if n != 175 or nonsingletons != [[4,11,16,23,41,48,102,114,168,175]]:
        raise AssertionError("unexpected 175-component decomposition")

    total = 1
    for comp in nonsingletons:
        idx = {v:j for j,v in enumerate(comp)}
        dp = {0: 1}
        for u in comp:
            nxt = {}
            allowed = [u] + edges[u-1]
            for mask, count in dp.items():
                for v in allowed:
                    j = idx.get(v)
                    if j is not None and not (mask & (1 << j)):
                        nxt[mask | (1 << j)] = nxt.get(mask | (1 << j), 0) + count
            dp = nxt
        total *= dp.get((1 << len(comp))-1, 0)
    if total != 3:
        raise AssertionError(f"P(175) should be exactly 3, got {total}")
    print("PASS: P(175)=3 exactly by a 10-by-10 permanent with 165 forced rows.")


def check_numeric_guards(limit=100000):
    # Additional implementation tests, NOT substitutes for algebraic lemmas.
    for n in range(365, limit+1):
        k = integer_cuberoot(2*n)
        candidates = [j**3 for j in (k, k+1)]
        if not any(n+174 <= c <= 2*n for c in candidates):
            raise AssertionError(f"existence gap n={n}")
        if n >= 556 and not any(n+176 <= c <= 2*n for c in candidates):
            raise AssertionError(f"multiplicity gap n={n}")
        if n >= 9842:
            children = [(k-j)**3-n-1 for j in range(3)]
            if not all(173 <= m < n for m in children):
                raise AssertionError(f"three-branch gap n={n}")
            if not all(integer_cuberoot(2*m) >= k-6 for m in children):
                raise AssertionError(f"three-branch height drop n={n}")
    print(f"PASS: numerical smoke tests for all structural inequalities n<= {limit}.")


def main():
    yes = check_small()
    _, archive = check_compact()
    check_reused_small_compression(yes)
    check_multiplicity(yes, archive)
    count_at_175_exact(archive[2])
    check_numeric_guards()
    print("ALL EXTENDED CERTIFICATES PASS")


if __name__ == "__main__":
    main()
