# Three four-cube phases for the [467,665] high-start problem

**Research status: completely checked finite experiments; a uniform
non-computational matching proof remains OPEN.**

The original five-cube high-start experiment found involutions
for all 199 lengths using sums
`{216,343,512,729,1000}`.
A more restrictive reanalysis shows that **no individual
length requires all five cube sums to obtain an involution**.
Three **four-cube palettes** suffice, with a uniform
fixed-point rule for each phase.

## 1. The three-phase four-cube statement

Let `P_C(n)` denote existence of an involution
`p:[1,n]->[1,n]` such that all `i+p(i)` belong
to a specified set of integer cubes `C`.

**Proposed four-cube phase theorem (experimentally verified):**

| length n | four allowed cubic sums | fixed points |
|---|---|---|
| 467 through 560 | 216,343,512,729 | none if even; exactly 108 if odd |
| 561 through 579 | 216,512,729,1000 | none if even; exactly 108 if odd |
| 580 through 665 | 343,512,729,1000 | none if even; exactly 256 if odd (500 also works) |

These three phases comprise 94, 19 and 86
lengths respectively, totaling 199.

Every one of these cases was found and checked
by an independent **general-graph Edmonds-blossom
maximum-matching computation** (not merely a
bipartite permanent/permutation check).
The experimental audit is in
[verify_high_start_four_color_phases.py](verify_high_start_four_color_phases.py).

**Not yet proved:** A single theorem establishing
all three intervals without 199 separate
matching computations. Therefore the proposed
phase theorem is **not a certified
computation-free result**.

## 2. Correct cubic fixed points for each palette

An involution with a single fixed point f must satisfy
`2*f in C`. This is a **necessary arithmetic constraint
before any graph-matching argument**.

- Phases I and II include 216, so the odd-n fixed
  point **108** is valid.
- Phase III omits 216. Its only permitted fixed points
  from even cubes are **256** (sum 512) and
  **500** (sum 1000). In particular **108 is forbidden
  at every odd Phase III length**, not only 581.
- Independent full-band general-graph matching
  checks find an involution at every odd n in
  581..665, **with either 256 or 500 as the
  sole fixed point**. Even n admit no fixed points.

**Correction to the earlier research log:** The previous
statement that Phase III could fix 108 at all odd
lengths except 581 was false. It omitted the
elementary requirement `2*f in C` and its
corresponding experimental verifier failed its
own fixed-point check. Both the verifier and the
phase theorem have now been corrected.

### A separate, stronger hybrid Tutte barrier at 581

The [31-interval Tutte certificate](TUTTE_OBSTRUCTION_581.md)
still proves a mathematically meaningful but
different assertion: if the fifth cube 216
were admitted **solely for the fixed point 108**
and every nontrivial 2-cycle were restricted to
the four cubes `{343,512,729,1000}`, then
n=581 would remain impossible. Deleting 108
and a 103-vertex set leaves 105 odd components.
Therefore any five-cube involution at 581 fixing
108 must also use cube 216 in **at least one
nontrivial 2-cycle**. This is an auxiliary
five-color restriction, not a four-color
fixed-point exception.

### A bounded-defect Hall and Pfaffian reduction (PROVED)

The [exact defect-matching theorem](BOUNDED_DEFECT_HALL_REDUCTION.md)
strengthens the 14/10/16-edge
bipartization: **all exceptional
edges are pairwise vertex-disjoint**.
Moreover, both endpoints of every
exceptional edge lie in the **same
class** of the bipartite graph left
after deleting these edges.

Thus a perfect four-cube involution
exists exactly when one can select a
subset `S` of **at most 16 prescribed
pairwise disjoint edges** and prove
Hall's bipartite matching criterion
after removing their endpoints.
The necessary balancing equation is
`|S_U|-|S_V|=(|U|-|V|)/2`,
and the observed absolute imbalance
is at most **4/8/4** across the
three phases. The perfect-matching
count has the exact positive expansion
`m(G)=sum_{S subset F} m(H-V(S))`
into at most `2^16` bipartite terms.
Algebraically, the exceptional edges
give a skew-adjacency/Pfaffian update
of rank at most **32**.

The [pure-arithmetic checker](verify_defect_matching_reduction.py)
audits all class alignments and
imbalance bounds without using a
general-graph matching solver.
This is an equivalence and a
constant-size algebraic reduction,
**not yet a phase-wide Hall proof**.

### At most 16 exceptional edges from a bipartite graph (PROVED)

The [four-odd-face near-bipartite theorem](FOUR_ODD_FACES_NEAR_BIPARTITE.md)
combines the explicit planar rotations with
**two vertex-disjoint paths in the planar dual**
joining the four odd faces. The corresponding
primal edges, in dual-path order, are completely
listed for each maximal graph.
Removing **14 / 10 / 16** edges, respectively,
makes the Phase I / II / III maxima bipartite.
Every shorter graph, and either permitted
fixed-vertex deletion, inherits the same
phase-independent exceptional-edge set.

