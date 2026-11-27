# Quantitative bound for the number of square indices

Let \(a_n=L_n+P_n\) be A060405 and let
\(\alpha=(1+\sqrt5)/2,\ \beta=1+\sqrt2,\ c=1/(2\sqrt2)\).
The square-gap theorem gives finiteness. The following argument
sharpens the quantitative bound using a minimal-dimension six-coordinate
embedding in the quantitative Subspace Theorem.

**Theorem.** The number of nonnegative integers \(n\) for which
\(a_n\) is an integer square is less than \(2.9\times10^{28}\).

## 1. Explicit approximation and five-unit coordinates

For \(n\ge1\), Binet's formulas give
\[
 a_n=c\beta^n+\alpha^n+e_n,\qquad
 |e_n|\le(1+c)\alpha^{-n}.
\]
The quantity \(u_n=(\alpha^n+e_n)/(c\beta^n)\) is positive:
\(\alpha^2>1+c\), and \(\alpha^n>(1+c)\alpha^{-n}\).
Also \(|\alpha^n+e_n|<2\alpha^n\).
For \(u\ge0\), Taylor's formula gives
\[
 0\le1+u/2-\sqrt{1+u}\le u^2/8.
\]
Consequently, setting \(\rho=\alpha^2/\beta^{3/2}\),
\[
 \left|\sqrt{a_n}-\sqrt c\,\beta^{n/2}
       -\frac{1}{2\sqrt c}(\alpha/\sqrt\beta)^n\right|
 <5\rho^n .
\]
Indeed the quadratic remainder is bounded by
\((2c^{3/2})^{-1}\rho^n\), and the inverse-root correction by
\((1+c)(2\sqrt c)^{-1}(\alpha\sqrt\beta)^{-n}\).
The latter base is smaller than \(\rho\); the sum of the two
constants is less than 5. Moreover \(\rho^4<1/4\).

Write \(n=4m+r\), \(0\le r\le3\), and put
\[
 U=\alpha^4,\quad V=\beta^2,\quad
 A_r=\sqrt c\,\beta^{r/2},\quad
 B_r=(2\sqrt c)^{-1}(\alpha/\sqrt\beta)^r.
\]
Then if \(a_{4m+r}=x^2\), \(x\ge0\), the error satisfies
\[
 |x-A_r V^m-B_r(U/V)^m|<5(U^2/V^3)^m<5\,4^{-m}.
\]

The real biquadratic field \(K=\mathbb Q(\sqrt2,\sqrt5)\) has four
archimedean places \(v_1=(+,+)\), \(v_2=(+,-)\), \(v_3=(-,+)\),
and \(v_4=(-,-)\), labeled by the signs of \((\sqrt2,\sqrt5)\) under
\(\sigma_v\). Use the five-element unit subset
\[
 {\cal W}_5=\{V,V^{-1},U/V,(UV)^{-1},UV\},
\]
omitting \(V/U\). The units in \({\cal W}_5\) are distinct because
\(U,V\) are multiplicatively independent: conjugating a relation
\(U^iV^j=1\) by the automorphism inverting \(U\) and fixing \(V\)
gives \(U^{2i}=1\), hence \(i=j=0\).

## 2. Minimal-dimension quantitative subspace theorem

Use the six-coordinate vector
\[
 {\bf y}=(x,(w^m)_{w\in{\cal W}_5})\in K^6.
\]
At each real place \(v\in\{v_1,v_2,v_3,v_4\}\), let
\(M_v=\max_i|\sigma_v(y_i)|\). For \(m\ge600\) and odd \(r\in\{1,3\}\),
the unit magnitudes at the four places are:
* at \(v_1\): \(|\sigma_{v_1}(w)|\in\{V,V^{-1},U/V,(UV)^{-1},UV\}\), maximum \(UV\);
* at \(v_2\): \(|\sigma_{v_2}(w)|\in\{V,V^{-1},(UV)^{-1},U/V,V/U\}\), maximum \(V\);
* at \(v_3\): \(|\sigma_{v_3}(w)|\in\{V^{-1},V,UV,V/U,U/V\}\), maximum \(UV\);
* at \(v_4\): \(|\sigma_{v_4}(w)|\in\{V^{-1},V,V/U,UV,(UV)^{-1}\}\), maximum \(UV\).

Since \(x\le 2.3\,V^m\) for \(m\ge600\), one has \(M_{v_1}=M_{v_3}=M_{v_4}=(UV)^m\)
and \(V^m\le M_{v_2}\le 2.3\,V^m\). All finite-place maxima equal 1 because
the \(w\) are units and \(x\) is integral. Hence the maximum-norm height of
[1] satisfies
\[
 (U^{3/4}V)^m\le H({\bf y})=(M_{v_2}(UV)^{3m})^{1/4}\le 2.3^{1/4}(U^{3/4}V)^m.
\]

