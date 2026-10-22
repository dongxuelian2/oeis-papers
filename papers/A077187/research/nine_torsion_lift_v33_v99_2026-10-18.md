# A077187: nine-torsion spectral lifting and the infinite \(v=33,99\) families

**2026-10-18. Theorem + exact finite elimination.** This continues
\`fixed_v_spectral_compression_v7_2026-10-18.md\` and the independently
certified *linear* \(v=11\) result. The unrestricted A077187
all-primes conjecture is not resolved.

## Main theorem

For every prime \(p\) satisfying
\[
\boxed{\operatorname{ord}_p(10)=11\cdot3^b2^a5^c,\qquad
  a,c\ge0,\quad 0\le b\le2,}
\]
there exists a positive integer \(k\) for which \(p\mid M(k)\).
The case \(b=0\) is the previously proved \(v=11\) theorem.
The cases \(b=1,2\) are **new infinite-order-class results**, not
bounded multiplicative-order checks.

The key fact is that the spectral functions at coprime parts
\(v=33\) and \(v=99\) are **the same algebraic functions** as for
\(v=11\), evaluated at a different argument, so **no new resultant
norms are required**.

## 1. Nine-torsion folding lemma

Here is a slightly more general structural result.

**Lemma (nine-torsion spectral lift).** Let \(v_0>1\) be coprime to
\(30\), and put \(h_0=\operatorname{ord}_{v_0}(10)\),
\(\ell_0=\operatorname{lcm}(v_0,h_0)\). Assume \(3\nmid\ell_0\).
For \(s\mid9\), \(s\in\{1,3,9\}\), suppose
\[
r=\operatorname{ord}_p(10)=s v_0 u,\qquad u=2^a5^c,
\]
and \(p\ge7\). Put
\[
g_0=\gcd(r,\ell_0)=\gcd(v_0u,\ell_0),
\quad n=r/g_0,\quad \xi=10^n\bmod p
\]
so that \(\xi\) is a primitive \(g_0\)-th root of unity.
Then the stable layer multipliers \(A_d\) and their cumulative
products \(P_d\) have period **\(\ell_0\)** (rather than the
possibly larger \(\ell=\operatorname{lcm}(sv_0,h_0)\)).
The full stable block has length \(T=n\ell_0\).
For each \(j=1,\ldots,\ell_0\), the \(n\) values
\(q_d=10^d\) at \(d=T+j+t\ell_0\), \(0\le t<n\),
are **all** roots of
\[
z^n=\xi^j
\quad\text{in }\mathbb F_p.
\]
Moreover the multiplier phases are exactly the generic
fixed-\(v_0\) phases,
\[
\boxed{
 A_{T+j}=\xi^{(g_0/v_0)\gamma'9j10^{j-1}},
 \qquad \gamma'=(s u)^{-1}\bmod v_0.
}\tag{1}
\]
Thus the generic fixed-\(v_0\) spectral coset formulas can be
reused with \(m=n\), the primitive root \(\xi\), and phase \(\gamma'\).

**Proof.** Since \(s\mid9\), \(10\equiv1\bmod s\), so
\(\operatorname{ord}_{sv_0}(10)=h_0\). Furthermore
\(s\) is coprime to \(\ell_0\), and
\[
T=\operatorname{lcm}(r,h_0)
=\operatorname{lcm}(r,\ell_0)
=r\ell_0/\gcd(r,\ell_0)=n\ell_0.
\]
For each stable \(d\), \(u\mid e_d=9d10^{d-1}\).
Modulo \(s\), \(e_{d+\ell_0}-e_d=0\) because
\(s\mid9\). Modulo \(v_0\), the same difference vanishes as
\(v_0\mid\ell_0\) and
\(10^{\ell_0}\equiv1\bmod v_0\).
Hence \(r\mid e_{d+\ell_0}-e_d\),
so \(A_{d+\ell_0}=A_d\).

The exponent \(9\sum_{d=e}^{e+\ell_0-1}d10^{d-1}\)
is divisible by \(u\) term by term and by \(s\) because \(s\mid9\).
Modulo \(v_0\), the exact finite-sum identity and
\(v_0\mid\ell_0,\ 10^{\ell_0}\equiv1\bmod v_0\)
imply divisibility (here \(9\) is invertible modulo \(v_0\)).
Thus every \(\ell_0\)-layer multiplier product equals 1,
and \(P_d\) also has period \(\ell_0\).

Since \(10\) has exact order \(r\), \(10^{\ell_0}\) has
order \(n=r/\gcd(r,\ell_0)\). The \(n\) values
\(10^{T+j+t\ell_0}\) are consequently distinct and
their \(n\)-th powers are all
\(\xi^j\). This proves the root-coset assertion.

For the last formula, write
\(g_0/v_0=t_0\). Then \(n=s u/t_0\), and every
stable \(e_d=9d10^{d-1}\) is divisible by \(n\):
\(u\mid10^{d-1}\), \(s\mid9\), \(t_0\mid u\).
Therefore \(A_d=\xi^{e_d/n}\).
Reducing \(e_{T+j}/n\) modulo \(g_0=t_0v_0\),
and using \(T\equiv0\bmod v_0\),
\(10^T\equiv1\bmod v_0\), gives exactly (1).
It depends on the effective phase \((su)^{-1}\bmod v_0\).
Finally substitute the \(\ell_0\) cosets into the universal
geometric-sum formulas, including the \(q=1\) term. QED.

**Scope.** This lemma is a universal *algebraic reduction* for every
base \(v_0\) satisfying its hypotheses. It does **not** automatically
prove that the drift is nonzero, and it does not claim such a
folding for base \(v_0=7\) (there \(\ell_0=42\) is divisible by 3).

## 2. Application to \(v_0=11\)

Here \(h_0=2,\ \ell_0=22,\ 3\nmid\ell_0\).
For \(s=3,9\) and \(u=2^a5^c\):
\[
\boxed{
 g_0=\begin{cases}11&a=0\\22&a\ge1,\end{cases}
\quad n=\frac{11su}{g_0},\quad
\xi=10^n,\quad\gamma'=(su)^{-1}\pmod{11}.}
\tag{2}
\]
Both drift coordinates are given by the **same 22-phase linear
polynomials**
\[
U=U_0(\xi,\gamma')+nU_1(\xi,\gamma'),\qquad
V=V_0(\xi,\gamma')+nV_1(\xi,\gamma')
\]
previously proved for \(v=11\) (the quadratic terms cancel by the
involution \(j\mapsto22-j\)). Thus simultaneous zero drift forces
\[
R_{g_0,\gamma'}(\xi)
=U_1V_0-U_0V_1=0\pmod p.
\]

The 20 exact integer norms
\(N_{g_0,\gamma'}=
|\operatorname{Norm}(4000R_{g_0,\gamma'})|\)
are already certified independently by
\`certify_fixed_v11.py\`. Their SHA-256 is
\`\`\`
513c1bc27609c811d838d00f6248f61f1f349c9b3e1fa6f54472e37597ab76e7
\`\`\`
and **none is zero**. Since \(p\ge r+1\ge34\), all
denominators and the scalar \(4000\) are invertible modulo \(p\).

Therefore zero drift would require
\[
\boxed{p\mid N_{g_0,\gamma'},\quad
p\mid\Phi_{11su}(10),\quad r=11su\mid p-1.}
\tag{3}
\]
In particular \(r<p\le N_{g_0,\gamma'}\). This converts both
infinite \(a,c\) ranges into a **finite exact norm-index exclusion**
with already established algebraic norms.

## 3. Exact exclusion, with no new symbolic resultant computation

The new independent script
\`certify_fixed_v33_v99.py\` duplicates the 20 pinned norm integers,
authenticates their SHA-256, and for **every** phase-admissible
\(r=11s2^a5^c\le N_{g_0,\gamma'}\) computes
\[
\gcd\bigl(N_{g_0,\gamma'},\Phi_{11s2^a5^c}(10)\bigr).
\]
It obtains \(\Phi_r(10)\bmod N\) from four fixed base
cyclotomic polynomials (index \(11s\), \(22s\), \(55s\),
\(110s\)) by the usual \(2,5\)-prime-power substitution,
using modular exponentiation. **No norm integer or
\(10^r-1\) is factored.** In fact, the computed gcd
is **1 in every case**:

| Coprime part \(v\) | Infinite order family | Complete checked index pairs | Nonunit gcds |
|---|---|---:|---:|
| 33 | \(r=33\cdot2^a5^c\) | 3,850 | 0 |
| 99 | \(r=99\cdot2^a5^c\) | 3,757 | 0 |

These are bounded *norm-index eliminations*, not a cutoff on
the target prime or its order. If \(r\) exceeds the relevant
fixed positive norm, then \(p>r\) already contradicts
\(p\mid N\), so the remainder of the infinite range is
covered automatically. The exact norm exclusions rule out (3).
Therefore every prime in either family has nonzero drift and
the previous two-offset theorem supplies a divisible mountain.
This proves the main theorem.

## 4. Independent field-level evidence

A separate standard-library-only script
\`audit_fixed_v33_v99.py\` checks 15 genuine primes with
exact order of the requested form. For each it computes
the drift twice: (i) the original complete \(2T\)-layer
state recursion in \(\mathbb F_p\), and
(ii) the 22-phase folded expression, with no calls to the
symbolic norm code. They agree, including
\[
\begin{array}{c|c|c|c}
p&r&U\bmod p&V\bmod p\\\hline
67&33&9&32\\
2377&264&2051&844\\
21121&10560&16550&11004\\
199&99&36&138\\
6337&6336&1654&6086\\
19801&9900&3922&3935
\end{array}.
\]
These numerical checks audit the folding formula; the actual
infinite-family proof uses the exact norm and exclusion above.

**Reproduce from the repository root:**
\`\`\`sh
python3 -m pip install sympy
python3 papers/A077187/research/certify_fixed_v11.py
python3 papers/A077187/research/certify_fixed_v33_v99.py
python3 papers/A077187/research/audit_fixed_v33_v99.py
\`\`\`

This extends the infinite subfamilies, but it neither proves
nonzero drift for arbitrary coprime-order \(v\) nor resolves
the unrestricted OEIS A077187 problem.


## 5. Exact 3-adic boundary of this folding mechanism

The restriction \(b\le2\) has an algebraic explanation rather than
being an arbitrary cutoff imposed by the finite exclusion.

**Proposition (sharp 3-primary multiplier defect).** Let
\(r=\operatorname{ord}_p(10)=11\cdot3^b2^a5^c\),
\(b\ge1\), and let \(d\) be in the stable digit-layer range.
For any \(t\ge0\), write \(L_t=22\cdot3^t\).
Then the ratio of stable layer multipliers has **exact order**
\[
\boxed{\operatorname{ord}\bigl(A_{d+L_t}/A_d\bigr)
=3^{\max(b-2-t,0)}\quad\text{in }\mathbb F_p^\times.}
\tag{4}
\]
Here \(A_d=10^{9d10^{d-1}}\).

**Proof.** Put \(e_d=9d10^{d-1}\). The exponent difference is
\[
e_{d+L_t}-e_d
=9\cdot10^{d-1}\bigl((d+L_t)10^{L_t}-d\bigr).
\]
Since \(L_t\) is even and divisible by 11, this difference is
divisible by 11. The smooth factor \(2^a5^c\) divides each
\(e_d\) in the stable range. The lifting-the-exponent lemma gives
\[
v_3(10^{L_t}-1)=v_3(10-1)+v_3(L_t)=2+t.
\]
Writing the bracket as
\(L_t+(d+L_t)(10^{L_t}-1)\), its first term has
3-adic valuation \(t\) and the second has valuation at least
\(t+2\). Therefore
\[
\boxed{v_3(e_{d+L_t}-e_d)=2+t}
\]
*exactly*, independent of \(d\). The order of
\(10^{e_{d+L_t}-e_d}\) inside the cyclic group of order
\(11\cdot3^b2^a5^c\) is thus precisely
\(3^{\max(b-2-t,0)}\). QED.

In particular:
- If \(b=1\) or \(2\), the multiplier is already
  **22-periodic**, enabling the fixed \(v=11\) algebra.
- If \(b\ge3\), its 22-step ratio has exact order
  \(3^{b-2}>1\), so the same 22-period folding is
  **provably impossible**.
- A multiplier period (not necessarily the minimal period among
  *all* positive shifts) is \(22\cdot3^{b-2}\).
  Its cyclotomic dimension grows with \(b\), so a further
  general theorem needs a new \(3\)-adic cancellation or tower
  argument, not more reuse of the existing 20 norms.

This locates the precise boundary of the new infinite-family proof.
It does **not** imply that \(b\ge3\) contains mountain
counterexamples; only this particular short-period mechanism stops
working without additional mathematics.