This changes the remaining positive
existence question into **bipartite Hall
conditions plus a bounded selection
from at most 16 specified edges**.
In particular, for a bipartition U,V
of the edge-deleted graph, each complete
matching must use at least
`abs(|U|-|V|)/2` exceptional edges.
The observed bipartition imbalances
are at most 4/8/4 in the three phases.

An [exact integer/dual-face checker](verify_near_bipartite_phases.py)
audits the three crossing-edge paths
and bipartiteness at every n,
without a matching or planarity
library. **Bipartiteness after
deleting a few edges does not
itself prove perfect matching.**

### Phase I requires only four exceptional-edge Hall templates

The new [Phase I four-pattern reduction](PHASE_I_FOUR_HALL_PATTERNS.md)
shows that all 94 lengths `467..560`
can be corrected using exactly
four finite exceptional-edge choices,
selected from their canonical
bipartition imbalance. They are
`empty`, `{(84,132)}`,
`{(101,115)}` (only n=559),
or `{(70,146),(84,132)}`.
The balancing equation holds
algebraically; an optional
[94-case augmenting-path audit](verify_phase_i_hall_patterns.py)
confirms a bipartite perfect matching
of each remainder. The necessary
uniform Hall theorem is **not yet
proved without finite computation**.

### Only 10–16 edges obstruct bipartiteness (PROVED)

The [bounded bipartite-core theorem](SMALL_BIPARTITE_CORE.md)
identifies one fixed deletion set per
palette, of sizes **14,10,16**. Each
set makes the corresponding endpoint
graph (n=560,579,665) bipartite.
All smaller phase graphs inherit
that property after restricting the
same deleted edges. A planar-dual
four-odd-face `T`-join argument
also proves these sizes are
**minimum possible for the maximal
graphs**.

**Exact reformulation:** For every
proposed perfect matching, the edges
among those at most 16 exceptional
edges form a matching Q, and the
remaining vertices have a matching
inside the bipartite graph obtained
by deleting all exceptional edges.
Conversely, finding such Q plus
a bipartite perfect matching
constructs the original involution.
The only outstanding positive step
is a uniform Hall statement for
the corresponding bipartite remainders.

### Uniform planar embedding across all 199 lengths (PROVED)

The [three-rotation planarity theorem](THREE_ROTATION_PLANARITY.md)
gives a remarkably compact embedding certificate:
for each phase's maximum n=560,579,665, place
the incident edges in the **same cyclic
color order at every vertex**:

```
Phase I:   (216,343,512,729)
Phase II:  (216,512,729,1000)
Phase III: (343,729,512,1000)
```

The exact dart-rotation face counts are
`(V,E,F)=(560,729,171),(579,656,79),
(665,892,229)`, respectively. Every
case has Euler characteristic `V-E+F=2`,
so these give connected planar embeddings.
Every smaller graph within the same
palette is an **induced subgraph** of the
corresponding maximum graph, so planarity
follows automatically for all 199 lengths
and remains true after deleting either
valid fixed point.

The [arithmetic-only rotation verifier](verify_three_rotation_planarity.py)
uses just integer reflection edges,
a cyclic permutation of darts and
Euler's formula: no matching or
planarity-finding library. Planarity
does not itself prove perfect-matching
existence, but it makes planar
Tutte/Pfaffian techniques available.

### A second short-path factorization: 245 even-cube paths

The [dual-reflection path theorem](DUAL_REFLECTION_PATHS.md)
shows that the **512/1000-only graph** has exactly
245 connected components for every 580<=n<=665:
one singleton, `744-n` 2-paths, `n-511`
3-paths, and 11 constant 4-paths. Its proof
merges 22 of the initial 512-reflection pairs
into eleven 4-paths and attaches each new
vertex to one remaining pair.

Under fixed point **256**, its even-cube
skeleton has **244 components and no
singletons**, while its odd-cube skeleton
has **194 components and at least one
singleton**. Under fixed point **500**,
the respective counts are **245 even
components with two singletons** and
**193 odd components with none**.
Thus both valid fixed-point choices
satisfy the exact relation
`#odd_components + #even_components = 438`,
but they simplify different two-cube
quotient descriptions.

The [standard-library audit](verify_dual_reflection_paths.py)
checks all component-size formulas,
without a matching solver. **Neither
short-path decomposition by itself
proves a perfect matching in the
four-cube union.**

### Complete third-phase forcing and the two valid fixed-point choices

Two new results sharpen the Phase III matching problem:

- [Phase III fixed-point duality](PHASE_III_FIXED_POINT_DUALITY.md)
  gives exact formulas for the odd component defect
  `q_256(n)=729-n`, and `q_500(n)=727-n`
  for odd n<=613, or `729-n` for odd n>=615.
  These imply rigorous necessary lower bounds
  for the number of 512/1000-colored 2-cycles.
- [Complete Phase III forced cascades](PHASE_III_FORCED_CASCADE.md)
  proves that, under fixed point 500, every odd
  n=581..601 has the same five forced pairs;
  all odd n=603..665 have only the forced pair
  `12<->331`. Under fixed point 256, the
  corresponding exact numbers of forced pairs
  are 6 / 3 / 4 / 0 in the intervals
  581..587 / 589..627 / 629..641 / 643..665.

