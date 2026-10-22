# A077187: the complete \(11\cdot2^a5^c\) order family

**October 18, 2026 — computer-assisted INFINITE order-family theorem,
unrestricted A077187 still open.**

This extends the generic fixed-\(v\) spectral compression proved in
[the companion \(v=7\) note](fixed_v_spectral_compression_v7_2026-10-18.md),
but displays a distinct additional **linear degeneration**.

## Theorem

For every prime \(p\) satisfying
\[
\boxed{\operatorname{ord}_p(10)=11\cdot2^a5^c,\qquad a,c\ge0}
\]
there is a positive integer \(k\) such that \(p\mid M(k)\).
More specifically, its stable drift is nonzero, and the two-offset
construction supplies
\(k=10^{jT}\) or \(10^{jT}+1\), with \(1\le j\le p\),
\(T=\operatorname{lcm}(\operatorname{ord}_p(10),2)\).

## Fixed-degree derivation, not a large-order search

Here \(v=11\), \(h=\operatorname{ord}_{11}(10)=2\),
\(\ell=\operatorname{lcm}(11,2)=22\).
Put \(u=2^a5^c\). Then
\[
g=\gcd(11u,22)=\begin{cases}11,&a=0,\\22,&a>0,\end{cases}
\quad m=11u/g,\quad
\zeta=10^m
\]
has exact order \(g\). The generic 22-coset formula gives
\[
U_\gamma(m)=U_0+U_1m+U_2m^2,\quad
V_\gamma(m)=V_0+V_1m+V_2m^2,\quad
\gamma=u^{-1}\bmod11.
\]

**New structural lemma for \(v=11\):** for each \(g=11,22\)
and every \(\gamma\in(\mathbb Z/11)^\times\),
\[
\boxed{U_2=V_2=0\quad\text{in }\mathbb Q(\zeta_g).}
\]
Thus the correct elimination is the **linear** determinant
\[
\boxed{R_{g,\gamma}=U_1V_0-U_0V_1,}
\]
not the quadratic expression \(A^2-BC\) with padded zero leading
coefficients (that latter expression vanishes identically).

The attached exact symbolic script verifies the two quadratic
coefficients vanish in all 20 phase cases, constructs \(R_{g,\gamma}\)
by exact degree-10 cyclotomic arithmetic, multiplies by 4000
to give algebraic integers, and computes
\[
N_{g,\gamma}
=\bigl|\operatorname{Norm}_{\mathbb Q(\zeta_g)/\mathbb Q}
(4000R_{g,\gamma})\bigr|>0.
\]
These are twenty explicit nonzero **fixed** integers, independently
pinned in [the certificate script](certify_fixed_v11.py).
The exact 20-line norm table has SHA-256
\`\`\`
513c1bc27609c811d838d00f6248f61f1f349c9b3e1fa6f54472e37597ab76e7
\`\`\`
All coefficients of \(U_i,V_i\) have rational denominators dividing
200, and \(p\) of exact order \(11u\) is greater than 11, so all
the reductions are legitimate modulo \(p\).

If zero drift occurred for a prime with order \(r=11u\), then
the correct phase \(\gamma\) would force
\[
p\mid N_{g,\gamma},\quad
p\mid\Phi_r(10),\quad r\mid p-1,\quad
r<p\le N_{g,\gamma}.
\]
The last inequality cuts the unbounded exponents down to a
**fixed finite index sieve**. As in the \(v=7\) proof, the
cyclotomic value is evaluated modulo the norm using
\[
\Phi_{11\cdot2^a5^c}(X)
=\Phi_{11\cdot2^{[a>0]}5^{[c>0]}}
\left(X^{2^{\max(a-1,0)}5^{\max(c-1,0)}}\right).
\]
The four base cyclotomic degrees are at most 40.

The reproducer examines all **3943 phase-admissible**
\((a,c)\) with \(11\cdot2^a5^c\le N_{g,\gamma}\),
where the **phase-dependent bound must be checked separately at
every pair**; it is not monotone as \(c\) changes.
For each index, it computes
\[
h=\gcd(N_{g,\gamma},\Phi_{11\cdot2^a5^c}(10))
\]
and repeatedly removes \(\gcd(h,11\cdot2^a5^c)\).
Every final residual is exactly 1. Hence no true-order prime
can divide its algebraic elimination norm; zero drift is excluded
for **every** \(a,c\), not merely those up to a chosen cutoff.

This certifies the theorem using at most 22 coset terms, degree-10
symbolic arithmetic, and a finite factorization-free norm exclusion,
rather than enumerating target primes.

## Scope and cross-check

The generic compression is algebraically proved for arbitrary
\(v\), but its resultant may degenerate or have prime factors
of actual order \(r\); the \(v=7\) and \(v=11\) cases are
separately proved by the two certificates. These two new families
cover orders with a prime factor outside \(\{2,3,5\}\) and
unbounded smooth components.

The independent standard-library prime-field audit
[audit_fixed_v11.py](audit_fixed_v11.py) checks both the
22-coset formula and an independently coded full-digit-layer
recurrence for selected primes of exact orders
\(11,22,44,55,88,110,5500,6875\).

Reproduce:
\`\`\`sh
python3 -m pip install sympy
python3 papers/A077187/research/certify_fixed_v11.py
python3 papers/A077187/research/audit_fixed_v11.py
\`\`\`

All claims remain subject to independent code and manuscript review.
The all-primes OEIS A077187 existence conjecture is **NOT** claimed solved.