At each place \(v\), extend \(\sigma_v\) to an automorphism
\(\widetilde\sigma_v\) of \(\overline{\mathbb Q}\). Take the five
coordinate forms \(Z_w\) at all four places; for the sixth form, take
\[
 L_{0,v}=X-\widetilde\sigma_v^{-1}(A_r)Z_{\sigma_v^{-1}(V)}
           -\widetilde\sigma_v^{-1}(B_r)Z_{\sigma_v^{-1}(U/V)}
\]
at \(v\in\{v_1,v_2,v_3\}\), and take \(X\) at \(v=v_4\).
At every place the coefficient determinant has absolute value 1.
Put \(L=\log(U^3 V^4)\) and \(\eta=199/200\).
For the normalized absolute values of [1], set
\[
 d_{w,v}=\frac{\eta}{L}\log\frac{|\sigma_v(w)|}{\tau_v}\qquad
 \bigl(w\in{\cal W}_5,\ \tau_{v_1}=\tau_{v_3}=\tau_{v_4}=UV,\ \tau_{v_2}=V\bigr),
\]
and set
\[
 d_{0,v_1}=d_{0,v_3}=\frac{\eta}{L}\log\frac{U}{V^4},\qquad
 d_{0,v_2}=\frac{\eta}{L}\log\frac{U^2}{V^4},\qquad
 d_{0,v_4}=\frac{\eta}{L}\log\frac{1}{U}.
\]
Every weight is nonpositive. Since \(\prod_{v}|\sigma_v(w)|=1\) for each
\(w\in{\cal W}_5\),
\[
 \sum_{v}\sum_{w\in{\cal W}_5}d_{w,v}=-5\eta,\qquad
 \sum_{v}d_{0,v}=\eta\frac{\log(U^3/V^{12})}{L}=-\eta+\eta\frac{\log(U^6/V^8)}{L}.
\]
Because \(U^6/V^8<0.078<1\), the total weight sum over all four places is
\[
 -6\eta+\eta\frac{\log(U^6/V^8)}{L}<-6.168<-6-\frac{1}{6}.
\]
Take \(\epsilon=1/6\). Increasing the weights by interpolating toward
the zero vector gives sum \(-6-\epsilon\), preserves nonpositivity, and
weakens the individual upper bounds required in (3.7) of [1].
For each form \(L_{i,v}\), the slack factor \((1-\eta)\) absorbs the bounded
constant factor \(2.3^{1/4}\) in \(H({\bf y})\) and the leading constants
\(5\) and \(2.3\) for all \(m\ge600\); for forms with \(|\sigma_v(w)|=\tau_v\)
one has \(d_{w,v}=0\) and \(|Z_w({\bf y})|_v/M_v\le 1\).
Thus all bounds in (3.7) of [1] hold for \(m\ge600\). The maximum over
automorphisms fixing \(K\) leaves \({\bf y}\) fixed.

Using only one or two approximation places gives product exponents
\(U^{2m}>1\) or \((U/V)^{4m}>1\), so three approximation places and
\(N=6\) coordinates are minimal for this construction over \(K\).

The union of the forms has cardinality at most \(R=9\).
Since \(A_r^2\in K\) and \(B_r/A_r\in K\), each coefficient field
over \(K\) has degree at most \(D=2\). The inhomogeneous form height
satisfies \(H^*(L_{0,v})\le \exp(h(A_r)+h(B_r))<1000\). Indeed,
\[
 h(A_r)\le\tfrac12(h(c)+r h(\beta)),\qquad
 h(B_r)\le\log 2+\tfrac12 h(c)+r h(\alpha)+\tfrac r2 h(\beta),
\]
where \(h(c)=\tfrac32\log 2\), \(h(\alpha)=\tfrac12\log\alpha\),
and \(h(\beta)=\tfrac12\log\beta\).
The height threshold of [1, Theorem 3.1] is at most
\(\max(1000^{1/54},6^{36})\), below \(H({\bf y})\) for \(m\ge600\).
With dimension six, that theorem covers the vectors for each \(r\) by at most
\[
 T=10^9\,2^{12}\,6^{14}\,6^3\log(324)\log\big(6\log 54\big)
 <1.3\times 10^{27}
\]
proper linear subspaces defined over \(K\).
The numerical inequality follows from \(\log 324<5.8\),
\(\log 54<4\), and \(\log 24<3.18\), each of which follows from
the exponential series.

## 3. At most eleven indices per subspace

Each proper subspace lies in a hyperplane
\[
 d_0 X+\sum_{w\in{\cal W}_5}d_w Z_w=0
\]
with coefficients in \(K\), not all zero.

If \(d_0=0\), the equation is a nonzero exponential polynomial in \(m\)
with at most five distinct positive bases, hence at most four real zeros
by Rolle's theorem and induction.

If \(d_0\ne0\), the hyperplane gives \(x=\sum_{w\in{\cal W}_5}b_w w^m\).
The exponent pairs of \({\cal W}_5\) in \((U,V)\) are
\(\{(0,1),(0,-1),(1,-1),(-1,-1),(1,1)\}\). Their pairwise sums together
with the four Binet pairs \((1,0),(-1,0),(0,2),(0,-2)\) form a set of
12 distinct pairs: \((-2,2)\), \((-1,2)\), and \((-2,0)\) are absent
from the 15-element grid \(\{-2,-1,0,1,2\}\times\{-2,0,2\}\).
Squaring and comparing with \(a_{4m+r}\) gives an exponential polynomial
with at most 12 distinct positive bases. It is nonzero by the same weight
argument on \(C_1 u+C_2 u^{-1}+C_3 v^2+C_4 v^{-2}=G(u,v)^2\), so Rolle's
bound yields at most 11 integer indices \(m\) on the hyperplane.

The [norm descent](norm-descent.md) restricts \(r\) to 1 and 3.
The number of square indices with \(m\ge600\) is thus at most \(22T\),
and there are at most 1200 indices with \(m<600\). Hence the total
number of square indices is at most \(22T+1200<2.9\times10^{28}\).

## 4. Effective zero location in any specified hyperplane

Normalize a hyperplane by \(d_0=1\) if \(d_0\ne0\), or by setting any
nonzero coefficient equal to 1 otherwise. Let \(B\) be the maximum
absolute logarithmic height of its resulting nonzero coefficients.

**Proposition.** Every square index \(n=4m+r\) whose vector belongs to
this hyperplane satisfies
\[
 n\le 1150(B+1)+3.
\]

