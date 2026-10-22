# A006716 research: repeated square blocks and modular local–global obstruction

**Status (2026-10-22):** a rigorous classification of an infinite family, obtained as an application of Ljunggren's **existing** theorem; a complementary elementary theorem about modular quadratic residues. This is research material, **not** a claim to have proved the finiteness of [A006716](https://oeis.org/A006716), and not an assertion of publication priority.

## Definition and relation to A087354

A006716 is the sequence of positive integer squares whose decimal digits all belong to `{1,4,9}`. The OEIS comment that the sequence is *probably finite* is an **unproved conjecture**. Every A006716 value having n digits also supplies an n-block all-one-digit representation relevant to the minimum digit length in A087354.

## 1. Rigorous exclusion of all repeated-square-block constructions

**Theorem 1 (no exact repetition).** Let `A=t^2>0` have exactly `d>=1` decimal digits. Write `W_k` for the integer formed by concatenating k copies of A:

```
B = 10^d,
W_k = A*(1+B+...+B^(k-1)) = t^2*(B^k-1)/(B-1).
```

Then `W_k` is a perfect square **if and only if** `k=1`.

**Proof.** If `W_k` is square, then so is the integer `(B^k-1)/(B-1)` (multiplying a positive integer by an integer square cannot change the parity of its prime exponents). For `k=2`, this integer equals `10^d+1 ≡ 2 (mod 3)`, hence is not a square. For `k>=3`, the 1943 theorem of Wilhelm Ljunggren classifies all positive-integer solutions to

```
(x^k-1)/(x-1) = y^2,   x>1, k>2:
(x,k,y)=(3,5,11) or (7,4,20).
```

Because `x=B=10^d>=10`, neither exceptional case applies. This establishes the claim. □

The theorem is a **corollary of published mathematics**, not a newly proved result about the general Nagell–Ljunggren equation. For example, `441=21^2` but `441441`, `441441441` and every further repetition of the block `441` are never integer squares.

