# A006063 — all 199 four-cube graphs are at most 16 edges from bipartite

**PROVED, including sharpness at the three maximal graphs:** Each of the three four-cube phases on
`467<=n<=665` admits one fixed, length-independent set
of at most **14, 10, or 16 exceptional cube-sum edges**,
whose removal makes every graph in that phase bipartite.
This is a mathematical consequence of the already
proved explicit planar rotations and four odd faces.
The actual edge sets and paired dual walks are printed
below; no full matching or permutation certificate is
used in the theorem.

**NOT PROVED:** This edge deletion theorem does not
establish that the original graphs admit perfect matchings.
Experiments indicate that only a handful of the exceptional
edges are needed in complete matchings, but that is a
separate finite observation.

## 1. The general four-odd-face lemma

Let G be a connected loopless planar graph with a fixed
orientable plane rotation. Suppose precisely four of its
faces have odd boundary-walk length. Name those faces
A,B,C,D.

**Lemma (two dual paths make the graph bipartite).**
Choose two vertex-disjoint paths in the plane dual,
one joining A to B and the other joining C to D.
Let F be the union of the corresponding primal
edges. Then `G-F` is bipartite.

**Proof.** Deleting a non-bridge primal edge merges
the two incident planar faces; the parity of the
new boundary walk is the sum modulo 2 of the former
parities, because both darts of the deleted edge
are removed. Deleting all edges along a
simple dual path merges its traversed faces,
and each intermediate face is even. The
two odd endpoint faces therefore merge to
one even face. The two dual paths have no
common face, so deleting the first path
does not disturb the face parity calculation
for the second. Every untouched face was
even; after both path deletions *all* faces
of the resulting planar graph have even
boundary-walk length. Every cycle is a
mod-2 sum of facial boundaries in a plane
embedding, so there is no odd cycle.
Therefore the resulting graph is
bipartite. QED.

A converse is also useful: if G-F is
bipartite, then every odd cycle of G must
use at least one edge of F. Thus the
explicit F is an **odd-cycle edge transversal**,
independent of any matching theorem.

## 2. Three exact maximum-length certificates

The [uniform planar rotation theorem](THREE_ROTATION_PLANARITY.md)
provides the phase-maximal connected plane graphs
with face counts and only four odd faces each.

### Phase I: n=560, sums {216,343,512,729}

The four odd faces have distinct minimum vertices
**39, 84, 60, 63**, of lengths 9,5,9,3.
Two vertex-disjoint dual paths connect
the faces with minimum vertices 39↔84
and 60↔63, respectively.

Their crossed primal edges, **in dual-path order**, are

```
P1:
(166,177), (98,118), (146,197), (67,149),
(101,115), (163,180), (84,132)                 [7 edges]

P2:
(60,156), (139,204), (91,125), (170,173),
(94,122), (142,201), (63,280)                  [7 edges]
```

Thus **14** specified edges suffice.

### Phase II: n=579, sums {216,512,729,1000}

The four odd faces have distinct minimum vertices
**29, 14, 12, 81**, of lengths 21,13,11,7.
Pair the faces with minima 29↔14 and 12↔81:

```
P1:
(29,187), (192,537), (207,522), (172,557),
(14,202)                                       [5 edges]

P2:
(66,150), (495,505), (61,155), (490,510),
(160,569)                                      [5 edges]
```

Thus **10** specified edges suffice.

### Phase III: n=665, sums {343,512,729,1000}

The four odd faces have distinct minimum vertices
**87, 63, 12, 36**, of lengths 9,3,9,5.
Pair the faces with minima 87↔36 and 63↔12:

```
P1:
(358,371), (189,540), (221,291), (336,393),
(224,505), (186,543), (355,374), (205,524)     [8 edges]

P2:
(280,449), (347,382), (213,516), (197,532),
(363,366), (194,535), (216,296), (181,331)     [8 edges]
```

Thus **16** specified edges suffice.

Each entry is an actual allowed cube-sum edge.
The two dual paths in each phase are disjoint
as sequences of faces, and the first/last
faces are exactly the four stated odd faces.
The remaining faces incident to the paths
have even lengths. These checks are elementary
applications of the *uniform color rotation*
from the planar theorem; no general
planarity algorithm is needed.

## 3. Sharpness: the exact minimum number of odd-cycle edges

The three displayed deletion sets are not just short:
they are **minimum-cardinality bipartizing
edge sets in their respective maximal graphs**.

**General theorem (odd-face metric matching formula).**
Let G be a connected plane graph with exactly
four odd facial boundary walks A,B,C,D. Give
every edge of the plane dual unit weight,
and write d(X,Y) for the shortest dual-path
distance between faces X and Y. Then the
minimum number of primal edges whose
deletion makes G bipartite is **exactly**

```
tau(G)=min(
 d(A,B)+d(C,D),
 d(A,C)+d(B,D),
 d(A,D)+d(B,C)).
```

**Proof.** Suppose F is any edge set
for which G-F is bipartite. Color the
vertices of G-F with two colors; this
colors all vertices of G as well.
Let F' consist of the *monochromatic*
edges of G. Then F' is a subset of F.

For any facial closed walk W, the
number of bichromatic edges traversed
by W is even: every such traversal
changes vertex color, and the closed
walk must return to its initial color.
Thus the number of monochromatic
edge occurrences is congruent to
the facial boundary length modulo 2.
In the plane dual, F' therefore has
odd degree at exactly the four odd
faces, and even degree elsewhere:
it is a dual **T-join** for
T={A,B,C,D}.

