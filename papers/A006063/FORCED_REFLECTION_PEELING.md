# Forced reflection peeling: a symbolic local avalanche and exact counts at 173–175

**Status: PROVED.** This is a mathematically different construction
from the 57 cubic-order determinant shapes. It certifies the first
three consecutive admissible lengths by elementary forced-neighbor
arguments and gives a uniform **three-band stripping theorem** for
every `173<=n<=181`.

The counts `P(173)=1`, `P(174)=1`, `P(175)=3` agree with
OEIS A096904; the purpose here is to explain these counts and
constructions directly, without a permanent, solver, or
endpoint-multiset atlas.

## 1. Universal leaf-reflection lemma

Let `V` be a finite set of distinct positive integers. Let
`H(V)` be the undirected, loop-permitting graph with vertices
`V`, in which `i` and `j` are adjacent exactly when
`i+j` is a perfect cube (loops allowed when `2*i` is a cube).
A cube-sum permutation of `V` means a bijection `p:V->V`
for which every `i+p(i)` is a cube.

**Forced-leaf lemma.** If a vertex `i` has exactly one
neighbor `j` in `H(V)`, every cube-sum permutation of
`V` must satisfy **both** `p(i)=j` and `p(j)=i`.
Removing the forced one-vertex loop (if `i=j`) or the
two-vertex reflected pair (if `i!=j`) gives a
**bijection** between all cube-sum permutations of
`V` and those of `V\{i,j}`.

**Proof.** Row `i` has only one allowed image `j`,
hence `p(i)=j`. Because the adjacency relation is
symmetric, column `i` has only row `j` available,
so necessarily `p(j)=i`. Conversely, any permutation
of the smaller set extends uniquely by these assignments.
These choices do not conflict, since the reduced permutation
uses neither the removed rows nor the removed columns. QED.

**Consequences.** One may peel degree-one vertices repeatedly,
in any order. Every resulting forced pair is an involution
edge. If the residual set becomes empty, the entire cube-sum
permutation is **unique** and is necessarily an involution.

## 2. Three symbolic forced bands, for every 173<=n<=181

Let `V=[1,n]`, with `173<=n<=181`. Only the
cubes `8,27,64,125,216,343` can occur as sums,
since `2*n<512`.

**Band 1.** Every vertex in

```
A1(n)=[125,342-n]
```

has exactly one neighbor, namely `216-i`. Indeed,
`i>=125` excludes all cubes `<=125`, while
`343-i>=n+1` excludes `343`. The remaining
`216-i` lies in `[n-126,91]`, so all reflected
pairs are disjoint and may be removed simultaneously.

**Band 2.** After deleting Band 1 and its images,
every vertex of

```
A2(n)=[34,215-n]
```

has exactly one *remaining* neighbor, namely `64-i`.
The possible `125-i` lies in the deleted image interval
`[n-126,91]`; the possible `216-i` exceeds `n`.
Its reflected image interval is `[n-151,30]`,
again disjoint from the other bands.

**Band 3.** After deleting the first two bands and
their images, every vertex of

```
A3(n)=[95,276-n]
```

has exactly one remaining neighbor, namely `216-i`.
The alternative `125-i` lies exactly in the deleted
second-band image interval `[n-151,30]`, and
`343-i>n`. Its reflected images lie in
`[n-60,121]`.

All three bands are valid for the entire interval
`173<=n<=181`, without separately listing nine
integer permutations. Their numbers of forced pairs are

```
|A1(n)|=218-n,
|A2(n)|=182-n,
|A3(n)|=182-n.
```

Hence these three symbolic layers force

```
boxed:  582-3*n
```

reflected pairs and delete **`1164-6*n`** vertices
from `H([1,n])`.

This is a genuine local **forced-edge avalanche**:
each removed interval eliminates an alternative cube,
turning an entire further interval into forced leaves.

## 3. Exact uniqueness for n=173

After the first three bands, use the following sequence
of remaining forced-leaf batches. The notation
`[a,b]:c` means remove every pair `(i,c-i)`
with `a<=i<=b`, and `{...}:c` means remove
each listed `i` with partner `c-i`.

| round | forced first endpoints | cube sums |
|---|---|---|
| 1 | [125,169] | 216 |
| 2 | [34,42] | 64 |
| 3 | [95,103] | 216 |
| 4 | {4,5} and [8,12] | 8 and 27 |
| 5 | {45,46,106,107,108,122} | 216 |
| 6 | {31} and {172,173} | 64 and 216 |
| 7–15 | 92, 1, 20, 111, 13, 104, 6, 123, 32 | 216, 8, 125, 125, 125, 125, 8, 216, 64 |

