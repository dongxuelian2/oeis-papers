# A077187: a Duhamel flux formula for all finite defects, and a genuine u=8 phase obstruction

**18 October 2026. Status:** exact general algebraic identities and a
Galois-theoretic obstruction to a *specific universal singular-window
strategy*. The full all-primes mountain conjecture remains **OPEN**.
This note adds structure rather than extending numerical order cutoffs.

## 1. Every finite defect is an explicit sum of local impulses

Let \(p\ge7\) be prime, \(r=\operatorname{ord}_p(10)\),
\(r=uv\), \(u=2^a5^c\), \((v,10)=1\), and
\[
 h=\max(a,c),\qquad
 T=\operatorname{lcm}(r,\operatorname{ord}_v(10))
 \quad(\operatorname{ord}_1(10)=1).
\]
All calculations are in \(\mathbb F_p\). Write \(F_i\)
for the *actual* complete \(i\)-digit layer maps, and
\(\widehat F_i=F_{T+i}\) for their stable continuation.
For \(i>h\), the maps agree, and the composition of the
\(T\) stable maps is a pure translation. Hence the
previously established finite-defect transfer yields
\[
S_{jT}=W+j\Delta,\qquad
W=(\widehat F_h\cdots\widehat F_1)^{-1}
 (F_h\cdots F_1)(0,0),
\]
where \(S_d=(C_{10^d-1},Y_{10^d-1})\) and
\(\Delta\) is the stable-period translation. In particular
\[
\boxed{W=S_{pT}\qquad\text{without assuming }\Delta=0.}
\tag{1}
\]

For \(1\le i\le h\), necessarily \(i<r\), hence
\(q_i=10^i\ne1\). Put
\[
L_i=10^{i-1},\quad
c_i=\frac{L_i}{q_i-1}+\frac1{(q_i-1)^2},\quad
b_i=-\frac{L_i}{q_i-1}+\frac{q_i}{(q_i-1)^2}.
\]
The two coordinate maps may be written
\[
F_i(C,Y)=\left(
 A_i(C+c_i)+\delta_i,\
 A_i^{-1}(Y+b_i)+f_i\right),
\]
where \(\delta_i,f_i\) depend only on \(q_i,L_i\)
and do not depend on the multiplier \(A_i\).
Write \(\widehat A_i=\rho_i A_i\) and
\[
P_{i-1}=\prod_{j=1}^{i-1}\widehat A_j,\qquad
(C_{i-1},Y_{i-1})=F_{i-1}\cdots F_1(0,0).
\]

**Theorem 1 (exact finite-defect Duhamel formula).**
For every \(r\) and every \(p\) as above,
\[
\boxed{
\begin{aligned}
W_C&=\sum_{i=1}^{h}P_{i-1}^{-1}
      (\rho_i^{-1}-1)(C_{i-1}+c_i),\\
W_Y&=\sum_{i=1}^{h}P_{i-1}
      (\rho_i-1)(Y_{i-1}+b_i).
\end{aligned}}
\tag{2}
\]
In particular, setting
\(X_i=P_{i-1}^{-1}(C_{i-1}+c_i)\) and
\(Z_i=P_{i-1}(Y_{i-1}+b_i)\), the scalar trace is an
**exact discrete defect flux**
\[
\boxed{
W_C+W_Y=
\sum_{i=1}^{h}(\rho_i-1)
   \left(Z_i-\rho_i^{-1}X_i\right).
}
\tag{3}
\]
There is **no division by** \(\rho_i-1\); every
degenerate case \(\rho_i=1\) vanishes automatically.
For \(u=1\), \(h=0\) and \(W=0\) by empty sums.

**Proof.** Let
\(x_i=F_i\cdots F_1(0,0)\) and
\(\widehat x_i=\widehat F_i\cdots\widehat F_1(0,0)\).
The telescoping identity for products of affine
maps gives
\[
x_h-\widehat x_h
=\sum_{i=1}^{h}
  \widehat D_h\cdots\widehat D_{i+1}
  (F_i(x_{i-1})-\widehat F_i(x_{i-1})),
\]
where
\(\widehat D_j=\operatorname{diag}(
 \widehat A_j,\widehat A_j^{-1})\).
