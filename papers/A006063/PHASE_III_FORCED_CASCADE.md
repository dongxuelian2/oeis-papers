# Complete forced-leaf cascade in four-cube Phase III

**PROVED by six finite boundary checks and interval monotonicity,
no perfect-matching algorithm.** This establishes the *entire*
forced-degree-one peeling process for all 43 odd lengths
`581<=n<=665`, under both valid normalized fixed points
`f=256` and `f=500`. It does **not** establish a perfect
matching in the leaf-free remainder.

Use the loopless graph `G_n(f)` on
`V=[1,n]\\{f}` with possible edge sums
`C={343,512,729,1000}`.
Write `(a,b;c)` for the compelled matched pair
`a<->b`, where `a+b=c`.
A leaf is a vertex of degree one in the
current induced graph. At each stage delete
a leaf and its unique neighbor.

## 1. The exact parameterized cascade

**Theorem (full third-phase leaf peeling).**
For every odd n in [581,665], the iterative
forced-leaf removal produces precisely the
following matched pairs, listed in the order
they become forced. After their removal,
every surviving vertex has degree **at least 2**.

If the sole fixed point is **500**:

| odd n | complete list of forced pairs |
|---|---|
| 581..601 | (12,331;343), (398,114;512), (229,283;512), (60,452;512), (548,181;729) |
| 603..665 | (12,331;343) |

If the sole fixed point is **256**:

| odd n | complete list of forced pairs |
|---|---|
| 581..587 | (87,425;512), (575,154;729), (358,371;729), (141,202;343), (527,473;1000), (39,304;343) |
| 589..627 | (87,425;512), (575,154;729), (358,371;729) |
| 629..641 | (87,425;512), (575,154;729), (358,371;729), (629,100;729) |
| 643..665 | no forced pair |

The numbers of compelled 2-cycles are respectively
`5,1` for fixed 500 and `6,3,4,0` for fixed 256.

## 2. Why the listed pairs become forced

Start with the previously proved twofold reflection
coverage lemma: before deleting a fixed vertex,
every node of the full four-color graph in
`580<=n<=665` has at least two **distinct nonloop**
neighbors. Thus any initial leaf in the normalized
graph must arise from removing the fixed vertex.

**Fixed 500.** Its only in-range nonloop neighbors
are 12 (by cube 512) and 229 (by cube 729).
The first becomes a leaf, forcing `12<->331`.
With 331 removed, vertex 398 has neighbors
114 (cube 512) and, if `n>=602`, 602
(cube 1000). Thus for odd n<=601 it becomes
a leaf, forcing `398<->114`.
Removal of 114 forces `229<->283`;
removal of 283 forces `60<->452`;
and removal of 452 forces `548<->181`.
From odd n>=603 the second alternative at 602
is present and the cascade stops after its
first pair.

**Fixed 256.** Its in-range nonloop neighbors are
87 (cube 343) and 473 (cube 729). Vertex 87
has only partner 425 (cube 512) if n<=641,
but also partner 642 (cube 729) if n>=642.
Thus for odd n<=641 it forces `87<->425`.
Deleting 425 makes `575<->154` compulsory;
deleting 154 makes `358<->371` compulsory
(the alternate neighbor 642 of 358 is out
of range for n<=641). Deleting 371
would force `141<->202` only if
`729-141=588` is not present, namely
for odd n<=587; this then forces
`527<->473`, then `39<->304`.
At odd n>=629, after the first three
pairs, vertex 629 is in the graph and
its cube-1000 partner 371 has been
removed, leaving only partner 100 by
cube 729. This forces `629<->100`.
At odd n>=643 the first vertex 87
already has two surviving neighbors,
and there is no initial leaf at all.

## 3. Why no further leaves occur: six small boundary checks

The preceding arguments show that the displayed pairs
are compulsory. We must still prove there is no
*additional* leaf after completing the list.

For each of the six parameter regimes, take its
smallest odd n=n0. Let U be the fixed vertex
together with all endpoints of the listed pairs.
Every vertex outside

```
T = {c-u : c in C, u in U, 1<=c-u<=n0}
    \\ U
```

has exactly the same neighbors as in the original
full loopless graph and thus retains degree >=2.
The following table gives **all** surviving
vertices whose degree might have decreased,
and their exact residual degree; every displayed
vertex has degree **2**.

| fixed | n0 | surviving potentially affected vertices T | residual degree |
|---|---:|---|---:|
| 500 | 581 | 162,277,446 | 2 each |
| 500 | 603 | 181,229,398 | 2 each |
| 256 | 581 | 189,208,310 | 2 each |
| 256 | 589 | 141,189,304,473 | 2 each |
| 256 | 629 | 141,189,243,304,412,473 | 2 each |
| 256 | 643 | 87,473 | 2 each |

Every entry follows directly from at most four
integer subtractions `c-i`, where c belongs
to the fixed four-cube palette. The full
pre-deletion graph has minimum degree at least
two, as shown by interval-overlap coverage.
The candidate table therefore proves the
residual graph at every regime's base n0
is entirely leaf-free.

Now increase n within the same regime,
preserving its fixed vertex and forced-pair
set U. Previously surviving vertices can
only **gain** neighbors. Every new vertex
`i>n0` has two partners

```
729-i  and 1000-i,
```

both positive and inside `[1,n]`, and
both outside the corresponding fixed
set U. These assertions follow from
the regime endpoints: for example,
in the fixed-500 581..601 regime
`1000-i>=399`, avoiding the removed
neighbor 398; for its n>=603 regime,
`1000-i<=397`, while U={500,12,331}.
The other four regimes obey the same
elementary interval bounds.
Thus each new vertex has at least two
surviving neighbors. Consequently **no
more leaves can appear at any n in that
regime**, proving the theorem. QED.

## 4. Significance and exact limitation

This theorem reduces 86 individual leaf-stripping
calculations (43 lengths times two fixed-point
normalizations) to **six arithmetic base cases
and a monotonicity argument**. It explains
the transition thresholds 588, 602, 629
and 642, and why fixed 500 provides a
particularly simple uniform forced pair
`12<->331` across all odd Phase III.

Together with
[PHASE_III_FIXED_POINT_DUALITY.md](PHASE_III_FIXED_POINT_DUALITY.md),
it supplies exact formulas for the odd-component
defect, the minimum number of even-color bridges,
and the complete compelled 2-cycle cascade
under either fixed point.

**Not proved here:** A perfect matching of the
large remaining leaf-free graph. A graph's
minimum degree being >=2 does not imply the
Tutte condition; a separate uniform matching
or augmentation theorem is still required
to eliminate the computational matching
observations on the whole [580,665] phase.

[verify_phase_iii_cascade.py](verify_phase_iii_cascade.py)
is an optional standard-library audit of the
six regimes and all 86 variants. It is not
used to infer existence from a matching solver.
