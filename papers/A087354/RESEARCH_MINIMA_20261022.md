# A087354 minimum-value research log (2026-10-22)

**Status:** exact computations and a finite counterexample to a proposed digit-length bound. **Not** a universal closed-form formula. This log is intentionally separate from `main.tex`, `minima.tex`, and both existing PDFs.

## Definition

Write `a(n)` for the **least perfect square** whose base-10 representation is a concatenation of exactly `n` positive perfect squares, with repetitions allowed. A block may contain a zero internally (e.g. 100) but may not have a leading zero.

## Exact new values

| n | exact a(n) | integer square root | digits | excess digits over n |
|---|---:|---:|---:|---:|
| 26 | 114491941251191919194194944 | 10700090712288 | 27 | 1 |
| 27 | 1494991191499944141414491136 | 38665115950944 | 28 | 1 |
| 28 | 14919999448111491414944114944 | 122147449617712 | 29 | 1 |
| 29 | 1111191491149991691191911414161 | 1054130680300119 | 31 | **2** |
| 30 | 1111194441113699414944949914441 | 1054132079539229 | 31 | 1 |
| 36 | 419994999149149944149149944191494441 | 648070211589107021 | 36 | 0 |

Each equality and square-block representation was checked using Python's exact `math.isqrt`. The minimum was established by exhaustive prefix-square interval branch-and-bound using integer arithmetic.

## Structural counterexample: n=29

For **n=29**, no 29-digit or 30-digit perfect square can be split into 29 positive square blocks. However,

```
1054130680300119^2 = 1111191491149991691191911414161
 = 1 | 1 | 1 | 1 | 1 | 9 | 1 | 4 | 9 | 1 |
   1 | 4 | 9 | 9 | 9 | 16 | 9 | 1 | 1 | 9 |
   1 | 9 | 1 | 1 | 4 | 1 | 4 | 16 | 1
```

contains exactly 29 positive square blocks. Exhaustion at length 31 excludes every smaller admissible square. Consequently,

```
a(29) = 1111191491149991691191911414161
decimal_length(a(29)) = 31 > 29+1.
```

Hence the conjectured universal bound `decimal_length(a(n)) <= n+1` is **false**. From the already known/certified values for n=1..28, n=29 is the first failure of this bound.

## Why the finite proof covers every possible competitor

Let `Q_d` be the set of positive squares with exactly `d` decimal digits. A word with `n` square blocks and `L=n+e` digits belongs to

```
union over (e_1,...,e_n >= 0, sum e_i=e)
       Q_(e_1+1) || ... || Q_(e_n+1).
```

For `e=0`, only `Q_1={1,4,9}` occurs.
For `e=1`, exactly one `Q_2={16,25,36,49,64,81}` block occurs.
For `e=2`, there are exactly two possibilities: two `Q_2` blocks, or one `Q_3` block (the 22 squares from 100 through 961). All remaining blocks are in `Q_1`. This is a complete classification by **total digit length**, not an assumption about typical witnesses.

For any word prefix `p` of `d` digits in a possible `L`-digit square, every completion lies in

```
[p*10^(L-d), (p+1)*10^(L-d)-1].
```

Prune this node only when the exact integer interval (restricted to the current verified witness upper bound) contains no integer square. The exact inequality is

```
isqrt(lower - 1) + 1 > isqrt(upper),  for lower > 0,
```

with `isqrt(0)=0` handling the root case. Thus **no admissible square is skipped**. Visiting all candidate block sequences up to each target bound proves minimality. The root estimate in the C++ implementation is corrected by integer multiplication before use, so this is not a floating-point proof.

## Reproduction

```sh
g++ -std=c++17 -O3 papers/A087354/verify_minima_extended.cpp -o /tmp/a087354_ext
/tmp/a087354_ext
```

The verifier also independently checks that each claimed value is a square and has an exact n-block partition. Existing verifiers for n=20..25 are unchanged.

## Remaining mathematical problem

This is **not** a formula for all n. In particular:
- The earlier experimental digit bound `<=n+1` cannot be used in an all-index proof.
- Fixed-excess block alphabets provide a rigorous general search reduction, but do not automatically supply an all-index formula.
- Future analytic attempts should target a provable infinite family of least values, a uniform nontrivial digit-length bound, or a structural characterization of missing-digit decimal squares. Distinguish rigorously proved statements from density heuristics.

No existing paper was revised and no OEIS entry was edited for this research step.


## Structural equivalence with OEIS A006716

