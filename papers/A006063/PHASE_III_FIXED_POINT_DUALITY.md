# Phase III fixed-point duality: exact odd-component counts and forced pairs

**Status: PROVED by two explicit short-path calculations, with no matching
solver.** For every odd integer `581<=n<=665`, the four-sum palette
`C={343,512,729,1000}` permits the candidate fixed points
`f=256` (512=2f) and `f=500` (1000=2f).
Computational matching experiments find a complete involution
for either choice at each length, but **existence is not used as a premise**
of the structural results below.

## 1. The fixed-point deletion theorem

Write `H_n` for the graph on `[1,n]` with only odd cube-sums
343 and 729. The previously established 193-path decomposition gives:

- 171 paths
  `C_x={x,343-x} union ({386+x} if 386+x<=n)
   union ({729-x} if 729-x<=n)`, `1<=x<=171`;
- 22 constant two-vertex paths.

For `n>=558`, exactly `d(n)=728-n` paths have odd size.

Let `q_f(n)` count the **odd-order connected components** of
the induced odd-sum graph `H_n - {f}`, for either valid fixed point.

**Theorem (exact Phase III fixed-point component defect).** For all
odd `581<=n<=665`,

```
q_256(n)=729-n,
q_500(n)=727-n,  581<=n<=613,
q_500(n)=729-n,  615<=n<=665.
```

**Proof.** Fixing 256 alters only `C_87`, which is

```
{87,256,473}                  when 581<=n<=641,
{87,256,473,642}              when 642<=n<=665.
```

The path has the edges `87--256--473` and, when present,
`87--642`. Deleting 256 turns the first three-vertex path
into **two isolated vertices** (two odd components, versus
one before deletion). In the four-vertex case, it leaves
the edge 87--642 plus isolated 473 (**one odd component,
versus zero before deletion**). In both regimes, the
number of odd components increases by exactly 1:
`q_256(n)=d(n)+1=729-n`.

Fixing 500 alters only `C_114`, which is

```
{114,229,500}                 when 581<=n<=613,
{114,229,500,615}             when 615<=n<=665.
```

The three-vertex path is `114--229--500`.
Deleting the leaf 500 leaves the even edge 114--229,
so the original one odd component disappears
(`q_500=d-1`). The four-vertex path has edges
`615--114--229--500`; deleting leaf 500 leaves
a three-vertex path, creating one odd component
(`q_500=d+1`). Substitution of `d=728-n`
gives the asserted formulas. QED.

## 2. Exact component-size distributions: 193 versus 194

The preceding proof determines not only odd-component
*counts* but the **complete component-size profiles**.

Let `N_r^{(f)}(n)` denote the number of r-vertex
components in the odd-cube graph `H_n-{f}`.
For every odd `581<=n<=665`:

**Fixed f=500:** always exactly **193** components,
each still a path with **2–4 vertices**:

| odd n | N2 | N3 | N4 |
|---|---:|---:|---:|
| 581..613 | 23 | 727-n | n-557 |
| 615..665 | 22 | 729-n | n-558 |

**Fixed f=256:** always exactly **194** components,
including at least one **isolated vertex**:

| odd n | N1 | N2 | N3 | N4 |
|---|---:|---:|---:|---:|
| 581..641 | 2 | 22 | 727-n | n-557 |
| 643..665 | 1 | 23 | 728-n | n-558 |

**Proof.** In the original 193-path decomposition,
for n>=558 the size counts are
`N2=22`, `N3=728-n`, `N4=n-557`.
For f=500, `C_114` is a 3-path when
n<=613 and a 4-path when n>=615;
removing its **endpoint** converts size
3 to 2 or size 4 to 3. Thus it preserves
the number of components and never creates
a singleton. For f=256, `C_87` is
a 3-path when n<=641 and a 4-path
when n>=643; deleting its **interior**
vertex converts size 3 into two singletons,
or size 4 into a singleton plus a 2-path.
This increases the total number of
components by one, to 194, in every case.
The four formulas follow by subtracting
and adding the affected path counts. QED.

