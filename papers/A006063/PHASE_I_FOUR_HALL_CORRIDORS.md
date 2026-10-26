# Phase I: only four exceptional-edge choices appear necessary

**EXPERIMENTALLY VERIFIED, NOT A CASE-FREE MATCHING THEOREM.**
This isolates a particularly narrow constructive target
for the first high-start phase `467<=n<=560`.
It builds on the rigorously proved
[14-edge optimal bipartization](FOUR_ODD_FACES_NEAR_BIPARTITE.md)
and its [exact Hall reduction](BOUNDED_DEFECT_HALL_REDUCTION.md).

## 1. Four candidate subsets from the same 14 edges

Let C=`{216,343,512,729}`.
For every n, remove the fixed point `108`
if n is odd. Remove the 14 fixed phase-I
exceptional edges to obtain a bipartite
graph `H_n` with its inherited
bipartition U,V from maximal n=560.
Let

```
delta(n) = abs(|U|-|V|).
```

The [standard-library arithmetic audit](verify_defect_matching_reduction.py)
shows that delta(n) can only be
`0,2,4` in this entire band, occurring
exactly 8,54,32 times respectively.

The following **single-valued rule for S(n)**
was found to pass bipartite matching
checks at all 94 lengths:

| condition | selected exceptional pairs S(n) | lengths |
|---|---|---:|
| delta=0 | empty set | 8 |
| delta=2, n<560 | {(101,115)} | 53 |
| delta=2, n=560 | {(84,132)} | 1 |
| delta=4 | {(67,149),(84,132)} | 32 |

The selected pairs sum to 216,216,
and 216/216 respectively. In particular,
only **cube 216** is needed for these
exceptional edges, even though the full
phase-I graph uses all four cube sums.
All selected exceptional pairs are
mutually vertex-disjoint and lie in
the larger side of the inherited
bipartition, making their selection
compatible with the balance condition.

**Experimental claim.** In every one
of the 94 tests, the ordinary bipartite
graph

```
H_n - V(S(n))
```

has a perfect matching. This was
checked with a bipartite
maximum-matching routine, not
established by a symbolic Hall lemma.

## 2. Exact target needed to make it a theorem

By the proved exceptional-edge
decomposition, the following
four-case claim would suffice
to establish a completely
non-general-matching construction
for Phase I:

**Four-corridor Hall conjecture.**
For every 467<=n<=560, the specific
S(n) above satisfies

```
|N_{H_n - V(S(n))}(X)| >= |X|
for all X subset U_n - V(S(n)).
```

The equality of the bipartition sizes
is already a consequence of the
proved delta(n) distribution and
the specified exceptional-edge classes.
What remains is only the **Hall
inequality**; all other properties
are algebraically established.

This narrows 94 unrelated
general-graph matching problems
to four **fixed exceptional
boundary conditions** on the
same explicit bipartite reflection
graph. The interval 512<=n<=560
also has an explicit forced-reflection
suffix `i<->729-i` for all i>=512.
After peeling that suffix, one may
try to prove a uniform Hall inequality
on the common low-vertex core.

## 3. Numerical and logical scope

- The four-corridor selection rule
  is **supported by 94 full bipartite
  matching tests**, not by a
  computation-free Hall proof.
- The 14-edge bipartization, its
  optimality at n=560, the
  bipartition balance condition,
  and the general exceptional-edge
  matching decomposition are
  **mathematically proved**.
- A proof of four-corridor Hall
  would settle Phase I. Phases II
  and III would still require
  their own positive Hall
  conditions; the original
  173..466 interval would remain
  a separate obligation.
