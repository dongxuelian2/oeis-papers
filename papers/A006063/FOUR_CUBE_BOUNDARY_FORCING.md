# Exact degree-one forcing across the three four-cube phases

**Status: PROVED directly by reflection intervals, no matching solver.**
This note gives the *entire initial degree-one set* of the
loopless, fixed-point-normalized graphs proposed in the
[three four-cube phases](FOUR_CUBE_PHASES.md).
These statements are necessary conditions on every
involution. They do not by themselves establish
existence of a perfect matching in the residual core.

Let `V_n=[1,n]` for even n. For odd n let
`V_n=[1,n]\\{f_n}`, with `f_n=108` for
`n<=579` and `f_n=256` for `n>=580`.
Both choices have a cubic self-sum in their
respective palettes. For a four-cube palette
C, make a loopless graph on V_n with edges
`{i,j}` for `i!=j`, `i+j in C`. A vertex
of degree one has its incident pair forced
in every perfect matching.

## 1. Phase I: [467,560], colors 216,343,512,729

**Theorem I (complete initial leaf set for 512<=n<=560).**
For each even n in [512,560], the degree-one
vertices are **exactly** `[512,n]`.
For each odd n in [513,559], they are
**exactly** `[512,n] union {404}`.

Every `i in [512,n]` must be matched to
`729-i`. At odd n, the additional forced
pair is `404<->325`.

**Proof.** For i>=512, cube sums
216,343,512 cannot give a positive partner;
729-i lies in [169,217] and is in V_n,
so the degree is exactly one. For
1<=i<=511, the domains of 216,343,512,729
overlap at least twice: at n=512
they are, respectively,
`[1,215]`, `[1,342]`, `[1,511]`,
`[217,512]`. Increasing n cannot
remove a neighbor. The only reflection
self-loops in this palette are at
108 (cube 216) and 256 (cube 512);
their other neighbors remain, so
discarding loops creates no further
degree-one vertices.

For odd n, deleting fixed point 108
can reduce degrees only at vertices
`343-108=235`, `512-108=404`,
and `729-108=621>n`.
Vertex 235 retains neighbors 277 and
494; vertex 404 retains only 325.
Thus the displayed sets are exact. QED.

## 2. Phase II: [561,579], colors 216,512,729,1000

**Theorem II (exactly two initial leaves).**
For every even n in [562,578], the
degree-one vertices are exactly
`{108,256}`, forcing

```
108 <-> 404,    256 <-> 473.
```

For every odd n in [561,579], after
deleting the proposed sole fixed point
108, the degree-one vertices are
exactly `{256,404}`, forcing

```
256 <-> 473,    404 <-> 325.
```

**Proof.** Over the entire phase,
the four reflection domains have
at least double coverage. At n=561
they include

```
216: [1,215],
512: [1,511],
729: [168,561],
1000:[439,561].
```

Every i lies in at least two. Only
i=108 and i=256 are self-reflection
vertices for the two small even cubes
216 and 512, reducing their loopless
degrees from two to one. For odd n,
fixed vertex 108 is absent, and its
neighbor 404 loses that sole 512-edge,
leaving exactly 729-404=325. No other
vertex loses its second nonloop
neighbor, since `729-108=621>n`
and `1000-108=892>n`. QED.

## 3. Phase III: [580,665], colors 343,512,729,1000

**Theorem III (exact initial leaf changes under the valid fixed-point rule).**
For even n throughout [580,664], the loopless
graph has **no** degree-one vertex.

For odd n throughout [581,665], the required
fixed point is **256** (the cube self-sum 512).
The remaining graph has exactly the following
initial degree-one vertices:

```
n in [581,641] odd:   {87}, forcing 87<->425;
n in [643,665] odd:   empty.
```

The alternative fixed point **500** is also
permitted by this phase's 1000 cube; the
displayed degree-one statement specifically
uses the fixed-256 normalization.

**Proof.** At n=580 the four reflection
domains are

```
343:  [1,342],
512:  [1,511],
729:  [149,580],
1000: [420,580].
```

They give at least two distinct nonloop
partners to every vertex; the potential
even-cube loops at 256 and 500 each have
two other neighbors. For new vertices
`581<=i<=665`, the two partners
`729-i` and `1000-i` are always
positive and inside `[1,n]`. Thus
all even graphs have minimum degree 2.

When vertex 256 is removed at odd n, its
only other in-range neighbors are
`343-256=87` and `729-256=473`.
Vertex 473 retains 39 (cube 512) and
527 (cube 1000), while vertex 87
retains 425 (cube 512). It acquires
another neighbor, 642 (cube 729),
as soon as `n>=642`. These are the
only vertices whose nonloop degrees
can decrease when 256 is removed.
The theorem follows. QED.

## 4. Precise use in a future four-cube proof

The above is a **uniform structural
boundary theorem**, not a perfect
matching theorem. It partitions
the high-window study into finitely
many regimes determined by the exact
reflection thresholds 512 and 642, and gives all initially forced
edges in each phase.

Removing these pairs sometimes
creates new degree-one vertices;
that subsequent cascade is precisely
the open part of a uniform local
matching/augmentation argument.
The [pure-Python audit](verify_four_cube_boundary_forcing.py)
checks the initial degrees for all
199 high-window lengths, without
using any matching solver.
