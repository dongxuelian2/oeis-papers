# A077187: a fixed-coprime-order spectral compression and the entire \(v=7\) family

**October 18, 2026. Status: new computer-assisted INFINITE order-family theorem.**
This research note extends the earlier \(v\mid9\) and smooth-order
classes. It does **not** solve the unrestricted all-primes conjecture.

## 1. The generic spectral reduction: arbitrary fixed coprime part \(v\)

Let \(p\ge7\) be prime with
\[
r=\operatorname{ord}_p(10)=uv,\quad
u=2^a5^c,\quad (v,10)=1.
\]
Set \(h=\operatorname{ord}_v(10)\) (take \(h=1\) for \(v=1\)),
\[
\boxed{\ell=\operatorname{lcm}(v,h),\quad
g=\gcd(r,\ell),\quad m=r/g,\quad T=m\ell.}\tag{1}
\]
Note \(v\mid g\mid\ell\). For **fixed \(v\)**, both \(\ell\)
and \(g\) are bounded independently of the unbounded powers \(2^a5^c\).
Put \(\zeta=10^m\bmod p\). Its order is exactly \(g\).

For the full \(d\)-digit layer let
\[
e_d=9d10^{d-1},\quad A_d=10^{e_d}\pmod p,\quad
q_d=10^d,\quad L_d=10^{d-1},\quad M_d=9L_d.
\]
All layers \(d\ge E=1+\max(a,c)\) are stable. In particular
\(u\mid e_d\), so \(A_d\in\mu_v=\langle 10^u\rangle\).

### Lemma 1: the multiplier and cumulative phase have period \(\ell\)

For every stable \(d\),
\[
\boxed{A_{d+\ell}=A_d,\qquad
\prod_{j=d}^{d+\ell-1}A_j=1\pmod p.}\tag{2}
\]
Indeed \(u\mid e_d,e_{d+\ell}\), and modulo \(v\) the difference of
exponents vanishes because \(v\mid\ell\) and
\(10^\ell=1\bmod v\). Hence \(r\mid e_{d+\ell}-e_d\).
Also
\[
9\sum_{j=d}^{d+\ell-1}j10^{j-1}
=(d+\ell-1)10^{d+\ell-1}-d10^{d-1}
-\sum_{j=d}^{d+\ell-2}10^j.
\]
Modulo \(v\), using \(10^\ell=1\) and
\(v\mid(10^\ell-1)/9\), the right side is
\(\ell10^{d-1}=0\). The \(u\)-part divides each summand,
so \(r\) divides the whole exponent. This proves (2).
The divisibility \(v\mid(10^\ell-1)/9\) follows from
\(v\mid\ell\), \(10^\ell\equiv1\bmod v\), with the
\(3\)-part handled by
\(v_3((10^\ell-1)/9)=v_3(\ell)\).

On the stable block \(T+1,\ldots,2T\), put
\(P_d=\prod_{j=T+1}^{d-1}A_j\).
Lemma 1 gives \(P_{d+\ell}=P_d\): **the cumulative phase
period is at most \(\ell\), not \(T\).**

### Lemma 2: collapse an entire coset of digit lengths

For an index \(a_0\in\{1,\dots,\ell\}\), the stable indices
\(d=T+a_0+j\ell\), \(0\le j<m\), share the same \(A\)
and \(P\). Their \(q_d=10^d\) run over all \(m\) roots of
\[
z^m=\zeta^{a_0}=:c.
\]
Define \(n_0=m-\mathbf 1_{c=1}\) and
\[
F_1=\sum_{z^m=c,\ z\ne1}\frac z{z-1},\qquad
F_2=\sum_{z^m=c,\ z\ne1}\frac z{(z-1)^2}.
\]
Direct logarithmic differentiation of \(z^m-c\) gives
\[
\boxed{
\begin{array}{c|c|c}
&F_1&F_2\\\hline
c\ne1&mc/(c-1)&m^2c/(c-1)^2\\
c=1&(m-1)/2&-(m^2-1)/12
\end{array}.}\tag{3}
\]
The \(c=1\) formulas follow by removing the root 1 from
\((z^m-1)/(z-1)\). Since \(p\ge7\) and \(m\mid p-1\),
the denominators are invertible.

