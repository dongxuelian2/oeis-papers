# A077187: the exact eighth-root transient trace and its non-rational squareclass

**October 18, 2026 — proved finite-defect structural theorem.**
No unbounded all-primes existence proof is claimed. This note targets
the *zero-drift* branch rather than increasing the computational-order
cutoff. It builds on the exact finite-defect transfer and the
u=8 tail-gauge formulas already in this PR.

## General theorem: finite-degree singular witnesses for fixed smooth part

Let \(p\ge7\) be prime, \(r=\operatorname{ord}_p(10)=uv\),
\(u=2^a5^c\), \((v,10)=1\), and let
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\).
Set \(W=S_{pT}\), the state at the end of the digit
window of length \(pT\).

**Theorem 0 (fixed-smooth-part singular reduction).**
In the entire \(pT\)-digit window,
\[
\boxed{\frac{M(k)}{10^{D(k-1)}}\equiv
k^2+W_C+W_Y\pmod p.}
\]
Consequently this window has a divisible mountain if
and only if \(-W_C-W_Y\) is a square in \(\mathbb F_p\)
(including zero). For each fixed \(u\), there are rational
algebraic functions \(f_{u,\gamma}\), with
\(\gamma=v^{-1}\bmod u\), whose coefficients and degree
depend only on \(u\), and
\[
\boxed{W_C+W_Y=f_{u,\gamma}(10^v),\quad
f_{u,\gamma}\in\mathbb Q(\zeta_u),\quad
[\mathbb Q(\zeta_u):\mathbb Q]=\varphi(u).}
\]
Here the expression means evaluation at the primitive
\(u\)-th root \(10^v\bmod p\), after reducing permissible
rational denominators. For \(u=1\), the field is
\(\mathbb Q\) and the finite-defect state is zero.
There is **no bound on \(v\)**.

**Proof.** The finite-defect transfer theorem (already
proved in this PR) writes the actual boundary states
as \(S_{jT}=W+jb\), with a stable translation \(b\).
At \(j=p\), \(S_{pT}=W\) in \(\mathbb F_p^2\),
irrespective of whether \(b=0\).
Since \(d=pT\) is a multiple of \(r\), the multiplier
\(q=10^d\) equals 1 and \(L=10^{d-1}=1/10\).
The complete singular digit layer changes the sum
\(C+Y\) by \(9L^2=9/100\), while the local
square identity gives the constant
\(C_{d-1}+Y_{d-1}+L-L^2\). Since
\(L-L^2=9/100\), this is precisely
\(C_d+Y_d=W_C+W_Y\). Its window is long
enough to attain every field residue \(k\bmod p\).
Finally the previously proved finite-defect rational-map
theorem expresses both coordinates of \(W\) by at most
\(E-1=\max(a,c)\) early affine maps, with multipliers
belonging to the fixed \(u\)-th root cyclotomic group.
The coefficient field has degree \(\varphi(u)\), independently
of \(v\). QED.

**Scope.** A fixed-degree character is a criterion for
this **particular singular window**, not a guarantee
that its character is positive. The nonzero-drift
construction and other digit windows may still give
witnesses when this singular criterion fails.
The \(u=8\) calculation below identifies an exact
cyclotomic squareclass that obstructs a straightforward
uniform perfect-square continuation of the \(u\mid20\)
argument.

## Theorem: a fixed cyclotomic parameter controls a singular witness

Let \(p\ge7\) be prime with
\[
r=\operatorname{ord}_p(10)=8v,\quad (v,10)=1,\qquad
T=\operatorname{lcm}(r,\operatorname{ord}_v(10)).
\]
Let \(\rho=\widehat A_1/A_1=10^{9(10^T-1)}\in\mathbb F_p\),
where \(A_1\) and \(\widehat A_1\) are the first-layer
original and stable multipliers. The finite-defect multiplier
theorem gives \(\operatorname{ord}_p(\rho)=8\),
\(\rho^4=-1\), and \(\rho_2=\rho_3=-1\).

Define the **fixed rational coefficients**, independent of \(v,p,T\),
\[
\boxed{
\begin{aligned}
a&=\frac{10}{81}
-\frac{219804400}{120758121\,10^{189}},\\
b&=\frac1{81}
+\frac{217557800\,10^{189}}{120758121},\\
c&=-\frac{11}{81}.
\end{aligned}}
\tag{1}
\]
Let \((C_d,Y_d)\) be the normalized ascending/descending
boundary state. The previously established finite-defect
transfer gives \(W=(C_{pT},Y_{pT})\), regardless of the
stable translation. Then
\[
\boxed{
W_C=-\frac{10}{81}+a\rho^{-1},\quad
W_Y=-\frac1{81}+b\rho,\quad
W_C+W_Y=c+a\rho^{-1}+b\rho.
}\tag{2}
\]
All denominators are invertible: their prime factors belong to
\(\{2,3,5,11,37\}\), whose multiplicative orders of 10
are not divisible by 8. Every application of an affine
inverse is therefore legal.

**Proof.** For each of the first three digit layers,
write its exact affine map
\[
F_d(C,Y)=\bigl(A_d C+B_d(A_d),\
       A_d^{-1}(Y+R_d(A_d))\bigr),
\]
where, with \(q=10^d,L=10^{d-1},n=9L\),
\[
S(A)=\frac{A-1}{q-1},\quad
J(A)=\frac{q-nA+(n-1)qA}{(q-1)^2},\quad
B(A)=(q-1)S(A)-J(A),\quad
R(A)=LS(A)+J(A).
\]
These are affine functions of \(A\). Their stable
counterparts replace \(A_d\) by \(A_d\rho_d\).
The defect transfer is exactly
\[
W=\widehat F_1^{-1}\widehat F_2^{-1}
   \widehat F_3^{-1}F_3F_2F_1(0,0).
\]
Substitute \(\rho_1=\rho,\ \rho_2=\rho_3=-1\),
and reduce powers by \(\rho^4=-1\). Exact rational
simplification yields (2) with (1). The accompanying
standard-library certifier independently recomputes this
composition in \(\mathbb Q[X]/(X^4+1)\), and asserts all
coefficients (not just their values at chosen primes). QED.

