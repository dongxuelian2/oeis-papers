# A077187: Möbius deck involution and exact phase-incidence counts

**2026-10-18 — PROVED universal finite-field theorem.**
Continuation of the stable-window phase and Lucas norm analysis.
The result is an **exact phase-count and collision classification**,
not an unrestricted all-primes proof and not a zero-drift solution.

## 1. The phase-incidence curve

Fix a prime \(p\ge7,\ p\ne11\),
\(r=\operatorname{ord}_p(10)\ge3\), and a full stable
post-boundary \(d=jT+1\) digit window. Let
\(\Delta=(U,V)\in\mathbb F_p^2\) denote the stable translation
and write \(t=j-1\bmod p\). The established local formula gives,
with \(z=10^n\in\mu_r\),
\[
Q_t(z)=a(z)+t\,b(z),\quad
a(z)=Az^2+Hz+B,\quad
b(z)=\alpha z^2+\beta,
\]
where \(H=-20/81\ne0,\ \alpha=10U,\ \beta=V\).
Every \(z\in\mu_r\) is attained by a valid window offset \(n\)
(the window length is greater than \(r\)).
If \(b(z)\ne0\), its **unique** successful block phase is
\[
\boxed{t(z)=-\frac{Az^2+Hz+B}{\alpha z^2+\beta}.}\tag{1}
\]
If \(a(z)=b(z)=0\) for any \(z\in\mu_r\), **all \(p\) phases**
succeed; such a root is independent of the block phase.
If \(b(z)=0\ne a(z)\), that \(z\) never contributes.

The case \(\Delta=0\) is entirely separate: \(b\equiv0\),
so the same window either succeeds in all \(p\) phases
(if \(a\) has a subgroup root), or fails in all of them.
The theorem below is for \(\Delta\ne0\).

## 2. Exact Möbius collision involution

Put
\[
D=A\beta-B\alpha,\qquad
\Lambda=D^2+H^2\alpha\beta.
\]

**Theorem 1 (degree-two deck involution).**
Suppose \((U,V)\ne0\) and no \(z\in\mu_r\) is a common
root of \(a,b\). For two *distinct* eligible
\(z,w\in\mu_r\) (both \(b\ne0\)), their phases coincide
if and only if
\[
\boxed{D(z+w)-H\alpha zw+H\beta=0.}\tag{2}
\]
If \(\Lambda\ne0\), all possible collisions are pairs
exchanged by the projective involution
\[
\boxed{\iota(z)=-\frac{Dz+H\beta}{D-H\alpha z}.}\tag{3}
\]
Its matrix
\[
M=\begin{pmatrix}-D&-H\beta\\-H\alpha&D\end{pmatrix}
\quad\text{satisfies}\quad M^2=\Lambda I.
\]
The involution need **not** preserve the whole multiplicative
subgroup: only eligible \(z\) for which
\(\iota(z)\in\mu_r\) actually collide.

If \(\Lambda=0\), the phase function (1) is
injective on all eligible subgroup points, so there are
no collisions.

**Proof.** Direct expansion gives
\[
a(z)b(w)-a(w)b(z)
=(z-w)\,[D(z+w)-H\alpha zw+H\beta].
\]
For \(z\ne w\), divide by the nonzero \(b(z)b(w)\)
to obtain (2). Solving the bilinear equation for \(w\)
gives (3), and direct multiplication yields \(M^2=\Lambda I\).
If \(\Lambda\ne0\), \(M\) represents a genuine involution
in \(\operatorname{PGL}_2(\mathbb F_p)\).

If \(\Lambda=0\), the rational function \(a/b\)
reduces to a nonconstant fractional-linear function:
when \(\alpha\beta\ne0\), the numerator and denominator
share a root \(z_0=D/(H\alpha)\); when \(\alpha=0\),
\(\Lambda=0\) forces \(A=0\) and the function is linear;
when \(\beta=0\), it forces \(B=0\), and the function is
a nonconstant affine function of \(z^{-1}\).
In each case it is injective on points where \(b\ne0\).
It cannot be constant since \(H\ne0\). QED.

