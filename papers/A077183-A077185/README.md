# A077183 and A077185: complete prime-divisibility conjecture proof

**Authors:** Qichao Wang (Hebei University of Technology); 董道豫 / Daoyu Dong (University of Electronic Science and Technology of China)
**Date:** October 17, 2026  
**Scope:** existence/nonexistence, not a formula for the least endpoint or quotient.

## Main conclusion

Let \(R(k)=k\Vert(k-1)\Vert\cdots\Vert2\Vert1\) (in decimal).
OEIS [A077183](https://oeis.org/A077183) gives the least \(k\) for which the \(n\)-th prime divides \(R(k)\), with a zero if none exists.
OEIS [A077185](https://oeis.org/A077185) gives the corresponding quotient \(R(k)/p_n\) and displays zero at excluded indices.

The 2005 OEIS conjecture is resolved:

\[
\boxed{\mathrm{A077183}(n)>0\iff n\notin\{1,3\}.}
\]

The two displayed zeros of A077185 occur exactly at \(n=1,3\); all other quotient terms are positive and well-defined. This does **not** supply a formula for the minimum in A077183 or the huge quotient terms in A077185.

## Stronger theorem in arbitrary bases

For **any base** \(b\ge2\) and **any prime** \(p\),

\[
\exists k\ge1:\ p\mid\bigl((k)_b\Vert(k-1)_b\Vert\cdots\Vert(1)_b\bigr)
\quad\Longleftrightarrow\quad p\nmid b.
\]

For each \(p\nmid b\), there are **infinitely many** such endpoints.

- If \(p\mid b\), all descending concatenations have residue 1 modulo \(p\), since they end in digit 1.
- If \(p\mid b-1\), then \(R_b(k)\equiv k(k+1)/2\pmod p\), so all \(k=2ps\) with \(s\ge1\) are witnesses.
- Otherwise let \(r=\operatorname{ord}_p(b)\), \(d=2r+1\), \(L=b^{2r}\), \(m_0=L-1\), and \(A=b^{D_b(m_0)}\pmod p\). All \(p\) candidate endpoints \(m_0+jr\) lie in one constant-width chamber. The key shift is

\[
R_b(m_0+jr)\equiv R_b(m_0)+j\,A\,r\,(b-1)^{-1}\pmod p.
\]

The slope is invertible, so choose

\[
j\equiv -R_b(m_0)\bigl(A\,r\,(b-1)^{-1}\bigr)^{-1}\pmod p.
\]

That gives an explicit witness satisfying

\[
k\le b^{2r}-1+(p-1)r<b^{2r+1}.
\]

## Reproducibility files

- **[main.pdf](main.pdf)** — compiled **two-page mathematical paper**, committed alongside the source.
- **[main.tex](main.tex)** — self-contained LaTeX paper using standard packages and the extarticle class.
- **[verify.py](verify.py)** — independent tests of known values and arbitrary-base witnesses, with no third-party Python packages.

Run the verification script, then compile main.tex twice with pdflatex to reproduce the paper.

**Numerical checks:**

- **63/63** published A077183 minimum endpoints verified by incremental brute force.
- **12/12** A077185 quotient values checked using literal decimal concatenations.
- **198** constructive witnesses tested in bases \(2,3,4,5,7,10,12,16\) for primes up to 101 that do not divide the base.
- Literal digit strings, independent recurrence, and modular block-sum calculations agree.

Finite checks supplement, but do not replace, the proof.

## Literature and priority

- [OEIS A077183](https://oeis.org/A077183), conjecture by Ryan Propper, July 29, 2005.
- [OEIS A077185](https://oeis.org/A077185), quotient sequence.
- [OEIS A000422](https://oeis.org/A000422), reverse concatenated integers.
- R. Stephan, *Factors and Primes in Two Smarandache Sequences*, Smarandache Notions Journal **9** (1998), 4–10 (linked from A077183).

The claimed proof is submitted for code/math review. No journal, referee or OEIS editor acceptance is asserted; publication novelty still requires literature vetting.

## Suggested OEIS comments (not yet submitted)

**A077183:** For every n >= 1, a(n) = 0 if and only if n = 1 or 3. For every prime p not dividing 10, there are infinitely many k for which k||(k-1)||...||1 is divisible by p. More generally, for every integer base b >= 2, such a k exists if and only if p does not divide b. Constructive proof: Q. Wang (2026), [link to paper].

**A077185:** The zero terms occur exactly at n = 1,3. For all other n, the minimum k = A077183(n) exists, so a(n) = A000422(k)/prime(n) is a well-defined positive integer. Proof: Q. Wang (2026), [link to paper].
