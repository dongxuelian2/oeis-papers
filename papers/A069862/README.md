# OEIS A069862: an all-index arithmetic minimum formula

**Authors:** Qichao Wang (Hebei University of Technology); Daoyu Dong / 董道豫 (University of Electronic Science and Technology of China).

## Proven theorems

For A069862, let a(n) be the **minimum** k for which n divides the decimal concatenation (n+1)||...||(n+k).

1. **For every n>=1, infinitely many lengths k work.** The self-contained prime-power lifting proof gives an explicit bound and a deterministic witness algorithm.
2. **The minimum itself has an exact finite arithmetic formula for every n.** Multiplicative orders, modular square roots, CRT and ceilings give explicit candidates in each digit interval; their finite minimum is a(n). The proof includes all smaller lengths and every digit-width transition.
3. For D = digits(n+1), if n divides 10^D, then **a(n)=n**. In particular a(10^r)=10^r for every integer r>=0.
4. For every j>=0 and n=(10^(6j+3)+1)/7, **a(n)=2n-1**. In particular a(143)=285.
5. If n>1 is an odd prime power, n divides 10^digits(n+1)-1, and 10^digits(n+1)>=2*n, then **a(n)=n-1**.

The uniform bound **a(n) < 10^n - n for n>=2** limits the formula to digit widths D through n. The lifting method extends the repository's A075002 proof, with the shifted-prefix 3-adic step proved explicitly.

## The all-index formula

Write n=R*m, with R=2^alpha*5^beta and gcd(m,10)=1. In a d-digit interval, put B=10^d, t=max(n,10^(d-1)-1), and let c be the prefix residue at t. The proof expresses c as a finite geometric sum of earlier complete digit intervals, so it requires no previous a-values or sequential prefix search.

Set h=ord_m(B), with h=1 for m=1; S(r)=(B^r-1)/(B-1), T(r)=(B^(r+1)-(r+1)*B+r)/(B-1)^2. For each phase j=0,...,h-1, the odd-part divisibility condition at offset j+h*z is exactly

\[
hS(h)z^2 + \bigl(2(t+j)S(h)+2T(h)-hS(h)\bigr)z
 +2\bigl(B^j c+tS(j)+T(j)\bigr)\equiv0\pmod m.
\]

The 2- and 5-part is the linear endpoint condition x=-B/(B-1) (mod R) after E=max(1,ceil(alpha/d),ceil(beta/d)) blocks. Here E<=4, so there are at most three exceptional endpoints per width. Each quadratic has at most 2^omega(m) compressed root classes; the proof explicitly handles zero polynomials and singular roots as well as simple roots.

CRT gives endpoint progressions x=x0+P*z. Their first endpoints in the stable part of the interval are

\[
X=x_0+P\left\lceil\frac{t+E-x_0}{P}\right\rceil.
\]

Keep only X<=10^d-1 and the valid exceptional endpoints. **a(n) is the minimum of these explicit candidates over d=D,...,n, minus n**; a(1)=1. All inputs, root-class formulas, and the proof of completeness appear in [minimum_formula.tex](minimum_formula.tex). An ASCII version is in [oeis_formula.txt](oeis_formula.txt).

This is a **finite arithmetic formula with a finite minimum**, not an elementary expression without minimization. It replaces the search through concatenation lengths with explicit arithmetic classes. [OEIS's Formula-field guidance](https://oeis.org/wiki/Style_Sheet#Formula) permits formulas for calculating terms and does not prescribe an elementary closed form; that guidance does not constitute editorial acceptance of this result.

For example, n=451 has no solutions anywhere in the 4- or 5-digit intervals. Its five classes in the 6-digit interval give first endpoints 100721, 101304, 101612, 101953, 102030; thus a(451)=100270. Run `python3 minimum_formula.py 451 --explain` to inspect every relevant interval.

## Existing work (not claimed as original)

The complete classification of n with a(n)=2 is equivalent to OEIS [A069860](https://oeis.org/A069860), whose formula was recorded by **David Wasserman in 2005**. The original draft had inadvertently treated that characterization as new; the revised article now credits the earlier work and excludes it from novelty claims.

## Reproducibility

- [main.tex](main.tex) — fully typeset mathematical paper.
- [main.pdf](main.pdf) — current seven-page article, rebuilt from the complete source on October 22, 2026 and visually checked on every page.
- [existence.tex](existence.tex) — self-contained all-index theorem, local shift lemmas and capacity bound.
- [minimum_formula.tex](minimum_formula.tex) — all-index minimum formula, explicit quadratic root classes, and proof of global minimality.
- [minimum_formula.py](minimum_formula.py) — direct evaluation of the arithmetic formula; no call to the orbit-search algorithm.
- [least.py](least.py) — separate exact minimum algorithm, used as an independent control.
- [verify_existence.py](verify_existence.py) — constructive witnesses and independent exact evaluation.
- [verify.py](verify.py) — exact-integer regression checks (finite checks are only corroborative).

Run `python3 verify.py`, `python3 verify_existence.py`, `python3 least.py --audit`, and `python3 minimum_formula.py --audit`. Compute any term with `python3 minimum_formula.py 37 451`.

Both the formula evaluator and the separate minimum algorithm agree with every entry in the [OEIS table for n=1..10000](https://oeis.org/A069862/b069862.txt), downloaded October 22, 2026 (SHA-256 `3ec25d25a94e401eb722ffaf92c878409afa8a330fb7f4fbe6867f524e628f0b`). Reproduce the formula comparison with `python3 minimum_formula.py --reference /path/to/b069862.txt`. The first 1000 outputs are also compared with direct, unskipped concatenation.

The formula audit exhausts **130,816 quadratic congruences** modulo every odd m<=31, then checks **2,331 higher-power/mixed-modulus cases**, including zero discriminants, common content and linear reductions. It verifies **144,000 arbitrary-state classifications** against direct transitions and **75 boundary sums** against independent binary affine composition. These controls cover absence of solutions and singular cases, not just successful witnesses.

The existence audit checks 12,510 direct recurrence cases, all n=1..250, and nine additional prime-power/mixed-modulus cases. All 259 constructed witnesses are independently recomputed by an exact geometric-derivative formula; the largest endpoint has 343 decimal digits. These finite checks validate the implementation, while the written proof establishes the universal claim.

Compile: pdflatex -interaction=nonstopmode -halt-on-error main.tex (twice).

## Suggested OEIS material, not yet posted

[oeis_formula.txt](oeis_formula.txt) gives the all-index formula in ASCII notation. The simpler family formulas remain valid: a(n)=n if n divides 10^digits(n+1), and a((10^(6j+3)+1)/7)=2*(10^(6j+3)+1)/7-1 for j>=0.

No claim of journal acceptance or exhaustive prior-art review is made.
