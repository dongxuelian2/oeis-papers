# A006063: 56 algebraic shapes, forced 173, six templates, and symbolic avalanche

**Current reduced existence proof:** The critical length `173` is
proved directly by [forced-reflection leaf peeling](FORCED_REFLECTION_PEELING.md).
The other previously exceptional lengths are described by
**56 cubic-root/output-order determinant shapes** (784 blocks),
while six previously derived symbolic templates construct **25**
further seed lengths. Thus 1 forced seed + 56 determinant seeds +
25 parametric-template seeds = **82 established bases**, and
the preexisting cubic-reflection closures give every length in
`[173,364]`. The interval-overlap avalanche propagates them to
all `n>=173`, symbolically.

A new **three-band forced avalanche** for all `173<=n<=181`
proves that the reflected bands
`[125,342-n]`, `[34,215-n]`, and `[95,276-n]`
are forced successively, identifying `582-3*n` reflected pairs.
The same graph-theoretic argument proves
`P(173)=1`, `P(174)=1`, and `P(175)=3`
by a 15-/19-round leaf-stripping certificate and a nine-cycle
core. It also proves that any 173-to-174 extension rewires
**25** existing assignments.

The full older 57-shape determinant proof and 57 numeric
endpoint identities remain available as independent
cross-checks, but **173 no longer requires an algebraic
shape or endpoint table**. A general case-free proof of the
entire middle interval is still open; the remaining 56
positive shape certificates have not been eliminated.

## 1. Two elementary operations

Let `P(n)>0` mean that a permutation `p:[1,n]->[1,n]` satisfies
`i+p(i)=k^3` for some positive integer `k` for every index `i`.

**Endpoint-balance lemma.** For integer breakpoints
`0=b_0<b_1<...<b_t=n` and cubes `c_j=k_j^3`, put
`L_j=c_j-b_j`, `R_j=c_j-b_(j-1)`. If
`1<=L_j<R_j<=n+1`, then the formula
`p(i)=c_j-i` for `b_(j-1)<i<=b_j` gives a legal permutation
if and only if the two **multisets** agree:

```
{1,R_1,...,R_t} = {n+1,L_1,...,L_t}.
```

Indeed, the reflected images are exactly the half-open integer intervals
`[L_j,R_j)`. Equality of the endpoint multisets says that the jump
of their covering multiplicity is `+1` at `1`, `-1` at `n+1`,
and zero elsewhere. Therefore every integer from `1` to `n` is
covered exactly once.

**Cubic suffix-reflection lemma.** Let `0<=m<n`, where `m=0`
denotes the empty permutation. If a legal permutation of length `m`
exists and `m+n+1=k^3`, retain it on `[1,m]` and append
`p(i)=k^3-i` on `[m+1,n]`. The appended images are exactly
`[m+1,n]`, so the resulting permutation is legal. This operation
requires no matching theorem or computational hypothesis.

## 2. Algebraic determinant parameterization (56 necessary shapes; 57 retained redundantly)

The original 57 cases are **mathematically parameterized** by the
[unimodular block-order theorem](UNIMODULAR_BLOCK_FACTORY.md). The
[57 cubic-order shapes](certificates/finite_57_cubic_order_shapes.txt)
contain only an output-block permutation `pi` and a cubic root
word `k` for each target length. **They contain no endpoints.**

For an output order `pi` on `t` blocks define

```
M[j,i] = [i<j] + [pos_pi(i)<pos_pi(j)] + [i=j],
d_j = k_j^3 - 1.
```

A general chord-diagram intersection-form argument proves that
**det M is always either 0 or 1**. Every one of the 57
supplied orders has `det M=1`. Consequently, the **single
integer-polynomial formula**

```
ell_j(k) = det(M with column j replaced by d)
```

constructs all the blocks of each of the 57 cases by Cramer's rule.
Whenever these integers are positive, the reflected blocks
`p(i)=k_j^3-i` **automatically form a permutation**, with no
separate endpoint-multiset verification. The 57 listed root words
produce positive vectors, whose global minimum entry is 1.

Furthermore **every one of these 57 algebraic families is infinite**:
let `v=M^(-1)*1`, for which the chord Pfaffian formulas give
`v_j in {-1,0,1}` and `sum(v_j)=t mod 2`. For an arbitrary
positive integer `h`, replacing `k` by `h*k` gives

```
ell_j(h) = ell_j + (h^3-1)*(ell_j+v_j) > 0,
N(h) = (N+epsilon)*h^3 - epsilon, epsilon=t mod 2.
```

