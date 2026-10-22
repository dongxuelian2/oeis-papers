# A077187: two-way block words, integrable digit layers, and witness multiplicity

**October 18, 2026 — PROVED structural results. The unrestricted OEIS conjecture remains OPEN.** This continuation emphasizes mathematical organization rather than larger finite-order searches.

## Theorem A: drift equals opposite-order block concatenations

Fix an integer \(r\ge2\), put \(N_r=10^r-1\), write
\(r=2^a5^cv,\ (v,10)=1\), and let
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\).
Let \(C_k=1\Vert\cdots\Vert k\), \(R_k=k\Vert\cdots\Vert1\),
\(D(k)=\sum_{j=1}^k\ell_{10}(j)\), \(Y_k=10^{-D(k)}R_k\)
modulo \(N_r\), and \(S_d=(C_{10^d-1},Y_{10^d-1})\).

Define the following **finite integers** (the reversal changes the
order of the integer blocks, **not the individual decimal digits**):
\[
\begin{split}
W^\uparrow_r&=10^T\Vert(10^T+1)\Vert\cdots\Vert(10^{2T}-1),\\
W^\downarrow_r&=(10^{2T}-1)\Vert\cdots\Vert(10^T+1)\Vert10^T .
\end{split}
\]

**Theorem.** For **every integer \(r\ge2\)**,
\[
\boxed{(U_r,V_r):=S_{2T}-S_T
\equiv(W^\uparrow_r,W^\downarrow_r)\pmod{10^r-1}.}
\]

**Proof.** Let \(K_0=10^T-1,\ K_1=10^{2T}-1\), and
\(H=D(K_1)-D(K_0)=9\sum_{d=T+1}^{2T}d10^{d-1}\).
The previously proved stable-period lemma implies \(r\mid H\),
so \(10^H=1\pmod{N_r}\).
The two concatenation identities hold as *ordinary integers*:
\[
C_{K_1}=10^H C_{K_0}+W^\uparrow_r,\quad
R_{K_1}=W^\downarrow_r\,10^{D(K_0)}+R_{K_0}.
\]
Normalize the second and subtract the two states:
\(Y_{K_1}=10^{-H}(W^\downarrow_r+Y_{K_0})\).
Since \(10^H=1\), the claimed difference follows. QED.

**Consequence.** For any prime \(p\) of exact order \(r\),
zero drift is *equivalent* to simultaneous divisibility of the two
oppositely ordered block words. The genuine primitive obstruction is
therefore
\[
\gcd(\Phi_r(10),W^\uparrow_r,W^\downarrow_r),
\]
whose prime factors not dividing \(r\) are precisely the true-order
zero-drift primes. This reformulation is unconditional; the desired
coprimality statement for all \(r\) is still **unproved**.

## Theorem B: integrability of every constant-length digit window

For any modulus coprime to 10, inside one \(d\)-digit interval set
\(q=10^d\). The exact step recurrence is
\[
C_{k+1}=q C_k+(k+1),\qquad
Y_{k+1}=q^{-1}(Y_k+k+1).
\]
Introduce **polynomial** centered coordinates
\[
\boxed{\begin{aligned}
X_q(k)&=(q-1)^2C_k+k(q-1)+q,\\
Z_q(k)&=(q-1)^2Y_k-k(q-1)+1 .
\end{aligned}}\tag{1}
\]
Substitution gives the *exact* diagonal semiconjugacy
\[
\boxed{X_q(k+1)=qX_q(k),\quad
Z_q(k+1)=q^{-1}Z_q(k),\quad X_q(k)Z_q(k)=I_q.}\tag{2}
\]
Over a field the coordinate change is invertible whenever \(q\ne1\).
When \(q=1\), equations (1) are still valid but degenerate; do not
mistake the semiconjugacy for an invertible coordinate transformation.

The normalized mountain residue has the universal identity
\[
\boxed{(q-1)^2\frac{M(k+1)}{10^{D(k)}}
=qX_q(k)+Z_q(k)-2q.}\tag{3}
\]
Indeed \(M(k+1)/10^{D(k)}=qC_k+Y_k+k+1\);
expanding (1) immediately gives (3).

