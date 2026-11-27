# Unified algebraic–analytic structure and new exclusions for A060405

Write \(a_n=L_n+P_n\), extended to integer indices. For odd \(n\), set
\(u=\alpha^n\) and \(v=\beta^n\), where \(\alpha=(1+\sqrt5)/2\) and
\(\beta=1+\sqrt2\), and define the double cover
\[
 S:\quad x^2 = f(u,v) := (u-u^{-1})+\frac{1}{2\sqrt2}(v+v^{-1})
\]
over \(K=\mathbb Q(\sqrt2,\sqrt5)\). This note classifies all monomial
splitting curves on \(S\), derives strengthened Gaussian and mixed-unit
divisor exclusions (including unconditional one-step prime forcing on
the odd branches \(r=\pm3\)), records the odd-offset Frobenius
corollaries, and describes the \(p=19,307\) double-root geometry and
5-adic splitting on the zero-anchor branch.

## 1. Complete classification of monomial splitting curves

A binomial-factor norm identity
\(U(u,v)^2 - D f(u,v) W(u,v)^2 \equiv 0 \pmod{c u^p v^q - 1}\)
of arbitrary degree requires \(f(u,v)\) restricted to the monomial curve
\(u^p v^q = c^{-1}\) (\(\gcd(p,q)=1\), \(c\in\mathbb C^\times\)) to
take the form \(C t^e g(t)^2\) in \(\mathbb C[t^{\pm1}]\).

**Theorem 1 (Splitting-curve completeness).** Over \(\mathbb C\), a
monomial curve \(u^p v^q = c^{-1}\) (\(\gcd(p,q)=1\)) gives
\(f|_{u^p v^q = c^{-1}} = C t^e g(t)^2\) precisely in four families:
1. \((p,q)=(0,1)\), where \(P_n=\pm 2i\), recovering the Gaussian
   factorization of [norm descent](norm-descent.md) §2;
2. \((p,q)=(1,0)\), where \(\sqrt2\,L_n=\pm 1\), giving the dual
   \(\mathbb Z[\sqrt2]\) norm identity below;
3. \((p,q)=(1,\pm 1)\), giving the two mixed-unit norm identities below;
4. \((p,q)=(2,\pm 1)\), where \(v=\pm u^{\pm 2}\), recovering
   [norm descent](norm-descent.md) §3.

