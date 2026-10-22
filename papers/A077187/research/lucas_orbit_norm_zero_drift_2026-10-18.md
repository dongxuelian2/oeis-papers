# A077187: an intrinsic orbit norm for every digit window

**2026-10-18. Status: universal algebraic identities and an exact
prime-specific zero-drift criterion. The all-primes conjecture is OPEN.**

This is a continuation of the updated \`HANDOFF.md\`,
\`general_dynamics.md\`, and \`zero_drift_continuation_2026-10-18.md\`.
It intentionally avoids increasing finite prime/order cutoffs.
The new result replaces square-root plus discrete-log-style subgroup
analysis by a **single scalar norm** per complete digit window. It does
not assert that one of those norms must vanish.

## 1. A cyclic resultant built from the first integral

Let \(p\ge7\) be prime, \(p\ne11\), and put
\(r=\operatorname{ord}_p(10)\). At the start of a \(d\)-digit
window, write
\[
 L=10^{d-1},\quad q=10^d,\quad (C,Y)=
 (C_{L-1},10^{-D(L-1)}R_{L-1})\pmod p.
\]
For \(q\ne1\), let \(h=\operatorname{ord}_p(q)=
r/\gcd(r,d)\) and define
\[
\begin{aligned}
 A&=q\left(C+\frac{L}{q-1}+\frac1{(q-1)^2}\right),\\
 B&=Y-\frac{L}{q-1}+\frac q{(q-1)^2},&
 H&=-\frac{2q}{(q-1)^2}.
\end{aligned}
\tag{1}
\]
The established within-window calculation gives for \(k=L+n\)
\[
 \frac{M(k)}{10^{D(k-1)}}=Aq^n+Bq^{-n}+H.
 \tag{2}
\]
For a **complete \(h\)-step orbit**, \(z=q^n\) runs exactly through
\(\mu_h\subset\mathbb F_p^\times\).
Consequently a divisible mountain is present in this orbit iff
\[
 Q(z)=Az^2+Hz+B
 \quad\text{shares a root with }z^h-1.
\]

**Theorem 1 (Lucas orbit-norm identity).** Define
\[
L_0=2,\qquad L_1=-H,\qquad
L_j=-H L_{j-1}-AB L_{j-2}\quad(j\ge2).
\]
Then in **every** field of odd characteristic,
\[
\boxed{\quad
 \mathcal N_h(A,H,B)
 :=\operatorname{Res}_z(z^h-1,Az^2+Hz+B)
 =A^h+B^h-L_h.
 \quad}\tag{3}
\]
In particular,
\[
\boxed{\text{the full window orbit contains a root}
 \iff \mathcal N_h(A,H,B)=0.}\tag{4}
\]
No modular square root, discrete logarithm, or enumeration of the
multiplicative subgroup is required.

**Proof.** Over a splitting extension and initially with \(A\ne0\),
factor \(Az^2+Hz+B=A(z-\alpha)(z-\beta)\).
Then \(\alpha+\beta=-H/A,\ \alpha\beta=B/A\), and
\[
\prod_{z^h=1}Q(z)
 =A^h(\alpha^h-1)(\beta^h-1)
 =A^h+B^h-A^h(\alpha^h+\beta^h).
\]
The last trace \(A^h(\alpha^h+\beta^h)\) satisfies precisely the
recurrence for \(L_h\). Both sides of (3) are polynomials in
\(A,H,B\) with integer coefficients, so the identity extends to
\(A=0\), \(B=0\), repeated roots and all other degeneracies.
Since \(h\mid p-1\), the roots of \(z^h-1\) in \(\mathbb F_p\)
are all distinct and are exactly \(\langle q\rangle\).
Thus their product vanishes iff an admissible root exists. QED.

Equivalently, introduce the \(2\times2\) transfer matrix
\[
K=\begin{pmatrix}-H&-AB\\1&0\end{pmatrix},
\qquad L_h=\operatorname{tr}(K^h).
\]
Equation (3) becomes
\[
\boxed{\mathcal N_h=A^h+B^h-\operatorname{tr}(K^h).}
\tag{5}
\]
It can be evaluated with \(O(\log h)\) field multiplications by
binary matrix powering. Alternatively, if \(S\) is the cyclic
permutation matrix of dimension \(h\), then
\(\mathcal N_h=\det(AS^2+HS+BI_h)\). This realizes the local
mountain condition as a genuine **cyclic group-algebra norm**.

**Theorem 2 (orbit-gauge invariance).** For every \(s\in\mathbb Z\),
\[
\boxed{\mathcal N_h(Aq^s,H,Bq^{-s})
                  =\mathcal N_h(A,H,B).}
\tag{6}
\]
Indeed \((q^s)^h=1\) and \(AB\) is unchanged, so (3) proves
the identity. Thus the scalar depends on the *unlabelled cyclic
orbit*, not on the selected starting offset. This is the natural
intrinsic replacement for testing particular \(n\)'s in the
hyperbola-line intersection formulation.

There are at most two distinct admissible residue classes
\(n\bmod h\) in any nonsingular window: \(Q\) is nonzero because
\(H=-2q/(q-1)^2\ne0\). This bound includes \(A=0\) or \(B=0\).

## 2. Singular windows are a separate finite-field norm

When \(q=1\), the earlier window formula is
\[
\frac{M(L+n)}{10^{D(L+n-1)}}=(L+n)^2+K,\qquad
 K=C+Y+L-L^2.
\tag{7}
\]
For any full period \(n\bmod p\), the values \(L+n\) range
over \(\mathbb F_p\). The exact singular orbit product is
\[
\boxed{
 \mathcal N_{\rm sing}(K)
 =\prod_{x\in\mathbb F_p}(x^2+K)
 =2K\bigl(1-(-K)^{(p-1)/2}\bigr).
}\tag{8}
\]
It vanishes exactly when \(-K\) is a quadratic residue, **including
zero**. To prove (8), if \(-K\) is a square the product is zero.
Otherwise let \(\alpha^2=-K\) in \(\mathbb F_{p^2}\);
Frobenius sends \(\alpha\) to \(-\alpha\), and
\(\prod_{x\in\mathbb F_p}(x^2+K)
=-(\alpha^p-\alpha)^2=4K\), agreeing with (8).
No division by a possibly zero coordinate occurs.

Every complete singular window also has at most two roots
\(n\bmod p\), counting distinct roots.

## 3. One scalar for the *entire* zero-drift stable orbit

Use the newly audited reduced-phase period from the updated PR:
\[
r=uv,\quad u=2^a5^c,\quad \delta=\gcd(v,9),\quad
t=v/\delta,\quad
T=\operatorname{lcm}(r,\operatorname{ord}_t(10)),
\quad \operatorname{ord}_1(10)=1.
\tag{9}
\]
The reduced-phase lemma proves that the full affine digit-layer maps
repeat after \(T\) in the stable range, and the \(T\)-layer composite
is a translation. Let
\[
\Delta_p=S_{2T}-S_T\in\mathbb F_p^2,
\quad S_d=(C_{10^d-1},Y_{10^d-1}).
\]
Assume \(\Delta_p=(0,0)\). Then the state at every later digit-layer
boundary satisfies
\[
\boxed{S_{d+T}=S_d\quad\text{for all }d\ge T.}\tag{10}
\]
This follows inductively from \(S_{2T}=S_T\) and the
periodicity \(F_{d+T}=F_d\) of the actual stable layer maps.

For each \(d=T+1,\ldots,2T\), evaluate its window norm:
\[
\mathcal R_d=
\begin{cases}
  \mathcal N_{r/\gcd(r,d)}(A_d,H_d,B_d),
       &10^d\ne1\pmod p,\\
  \mathcal N_{\rm sing}(K_d),&10^d=1\pmod p.
\end{cases}
\]
Finally define the **whole-period orbit norm**
\[
\boxed{\mathfrak O_p=\prod_{d=T+1}^{2T}\mathcal R_d
 \ \in\mathbb F_p.}\tag{11}
\]

**Theorem 3 (exact full stable-cycle criterion).**
Under the hypothesis \(\Delta_p=0\),
\[
\boxed{
\mathfrak O_p=0\ \Longleftrightarrow\
\exists k\text{ in any stable digit window with }p\mid M(k).
}\tag{12}
\]
If one such \(k\) exists then infinitely many different such
mountains exist, by shifting the digit length by \(T\).

**Proof.** Every reference window has length
\(9\cdot10^{d-1}>p\) for \(d>T\ge r\),
since \(p\mid10^r-1\). Hence each nonsingular reference
window contains every \(n\bmod h\), and each singular window
contains every \(n\bmod p\). Theorems 1 and (8) show that
\(\mathcal R_d=0\) iff that entire digit window contains a
divisible mountain. Their product is zero iff at least one
such window does. By (10), the state and all field parameters
of the \(d+T\) window repeat the \(d\) window, so the same
offset solutions recur at arbitrarily large digit lengths. QED.

**Exact counterexample characterization (not a claim of existence).**
A prime \(p\ge7,\ p\ne11\) that divides no mountain must have:
(i) \(\Delta_p=0\); (ii) \(\mathfrak O_p\ne0\);
and (iii) no witness among the finitely many early digit windows
\(1\le d\le T\), tested at their actual finite offsets.
Conversely all three conditions suffice to establish such a
counterexample. (Nonzero drift already guarantees witnesses by
the established two-offset theorem.)

This compresses all *late* zero-drift root questions into a **single
precisely defined field scalar**. It does **not** prove the scalar must
vanish under zero drift: the additional implication
\[
\boxed{\Delta_p=0\ \Longrightarrow\ \mathfrak O_p=0}
\tag{13}
\]
is a **new sufficient target**, currently OPEN. The prior
positive-density three-window obstruction does not address (13),
because (13) uses *every phase of the stable period* and only claims
a conclusion conditional on actual zero drift.

## 4. What genuinely remains difficult

The updated \`HANDOFF.md\` rules out simply increasing the number of
fixed transient windows: their squareclasses can be independent,
and the three-window assertion was disproved for a positive-density
set of primes. The orbit norm above avoids this specific defect,
but replacing \(T\) separate norms by a **bounded-dimensional
expression** would require an additional relation between stable
window states across the reduced \(\ell\)-phase cosets.
Unlike their layer multipliers, the affine inhomogeneous terms
vary with \(q_d=10^d\); their partial sums are not generally
short-periodic. No such relation has been proved.

The two possible structural routes are consequently sharply
distinguished:
- Prove nonzero primitive drift, e.g. by a uniform cyclotomic
  Bezout identity; or
- Prove the zero-drift-to-orbit-norm implication (13), which must
  exploit the **actual concatenation cocycle**, not only abstract
  periodicity.

Theorems 1--3 and their O(log h) algorithm are proved for arbitrary
multiplicative orders; the unrestricted A077187 existence conjecture
is **not solved**.