For \(q\ne1\) modulo a prime, the mountain condition is equivalent to
intersecting an invariant hyperbola with a line:
\[
XZ=I_q,\qquad qX+Z=2q.
\]
Writing \(t=qX\) gives
\[
\boxed{(t-q)^2=q(q-I_q).}\tag{4}
\]
A necessary discriminant condition is that \(q(q-I_q)\) be a quadratic
residue (including zero). It is *not sufficient* without orbit
membership: \(X\) must lie in \(X_0\langle q\rangle\).
This is a geometric explanation of the earlier subgroup-root tests.

When \(q=1\), the scaled identity (3) loses information. The direct
recurrence instead gives the previously established polynomial
\[
(n+L)^2+C+Y+L-L^2,\qquad L=10^{d-1},
\]
for the normalized mountain at \(k=L+n\), with \((C,Y)\) the
pre-window state.

**Explicit interface dynamics.** At a digit-length boundary
\(k=10^d-1\), put \(q'=10q\), \(a=q-1\), \(b=q'-1\). If \(a\ne0\)
modulo the prime, write \(\lambda=(b/a)^2\). The coordinates at the
*same state*, before and after switching the digit width, satisfy
\[
\begin{aligned}
X_{q'}(k)&=\lambda X_q(k)+k(b-\lambda a)+q'-\lambda q,\\
Z_{q'}(k)&=\lambda Z_q(k)-k(b-\lambda a)+1-\lambda.
\end{aligned}\tag{5}
\]
Thus global dynamics consists of invertible diagonal motion inside
each nonsingular digit window and explicit affine interface maps,
with separate unipotent \(q=1\) windows. Each local \(I_q\) is
conserved inside a window, **not across interfaces**.

## Theorem C: reflected-block cancellation and singular-layer flux

For a full \(d\)-digit layer let \(L=10^{d-1}\),
\(m=9L\), \(q=10^d\), \(A=q^m\), and
\(S=\sum_{i=0}^{m-1}q^i\). The increasing and descending block integers
are, respectively,
\[
B_d=\sum_{i=0}^{m-1}(L+i)q^{m-1-i},\quad
R_d^*=\sum_{i=0}^{m-1}(L+i)q^i .
\]
Pairing \(i\) with \(m-1-i\) uses
\(L+m-1=q-1\), giving the **exact integer reflection identity**
\[
\boxed{B_d+R_d^*=(L+q-1)S.}\tag{6}
\]
The full-layer map \(C'=AC+B_d,\ Y'=A^{-1}(Y+R_d^*)\)
therefore has the exact twisted scalar relation
\[
\boxed{C'+AY'-AC-Y=(L+q-1)S.}\tag{7}
\]
In particular the weighted first-moment sum \(J\) cancels completely.
For a prime field with \(A=1\):
- If \(q\ne1\), \(S=0\) and \(C'+Y'=C+Y\).
- If \(q=1\), \(S=m=9L\) and the scalar jump is
  \(9L^2=9/100\).

This rederives the earlier \(v\mid9\) drift invariant conceptually,
as a **single singular-window contribution**. When \(A\ne1\),
the varying twists prevent naive telescoping of (7); that is a
concrete missing step, not an established cancellation.

## Theorem D: almost every small offset gives infinitely many witnesses

Let \(p\ge7,\ p\ne11\), with \(r=\operatorname{ord}_p(10)\ge3\).
Let \(T\) be the stable period and suppose \((U,V)\ne(0,0)\).
For each \(n\in\{0,\dots,r-1\}\), the normalized residue of
\(M(10^{jT}+n)\) is affine in \(j\) and has slope
\[
\boxed{\sigma_n=10^{n+1}U+10^{-n}V.}\tag{8}
\]

**Theorem.** At most \(\gcd(2,r)\) of the \(r\) slopes vanish.
For every other offset \(n\), a *unique residue class of*
\(j\bmod p\) produces a divisible mountain; there is a representative
\(1\le j\le p\), and \(j\mapsto j+mp\) provides infinitely many
different mountains. In particular, at least
\[
\boxed{r-\gcd(2,r)}
\]
distinct fixed-offset families of divisible mountains exist
whenever the drift is nonzero.

**Proof.** Since \(S_{jT}=S_T+(j-1)(U,V)\), the \(n\) subsequent
insertions in the next digit window send initial-state differences to
\((10^nU,10^{-n}V)\); the mountain residue adds another factor 10 to
the ascending coordinate, proving (8). A nonzero affine slope has one
zero in \(\mathbb F_p\). If \(U=0\), \(V\ne0\) makes every slope
nonzero. Otherwise \(\sigma_n=0\) iff
\(10^{2n+1}=-V/U\). The map \(n\mapsto10^{2n+1}\) on the cyclic group
of order \(r\) has fibers of size \(\gcd(2,r)\), so it has either no
solutions or that many. QED.

This replaces the earlier two-offset *existence* observation by a
quantitative picture of the entire affine family. It does not prove
nonzero drift for arbitrary primes.

## Research bottleneck

The unrestricted conjecture would follow from ruling out a genuine
primitive prime common to both block words of Theorem A, but no such
unbounded-order argument is known. A distinct path is to show that if
this common prime exists, at least one invariant hyperbola in a stable
digit-layer cycle still intersects the corresponding mountain line
in an **attainable subgroup orbit** (Theorem B).

The mathematical source of difficulty is now explicit: the
interface maps and \(A\ne1\) twists (Theorem C), **not** the
integrable within-layer dynamics. Finite order-bound experiments are
orthogonal to that missing global argument. No full proof of
A077187 is claimed.


## 6. Exact whole-period twisted-reflection decomposition (new)

The layerwise reflection identity (7) can be promoted to a **precise
global formula** showing exactly which phase mismatch prevents naive
telescoping.

Work in \(R=\mathbb Z/(10^r-1)\), with the stable block
\(d=e,\ldots,e+T-1\), \(e=T+1\). For each layer set
\[
m_d=9\cdot10^{d-1},\quad h_d=dm_d,\quad
q_d=10^d,\quad L_d=10^{d-1},\quad
A_d=10^{h_d},
\]
and write \(B_d\), \(R_d^*\), \(\Sigma_d\) for its increasing word,
decreasing word, and geometric sum as in Theorem C. Define the
**position phase**
\[
P_d=10^{\sum_{i=e}^{d-1}h_i},\qquad
\Theta_d=P_d^2 A_d
       =10^{\,2\sum_{i=e}^{d-1}h_i+h_d}.
\]
Every \(P_d\) and \(A_d\) is a unit in \(R\), and the total product of
the \(A_d\)'s is 1.

**Theorem E (twisted reflection/flux identity).** For every integer
\(r\ge2\) and **every scalar \(\lambda\in R\)**,
\[
\boxed{
\lambda U_r+V_r=
\sum_{d=e}^{e+T-1}
P_d\left[
 (L_d+q_d-1)\Sigma_d
 +(\lambda\Theta_d^{-1}-1)B_d
\right]\quad\text{in }R.}
\tag{9}
\]

**Proof.** Let \(W^\uparrow,W^\downarrow\) be the block words in
Theorem A. In the increasing word, the entire \(d\)-layer integer
\(B_d\) is followed by \(\sum_{i>d}h_i\) decimal digits. Since the
total block digit count is divisible by \(r\), its weight modulo \(R\)
is \((P_d A_d)^{-1}=P_d\Theta_d^{-1}\). In the decreasing word, the
entire \(d\)-layer integer \(R_d^*\) is followed by
\(\sum_{i<d}h_i\) decimal digits, giving weight \(P_d\).
Theorem A therefore yields
\[
U_r=\sum_d P_d\Theta_d^{-1}B_d,\qquad
V_r=\sum_d P_d R_d^* .
\]
Insert the exact reflection relation
\(R_d^*=(L_d+q_d-1)\Sigma_d-B_d\).
Collect coefficients of \(B_d\) to obtain (9). QED.

This works for \(\lambda=1\), targeting the scalar drift
\(U_r+V_r\), and \(\lambda=10\), targeting the single-offset
slope \(10U_r+V_r\). No field assumption, division by \(q_d-1\),
or finite computational certificate is needed.

**What the formula does and does not accomplish.**
For the already-proved \(v\mid9\) class, every stable \(A_d=1\).
Hence every \(P_d=\Theta_d=1\), so the entire mismatch sum
for \(\lambda=1\) vanishes. Also \(\Sigma_d=0\) when
\(q_d\ne1\), while the unique \(q_d=1\) phase contributes \(9/100\)
modulo a prime of exact order \(r\). Thus (9) recovers the existing
elementary nonvanishing invariant **as a global reflected-word
identity**, rather than a fortuitous cancellation of a first-moment
formula.

For general \(r\), however, \(A_d\), \(P_d\), and \(\Theta_d\) vary,
and there is no known reason that
\(\sum_dP_d(\Theta_d^{-1}-1)B_d\) vanishes or avoids canceling
the reflected baseline. **Controlling this explicit mismatch is
a genuinely open global step.** Equation (9) by itself does not
prove the empirical scalar GCD identities.

### Cyclic digit-profile / Fourier reformulation

There is also a completely finite group-ring representation of the
two block words. If \(w=\sum_{\ell\ge0}b_\ell10^\ell\) is any decimal
integer (least-significant digits indexed first), define its cyclic
digit profile
\[
a_j^{(r)}(w)=\sum_{\ell\equiv j\pmod r}b_\ell,\quad
P_w^{(r)}(X)=\sum_{j=0}^{r-1}a_j^{(r)}(w)X^j .
\]
Then
\[
\boxed{w\equiv P_w^{(r)}(10)\pmod{10^r-1}.}
\]
For \(w=W^\uparrow_r,W^\downarrow_r\), a prime of exact order \(r\)
has zero drift precisely when the two cyclic digit-profile
polynomials both vanish at the primitive root \(X=10\) in
\(\mathbb F_p\). This is a **simultaneous cyclic Fourier-zero
problem**, with the layerwise reflected-word relation (9) coupling
its two profiles. It is an equivalent reformulation, not an
independent nonvanishing proof.


### Maximality of the phase-free family

The \(v\mid9\) theorem is not an arbitrary convenient subfamily: it
is **exactly the case in which the position-phase mismatch disappears
identically at every stable layer.**

**Proposition.** Let \(p\ge7,\ p\ne11\) be prime with exact order
\(r=2^a5^cv\), and let \(d=e,\dots,e+T-1\) be the stable block
above. Then the following are equivalent:

1. \(v\mid9\);
2. \(A_d=1\pmod p\) for every \(d\) in the stable block;
3. \(\Theta_d=1\pmod p\) for every \(d\) in the stable block.

**Proof.** For stable \(d\), the smooth factor \(u=2^a5^c\)
divides \(10^{d-1}\). Since \(r=uv\), \(u\) and \(v\) are coprime,
and \((v,10)=1\),
\[
A_d=10^{9d10^{d-1}}=1\pmod p
\iff r\mid9d10^{d-1}\iff v\mid9d .
\]
Thus \(v\mid9\) forces (2). Conversely, if (2) holds for the two
consecutive indices \(e,e+1\), then \(v\mid9e\) and
\(v\mid9(e+1)\), so \(v\mid\gcd(9e,9(e+1))=9\).
This proves (1) iff (2).

If (2) holds, then \(P_d=\prod_{i=e}^{d-1}A_i=1\), hence
\(\Theta_d=P_d^2A_d=1\), proving (3).
Conversely \(\Theta_e=A_e=1\), and if \(\Theta_d=1\)
then \(P_d=1\) inductively, so
\(A_d=\Theta_d/P_d^2=1\) and
\(P_{d+1}=P_dA_d=1\). Thus (3) implies (2). QED.

Consequently the reflection cancellation mechanism underlying
the \(9/100\) invariant is **maximal among all subfamilies in which
every individual stable layer is untwisted**. Extending the argument
to \(v\nmid9\) requires a genuinely global cancellation or
nonvanishing analysis of the varying phase factors; it cannot be
obtained by simply adding more untwisted layers.