Now consider the **singular digit window of length \(d=pT\)**.
Since \(r\mid d\), one has \(10^d=1\) modulo \(p\).
The general singular-window mountain identity is
\[
\frac{M(k)}{10^{D(k-1)}}=
k^2+C_{d-1}+Y_{d-1}+L-L^2,\quad L=10^{d-1}.
\]
The complete layer has \(C_d+Y_d=
C_{d-1}+Y_{d-1}+9L^2\) because its multiplier is
1. Here \(L=1/10\), so \(L-L^2=9/100=9L^2\).
Hence the normalized mountain residue **in this
entire digit window** is simply
\[
\boxed{
\frac{M(k)}{10^{D(k-1)}}=
k^2+W_C+W_Y
=k^2+c+a\rho^{-1}+b\rho.
}\tag{3}
\]
The window is longer than \(p\), so every \(k\bmod p\)
is attained by an actual positive \(d\)-digit center.

**Corollary (fixed-degree singular-window criterion).**
For every prime with \(\operatorname{ord}_p(10)=8v\),
the \(pT\)-digit window contains a divisible mountain
**if and only if**
\[
\boxed{-c-a\rho^{-1}-b\rho
\text{ is a square in }\mathbb F_p,\text{ including }0.}
\tag{4}
\]
Thus the whole first-singular-window test for an unbounded
coprime factor \(v\) lives in a **fixed degree-4
cyclotomic algebra**, not in a degree growing with \(v\).
It is a sufficient witness construction, not a universal
existence theorem: other digit windows or nonzero drift
can succeed when this one fails.

## Theorem: the trace has a genuinely non-rational squareclass

Let \(K=\mathbb Q(\zeta_8)\), and put
\(E=c+a\zeta_8^{-1}+b\zeta_8\).
The extension \(K/\mathbb Q\) has degree four.
Since multiplication by \(\zeta_8\) has norm 1,
\[
\boxed{
\operatorname{Norm}_{K/\mathbb Q}(E)
=(a^2-b^2)^2+(2ab-c^2)^2.
}\tag{5}
\]
To see this, compute the resultant
\(\operatorname{Res}_X(X^4+1,bX^2+cX+a)\).
Pairing the roots \(X,-X\) first and writing \(Y=X^2\)
reduces it to
\[
\operatorname{Norm}_{\mathbb Q(i)/\mathbb Q}
\bigl((a^2-b^2)+(2ab-c^2)i\bigr),
\]
which is (5).

**Moreover \(E\) is not a rational multiple of
a square in \(K\):**
\[
\boxed{E\notin\mathbb Q^\times(K^\times)^2.}\tag{6}
\]
This follows from an exact *small-prime* obstruction
that avoids even computing the huge rational norm.
All rational denominators in (1) are nonzero modulo 23;
one checks
\[
a\equiv10,\quad b\equiv22,\quad c\equiv1\pmod{23}
\quad\Longrightarrow\quad
\operatorname{Norm}(E)\equiv7\pmod{23}.
\]
But 7 is a quadratic **nonresidue** modulo 23.
Thus the rational norm is nonsquare. Were \(E=qs^2\)
with \(q\in\mathbb Q^\times,s\in K^\times\), its
degree-four field norm would be
\(q^4\operatorname{Norm}(s)^2\), necessarily a rational
square. Contradiction. QED.

**Interpretation.** Unlike the elementary \(u\mid20\)
perfect-square witness, the \(u=8\) singular-window
criterion involves a *genuine cyclotomic quadratic
character*, which cannot be converted by a universal
algebraic square rescaling to a single rational Legendre
symbol. This precisely identifies a source of the
obstruction to extending the elementary construction.
It does **not** say that the symbol is always negative,
nor that A077187 has a counterexample.

## Independent finite-field checks (consistency, not the proof)

The script \`audit_u8_singular_trace_norm.py\` verifies (2)
**symbolically** in the full quartic algebra, checks
the nonrational squareclass by the residue 7 modulo 23,
and then independently computes the original full
digit-layer recursion and inverse stable defect at these
seven true-order primes:

| \(p\) | \(r\) | \(\rho\) | \(W_C+W_Y\) | \(\chi_p(-W_C-W_Y)\) |
|---:|---:|---:|---:|---:|
| 73 | 8 | 22 | 27 | +1 |
| 137 | 8 | 96 | 36 | +1 |
| 233 | 232 | 97 | 38 | +1 |
| 313 | 312 | 5 | 248 | -1 |
| 617 | 88 | 435 | 598 | +1 |
| 2393 | 184 | 58 | 2087 | +1 |
| 7841 | 56 | 2725 | 1339 | -1 |

In particular, \(p=313,7841\) show that the **singular
window is not a universal rescue** for the previously
refuted fixed early-window construction, even when its
center interval is long enough to contain all field residues.
These are not counterexamples to mountain divisibility.

**Open:** The uniform full-primes theorem still requires
proving nonzero drift or locating a root in *some other*
window when this cyclotomic character is negative.
The all-primes OEIS conjecture remains OPEN.
