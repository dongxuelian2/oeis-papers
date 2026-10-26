# A006063 — rigorous interval-overlap avalanche and its sharp finite barrier

**Status: PROVED (conditional avalanche), OPEN (elimination of finite seeds).**
This note does **not** claim to remove the 57 finite cubic-order
parameter choices. It establishes the exact interval-propagation
mechanism, its completely symbolic infinite tail, and a precise
obstruction showing why pure suffix reflection cannot supply the
missing initial conditions.

Write `G(n)` for the existence of a permutation of `[1,n]`
whose index-image sums are all cubes. Write `G(0)` for the
empty permutation.

## The interval-overlap avalanche lemma

**Lemma 1 (one-cube reflected interval).** Suppose `G(m)`
is known for **every** integer `m in [a,b]`, with
`0<=a<=b`. For every cube `c=k^3`, every integer
`n` in

```
J_c([a,b]) = [ max(1,ceil(c/2),c-b-1), c-a-1 ]
```

is also good, provided the displayed interval is nonempty.

**Proof.** Put `m=c-n-1`. The interval bounds give
`a<=m<=b`, `m>=0`, and `m<n`. Retain the
good permutation on `[1,m]` and set `p(i)=c-i`
for `m+1<=i<=n`. The appended suffix maps bijectively
onto itself; its index-image sums are exactly `c`.
The construction is valid for every such integer `n`. QED.

**Lemma 2 (interval-overlap avalanche).** Suppose `G(n)`
holds for every `n in [a,b]` with `1<=a<=b`.
If there is a cube `c` such that

```
a+b+2 <= c <= 2*b+2,                               (A)
```

then

```
G(n) for every a<=n<=c-a-1.
```

In particular the certified upper endpoint grows from `b`
to `b'=c-a-1 >= b+1`.

**Proof.** Lemma 1 gives the reflected interval
`[c-b-1,c-a-1]` after truncation by `ceil(c/2)`.
Condition `c<=2*b+2` ensures that the very next
integer `b+1` is in that interval. Condition
`c>=a+b+2` ensures that its right endpoint is at
least `b+1`. Consequently the new reflected interval
touches the old one and their union contains the full
interval `[a,c-a-1]`. QED.

The condition (A) is also **necessary for this particular
one-cube, one-interval extension from [a,b] to include b+1**:
the only predecessor for n=b+1 under cube c is
`m=c-b-2`, and membership `m in [a,b]` gives
exactly (A). It is not claimed necessary for existence
of other permutations or other constructions.

**Lemma 3 (many-interval avalanche).** If good integers
are known on a union of closed integer intervals
`I_1 union ... union I_r`, append every nonempty
`J_c(I_j)` from Lemma 1 for each cube `c`,
merge overlapping *or adjacent* integer intervals,
and repeat. Every point in every resulting interval
is good. This follows by induction from Lemma 1,
and is a pure symbolic union/overlap rule. It does
not automatically establish that all gaps disappear.

## The infinite avalanche for A006063

**Theorem 4 (purely algebraic tail).** If `G(n)` is
known for each integer `173<=n<=364`, then
`G(n)` holds for **all** `n>=173`, with no
further matching, determinant checks, or finite search.

**Proof.** In Lemma 2 take `a=173`, `b=364`,
`c=9^3=729`. Since

```
173+364+2=539 <= 729 <= 730=2*364+2,
```

the entire interval `[173,555]` is good.
For `k>=9`, assume `[173,k^3-174]` is good.
The next cube `c=(k+1)^3` obeys

```
a+(k^3-174)+2 = k^3+1 <= (k+1)^3,
(k+1)^3 <= 2*k^3-346 = 2*(k^3-174)+2.
```

The second inequality is equivalent to

```
f(k)=k^3-3*k^2-3*k-347 >= 0.
```

At `k=9`, `f(9)=112`; and

```
f(k+1)-f(k)=3*k^2-3*k-5 > 0    for k>=9.
```

Lemma 2 therefore extends `[173,k^3-174]` to
`[173,(k+1)^3-174]`. These endpoints tend to
infinity. QED.

This replaces the earlier strong-induction cube-gap
calculation with a genuine **interval-overlap induction**,
but has exactly the *same finite starting obligation*.

## Why an overlap-only final lemma cannot replace the finite base

**Proposition 5 (covering reflection intervals is insufficient).**
For `n=65`, the cube-reflection domains

```
I_64=[1,63],  I_125=[60,65]
```

cover every integer from `1` to `65` and overlap
on `[60,63]`. Nevertheless `G(65)` is false.

**Proof (an explicit Hall obstruction).** The four rows

```
S={3,40,59,64}
```

have possible image columns only in

```
N(S)={5,24,61}
```

under all cubes in `[2,130]`, namely
`8,27,64,125`. Since `|N(S)|=3<4=|S|`,
a perfect cube-sum matching cannot exist. QED.

**Proposition 6 (length 173 cannot be obtained by suffix reflection
from any smaller legal length).** A single strictly increasing
cubic suffix reflection of length `n=173` would require

```
m=c-174 >=0,  m<173,  c a cube,
```

and therefore `c=216,343`; the only possible
predecessors are `m=42,169`. Neither is good.

**Proof (two short Hall obstructions, grouped in pairs).**

For `m=42`, define

```
S_42=[1,2] union [20,21] union [38,39]   (6 rows).
```

Its cube-sum neighbors from `8,27,64` lie exactly in

```
N(S_42)=[6,7] union [25,26]              (4 columns).
```

Thus `G(42)` is false.

For `m=169`, define the fourteen-row set

```
S_169=[8,9] union [38,39] union [45,46]
      union [99,100] union [129,130]
      union [136,137] union [160,161].
```

Its cube-sum neighbors from `8,27,64,125,216`
lie exactly in the twelve-column set

```
N(S_169)=[18,19] union [25,26] union [55,56]
         union [79,80] union [86,87] union [116,117].
```

Again `|N(S_169)|=12<14=|S_169|`.
Both obstructions are checked directly by cube
subtraction and need no computer-assisted matching.
So no predecessor is available for `n=173`. QED.

**Proposition 7 (the 338-to-339 avalanche bottleneck).**
Suppose one has only a *contiguous* known interval
`[173,338]` to feed Lemma 2. To extend it to
include 339 with a single cube, condition (A)
would require

```
513=173+338+2 <= c <= 2*338+2=678.
```

There is **no integer cube** in this range:
`8^3=512` and `9^3=729`.
Hence the basic interval-overlap avalanche cannot
bridge this gap. Other available small predecessors
or new local matching constructions may bridge
some or all positions, but those are **additional
mathematical input**, not consequences of Lemma 2.

## Research conclusion

The interval-overlap avalanche is now completely
proved and completely removes the **infinite tail's**
need for finite or computational validation.
It does **not** remove the essential question:

```
Can the full 173..364 interval be obtained without
57 separately selected algebraic parameter shapes?
```

A positive answer requires a stronger *local
cube-sum matching/augmentation or gluing theorem*,
not just coverage or overlap of cube-reflection
domains and not just repeated suffix reflection.

The results above should **not** be presented as
a case-free proof of the initial interval.
