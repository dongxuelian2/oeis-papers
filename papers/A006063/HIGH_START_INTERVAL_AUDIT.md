# Is A006063's avalanche starting too low? High-start interval analysis

**Status: theorem-level launch mathematics + a clearly labeled finite matching experiment.**
This note investigates whether replacing the difficult finite base
`[173,364]` by a larger, more regular interval leads to a better
*eventual* existence theorem. It does **not** claim an unconditional
case-free proof of the proposed higher base.

## 1. Exact optimal two-cube launch windows (PROVED)

Let `G(n)` mean existence of a cube-sum permutation of `[1,n]`.
The proved interval avalanche says that if `G(n)` holds for every
`n in [a,b]`, then a cube `c` with

```
a+b+2 <= c <= 2*b+2
```

extends existence through `c-a-1`.

**Launch-window theorem.** Fix `k>=6` and plan to propagate first by
`c=k^3` and then by `d=(k+1)^3` without proving any new
lengths between the two reflections. The smallest feasible upper
endpoint is

```
b_k = floor((k^3-1)/2).
```

The largest lower endpoint which guarantees that the first
reflection reaches the threshold for the next cube is

```
a_k = k^3 - 1 - floor(((k+1)^3-1)/2).
```

For the interval `[a_k,b_k]`, both launch conditions hold.
The minimum contiguous base width under this two-stage strategy is

```
w_k = b_k - a_k + 1
    = ((k+1)^3-k^3+1)/2
    = (3*k^2+3*k+2)/2.
```

**Proof.** For the first cube to touch `b+1`,
`k^3<=2b+2` implies `b>=b_k`.
It produces the new upper endpoint `k^3-a-1`.
For the next cube to touch the extended interval,
we must have
`k^3-a-1>=floor(((k+1)^3-1)/2)`,
equivalently `a<=a_k`.
Both constraints are attained simultaneously.
Also `k^3>=a_k+b_k+2` because consecutive
cubes have a positive integer gap.
Thus this interval launches the first two cube reflections.
For subsequent cubes the condition
`(j+1)^3<=2*j^3-2*a_k` only becomes easier:
the right-minus-left quantity
`2*j^3-(j+1)^3` increases for `j>=2`,
since its first difference is
`3*j^2-3*j-5>0`. QED.

Numerical examples (endpoints are exact integers):

| first cube | smallest self-propagating base | base width |
|---|---|---:|
| 9^3=729 | [229,364] | 136 |
| 10^3=1000 | [334,499] | 166 |
| 11^3=1331 | [467,665] | 199 |
| 12^3=1728 | [629,863] | 235 |
| 13^3=2197 | [825,1098] | 274 |
| 16^3=4096 | [1639,2047] | 409 |

**Tradeoff:** The width `w_k` grows approximately as
`1.5*k^2`. Raising the start therefore does *not*
automatically reduce the absolute finite proof size,
but it can improve the graph's combinatorial structure.

## 2. Why [229,364] is not an obvious simplification (PROVED)

The base `[229,364]` is shorter than `[173,364]`,
but if no previously proved lengths below 229 are allowed
(except the empty length 0), strictly increasing cubic
suffix reflection derives only **28** of these 136
lengths from smaller lengths *within the new band*.
The other **108** lengths have no available predecessor
under that restricted rule and need independent construction.

More precisely the 108 ungenerated lengths comprise
the integer ranges `[229,255]`, `[283,341]`,
and `[343,364]`. The missing length 342 itself is
trivially generated from the empty permutation using cube 343.
Thus the 29% width reduction does not remove the need
for many local constructions. Moreover it cannot
establish the skipped lengths `173..228`, which
remain necessary for the full original statement.

## 3. A genuinely more regular band: [467,665]

We found a stronger, rigorously provable structural
feature of `[467,665]`. Let the five permitted cube
sums be

