# Dual 193/245-path reflection decomposition in the four-cube high band

**Status: PROVED with elementary interval reflections; no perfect
matching solver and no numerical permutation atlas.**

This note gives a second, transverse short-path decomposition
of the four-cube graph `{343,512,729,1000}` on
`[1,n]`, throughout `580<=n<=665`.
It complements the previously proved
[193 odd-cube paths](ODD_CUBE_PATH_QUOTIENT.md),
and explains the exact structural tradeoff between
the arithmetically valid odd-length fixed points
256 and 500.

## 1. The even-cube skeleton has exactly 245 paths

Let `E_n` be the **loopless undirected** graph
with vertices `1,...,n` and edges `i--j`
when `i!=j` and `i+j` is either `512`
or `1000`.

**Theorem (245-path decomposition).**
For every integer `580<=n<=665`, the graph
`E_n` has **exactly 245 connected components**,
every one an isolated vertex or a simple path
on two, three, or four vertices. In terms of
the number `N_r(n)` of r-vertex components,

```
N_1(n) = 1,
N_2(n) = 744-n,
N_3(n) = n-511,
N_4(n) = 11.
```

**Proof.** The reflection `i -> 512-i`
pairs `[1,511]\\{256}` into 255
two-vertex paths

```
P_a = {a,512-a},  a=1,...,255,
```

while 256 is an isolated vertex (its
512-reflection is a forbidden self-loop;
its 1000-reflection would be 744>n).

The 1000-sum edges **already inside**
`[1,511]` join exactly the 11 pairs
of base components

```
P_a and P_(24-a), for a=1,...,11.
```

Their four-vertex paths are explicitly

```
a --(512)--> 512-a
  --(1000)--> 488+a
  --(512)--> 24-a.
```

The 22 participating base pair labels
`1,...,11,13,...,23` are all distinct.
No other 1000-sum edge lies entirely in
`[1,511]`, since such an edge must join
integers in `[489,511]`.

Now each new vertex `y in [512,n]`
has **only one** possible neighbor,
`1000-y` (the 512 reflection is
nonpositive). Its neighbor belongs to

```
P_(y-488) = {y-488,1000-y},
where y-488 runs from 24 to n-488<=177.
```

These components are distinct and are
none of the 22 base components already
merged into 4-paths. Every new y therefore
attaches as a **leaf to a distinct 2-path**,
creating exactly one 3-path.

There are precisely `n-511` new vertices,
so `N_3=n-511`. The 11 merged
4-paths remain fixed. Among the original
255 base 2-paths, 22 were consumed
in the merges and `n-511` were
extended, leaving

```
N_2=255-22-(n-511)=744-n.
```

The singleton 256 remains. The total
component number is

```
1+(744-n)+(n-511)+11=245.
```

The component sizes account for all n
vertices, and there are no extra
edges. QED.

The same difference-of-reflections
mechanism underlies both decompositions:
`R_1000 R_512(i)=i+488`,
versus `R_729 R_343(i)=i+386`
for the earlier odd-cube skeleton.

## 2. Remove one fixed point: 193+245=438

For odd `581<=n<=665`, the only
permitted single fixed points for
this four-cube palette are
`256` and `500`.
Write `O_n(f)` for the odd-sum graph
using 343,729 with fixed f deleted,
and `E_n(f)` for the even-sum graph
using 512,1000 with fixed f deleted.

The [fixed-point duality theorem](PHASE_III_FIXED_POINT_DUALITY.md)
already proves:

```
components(O_n(256)) = 194, with 1 or 2 singleton components;
components(O_n(500)) = 193, with no singleton component.
```

**Theorem (transverse fixed-point tradeoff).**
For every odd `581<=n<=665`,

```
components(E_n(256)) = 244, with NO singleton component;
components(E_n(500)) = 245, with exactly TWO singleton components.
```

More precisely, the component-size counts are:

| fixed point | N1 | N2 | N3 | N4 |
|---|---:|---:|---:|---:|
| 256 | 0 | 744-n | n-511 | 11 |
| 500 | 2 | 743-n | n-511 | 11 |

**Proof.** Vertex 256 is the unique
isolated vertex in the even-sum
skeleton `E_n`. Deleting it
removes one component without
affecting any other path. Thus
fixing 256 leaves exactly 244
2-to-4-vertex paths.

Vertex 500 instead belongs to
the constant 2-path `{12,500}`
(summed under cube 512), and its
1000-reflection is a forbidden
self-loop. Deleting 500 turns
that 2-path into isolated 12.
The original isolated 256 remains,
hence exactly two singletons, and
the total number of components
remains 245. The displayed
component-size formulas follow. QED.

**Corollary (dual conservation).** For
either valid fixed point f=256 or f=500,

```
#components(O_n(f)) + #components(E_n(f)) = 438.
```

In detail,

```
f=256: 194+244=438,
f=500: 193+245=438.
```

This is a direct consequence of the
two explicit decompositions, not
a proposed general invariant for
arbitrary sets of cube sums.

## 3. Consequence for a future constructive proof

The two possible normalizations optimize
**different** short-path quotient models:

- **Odd-path quotient (343,729)**
  favors fixed **500**: 193 modules,
  none isolated. The extra even-color
  edges 512 and 1000 must connect
  compatible states on these modules.
- **Even-path quotient (512,1000)**
  favors fixed **256**: 244 modules,
  none isolated. The extra odd-color
  edges 343 and 729 must connect
  compatible states on these modules.

In each quotient, a path with at most
four vertices has one of only
**1,2,3,5 endpoint masks**, depending
on its size 1,2,3,4, which leave
even-length path runs and therefore
a unique internal perfect matching.
The proof of this mask theorem is
the same path-complement argument
as in [ODD_CUBE_PATH_QUOTIENT.md](ODD_CUBE_PATH_QUOTIENT.md);
it applies verbatim to the even-sum
short-path decomposition.

The resulting mathematical task is
**not** to inspect 665 individual
vertices. It is to construct a
compatible collection of matching
edges between either 193 (odd-based)
or 244 (even-based) uniformly bounded
path modules.

**Limit:** The two factor decompositions
and their exact counts do not, by
themselves, prove that the full
four-cube union contains a perfect
matching. A positive uniform state
selection/augmentation theorem is
still missing. The independent
[verify_dual_reflection_paths.py](verify_dual_reflection_paths.py)
audits the size formulas arithmetically
without a matching algorithm.
