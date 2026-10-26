# A001292: cyclic concatenations and perfect powers

Kashihara's conjecture remains open. The [four-page manuscript](main.pdf)
proves a density-zero theorem and exact 3-adic formulas at complete digit
boundaries. Its source is [main.tex](main.tex).

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
python search_gmp.py 1000
```

The boundary verifier checks digit lengths `d=1..60000`, independent matrix
blocks, rational Taylor coefficients, and literal prefixes through `m=999999`.
[VERIFICATION.txt](VERIFICATION.txt) records the checks.

The earlier full search, `python search_gmp.py 5000`, covers all 12,502,499
nontrivial rotations with `m<=5000`, finding no perfect power.
[SEARCH_5000.json](SEARCH_5000.json) pins the unchanged search source and GMP version.
The search uses 64-bit Linux GMP through Python's standard `ctypes` module;
its [perfect-power predicate](https://gmplib.org/manual/Integer-Roots) tests all exponents.

The PDF and source hashes are recorded in [publication.json](publication.json).
