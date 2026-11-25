# Quantitative bound for the number of square indices

Let \(a_n=L_n+P_n\) be A060405 and let
\(\alpha=(1+\sqrt5)/2,\ \beta=1+\sqrt2,\ c=1/(2\sqrt2)\).
The previous square-gap result proves finiteness without giving a
bound on the number of exceptional indices. The following argument
gives an explicit, though very large, bound on their number.
It does not bound their positions.

**Theorem.** The number of nonnegative integers \(n\) for which
\(a_n\) is an integer square is less than \(10^{3739}\).

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

Use the seven-dimensional vector
\[
 {\bf z}=(x,(w^m)_{w\in{\cal W}})\in K^7.
\]
Let \(S\) be the four archimedean places of \(K\).
For each place \(v\), with real embedding \(\sigma_v\), choose the
six coordinate forms \(Z_w\), and one form \(L_{0,v}\) with
coefficient of \(X\) equal to 1. Its other two nonzero
coefficients are chosen so that evaluation at that embedding is
exactly \(x-A_r V^m-B_r(U/V)^m\).
Explicitly, extend \(\sigma_v\) to an automorphism \(\widetilde\sigma_v\)
of \(\overline{\mathbb Q}\), and use
\[
 L_{0,v}=X-\widetilde\sigma_v^{-1}(A_r)Z_{\sigma_v^{-1}(V)}
           -\widetilde\sigma_v^{-1}(B_r)Z_{\sigma_v^{-1}(U/V)}.
\]
The forms have determinant of absolute value 1 at every place.
All coordinate bases are units, and \(x\) is integral. Thus at
every finite place the maximum norm of the vector is 1. The
product formula cancels the archimedean absolute values of each
of the six unit coordinates. With absolute values normalized
as in Evertse [1], the product of the 28 form evaluations is
therefore
\[
 \prod_{v\in S}\prod_{i=0}^{6}|L_{i,v}({\bf z})|_v
 =|x-A_rV^m-B_r(U/V)^m|<5\,4^{-m}.
\]

The Euclidean projective height \(H({\bf z})\) in [1] satisfies
\[
 5^m<H({\bf z})<150^m\qquad(m\ge1).
\]
For the lower bound use the coordinates \(V^{\pm m}\), whose
maximum at each embedding is \(V^m>5^m\).
For the upper bound every conjugate of a base is at most
\(UV<40\), while \(x<\sqrt3\,\beta^{(4m+3)/2}<7V^m<50^m\).
Thus \(H({\bf z})<\sqrt7\,50^m<150^m\).

The forms have coefficient-field degree over \(K\) at most 4,
since the only needed extra generators are square roots of \(c\)
and \(\beta\) (or their conjugates). Their coefficient-vector
heights are less than 1000. For clarity, with \(h\) the absolute
logarithmic scalar height,
\[
 h(A_r)\le\tfrac14\log 8+\tfrac34\log\beta,\qquad
 h(B_r)\le\log2+\tfrac14\log8+
                 3(\tfrac12\log\alpha+\tfrac14\log\beta).
\]
The Euclidean projective height of the three nonzero coefficients
is at most \(\sqrt3\exp(h(A_r)+h(B_r))<1000\).

For \(m\ge5\), we have \(H({\bf z})>1000\) and
\[
 5\,4^{-m}<150^{-m/10}< H({\bf z})^{-1/10}.
\]
Since the finite-place norm of the vector is 1, division by the
archimedean vector norms gives precisely inequality (1.3) of [1]
with dimension 7, four places, \(\delta=1/10\), coefficient-field
degree bound 4 and form-height bound 1000.
By part (i) of the theorem on p. 228, for each fixed \(r\),
all such vectors are contained in at most
\[
 T=(2^{60\cdot7^2}10^{7\cdot7})^4
             \log16\,\log\log16<10^{3737}
\]
proper \(K\)-linear subspaces. For the last inequality it suffices
to note \(\log16\log\log16<3\) and to compare the integers
\(3\cdot2^{11760}\cdot10^{196}\) and \(10^{3737}\).

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

There are four choices of \(r\). The number of indices with
\(m\ge5\) is at most \(56T\); there are only twenty indices
with \(m<5\). Hence the total is less than \(10^{3739}\).

## 4. Consequence for the classification target

The bound is effective as a count, not as an index cutoff.
The quantitative theorem does not identify the hyperplanes;
their unknown coefficients prevent application of an effective
zero-location bound to their exponential polynomials.
The computation excluding all indices up to \(10^{322}\)
therefore cannot yet be combined with this count to prove
that \(n=3\) is the only nonnegative square index.

This reduction isolates the missing effective input in the
archimedean method: a computable height bound for the relevant
exceptional hyperplane coefficients, or another effective
description of their intersection with the exponential curve.
The local anchor-forcing approach remains independent.

## Reference

[1] J.-H. Evertse, *An improvement of the quantitative Subspace
theorem*, Compositio Mathematica 101 (1996), 225–311,
inequality (1.3) and theorem (i), p. 228.
https://www.numdam.org/item/CM_1996__101_3_225_0/
