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
cover, totally ramified at those four points. A unit of the
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
none of the three \(Z\)-factors in (17) vanishes.
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

## Reference

[1] J.-H. Evertse and R. G. Ferretti,
*A further improvement of the Quantitative Subspace Theorem*,
Annals of Mathematics 177 (2013), 513–590, Theorem 3.1.
https://doi.org/10.4007/annals.2013.177.2.4
