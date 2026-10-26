# A three-endpoint planar embedding theorem for all 199 four-cube graphs

**Status: PROVED from three explicit combinatorial rotation certificates.**
No general-graph matching algorithm is used or assumed.

For each allowed four-cube palette `C` and n, define
the **unpunctured loopless graph** `G(n,C)`
on vertices `1,...,n`, joining distinct
vertices u and v precisely when `u+v in C`.
Deleting the single fixed vertex f (when
n is odd) yields the graph whose perfect
matching is sought for a cube-sum involution.

## 1. Uniform planarity across all three phases

**Theorem (three-endpoint planarity).** For each n in
the indicated range, the following four-color graph
is planar, even *before* removing any fixed vertex.

| Phase | n | four cube sums C | cyclic edge-color order |
|---|---|---|---|
| I | 467..560 | 216,343,512,729 | (216,343,512,729) |
| II | 561..579 | 216,512,729,1000 | (216,512,729,1000) |
| III | 580..665 | 343,512,729,1000 | **(343,729,512,1000)** |

At every vertex, the proposed clockwise
rotation is obtained by taking the
displayed cyclic color order and simply
discarding missing edges and self-loops.
It is **the same rule at every vertex**,
with no special vertices or n-dependent
adjustment.

The cyclic order in Phase III is
deliberately NOT increasing numeric order:
the colors 729 and 512 are swapped.

## 2. Three explicit Euler/rotation certificates

An **oriented dart** is a directed edge
`(u,v)`. For a chosen cyclic ordering
of neighbors around each v, let

```
Phi(u,v) = (v, successor_of_u_around_v).
```

This is a permutation of the `2E`
darts. Its cycles are precisely the
oriented boundary walks of the faces
of the associated orientable ribbon-graph
embedding. This is a purely finite
combinatorial definition of the faces,
not a planarity-finding algorithm.

**Exact certificate at each phase's
maximum length:**

| Phase | maximum n=V | E | F=cycles(Phi) | V-E+F |
|---|---:|---:|---:|---:|
| I | 560 | 729 | 171 | **2** |
| II | 579 | 656 | 79 | **2** |
| III | 665 | 892 | 229 | **2** |

For additional auditability, the complete
face-size multiplicities are:

```
Phase I (n=560):
  length 3:1, 5:1, 6:62, 9:2, 10:104, 20:1.
  Face count 171; total dart length 1458=2*729.

Phase II (n=579):
  length 7:1, 11:1, 12:11, 13:1,
  14:35, 21:1, 22:29.
  Face count 79; total dart length 1312=2*656.

Phase III (n=665):
  length 3:1, 5:1, 6:119, 8:8, 9:2, 10:98.
  Face count 229; total dart length 1784=2*892.
```

All three endpoint graphs are **connected**:
starting from 1 and repeatedly adjoining the
four allowed reflections `c-v` within
`[1,n]` reaches every vertex. This
property can be checked from the four
integer reflection intervals; an exact
integer traversal is also included in
the independent verifier.

**Proof of the theorem.** Specify the
clockwise edge-color orders in the table.
They define a connected orientable
combinatorial embedding at each
maximum length. The exact dart-cycle
counts above yield `V-E+F=2`, so
the underlying closed orientable
surface has genus `(2-(V-E+F))/2=0`.
Therefore these are **planar embeddings**.

For any smaller n in the same phase,
the graph `G(n,C)` is exactly the induced
subgraph of `G(n_max,C)` on vertices
`1,...,n`, since the palette C does
not vary within the phase. A subgraph
of a planar graph is planar. Deleting
the permitted fixed point (108 in
Phases I/II, 256 or 500 in Phase III)
preserves planarity. Thus every graph
in the full 199-length research window
is planar. QED.

**Logical status of the three face
count tables.** They are finite
exact integer certificate equalities
for three explicit graph rotations,
not a parameter-free closed formula
for face counts in arbitrary four-cube
graphs. The proof no longer relies
on 199 separate computational
planarity observations; it requires
only these three small, independently
checkable combinatorial embeddings.

## 3. The face count reduces to just 26 color-word templates

For an even more explicit arithmetic account of
the three Euler face counts, encode each palette's
four cube sums in **increasing numeric order**
as `A,B,C,D`. In Phase III, note that
the *rotation* is still `A,C,B,D`;
the letters below refer to cube values,
not to clockwise rank.

