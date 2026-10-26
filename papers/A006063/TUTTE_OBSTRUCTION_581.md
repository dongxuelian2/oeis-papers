# Hybrid five-cube Tutte obstruction at n=581

**PROVED: if a cube-sum involution at n=581 fixes
108 and uses the palette
`{216,343,512,729,1000}`, then it must use
cube 216 on at least one nontrivial 2-cycle.**
Merely using 216 at the fixed point and
restricting every 2-cycle to
`{343,512,729,1000}` is impossible.

**Important correction:** The four-cube
palette `{343,512,729,1000}` does not
contain 216, so an involution using only
these four cubes cannot fix 108 **at any
odd length**, not merely 581. Valid
single fixed points for this palette
are 256 or 500. The obstruction below
is therefore about a *hybrid five-cube
normalization* rather than a valid
four-cube fixed-108 case.

The statement is a genuine Tutte
graph-theoretic certificate, proved
by elementary integer reflection
arithmetic and the 1-factor theorem,
not a failed matching-solver call.

## 1. The graph and its 31-interval obstruction set

Remove vertex 108 from `[1,581]`. On the remaining
580 vertices, define an **undirected, loopless** graph G
by placing an edge between distinct x,y exactly when

```
x+y in {343,512,729,1000}.
```

Let S be the union of these **31 closed integer intervals**:

```
[148,151], {156}, [161,162], [165,167], {170},
[174,175], [179,180], [184,186], [203,204],
[209,210], [215,217], [263,271], [276,277],
[281,282], [286,287], [298,301], [305,306],
[311,320], [324,325], [329,330], [334,336],
[432,441], [445,446], [450,451], [455,457],
[467,470], [474,475], [480,489], [493,494],
[498,499], [503,505].
```

The intervals are disjoint, none contains 108, and
their lengths sum to exactly

```
|S| = 103.
```

## 2. All remaining connected components are odd

Direct interval/reflection arithmetic for the four maps
`x -> 343-x, 512-x, 729-x, 1000-x`, restricted to

```
T = [1,581] \ ({108} union S),
```

gives the following **complete component-size table**:

| component size | number of components | covered vertices |
|---:|---:|---:|
| 1 | 60 | 60 |
| 3 | 18 | 54 |
| 5 | 13 | 65 |
| 7 | 2 | 14 |
| 11 | 7 | 77 |
| 17 | 3 | 51 |
| 63 | 1 | 63 |
| 93 | 1 | 93 |
| **Total** | **105** | **477** |

The total number of surviving vertices is indeed
`581-1-103=477`. All eight possible component
sizes shown are **odd**.

For a self-contained integer check of this table,
take any vertex `v in T` and repeatedly include
`c-v in T` for each of the four cubes c. Repeat
to closure. That constructs **exactly the
connected component** of v; remove it and
continue with the smallest remaining vertex.
This algorithm is only the definition of
connected components, not a matching solver.
An independent short [standard-library verifier](verify_tutte_581.py)
reproduces all sizes from the 31 displayed
intervals, without NetworkX, SciPy, optimization
or any archived cube-sum permutations.

## 3. Tutte's theorem rules out the hybrid restricted involution

Tutte's 1-factor theorem states that a finite
loopless undirected graph H has a perfect
matching if and only if **for every**
`S subset V(H)`, the number `o(H-S)`
of odd-order components is at most `|S|`.

For our explicit S,

```
o(G-S) = 105 > 103 = |S|.
```

Consequently G **has no perfect matching**.

A cube-sum involution on `[1,581]` with
sole fixed point 108 **and no other cube-216
edges** would restrict to a perfect matching
on G: its 2-cycles are edges of G and cover
all other vertices. This contradicts Tutte.
Thus any five-cube involution with fixed
point 108 must use at least one additional
nontrivial 2-cycle whose index sum is 216. QED.

The obstruction is *not* a bipartite Hall
obstruction for ordinary permutations:
the corresponding directed cube-sum
adjacency matrix can still support a
complete cycle cover, which may include
cycles longer than two. It also does
not rule out an involution with fixed point
256 or 500, since deleting a different
fixed vertex produces a different graph.

## 4. Consequences and limitations

The [three four-cube phases](FOUR_CUBE_PHASES.md)
must use a valid fixed-point rule. In
Phase III, every odd n uses fixed point
256 or 500 (because 216 is not among
its four cube sums); this has been
independently rechecked for all odd
581<=n<=665.

The present proof says something
**stronger than the trivial invalidity
of fixed point 108 in Phase III**:
even if the fifth cube 216 is permitted
at the self-loop 108, one must also use
at least one separate 216-reflection
pair to obtain a five-cube involution
at n=581. The 103-vs-105 component
certificate explains a real combinatorial
deficit in the remaining four-color
graph. The amount of additional
216-colored matching used is a separate
question.

This negative result neither constructs
nor excludes four-cube involutions with
fixed point 256 or 500, nor does it
establish a phase-wide positive matching
theorem.