For any nonsingular \(q\ne1\), with
\(B_d\) and \(R_d^*\) the ascending and descending layer words,
the exact geometric-sum identities give
\[
\begin{aligned}
B_d&=(A-1)\Bigl(1+\frac q{(q-1)^2}\Bigr)
          -\frac{M_d A}{q-1},\\
R_d^*&=(A-1)\Bigl(\frac{L_d}{q-1}
                     -\frac q{(q-1)^2}\Bigr)
          +\frac{M_d A}{q-1}.
\end{aligned}\tag{4}
\]
At \(q=1\), necessarily \(A=1\), \(L_d=1/10\),
\(M_d=9/10\); both layer words have the **same universal
singular residue**
\[
\boxed{B_d=R_d^*=\frac9{200}\pmod p.}\tag{5}
\]

Recall that \(U,V\) are the stable-period drift coordinates,
equivalently the two long oppositely ordered block words.
For the residue class \(a_0\), put
\[
\alpha=P^{-1}(1-A^{-1}),\quad \beta=P(A-1).
\]
The **complete coset contributions**, including the unique singular
layer when \(c=1\), are
\[
\boxed{\begin{aligned}
U_{a_0}
  &=\alpha(n_0+F_2)-\frac9{10}P^{-1}F_1
        +\mathbf1_{c=1}\frac9{200}P^{-1},\\
V_{a_0}
  &=\beta\Bigl(\frac1{10}F_1-F_2\Bigr)
        +\frac9{10}PAF_1
        +\mathbf1_{c=1}\frac9{200}P .
\end{aligned}}\tag{6}
\]
And \(U=\sum_{a_0=1}^{\ell}U_{a_0}\),
\(V=\sum_{a_0=1}^{\ell}V_{a_0}\).
Equation (6) follows from the exact reflected-word
decomposition and the elementary coset sums (3).

**Main structural consequence.** For fixed \(v\), these sums have
only \(\ell\) terms and both drift coordinates are polynomials in
\(m\) of degree **at most two**, with coefficients in
\(\mathbb Q(\zeta_g)\), where \(g\le\ell\) is bounded independently of
\(a,c\). This is a genuine **unbounded smooth-part compression**.

More explicitly, write \(\gamma=u^{-1}\bmod v\). Then
\[
\boxed{
A_{T+a_0}=
\zeta^{(g/v)\gamma\,9a_0\,10^{a_0-1}},\qquad
P_{T+a_0}=\prod_{b=1}^{a_0-1}A_{T+b}.}\tag{7}
\]
Only the finite parameters \(g\mid\ell\) and
\(\gamma\in(\mathbb Z/v)^\times\) enter the coefficient formulas.
Thus for any **fixed** \(v\), finitely many small cyclotomic
resultants control the entire infinite two-/five-smooth family.
The resultant need not be nonzero for every \(v\), and the general
case remains open.

## 2. A new infinite family: \(v=7\)

For \(v=7\), \(h=\operatorname{ord}_7(10)=6\) and
\(\ell=42\). Since \(u=2^a5^c\),
\[
\boxed{
g=\gcd(7u,42)=
\begin{cases}7&a=0,\\14&a\ge1.\end{cases}}\tag{8}
\]
For either \(g\), there are only six phases
\(\gamma=u^{-1}\bmod7\). Formula (6) produces
\[
U_\gamma(m)=U_0+U_1m+U_2m^2,\quad
V_\gamma(m)=V_0+V_1m+V_2m^2
\]
with coefficients in \(\mathbb Q(\zeta_g)\). Define
\[
\begin{aligned}
A&=U_2V_0-U_0V_2,\quad
B=U_2V_1-U_1V_2,\quad
C=U_1V_0-U_0V_1,\\
\mathcal R_{g,\gamma}(\zeta_g)&=A^2-BC.
\end{aligned}
\]
Simultaneous zero drift forces this resultant to vanish modulo \(p\).

### Exact low-degree certificate