To prove this, write the nonzero exponential polynomial obtained in
Section 3 as \(f(m)=\sum_i c_i\lambda_i^m\) with real coefficients in
\(K\) and positive distinct bases. In \({\cal W}_5\), the maximum number
of ordered pairs summing to any given exponent pair is 4 (attained at
\((0,0)\) and \((1,0)\)). Each coefficient \(c_i\) after squaring is a
sum of at most four ordered products of two hyperplane coefficients,
with at most one original Binet coefficient subtracted. The heights of
the original Binet coefficients for \(0\le r\le3\) are less than 3, so
\[
 h(c_i)\le 8B+3+\log 5<8B+5.
\]
The case \(d_0=0\) satisfies the stronger bound \(h(c_i)\le B\).
Since \([K:\mathbb Q]=4\), every nonzero \(c_i\) satisfies
\[
 e^{-4(8B+5)}\le |c_i|\le e^{4(8B+5)}.
\]

As verified on the \(\{-2,-1,0,1,2\}\times\{-2,0,2\}\) grid from
\(6.85<U<6.86\) and \(5.82<V<5.83\), the ratio of any two unequal bases,
larger divided by smaller, exceeds \(5/4\). At a zero \(m\ge0\), the
largest base with nonzero coefficient is cancelled by the remaining at
most 11 terms. Dividing by that largest term gives
\[
 1\le 11 e^{64B+40}(4/5)^m.
\]
Hence
\[
 m\le\frac{64B+40+\log 11}{\log(5/4)}<287.5(B+1),
\]
and \(n=4m+r\le 1150(B+1)+3\). This proves the proposition.

## 5. Single-line closing targets

Combining the proposition with the [finite certificate](extended-lifting.md)
through \(10^{902}\) reduces the complete infinite square classification
to either of two single-line statements across the surviving odd classes:

1. An explicit bound \(B\le 8.6\times 10^{898}\) on the normalized
   coefficient heights of the \(K^6\) covering hyperplanes in Section 2.
2. Directly in terms of the binary approximation, the inequality
   \(\|A_r V^m+B_r (U/V)^m\|_{\mathbb Z}\ge 5(U^2/V^3)^m\) for
   \(r\in\{1,3\}\) and all \(m\ge2.5\times 10^{901}\).

## 6. Norms of fixed Laurent expressions

The approximation in Section 1 uses a different linear form
at each place. The following calculation describes the scope
of a single Laurent expression evaluated at all places.

Let \(r\in\{1,3\}\), put \(u_m=\alpha^m\), \(v_m=\beta^m\),
and use \(U,V\) as indeterminates in this section. Define
the Laurent polynomial
\[
 f_r(U,V)=\alpha^r U^4-\alpha^{-r}U^{-4}
   +c\bigl(\beta^r V^4+\beta^{-r}V^{-4}\bigr).
\]
Then \(f_r(u_m,v_m)=a_{4m+r}\). For any finite extension
\(E/K\), let
\[
 \mathcal R_E=
 E[U^{\pm1},V^{\pm1},X]/(X^2-f_r(U,V)).
\]
Given a nonzero \(H\in\mathcal R_E\), evaluate \(H^\sigma\)
at each embedding \(\sigma:E\hookrightarrow\mathbb C\) on the tuple
\((\sigma(u_m),\sigma(v_m),x_m)\), with the same positive real
root \(x_m=\sqrt{a_{4m+r}}\) at every embedding. Write \(J_H(m)\)
for the product of the absolute values of these evaluations.
At a square index this is the absolute algebraic norm
of \(H(u_m,v_m,x_m)\).

**Proposition.** The limit
\(\lim_{m\to\infty}m^{-1}\log J_H(m)\) exists and is
nonnegative. If it is zero, \(J_H(m)\) is a positive
constant, the absolute norm of a nonzero algebraic number
in \(K\).

**Proof.** First consider \(E=K\) and write \(H=P+XQ\)
with \(P,Q\) Laurent polynomials. At a real embedding
of \(K\), write \(s_5,s_2\in\{-1,1\}\) for the signs of
\(\sqrt5,\sqrt2\). A monomial \(U^iV^j\) then has growth
exponent
\[
 w_\sigma(i,j)=s_5i\log\alpha+s_2j\log\beta.
\]
The weights of distinct monomials differ. Indeed, an
integer relation between \(\log\alpha\) and \(\log\beta\)
would give \(\alpha^i\beta^j=1\). Conjugating only
\(\sqrt5\) then gives \(\alpha^{2i}=(-1)^i\),
forcing \(i=j=0\). Thus each nonzero Laurent polynomial
has a unique leading monomial at each embedding.

By Binet's formula \(x_m\sim A_r\beta^{2m}\), using \(A_r\)
from Section 1. The constant
\[
 A_1=\frac{\sqrt{2+\sqrt2}}2=\frac{\zeta_{16}+\zeta_{16}^{-1}}2
\]
generates the cyclic quartic real cyclotomic field of
conductor 16. The field \(K\) is biquadratic, so \(A_1\)
lies outside \(K\). Since \(A_3=\beta A_1\), the same
holds for \(A_3\).

If the leading exponents of \(P\) and of \(x_mQ\) coincide,
cancellation would require \(A_r\) to equal a signed ratio
of the embedded leading coefficients of \(P\) and \(Q\).
That ratio belongs to \(K\), since \(K/\mathbb Q\) is Galois.
The leading exponent
of \(P+x_mQ\) is the larger of the two exponents, including
the case of equality. Considering even and odd \(m\)
accounts for signs of conjugate units and gives the
same exponent on both subsequences.

If \(Q\ne0\), fix any monomial in \(Q\). At each embedding
the leading exponent of \(P+x_mQ\) is at least that
monomial's weight plus \(2\log\beta\). The four weights
sum to zero, so the total exponent is at least
\(8\log\beta>0\). If \(Q=0\), each opposite pair of
embeddings gives the width of the support of \(P\) in
that weight direction. If the support has at least two
monomials, each width is positive by the distinct weights.
For a single monomial the product of the unit factors
has absolute value 1, giving precisely the absolute norm of its
nonzero coefficient.

