# Quantitative bound for the number of square indices

Let \(a_n=L_n+P_n\) be A060405 and let
\(\alpha=(1+\sqrt5)/2,\ \beta=1+\sqrt2,\ c=1/(2\sqrt2)\).
The square-gap theorem gives finiteness. The following argument
bounds the number of square indices using explicit approximation
weights in the quantitative Subspace Theorem.

**Theorem.** The number of nonnegative integers \(n\) for which
\(a_n\) is an integer square is less than \(10^{29}\).

## 1. Explicit approximation and conjugate coordinates

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
 |x-A_r V^m-B_r(U/V)^m|<5\,4^{-m}.
\]

The real biquadratic field \(K=\mathbb Q(\sqrt2,\sqrt5)\) has four
archimedean places. The six distinct positive algebraic units
\[
 {\cal W}=\{V,V^{-1},UV,U/V,V/U,(UV)^{-1}\}
\]
are exactly the union of the conjugates of \(V\) and \(U/V\).
They are distinct because \(U,V\) are multiplicatively independent.
To see this, conjugate a proposed relation \(U^iV^j=1\) by the
automorphism that inverts \(U\) and fixes \(V\); dividing the
relations gives \(U^{2i}=1\), hence \(i=j=0\).

## 2. Quantitative subspace theorem

Use the vector
\[
 {\bf z}=(x,(w^m)_{w\in{\cal W}})\in K^7.
\]
At each real place \(v\) of \(K\), extend its embedding \(\sigma_v\)
to an automorphism \(\widetilde\sigma_v\) of \(\overline{\mathbb Q}\).
Take the six coordinate forms \(Z_w\), and take
\[
 L_{0,v}=X-\widetilde\sigma_v^{-1}(A_r)Z_{\sigma_v^{-1}(V)}
           -\widetilde\sigma_v^{-1}(B_r)Z_{\sigma_v^{-1}(U/V)}.
\]
At every place the coefficient determinant has absolute value 1.
The usual maximum-norm height of [1] is \(H({\bf z})=(UV)^m\)
for \(m\ge600\): all finite-place maxima are 1 since the \(w\)
are units and \(x\) is integral, and at each real place the largest
unit coordinate has ordinary absolute value \((UV)^m\), greater
than \(x<7V^m\).

Set \(\epsilon=3/8\). For the normalized absolute values of [1],
take weights
\[
 d_{0,v}=-(1+\epsilon)/4,\qquad
 d_{w,v}=\big(\log|\sigma_v(w)|/\log(UV)-1\big)/4.
\]
All weights are nonpositive. They sum over the four places
to \(-7-\epsilon\), since the product of the six \(w\) is 1.
The coordinate forms attain the bounds in (3.7) of [1].
For \(L_{0,v}\) the bound follows from
\(5\cdot4^{-m}<H({\bf z})^{-\epsilon}\), since \(UV<40\) and
\((128/125)^{600}>5^8\). The maximum over automorphisms fixing
\(K\) leaves \({\bf z}\) fixed.

The union of the forms has cardinality at most 10. Their coefficient
fields over \(K\) have degree at most 2, since \(A_r^2=c\beta^r\)
and \(2A_r B_r=\alpha^r\). For the inhomogeneous form height,
\(H^*(L_{0,v})\le \exp(h(A_r)+h(B_r))<1000\), with
\[
 h(A_r)\le\tfrac14\log 8+\tfrac34\log\beta,\qquad
 h(B_r)\le\log2+\tfrac14\log8+
                 3(\tfrac12\log\alpha+\tfrac14\log\beta).
\]
The Euclidean version of the form height also lies below 1000.
The lower height threshold of [1, Theorem 3.1] is
\(\max(1000^{1/60},7^{56/3})\), below \(H({\bf z})\)
for \(m\ge600\). That theorem covers the vectors for each \(r\)
by at most
\[
 T=10^9\,2^{14}\,7^{14}\,(8/3)^3
       \log(160)\log\big((8/3)\log60\big)
\]
proper linear subspaces defined over \(K\).

## 3. At most fourteen indices per subspace

Each proper subspace lies in a hyperplane
\[
 d_0X+\sum_{w\in{\cal W}}d_w Z_w=0
\]
with coefficients in \(K\), not all zero.

If \(d_0=0\), the resulting equation is a nonzero exponential
polynomial in \(m\) with at most six distinct positive bases.
It has at most five real zeros. In general, a nonzero real
linear combination of \(k\) distinct positive exponential bases
has at most \(k-1\) distinct real zeros: divide by the smallest
exponential and apply Rolle's theorem to the derivative, then
use induction.

