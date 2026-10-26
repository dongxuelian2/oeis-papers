# A006063: three exact algebraic block templates replace eight finite rows

**Purpose.** The previous self-contained existence certificate needed 82
separate endpoint-multiset checks. This note gives **three symbolic
constructions**, proving eight of those base lengths without checking
eight individually generated endpoint lists. Hence the actual finite
certificate may be reduced to **74 exceptional integer identities** in
[certificates/finite_74_exceptional_atlas.txt](certificates/finite_74_exceptional_atlas.txt),
plus the three formulas below. The full 82-row
[atlas](certificates/finite_82_seed_atlas.txt) remains as an independent
comparison. This is a partial parameterization, **not** a uniform
case-free proof of every length.

## Universal reflected-block rearrangement lemma

Let `ell_1,...,ell_t` be positive integers with sum `n`.
Divide `[1,n]` into input blocks `I_j` of these lengths
in their original order. Choose an arbitrary permutation
`pi=(pi_1,...,pi_t)` of the block labels, and divide a second
copy of `[1,n]` into **output** blocks of lengths
`ell_(pi_1),...,ell_(pi_t)` in that order.
Let `A_j` be the sum of input-block lengths before `I_j`
and `B_j` the sum of output-block lengths appearing before
block `j` in the order `pi`. Put

```
C_j = 1 + A_j + B_j + ell_j.
```

The formula `p(i)=C_j-i` on `I_j` maps it **exactly**
onto its prescribed output block. In particular, whenever
**all `C_j` are integer cubes**, the result is a cube-sum
permutation on `[1,n]`. This is a symbolic rearrangement
lemma: disjointness and surjectivity are automatic from the
chosen output-block partition, not from a matching computation.

It also recovers the boundary-balance criterion in a constructive
form: the values `B_j+1` and `B_j+ell_j` give the image interval
directly.

## Family I: four reflected blocks

Take two integer cubes `U<V` and define

```
a = 2*U - V - 1,       b = 2*V - 3*U + 1.
```

Assume `a,b>0`. Choose input lengths `(a,b,a,b)`
and output order `(3,4,1,2)`. The universal lemma computes

```
(C_1,C_2,C_3,C_4) = (U,V,U,V),
n = 2*(V-U).
```

The following **three instances** are consequences of the
same two-variable symbolic identity, with no endpoint search:

| (U,V) | (a,b) | n |
|---|---|---|
| (64,125) | (2,59) | 122 |
| (125,216) | (33,58) | 182 |
| (216,343) | (88,39) | 254 |

This family works for any pair of positive cubes satisfying
the stated inequalities (not just the three listed instances).

## Family II: five reflected blocks

Take positive integer cubes `X<Y<Z` and put

```
a = 2*Y - Z - 1,
b = X + 2*Z - 4*Y + 1,
c = Y - X.
```

If `a,b,c>0`, use input lengths `(a,b,c,a,c)`
and output order `(4,2,5,1,3)`. Direct substitution yields

```
(C_1,C_2,C_3,C_4,C_5) = (Y,X,Z,Y,Z),
n = 2*Y - X - 1.
```

Two explicit instances with `Y=64,Z=125` are

| X | (a,b,c) | n |
|---|---|---|
| 27 | (2,22,37) | 100 |
| 8 | (2,3,56) | 119 |

In particular the formerly 14-segment row for 119 is
now a **five-block** instance of a general formula.

## Family III: six reflected blocks

Take positive integer cubes `X,W,Y,Z` (they need not be
pairwise distinct). Set

```
a = 2*Y-Z-1,
b = X-2*a-1,
c = W+2*a-2*X+1,
d = Y+X-W-2*a-1.
```

If `a,b,c,d>0`, use input lengths
`(a,b,c,d,a,d)` and output order
`(5,2,3,6,1,4)`. The required sums and total length are

```
(C_1,C_2,C_3,C_4,C_5,C_6) = (Y,X,W,Z,Y,Z),
n = 2*Z-2*Y+X-W.
```

The following three cases all use `Y=64,Z=125`:

| (X,W) | (a,b,c,d) | n |
|---|---|---|
| (8,64) | (2,3,53,3) | 66 |
| (27,64) | (2,22,15,22) | 85 |
| (8,27) | (2,3,16,40) | 103 |

The positive-block conditions are explicit integer inequalities.
No statement about the classification of all cube quadruples is
needed.

## Result for the finite A006063 existence proof

Combining the three families gives the following eight lengths
**without exceptional rows**:

```
66, 85, 100, 103, 119, 122, 182, 254.
```

The remaining 74 base lengths are covered by the
[74-row atlas](certificates/finite_74_exceptional_atlas.txt):
**969 reflected intervals** (versus 1,009 in the redundant
full 82-row atlas). For every exceptional row, the original
endpoint-balance lemma proves a legal permutation. For the
eight special lengths, the formulas in this note do so directly.
From these 82 established lengths and the empty permutation,
the growing cubic suffix lemma supplies 26 additional lengths
below 173 and 132 additional lengths in 173..364.
The elementary cubic-gap strong induction then proves
`P(n)>0` for every `n>=173`, exactly as before.

An independent [checker](verify_74_plus_templates.py) reads
**only** the 74 exceptional rows, regenerates the eight
special permutations from the symbolic formulas, and checks
all 192 target lengths. It does not consult the 82-row atlas,
matching data, or OEIS classification files. Nothing in the
mathematical proof depends on running it.

## Affine rigidity: why simple interpolation cannot replace all cases

For any legal piecewise-reflection permutation, if block `j`
has length `ell_j` and cube sum `C_j`, then summing
`i+p(i)` over all `i` gives the elementary identity

```
sum_j ell_j*C_j = n*(n+1).
```

**Rigidity lemma.** Fix `t` and fixed cube values
`C_1,...,C_t`. If every breakpoint `b_j(n)`
is an affine function of `n`, with `b_0(n)=0` and
`b_t(n)=n`, then the same resulting piecewise-reflection
word cannot give legal permutations at **three distinct**
values of `n`.

**Proof.** Each length `ell_j(n)=b_j(n)-b_(j-1)(n)`
is affine, hence the left-hand side of the displayed
identity is affine in `n`. The right-hand side
`n(n+1)` is a monic quadratic polynomial. Their
difference cannot vanish at three distinct integers.

This statement does **not** rule out varying the cubes,
non-affine breakpoints, piecewise templates, or composition
of constructions; indeed those are the appropriate routes
for further compression. It only excludes the tempting
strategy of interpolating long runs of finite rows using
one fixed cube word with affine endpoints.
