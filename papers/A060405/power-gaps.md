# Near-perfect-power gaps and the cubic resonance

Write \(a_n=L_n+P_n\) and define, for integer \(k\ge2\),
\[
 \Delta_k(n)=\min_{x\in\mathbb Z_{\ge0}}|a_n-x^k|.
\]
The square case was treated in square-gap.md. This note gives the
corresponding asymptotic separation for all fixed exponents, including
one exceptional cubic progression with a different exponent.

## Theorem

Let \(\alpha=(1+\sqrt5)/2,\ \beta=1+\sqrt2\).

1. For each fixed \(k\ge4\),
\[
 \lim_{n\to\infty}\frac{\log\Delta_k(n)}n
 =(1-1/k)\log\beta.
\]
2. For \(k=3\) and \(r=1,2\),
\[
 \lim_{\substack{n\to\infty\\n\equiv r\bmod3}}
 \frac{\log\Delta_3(n)}n=\tfrac23\log\beta.
\]
3. For every \(m\ge1\), the unique nearest cube to \(a_{3m}\)
is \((2P_m)^3\), and
\[
 \Delta_3(3m)=L_{3m}+3(-1)^mP_m>0,\qquad
 \lim_{m\to\infty}\frac{\log\Delta_3(3m)}{3m}=\log\alpha.
\]

In particular no index divisible by three gives a cube. The
limits in (1) and (2) are ineffective statements about large
indices, while (3) holds at every indicated index.

## Proof

Put \(c=1/(2\sqrt2)\). For each fixed \(k\ge3\), Taylor's formula
and the Binet expressions give
\[
 a_n^{1/k}=c^{1/k}\beta^{n/k}
 +O\bigl((\alpha\beta^{1/k-1})^n\bigr).
\]
Here \(\alpha\beta^{1/k-1}<1\): it is at most
\(\alpha\beta^{-2/3}<1\), since \(\alpha^3<\beta^2\).

Write \(n=km+r\), \(0\le r<k\), and put
\(C=(c\beta^r)^{1/k}\), the positive real root. The displayed
expansion is an exponentially good approximation to \(C\beta^m\).
If \(C\notin K_0=\mathbb Q(\sqrt2)\), some automorphism of
\(\overline{\mathbb Q}\) fixes \(\beta\) but moves \(C\).
By Theorem 1.4(iii) of Kulkarni–Mavraki–Nguyen [1], such a
coefficient cannot give infinitely many exponentially close
integer approximations to \(C\beta^m\): the quotient of the
conjugate base by the base is 1, so the corresponding term
would have to be fixed. The theorem applies to a constant
coefficient in a fixed number field, and the singleton tuple
\((\beta)\) is nondegenerate.

For \(C\in K_0\), taking field norms in \(C^k=c\beta^r\) gives
\[
 N(C)^k=(-1)^{r+1}/8.
\]
The rational 2-adic valuation of this identity forces \(k\mid3\).
Thus no such \(C\) exists for \(k\ge4\).
For \(k=3\), \(c=(1/\sqrt2)^3\); membership of \(C\) in \(K_0\)
would imply that the positive cube root of \(\beta^r\) lies
in \(K_0\). For \(r=1,2\) it would be an algebraic integer
unit \(u\) with \(1<u<\beta\), since both it and its inverse
satisfy monic equations over the ring of integers.
But \(\mathcal O_{K_0}=\mathbb Z[\sqrt2]\), and no unit is
strictly between 1 and \(1+\sqrt2\). Indeed, write
\(u=a+b\sqrt2\) and \(u'=\pm u^{-1}\); then
\(0<b=(u-u')/(2\sqrt2)<1\) in that interval.
For \(r=0\) the coefficient \(1/\sqrt2\) does belong to \(K_0\).

In every nonresonant residue class, for every \(\epsilon>0\)
and all sufficiently large \(n\),
\[
 \|a_n^{1/k}\|_{\mathbb Z}>e^{-\epsilon n}.
\]
Otherwise the approximation above would give infinitely many
exponentially close integer approximations forbidden by [1].
For \(y=a_n^{1/k}\) and \(x\ge0\), factor the difference of
powers to obtain
\[
 |y^k-x^k|\ge y^{k-1}|y-x|.
\]
Choosing the nearest integer to \(y\) also gives an upper bound
\(k(y+1/2)^{k-1}/2\) for the distance to a \(k\)-th power,
by the mean value theorem. Since
\(y\sim c^{1/k}\beta^{n/k}\), the two bounds prove (1) and (2).

For the resonant progression, the Pell triplication identity
\[
 P_{3m}=8P_m^3+3(-1)^mP_m
\]
follows by expanding
\((\beta^m-(-\beta^{-1})^m)^3\).
Thus \(a_{3m}=(2P_m)^3+L_{3m}+3(-1)^mP_m\).

We claim \(3P_m<L_{3m}<6P_m^2\) for all \(m\ge1\).
The lower bound follows from \(L_3=4>3P_1\),
\(L_{j+3}=2L_{j+1}+L_j>3L_j\) for \(j\ge3\), and
\(P_{m+1}<3P_m\).
For the upper bound, check \(m=1,2\) directly:
\(4<6\) and \(18<24\).
For \(m\ge2\), \(P_{m-1}/P_m>1/3\), so
\(P_{m+1}^2>(7/3)^2P_m^2>5P_m^2\), whereas
\(L_{3m+3}<5L_{3m}\). Induction proves the claim.

It follows that the displacement from \((2P_m)^3\) is
positive and smaller than \(6P_m^2+3P_m\), which is less
than half of the next cube gap \(12P_m^2+6P_m+1\).
Hence \((2P_m)^3\) is the unique nearest cube.
Finally \(P_m/L_{3m}\to0\) because \(\beta<\alpha^3\);
the displacement is asymptotic to \(L_{3m}\).
This proves (3). QED.

The cubic resonance explains why the square-gap exponent
cannot simply be generalized by replacing 2 with an arbitrary
power without examining the dominant coefficient.

## Reference

[1] A. Kulkarni, N. M. Mavraki, K. D. Nguyen,
Algebraic approximations to linear combinations of powers:
an extension of results by Mahler and Corvaja-Zannier,
Trans. Amer. Math. Soc. 371 (2019), 3787–3804, Theorem 1.4.
https://arxiv.org/abs/1511.08525