If \(d_0\ne0\), the hyperplane gives
\(x=\sum_w b_w w^m\). Squaring and comparing with \(a_{4m+r}\)
gives an exponential polynomial with at most fifteen distinct
positive bases. In fact the exponent pairs of \({\cal W}\) in
\((U,V)\) are \(\{0,1,-1\}\times\{1,-1\}\); their pairwise
sums belong to \(\{-2,-1,0,1,2\}\times\{-2,0,2\}\).
The four original bases \(U,U^{-1},V^2,V^{-2}\) also lie
in this set of fifteen.

This exponential polynomial is nonzero. Otherwise independence
of distinct positive exponential bases and of \(U,V\) gives
a Laurent polynomial identity
\[
 C_1 u+C_2u^{-1}+C_3v^2+C_4v^{-2}=G(u,v)^2
\]
with all \(C_i\ne0\).
Assign weight 2 to \(u\) and weight 1 to \(v\). The maximal
weight part on the left is \(C_1u+C_3v^2\); on the right
it is the square of the maximal weight part of \(G\).
The binomial \(C_1u+C_3v^2\) has an irreducible factor of
multiplicity one in \(\overline{\mathbb Q}[u^{\pm1},v^{\pm1}]\):
as a polynomial in \(u\) it is linear, with nonzero root
\(-C_3v^2/C_1\) in \(\overline{\mathbb Q}(v)\).
It cannot be a square. This contradiction proves nonvanishing.
Rolle's bound now gives at most fourteen integer indices \(m\)
on the hyperplane.

The [norm descent](norm-descent.md) restricts \(r\) to 1 and 3.
The number of indices with \(m\ge600\) is thus at most \(28T\),
and there are at most 2400 indices with \(m<600\). The logarithmic
factors in \(T\) are less than \(26/5\) and \(5/2\), respectively.
The resulting upper bound satisfies \(28T+2400<10^{29}\).

## 4. Effective zero location in any specified hyperplane

There is a concrete sufficient height bound for completing the
archimedean route. Normalize a hyperplane by \(d_0=1\) if
\(d_0\ne0\), or by setting any nonzero coefficient equal to 1
otherwise. Let \(B\) be the maximum absolute logarithmic height
of its resulting nonzero coefficients.

**Proposition.** Every square index \(n=4m+r\) whose vector
belongs to this hyperplane satisfies
\[
 n\le 2000(B+1)+3.
\]

To prove this, write the nonzero exponential polynomial obtained
in Section 3 as \(f(m)=\sum_i c_i\lambda_i^m\) with real
coefficients in \(K\) and positive distinct bases. In the
\(d_0\ne0\) case, each coefficient after squaring is a sum
of at most six ordered products of two hyperplane coefficients,
possibly with one original Binet coefficient subtracted.
The heights of the original Binet coefficients for \(0\le r\le3\)
are less than 3, so
\[
 h(c_i)\le12B+3+\log7<12B+5.
\]
The case \(d_0=0\) has the stronger bound \(h(c_i)\le B\).
Since \([K:\mathbb Q]=4\), every nonzero \(c_i\) satisfies
\[
 e^{-4(12B+5)}\le |c_i|\le e^{4(12B+5)}.
\]

The ratio of any two unequal bases, larger divided by smaller,
is greater than \(5/4\). For the fifteen squared bases this
follows by taking differences of their exponent pairs: the
difference in the \(V\)-exponent is \(0,\pm2,\pm4\), and the
difference in the \(U\)-exponent is between -4 and 4.
For a zero \(V\)-exponent the ratio is at least \(U\).
For absolute \(V\)-exponent 2, the only adjacent powers of
\(U\) around \(V^2\) are \(U,U^2\); for absolute
\(V\)-exponent 4 they are \(U^3,U^4\).
All four ratios of adjacent powers to the intermediate value
(or its reciprocal, as appropriate) exceed \(5/4\), directly
from \(6.85<U<6.86\) and \(5.82<V<5.83\).
The six unsquared bases have exponent differences inside the
same ranges and satisfy the same bound.

At a zero \(m\ge0\), the largest base with nonzero coefficient
must be cancelled by the remaining at most fourteen terms.
Dividing by that largest term gives
\[
 1\le14 e^{96B+40}(4/5)^m.
\]
Hence
\[
 m\le\frac{96B+40+\log14}{\log(5/4)}
 <500(B+1).
\]
This proves the proposition. In particular, any explicit
upper bound on the normalized coefficient heights of the
exceptional hyperplanes in Section 2 immediately gives a
linear, explicit upper bound on the last square index.

## 5. Consequence for the classification target

A uniform bound on the coefficient heights of a covering family
of hyperplanes would turn the count into an index cutoff by
the proposition. The explicit cutoff needed to combine this
approach with the current [finite certificate](extended-lifting.md)
is \(10^{902}\).

## Reference

[1] J.-H. Evertse and R. G. Ferretti,
*A further improvement of the Quantitative Subspace Theorem*,
Annals of Mathematics 177 (2013), 513–590, Theorem 3.1.
https://doi.org/10.4007/annals.2013.177.2.4