The accompanying SymPy script performs exact arithmetic in
\(\mathbb Q[X]/\Phi_g(X)\) (degree \(\varphi(g)=6\)),
using **42 cosets, not \(T\) digit layers**.
For every \(\gamma=1,\dots,6\), it verifies the integer coefficients
of \(40000\mathcal R_{g,\gamma}\) and computes its exact norm:
\[
\boxed{\begin{aligned}
g=7:\quad N_7&=
33476324853960868807109434619064591936,\\
g=14:\quad N_{14}&=
114974543608404744933251944861980458578855689.
\end{aligned}}\tag{9}
\]
The six phases for each \(g\) share the same nonzero absolute norm;
their resultant polynomials need not be identical.
Denominators introduced by rational subgroup sums have support in
\(2,3,5,7\); no prime \(p\) of exact order \(7u\) equals
any of these. In particular, the final resultant is integral
after multiplication by 40000.

If a prime \(p\) with exact order \(r=7u\) had zero drift, then
\[
\boxed{p\mid N_g,\qquad r\mid p-1,\qquad
p\mid\Phi_r(10),\qquad p\nmid r.}\tag{10}
\]
Thus \(r<p\le N_g\). This reduces **unbounded** \(a,c\)
to a finite elimination of smooth-order indices bounded by
the *fixed six-degree norm*, not to a search over primes.

### Exact finite elimination without factoring either norm

The script verifies the identity
\[
\Phi_{7\cdot2^a5^c}(X)
=
\Phi_{7\cdot2^{[a>0]}5^{[c>0]}}
\!\left(X^{2^{\max(a-1,0)}5^{\max(c-1,0)}}\right).
\]
The base cyclotomic polynomial has degree at most 24.
For each \(r=7\cdot2^a5^c\le N_g\), compute
\[
h_r=\gcd(N_g,\Phi_r(10)).
\]
Repeatedly divide \(h_r\) by \(\gcd(h_r,r)\).
**Every residual equals 1.** This eliminates every possible
exact-order prime from (10), even if that prime is a factor of
the original norm. No primality proof or factorization of the
large norm numbers is used.

The exhaustive index counts, pinned in the checker, are
\[
\boxed{53\text{ cases with }a=0,\qquad
4479\text{ cases with }a\ge1.}
\]
These checks are **not** a growing brute-force search for witnesses:
they constitute a finite algebraic resultant exclusion, of fixed
size once \(v=7\) is fixed.

### Theorem (complete \(7\)-coprime-part infinite family)

For every prime \(p\) with
\[
\boxed{\operatorname{ord}_p(10)=7\cdot2^a5^c,\quad a,c\ge0}
\]
the stable drift is nonzero. Therefore, by the previously proved
two-offset linear congruence, there exist
\(1\le j\le p\) and \(\varepsilon\in\{0,1\}\) such that
\[
\boxed{p\mid M(10^{jT}+\varepsilon),\quad
T=\operatorname{lcm}(
7\cdot2^a5^c,\operatorname{ord}_7(10))
=\operatorname{lcm}(7\cdot2^a5^c,6).}
\]
**Proof.** The spectral compression and resultant calculation imply
(10) whenever drift is zero. The exhaustive exact finite cyclotomic
elimination excludes (10) for all \(a,c\). Thus drift is nonzero.
The two-offset theorem applies. QED.

This is an infinite-order-class result and includes unbounded
powers of 2 and 5 with a prime factor 7 in the multiplicative order.
It does **not** claim the result for arbitrary \(v\).

## 3. Independent prime-field checks and proof status

A separate field-level audit checks the compressed formula and original
full \(2T\)-layer recurrence for primes including
\(29,71,113,239,421,701,7841,17921\).
These samples are consistency tests, not the proof of the infinity
claim; the proof rests on the exact symbolic norm and finite exclusion.

Reproduce from the repository root:
\`\`\`sh
python3 -m pip install sympy
python3 papers/A077187/research/certify_fixed_v7.py
python3 papers/A077187/research/audit_fixed_v7.py
\`\`\`

The exact algebraic claim and scripts are submitted for independent
mathematical review. OEIS A077187 in its unrestricted all-primes form
remains OPEN. For other fixed coprime parts \(v\), the same algebra
offers a finite-dimensional framework, but each case still requires
nondegeneracy and elimination.
