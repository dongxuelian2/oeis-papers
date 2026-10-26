# A006063 — exact bounded-defect Hall/Pfaffian reduction

**PROVED:** All 199 four-cube graphs in the proposed
high-start avalanche band can be described as
a bipartite graph plus a **fixed set of at most
16 mutually vertex-disjoint exceptional edges**.
This is stronger than the 14/10/16 near-bipartite
result: the exceptional edges themselves form
a matching, and every one is monochromatic
in the bipartition of the remaining graph.

**Research status:** The reduction to Hall
conditions and bipartite matching counts
is an equivalence, not a proof that those
conditions always hold. An unconditional
four-color existence theorem is still open.

## 1. Three maximum graphs have matching-shaped defects

Let `H_n` be the graph obtained from the
four-cube graph `G_n` by deleting the
corresponding exceptional-edge set
`F_I,F_II,F_III` printed in
[FOUR_ODD_FACES_NEAR_BIPARTITE.md](FOUR_ODD_FACES_NEAR_BIPARTITE.md).
Its planar dual proof shows that H_n
is bipartite for every n in its phase.

**Theorem (disjoint monochromatic defect edges).**
For the phase maximum graphs n=560,579,665:

1. `F_I,F_II,F_III` have respectively
   **14, 10 and 16 edges**.
2. In each phase these exceptional edges
   are **pairwise vertex-disjoint**.
3. The remaining connected bipartite
   graph `H_max` has a bipartition
   `U union V`; both endpoints of
   every edge in F lie **in the same
   bipartition class**.
4. These properties are inherited by
   every smaller induced graph in the
   phase, and by deletion of either
   permitted fixed vertex.

**Proof.** Property 1 is already proved
by the two-odd-face-pair dual paths.
Property 2 follows directly from the
three printed edge lists: their
28, 20, and 32 endpoints, respectively,
are all distinct. For property 3,
the bipartite 2-coloring of H_max
is uniquely determined up to color
swap by the explicit four-color
reflection edges that remain.
Following those reflections from
vertex 1 shows that each listed
exceptional edge has endpoints
with the same inherited color.
This is an exact integer consequence
of the three fixed reflection
color rotations, reproduced by the
short pure-arithmetic verifier.
Property 4 follows by restricting
that bipartition, with no new
coloring choices needed. QED.

**Important:** No perfect matching is
asserted in this theorem. The edge
sets are known exactly, rather than
asserting there exists an uncomputed
bipartization.

## 2. Exact finite-defect Hall equivalence

The following proposition is valid for
**any** graph, without requiring planarity.

**Lemma (exceptional matching decomposition).**
Let `G=H union F`, where H is
bipartite with a prescribed bipartition
`U union V`, and F is a matching
whose every edge has both endpoints
inside U or both inside V.
Then G has a perfect matching
**if and only if** there exists a
subset `S subset F` satisfying:

1. With `a=|S∩E(U)|` and
   `b=|S∩E(V)|`,

   ```
   a-b=(|U|-|V|)/2.
   ```

2. After removing every endpoint
   of S from H, the bipartite graph
   `H_S=H - V(S)` satisfies Hall's
   condition, namely

   ```
   |N_{H_S}(X)| >= |X|
   for every X subset U \ V(S).
   ```

**Proof.** If M is a perfect
matching in G, put S=M∩F.
The remaining edges M\S belong to H
and give a bipartite perfect matching
of H_S. Removing S removes 2a
vertices from U and 2b from V,
giving the balancing equality.
Hall's inequalities are necessary.
Conversely, any S with the
balancing equation leaves equally
sized bipartition classes.
Hall's theorem supplies a
perfect matching of H_S, which
can be united with all edges
of S. Because F is a matching,
the union is a perfect matching
of G. QED.

Thus for A006063 one need only
consider **at most `2^16=65536`
subsets of a fixed matching F**.
No arbitrary odd cycles or Tutte
sets need be searched after a
particular S is selected. The
remaining condition is the ordinary
bipartite Hall theorem.

## 3. Phase-dependent parity-balance constraints

Use the color class determined
by the first vertex of the maximal
graph, retaining it as n decreases
and after deleting the sole fixed
vertex. Denote by `Delta(n)=|U|-|V|`
the corresponding signed difference.

The directly auditable **absolute
balance magnitudes** over each phase
are:

| phase | values of abs(Delta(n)) | edge classes in F, up to swapping U,V |
|---|---|---|
| I: 467..560 | 0,2,4 | 8 edges on one side, 6 on the other |
| II: 561..579 | 4,6,8 | 7 on one side, 3 on the other |
| III: 580..665, odd f=500 | 0,2,4 | 9 on one side, 7 on the other |

Thus the balancing equation
requires only **0–2** positive
side-correction edges in Phase I,
**2–4** in Phase II, and at most
**2** in Phase III, before allowing
additional canceling pairs
(one exceptional edge from each side).
These are lower bounds on how many
exceptional pairs a matching must
use, not existence results.

**Independent experimental information,
clearly not a theorem:** minimum-weight
complete matching runs for the three
phases found that every n has a
perfect matching using respectively
no more than **2, 4, and 5** edges
of its fixed F. In Phase I, the
experimental minimum always equals
`abs(Delta(n))/2`. Therefore a
promising sharper Phase I target is
to prove Hall after deleting at
most two well-chosen exceptional
same-side pairs, with no opposing-side
correction at all.

## 4. Exact expansion of the matching counting function

Let `m(Q)` denote the **number** of
perfect matchings of a finite graph Q,
with `m(empty)=1`. Every matching
M of G determines uniquely
`S=M∩F`. Conversely, each subset
S of the exceptional matching,
together with a perfect matching of
H_S, determines a perfect matching
of G. Therefore:

```
boxed: m(G)=sum_{S subset F} m(H-V(S)).
```

The terms with unequal remaining
bipartition sizes vanish automatically.
Since H is bipartite, any remaining
nonzero term is the **permanent of a
bipartite adjacency matrix**;
since H is also planar, it can
alternatively be evaluated via a
Kasteleyn-signed determinant.

This is a finite `2^16`-term
positive-integer identity, valid
for **every one of the 199 graphs**.
It eliminates the need for a
general-graph matching algorithm
from the *statement* of the
remaining existence condition:

```
m(G)>0 iff at least one balanced
bipartite Hall minor m(H-V(S))>0.
```

It does **not** yet provide the
missing uniform proof that at
least one of those minors is
positive for every n.

## 5. A bounded-rank Pfaffian interpretation

Take any skew-symmetric weighted
adjacency matrix K for G.
Splitting its edge contributions
between H and F gives

```
K = K_H + R,
```

where the perturbation R has
nonzero entries only at the
disjoint edges of F. Therefore

```
rank(R) <= 2*|F| <= 32.
```

The Pfaffian of K can be expanded
by selecting a subset of those
exceptional pairs, yielding
Pfaffians of skew bipartite
matrices on the remaining
vertices. Under a planar
Kasteleyn orientation, the
absolute Pfaffian is the number
of perfect matchings. Thus
the positive counting identity
above is also a **bounded-rank
planar Pfaffian reduction**.

This clarifies the next useful
mathematical target: find a
`S(n) subset F` satisfying the
balance equation, with a
**uniform Hall proof for the
bipartite graph H_n-V(S(n))**.
That would close the three
high-start phases without 199
general-graph matching runs.

The independent
[verify_defect_matching_reduction.py](verify_defect_matching_reduction.py)
checks all exceptional-edge
disjointness, class agreement,
and small balance magnitudes
by integer arithmetic alone.