For general \(E\), the polynomial \(X^2-f_r(U,V)\)
remains irreducible over \(\overline K(U,V)\).
To see this, multiply \(f_r\) by \(U^4\) and view the
result as a polynomial in \(U\) over \(\overline K(V)\).
It is quadratic in \(U^4\), with nonzero constant and
leading coefficients and a nonconstant linear
coefficient. Its discriminant is a nonconstant rational
function of \(V\), giving distinct roots in \(U^4\).
The constant term makes both roots nonzero.
Hence the polynomial in \(U\)
has eight distinct roots and cannot be a square.
Irreducibility makes \(\mathcal R_{\overline K}\) a domain.
The product of the conjugates of \(H\) over the embeddings
of \(E/K\) is therefore nonzero and Galois-invariant, so it
lies in \(\mathcal R_K\). Extending each embedding of \(K\)
to \(E\) accounts for every factor of \(J_H(m)\) exactly once.
Thus its four-place product equals \(J_H(m)\),
and the preceding computation applies. \(\square\)

This rules out a norm tending to zero from any fixed
regular Laurent expression, or a fixed finite collection
of such expressions, on this model. An effective argument
can still use rational functions with additional
denominators whose arithmetic is controlled on square
solutions, or a different effective reduction.

**Units on the original double cover.** Before the
substitution \(u=\alpha^rU^4,\ v=\beta^rV^4\), set
\[
 f(u,v)=u-u^{-1}+c(v+v^{-1}).
\]
Over any extension of \(K\), the units of the Laurent ring
with \(x^2=f(u,v)\) are exactly the nonzero scalar multiples
of \(u^iv^j\). Indeed, if \(P+xQ\) is a unit, then
\(P^2-fQ^2\) is a unit in the coefficient Laurent ring.
If \(Q\ne0\), every generic weight selects a leading
exponent in \(fQ^2\) outside \(2\mathbb Z^2\), because
all four exponents of \(f\) lie outside that sublattice.
The leading exponent in \(P^2\), when \(P\ne0\), lies
in \(2\mathbb Z^2\), so these leading terms survive in the
difference whenever they are maximal. The support function
of the difference is the maximum of the two support functions
for generic weights, and then for all weights by continuity.
Its Newton polygon therefore contains that of \(fQ^2\),
which is two-dimensional. A Laurent unit
has a single exponent. Thus \(Q=0\), and \(P\) is a Laurent
monomial.

**Units after the fourth-power substitution.** Over any coefficient
extension of \(K\), the units of \(\mathcal R_E\) are also the
scalar Laurent monomials \(U^iV^j\). The proof uses the conic
over the \(V\)-line. Over an algebraically closed coefficient
field, write \(a=\alpha^r,\ b=-\alpha^{-r}\), and
\[
 C(V)=c(\beta^rV^4+\beta^{-r}V^{-4}),\qquad
 T=U^4,\qquad Y=U^2X.
\]
Thus \(Y^2=aT^2+C(V)T+b\). Choose \(A^2=a\), \(B^2=b\);
the affine conic with \(T\) invertible has the presentation
\[
 Z=(Y-B)/T,\qquad (Z^2-a)T=C(V)-2BZ.
 \tag{16}
\]

Over the field of rational functions in \(V\), \(T\) on the
smooth projective conic has two simple zeros and two simple
poles. Taking \(U^4=T\) gives a geometrically integral cyclic
cover, totally ramified at those four points. The affine curve
\(Y^2=aU^8+C(V)U^4+b\) is smooth because the polynomial on
the right has eight distinct roots over the algebraic closure
of the rational function field. A unit of the
Laurent square cover has divisor supported at the four points
above them, each fixed by the cover automorphism \(U\mapsto\zeta_4 U\)
with \(Y\) fixed. The ratio of a conjugate of the unit to itself
therefore has zero divisor, so belongs to the coefficient field
of the curve, namely the rational function field in \(V\).
Its fourth power is 1. Dividing the unit by a suitable power
of \(U\) makes it invariant. The invariant subring is precisely
the conic ring (16), since adjoining \(U^4=T\) gives a free
basis \(1,U,U^2,U^3\) over that ring. The invariant unit and
its inverse both belong to it.

The conic over the rational function field in \(V\) is the
\(Z\)-line with \(Z=A,-A,C/(2B)\) removed. Thus its units are
\[
 c_0(V)(Z-C/(2B))^i(Z-A)^j(Z+A)^l
 \tag{17}
\]
with \(c_0(V)\) rational and \(i,j,l\) integers.
Each of \(C(V)-2AB\) and \(C(V)+2AB\) has simple nonzero roots:
its equation in \(V^4\) is quadratic with nonzero constant
and discriminant, since \(ab=-1\) and \(c^2=1/8\).

At a root \(V_0\) of \(C-2AB\), the fiber of (16) has two
components. One is \(Z=A\), and the other is
\((Z+A)T+2B=0\). At the generic point of the latter,
all three \(Z\)-factors in (17) are units. At the generic point
of either component, \(V-V_0\) is a uniformizer, since the
factor of the fiber equation defining the other component is
a unit and \(C-2AB\) has a simple root at \(V_0\).
The unit condition therefore gives \(v_{V_0}(c_0)=0\).
At the generic point of the first component,
\[
 (Z-A)((Z+A)T+2B)=C-2AB
\]
shows that \(Z-A\) has order 1. Equation (16) gives the
same order for \(Z-C/(2B)\). Consequently \(i+j=0\).
At the roots of \(C+2AB\) the same two components with
the signs reversed give \(i+l=0\).
For every other nonzero finite \(V_0\), the fiber shows
\(v_{V_0}(c_0)=0\) by evaluating at its generic point.
Thus \(c_0(V)\) is a scalar times a power of \(V\), and
the remaining expression (17) is a scalar times \(T^i\)
by (16). Restoring the initial power of \(U\) proves
the unit classification.

