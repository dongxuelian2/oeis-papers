# A077187: exact density 1/32 for failure of the first u=8 post-defect window

**2026-10-18. PROVED quantitative corollary and independent small certificate.**
This is a sharpening/standalone proof for **one particular window** of the
previously proved positive-density *three-window* obstruction in
\`zero_drift_continuation_2026-10-18.md\`. It is **not a counterexample**
to existence of a divisible mountain and **not** a full solution of
A077187. Importantly, this result concerns the **actual** decimal
phase selected by each prime, not a choice among formal conjugates.

## The universal phase-free quadratic

Let \(p\ge7\), \(r=\operatorname{ord}_p(10)=8v\),
\((v,10)=1\), and
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\).
After \(p\) stable blocks the exact finite-defect state is
\[
W_C=-10/81+a\rho^{-1},\qquad
W_Y=-1/81+b\rho,\qquad
\rho=10^{9(10^T-1)}\in\langle10\rangle,
\]
where the **fixed rational numbers**
\[
a={10\over81}-{219804400\over120758121\cdot10^{189}},
\qquad
b={1\over81}+{217557800\cdot10^{189}\over120758121}
\]
were independently verified in the previous finite-defect result.

The full \((pT+1)\)-digit interval begins at \(k=10^{pT}\).
Its normalized mountain polynomial, with
\(z=10^n\in\langle10\rangle\), is
\[
10a\rho^{-1}z^2-\frac{20}{81}z+b\rho.
\]
The substitution **\(y=\rho^{-1}z\)** is a bijection of
\(\langle10\rangle\), so the equation is equivalent to
\[
\boxed{10ay^2-\frac{20}{81}y+b=0,\qquad
y\in\langle10\rangle.}\tag{1}
\]
Thus the actual root phase \(\rho\) disappears **exactly**, not
statistically. The discriminant is the fixed rational
\[
\boxed{\mathcal D=(20/81)^2-40ab.}\tag{2}
\]
If \(\mathcal D\) is a nonsquare modulo \(p\), **no integer center
in that entire digit interval gives a divisible mountain**, even
when we allow every \(y\in\mathbb F_p\) rather than just the subgroup.
If it is square, subgroup membership is still necessary, and is
not automatic.

## Theorem: actual failure has natural density 1/32

**Theorem.** Consider primes \(p\) satisfying all three conditions
\[
\boxed{\begin{aligned}
p&\equiv57\ \text{or}\ 73\pmod{80},\\
\left({\mathcal D\over p}\right)&=-1 .
\end{aligned}}\tag{3}
\]
Excluding the finitely many denominator/ramification primes,
this set has natural density **exactly \(1/32\)** among all
rational primes. Every prime in the set has \(u=8\) as
the \(2,5\)-smooth part of its multiplicative order \(r\),
and **the entire post-\(pT\) first nonsingular digit window
fails to contain a divisible mountain**.

*Proof.* The residue classes \(57,73\bmod80\) satisfy
\(p\equiv9\bmod16\), so \(v_2(p-1)=3\), and
\(p\equiv2\) or \(3\bmod5\), so \(v_5(p-1)=0\).
Moreover \(p\equiv1\bmod8\) gives \((2/p)=1\), while
quadratic reciprocity gives \((5/p)=(p/5)=-1\).
Therefore \((10/p)=-1\). In a cyclic group of order
\(p-1\) with \(v_2(p-1)=3\), a quadratic nonsquare has
multiplicative order with exact 2-adic valuation 3.
Consequently
\[
v_2(r)=3,\qquad v_5(r)=0,
\]
so the fixed \(u=8\) model applies to **every** such prime.

To show the discriminant character in (3) is independent of
the residue class, let \(K=\mathbb Q(\zeta_{80})\).
An exact **single-prime certificate** at the completely
split prime \(401\equiv1\bmod80\) is
\[
\boxed{a\bmod401=146,\quad b\bmod401=228,\quad
\mathcal D\bmod401=24,\quad(24/401)=-1.}\tag{4}
\]
The rational denominator of \(\mathcal D\) is invertible
modulo 401. If \(\sqrt{\mathcal D}\in K\), then every
unramified rational prime that splits completely in \(K\)
would split in \(\mathbb Q(\sqrt{\mathcal D})\); this
contradicts (4). Hence
\[
K\cap\mathbb Q(\sqrt{\mathcal D})=\mathbb Q,\qquad
[K(\sqrt{\mathcal D}):\mathbb Q]=64.
\]
This is an abelian (hence Galois) compositum, with
\(\operatorname{Gal}\cong(\mathbb Z/80\mathbb Z)^\times
\times C_2\).
The Chebotarev density theorem assigns density
\(1/64\) to each of the two Frobenius elements
\((57,-1)\) and \((73,-1)\).
Their union has density \(2/64=1/32\).
For these primes \(\mathcal D\) is nonsquare, so
the quadratic (1) has no solution even in
\(\mathbb F_p\). QED.

**Relation to the stronger existing result.**
The prior \`zero_drift_continuation_2026-10-18.md\`
already proves that a set of density \(1/128\)
defeats the **first three** post-defect windows.
The result here is **not** a new three-window
counterexample; it supplies a simpler single-prime
independence certificate and the *exact, larger density
\(1/32\) for failure of the first window alone*.
Both results concern a chosen witness-construction
strategy, and neither assumes or proves true zero drift.

## Examples and the precise subgroup obstruction

The standalone audit compares (1) directly with the
original complete digit-layer maps. Examples with
\(p\equiv57,73\bmod80\):

| \(p\) | \(r\) | \(\chi_p(\mathcal D)\) | roots in \(\langle10\rangle\) |
|---:|---:|---:|---:|
| 73 | 8 | +1 | 0 |
| 137 | 8 | +1 | 0 |
| 233 | 232 | +1 | 2 |
| 313 | 312 | -1 | 0 |
| 457 | 152 | -1 | 0 |
| 617 | 88 | -1 | 0 |
| 857 | 856 | +1 | 2 |
| 1993 | 664 | +1 | 0 |

Even when the discriminant is a square, group-orbit
attainability is a strictly separate condition.

**Open:** Neither this result nor the earlier
three-window obstruction proves that a *genuine*
zero-drift prime has no witness in a later digit window.
The outstanding A077187 existence problem is still OPEN.
