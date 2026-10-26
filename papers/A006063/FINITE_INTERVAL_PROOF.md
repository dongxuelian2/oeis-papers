# A006063: finite base cases as algebraic interval identities

This note is intentionally restricted to the finite gap **173 <= n <= 364**.
It does not pursue asymptotic, counting, or sharpness improvements.
The claim is a paper-checkable proof that does not require executing a
bipartite-matching algorithm or a 191-step cumulative augmenting-path
validator.

## Interval reflection lemma

Choose integers

    0=b_0 < b_1 < ... < b_t=n

and integer cube roots k_1,...,k_t. Define

    p(i)=k_j**3-i  for b_(j-1)<i<=b_j.

Let

    L_j=k_j**3-b_j,
    R_j=k_j**3-b_(j-1).

Require 1<=L_j<R_j<=n+1. Then the image of the j-th
input interval is exactly [L_j,R_j) in the half-open
integer-interval convention.

**Criterion (necessary and sufficient):**

    multiset(1,R_1,...,R_t)
      = multiset(n+1,L_1,...,L_t).

**Proof:** Let f(x) be the number of output intervals
covering x, with f(0)=f(n+1)=0. The difference
f(x)-f(x-1) is the number of interval starts at x minus
the number of interval ends at x. The multiset identity
is equivalent to this difference being +1 at x=1,
-1 at x=n+1, and 0 elsewhere. Thus f(x)=1 for
1<=x<=n. Hence the output intervals partition [1,n]
exactly once and all row sums are cubes. The converse
follows by reversing the argument.

This lemma is a *symbolic arithmetic assertion*. It
does not say "run the matching algorithm".

## Standalone base certificate

[certificates/finite_block_atlas.txt](certificates/finite_block_atlas.txt)
contains **109** explicit rows, one for each integer

    173 <= n <= 255,  or  339 <= n <= 364.

A row begins with its length n; every token b:k specifies
a segment endpoint b and its cube root k. The leftmost
boundary is always b_0=0; the last is b_t=n. To inspect a
row, form the two finite integer lists:

    list A = (n+1, k_1**3-b_1,...,k_t**3-b_t)
    list B = (1, k_1**3-b_0,...,k_t**3-b_(t-1)).

All numbers lie in [1,n+1], and the two lists have the
same elements with the same multiplicities.

For example:

    n=340:
      7:2 19:3 44:4 171:6 340:8

Both sorted lists are

    1, 8, 20, 45, 172, 341.

For the non-involutive exceptional n=236, the table row is

    7:2 18:6 43:5 45:6 54:4 79:5 81:6
    106:5 134:7 145:6 170:7 172:6
    206:7 208:6 236:7

and its common sorted boundary list is

    1, 8, 10, 19, 44, 46, 71, 82,
    107, 135, 137, 171, 173, 198, 209, 237.

These are two representative examples of the same exact
verification step. The entire table has 1,123 segments
in total, using only roots 2 through 8.

The table is also included in the LaTeX paper, so it
is inspectable without downloading any JSON archives.

## Why the exceptional n=236 cannot be replaced by involution blocks

It is tempting to prove all cases by pairing positions in
transpositions (an involution). This is impossible at n=236,
although the 15-segment row above is a legal permutation.

For a direct parity obstruction, let G be the undirected
cube-sum graph on [1,236], and remove the 86 vertices in

    S = [1,3] U [9,13] U [19,24] U [35,39]
        U [45,49] U [56,60] U [71,74] U [81,85]
        U [107,115] U [117,121] U [126,130]
        U [136,140] U [147,151] U [162,166]
        U [172,176] U [198,201] U [208,212].

Here [a,b] is the full integer interval from a to b.
Checking only the possible cube-sum edges
8,27,64,125,216,343 shows that the components of
G minus S consist of:

    87 singleton components;
    one 5-vertex component {14,50,75,141,202};
    further components of sizes 4,6,10,12,12,14.

Exactly one singleton, vertex 4, has an allowed loop
(2*4=8); the odd five-vertex component has no loop.
Thus **87 distinct odd components without an allowed
fixed point** must each use at least one matching edge
to S in any hypothetical involution. Since |S|=86,
there are not enough vertices of S. Hence no legal
involution exists at n=236.

This is a short finite parity/Tutte obstruction,
independent of the 109 general permutation formulas.
It explains why the self-contained base proof must allow
ordinary permutations, not only involutions.

## Extending from the table to all n>=173

For 256 <= n <= 338, put m=511-n. Then

    173 <= m <= 255,    m < n,
    m+n+1 = 512 = 8**3.

Retain the known permutation on [1,m] and reflect the
suffix [m+1,n] by i -> 512-i. This is a bijection
with all new index-image sums 512.

For n >= 365, the cubic gap lemma supplies a cube c with

    n+174 <= c <= 2*n.

The predecessor m=c-n-1 lies in [173,n-1] and
strong induction supplies the needed permutation at m.
The suffix reflection i -> c-i constructs size n.
Thus **all n>=173** follow from the 109 elementary
integer multiset identities.

## What is and is not eliminated

- **Eliminated from the proof:** runtime matching search,
  the 191 successive augmented paths and their
  error-prone dependency on earlier paths,
  and opaque permutation arrays.
- **Not eliminated:** finite **case distinctions**.
  There are still 109 explicit arithmetic identities
  with 1,123 interval boundaries to check. This is an
  elementary finite *mathematical* certificate, not a
  uniform closed-form construction valid for the
  whole middle interval without a table.
- [finite_endpoint_identity.py](finite_endpoint_identity.py)
  is an optional independent exact-integer audit of the
  asserted equalities; it is not logically required
  to interpret or verify the displayed proof.

Replacing the remaining finite table by a handful
of parameterized formulas is a separate, still-open
proof-compression problem.
