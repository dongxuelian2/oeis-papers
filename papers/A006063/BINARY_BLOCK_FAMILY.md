# Eight seed lengths from one 12-block formula and three binary switches

This algebraic construction replaces the separate 11-block specialization
in [ELEVEN_BLOCK_FAMILY.md](ELEVEN_BLOCK_FAMILY.md) as the **stronger
fourth symbolic family** in the A006063 existence proof. It produces
eight previously tabulated seed lengths, rather than four.

The mathematical proof is independent of any computational search
or the older integer atlases. It is an explicit application of the
reflected-block rearrangement lemma.

## A universal 12-block parametric formula

Choose **integers** `X,T,Q` and define

```
u = X-7
v = T-2*X+7
w = X+27-T
z = Q+2*T-2*X-121
h = X+152-T-Q
```

Use input block lengths

```
(3,u,v,w,3,w,z,h,3,27,3,h)
```

and output block order

```
(11,2,3,6,9,4,7,12,5,10,1,8).
```

Assume `u,v,z >= 0` and `w,h>0`.
All other block lengths are manifestly positive.
The rearrangement identity `C_j=1+A_j+B_j+ell_j` gives
the **twelve nominal block sums**

```
(125,X,T,64,125,64,Q,216,125,216,125,216).
```

Consequently, a legal cube-sum permutation is obtained whenever:

- `u>0` implies `X` is a positive cube;
- `v>0` implies `T` is a positive cube;
- `z>0` implies `Q` is a positive cube.

If any of `u,v,z` is zero, its block is omitted from both
the input and output partitions, so its nominal sum is **irrelevant**
and need not be cubic. The total length is

```
n = 276+X-T-Q.
```

This is a genuine **three-parameter family**, not a finite list of
separately checked permutations. No nontrivial computer algebra is
needed to verify its sums: substitute the five displayed block
length expressions into the prefix-sum formula.

## Three independent binary choices

Take `X` from `{7,8}`. Its first optional block has length
`u=0` or `1`; when positive, `X=8=2**3`.

Choose either `T=2*X-7` (so `v=0`) or `T=27=3**3`
(so `v>0`).

Choose either `Q=121-2*T+2*X` (so `z=0`) or
`Q=125=5**3` (so `z>0`).

For all eight combinations, `w,h>0` and all required
cube conditions hold. The values `X=7`, `T=7,9`
or `Q=81,83,119,121` occur **only in omitted blocks**;
their noncubic status causes no problem.

| X | T | Q | (u,v,z) | resulting n |
|---:|---:|---:|---|---:|
| 7 | 27 | 125 | (0,20,44) | 131 |
| 8 | 27 | 125 | (1,18,42) | 132 |
| 8 | 9 | 125 | (1,0,6) | 150 |
| 7 | 7 | 125 | (0,0,4) | 151 |
| 7 | 7 | 121 | (0,0,0) | 155 |
| 8 | 9 | 119 | (1,0,0) | 156 |
| 8 | 27 | 83 | (1,18,0) | 174 |
| 7 | 27 | 81 | (0,20,0) | 175 |

The simultaneous zero-block deletions recover the shorter
10- or 11-block patterns, including all four special cases
in the previous 11-block note. The formula still works
algebraically for other admissible integer parameters.

## Effect on the existence proof

The previous four-, five-, and six-block algebraic families
give eight base lengths `66,85,100,103,119,122,182,254`.
This twelve-block family gives eight further base lengths
`131,132,150,151,155,156,174,175`.

Thus there are **16 parametrically obtained base lengths**
and just **66 unrelated endpoint-multiset identities**
([atlas](certificates/finite_66_exceptional_atlas.txt),
containing **885 reflected blocks**).
They still give the same 82 independently established seed
lengths (22 below 173 and 60 in 173..364), and the existing
reflection closure and cubic-gap argument prove all `n>=173`.

The older 70/74/82/109-row atlases remain independent,
redundant cross-checks. No claim of a case-free proof of
the **66 remaining exceptions** or optimality is made.