```
C = {216,343,512,729,1000} = {6^3,7^3,8^3,9^3,10^3}.
```

For every `n in [467,665]`, let `H_n`
be the *undirected* cube-sum graph on
`[1,n]`, with `i--j` when `i+j in C`
(loops allowed at even half-cubes).

**Twofold-reflection coverage lemma (PROVED).** Every
vertex of `H_n` has at least **two distinct**
permitted cube-sum neighbors, for all
`467<=n<=665`.

**Proof.** At `n=467`, the reflection
domains of the first four cubes are

```
I_216=[1,215],
I_343=[1,342],
I_512=[45,467],
I_729=[262,467].
```

Each index in `[1,467]` lies in at least two
of these four intervals, by inspecting the
breakpoints `1,45,216,262,343,468`.
Every fixed cube's reflection domain only
expands as n increases. For `467<n<=511`,
each new index `468<=i<=n` has two
distinct valid partners `512-i` and
`729-i`. From `n=512` onward, every
new index `512<=i<=n<=665` has partners
`729-i in [64,217]` and
`1000-i in [335,488]`, both inside
`[1,n]`. Thus no vertex of any
`H_n` in this window is a forced leaf. QED.

This degree condition is *not by itself a
perfect matching theorem* (a graph can have
minimum degree 2 and still fail Tutte/Hall).

## 4. A striking finite observation: 199 five-cube involutions

**COMPUTATIONALLY OBSERVED, NOT YET PROVED WITHOUT CASEWORK.**
An independent maximum-cardinality general-graph matching
search (Edmonds blossom, with NetworkX) produced:

- For every **even** `n in [467,665]` (99 values),
  a fixed-point-free involution `p`, using
  **only** cube sums in `C`.
- For every **odd** `n in [467,665]` (100 values),
  an involution using only `C` and satisfying
  **`p(108)=108`**, since `108+108=216`.
- Thus all 199 lengths passed, using the **same five cubes**.
  The optional reproducibility script is
  [verify_high_start_five_cubes.py](verify_high_start_five_cubes.py).

These finite matching results are useful **experimental
evidence only**. They are not a proof that one general
Tutte inequality holds throughout the interval.

For n=360 and n=362 in the smaller comparison
window [334,499], matching with the five sums
`{64,216,343,512,729}` fails if one
*requires no fixed points*. However both
admit involutions if two fixed points are
allowed. Earlier claims that no involution
existed at those lengths were an error.

### The five colors are collectively irredundant (PROVED by Hall)

The five-cube palette is not merely an artifact of a solver
search. **Deleting any one of these five cubes makes at
least one length in [467,665] impossible**, even if one
allows arbitrary (non-involutive) cube-sum permutations.

For each omitted cube in the first column, at the given
length n, the listed set S of input rows has as its
**entire** set of remaining possible image columns N(S)
the set on the right:

| omitted cube | n | S | N(S) |
|---|---:|---|---|
| 216 | 467 | 5,30,78,126,174,247,295,343,416,464 | 48,96,169,217,265,313,338,386,434 |
| 343 | 467 | 1,80,159,238,297,376,455 | 57,136,215,274,353,432 |
| 512 | 475 | 89,216,475 | 127,254 |
| 729 | 470 | 5,174,301,343,470 | 42,169,211,338 |
| 1000 | 652 | 1,218,387,435,514,604,652 | 77,125,215,294,342,511 |

Each equality is checked directly by evaluating
`(C\\{omitted cube}-S) intersect [1,n]`.
In all five cases, **|N(S)|=|S|-1**, contradicting
Hall's necessary condition. No computational matching
solver is required to validate these five certificates.

This establishes *irredundancy within the displayed
five-cube palette for the entire proposed band*.
It does **not** prove that no *different* choice of
four cubes, perhaps including smaller cubes such
as 125 or 64, could work uniformly; such a global
four-cube exclusion would require separate analysis.

### Proposed single mathematical target

