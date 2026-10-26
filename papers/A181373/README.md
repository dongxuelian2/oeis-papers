# A181373: circular Champernowne divisibility

**Author:** Qichao Wang (Hebei University of Technology)  
**Date:** 2026-10-16  
**Status:** A constructive proof is presented for review; not yet independently refereed or submitted to OEIS.

## Result

Let \(C(m)=1\Vert 2\Vert\cdots\Vert m\) denote the decimal concatenation of the first \(m\) positive integers, and let \(D(m)\) be its total number of digits. For every prime \(p\notin\{2,5\}\) there are **infinitely many** \(m\) such that \(p\mid C(m)\) and \(p\) divides every cyclic **digit** rotation of \(C(m)\). For \(p=2,5\), no such \(m\) exists. Therefore

\[
  \mathrm{A181373}(n)>0\quad\Longleftrightarrow\quad n\notin\{1,3\}.
\]

For every prime \(p\ge7\), the proof supplies

\[
  m\le 10^{p-1}+p(p-1)-1.
\]

It also proves the bound \(m\le 10^{2r}+pr-1\), where \(r=\operatorname{ord}_p(10)\). These are constructive **existence** bounds, not formulas for the least \(m\).

## Explicit witness constructions

**Fermat construction:** Put \(r=p-1\), \(d=p\), \(L=10^{p-1}\), \(H=D(L-1)\). Choose \(0\le\delta<r\) with \(\delta\equiv-H-1\pmod r\), set \(m_0=L+\delta\), and choose

\[
j\equiv-9C(m_0)\pmod p,\qquad 0\le j<p.
\]

Then \(m=m_0+jr\) is a witness.

**Order-sensitive construction:** Put \(r=\operatorname{ord}_p(10)\), \(d=2r+1\), \(L=10^{2r}\), \(H=D(L-1)\), and again take \(m_0=L+\delta\), where \(\delta\equiv-H-1\pmod r\) and \(0\le\delta<r\). **Now the correct choice is different:**

\[
\boxed{j\equiv 9r^{-1}C(m_0)\pmod p,\qquad 0\le j<p,}
\]

where \(r^{-1}\) is the inverse of \(r\) modulo \(p\). Then \(m=m_0+jr\) is a witness. The main identity behind both constructions is

\[
  C(m+r)-C(m)\equiv-r\,9^{-1}\pmod p
\]

inside a constant-digit-length block, when \(10^r\equiv1\pmod p\) and \(d\equiv1\pmod r\).

**Important:** The Fermat formula for \(j\) must **not** be reused unchanged in the order-sensitive construction unless \(r=p-1\). The paper includes both formulas explicitly following independent review.

## Files and validation

- [main.tex](main.tex): self-contained LaTeX paper with complete proof and references.
- [verify.py](verify.py): independent modular prefix evaluator, published-term cross-check, Fermat witnesses, and order-sensitive witness checks.
- [Compiled paper PDF (main.pdf)](main.pdf): complete typeset proof tracked in GitHub.
- Compile locally with pdflatex if you want to reproduce the PDF.

Reproduce by running Python verification, followed by pdflatex twice on main.tex.

The checks include 12 published OEIS minima and the Fermat witness construction for **23 primes**, \(7\le p\le101\). The explicit enumeration of all \(p\) distinct candidate residues is tested only for the subset \(p\le67\); for larger checked primes, the script verifies the constructed witness and digit-length condition. Additional order-sensitive checks test \(p=7,11,13,17,37,101\), including cases where reusing the Fermat formula would fail.

Finite checks are not substitutes for the mathematical proof. The global existence theorem is unconditional; no closed formula for each minimum is claimed.

## References

- [A181373](https://oeis.org/A181373), [A007908](https://oeis.org/A007908), [A058183](https://oeis.org/A058183).
- [Ripà and Dalmasso (2012)](https://nntdm.net/volume-18-2012/number-1/29-48/), *Patterns related to the Smarandache circular sequence primality problem*.
- [Ripà (2025)](https://doi.org/10.5281/zenodo.17382562), a subsequent note on modular patterns.
- [Earlier OEIS paper](../A075000-A075002/), addressing distinct divisibility questions.