Each row/batch is an exact forced-leaf rule in the
graph induced by the vertices remaining after the
preceding rounds. These entries can be checked
**by cube subtraction**, using only
`8,27,64,125,216,343`.

The table removes every vertex of `[1,173]`.
By the forced-leaf lemma there is exactly **one**
cube-sum permutation, and it is an involution.
Its three fixed points are `4,32,108`, with
sums `8,64,216`. Thus

```
P(173)=1.
```

This is a direct purely graph-theoretic finite-base
proof of existence and uniqueness at the critical
length 173. It does not depend on the old 173
endpoint atlas row or its unimodular root-word
representation.

## 4. Exact uniqueness for n=174

The analogous forced-leaf rounds are

| round | forced first endpoints | cube sums |
|---|---|---|
| 1 | [125,168] | 216 |
| 2 | [34,41] | 64 |
| 3 | [95,102] | 216 |
| 4 | {4} and [8,11] | 8 and 27 |
| 5 | {45,46,47,106,107,108} | 216 |
| 6 | {15} and {172,173,174} | 27 and 216 |
| 7–19 | 113, 22, 3, 94, 33, 124, 7, 105, 14, 112, 21, 2, 93 | 216, 27, 125, 125, 125, 125, 27, 216, 27, 216, 27, 125, 125 |

Every vertex disappears. Therefore the cube-sum
permutation is unique, involutive, and has fixed
points `4,108`. In particular,

```
P(174)=1.
```

## 5. The ten-vertex core at n=175: exactly three permutations

For n=175, the first three forced layers have sizes
`43,7,7`. Further forced batches are:

- Round 4: `[8,10]` under cube `27`.
- Round 5: `{45,46,47,106,107,108}` under cube `216`.
- Round 6: `{15}` under cube `27`, and
  `{172,173,174}` under cube `216`.
- Rounds 7–19: the **same 13 singleton forced pairs**
  as rounds 7–19 for n=174.

After these 83 forced removals, exactly ten vertices remain:

```
Vcore = {4,11,16,23,41,48,102,114,168,175}.
```

The induced cube-sum graph on these ten vertices
consists **precisely** of:

- the loop at `4`,
- the edge `4—23`,
- and the chordless odd 9-cycle

```
23—41—175—168—48—16—11—114—102—23.
```

Every edge displayed has a cubic endpoint sum;
the cycle sums in order are
`64,216,343,216,64,27,125,216,125`.

If `p(4)=4`, the remaining odd cycle has exactly
two directed cycle covers: the two orientations of
the full 9-cycle. If `p(4)=23`, the singleton
available column 4 forces `p(23)=4`, and the
remaining eight vertices form a path with a
unique covering by four reflected 2-cycles.
There are no other possibilities.

Thus the core has exactly **three** cube-sum
permutations. The forced-leaf lemma preserves the
count, giving

```
P(175)=3.
```

## 6. A lower bound on bounded-radius local extension

The unique permutations at lengths 173 and 174
disagree on **25 pre-existing input positions**:

```
[1,3], [5,7], [13,14], [20,22], [31,33], {42},
[92,94], [104,105], [111,112], [122,124].
```

This set has size 25, as can be verified directly
from the two forced-leaf tables. Therefore **every**
valid procedure extending a permutation of length
173 to length 174 must change all these 25 old
images; a uniformly bounded gadget modifying
fewer than 25 pre-existing rows cannot work here.
One standard alternating augmenting path has
26 newly selected cube-sum edges.

This obstruction is much stronger than simply
observing that 173 has no shorter cubic-suffix
predecessor. It explains why a naive constant-size
local edge-switching lemma is insufficient even
to pass the first threshold.

## 7. Exact scope

These results replace a critical numerical existence
certificate at n=173 with a self-contained forced-leaf
proof, give a parametric three-band avalanche for
173<=n<=181, and explain the abrupt change in the
permutation count at n=175.

They do **not** automatically prove all remaining
lengths 176..364. A general local Hall/augmentation
theorem capable of closing that interval without
further finite parameter choices is still open.
The optional independent forced-stripping checker
reproduces the displayed arithmetic; it is not a
logical premise of the lemmas.
