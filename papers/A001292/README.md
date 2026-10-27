# A001292: cyclic concatenations and perfect powers

Kashihara's conjecture remains open. The [manuscript](main.pdf) proves a
density-zero theorem and exact local obstructions at complete digit boundaries.
Its source is [main.tex](main.tex).

For a set of positive digit lengths `d` of lower natural density at least
**286397396/333333333 = 85.91921888...%**, every rotation at `m=10^d-1`
is not a nontrivial perfect power. This is a density among digit lengths `d`.
The proof combines exact 3-adic restrictions with affine residue formulas
at the primes 37 and 333667.

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
python search_gmp.py 1000
```

The boundary verifier checks digit lengths `d=1..60000`, independent matrix
blocks, rational Taylor coefficients, and literal prefixes through `m=999999`.
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
