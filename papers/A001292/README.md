# A001292: cyclic concatenations and perfect powers

Kashihara's conjecture remains open. The [manuscript](main.pdf) proves a
density-zero theorem and exact local obstructions at complete digit boundaries.
Its source is [main.tex](main.tex).

The local lifting extends to **every `d`-digit integer `m`**. If
`r=ord_p(10)`, `r|P`, `10^P=1 (mod 9r)`, `p` does not divide `P`, and
`P|d`, set `a=v_p(d)` and `C=W_(10^P-1) mod p`. Every rotation satisfies

\[
R_{m,k}\equiv10^{D(k)}\left(\frac{m(m+1)}2+C\frac dP\right)
\pmod{p^{a+1}}.
\]

The formula allows `C=0`. When `Pp|d`, exactly `2(p-1)` classes of `m mod p^2`
give valuation one at `p` for every rotation. In particular, for `d=111u`,
all rotations are excluded if `m=0,-1 (mod 37)` except the two classes
`m=296u,1073u-1 (mod 1369)`: **72 classes modulo 1369**.
Another infinite family is `d=3 (mod 111)`, `m=126 (mod 999)`, with `m`
in the indicated digit interval; it combines exact valuation 2 at 3 with
a nonsquare character at 37.

For every positive `epsilon`, there is an arithmetic progression of digit
lengths such that, in every sufficiently large corresponding digit interval,
at least a fraction `1-epsilon` of the integers `m` have **no powerful value
among any of their rotations**. The proof combines the independent
valuation-one classes with the divergent reciprocal sum of primes
`p=3 (mod 40)` from Dirichlet's theorem. The fraction counts whole rotation
blocks indexed by `m` inside those digit intervals.

For a set of positive digit lengths `d` of lower natural density at least
**95.53273407...%**, every rotation at `m=10^d-1`
is not a nontrivial perfect power. This is a density among digit lengths `d`.
The proof combines exact 3-adic restrictions with affine residue formulas
at the primes 37, 333667, 757, and 440334654777631, together with
fifth- and seventh-power families.

Every rotation at `m=10^d-1` is excluded for **all `d=1..27`, and for
`d=54,243`**. These are complete boundary blocks, each with `10^d-1`
rotations. The proof combines the valuation formula below with six finite
moduli. [Exact certificates](BOUNDARY_CHARACTERS.json) include complete
Lucas primality proofs and the modular residues.

Each character certificate extends to an infinite arithmetic progression.
Examples are

\[
d\equiv12,15\pmod{333},\qquad
d\equiv27\pmod{37249072371},\qquad
d\equiv243\pmod{25475666076}.
\]

The fifth- and seventh-power families have exact local criteria, including
parameters divisible by the testing prime. For `(p,e)=(440334654777631,5)`
at `d=27u`, or `(p,e)=(757,7)` at `d=243u`, write `u=p^a t` with `p` not
dividing `t`. Every rotation is an `e`th power over the `p`-adic field
exactly when `e` divides `a` and `t^((p-1)/e)=1 (mod p)`. If `3` does not
divide `u`, failure of either condition excludes every integer perfect power.

A general lifting theorem supplies the exact valuation behind these criteria.
Let `p>=7` be prime, `r=ord_p(10)`, and choose `P` with `r|P`, `10^P=1 (mod 9r)`, `p` not
dividing `P`, and `C=W_(10^P-1)` nonzero modulo `p`. For every `P|d` and
`a=v_p(d)`, all rotations satisfy

\[
v_p(R)=a,\qquad R/p^a\equiv10^{D(k)}C\frac{d}{Pp^a}\pmod p.
\]

All six certified primes satisfy these hypotheses. Their pairs `(p,P)` are
`(37,3)`, `(757,27)`, `(333667,9)`, `(440334654777631,27)`, `(1527791,903)`,
and `(43037,812)`. Thus `d=Ppt`, with `p` not dividing `t`, excludes an
entire rotation block. For example, at `d=327024` the valuations at 3 and
757 are 5 and 1, so no perfect-power exponent is possible.