**Structural consequence.** Within the two
arithmetically legal one-fixed-point choices,
`f=500` is the **unique normalization
that preserves the original 193 disjoint
2–4-vertex path modules**, whereas `f=256`
creates a second module and at least one
isolated odd-color vertex. For a future
uniform finite-state gadget proof, fixing
500 throughout Phase III is therefore
the cleaner mathematically justified choice.
This comparison makes no claim that a
four-cube perfect matching exists; it
only simplifies the equivalent state problem.

## 3. Uniform initial forced-edge theorem

**Theorem (precise initial leaves under either fixed point).**
Use the *full four-sum* loopless graph on
`[1,n]\\{f}`, with the indicated fixed point removed.

For all odd `581<=n<=665`:

- If `f=500`, the graph has **exactly one initial
  degree-one vertex**, namely `12`, and its unique
  neighbor is `331`, since `12+331=343`.
- If `f=256`, the graph has exactly the one
  initial degree-one vertex `87` for
  `581<=n<=641`, forcing `87<->425`.
  For `643<=n<=665`, it has **no** initial
  degree-one vertices.

**Proof.** Before removing the fixed vertex, every
vertex has at least two distinct nonloop neighbors in
the four-sum graph throughout this band, by the
previous reflection-domain overlap theorem.
Removing a fixed vertex can reduce only its old neighbors.

For 500, those neighbors are 12 (via 512) and
229 (via 729). Vertex 12 retains 331 (via 343)
and has no other allowed in-range neighbors,
because `729-12=717>665`. Vertex 229 retains
both 114 (via 343) and 283 (via 512), and
therefore does not become a leaf.

For 256, the old nonloop neighbors are 87
(via 343) and 473 (via 729). Vertex 473
retains 39 (via 512) and 527 (via 1000).
Vertex 87 retains 425 (via 512), and
acquires 642 (via 729) when `n>=642`.
The fixed-256 statement follows. QED.

## 4. An exact even-cube matching resource bound

Consider a fixed-point-free perfect matching
on `[1,n]\\{f}` using the four cubes. Relative
to the odd-cube components from Section 1,
any odd component must have at least one
matching edge exiting that component. Such
edges must use one of the **two even cubes**
`512,1000`. Each even-cube edge can serve
at most two odd components. Therefore
the number `E_even` of even-cube 2-cycles
necessarily satisfies

```
E_even >= q_f(n)/2.
```

The above formulas yield:

```
fixed 256:  E_even >= (729-n)/2     for all odd 581<=n<=665;
fixed 500:  E_even >= (727-n)/2     for odd 581<=n<=613;
fixed 500:  E_even >= (729-n)/2     for odd 615<=n<=665.
```

For example at n=581, fixing 256 forces
at least 74 even-cube pairs, whereas
fixing 500 forces at least 73. This
**does not** prove that either lower
bound is attainable: actual four-cube
perfect matchings may require many
more even-cube edges.

## 5. Why this matters for an unconditional phase theorem

The usual fixed-256 normalization is valid
at every odd Phase III length, but its odd
component defect is always 2 larger than
fixed 500 over the initial 17 odd lengths
581..613. Choosing 500 also gives **the same
forced pair 12<->331 across the entire
odd Phase III interval**, while the forced
pair for fixed 256 disappears at n=643.

This leads to two legitimate, mathematically
different normalizations for an eventual
uniform matching proof. One may use
fixed 500 throughout Phase III for a constant
leaf rule, or choose 500 until 613 and 256
later, without changing the four-sum palette.

**What remains open:** Proving the full
perfect-matching Tutte conditions uniformly
for either normalization. All statements
above are necessary structural constraints,
not a proof of positive four-cube matching
existence for every length.
