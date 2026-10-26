# A 15-block two-switch construction for six A006063 lengths

This is a fifth parameterized, calculation-free block-rearrangement family.
It replaces six separately checked endpoint identities for lengths

```
228, 229, 231, 238, 240, 241.
```

It is a direct application of the universal block-order lemma already proved
in [PARAMETRIC_BLOCK_TEMPLATES.md](PARAMETRIC_BLOCK_TEMPLATES.md): for input
blocks of lengths `ell_j` and output order `pi`, the reflected sum of
nonempty block `j` is `C_j=1+A_j+B_j+ell_j`. The result is a bijection
as soon as the output order lists every nonempty input block exactly once
and all its `C_j` are cubes.

## One mother template, three binary switches with a restriction

Choose binary variables `alpha,beta in {0,1}` subject to
**`alpha <= beta`** and put

```
t0 = 7 + 4*beta + 2*alpha,
t in {0,t0}.
```

Let the fifteen nonnegative input block lengths be

```
l1  = 2*beta
l2  = 7-alpha-4*beta-alpha*beta
l3  = alpha
l4  = alpha*beta
l5  = 13+4*beta
l6  = alpha
l7  = 23-4*beta-alpha
l8  = 13+4*beta
l9  = 48-alpha-45*beta+alpha*beta
l10 = 2*beta
l11 = beta*(39-alpha)
l12 = t
l13 = 30+alpha-t
l14 = 13+4*beta
l15 = 91+alpha-t.
```

Take output block order

```
pi = (10,4,6,2,8,3,11,1,9,14,7,12,15,5,13).
```

Zero-length blocks are deleted from both the input and output orders.
The total length is

```
n = 238 + alpha + 2*beta - t.
```

## Cubic sums: direct symbolic calculation

Substituting these lengths in `C_j=1+A_j+B_j+ell_j`
and using `alpha*beta=alpha` (because `alpha<=beta`),
the **nominal** block sums are exactly

```
(21+43*beta, 8, 28-alpha, 8, 216, 21+2*alpha+4*beta,
 125, 64, 125, 105-41*beta, 125, 209-2*alpha-4*beta+t,
 343, 216, 343).
```

Every **nonempty** block has a perfect-cube sum:
- The first, tenth, and eleventh blocks are nonempty only when
  `beta=1`, giving sums `64,64,125`.
- The third, fourth, and sixth blocks are nonempty only when
  `alpha=beta=1`, giving `27,8,27`.
- Blocks 2,5,7,8,9,13,14,15 have sums
  `8,216,125,64,125,343,216,343`.
- Block 12 is empty at `t=0`; at `t=t0`, its sum is
  `209-2*alpha-4*beta+t0=216`.

The restriction `alpha<=beta` is **necessary for this displayed
cubic-sum argument**. For `alpha=1,beta=0` one nonempty block would
have nominal sum `28`, which is not cubic. That invalid branch is
not silently counted as another construction.

The positivity of every required block follows immediately from the
three allowed pairs `(alpha,beta)=(0,0),(0,1),(1,1)`
and `t=0` or `t0`. No matching algorithm or case-dependent
endpoint multiset calculation is needed.

## Six consequences

| alpha | beta | t | n |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 238 |
| 0 | 0 | 7 | 231 |
| 0 | 1 | 0 | 240 |
| 0 | 1 | 11 | 229 |
| 1 | 1 | 0 | 241 |
| 1 | 1 | 13 | 228 |

These six formulas agree *term by term* with the previous explicit
endpoint identities, but the paper now obtains them simultaneously
from one algebraic family.

This reduces the primary independent numeric table from **66**
to **60 rows** (885 to **816** interval blocks).
The four earlier families already generated 16 seed lengths;
this fifth family adds six more, so **22 of the 82 finite seeds**
are now symbolic specializations.

See [finite_60_exceptional_atlas.txt](certificates/finite_60_exceptional_atlas.txt)
and [verify_60_plus_templates.py](verify_60_plus_templates.py)
for an optional independent integer audit. The global existence
theorem and strictly increasing cubic suffix-reflection closure
are unchanged. A case-free proof of the remaining 60 exceptions
is *not* claimed.