Remove the vertex 108 when n is odd, and call
the resulting *loopless* graph `F_n`.
A proof of the following **Tutte condition**, with
no 199-row matching atlas, would be sufficient:

```
For each 467<=n<=665 and each S subset V(F_n),
the number of odd components of F_n-S is <= |S|.
```

By Tutte's 1-factor theorem this implies a
perfect matching of `F_n`. Pair matched
vertices via their corresponding cubic sums;
for odd n, add the fixed point 108.
This establishes a cube-sum involution on
every n in the window by **one structural
matching principle**, not 199 numerical
matching runs.

**Conditional stronger conclusion.** Cubic
suffix reflection preserves involutions,
so the already proved interval avalanche
would then give cube-sum involutions
for **every n>=467**:

```
[467,665] --1331--> [467,863]
          --1728--> [467,1260] --2197--> ...
```

The first step follows because
`467+665+2=1134<=1331<=1332=2*665+2`.
The rest is guaranteed by the same
symbolic monotone cube-gap inequality
as in Section 1.

## 5. A sharp obstruction to fixed-word interpolation (PROVED)

A tempting shortcut is to fix one ordered list of cubic sums
`(k_1^3,...,k_t^3)` and one output block order `pi`,
then vary the input-block lengths continuously over all
199 target integers. **This is algebraically impossible,
even if the block-order matrix is singular.**

**Fixed-word length rigidity theorem.** For a fixed cubic
sum word and a fixed output-block order, *all* positive
solutions to the block-rearrangement equations have exactly
the **same total length N**.

**Proof.** Write the block-order matrix as
`M = u*u^T + K`, where `u` is the all-ones vector
and `K` is skew-symmetric. This follows from the
universal identity `M+M^T=2*u*u^T`. If two
positive integer block vectors `ell,ell'` solve
`M*ell=M*ell'=k^3-u`, their difference
`v=ell-ell'` satisfies `M*v=0`. Therefore

```
0 = v^T*M*v = (u^T*v)^2 + v^T*K*v
  = (sum_j v_j)^2.
```

Thus `sum(ell_j)=sum(ell'_j)`. QED.

This strengthens the earlier *affine interpolation
obstruction*: the impossibility holds for **any**
variation of positive integer block lengths, not only
affine variation. For the new five-cube window, a
uniform argument therefore must change the root-word
and/or output order with n, or use a theorem such
as Tutte's 1-factor criterion that does not fix a
piecewise-reflection word in advance.

## 6. A full odd-reflection path quotient theorem (PROVED)

The companion [ODD_CUBE_PATH_QUOTIENT.md](ODD_CUBE_PATH_QUOTIENT.md)
proves that, throughout the entire proposed
high base `467<=n<=665`, the graph using just
odd cube sums **343 and 729** decomposes into
**exactly 193 paths**, each with **2, 3, or 4
vertices**. The two reflections compose
to translation by 386, and their fixed
initial matching pairs all vertices in
`[1,386]`.

Even more precisely:

```
467<=n<=557:
  #2-paths = 579-n, #3-paths = n-386, #4-paths = 0;
558<=n<=665:
  #2-paths = 22,    #3-paths = 728-n, #4-paths = n-557.
```

There is a closed formula for the number
`q(n)` of odd-cardinality path components
after deleting the proposed fixed point
108 for odd n; see the linked proof.
Every five-color involution with that
fixed-point rule must use **at least
`q(n)/2` even-cube 2-cycles**. In
particular, n=556,557,558 require
**at least 85** such even-cube edges.
This is a macroscopic constraint, not a
tiny missing-edge patch.

A second exact **finite-state gadget theorem**
shows that each of these paths admits at
most **five legal external-vertex masks**.
A perfect five-cube involution exists
if and only if one can select disjoint
edges of even sums 216,512,1000 whose
endpoint masks lie in these 1/2/3/4-path
tables; the remaining odd-cube edges
then match uniquely. This is an
equivalent **193-component compatible
state problem**, not a proved solution.