These are **symbolic identities valid for every h**, not
computationally extrapolated examples. For odd `t` the lengths
are `(N+1)h^3-1`; for even `t`, `Nh^3`.

**Precise remaining finite obligation:** 57 root words and output
orders are still explicitly selected, and the determinant-length
vectors at those root words must be certified positive. Thus
this is a **unified algebraic construction of all 57**, not a
case-free existence proof with no finite data. The old endpoint
atlas is retained only as an independent redundant check.

### 2a. Six additional compact block families

## 3. The reduced finite arithmetic base: 56 + 1 + 25

The active [56-shape algebraic table](certificates/finite_56_cubic_order_shapes.txt)
contains no precomputed interval boundaries and recovers **784** input
blocks from exact Cramer determinants. The excluded `n=173` shape
is replaced by the [forced-neighbor theorem](FORCED_REFLECTION_PEELING.md),
with a 15-round purely graph-theoretic uniqueness proof. The
[56+forced checker](verify_56_plus_forcing.py) reconstructs
all 82 seeds without reading any legacy endpoint atlas.

## 3. The self-contained finite arithmetic base

The 57 parameter shapes above derive all **795** residual reflected
blocks algebraically. The older
[57 endpoint identity rows](certificates/finite_57_exceptional_atlas.txt)
remain available only as an independent redundant finite certificate.
The six universal algebraic block-rearrangement families provide
**25 additional base lengths**:

- [Four-, five-, six-block formulas](PARAMETRIC_BLOCK_TEMPLATES.md):
  `66,85,100,103,119,122,182,254`.
- [Twelve-block three-switch family](BINARY_BLOCK_FAMILY.md):
  `131,132,150,151,155,156,174,175`.
- [Fifteen-block constrained-switch family](FIFTEEN_BLOCK_FAMILY.md):
  `228,229,231,238,240,241`.
- [Ten-block nested-switch family](TEN_BLOCK_FAMILY.md):
  `345,351,357`.

The **82 independently justified seed lengths** are exactly:

**22 lower seeds:**
`66,82,85,100,103,116,118,119,120,121,122,123,125,126,127,129,
131,132,150,151,155,156`.

**60 middle seeds:**
`173,174,175,176,177,179,180,181,182,184,185,188,194,197,198,199,
200,201,202,203,204,205,206,228,229,231,233,234,235,236,238,
240,241,243,245,246,247,248,249,250,251,252,253,254,339,341,
343,344,345,346,347,348,349,350,351,353,354,357,358,363`.

Of the 57 explicitly printed rows, **10** are below 173
and **47** lie between 173 and 364. The other **12 lower** and
**13 middle** seeds arise by the six symbolic template families.
The full 82-row comparison atlas is retained independently
with 1,009 intervals, including the 214 template intervals.

A block-rearrangement family is not a restatement of the
endpoint criterion: for input lengths `ell_j`, output order
`pi`, and input/output prefix lengths `A_j,B_j`, the sums
`C_j=1+A_j+B_j+ell_j` are **symbolically proven cubes** for
each nonempty block. The output intervals automatically partition
`[1,n]`; an empty block imposes no cube condition.

## 4. Closure: all lengths from 173 to 364

Take the empty permutation at length `0`, the 56 required determinant
shapes, the forced-reflection base at `173`, and the 25 symbolic
outputs of the six parameter families,
and apply the cubic suffix-reflection lemma in increasing order of
the target length `n`. At each omitted `n<=364`, test whether a
cube `c` among `8,27,64,125,216,343,512` has
`m=c-n-1` already constructed with `0<=m<n`.

The exact closure yields **26 further lengths below 173** (48
constructed positive lengths below 173 in total) and **132 further
lengths in [173,364]**. Thus the 60 directly certified lengths plus
the 132 reflected lengths exhaust all 192 integers in [173,364].
The 132 comprise **49 direct reflections from smaller lengths below
173**, together with **83 reflections from lengths 173..255**, which
cover 256..338 via `m=511-n` and cube `512`.

A representative compression:

```
n = 211:  m=131, c=343, so p(i)=343-i on 132<=i<=211.
n = 340:  m=171, c=512, so p(i)=512-i on 172<=i<=340.
n = 342:  m=0,   c=343, so p(i)=343-i on 1<=i<=342.
```

In particular, length 211 no longer needs its former 53-segment
independent entry. This is an algebraic proof dependency, not a
shorter printout of that entry.

The closure does not presuppose the published list of admissible
lengths below 173: the 48 needed lower lengths are **constructed**
from the 22 established lower seeds (10 printed exceptional rows
and 12 symbolic instances) and the empty seed. Likewise,
this note does not assert nonexistence at any smaller lengths.

