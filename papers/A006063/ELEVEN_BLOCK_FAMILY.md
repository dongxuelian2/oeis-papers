# A cubic five-parameter family with an optional zero-length block

This note supplies a **fourth symbolic seed family** for A006063.
It covers **131, 150, 156, and 175 simultaneously** and reduces
the number of unrelated integer endpoint identities from 74 to **70**.
It uses no bipartite matching, generic integer programming, or old
permutation archive in its proof.

## General block-rearrangement mechanism

Let positive input block lengths be `ell_1,...,ell_t`, and let
`pi` specify their order among the output blocks. If `A_j` and
`B_j` are their respective input/output prefix lengths, then

```
p(i) = (1+A_j+B_j+ell_j)-i
```

on input block `j` maps it exactly onto its output block. Thus,
if each nonempty block sum `C_j=1+A_j+B_j+ell_j` is a cube,
the resulting map is a cube-sum permutation. A block of length zero
is simply omitted from **both** orders; its nominal sum `C_j`
need not be cubic.

## The 11-block symbolic family

Let `X,Y,Z,W,Q` be integers, with `X,Y,Z,W` positive cubes.
Define the six *integer* lengths

```
a = 4*Z - 2*W - Y - 1
b = 4*W + X + 2*Y - 8*Z + 1
c = 2*Z - W - X
d = Q + 4*W + 2*X - 8*Z + 1
e = 3*Z - W - X - Q
f = 3*W + 2*Y - 6*Z + 1.
```

Assume **a,b,c,e,f > 0 and d >= 0**. If `d>0`, additionally
require `Q` to be a positive cube. If `d=0`, the nominal
sixth block is *empty*; then `Q` is unconstrained.

In input order, use the eleven block lengths

```
(a,b,c,a,c,d,e,a,f,a,e).
```

Send these blocks to their output positions in the order

```
(10,2,5,8,3,6,11,4,9,1,7).
```

Using the rearrangement lemma, the eleven nominal block sums,
computed algebraically, are

```
(Z,X,Y,Z,Y,Q,W,Z,W,Z,W).
```

Hence every **nonempty** block has a cubic index-image sum.
The total number of elements is

```
n = 4*Z - W - X - Q - 1.
```

When `d=0`, delete label 6 from both orders, retaining the
remaining ten blocks. Solving `d=0` gives
`Q=8*Z-4*W-2*X-1`, which need not be a cube, and now

```
n = 3*W + X - 4*Z.
```

These formulas are **symbolic identities for arbitrary admissible
integer cubes**, not just rewritten certificates for the four
specific target lengths.

## Four applications from the same general family

Fix `(Y,Z,W)=(64,125,216)` and take `X=8` or `27`.

| X | Q | d | resulting n | input blocks |
|---:|---:|---:|---:|---|
| 8 | 125 | 6 | 150 | 3,1,26,3,26,6,26,3,27,3,26 |
| 27 | 125 | 44 | 131 | 3,20,7,3,7,44,7,3,27,3,7 |
| 8 | 119 | 0 | 156 | 3,1,26,3,26,0,32,3,27,3,32 |
| 27 | 81 | 0 | 175 | 3,20,7,3,7,0,51,3,27,3,51 |

In the final two rows, `Q=119` and `Q=81` are **not cubes**
but their blocks have zero length, so no index receives either
noncube sum. This is essential: demanding cubic sums at empty
blocks would incorrectly exclude the degenerate constructions.

For all four rows, the output order is the same eleven-label
permutation with label 6 omitted when empty. Direct substitution
checks all the required sums. The integer block lengths are
positive except for the deliberately empty sixth block.

## Result and logical boundary

The [70-row exceptional atlas](certificates/finite_70_exceptional_atlas.txt)
contains **927** reflected integer blocks. Together with the first
three block families (8 seed lengths) and this one (4 more), it
constructs the same 82 independent seed lengths as the older
82-row table. The **12 parametrically proved seed lengths** are

```
66, 85, 100, 103, 119, 122, 131, 150, 156, 175, 182, 254.
```

The remaining 26 lower and 132 middle lengths follow by strictly
increasing cubic suffix reflections. The symbolic cubic-gap lemma
extends the result to all `n>=173`.

The script `verify_70_plus_templates.py` is only a reproducibility
audit. The proof above requires no runtime computation. This does
**not** claim a case-free proof of the remaining 70 exceptions,
or optimality of the template collection.