Let `D(n)` denote the decimal digit length of `a(n)`.
Every eligible n-block word has at least n digits. Equality `D(n)=n`
holds if and only if **each block is one decimal digit**, necessarily
in `{1,4,9}`. Thus:

```
D(n)=n  <==>  there exists an n-digit perfect square using only 1,4,9.
```

This is exactly the length-existence question for
[OEIS A006716](https://oeis.org/A006716). That entry explicitly
conjectures, but does not prove, that its sequence is finite. Consequently,
even characterizing the indices at which `a(n)` has the theoretical
minimum n digits reaches a separate unresolved problem. This reduction
is **an equivalence**, not a proof of the conjecture.

As a further exact, independently exhausted result,

```
a(36) = 419994999149149944149149944191494441
      = 648070211589107021^2.
```

It is a 36-digit square with all digits in `{1,4,9}`, and its
minimality among all 36-block representations follows from enumerating
the complete 36-digit language `{1,4,9}^36` up to this square.
The numeric square was previously known as an entry of A006716;
**its identification as the exact A087354(36) is the additional
computational claim here**. The value also demonstrates that the
extra-digit phenomenon at n=29 does not persist for every larger n.

The `verify_minima_extended.cpp` program certifies this case as well.


## Further exact minima: n=31, 32, 33, 34

A second exhaustive search, using **exact square-root-interval cutoff**, determines four further terms:

| n | exact a(n) | exact square root | digits | excess |
|---|---:|---:|---:|---:|
| 31 | 49914994111911949994369194414144 | 7065054430923512 | 32 | 1 |
| 32 | 1111114494199449941144494641164944 | 33333384079619788 | 34 | **2** |
| 33 | 1144999199499994444141914194949136 | 33837836802904444 | 34 | 1 |
| 34 | 19144941911414919911419125114194449 | 138365248207109143 | 35 | 1 |

**Consequences.** For n=32, exhaustive search rules out *both* 32-digit and 33-digit concatenation squares, providing a second index (after n=29) with minimum digit surplus at least 2. The 34-digit witness above achieves the bound. All square identities and exact n-block partitions were checked separately using Python's `math.isqrt` and dynamic programming. The C++ root-interval program independently certifies the minima without probabilistic primality or floating-point decisions.

### Square-root-interval cutoff lemma

At any branch with a decimal prefix p of d digits and target total length L, cap the interval of possible completions to the current certified upper bound U:

```
A = p * 10^(L-d)
B = min((p+1)*10^(L-d)-1, U)
r_min = isqrt(A-1)+1  (or 0 for A=0)
r_max = isqrt(B).
```

If `A>B` or `r_min>r_max`, prune. If the interval contains only one or two candidate roots, **enumerate their full integer squares directly** and check the complete n-block partition by digit DP. There is no need to continue expanding the remaining block suffix. This is complete: every possible square extending p corresponds to one integer root in this exact closed interval.

The cutoff can always be applied by `d>=floor(L/2)+2`. Indeed, all L-digit square roots are at least `10^((L-1)/2)`; successive squares are separated by at least `2*10^((L-1)/2)+1`. At that depth, a prefix interval has width strictly smaller than this gap, so there is at most one square in the interval. The implementation also cuts off **earlier** whenever it detects at most two candidate roots.

This gives a deterministic fixed-surplus search. For `L=n+e` with fixed nonnegative integer e, at most e extra digits are distributed over n positive square blocks. There are only `O_e(n^e 3^d)` possible block-string prefixes of digit length d, since the 1-digit alphabet has size three and all longer block alternatives are bounded in number when e is fixed. Therefore the root-cutoff search visits at most `O_e(n^e 3^((n+e)/2+O(1)))` such prefixes, plus polynomial-time integer-root and membership checks. This replaces enumeration of approximately `3^n` complete one-digit block words by a square-root-level search. It is **not** a closed formula for the minima.

### Reproduce

```sh
g++ -std=c++17 -O3 papers/A087354/verify_minima_root_cutoff.cpp -o /tmp/a087354_roots
/tmp/a087354_roots
```

This verifier checks n=31 through n=34 in ascending length order, with each expected minimum serving only as a legitimate search upper bound. It excludes every smaller square, including all shorter lengths, and independently checks the asserted witness partitions. The GitHub Actions research workflow also runs the verifier.

**Still open:** There is no all-index closed formula for a(n), and neither the n-digit/n+1-digit existence pattern nor a sharp universal digit bound has been resolved. Existing paper files are intentionally unchanged.