## 3. Exact number of successful block phases using polynomial GCDs

Define polynomials over \(\mathbb F_p\):
\[
\begin{split}
P(X)&=X^r-1,\qquad b(X)=\alpha X^2+\beta,\\
F(X)&=(-DX-H\beta)^r-(D-H\alpha X)^r,\\
J(X)&=-H\alpha X^2+2DX+H\beta.
\end{split}
\]
Let
\[
n_0=\deg\gcd(P,b),\quad m=r-n_0.
\]
Because \(P\) is square-free and splits in \(\mathbb F_p\),
\(n_0\) is exactly the number of offsets with zero slope;
for \(\Delta\ne0\), \(n_0=0\) or
\(n_0=\gcd(r,2)\).

**Theorem 2 (phase-count polynomial formula).**
Under the assumptions of Theorem 1, the number \(N\)
of distinct successful phase classes \(t\bmod p\) is:
- If \(\Lambda=0\), \(\boxed{N=m}\).
- If \(\Lambda\ne0\), define
\[
\begin{aligned}
e&=\deg\gcd(P,F)-\deg\gcd(P,F,b),\\
f&=\deg\gcd(P,J)-\deg\gcd(P,J,b).
\end{aligned}
\]
Then
\[
\boxed{N=m-\frac{e-f}{2}.}\tag{4}
\]
In particular \(e-f\) is even and
\[
\boxed{\left\lceil\frac{m}{2}\right\rceil\le N\le m.}
\tag{5}
\]
If a common subgroup root of \(a,b\) exists, instead \(N=p\).
At \(\Delta=0\), \(N=p\) or \(0\) as noted above.

**Proof.** Eligible subgroup points are precisely the \(m\)
roots of \(P\) not annihilated by \(b\). When
\(\Lambda\ne0\), the condition
\(\iota(z)\in\mu_r\) is \(F(z)=0\), with the denominator-zero
case excluded automatically: if \(D-H\alpha z=0\),
then \(-Dz-H\beta\ne0\) because \(M\) is invertible.
The GCD-degree difference defining \(e\) counts precisely
eligible points with another point of their projective orbit
in \(\mu_r\). The fixed-point equation \(\iota(z)=z\)
is \(J(z)=0\), so \(f\) counts eligible fixed points.
If no universal root exists, the partner of an eligible point
is eligible whenever it belongs to \(\mu_r\):
\(b(w)=0\) would force \(a(w)=0\) by the cross-product
identity, contradicting the hypothesis.
Every non-fixed eligible pair is counted twice in
\(e-f\) and represents just one successful phase.
Subtracting their number from \(m\) gives (4).
For \(\Lambda=0\), injectivity was proved above.
The inequalities follow immediately. QED.

The formula does not scan phases \(t\) or enumerate subgroup
elements \(z\): it uses **finite-field polynomial GCDs**
with degrees at most \(r\). It is an exact, factorization-free
structural sharpening of the previous lower bound
\(N\ge\lceil(r-\gcd(2,r))/2\rceil\).

## 4. Meaning for the remaining conjecture

The rational phase map (1) is a degree-two cover of
\(\mathbb P^1\); its nontrivial deck transformation is
the Möbius involution (3). All duplications of
witness-producing phases arise from intersections
\(\mu_r\cap\iota(\mu_r)\), not from unexplained
numerical coincidences.

**Important limitation:** at true zero drift, \(b\equiv0\)
and the phase map collapses. Both the Fermat–Lucas double
norm and the Möbius cover then become constants, so neither
alone forces a root. The remaining universal question is
whether the **actual digit-layer cocycle** supplies a
separate identity implying that some stable-window norm
vanishes. No such identity is claimed here, and the
unrestricted A077187 conjecture remains OPEN.