Every such T-join decomposes into
paths pairing its four odd-degree
terminals, with optional cycles.
The total path length is bounded
below by one of the three displayed
pairwise-distance sums. Consequently

```
|F| >= |F'| >= tau_metric.
```

Conversely, take shortest dual paths
for the pairing attaining the minimum.
Their symmetric difference is a
dual T-join of size at most the
sum of their lengths. Deleting
the corresponding primal edges makes
every resulting facial walk even,
by the preceding odd-face merging
argument, and hence makes G
bipartite. This proves equality. QED.

For the three explicit planar
rotations, the following are the
complete six-distance tables.
Face names are their **minimum
vertex labels**, which identify
the four odd faces uniquely.

**Phase I, n=560:** odd faces
A=39, B=84, C=60, D=63.

| dual face pair | distance |
|---|---:|
| 39–84 | 7 |
| 39–60 | 7 |
| 39–63 | 11 |
| 84–60 | 10 |
| 84–63 | 8 |
| 60–63 | 7 |

Three pairing lengths:
`7+7=14`, `7+8=15`, `11+10=21`.
Thus **tau(G_560)=14**.

**Phase II, n=579:** odd faces
A=29, B=14, C=12, D=81.

| dual face pair | distance |
|---|---:|
| 29–14 | 5 |
| 29–12 | 6 |
| 29–81 | 8 |
| 14–12 | 8 |
| 14–81 | 7 |
| 12–81 | 5 |

Three pairing lengths:
`5+5=10`, `6+7=13`, `8+8=16`.
Thus **tau(G_579)=10**.

**Phase III, n=665:** odd faces
A=87, B=63, C=12, D=36.

| dual face pair | distance |
|---|---:|
| 87–63 | 12 |
| 87–12 | 8 |
| 87–36 | 8 |
| 63–12 | 8 |
| 63–36 | 10 |
| 12–36 | 12 |

Three pairing lengths:
`12+12=24`, `8+10=18`,
`8+8=16`.
Thus **tau(G_665)=16**.

The dual distances are exact finite
integer statements in the three
**previously specified constant-color
rotation systems**. Their lower bounds
may be checked by breadth-first
layers in the tiny dual face graphs
(171, 79 and 229 faces);
the explicit two paths in Section 2
attain the minimizing pairings.
[verify_near_bipartite_phases.py](verify_near_bipartite_phases.py)
now audits all six distances per
graph without a matching or
planarity-finding library.

The equality tau=14/10/16 concerns
the three **maximal** graphs.
The same edge sets establish only
**upper bounds** for smaller induced
graphs; it is not claimed that
the bounds remain optimal at every
intermediate n.

## 4. Why the three certificates cover all 199 lengths

**Theorem (uniform 16-edge near-bipartiteness).**
For every integer `n in [467,665]`,
let C_n be the specified phase palette and
G_n the corresponding four-cube graph
on `[1,n]`, optionally with the prescribed
fixed point deleted. There exists a
phase-dependent but **n-independent** set
F of at most 16 allowed edges such that

```
G_n - (F intersect E(G_n))
```

is bipartite.

**Proof.** Apply the lemma to the three
maximum-length graphs using their displayed
two dual paths. For any smaller n in the
same phase, G_n is the induced subgraph
of the relevant maximum graph on
`[1,n]`. Deleting an additional fixed
vertex is another induced-subgraph operation.
Every subgraph of a bipartite graph is
bipartite. QED.

One also obtains **at most four odd faces**
for the inherited planar rotations of all
shorter graphs: removing a primal edge
merges two faces, changing their total
number of odd boundary faces from 0 or 2
to 0, or from 1 to 1. Thus edge deletion
never increases the number of odd faces.
Vertex deletion amounts to repeated
edge deletion followed by removing an
isolated vertex, which does not create
odd faces. The starting maximum graphs
have exactly four odd faces.

## 5. What remains for positive matching existence

For any graph H with `H-F` bipartite,
let U,V be a bipartition of H-F.
Every perfect matching of H uses at
least

```
abs(|U|-|V|)/2
```

edges whose endpoints lie in the same
bipartition class, hence at least that
many edges from F. This is a purely
combinatorial **balance obstruction**,
not an existence theorem.

For the three phase-maximal bipartizations,
the two classes are globally determined:
the graphs remain connected after
the exceptional edges are removed.
The experimentally computed balance
defects across each phase are small:

| phase | possible abs(|U|-|V|) in fixed-point graphs | lower bound on exceptional pairs |
|---|---|---|
| I | 0,2,4 | 0,1,2 |
| II | 4,6,8 | 2,3,4 |
| III (odd fix 500) | 0,2,4 | 0,1,2 |

**EXPERIMENTAL, NOT A PROOF:** Minimum-exception
full matching searches found perfect matchings
using at most **2**, **4**, and **5**
edges of the respective sets F across all
94,19,86 lengths. Their maximum counts
are much smaller than the total number
of deleted edges (14,10,16).
A future proof could combine a *bipartite*
Hall theorem for H-F with a bounded
selection of these 40 explicit
exceptional edge candidates. This may
be a more tractable route than a general
planar Tutte analysis.

The proof of the edge-bipartization theorem
itself depends only on four odd faces,
two explicit dual paths, and
induced-subgraph inheritance. The new
standard-library
[verify_near_bipartite_phases.py](verify_near_bipartite_phases.py)
reconstructs every step without matching
or optimization libraries.