The linear part of the inverse stable-prefix map
is \((\widehat D_h\cdots\widehat D_1)^{-1}\).
Therefore its image of the difference is
\[
W=\sum_i
 (\widehat D_i\cdots\widehat D_1)^{-1}
 (F_i(x_{i-1})-\widehat F_i(x_{i-1})).
\]
The coordinate differences are
\[
\begin{aligned}
F_i^C(x)-\widehat F_i^C(x)
   &=\widehat A_i(\rho_i^{-1}-1)(C+c_i),\\
F_i^Y(x)-\widehat F_i^Y(x)
   &=\widehat A_i^{-1}(\rho_i-1)(Y+b_i).
\end{aligned}
\]
Cancelling \(\widehat A_i\) gives exactly (2).
Adding the coordinates and factoring \(\rho_i-1\)
proves (3). QED.

**Interpretation.** The complete finite-defect trace
is a sum of *local mismatches*, transported only through
the preceding stable multipliers. It is not necessary
to invert a long affine product. Each term is determined
by the actual prefix, the current phase \(\rho_i\),
and a unit \(P_{i-1}\). This is a general algebraic
reduction independent of how large \(v\) is.

For the formerly solved \(u\mid20\) family all
\(\rho_i=1\) except potentially \(i=1\). The
Duhamel formula immediately reduces to
\[
W_C=\frac{10}{81}(\rho_1^{-1}-1),\qquad
W_Y=\frac1{81}(\rho_1-1),
\]
recovering the previously proved perfect-square
first-window witness (a useful structural consistency check).

## 2. The u=8 defect lies on one fixed hyperbola