For any oriented face, read the cube-color
word encountered along its directed boundary
and choose the **lexicographically least
cyclic rotation** of that word. The face
also has a well-defined minimum vertex.
The resulting complete list of face
types uses only **8, 9 and 9 templates**:

**Phase I, n=560 (A=216, B=343, C=512, D=729)**

| cyclic face word | allowed minimum vertex | faces |
|---|---|---:|
| ABCDCABCDC | [1,38] ∪ [40,59] ∪ [61,83] | 81 |
| BCDBCD | [1,62] | 62 |
| ABCDDABCDD | [1,23] | 23 |
| ABCDDBCDCABCDDBCDCDD | {47} | 1 |
| ABCDCABDC | {39} | 1 |
| ABCDC | {84} | 1 |
| ABCDCBCDC | {60} | 1 |
| BCD | {63} | 1 |

The total is `81+62+23+5=171` faces.

**Phase II, n=579 (A=216, B=512, C=729, D=1000)**

| cyclic face word | allowed minimum vertex | faces |
|---|---|---:|
| ABCBABCBCDBABCBABCBCDB | [13,28] ∪ [30,41] | 28 |
| ABCBCDCABCBCDC | [1,13] ∪ [15,26] | 25 |
| ABCBCDBABCDC | [1,11] | 11 |
| ABCBCDBABCBCDB | [71,80] | 10 |
| ABCBABCBCDBABCBBCBCDB | {29} | 1 |
| ABCBCDCABCCDC | {14} | 1 |
| ABCBCDCBCDCABCBCDCBCDC | {53} | 1 |
| ABCBCBABCDC | {12} | 1 |
| ABCBCDB | {81} | 1 |

The total is `28+25+11+10+5=79` faces.

**Phase III, n=665 (A=343, B=512, C=729, D=1000)**

| cyclic face word | allowed minimum vertex | faces |
|---|---|---:|
| ACDCBACDCB | [72,86] ∪ [88,144] | 72 |
| ACBACB | [1,62] | 62 |
| BDCBDC | [64,120] | 57 |
| ABDCBABDCB | [9,11] ∪ [13,35] | 26 |
| ABDCBACD | [1,8] | 8 |
| ACDCACDCB | {87} | 1 |
| ACB | {63} | 1 |
| ABCBABDCB | {12} | 1 |
| ABDCB | {36} | 1 |

The total is `72+62+57+26+8+4=229` faces.

The validity of each template is checked
by the explicit reflection rule
`v -> c-v` and the uniform successor
rotation at the next vertex. The
permitted minimum-vertex sets are
unions of **short integer intervals**,
rather than arbitrary lists of hundreds
of faces. In each case, the intervals
count every cyclic face word exactly
once and the total word lengths equal
`2E`. This yields a compact 26-family
**finite arithmetic proof certificate**
of the three planar endpoint embeddings.

A second independent, standard-library
[26-template checker](verify_planar_face_word_templates.py)
compares all cyclic words and their
minimum-vertex intervals, not just
aggregate Euler face counts. This still relies
on finitely stated arithmetic
identities; it does not imply the
unproved positive matching theorem.

## 4. What the theorem contributes—and what it does not

The full four-color perfect-matching
problem is now restricted to a family
of **connected planar graphs with
maximum degree four**. Combined with
[DUAL_REFLECTION_PATHS.md](DUAL_REFLECTION_PATHS.md),
the same graphs are unions of two
transverse path systems, each with
components containing at most four
vertices.

This opens more structured routes to
the missing uniform matching theorem:

1. A **planar Tutte criterion**:
   control the odd faces/odd components
   of deletions by exploiting the explicit
   four-color rotation rather than
   treating the graphs as arbitrary.
2. A **Kasteleyn–Pfaffian certificate**:
   a suitable planar orientation expresses
   the number of perfect matchings as
   an absolute Pfaffian. Proving its
   nonvanishing uniformly would establish
   the conjectured involutions.
3. A **two-path-state transfer theorem**
   using the finite 2/3/4-vertex
   path-local masks and the planar
   arrangement of their incidences.

**Important:** A connected planar graph
with minimum degree at least 2 need not
have a perfect matching. Planarity by
itself does **NOT** upgrade the 199/199
four-color matching experiments into
a computation-free positive existence
theorem.

The independent
[verify_three_rotation_planarity.py](verify_three_rotation_planarity.py)
uses only integer graph arithmetic,
a trivial connectedness traversal,
and permutation cycles of the
explicit dart rotation to reproduce
the three finite Euler certificates.
It does **not** call a matching
solver or a planarity-finding library.