An arithmetic-only checker
[verify_odd_cube_path_quotient.py](verify_odd_cube_path_quotient.py)
audits the formulas across the band
without a matching solver or any old
permutation atlas. The theorems themselves
need only simple interval arithmetic.

## 7. Two-seed alternating ladders (EXPERIMENT ONLY)

Let a five-color involution on n have
fixed point 108 exactly when n is odd.
Add two new vertices `x=n+1,y=n+2`.
If there is an **alternating simple path**
from x to y, beginning and ending
with currently unmatched edges and
alternating with the old 2-cycles,
flipping along the path produces a
five-color involution on n+2 with the
same fixed-point rule.

This elementary **path-flip lemma is
fully proved**: an alternating path
of `2r+1` edges contains `r`
old matching edges and `r+1` new
edges. Removing the old and adding
the new pairs matches every internal
vertex exactly once and matches
both new endpoints. Cubic sums
are preserved because every edge
in the alternating path is one of
the five permitted reflections.

A new [two-seed iterative audit](verify_high_start_two_seed_ladder.py)
uses a general matching solver only
to obtain starting involutions at
**467 and 468**, then carries out
the above elementary operation
successively for every parity:

```
467 -> 469 -> ... -> 665   (99 path flips)
468 -> 470 -> ... -> 664   (98 path flips).
```

All **197** augmenting-path searches succeeded
in the tested deterministic ordering.
The largest observed path had **47
edges on the odd ladder** and **45
edges on the even ladder**.

These data compress the experiment
from 199 independently solved matchings
to two initial matches and 197
elementary path flips. But there is
still **no uniform theorem guaranteeing
the alternating path at each step**;
calling this a case-free proof of
the high base would be incorrect.

## 8. Correct Phase III fixed points and the 581 hybrid Tutte barrier

**Correction:** A four-cube involution using sums
`{343,512,729,1000}` cannot have fixed point
108, since `2*108=216` is not in that palette.
All odd lengths in Phase III (581..665), not
just 581, must select a valid fixed point;
the independent matching audit shows that
**either 256 or 500 works at all 43 odd lengths**.

The [103-vs-105 Tutte certificate](TUTTE_OBSTRUCTION_581.md)
at n=581 is still a nontrivial *hybrid
five-cube obstruction*: even allowing
cube 216 for fixed point 108, restricting
all its other 2-cycles to the four Phase III
colors is impossible. Indeed after
deleting 108 and 103 more vertices, the
four-color graph splits into 105 odd
components. Thus at least one
**nontrivial** sum-216 pair is required
in any five-cube involution fixing 108
at this length. The certificate does
not establish a four-color positive
existence theorem, which remains
experimentally supported.

The [corrected Phase III initial-leaf
theorem](FOUR_CUBE_BOUNDARY_FORCING.md)
uses fixed point 256 for every odd
n=581..665. Its only initial leaf
is vertex 87 for odd n<=641;
odd n>=643 have no initial leaf.

## 9. What moving the start can and cannot solve





**Yes:** The high window replaces many
complicated small-degree graph instances
by a regular five-cube, minimum-degree-two
involution problem, with the *same fixed point*
108 for all odd n. This is a much sharper
and more promising combinatorial statement
than arbitrary permutation existence.

**No:** Even a complete case-free proof of
the high-window Tutte condition would only
settle all `n>=467`. It would not by itself
prove the original `173<=n<=466` part.
The original finite parameter choices are
not logically removed just by raising the
starting length. A final global proof would
need a separate low-range reduction, or a
new downward/gluing theorem.

**Research verdict:** Keep [467,665] as the
main exploratory target for a generalized
five-reflection Tutte construction. Retain
[229,364] as the width-minimizing alternative,
but do not assume it is easier to prove.
