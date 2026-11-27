# Exponential separation from squares and fixed square classes

Let \(a_n=L_n+P_n\) be A060405, with \(n\ge0\), and put
\[
 \alpha=\frac{1+\sqrt5}{2},\quad \beta=1+\sqrt2,\quad
 c=\frac1{2\sqrt2}.
\]
The results below use the Diophantine approximation theorem of
Kulkarni, Mavraki and Nguyen [1], rather than congruence certificates.

## 1. A uniform asymptotic expansion

The Binet formulas imply
\[
 a_n=c\beta^n+\alpha^n+
 O(\alpha^{-n}).
\]
Indeed the remaining two terms are
\((-1)^n(\alpha^{-n}-c\beta^{-n})\).
Writing \(u_n=(a_n-c\beta^n)/(c\beta^n)\), we have
\(u_n=O((\alpha/\beta)^n)\). For large \(n\), Taylor's theorem
gives \((1+u_n)^{1/2}=1+u_n/2+O(u_n^2)\), hence
\[
 \sqrt{a_n}=\sqrt c\,b_1^n+
 \frac1{2\sqrt c}b_2^n+O(\rho^n),
 \qquad
 b_1=\sqrt\beta,\quad b_2=\frac{\alpha}{\sqrt\beta},
 \quad \rho=\frac{\alpha^2}{\beta^{3/2}}.
\]
Here the inverse-root error is
\(O((1/(\alpha\sqrt\beta))^n)\), which is absorbed in
\(O(\rho^n)\), since \(\beta<\alpha^3\).
The elementary inequalities
\[
 1<b_2<b_1,\qquad 0<\rho<1
\]
follow from \(\beta<\alpha^2<\beta^2\) and \(\alpha^4<\beta^3\).
The error constant is independent of any positive integer \(d\)
when the expansion is divided by \(\sqrt d\).

## 2. The conjugate obstruction

The following consequence of [1, Theorem 1.4(iv)] is useful.
For a nondegenerate tuple of algebraic numbers \(b_i\) with
\(|b_i|\ge1\), an infinite sequence of exponentially close
integer approximations to
\(\sum_i q_{i,n}b_i^n\), with nonzero coefficients in a fixed
number field and \(h(q_{i,n})=o(n)\), requires that every
conjugate \(\sigma(b_i)\) of modulus at least one be equal to some
\(b_j\) up to multiplication by a root of unity. Here \(h\)
is absolute logarithmic Weil height. For varying coefficients
along a subsequence, the height condition gives a positive
sublinear majorant as required in that theorem.

Our tuple \((b_1,b_2)\) is nondegenerate because its two
positive entries have different magnitudes. Choose an embedding
of \(\mathbb Q(\sqrt2,\sqrt5)\) fixing \(\sqrt5\) and changing
\(\sqrt2\) to \(-\sqrt2\), and extend it to an automorphism of
\(\overline{\mathbb Q}\). It sends \(\beta\) to \(-\beta^{-1}\).
Consequently
\[
 |\sigma(b_2)|=\alpha\sqrt\beta>b_1>b_2.
\]
Neither quotient \(\sigma(b_2)/b_i\) can be a root of unity.
The necessary condition therefore fails, independently of
the choice of the nonzero coefficients of sublinear height.

## 3. Exponential gap from the nearest square

**Theorem.** Define
\(\Delta_n=\min_{x\in\mathbb Z}|a_n-x^2|\).
For every \(\epsilon>0\), for all sufficiently large \(n\),
\[
 \|\sqrt{a_n}\|_{\mathbb Z}>e^{-\epsilon n},
 \qquad
 e^{(\frac12\log\beta-\epsilon)n}<\Delta_n
 <e^{(\frac12\log\beta+\epsilon)n}.
\]
In particular \(\Delta_n>0\) eventually, and
\[
 \lim_{n\to\infty}\frac{\log\Delta_n}{n}
 =\frac12\log\beta.
\]

**Proof.** Suppose the first inequality failed infinitely often
for some \(\epsilon>0\). By the expansion in Section 1 the
two-term power sum with constant coefficients would then be
within \(O(e^{-\epsilon n}+\rho^n)\) of an integer infinitely
often. Choosing \(\theta\) strictly between
\(\max(e^{-\epsilon},\rho)\) and one absorbs the implied
constant. The conjugate obstruction contradicts [1, Theorem
1.4(iv)], which permits the distance to be zero.

For \(x\ge0\), factor
\[
 |a_n-x^2|=|\sqrt{a_n}-x|(\sqrt{a_n}+x)
 \ge \sqrt{a_n}\|\sqrt{a_n}\|_{\mathbb Z}.
\]
Since \(\sqrt{a_n}\sim\sqrt c\,\beta^{n/2}\), use the first
inequality with \(\epsilon/2\) to absorb the constant in the
desired lower bound. For the upper bound choose the nearest
integer to \(\sqrt{a_n}\); the error is at most
\(\sqrt{a_n}+1/4\). This proves the estimates and the limit.

## 4. Fixed square classes and the limitation of variable coefficients

For every fixed positive integer \(d\), the identical argument applied
to \(\sqrt{a_n/d}\) gives
\[
 \lim_{n\to\infty}\frac1n\log\min_{x\in\mathbb Z}|a_n-dx^2|
 =\tfrac12\log\beta.
\]
The coefficients are now divided by \(\sqrt d\) but are still fixed.
Consequently the squarefree kernel
\[
 \operatorname{sf}(a_n)=\prod_{v_p(a_n)\text{ odd}}p
\]
tends to infinity. Indeed, a bounded kernel would give infinitely
many indices in one fixed square class, contrary to the gap estimate.

The same argument is uniform along any subsequence \(n_j\) with
positive integers \(d_j\) such that \(\sqrt{d_j}\) belong to a
fixed number field and \(\log d_j=o(n_j)\). To apply [1] with
arbitrary varying square classes, however, its fixed-number-field
hypothesis would need to be addressed. No exponential lower bound
on the unrestricted squarefree kernel is asserted here.

## 5. Finiteness with unrestricted perfect-power exponent

The fixed-exponent argument in README.md proves, for every
integer \(k\ge2\), finiteness of the solutions \(a_n=x^k\).
The general exponent bound of Shorey–Stewart and Pethő,
as recalled in [2, introduction], applies to simple
integer recurrences with a dominant root and at least one other
root. Our characteristic polynomial is
\((X^2-X-1)(X^2-2X-1)\), with four distinct roots and unique
dominant root \(\beta\). Thus there is an effectively computable
upper bound for the exponent \(k\) in solutions with \(n,x,k>1\).
Combining that bound with the fixed-exponent finiteness theorem
proves that A060405 contains only finitely many perfect powers
even with the exponent allowed to vary.

This does not bound the last square index. The asymptotic gap
theorem uses the Subspace Theorem and is likewise ineffective
as an index bound. In particular the earlier congruence certificate
and the gap theorem do not yet overlap to give the unrestricted
classification.

## References

[1] A. Kulkarni, N. M. Mavraki and K. D. Nguyen,
Algebraic approximations to linear combinations of powers:
an extension of results by Mahler and Corvaja-Zannier,
Trans. Amer. Math. Soc. 371 (2019), 3787–3804.
https://arxiv.org/abs/1511.08525 (Theorem 1.4).

[2] Y. Bugeaud and H. Kaneko, On perfect powers in linear
recurrence sequences of integers, Kyushu J. Math. 73 (2019),
221–231. https://doi.org/10.2206/kyushujm.73.221
