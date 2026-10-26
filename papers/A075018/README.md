# OEIS A075018: universal existence and an even-base permutation theorem

**Authors:** Qichao Wang (Hebei University of Technology); 董道豫 / Daoyu Dong (University of Electronic Science and Technology of China)
**Date:** October 17, 2026  
**Scope:** rigorous universal existence theorem plus exact minima and complete witness classification for an infinite family of indices; no all-index least-value formula is claimed.

## Main result

[OEIS A075018](https://oeis.org/A075018) defines a(n) to be the smallest integer k such that the decimal concatenation of k, k-1, k-2, k-3 is divisible by n, or zero when no k exists.

We prove:

\[
\boxed{\mathrm{A075018}(n)>0\quad\text{for every }n\ge1.}
\]

In fact, infinitely many four-block descending concatenations are divisible by any fixed n.

The stronger main theorem states: for every **even base b**, every integer modulus **N >= 1**, every number of blocks **t >= 1**, and **any prescribed permutation** of t consecutive positive integers, there are infinitely many equal-width block concatenations divisible by N.

Crucially, **N and t are independent**. This extends the setting of the prior [even-base arithmetic-progression theorem](../A075000-A075002/) (in which the modulus equals the block count). Literature priority of the stronger result has not been established.

## Exact least values for infinitely many indices

For every integer `r >= 2` and every positive divisor `d` of `30`,

```
A075018(d*10^r) = d*10^r + 3.
```

More strongly, for every `k >= 4`, the four-block descending concatenation
`k||(k-1)||(k-2)||(k-3)` is divisible by `d*10^r` **if and only if**
`k ≡ 3 (mod d*10^r)`. The exceptional starting point `k=3`
gives 3210, which is not divisible by 100.

**Proof idea:** Divisibility by `10^r` forces the positive final block
`k-3=t*10^r`. Splitting off the final block gives
`C(k)/10^r = 10^digits(t) * U(k) + t`, where
`U(k)=k||(k-1)||(k-2)`. The first summand is 0 modulo 2 and 5;
it is also 0 modulo 3 because `U(k) ≡ k+(k-1)+(k-2) ≡ 0 (mod 3)`.
Since `d` is a squarefree divisor of 30, divisibility by `d`
is equivalent to `d|t`, proving both directions and minimality.

Examples: `A075018(100)=103`, `A075018(300)=303`,
`A075018(1500)=1503`, `A075018(3000)=3003`.
The theorem covers an infinite subsequence but not a full closed form
for arbitrary moduli. A standalone exact modular verification script is
included in `verify_minima.py`.

## Explicit four-block construction

Write n=qm with q=2^v2(n) * 5^v5(n) and gcd(m,10)=1. By the Chinese remainder theorem, choose a congruent to 0 modulo q and congruent to -6 * inverse(4) modulo m. Select any sufficiently large digit width d with

\[
q\mid10^d,\qquad10^d\equiv1\pmod m,\qquad9\cdot10^{d-1}\ge n+3.
\]

Choose a in the specified residue class within the common digit-length window, then k=a+3 is a valid witness. Indeed the concatenation C=(a+3)||(a+2)||(a+1)||a obeys

\[
C\equiv a=0\pmod q,\quad C\equiv4a+6=0\pmod m.
\]

The full proof covers the general arbitrary-permutation case.

## Repository contents

- **[main.pdf](main.pdf)**: compiled mathematical paper, including the exact-minimum theorem (regenerated for both authors).
- **[main.tex](main.tex)**: editable LaTeX source.
- **[verify.py](verify.py)**: dependency-free Python verification and reproducible witnesses.

To reproduce:

~~~sh
python verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

### Numerical audit

- **65/65** published terms in [A075018 b-file](https://oeis.org/A075018/b075018.txt) match direct brute-force minimum search.
- **600/600** descending four-block witnesses constructed for n=1,...,600.
- **6720/6720** combinations of seven even bases, 80 moduli, twelve block lengths, and seeded random block permutations pass; an independent literal-integer check is used whenever feasible.

These finite checks are supplements; the theorem itself is unconditional.

## Source and OEIS comment

OEIS A075018 does not currently record an all-index positivity proof. A concise proposed COMMENT (not submitted):

> For every n >= 1, a(n) > 0. In fact, infinitely many concatenations of four consecutive positive integers in decreasing order are divisible by n. More generally, for any even base b, any positive integers t and N, and any fixed permutation of t consecutive positive integers, there exist infinitely many equal-width block concatenations divisible by N. Proof: Q. Wang (2026), https://github.com/dongxuelian2/oeis-papers/tree/main/papers/A075018 .

Other reference: F. Luca and B. Teguia Tabuguia, *Concatenations of terms of an arithmetic progression*, JDEA 32 (2026), 437--456, doi:10.1080/10236198.2025.2603385.

**No OEIS edits or claims of external peer-review acceptance are made by this PR.**
