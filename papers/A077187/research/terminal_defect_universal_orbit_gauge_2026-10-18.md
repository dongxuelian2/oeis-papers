# A077187: universal terminal-defect orbit conjugacy and why window-switching is necessary

**2026-10-18 — PROVED general orbit identity and a positive-density
failure theorem inside an already solved order family.**
The unrestricted all-primes mountain existence question remains OPEN.
This development complements
\`u8_single_window_density_one_thirtysecond_2026-10-18.md\`,
rather than raising numerical order cutoffs.

## 1. Universal conjugacy at the stable-cutoff digit layer

Let \(p\ge7,\ p\ne11\) be prime, put
\(r=\operatorname{ord}_p(10)=uv\),
\(u=2^a5^c\), \((v,10)=1\), and
\[
h=\max(1,a,c),\qquad
T=\operatorname{lcm}(r,\operatorname{ord}_v(10)).
\]
For \(r\ge2\), \(h<r\), so \(q=10^h\ne1\pmod p\).
Write \(S_d=(C_d,Y_d)\) for the state at the end of
the complete \(d\)-digit layer, with \(S_0=(0,0)\).
Let \(F_h\) denote its actual full-layer map and
\(\widehat F_h=F_{T+h}\) its stable continuation.
The original and stable maps agree after layer \(h\).
Consequently the finite-defect transfer gives
\(S_{pT}=W\), and the pre-state of the
\((pT+h)\)-digit window is
\[
\boxed{\widehat F_h^{-1}F_h(S_{h-1}).}\tag{1}
\]
No assumption that the stable drift is zero is used.

For the actual \(h\)-digit window define
\[
L=10^{h-1},\quad q=10^h,\qquad
c_h={L\over q-1}+{1\over(q-1)^2},\quad
b_h=-{L\over q-1}+{q\over(q-1)^2}.
\]
Let \(A_h,\widehat A_h\) be its actual and stable full-layer
multipliers and \(\rho_h=\widehat A_h/A_h\).
The centered affine maps have the same additive constants,
so (1) yields
\[
\boxed{
C_{\rm late}+c_h=\rho_h^{-1}(C_{h-1}+c_h),\quad
Y_{\rm late}+b_h=\rho_h(Y_{h-1}+b_h).}\tag{2}
\]
Moreover \(\rho_h\in\langle q\rangle\). Indeed
\[
\rho_h=10^{9\cdot10^{h-1}((T+h)10^T-h)}
\]
and \(\gcd(h,r)\mid T\) and \(\gcd(h,r)\mid h\),
so the exponent is divisible by \(\gcd(h,r)\).
The cyclic group \(\langle10^h\rangle\) consists exactly
of the powers \(10^{gk}\), \(g=\gcd(h,r)\).

**Theorem 1 (stable-cutoff orbit gauge).**
The entire late \((pT+h)\)-digit window has a divisible
mountain iff the **fixed original \(h\)-digit polynomial**
\[
\boxed{
q(C_{h-1}+c_h)y^2-
{2q\over(q-1)^2}y+(Y_{h-1}+b_h)=0
\qquad (y\in\langle q\rangle)
}\tag{3}
\]
has an admissible root. Specifically, the original
local parameter \(y\) and the late parameter \(z\)
are related by \(z=\rho_h y\).

*Proof.* The general \(q\ne1\) window equation is
\(q(C+c_h)z^2-2qz/(q-1)^2+(Y+b_h)=0\).
Substitute (2) and \(z=\rho_h y\); the whole equation
becomes \(\rho_h\) times (3). Since \(\rho_h\in\langle q\rangle\),
the substitution is a bijection of the allowed subgroup.
The late window has more than \(r\) center positions,
so it realizes the entire subgroup. QED.

The constants \(C_{h-1},Y_{h-1}\) come from the
**ordinary finite concatenations ending at \(10^{h-1}-1\)**.
For fixed \(h\), equation (3) has rational coefficients
independent of \(p\), \(v\), and all stable multipliers.
It may have roots in the *full* subgroup even when the
literal small original \(h\)-digit window is too short
to attain all subgroup phases.

The \(h=1\) case has \(S_0=0\), and (3) reduces to
\[
(10y-1)^2/81=0,\qquad y=1/10\in\langle10\rangle.
\]
This recovers the classic single-defect mechanism.
For \(h\ge2\), no universal root claim follows.

## 2. Explicit h=2 polynomial and rational discriminant

For \(h=2\), the original first layer has the *exact*
integer/rational state
\[
C_1=123456789,\qquad Y_1={987654321\over10^9}.
\]
Putting \(q=100,L=10\) in (3), we get
\[
\boxed{A_2y^2+H_2y+B_2=0,\quad y\in\langle100\rangle}
\]
with
\[
A_2={120999998998000\over9801},\quad
H_2=-{200\over9801},\quad
B_2={8790000000121\over9801000000000}.
\]
Its **exact rational discriminant** is
\[
\boxed{\mathcal D_2=H_2^2-4A_2B_2
=-{669867392724508459\over15125000}.}\tag{4}
\]
These numbers depend only on the initial
finite decimal prefix, not on the large multiplicative
order or on any primitive-root phase.

## 3. The terminal window fails on a density 1/32 set of u=4 primes

**Theorem 2 (necessary window switching in a solved subfamily).**
The set
\[
\boxed{\{p\text{ prime}:
p\equiv29\pmod{40},\
(\mathcal D_2/p)=-1\}}
\tag{5}
\]
has natural density **exactly \(1/32\)** among
rational primes. Every such prime has smooth
multiplicative-order part \(u=4\), and the
entire \((pT+2)\)-digit terminal-defect window
has **no divisible mountain**, even though the
previously proved \(u\mid20\) theorem guarantees
a divisible mountain in another window.

*Proof.* For \(p\equiv29\bmod40\),
\(p\equiv5\bmod8\), so \(v_2(p-1)=2\) and
\((2/p)=-1\). Also \(p\equiv4\bmod5\),
so \(5\nmid p-1\) and \((5/p)=(p/5)=1\).
Thus \((10/p)=-1\), and
\(v_2(\operatorname{ord}_p(10))=2\),
\(v_5(\operatorname{ord}_p(10))=0\);
hence \(u=4\) and \(h=2\).

To show the discriminant character can be independently
negative in this CRT class, let \(K=\mathbb Q(\zeta_{40})\).
At the completely split rational prime \(41\equiv1\bmod40\),
the exact reduction (4) gives
\[
\boxed{\mathcal D_2\bmod41=12,\qquad (12/41)=-1.}
\]
Consequently
\(\sqrt{\mathcal D_2}\notin K\).
The abelian compositum
\(K(\sqrt{\mathcal D_2})/\mathbb Q\)
has degree \(2\varphi(40)=32\).
The Chebotarev density theorem assigns exactly
\(1/32\) to the Frobenius pair
\((29\bmod40,-1)\).
For every unramified prime with this pair,
the quadratic (3) is irreducible modulo \(p\)
and hence has no admissible subgroup root.
This is exactly the late terminal window by
Theorem 1. The already proved \(u\mid20\)
single-defect theorem guarantees another witness,
demonstrating that *switching windows is genuinely
necessary even in a fully solved family*. QED.

**Examples:** \(p=229,269,349,709,829\) have
\(\chi_p(\mathcal D_2)=-1\), so this terminal
window fails. At \(p=109,149,509\), the fixed
quadratic does have a subgroup root; at \(p=389\),
the discriminant is square but subgroup membership
fails. These samples illustrate, but do not prove,
the exact density theorem.

## 4. The open global implication

Theorem 1 controls the *last transient window* with
a fixed rational quadratic for every smooth part \(u\).
Theorems 2 and the prior u=8 density result prove
that it is generally **not sufficient to use only
this one window**. In the solved \(u\mid20\)
family, the necessary alternative is another early
window (already supplied in the original proof).

This gives an explicit direction for unresolved \(u\):
relate the rational terminal quadratic to the
previous windows through the actual finite-defect
cocycle, or use an independent full stable-period
root mechanism under zero drift. Neither is
established here. A077187 remains **OPEN**.

## Reproducibility

Run \`python3 papers/A077187/research/audit_terminal_defect_gauge_u4.py\`.
The independent standard-library audit checks exact rational
coefficients, the split-prime 41 obstruction, and the
gauge equivalence of original and shifted digit-layer
states for **nine genuine target primes**.
The dedicated \`.github/workflows/a077187-terminal-defect-gauge.yml\`
reproduces it in GitHub Actions.
