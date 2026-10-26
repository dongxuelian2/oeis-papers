# A248520 and A248521: exact cotangent counts and both density conjectures

Write `F(k)=floor(cot(pi/(2k)))`. Its consecutive differences are always 0 or 1.
The [paper](main.pdf) proves the two asymptotic conjectures on the official pages,
with the stronger bounded additive errors:

- [A248521](https://oeis.org/A248521): `a_1(n)=pi*n/2+O(1)`.
- [A248520](https://oeis.org/A248520): `a_0(n)=pi*n/(pi-2)+O(1)`.

The exact counts through N are `F(N+1)` and `N-F(N+1)`, respectively.
Every term is determined by these formulas:

```
a_1(n) = ceil(pi/(2*atan(1/n))) - 1
beta = 1 - 2/pi
L = floor((n-1)/beta) + 1
U = floor(n/beta)
a_0(n) = min {k in [L,U]: k-F(k+1)=n}.
```

The interval [L,U] contains at most three integers. The second formula explicitly
retains this finite minimum; neither formula relies on earlier sequence terms.

Run `python3 papers/A248520-A248521/verify.py`. Standard-library rational interval
arithmetic certifies every floor and ceiling using Machin's identity and
alternating Taylor bounds. Checks cover 471 official A248520 terms, 469 official
A248521 terms, direct cotangent differences through position 3000, both exact
counting functions and term formulas, and boundary tests up to index `10^30+57`.
The stored files are clearly marked prefixes of the official 10000-term b-files.
Universal claims follow from the paper proofs, not these finite checks.

`oeis.txt` is a proposed update, not an accepted or submitted OEIS entry edit.
