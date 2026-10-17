# A077187 — unrestricted-order drift dichotomy (research continuation)

**Status: PROVED intermediate lemmas, NOT the all-primes conjecture.**
Continuation of \`research/finite_defect_transfer_2026-10-17.md\`. This note does not change the class-specific theorem in \`main.tex\`.

## General period

For each prime \(p\ge7\), \(p\ne11\), let \(r=\operatorname{ord}_p(10)\), write \(r=2^a5^cv\) with \(\gcd(v,10)=1\), and put
\[
T=\operatorname{lcm}(r,\operatorname{ord}_v(10)),\qquad \operatorname{ord}_1(10)=1.
\]
Let \(S_d=(C_{10^d-1},10^{-D(10^d-1)}R_{10^d-1})\) be the ascending/normalized descending digit-layer state.

Full-layer maps are periodic after \(E=1+\max(a,c)\); each product of \(T\) consecutive stable maps is a translation (reciprocal diagonal multipliers have product 1). Since \(T\ge E\),
\[
S_{jT}=S_T+(j-1)\Delta,\quad j\ge1,\qquad \Delta=S_{2T}-S_T=(U,V).
\]

## New theorem A: unrestricted-order constructive implication

If \((U,V)\ne(0,0)\), **there exists \(1\le j\le p\)** such that
\[
p\mid M(10^{jT})\quad\hbox{or}\quad p\mid M(10^{jT}+1).
\]
Indeed the normalized residues of the two mountains, the second multiplied by 10, are
\[
f_0(j)=10C_{jT}+Y_{jT}+1,\quad
f_1(j)=1000C_{jT}+Y_{jT}+121.
\]
Their respective affine slopes are \(10U+V\) and \(1000U+V\). Both cannot be zero unless \((U,V)=(0,0)\), since their difference is \(990U\) and \(p\nmid990\). Solve the nonconstant linear congruence for \(j\) modulo \(p\), using representatives \(1,\ldots,p\).

**No assumption whatsoever on the prime factors of \(r\).**

## New theorem B: zero-drift decision in 2T digit windows

If \(\Delta=0\), then \(S_{d+T}=S_d\) for all \(d\ge T\). The existence of any divisible mountain is equivalent to existence of one with \(1\le k<10^{2T}\).

For each digit length \(d\), let \(L=10^{d-1}\), \(q=10^d\), \(S_{d-1}=(C,Y)\), and \(k=L+n\).

When \(q\ne1\) modulo \(p\), let \(z=q^n\) and set
\[
A=qC+\frac{Lq}{q-1}+\frac q{(q-1)^2},\quad
B=Y-\frac L{q-1}+\frac q{(q-1)^2}.
\]
Then the exact normalized mountain vanishes iff
\[
A z^2-\frac{2q}{(q-1)^2}z+B=0
\quad\text{for }z\in\langle q\rangle,
\]
with offset \(n\in[0,9L-1]\) respecting the finite window width. If \(q=1\), the condition is
\[
(L+n)^2+C+Y+L-L^2=0\pmod p.
\]
All windows after \(2T\) repeat an earlier state and \((q,L)\) phase; representatives in windows \(T+1,\ldots,2T\) allow every residue offset \(0\le n<p\), since \(p<10^r\le10^T\). Thus the \(2T\)-window test is **complete for this fixed prime**, not a global existence proof.

Together, if a witness exists, one exists with \(k\le10^{pT}+1\).

## Verified examples / scope

Direct modular recursion gave:
- \(p=73,\ T=8,\ \Delta=(25,24),\ j=33:\quad73\mid M(10^{264})\).
- \(p=113,\ T=336,\ \Delta=(112,56),\ j=82:\quad113\mid M(10^{27552})\).
- \(p=233,\ T=1624,\ \Delta=(205,150),\ j=92:\quad233\mid M(10^{149408})\).
- \(p=313,\ T=312,\ \Delta=(198,283),\ j=199:\quad313\mid M(10^{62088})\).
- \(p=1489,\ T=3720,\ \Delta=(138,613),\ j=103:\quad1489\mid M(10^{383160})\).

All 165 primes in \(7\le p<1000\) were checked and no zero drift was found (finite evidence only). An independent implementation of the digit-layer recurrence checked the predicted witnesses for representative primes, as well as literal short mountains.

**Open gap:** prove every prime has nonzero drift, or prove the finite subgroup equation has a root in at least one window when drift vanishes. Neither is established here. Do not promote per-prime decidability to the universal OEIS conjecture.

The full 2-page PDF, exact per-prime checker and independent tests are included in the companion conversation research package.