The cascade proof requires only **six elementary
boundary checks** and monotonicity, not 86
independent matching searches. Both statements
are necessary structural results; neither
supplies a perfect matching of the final core.
The optional [standard-library verifier](verify_phase_iii_cascade.py)
audits all formulas and forced pairs.

## 3. Why the phase structure is mathematically useful

The three palettes overlap and differ
by replacing exactly one reflection:

```
Phase I:   {216,343,512,729}        (without 1000)
Phase II:  {216,512,729,1000}       (without 343)
Phase III: {343,512,729,1000}       (without 216)
```

Each phase can be attacked using **one
four-reflection graph**, instead of
requiring all five reflections at
every n. The short middle phase
561..579 is only 19 lengths long.

The symbolic [193-path quotient theorem](ODD_CUBE_PATH_QUOTIENT.md)
applies particularly to Phases I and III,
which both retain the odd reflections
343 and 729. In those phases, the
remaining two **even** reflections
must satisfy the path-local state
constraints of the finite-state
gadget theorem. Phase II uses a
different underlying odd-cube
skeleton, with 729 as its sole
odd reflection; proving it may
require a different local reduction.

A future proof may therefore split
naturally into three shorter structural
lemmas, rather than one large
five-reflection Tutte criterion.

**Subtlety:** No single one of these three four-cube palettes
covers all 199 lengths under the proposed fixed-point rule.
The previously established Hall
certificates show that *every cube in
the five-cube union* is indispensable
to that **uniform palette**; this is
fully compatible with each n using
some four-cube subset *depending on n*.

### Exact initial forced-edge regimes (PROVED)

A separate [four-cube boundary-forcing theorem](FOUR_CUBE_BOUNDARY_FORCING.md)
classifies every **degree-one vertex** in all three
palette phases. In Phase I at 512<=n<=560,
the full suffix [512,n] must be reflected under
sum 729; at odd n, 404<->325 is also forced.
Phase II always begins with exactly two forced
edges: 256<->473 plus either 108<->404 (even)
or 404<->325 (odd). In Phase III, even n
have no initial degree-one vertices; with
fixed point 256, odd n force 87<->425
through n=641 and have no initial leaves
from n=643 onward.

All of this is proved by reflection-domain
arithmetic and checked by
[verify_four_cube_boundary_forcing.py](verify_four_cube_boundary_forcing.py)
without using any matching solver. These
are **necessary local assignments**, not
a phase-wide positive existence theorem.

## 4. Two-seed path ladders and the exact augmentation lemma

**Elementary alternating-path flip lemma (PROVED).**
Suppose an even-vertex subset has a perfect
matching M. Add two new vertices x,y.
Suppose the augmented graph admits a
simple path from x to y with edges
alternating **outside M / inside M /
outside M / ... / outside M**.
Then toggling the edge membership
along that path produces a perfect
matching of the augmented graph.

**Proof.** Every internal vertex has
exactly one incident path edge in M
and exactly one path edge outside M;
the toggle exchanges those choices.
Both unmatched endpoints x,y gain one
matching edge. No other matching
edge changes. QED.

This lemma preserves the cube-sum condition
if every path edge is permitted by its
cube sum. For odd n, removing the
chosen fixed point before applying the
lemma also preserves its single
fixed point upon extending n to n+2.

An optional two-seed experiment,
[verify_high_start_two_seed_ladder.py](verify_high_start_two_seed_ladder.py),
uses the full five-color palette,
finds initial matchings at n=467 and
468, and then performs *only*
alternating-path flips:

```
467 -> 469 -> ... -> 665   (99 verified transitions)
468 -> 470 -> ... -> 664   (98 verified transitions)
```

The largest observed alternating path
uses 47 edges on the odd ladder and
45 edges on the even ladder. This
reproduces 199 involutions with only
**two initial general-matching searches**,
but the path existence at all 197
steps is **still computationally checked,
not proved by a general expansion lemma**.
Moreover it uses five colors, so it
is independent of the pointwise
four-color phase observation.

## 5. Revised research target

The right next step is no longer
`prove one five-cube Tutte theorem over 199 lengths`.

It is more precise to ask for:

1. A uniform four-reflection matching
   argument over **467..560**, palette
   `{216,343,512,729}`.
2. A second, possibly shorter theorem
   for **561..579**, palette
   `{216,512,729,1000}`.
3. A third matching theorem for
   **580..665**, palette
   `{343,512,729,1000}`, allowing
   fixed point **256 at 581**.

All three are currently supported
by computation, not completed
symbolic matching arguments.
Proving them without numeric case
lists would yield the stronger
existence statement that every
`n>=467` has a cube-sum involution,
after applying the already proved
cubic suffix interval avalanche.
The lower range `173..466` still
requires a separate argument.

The prior mathematical theorems on
unimodular determinant shapes,
forced leaf peeling and the
infinite avalanche are unaffected.