Every selected seed length is irredundant **within the stated 82-length
system under strictly growing cubic suffix reflections**: when
processed in increasing order, no seed can be obtained from a
previously constructed shorter length by this one operation.
This is not a claim of a globally minimal basis under arbitrary
permutation constructions.

## 5. Exact interval-overlap avalanche (no computation in the infinite tail)

The full [mathematical proof and sharp Hall limitations](INTERVAL_OVERLAP_AVALANCHE.md)
are written out separately.

**Avalanche lemma.** If every length in `[a,b]` admits a cube-sum
permutation and an integer cube `c` obeys

```
a+b+2 <= c <= 2*b+2,
```

then every length in `[a,c-a-1]` also admits one. For each
new length `n`, put `m=c-n-1`; the inequalities ensure
`a<=m<=b` and `m<n`. The cubic suffix reflection
`p(i)=c-i` on `[m+1,n]` extends the permutation.

Starting with the independently established finite interval
`[173,364]`, choose `c=9^3=729`: the inequalities
`539<=729<=730` give the extended interval `[173,555]`.
For every `k>=9`, use `c=(k+1)^3` to extend
`[173,k^3-174]` to `[173,(k+1)^3-174]` because

```
k^3+1 <= (k+1)^3 <= 2*k^3-346,
f(k)=k^3-3*k^2-3*k-347 >= f(9)=112,
f(k+1)-f(k)=3*k^2-3*k-5 > 0.
```

The expanding upper bounds tend to infinity; therefore
every `n>=173` is covered with **no new finite certificate**.

**Not a finite-base elimination theorem.** Domain overlap alone
does not imply Hall. At `n=65`, reflection domains `[1,63]`
and `[60,65]` cover the full range, but
`S={3,40,59,64}` has just three cube-sum neighbors
`{5,24,61}`. Length `173` cannot be obtained by suffix
reflection from a shorter good length: its only possible
predecessors are `42` and `169`, both excluded by
explicit Hall sets in the linked note. Moreover,
`[173,338]` cannot extend past `338` using the
simple single-cube avalanche since the required interval
`[513,678]` contains no cube.

**Theorem (exact scope).** The forced-reflection theorem at 173,
56 positive algebraic cubic-order shapes, six explicit block
template families, the empty permutation, the finite reflection
closures, and the interval-overlap avalanche prove `P(n)>0` for **every `n>=173`**. The initial finite
shape selection and 56 positivity conditions have **not**
been eliminated. A case-free result would require a stronger
local cube-sum matching or augmentation theorem.

## 6. Verification, limitations, and next mathematical questions

[verify_56_plus_forcing.py](verify_56_plus_forcing.py) reads
the **56 reduced cubic-order shapes**, reconstructs their
strictly positive integer lengths, calls the independent
forced-leaf proof for the omitted `173` seed, and combines
these with the original 25 algebraic-template constructions
to verify all 82 bases. It never reads the older 57-row
endpoint certificate.

[verify_forced_peeling.py](verify_forced_peeling.py) independently
checks the three parametric forced bands, exact uniqueness
at 173 and 174, the 10-vertex core and count at 175, and
the 25 obligatory reassignments from 173 to 174.


[verify_57_plus_templates.py](verify_57_plus_templates.py) reads
**only the 57 exceptional rows** and regenerates 25 other base
lengths from the six algebraic formulas. It independently checks
all integer endpoint bounds and multisets, every block's cubic sum,
and the increasing finite suffix-reflection closure.

The new [unimodular-factory checker](verify_unimodular_factory.py)
reads the cubic-root words and output-block orders alone, uses exact
integer Bareiss elimination to recover all 57 positive vectors,
checks the cubic dilation formula, and independently closes the
finite interval. It never reads the old 57-row endpoints.

A second, independent reconstruction directly produced
the actual permutations for all **240 covered positive lengths**
(48 below 173 and all 192 lengths in 173..364) and checked
both bijectivity and the cubic-sum property. The older
60/66/70/74/82/109-row certificates remain available for
redundant audits. The **interval-overlap infinite-tail induction**
is symbolic and is not a computational assumption.

**Unresolved:** There remain **56 finite positivity obligations
for 56 selected determinant parameter sets**, along with the new
non-parametric, finite forced-leaf certificate for length 173. The interval-overlap avalanche does not
prove the base interval without those choices. The determinant theorem algebraically generates 56 selected
base lengths, the leaf theorem generates 173, and six compact
templates cover 25 lengths; the remaining 56 parameter choices
have not been eliminated.
Neither a minimality statement for 57 nor an independent
peer-review or literature-priority claim is made.