**Reference:** N. Saradha and T. N. Shorey, *The equation (x^n−1)/(x−1)=y^q with x square*, Mathematical Proceedings of the Cambridge Philosophical Society **125** (1999), 1–19, doi: [10.1017/S0305004198002564](https://doi.org/10.1017/S0305004198002564), introduction recalling Ljunggren's 1943 `q=2` classification. This source is cited for the theorem, not for novelty of this particular corollary.

## 2. A strong finite-modulus illusion

**Theorem 2 (arbitrarily long nonsquares passing any fixed modular square sieve).** Suppose additionally that A is a d-digit positive square with `d>=3`, and use `W_k` above. Then:

1. For **every** `k>=1` and every `a,b>=0`, `W_k` is a square modulo `2^a*5^b`.
2. For **every** positive integer `M`, there are **infinitely many** k (indeed an explicit arithmetic progression) such that `W_k` is a square modulo M.
3. Nevertheless **none** of these `W_k` for `k>=2` is an integer square, by Theorem 1.

**Proof.** The geometric factor `S_k = 1+B+...+B^(k-1)` satisfies `S_k ≡ 1 (mod 8)` because `8|B=10^d` when d>=3, and `S_k ≡ 1 (mod 5)` because `5|B`. Every odd integer congruent to 1 modulo 8 is a square modulo each power of 2; every 5-adic unit congruent to 1 modulo 5 is a square modulo each power of 5 (via standard Hensel lifting). Hence `S_k`, and therefore `W_k=A*S_k`, is a square modulo `2^a*5^b` for all k.

For arbitrary M, let `m=M/(2^v2(M)*5^v5(M))`, so `gcd(m,10)=1`. Put

```
T = phi((B-1)*m),
k = j*T  (j = 1,2,3,...).
```

Euler's theorem applies because `gcd(B,(B-1)*m)=1`, so `B^k ≡ 1 (mod (B-1)*m)`. Therefore the integer quotient `S_k=(B^k-1)/(B-1)` is divisible by m, and `W_k ≡ 0 (mod m)`, a square residue. Combine with the already-proved 2- and 5-primary square residues using CRT. Since there are infinitely many positive multiples of T, (2) follows. Statement (3) is Theorem 1. □

**Interpretation.** Even a sieve built from any preselected finite family of moduli cannot eliminate all sufficiently long repetitions of a 3-or-more-digit square block. Taking the product of the moduli and applying Theorem 2 supplies arbitrarily long actual nonsquare decimal words which pass **all** those modular quadratic-residue tests simultaneously.

This is *not* an argument that A006716 is infinite: passing all tests modulo a **fixed** integer M does not imply that a given integer is an actual square. The modulus is not allowed to grow with the repetition count in this assertion.

### A concrete A006716 example

Take `A=441=21^2`, so `B=1000`:

```
W_k = 441441...441 (k repeated 441-blocks)
    = 441*(1000^k-1)/999.
```

Every W_k uses exclusively digits 1 and 4, and every k>=2 is **not** an integer square; nevertheless, for every prescribed modulus M an infinite progression of these W_k are quadratic residues modulo M.

The corresponding infinite 10-adic periodic word has limit

```
sum_(j>=0) 441*1000^j = -441/999 = -49/111   in Z_10.
```

It is a 2-adic square since `-49/111 ≡ 1 (mod 8)`, and a 5-adic square since `-49/111 ≡ 1 (mod 5)`. This is another description of the persistent local square-residue phenomenon, not an ordinary real-valued square identity.

## 3. Elementary local constraints, relevant for future searches

- If a positive square uses only digits **1 and 9**, it is either 1 or 9. For a word of length >=3, all these digits are 1 mod 8 and its final three digits contribute `4+2+1 ≡ 7 (mod 8)`, which is not a square residue. For length two, all four possibilities are `3 (mod 8)`, also not square residues.
- For any A006716 square of length >=3, its final three digits must be one of `144,441,444,449,944`. This follows by enumerating the 27 allowed three-digit tails against quadratic residues modulo 1000. It is only a **necessary** condition, not a list of actual three-digit squares.

## 4. Research decision

We have **not** established a new A006716 term, a finiteness theorem, or a formula for A087354. The repeated-block approach is mathematically **closed off** by Ljunggren's theorem. At the same time, Theorem 2 shows why searches relying on a fixed finite set of quadratic-residue moduli are intrinsically incomplete as a way to prove finiteness.

Further progress must exploit information that changes with digit length (for example, unbounded moduli, global size constraints, or genuinely nonperiodic digit patterns) rather than repeating an existing square block.

## Independent finite audit

Run:

```sh
python papers/A006716/verify_repetition.py
```

This script verifies selected perfect-square seeds and repetition counts, checks the modular construction for M up to 350, and independently derives the five allowed length-three suffixes. The symbolic proof of Theorem 1 depends on Ljunggren's cited theorem; finite tests are not substituted for it.


## Further result: uniform length coverage beyond periodic words

A separate [local-sieve barrier note](LOCAL_SIEVE_BARRIER.md) proves a stronger result: **for every fixed modulus M and every sufficiently large length n**, there are exponentially many n-digit words over `{1,4,9}` ending in `441` and square modulo M, with no fixed-block periodicity restriction. An exact classification also shows that precisely `2*3^(n-3)` odd-ending n-digit digit-set words are square modulo `10^n`, with eight roots each. Independent tests are in [verify_local_sieve.py](verify_local_sieve.py). Neither result establishes the existence of new ordinary integer squares or resolves A006716's finiteness conjecture.


## Global root sparsity and complete bounded-support certificate

A separate [sparse-root theorem and classification](SPARSE_ROOTS.md)
moves beyond modular necessary conditions. Two elementary **integer-square**
gap lemmas show that any root with `r` nonzero decimal digits and a square
containing no zero digit has nonzero positions
`0=e_1<...<e_r` satisfying `e_(j+1)<=2*e_j+2`, with an additional
bound `e_r<=e_(r-1)+3` at the top. A digit-sum inequality also gives
`digits(x^2)<=81*r^2`.

Using **exact arbitrary-precision arithmetic** and only these sound
pruning rules, [verify_sparse_roots.cpp](verify_sparse_roots.cpp)
completely classifies A006716 square roots with **at most 12**
nonzero decimal digits, without placing an artificial numerical
size bound on the root. Precisely 16 roots occur (all previously known
OEIS terms), and no roots occur at support 4, 8, 10, 11, or 12.
The final support-12 level tests 23,707,917 candidate roots.
An [independent Python audit](verify_sparse_roots.py) checks the
elementary lemmas and exhausts support at most 4.

This **does not** prove A006716 finite: the largest currently recorded
square has a root with 14 nonzero digits. No OEIS edit or manuscript
change is made here.


## Updated global sparse-root boundary: full support 14

The [exact leading-pair interval theorem and support-14 classification](LEADING_PAIRS_AND_SUPPORT14.md)
extends the global finite certificate from 13 to **14 nonzero digits in the square root**.
[Independent rational-table verification](verify_leading_pairs.py) shows that
if the top two nonzero root digits have a position gap of three, the digits
must be `7,7` or `7,8`; all other possibilities are excluded by
the first six significant digits of the square. This upper-prefix condition
is used **only at the final root-digit insertion**.

Six complete [arbitrary-precision root searches](verify_sparse_roots_14.cpp),
partitioned by root units digit, inspect **77,043,158 final candidate roots**
and find exactly **one** 14-sparse solution,
`648070211589107021`, already present in OEIS A027675.
Together with the previously certified support <=13 cases, this completely
classifies all A006716 roots with **at most 14 nonzero digits**:
the **17 presently listed OEIS roots, and no others in this structural class**.
The problem for support >=15, and the full finiteness conjecture, remain open.

## Support 15 and the top-three high-gap theorem

A dedicated [research supplement](SUPPORT15_TOP_THREE.md) fully excludes all A006716 roots with **exactly 15 nonzero decimal digits**, via **297,161,668** exact-integer terminal checks over six root units digits. Coupled with the earlier support <=14 theorem, the complete bounded-support classification through **r=15** contains exactly the same 17 previously recorded roots. The same note proves a new **global restriction on the highest three nonzero root-digit positions** and supplies an [independent exact eight-digit-prefix proof audit](verify_top_three_gaps.py). Root support >=16 and the global finiteness conjecture are not resolved by this result.

## Support 16 and the exact leading-triple mask

The latest [complete support-16 research note](SUPPORT16.md) and [reproducible six-shard verifier](verify_sparse_roots_16.cpp) exhaust all roots with 16 nonzero decimal digits, finding no solutions among **268,308,611** final candidates. With all lower supports, this is a complete classification of **every** A006716 root with **at most 16 nonzero digits**: the **17 known roots**, and no others in that structural class. The high-three-digit mask is generated from exact eight-digit leading-square intervals, independently checked by [verify_top_three_gaps.py](verify_top_three_gaps.py), and applied one layer earlier when no completion exists. This does not prove global finiteness; hypothetical further roots must have >=17 nonzero digits.


## Universal upper-span gap lemma (new)

The separate [high-to-low gap theorem](GLOBAL_HIGH_GAP.md) proves a
support-independent constraint for **every zero-free decimal square**:
if the nonzero root positions decrease as `e1>e2>...>er`, then
`e_j-e_(j+1) <= e1-e_j+3` for every `2<=j<r`;
if the highest root digit belongs to `{1,2,3}`, improve `+3` to
`+2`. The proof is an elementary size comparison showing that
otherwise the digit at position `2e_j-1` of the square must be zero.
Coupled with the previously certified highest-three-gap table, this
bounds the *fourth highest gap* by **9** for any A006716 square
with at least four nonzero root digits. It is an all-length necessary
condition, not a proof of finiteness. Its [finite regression audit](verify_high_gap.py)
passed in [GitHub Actions](https://github.com/dongxuelian2/oeis-papers/actions/runs/39765056417).

## Support 17 and the global fourth-gap theorem

The new [SUPPORT17.md](SUPPORT17.md) provides an exact-integer six-way certificate that **no** A006716 square root has exactly **17** nonzero decimal digits, after **1,034,989,170** terminal checks. Together with all smaller supports, this completely classifies roots with **at most 17 nonzero digits**: only the 17 already known. Independent mathematics in [GLOBAL_HIGH_GAP.md](GLOBAL_HIGH_GAP.md) and [TOP_FOUR_GAP.md](TOP_FOUR_GAP.md) proves that the *fourth-highest nonzero root-digit gap is at most seven* for every A006716 root, and gives a general descending-root-gap bound. The [independent ten-digit-prefix check](verify_top_four_gaps.py) passed GitHub CI. The entire A006716 finiteness conjecture is still unresolved.


## Fifth and sixth highest nonzero root gaps

The new [top-five theorem](TOP_FIVE_GAP.md), verified by an independent
[14-digit exact-prefix audit](https://github.com/dongxuelian2/oeis-papers/actions/runs/39770128066),
proves that **the fifth-highest nonzero root-digit gap is at most 5**
for *every* A006716 root with at least five nonzero digits.

The subsequent [top-six theorem](TOP_SIX_GAP.md), independently verified by a
[16-digit exact-prefix audit](https://github.com/dongxuelian2/oeis-papers/actions/runs/39770626224),
proves that the sixth-highest gap is **at most 6**. They sharpen
the general upper-span recurrence to `d_j<=27*2^(j-6)` for j>=6,
independent of root size or total support count.

The exact [support-18 search](verify_sparse_roots_18.cpp)
uses four-digit leading-root masks and is separately audited in
[GitHub Actions](https://github.com/dongxuelian2/oeis-papers/actions/runs/39769301304).
Until every units-digit branch completes, no r=18 classification is claimed.