**Proof.** Parameterize \(u^p v^q=c^{-1}\) by \((u,v)=(a_0 t^q, b_0 t^{-p})\).
The four monomial exponents of \(f\) are \(\pm q,\pm p\).
When \(pq\ne 0\) and \(|p|\ne |q|\), these four exponents are distinct.
By the symmetries \(t\mapsto t^{-1}\) and \(u\leftrightarrow v\), write
\(M=\max(|p|,|q|)\), \(m=\min(|p|,|q|)\), \(k=M-m>0\), and
\(P(t)=t^M f(t)=u_0 t^{2M}+u_1 t^{M+m}+u_2 t^{M-m}+u_3\) with
\(u_0 u_1 u_2 u_3\ne 0\). Since \(P(0)\ne 0\), \(f=C t^e g(t)^2\) holds
precisely when \(P(t)\) is a polynomial square \(h(t)^2\) of degree \(M\).
Rescaling \(t\) and \(P\) gives \(P(t)=t^{2M}+2\lambda t^{M+m}+u_2' t^{M-m}+u_3'\)
with \(\lambda\ne 0\). Matching coefficients from \(t^{2M}\) down to
\(t^M\) uniquely forces \(h(t)=t^M\sum_{j=0}^{\lfloor M/k\rfloor}\binom{1/2}{j}(2\lambda)^j t^{-jk}\).
Because \(u_3'=h(0)^2\ne 0\), the constant term is nonzero, forcing
\(k\mid M\). Since \(\gcd(M,k)=\gcd(M,m)=1\), we obtain \(k=1\) and
\(m=M-1\). The leading remainder term of \(h(t)^2\) below \(t^M\) lies at
\(t^{M-1}\) with nonzero coefficient \(-2\binom{1/2}{M+1}(2\lambda)^{M+1}\).
For this remainder to match \(u_2' t^{M-m}=u_2' t\), we need \(M-1=1\),
so \((m,M)=(1,2)\). Checking \((1,2)\) in both orientations:
\((p,q)=(2,\pm 1)\) realizes the square with \(v=\pm u^{\pm 2}\),
whereas \((p,q)=(1,\pm 2)\) fails the coefficient ratio \(u_0 u_3 / (u_1 u_2)\)
by a factor of 64. The remaining boundary cases are \(pq=0\) and
\(|p|=|q|\), giving Families (1), (2), and (3). \(\square\)

In the even-index regime, Family (1) shifts from \(P_n=\pm 2i\) to
\(P_{2m}-2=2Q_{m+1}P_{m-1}\), whose factor index \(n+2\) matches the
even-anchor offset \(n-r\) at \(r=-2\). For the odd anchors
\(r\in\{3,-3,-1\}\), the offsets \(n-r\in\{n-3,n+3,n+1\}\) lie outside
the indices produced by all four splitting-curve families.

**Dual \(\mathbb Z[\sqrt2]\) identity (Family 2).** For odd \(n=2m+1\),
put \(w_+=P_m+(-1)^m P_{m+1}+\frac12(Q_m-(-1)^m Q_{m+1})\sqrt2\in\mathbb Z[\sqrt2]\)
and let \(w_-\) be its \(\mathbb Q(\sqrt2)\)-conjugate. Direct
expansion from Binet's formulas gives \(\beta w_+^2=\sqrt2 P_n+1\),
\(\beta^{-1}w_-^2=\sqrt2 P_n-1\), and \(w_+ w_-=(-1)^m Q_n\).
Substituting \(P_n=x^2-L_n\) yields
\[
 (\beta w_+)^2-(\sqrt2\beta)\,x^2=-\beta(\sqrt2 L_n-1).
\]
At any odd prime ideal \(\mathfrak p\mid(\sqrt2 L_n-1)\), one has
\(\sqrt2\beta\equiv(2L_n+1)/L_n\pmod{\mathfrak p}\).
For positive odd \(n\), put \(N=2L_n^2-1\). Then
\[
 \left(\frac{(2L_n+1)L_n}{N}\right)
 =\left(\frac{L_n+1}{N}\right)=+1.
\]
The first equality uses \(2L_n^2\equiv1\pmod N\). Write
\(L_n+1=2^e d\) with \(d\) odd. If \(L_n\) is odd, then
\(N\equiv1\pmod8\). If \(L_n\) is even, the Lucas recurrence
modulo four has period six and gives \(4\mid L_n\) at every odd index
with even \(L_n\), so \(e=0\) and \(d\equiv1\pmod4\).
In both cases reciprocity yields \((d/N)=(N/d)=1\), since
\(L_n\equiv-1\pmod d\).

**Mixed-unit identities (Family 3).** For odd \(n=2m+1\), expanding in
\(K\) gives
\[
 (4x)^2-(2\alpha)(3\alpha^m)^2
 =2\alpha^{-n}N_{K/\mathbb Q(\sqrt5)}\!\left((\alpha\beta)^n-2\sqrt2\right)
 =(7L_n+16P_n)-9F_n\sqrt5,
\]
\[
 2\sqrt2\,x^2-9\beta(\beta^m)^2
 =8\beta^{-n}N_{K/\mathbb Q(\sqrt2)}\!\left((\alpha\beta)^n+\frac{1}{2\sqrt2}\right)
 =-9Q_n+(2L_n-7P_n)\sqrt2.
\]
With \(c=1/(2\sqrt2)\), the norms on the right expand to
\(-u^2+c^{-1}u(v+v^{-1})-c^{-2}\) and
\(-v^2+cv(u-u^{-1})+c^2\), respectively.

## 2. Strengthened Gaussian and mixed-unit divisor constraints

The certificate [verify_unified_structure.py](verify_unified_structure.py)
supplies explicit odd-valuation Gaussian prime witnesses with
\(\chi_\pm=-1\) in \(R_s\) ([norm descent](norm-descent.md) §2),
yielding the following unconditional exclusions for every odd square
index \(n\ge3\):
* \(p\nmid n-2\) for \(p\in\{17,31,37,43,47,61,71,73\}\);
* \(p\nmid n+2\) for \(p\in\{19,31,37,47,71\}\);
* \(49,121\nmid n+2\), \(55,65,77\nmid n\pm2\), \(91\nmid n-2\), and
  \(125\nmid n\pm2\) (bounding \(v_5(n+2)\le2\) on \(r=3\) and
  \(v_5(n-2)\le2\) on \(r=-3\));
* on \(r\equiv-1\pmod{720720}\), \(p\nmid (n-2)/3\) for
  \(p\in\{19,29,31,59,61\}\).

For [norm descent](norm-descent.md) §3, any odd prime ideal
\(\mathfrak p\) of \(K\) dividing both \(\eta^n-1\) and \(\xi^n-1\)
satisfies \(\eta^n\equiv\xi^n\equiv1\pmod{\mathfrak p}\), whence
\(\beta^{2n}\equiv 1\) and \(\alpha^{4n}\equiv 1\pmod{\mathfrak p}\).
Since \(n\) is odd, \(\beta^n\equiv\pm1\) implies \(p\mid Q_n\), and
\(\alpha^{2n}\equiv\pm1\) implies \(p\mid 5F_n L_n\). Thus common odd
primes divide \(\gcd(Q_n,5F_n L_n)\). Moreover, \(\xi=\eta u^2\) is a
square modulo any \(\mathfrak p\mid(\eta^s-1)\) for odd \(s\).

**Proposition 2 (One-step prime forcing from §3).** Whenever an odd
divisor \(s\mid n\) has a prime ideal \(\mathfrak p\mid(\eta^s-1)\) of
odd valuation with \((2\sqrt2/\mathfrak p)_2=-1\) and
\(\operatorname{ord}_{\mathfrak p}(\xi)\nmid n\), the rational prime
\(p\) below \(\mathfrak p\) divides \(n\). Indeed, if \(p\nmid n\),
the quotient \((\eta^n-1)/(\eta^s-1)\) reduces to the unit \(n/s\)
modulo \(\mathfrak p\). The product \((\eta^n-1)(\xi^n-1)\) then has
odd valuation, contradicting the norm condition in [norm descent](norm-descent.md) §3.
In particular:
* for every odd square index \(n\ge3\), \(33\mid n\implies 1321\mid n\)
  (\(\operatorname{ord}_{\mathfrak p}(\xi)=110\)) and
  \(35\mid n\implies 7001\mid n\) (\(\operatorname{ord}_{\mathfrak p}(\xi)=250\));
* on the two branches \(n\equiv\pm3\pmod{720720}\), the condition
  \(17\mid n\) implies \(s=51\mid n\). The witness above \(51511\) has
  \(\operatorname{ord}_{\mathfrak p}(\xi)=8585=5\cdot17\cdot101\);
  since \(5\nmid n\), it forces \(51511\mid n\).

## 3. All-parity Frobenius descent and zero-anchor double-root geometry

For arbitrary integers \(r_0,k\in\mathbb Z\), prime \(p>5\), and
\(e\ge1\), writing \(\varepsilon_5=(5/p)^e\) and \(\varepsilon_2=(2/p)^e\),
the Frobenius identity extends uniformly across all parities:
\[
 a_{r_0+kp^e}\equiv \varepsilon_5^{k}\,L_{r_0+\varepsilon_5 k}
                   +\varepsilon_2^{k}\,P_{r_0+\varepsilon_2 k}\pmod p.
\]
Setting \(r_0=0\) gives \(a_{mp^e}\equiv L_m+(2/p)^e P_m\pmod p\) for
odd \(m\). Setting \((r_0,k)=(-2,1)\) excludes \(n+2=p^e\) for odd
\(e\) whenever \((5/p)=-1\) and \((2/p)=+1\) (since \(a_n\equiv 5\pmod p\)),
and \((r_0,k)=(2,3)\) excludes \(n-2=3p^e\) for odd \(e\) whenever
\((5/p)=+1\) and \((2/p)=-1\) (since \(a_n\equiv 10\pmod p\)).

On the zero-anchor branch \(n=k-1\equiv-1\pmod{720720}\), extending the
forced-prime closure of [extension](extension.md) §3 to \(p<250{,}000\)
yields 3,908 forced primes (over 19,000 digits) across 8 rounds, while
the proportion of forced primes decays from \(25.8\%\) at \(X=30{,}000\)
to \(17.7\%\) at \(X=250{,}000\). Combining the 6-round closure below
\(30{,}000\) (837 forced primes) with the exact 5-adic split of
[local geometry](local-geometry.md) Theorem 2 adds the row \(p=5\) to the
\(\mathbb F_2\) linear system of
[forced square classes](forced-squareclass.md), raising the first
consistent outside-prime bound from \(9857\) to \(9949\) (\(\delta=0\),
rank \(842/844\)) and \(9967\) (\(\delta=1\), rank \(843/844\)).

In Round 1 of the closure below \(250{,}000\), exactly two primes
\(p\in\{19,307\}\) satisfy \(T^{h_p}\equiv I\pmod p\) with
\(v_p(a_{h_p-1})=2\) (`h_19=360`, `h_307=5544`). Because
\(v_p(\ell C^3 s)\ge 3\) and \(j-v_p(j!)\ge 3\) for all \(j\ge3\) at
\(p>5\), the restricted power series \(F_p(t)=a_{h_p t-1}/p^2\) lies
in \(\mathbb Z_p\langle t\rangle\) and reduces modulo \(p\) to
\[
 F_{19}(t)\equiv 15\,t(t-4)\pmod{19},\qquad
 F_{307}(t)\equiv 81\,t(t-33)\pmod{307}.
\]
Hensel's lemma gives two simple roots \(0\) and \(\tau_p\in r_0+p\mathbb Z_p\),
with \(\tau_{19}\equiv 1350020572964207\pmod{19^{12}}\) and
\(\tau_{307}\equiv 69800898470995632160\pmod{307^8}\). Since
\(p\equiv3\pmod4\), the divided-difference leading unit is a quadratic
residue near \(t=0\) (`16 mod 19`, `90 mod 307`) and a quadratic
nonresidue near \(t=\tau_p\) (`3 mod 19`, `217 mod 307`).

## 4. Minimal open targets

The infinite classification reduces to either:
1. the global analytic closing bound in
   [quantitative square count](quantitative-square-count.md) §5
   (\(B\le 8.6\times 10^{898}\) for the \(K^6\) covering hyperplanes,
   or equivalently \(\|A_r V^m+B_r(U/V)^m\|_{\mathbb Z}\ge 5(U^2/V^3)^m\)
   for \(r\in\{1,3\}\) and \(m\ge2.5\times 10^{901}\)), covering all
   three odd branches simultaneously; or
2. for the zero-anchor branch \(r=-1\) independently, non-termination
   of the forced-prime closure (for every finite divisor \(D\) in the
   closure, existence of \(p\nmid D\) with \(h_p\mid D\) and
   \(v_p(a_{h_p-1})=1\)).

## 5. Finite étale covers of the odd square surface

Let \(T=(\mathbb G_m)^2\) over the coefficient field \(K\).
The affine square surface \(S\) over \(T\) has equation
\[
 x^2=f(u,v),\qquad f(u,v)=u-u^{-1}+c(v+v^{-1}),\qquad
 c=1/(2\sqrt2).
\]
Every finite étale cover of \(S\) is the pullback of a unique
finite étale cover of \(T\), up to isomorphism. The same holds
for each square surface obtained by a monomial isogeny of
the two torus coordinates, including the fourth-power model
of the [quantitative analysis](quantitative-square-count.md#6-norms-of-fixed-laurent-expressions).

Over \(\mathbb C\), the Newton polytope of \(x^2-f\) is the
three-dimensional pyramid with a diamond base in the plane
of \(u,v\) and the apex at the exponent of \(x^2\). A face
containing the apex has nonzero logarithmic \(x\)-derivative
on the torus. Each edge of the base is a binomial with two
distinct exponents, hence has a smooth zero set on the torus.
At a critical point of \(f\) on the torus, \(u^2=-1\) and
\(v^2=1\), so \(f=\pm2i\pm2c\ne0\). These checks give
Newton nondegeneracy, both for \(x^2-f\) in three variables
and for its restriction \(-f\) at \(x=0\) in two. A monomial
isogeny or a nonzero rescaling of the torus coordinates
preserves the checks by étale pullback and invertible real
transformation of the exponent planes.

These are the hypotheses of Oka's full nondegenerate
complete-intersection theorem with the single polynomial
coordinate \(x\). For dimension three and one equation it
gives an isomorphism on topological fundamental groups for
the inclusion \(S(\mathbb C)\hookrightarrow (\mathbb C^*)^2\times
\mathbb C\). Composing with the projection to \(T(\mathbb C)\)
thus gives \(\pi_1^{\mathrm{top}}(S(\mathbb C))\cong\mathbb Z^2\)
and identifies the projection with that isomorphism.
[Oka, Nagoya Mathematical Journal 121 (1991), Theorem (1.1)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0027763000003421)

The comparison of finite étale and topological coverings and
invariance under algebraically closed field extension give
the isomorphism of geometric étale fundamental groups. Over
\(K\), the morphism of étale fundamental-group exact sequences
induces that isomorphism on the geometric kernels and the
identity on \(\operatorname{Gal}(\overline K/K)\). It is therefore
also an isomorphism in the middle, proving the cover statement.
In particular a lifting condition through such a cover at a
square index depends only on \((u,v)=(\alpha^n,\beta^n)\).

The geometric Picard group of \(S\) has no torsion. For every
positive integer \(m\), the Kummer sequence puts its
\(m\)-torsion in the quotient of
\(H^1_{\mathrm{\acute et}}(S_{\overline K},\mu_m)\) by the classes
of units. The two torus units already generate this cohomology
by the isomorphism above. Thus a Kummer cover produced by a
torsion divisor does not add any further étale descent.

## 6. Elliptic division and varying ramification

Put \(C=c(v+v^{-1})\) and set \(Y=ux\) on the surface.
The fibration in \(v\) has elliptic equation
\(Y^2=u^3+Cu^2-u\), with the rational point \((0,0)\) of
order two. The isogeny with this kernel maps to
\[
 E'_v: Y'^2=X((X-C)^2+4),\qquad
 X=x^2,\quad Y'=x(u+u^{-1}).
 \tag{10}
\]
In particular these formulas satisfy the target equation,
since \(X-C=u-u^{-1}\). The target has full two-torsion over
\(K(i)\), at \(X=0,C-2i,C+2i\).

Let \(n\ge1\) be an odd square index and specialize
\(u=\alpha^n,v=\beta^n\), so \(C=P_n\). Write \(M=K(i,\sqrt\alpha)\)
and \(\vartheta=\alpha^{n/2}\in M\). The three
differences of \(X\) from the roots of the target cubic
are squares in \(M\), with respective square roots up to sign
\[
 x,\qquad A_+=\vartheta+i\vartheta^{-1},\qquad
 A_-=\vartheta-i\vartheta^{-1}.
\]
Their squares are \(a_n,L_n+2i,L_n-2i\), respectively.
Consequently the point in (10) can be halved over \(M\).
For any half point with first coordinate \(X_1\), choose the
signs of the three roots \(r_1,r_2,r_3\) so that
\(r_1r_2r_3=-Y'\). The explicit halving formula gives
\[
 X_1-(C-2i)=(r_1+r_2)(r_2+r_3),\qquad
 r_2+r_3\in\{\pm2\vartheta,\ \pm2i\vartheta^{-1}\}.
 \tag{11}
\]
The formula follows by adding \(r_2^2=X-(C-2i)\) to the
correction \(r_1r_2+r_1r_3+r_2r_3\) in the half point's first
coordinate. [Bekker and Zarhin, *Division by 2 of rational points on elliptic curves*](https://doi.org/10.1090/spmj/1512)

For every finite set of rational primes \(S_0\) containing
2 and 5, there is an effective bound \(N(S_0)\) such that
for every odd square index \(n>N(S_0)\), no half point
in (11) can be halved in an extension of \(M\) unramified
outside \(S_0\).

To prove it, first consider an arbitrary positive odd index.
If \(P_n^2+4\) has even valuation outside \(S_0\), write
\(P_n^2+4=d z^2\) with \(d>0\) squarefree and supported on
\(S_0\). The Pell identity gives \(Q_n^2=2P_n^2-1\), so
\((P_n,dzQ_n)\) is an integral point on
\[
 W^2=d(T^2+4)(2T^2-1).
\]
The quartic has four distinct roots for every such \(d\),
and there are finitely many \(d\). The effective bound for
integral solutions of hyperelliptic equations therefore bounds
\(P_n\), hence \(n\), in terms of \(S_0\).
[Bérczes, Evertse and Győry, *Effective results for hyper- and superelliptic equations over number fields*, Theorem 2.2](https://arxiv.org/abs/1301.7168)

For odd \(n\), \(P_n\) is odd, and the Gaussian factors
\(P_n\pm2i\) are coprime. At a rational prime outside \(S_0\)
of odd valuation in \(P_n^2+4\), the unique Gaussian prime
\(\pi\) dividing \(P_n-2i\) has that same odd valuation.
By the [Gaussian square identity](norm-descent.md#2-a-gaussian-factorization-for-the-odd-indices),
\(A_+\) lies in \(J=\mathbb Q(i,\sqrt{1+2(-1)^{(n-1)/2}i})\)
and the norm of either \(x+A_+\) or \(x-A_+\) from \(J\)
to \(\mathbb Q(i)\) is \(P_n-2i\).
The extension is unramified at \(\pi\). Since the norm
valuation is odd, at least one prime over \(\pi\) has odd
valuation in the factor \(r_1+r_2\), irrespective of the
sign choice. Also \(M/\mathbb Q(i)\) is unramified at
primes above \(p\notin S_0\), since it is built from the
units \(\alpha\), \(i\) and the radicals \(\sqrt2,\sqrt5\).
In (11) the factor \(r_2+r_3\) is a unit at every odd
prime. Thus \(X_1-(C-2i)\) has odd valuation at a prime
of \(M\) outside \(S_0\). It cannot become a square in an
extension unramified at that prime, as would be required
for a second halving.

**The other fibration.** Write \(t=u-u^{-1}\). The change
\((V,Z)=(cv,cvx)\) gives \(Z^2=V^3+tV^2+c^2V\), with
the order-two point \((0,0)\). Its corresponding isogeny
gives the point
\[
 X=x^2,\quad Z'=cx(v-v^{-1})\qquad\text{on}\qquad
 Z'^2=X\big((X-t)^2-4c^2\big).
\]
At an odd square index put \(n=2m+1\). The square roots
of \(X\), \(X-(t-2c)\) and \(X-(t+2c)\) are, up to sign,
\[
 x,\qquad B_+=\tfrac12(\theta\beta^m+\theta'\beta^{-m}),\qquad
 B_-=\tfrac12(\theta\beta^m-\theta'\beta^{-m}),
\]
with \(\theta=\sqrt{2+\sqrt2}\), \(\theta'=\sqrt{2-\sqrt2}\).
Here \(B_\pm^2=P_n\pm2c\). The first halving is defined
over \(K(\theta)\). In the corresponding version of (11),
the sum of the signed roots from \(B_+,B_-\) is a unit at
every odd prime, and the relative norm of \(x\pm B_+\) to \(K\) is
\(L_n-2c\). The conjugate factor is \(L_n+2c\).
At odd primes their valuation supports are disjoint in
\(K\), and the product is \((2L_n^2-1)/2\).

In the quadratic field \(\mathbb Q(\sqrt2)\), a rational
prime \(p>2\) dividing \(2L_n^2-1\) splits, because
\(2L_n^2\equiv1\pmod p\). At the prime dividing
\(L_n-2c\), the valuation is \(v_p(2L_n^2-1)\).
The same parity holds after extension to \(K\) if \(p>5\),
since that extension is unramified there. Thus an odd
valuation in \(2L_n^2-1\) forces ramification in the
second halving of every half point in this fibration.
Conversely at any \(p>5\) not dividing \(2L_n^2-1\),
the coordinates required for the second halving are units
at all primes above \(p\), by the same formulas. Adjoining
their square roots is unramified there.

As in the first fibration, the ramification cannot be
confined to any fixed \(S_0\) at sufficiently large square
indices, with effective threshold. If
\(2L_n^2-1=d z^2\) has squarefree part supported in \(S_0\),
use \(L_n^2+4=5F_n^2\) to obtain the integral point
\((L_n,5dF_nz)\) on \(W^2=5d(T^2+4)(2T^2-1)\).

On the two nonzero anchors there is a rational prime
\(p>5\) that must ramify in the second halving for the first
fibration and is unramified for the second fibration.
Indeed \(P_n^2+4\equiv5\pmod8\), so some prime with odd
valuation in it is \(5\bmod8\) because all its primes are
\(1\bmod4\). The prime 5 itself does not divide
\(P_n^2+4\) on either nonzero anchor, since the Pell
matrix has period dividing 12 modulo 5 and
\(P_{\pm3}\equiv0\pmod5\). A prime \(5\bmod8\) cannot
divide \(2L_n^2-1\). This distinguishes the two division
extensions even after passing to the compositum of their
fixed fields, which is unramified at that prime.

## Reproduction

Run:

    python3 verify_unified_structure.py

The certificate verifies all constants for the \(N=6\) Subspace Theorem
reduction, the dual \(\mathbb Z[\sqrt2]\) and mixed-unit norm identities,
every §2 and §3 prime witness, the all-parity Frobenius identity, the
\(p=19,307\) double-root liftings, and the 5-adic split linear system.