For the first `N` sequence entries, the number of nontrivial perfect powers is

\[
O\!\left(\frac{N(\log\log N)^2}{\log N}\right).
\]

The same estimate holds for powerful values, in every fixed integer base.
The [sieve companion](POWERFUL_SIEVE.md) gives a Markdown version of this argument.

For `m=10^d-1`, write `h=v_3(d)` and `u=d/3^h`. Every whole-block rotation `R` has

\[
v_3(R)=h+2,\qquad R/3^{h+2}\equiv u(2+6d)\pmod9.
\]

If the prime divisors of `h+2` form the set in the left column, the right
column excludes every nontrivial perfect power in the entire rotation block:

| Prime divisors of `h+2` | Excluded classes of `u` |
| --- | --- |
| `{2}` | `u=1 (mod 3)` |
| `{3}` | `u=1,2,7,8 (mod 9)` |
| `{2,3}` | `u=1,7 (mod 9)` |

In particular, every `d=3,6,9,21,24 (mod 27)` is excluded, as is `d=81`.
Examples of whole rotation blocks are `m=10^6-1, 10^9-1, 10^81-1`.

For `(p,s)=(37,3)` or `(333667,9)`, the residue of `W_(10^d-1)` is affine
in `floor(d/s)` on each fixed class `d mod s`. If `s` divides `d`, every
rotation also satisfies

\[
v_p(R)=v_p(d),\qquad
R/p^{v_p(d)}\equiv10^{D(k)}C_s\frac{d}{s p^{v_p(d)}}\pmod p,
\]

where `k` is the cut after an entire integer block, `D(k)` is its digit
length, `C_3=33 (mod 37)`, and `C_9=221885 (mod 333667)`.
In particular, the whole block is excluded for `d=111t` with `37` not dividing
`t`, and for `d=3003003t` with `333667` not dividing `t`.
The unit obstructions also exclude `d=2,12,15,18`.

Earlier [residue exclusions](RESIDUE_EXCLUSIONS.md) treat mod-27 classes
and a mod-13 infinite family. The [boundary equations](STRUCTURE.md)
retain the exact rotation and give necessary continued-fraction conditions.

## Checks

Run from this directory:

```sh
python verify_a001292.py
python verify_structure.py
python verify_powerful_sieve.py
python verify_boundary_valuations.py
python verify_local_primes.py
python verify_boundary_characters.py
python verify_general_boundary_primes.py
python verify_digit_intervals.py
python search_gmp.py 1000
```

The boundary verifier checks digit lengths `d=1..60000`, independent matrix
blocks, rational Taylor coefficients, and literal prefixes through `m=999999`.
The character verifier checks all finite certificates by both a closed block
formula and matrix concatenation, the period hypotheses, the two linear
families, 2,205 literal rotation characters, and the exact density bound.
The general-prime verifier compares complete blocks with independent matrix
words for all six primes, audits the local criteria at positive valuations,
and directly iterates `d=1..327024` at 757. Newton checks through valuation 8
use the proved coefficient bound and are recorded separately.
The digit-interval verifier checks literal rotations, independent prefixes
and interval endpoints at three primes, complete valuation-one class counts,
and all 2,531,281 classes of a two-prime CRT modulus.
[VERIFICATION.txt](VERIFICATION.txt) records the checks.

The local-prime verifier compares geometric block sums with matrix powers,
literal rotation residues, and Newton sums from the proved interpolation.
`python verify_local_primes.py --extended` directly iterates through
`d=3003003` at the prime 333667, reaching its first positive valuation.

The earlier full search, `python search_gmp.py 5000`, covers all 12,502,499
nontrivial rotations with `m<=5000`, finding no perfect power.
[SEARCH_5000.json](SEARCH_5000.json) pins the unchanged search source and GMP version.
The search uses 64-bit Linux GMP through Python's standard `ctypes` module;
its [perfect-power predicate](https://gmplib.org/manual/Integer-Roots) tests all exponents.

The PDF and source hashes are recorded in [publication.json](publication.json).