If the factors of \(C(V)^2-4ab\) are inverted, the same
argument describes all the additional units. They are
generated by \(Z-A,Z+A\) and the factors \(V-V_0\) at the
removed fibers, together with the Laurent monomials.
In fact (16) gives \(Z-C/(2B)\) as a Laurent unit times
\((Z-A)(Z+A)\), and
\[
 (Z\mp A)((Z\pm A)T+2B)=C\mp2AB .
\]
On the recurrence orbit, \(C(V)=P_{4m+r}\) and
\(C(V)^2-4ab=P_{4m+r}^2+4=P_{4m+r-2}P_{4m+r+2}\).
Thus the extra unit factors have prime support furnished
by the Pell factors of the Gaussian norm descent.

**Height and prime support of the specialized units.** Choose
\(B=i/A\) with \(A=\alpha^{r/2}\).
At a square index \(n=4m+r\), put \(\vartheta=\alpha^{n/2}\)
and write
\[
 w_-=U^2(Z-A)=x_m-\vartheta-i\vartheta^{-1},\qquad
 w_+=U^2(Z+A)=x_m+\vartheta-i\vartheta^{-1}.
\]
Write \(D=1+2(-1)^{(n-1)/2} i\). In the quadratic extension
\(J_-=\mathbb Q(i,\sqrt D)\) of \(\mathbb Q(i)\),
\(\vartheta+i\vartheta^{-1}\) is a square root of \(L_n+2i\).
The [Gaussian identity](norm-descent.md#2-a-gaussian-factorization-for-the-odd-indices)
places this root in \(J_-\), of the form \(z_0\sqrt D\) with
\(z_0\) a Gaussian integer. Thus \(w_-\) has norm \(P_n-2i\)
to \(\mathbb Q(i)\). Its partner \(w_+\) belongs to the
complex conjugate field \(J_+\) and has norm \(P_n+2i\).
Both are algebraic integers.

Set
\[
 G=P_n^2+4=P_{n-2}P_{n+2},\qquad E_n=\frac{G}{\gcd(G,x_m^2)}.
\]
For every rational prime \(p\mid E_n\), write
\(e_p=v_p(G)-2v_p(x_m)>0\).
There is a unique Gaussian prime \(\pi\) over \(p\) that
divides \(P_n-2i\), with valuation \(v_p(G)\).
Indeed \(G\) is coprime to 6, and \(P_n-2i\) and \(P_n+2i\)
are coprime.
If \(\pi\) is unramified and inert in \(J_-\), the norm
valuation is at most \(2v_p(x_m)\).
The only possibly ramified odd prime is the one dividing
\(D\), above 5. There \(x_m^2\) and \(Dz_0^2\) have
even and odd valuation, respectively, so the same bound
also holds. The conjugate prime above 5 is inert, since
\(D\equiv2\bmod\overline D\), a nonresidue modulo 5.
Thus every \(p\mid E_n\) is greater than 5 and \(\pi\) splits
in \(J_-\). At its two primes the valuations of \(w_-\)
have sum \(v_p(G)\). They differ, because equal valuations
would imply \(v_p(2x_m)\ge v_p(G)/2\). Their minimum is
therefore \(v_p(x_m)\) and their difference in absolute
value is \(e_p\). The conjugate prime of \(\mathbb Q(i)\)
has the corresponding valuation difference for \(w_+\).
Moreover
\[
 E_n\ \ge\ \frac{P_n^2+4}{L_n^2+4}
          \ =\ \exp\!\big(2n\log(\beta/\alpha)+O(1)\big),
 \tag{20}
\]
since \(\gcd(G,x_m^2)\mid L_n^2+4\).

Let \(\Psi\) be a localized unit written as a scalar \(\lambda\)
times Laurent monomials in \(U,V\), a product of powers of
\(V-V_0\) at the removed fibers, and \((Z-A)^j(Z+A)^l\).
The field generated by the \(V_0\), \(i\), and \(\beta\)
is unramified at odd primes. In fact \(V_0^4\) is one of
\(\pm i\beta^{\pm2-r}\), a unit, and the polynomial defining
its fourth roots has discriminant a unit at odd primes.
The quadratic field extension \(J_-/\mathbb Q(i)\)
ramifies at the prime dividing \(D\), whereas \(J_+\) and
the field of the fibers are unramified there. Thus the
automorphism that exchanges the two roots for \(J_-\) acts
on the compositum while fixing \(J_+\), \(\beta\), and all \(V_0\).
There is a corresponding automorphism for \(J_+\).
The compositum contains \(\sqrt5\), from the product of the
two quadratic radicals, and hence contains \(U=\alpha^m\).

Work first with \(\Psi/\lambda\) and the normalized
absolute logarithmic height. At primes over the Gaussian
\(\pi\) contributing \(e_p>0\), the first automorphism
pairs the primes over the two split primes of \(J_-\).
The two valuations of \(\Psi/\lambda\) differ by
\(|j|e_p\) in absolute value after dividing by the
ramification index over \(J_-\): the factors in \(V-V_0\)
and \(w_+\) are fixed, and the original Laurent monomials
are units at finite places. The sum of the absolute values
of the paired valuations is at least their difference.
The local degree weights above either split prime sum
to \(1/[J_-:\mathbb Q]=1/4\).
The same argument on the conjugate Gaussian prime gives
\(|l|e_p\) with weight \(1/4\), on disjoint prime support.
Taking half the sum of the absolute logarithms, as in
the product-formula expression for height, gives
\[
 h(\Psi)\ \ge\ \frac{|j|+|l|}{8}\log E_n-h(\lambda).
 \tag{21}
\]

These specialized units also have prime support outside
any prescribed finite set for all sufficiently large square
indices, unless the unit is a scalar Laurent monomial.
For \(j\ne0\) or \(l\ne0\), use the same paired valuations
outside the rational primes below the prescribed set and
the primes of \(\lambda\). At a fixed prime the valuations
of \(P_{n\pm2}\) are \(O(\log n)\), by the binomial lifting
formula for the fixed unit \(\beta\), since for odd \(s\),
\(P_s=\beta^{-s}(\beta^{2s}+1)/(2\sqrt2)\).
Thus (20) leaves positive excess outside these finitely
many primes for all sufficiently large \(n\).
For \(j=l=0\), if a factor \(V-V_0\) has nonzero exponent,
it can share prime support with another such factor only
at the fixed primes of the difference between the two roots. Exclude the
primes of \(\lambda\) and of all such differences.
Each value \(\beta^m-V_0\) has absolute norm growing
exponentially in \(m\), since half the embeddings send
\(\beta\) to a unit of absolute value \(\beta>1\), while
the others give \(\beta^m\) tending to zero.
At each fixed prime its valuation is \(O(\log n)\):
\(V_0^4=\pm i\beta^{\pm2-r}\) and
\(\beta^m-V_0\) divides \(\beta^{4(n\mp2)}-1\) up to a unit.
The binomial valuation bound follows by first raising a unit
to its finite residue order and then to a fixed power of
the residue prime, so that the usual logarithmic lifting
formula applies. All the indicated constants are effective
for a fixed set of primes. More explicitly, if a unit has residue order \(h\)
at a fixed prime above \(p\), choose a fixed \(c\) so that the lifting formula
applies to its \(hp^c\)-th power. The binomial for the original exponent
divides the binomial for that exponent multiplied by \(hp^c\), whose
valuation is a constant plus the valuation of the original exponent.

## 7. The canonical exceptional subspace in a symmetric approximation

Put \(s=\sqrt2\), \(\theta=\sqrt{2+s}\), \(\theta'=\sqrt{2-s}\),
and \(L=\mathbb Q(\theta,\sqrt5)\). Its eight real embeddings are
generated by \(\tau\) and \(\eta\), where
\(\tau(\theta)=\theta'\), \(\tau(\theta')=-\theta\),
\(\tau(\alpha)=\alpha\), and \(\eta\) fixes \(\theta\) and sends
\(\alpha\) to \(-\alpha^{-1}\). The first field is cyclic of
degree four, with unique quadratic subfield \(\mathbb Q(s)\),
so \(L\) has degree eight. In particular \(\tau(s)=-s\) and
\(\tau(\beta)=-\beta^{-1}\).

For an odd square index \(n=2m+1\ge5\) and \(x>0\) with
\(x^2=a_n\), take the seven coordinates
\[
\begin{array}{lll}
 y_0=2x,& y_1=\beta^m\theta,&y_2=(-1)^{m+1}\beta^{-m}\theta',\\
 y_3=s\theta\beta^{-m-1}\alpha^n,& y_4=-s\theta\beta^{-m-1}\alpha^{-n},\\
 y_5=(-1)^{m+1}s\theta'\beta^{m+1}\alpha^n,&
 y_6=(-1)^m s\theta'\beta^{m+1}\alpha^{-n}.
\end{array}
\]
The simultaneous conjugation of these coordinates is
\(g(\mathbf y)=\rho(g)\mathbf y\), where the rational signed
permutations are
\[
 \rho(\tau)Y=(Y_0,-Y_2,Y_1,-Y_5,-Y_6,Y_3,Y_4),\qquad
 \rho(\eta)Y=(Y_0,Y_1,Y_2,Y_4,Y_3,Y_6,Y_5).
\]
These identities follow from the actions on \(\alpha,\beta,\theta,\theta'\)
and the parity of \(n\). The matrices commute.

Write \(a=\log\alpha\), \(b=\log\beta\), \(z=\alpha/\beta\),
and \(u=(\alpha\beta)^{-n}\). At the identity embedding the
distinguished form is \(L_0=Y_0-Y_1-Y_3\), with the other six
forms \(Y_1,\ldots,Y_6\). Indeed \(y_1=2^{1/4}\beta^{n/2}\)
and Binet's formula gives
\[
 \frac{4x^2}{y_1^2}=1+t,\qquad t=2s z^n-2s u+\beta^{-2n}.
\]
Here \(0<t<2s z^n<1\). The inequalities
\(1+t/2-t^2/8\le\sqrt{1+t}\le 1+t/2\) give
\[
 \frac{|L_0(\mathbf y)|}{y_1}\le z^{2n}+s u,\qquad
 |L_0(\mathbf y)|<\frac75\left(\frac{\alpha^2}{\beta^{3/2}}\right)^n.
 \tag{22}
\]
For the strict bound use \(u/z^{2n}=(\beta/\alpha^3)^n\),
\(\beta/\alpha^3<3/5\), \(s<3/2\), and \(2^{1/4}<6/5\).
The other six values are exact powers times constants of absolute
value either \(2^{1/4}\) or \(2^{3/4}\). The real exponents for
all seven forms, including the upper bound in (22), are
\[
 (\lambda_0,\ldots,\lambda_6)=
 \left(2a-\tfrac32b,\tfrac b2,-\tfrac b2,a-\tfrac b2,
       -a-\tfrac b2,a+\tfrac b2,\tfrac b2-a\right).
 \tag{23}
\]

At the real place \(v_g\) use the basis
\(L_{i,g}=L_i\circ\rho(g)^{-1}\) with the corresponding weights
\(c_{i,g}=(\lambda_i-\lambda_0/7)/8\). Signed coordinate forms
have the same role as unsigned ones in these weights.
At finite places use the coordinate basis with zero weights.
Each basis has determinant of absolute value 1, and the
weights sum to zero at each place. Their summed maxima are
\(\lambda_5-\lambda_0/7<1\). For these inequalities one may
use \(0.481<a<0.482\) and \(0.881<b<0.882\).
For example, these enclosures follow from
\(1.61803<\alpha<1.61804\), \(2.41421<\beta<2.41422\),
and the logarithm series in \((q-1)/(q+1)\) for each rational
endpoint \(q\). For the first eight terms the positive tail
is at most \(2((q-1)/(q+1))^{17}/(17(1-((q-1)/(q+1))^2))\).

Use the product-formula absolute values normalized by
\([L:\mathbb Q]=8\), so an archimedean local factor is the
eighth root of the usual real absolute value. For \(Q=e^n\),
each real factor of the twisted height
\(H_{\mathcal L,\mathbf c,Q}(\mathbf y)\) is bounded by
\(2^{1/8}\exp(\lambda_0 n/56)\) by (22)–(23).
At finite places every coordinate is integral, so each factor
is at most 1. Consequently, for \(n\ge100\),
\[
 H_{\mathcal L,\mathbf c,Q}(\mathbf y)
 \le 2\exp(\lambda_0 n/7)<Q^{-1/25}.
 \tag{24}
\]

**The canonical subspace is zero.** With the minimum over
bases of restrictions as in [1, (2.19)–(2.21)], write \(w(W)\)
for the sum of the local weights of a proper subspace \(W\)
of \(\overline{\mathbb Q}^7\). The canonical subspace \(T\)
maximizes \(w(W)/(7-\dim W)\), with minimal dimension in case
of equality. Its uniqueness and the rationality of the forms
make \(T\) rational. The same uniqueness makes \(T\) invariant
under \(\rho(\tau)\) and \(\rho(\eta)\), which permute the real
weighted bases and preserve the zero finite weights.
It suffices to show \(w(W)<0\) for each nonzero proper rational
invariant \(W\), of dimension \(k\).

If \(W\) contains \(e_0=(1,0,\ldots,0)\), choose \(k-1\)
fixed coordinate restrictions from \(Y_1,\ldots,Y_6\) that
are independent on \(W\). At every real place the distinguished
form adds another independent restriction, since its value on
\(e_0\) is 1. The sum of the uncentered exponents of any fixed
coordinate over all real places is zero, by its signed permutation
orbit in (23). The total centered weight of these choices is
\(\lambda_0(1-k/7)<0\).

Otherwise \(W\) is contained in \(Y_0=0\), because the projection
onto \(\mathbb Q e_0\) is \((1+\rho(\tau)^2)/2\). Decompose \(W\)
into the two eigenspaces for \(\rho(\eta)\). The full negative
eigenspace is the rational two-dimensional plane with
\(Y_1=Y_2=0,\ Y_4=-Y_3,\ Y_6=-Y_5\); it is irreducible for
\(\rho(\tau)\) since that map squares to \(-1\). In the positive
eigenspace there are two copies of the same rotation, on
\(E=(Y_1,Y_2)\) and \(B=(Y_3,Y_5)\) with
\(Y_3=Y_4,\ Y_5=Y_6\). A two-dimensional invariant subspace of
the positive eigenspace is \(E\) or a graph from \(B\) to \(E\),
since a nonzero projection to \(B\) is onto.

In this case the minimized weight is the same at all real
places, by invariance of \(W\). The following independent sets
at the identity embedding suffice. The sums refer to the
uncentered exponents (23).

| \(W\) | Basis of restrictions | Exponent sum |
| --- | --- | --- |
| \(k=2\), pure \(E\) | \(L_0,Y_2\) | \(\lambda_0-b/2\) |
| \(k=2\), all other cases | \(Y_4,Y_6\) | \(-2a\) |
| \(k=4\), full positive eigenspace or \(E\) plus the negative plane | \(L_0,Y_2,Y_4,Y_6\) | \(\lambda_0-b/2-2a\) |
| \(k=6\) | \(L_0,Y_2,Y_3,Y_4,Y_5,Y_6\) | \(\lambda_0-b/2\) |

The remaining \(k=4\) case is a graph plus the negative plane.
Use \(v_3=(Y_3+Y_4)/2\), \(v_5=(Y_5+Y_6)/2\) on the graph,
so \(Y_1=A v_3+B' v_5\) and \(Y_2=-B'v_3+A v_5\) for some
\(A,B'\in\mathbb Q\). The map has this form because it commutes
with the rotation. The three restrictions \(Y_3,Y_4,Y_6\) are
independent and their span excludes \(v_5\), which has a nonzero
coefficient of \(Y_5\) in the free coordinates \(Y_3,Y_4,Y_5,Y_6\).
If \(A\ne0\), add \(Y_2\) for exponent sum \(-a-b\).
If \(A=0\) and \(B'\ne0\), add \(L_0\) for sum
\(\lambda_4+\lambda_0\). If \(A=B'=0\), use
\(L_0,Y_4,Y_5,Y_6\) for sum \(\lambda_0-\lambda_3\).
Each sum in the table and these three sums is strictly less
than \(k\lambda_0/7\), using the same bounds for \(a,b\).
Centering (23) thus gives \(w(W)<0\). Since \(w(0)=0\), the
canonical space is \(T=0\).

With \(\delta=1/25\) and \(R=15\) (at most eight distinguished
forms and seven coordinate forms, after choosing coordinate
signs), [1, Theorem 2.3] applies directly to (24). Its height
intervals cover all \(Q=e^n\) for the square indices \(n\ge100\).
The theorem bounds the number of intervals and the ratio of
their logarithmic endpoints. To bound \(n\) by this argument
one still needs an effective upper limit on their locations.

**Zeros in a specified hyperplane.** The symmetric vector also
has a direct effective zero bound. If \(\sum_{j=0}^6c_jy_j=0\)
for \(\mathbf c\in L^7\setminus\{0\}\), put \(B_0=h(\mathbf c)\),
the absolute projective logarithmic height. Then
\[
 n\le 200 B_0+105.
 \tag{25}
\]
Normalize \(c_0=-1\) if \(c_0\ne0\), otherwise normalize a
nonzero coefficient to 1. Each nonzero normalized coefficient
has absolute value between \(e^{-8B_0}\) and \(e^{8B_0}\), by
the height of a coordinate ratio. A nonzero difference from
1 has absolute value at least \(2^{-8}e^{-8B_0}\), by the
height inequality for a sum. Dividing by \(y_1\) gives
the following distinct exact ratios for the unit coordinates:
\[
 \frac{(y_1,y_2,y_3,y_4,y_5,y_6)}{y_1}
 =\big(1,(-1)^{m+1}\beta^{-n},s z^n,-s u,
       (-1)^{m+1}s\alpha^n,(-1)^m s\alpha^{-n}\big).
\]
If \(c_0=-1\), Taylor's formula additionally gives
\[
 \frac{2x}{y_1}=1+s z^n-z^{2n}+R_n,\qquad |R_n|<4z^{3n}.
\]
In fact the first-order error from \(t-2s z^n\) is at most
\(s u\), the error in the quadratic term is at most \(2u z^n\),
and the third-order remainder is at most \(s z^{3n}\).
Use \(u<z^{3n}\) and \(z<7/10\). If \(c_0=-1\), the term
with base \(z^2\) has coefficient 1 and guarantees a nonzero
term preceding the error. Otherwise the distinct exact ratios
give a nonzero term without an error. The bases in decreasing
order, inserting \(z^3\) for the error, are
\[
 \alpha>1>z>\alpha^{-1}>z^2>\beta^{-1}>z^3>(\alpha\beta)^{-1}.
\]
The difference of the logarithms of any successive pair is
greater than \(0.08\), by the bounds on \(a,b\). In the equation
for the hyperplane, divide by the largest base to the power \(n\)
among terms with nonzero coefficient. Its coefficient has
absolute value at least \(2^{-8}e^{-8B_0}\). The other terms
and the error have total absolute value at most
\(16e^{8B_0}e^{-0.08n}\). This implies (25), since
\(\log(4096)/0.08<105\).

**Seven-index determinant and a smaller global count.** For
square indices \(n_1<\cdots<n_7\) in one of the three odd
anchor classes, let \(D\) be the determinant of their seven
columns \(\mathbf y(n_j)\). It is a rational integer. Each
entry is integral, and conjugation multiplies the determinant
by \(\det \rho(g)=1\), since \(\rho(\tau)\) is a rotation on
each of three coordinate pairs and \(\rho(\eta)\) is the
product of two transpositions. Replacing row zero by \(L_0\)
preserves the determinant.

At the identity embedding the resulting entries in row \(i\)
and column \(j\) are \(d_{ij}\exp(\lambda_i n_j)\). For
\(n_1\ge3000\), each \(|d_{ij}|\) is between \(1/2\) and 2.
For row zero this uses the Taylor remainder from the proof
of (25), since the leading coefficient is \(-2^{1/4}\).
The other rows have their exact constants. The exponents in
increasing order are \(\lambda_4,\lambda_2,\lambda_0,\lambda_6,
\lambda_3,\lambda_1,\lambda_5\); consecutive differences
exceed \(0.08\). The ordering of the columns maximizes the
exponent sum \(S=\sum_{j=1}^7\lambda_{(j)} n_j\) by pairing
increasing exponents with increasing indices. Here \(\lambda_{(j)}\)
denotes the \(j\)-th exponent in increasing order. Every
other permutation loses at least \(0.08\cdot720720\), since
removing one inversion increases its sum by more than that
amount. The leading permutation contributes at least
\(2^{-7}e^S\), and all others together contribute at most
\(7!2^7 e^{S-0.08\cdot720720}<2^{-7} e^S\). Hence \(D\ne0\).

If all seven indices are in \([N,5N/4]\) for \(N\ge3000\),
then \(S\le N(\lambda_0+ (2a+b/2)/4)\), since
\(\sum_i\lambda_i=\lambda_0\) and the positive exponents
sum to \(2a+b/2\). The rational log bounds give
\(\lambda_0+(2a+b/2)/4<-0.006\), so
\[
 |D|\le7!2^7 e^{-0.006N}<1.
\]
This contradicts \(D\in\mathbb Z\setminus\{0\}\). Thus at
most six square indices in each anchor fall in such a window.

In the notation of [1, (2.22)] the number of exceptional
intervals is at most
\[
 m_0=\left\lfloor 10^5 2^{14}7^{10}25^2\log(1125)\right\rfloor
 <2.1\times10^{21},\qquad \omega_0=25\log45<100.
\]
The initial cutoff \(C_0\) for \(Q\) is less than \(e^{100}\):
the factor \(H_{\mathcal L}^{1/R}\) is at most \((7!)^{1/R}\)
because all forms have integer coefficients of absolute value
at most 1, and \(7^{25}<e^{100}\). Taking logarithms, each
remaining interval is covered by 21 windows of ratio \(5/4\),
since \((5/4)^{21}>100\). Intersecting a window with
\([3000,\infty)\) preserves this ratio bound. The initial
finite certificate leaves only \(n=3\) below 3000.
Consequently the total number of square indices is bounded by
\[
 1+3\cdot6\cdot21\,m_0 < 8\times10^{23}.
\]

## Reference

[1] J.-H. Evertse and R. G. Ferretti,
*A further improvement of the Quantitative Subspace Theorem*,
Annals of Mathematics 177 (2013), 513–590, Theorem 3.1.
https://doi.org/10.4007/annals.2013.177.2.4