For \(u=8\), the first three defect multipliers are
\(\rho_1=\rho\), \(\rho_2=\rho_3=-1\),
with \(\rho^4=-1\). The exact three-layer computation
already established in
\`u8_singular_norm_structure_2026-10-18.md\` yields
\[
W_C=-10/81+a\rho^{-1},\qquad
W_Y=-1/81+b\rho,
\tag{4}
\]
where
\[
a=\frac{10}{81}
 -\frac{219804400}{120758121\cdot10^{189}},\quad
b=\frac1{81}
 +\frac{217557800\cdot10^{189}}{120758121}.
\]
Multiplying the shifted coordinates now gives the
**phase-independent invariant**
\[
\boxed{
(W_C+10/81)(W_Y+1/81)=ab.}
\tag{5}
\]
Thus the entire family of finite-defect states,
as the primitive eighth-root phase varies, is
contained in **one fixed rectangular hyperbola**.
This is a stronger geometric description of the
previous coordinate formulas.

For the first long \(q=10\) window after \(pT\),
the admissible subgroup quadratic is
\[
10(W_C+10/81)z^2-\frac{20}{81}z
 +(W_Y+1/81)=0.
\]
By (5), its discriminant is the **fixed rational**
\[
\boxed{\mathcal D=(20/81)^2-40ab,}
\tag{6}
\]
independent of \(\rho,p,v\), although subgroup-root
membership is still sensitive to the multiplicative
order \(r\). This explains the rational discriminant
found independently in the earlier tail-gauge note.
A square discriminant alone does not imply a
root in \(\langle10\rangle\).

For the *singular* \(pT\)-digit window, in contrast,
the condition is
\[
k^2+E(\rho)=0,\qquad
E(\rho)=-11/81+a\rho^{-1}+b\rho.
\tag{7}
\]
Its squareclass depends on the phase.

## 3. Positive-density Galois mixing of formal u=8 phases

Put \(K=\mathbb Q(\zeta_8)=\mathbb Q(i,\sqrt2)\),
\(E=E(\zeta_8)\), and
\(N=\operatorname{Norm}_{K/\mathbb Q}(E)\in\mathbb Q^\times\).
The previously proved norm formula reads
\[
N=(a^2-b^2)^2+(2ab-121/6561)^2.
\tag{8}
\]

**Theorem 2 (positive-density mixed formal phases).**
There is a set of rational primes of natural density
**exactly \(1/8\)** for which \(p\equiv1\pmod8\),
all coefficients in (7) are defined modulo \(p\), and
among the **four primitive eighth roots**
\(\rho\in\mathbb F_p^\times\) the square characters
\(\chi_p(-E(\rho))\) include **both** \(+1\) and \(-1\).
In particular a purported proof that (7) is a square
*uniformly for all primitive eighth-root phases*
is impossible.

**Proof.** The exact coefficients satisfy
\[
(a,b,c=-11/81)\equiv(10,22,1)\pmod{41}
\quad\text{[correction: these are NOT the residues at 41]};
\]
for the actual argument we use the independently
computed, fully specified value
\[
\boxed{N\bmod41=26,\quad \chi_{41}(26)=-1.}
\]
Because \(41\equiv1\pmod8\), it splits completely
in \(K\), but \(N\) is nonsquare modulo 41.
Consequently \(\sqrt N\notin K\). Thus
\(L=K(\sqrt N)\) is a multiquadratic Galois
extension of \(\mathbb Q\) of degree 8.
The Chebotarev density theorem applied to the
Galois element fixing \(K\) and negating \(\sqrt N\)
produces a set of primes of density \(1/8\).
For each unramified such prime \(p\), we have
\(p\equiv1\pmod8\) and \(\chi_p(N)=-1\).
All four primitive eighth roots lie in \(\mathbb F_p\),
and since \(N=\prod_{\rho}E(\rho)\),
\[
\prod_{\rho\text{ primitive}}\chi_p(-E(\rho))
=\chi_p((-1)^4N)=-1.
\]
No factor vanishes because \(N\ne0\bmod p\).
Among four signs, a product \(-1\) entails
an odd number of negative signs, hence at least
one positive and one negative. QED.

**Crucial distinction:** the four \(\rho\)'s here are
**formal Galois-conjugate phases at the same split prime**.
For an actual target prime whose order has smooth part
\(u=8\), the decimal cocycle selects **one particular**
\(\rho=10^{9(10^T-1)}\). The theorem does not assert
that this particular \(\rho\) is among the failing
phases; it does **not** establish a positive density of
actual mountain-counterexample primes or even of
actual singular-window failures. It only proves a
strong structural obstruction to a phase-independent
square argument.

Small checks: at split \(p=41,73,97,137\),
the norm is a nonsquare; evaluating the four
conjugate phase characters yields signs
\[
\begin{array}{c|c}
p&(\chi_p(-E(\rho)))_{\rho\text{ primitive}}\\\hline
41&(-1,-1,+1,-1)\\
73&(+1,+1,+1,-1)\\
97&(-1,+1,-1,-1)\\
137&(+1,+1,+1,-1)
\end{array}
\]
after ordering roots increasingly. These are
checks of the universal field/norm formula,
not the proof of the density statement.

## 4. The remaining zero-drift gap

Equation (3) is an explicit arithmetic flux identity
for the **finite defect**, and (5) shows that a
fixed-smooth-part family may lie on a small-degree
algebraic variety. However the genuine zero-drift
condition \(\Delta=0\) constrains the **stable monodromy**,
not merely the finite-defect flux. There is still no
proved implication
\[
\Delta=0\ \Longrightarrow\
-\bigl(W_C+W_Y\bigr)\text{ is a square},
\]
nor does any proof here guarantee a root in another
stable window if this one fails.

The priority is therefore a *cross-constraint* between
the stable cocycle and the finite defect, rather than
another norm table, enlarged bounded-order computation,
or assumption that a single window is universal.

### Reproducibility

Run
\`python3 papers/A077187/research/audit_defect_duhamel_flux.py\`.

The standard-library audit compares the Duhamel formula
to an independent inverse affine prefix at 16 genuine
primes, and to \(2S_T-S_{2T}\) when \(T\le500\).
It also checks the \(u=8\) hyperbola and four
formal primitive-root character sets.
The dedicated
\`.github/workflows/a077187-duhamel-flux.yml\`
has passed. The unrestricted OEIS A077187
conjecture remains **OPEN**.
