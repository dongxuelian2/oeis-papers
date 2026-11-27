# Norm descents for the square indices of A060405

Write \(a_n=L_n+P_n\), and let \(F_n\) be the Fibonacci numbers. Define
\(Q_j\) by \((1+\sqrt2)^j=Q_j+P_j\sqrt2\). The descent below completes
the even-index classification. A Gaussian factorization gives further
necessary conditions on the odd indices.

## 1. Exclusion of all even indices

**Theorem.** For every \(n\ge0\) with \(n\equiv6\pmod8\), \(a_n\) is
nonsquare. Consequently every nonnegative square index of A060405 is
odd.

**Proof.** Write \(n=2m\), so that \(m\equiv3\pmod4\), and put
\(Y=m+1=2^k t\) with \(k\ge2\) and \(t\) odd. Binet's formulas give
\(L_{2m}=5F_m^2-2\). The Pell addition and subtraction identities give
\(P_{2m}-P_2=2Q_{m+1}P_{m-1}\), because \(m-1\) is even. Thus a
square value \(a_{2m}=x^2\) satisfies
\[
x^2-5F_m^2=2Q_Y P_{Y-2}.                                      \tag{1}
\]
For every odd prime \(p\) with \((5/p)=-1\), a nonzero value of
\(X^2-5Z^2\) has even \(p\)-adic valuation. Divide out the common
power of \(p\) from \(X,Z\), then use the nonsquare residue of 5.

Put \(\beta=1+\sqrt2\). At an odd prime \(p\), regard \(\beta\) as a
unit in a residue field contained in \(\mathbb F_{p^2}\). For even
\(s\), the conditions \(p\mid Q_s\) and \(p\mid P_s\) are equivalent
to \(\beta^{2s}=-1\) and \(\beta^{2s}=1\), respectively. A common
odd prime divisor of \(Q_Y,P_{Y-2}\) would therefore satisfy
\(\beta^4=-1\) and divide \(Q_2=3\). But
\(\beta^4=17+12\sqrt2\equiv-1\pmod3\), so \(3\nmid Q_Y\) for
\(4\mid Y\). Equation (1) requires
\[
v_p(Q_Y)\equiv0\pmod2 \qquad (p\text{ odd},\ (5/p)=-1).        \tag{2}
\]

For even \(s\), odd \(b\), and an odd prime \(p\mid Q_s\), one has
\[
v_p(Q_{sb})=v_p(Q_s)+v_p(b).                                  \tag{3}
\]
Indeed \(2\beta^s Q_s=1+\beta^{2s}\), and one applies the
binomial valuation formula to \(-\beta^{2s}\) at a prime over \(p\)
in \(\mathbb Q(\sqrt2)\). The extension is unramified at odd primes.
Also \(Q_s\mid Q_{sb}\), since \(Z+1\) divides \(Z^b+1\) for odd
\(b\), so the rational quotient is an algebraic integer. Both
companion terms are odd by the recurrence. If \(q\ne p\) divides
\(Q_{sp}/Q_s\) for an odd prime \(p\), (3) shows \(q\nmid Q_s\).
Consequently \(\beta^{2s}\) has a \(p\)-part in its order modulo
\(q\), since its \(p\)-th power is \(-1\) and it differs from
\(-1\). Thus \(p\mid q^2-1\), and oddness of \(p,q\) gives \(q>p\).

Modulo 5 one has \(\beta^6=-1\), \(Q_4\equiv Q_8\equiv2\), so
\(Q_s\equiv2\pmod5\) whenever \(4\mid s\) and \(3\nmid s\).
Start with \(s=2^k\). The equality \((Q_s/5)=-1\) gives an odd
prime \(p\) with \((5/p)=-1\) and \(v_p(Q_s)\) odd. As
\(3\nmid Q_s\), this prime exceeds 5. By (2) and (3), \(p\mid Y/s\).

Given such \(s,p\), form \(C=Q_{sp}/Q_s\). Since \(3\nmid sp\),
\(C\equiv1\pmod5\). Equation (3) gives \(v_p(C)=1\). Quadratic
reciprocity and the positive character of \(C\) therefore give a
second prime \(q\ne p\) with \((5/q)=-1\) and \(v_q(C)\) odd.
This prime exceeds \(p\), and its valuation in \(Q_{sp}\) is odd
because \(q\nmid Q_s\). Replace \((s,p)\) by \((sp,q)\). Each
replacement preserves \(s\mid Y\) and \(3\nmid s\). Iteration
would give infinitely many distinct prime divisors of \(Y\), a
contradiction.

For the other even classes, the recurrence state
\((L_n,L_{n+1},P_n,P_{n+1})\) returns to its initial state after 48
steps both modulo 16 and modulo 5. Iteration gives the following
values modulo 16 for \(n=r,r+8,\ldots,r+40\).

| \(r\) | Values of \(a_n\bmod16\) |
|---:|:---|
| 0 | \(2,7,15,10,15,7\) |
| 2 | \(5,5,4,13,13,12\) |
| 4 | \(3,6,3,11,14,11\) |

The square residues modulo 16 are \(0,1,4,9\), so the table
leaves only \(n\equiv18\pmod{48}\). But \(a_{18}\equiv3\pmod5\).
This completes the even-index classification. \(\square\)

## 2. A Gaussian factorization for the odd indices

For each positive odd \(s=2h+1\), put
\[
R_s=Q_h+(1+i)P_h\in\mathbb Z[i],\qquad d_\pm=1\pm2i.
\]
For an odd Gaussian prime \(\pi\) coprime to \(d_\pm\), write
\(\chi_\pm(\pi)=(d_\pm/\pi)_2\) for the quadratic residue symbol.
Extend it multiplicatively to Gaussian elements of odd norm coprime
to \(d_\pm\), and assign value zero when \(d_\pm\) divides the element.

**Theorem.** Let \(n\ge3\) be an odd square index. Then \(3\nmid n+2\),
and at every positive divisor \(s\mid n+2\), the valuation of \(R_s\)
at each Gaussian prime with \(\chi_+(\pi)=-1\) is even. For
\(s\mid n-2\), the corresponding conclusion holds with \(\chi_-\)
if \(3\nmid s\) or \(5\nmid n-2\).
If \(3\mid n-2\) and \(5\nmid n-2\), then \(v_3(n-2)=1\)
and every prime dividing \((n-2)/3\) is a quadratic residue modulo 5.

**Factorization.** For \(n=2m+1\), set \(d=d_+\) for even \(m\)
and \(d=d_-\) for odd \(m\). One has \(L_n+2i=dz^2\) with
\(z=(L_m+\overline d F_m)/2\in\mathbb Z[i]\). To check it, expand
the square, use \(d\overline d=5\) and
\(L_m^2-5F_m^2=4(-1)^m\), and use
\(L_{2m+1}=(L_m^2+10L_mF_m+5F_m^2)/4\). The parity of
\(L_m,F_m\) agrees since \(L_m=2F_{m+1}-F_m\).

Put \(\gamma=-i\beta\) and let \(K=\mathbb Q(i,\sqrt2)\).
For \(s=2h+1\), one has
\[
\gamma^s-1=(-1)^h\beta^h(\gamma-1)R_s.                         \tag{4}
\]
For example, substitute \(\beta^h=Q_h+\sqrt2P_h\) and
\(\beta^{-h}=(-1)^h(Q_h-\sqrt2P_h)\) in the left hand side.
The same substitution gives the following Pell factorization
for odd \(n\ge3\):
\[
P_n-2i=
\begin{cases}
R_{n-2}\,\overline{R_{n+2}},&n\equiv3\pmod4,\\
\overline{R_{n-2}}\,R_{n+2},&n\equiv1\pmod4.
\end{cases}                                                   \tag{5}
\]
In detail, for \(j=n-2\), \(\ell=n+2\), multiply
\((\beta^{j/2}-i\beta^{-j/2})(\beta^{\ell/2}+i\beta^{-\ell/2})\)
to get \(2\sqrt2(P_n-2i)\). For \(s=2h+1\) each minus factor
divided by \(\beta^{1/2}-i\beta^{-1/2}\) is \(R_s\) if \(h\)
is even, and \((1+i)\overline{R_s}/\sqrt2\) if \(h\) is odd.
The plus factors are conjugate. The two indices have equal
\(h\)-parity and the constant product is \(2\sqrt2\), giving (5).

The rational norms of \(R_j,R_\ell\) are \(P_j,P_\ell\), by
\(P_{2h+1}=P_{h+1}^2+P_h^2\). They are coprime. An odd common
prime divisor would give \(\beta^{2j}=\beta^{2\ell}=-1\) and
\(\beta^8=1\) in its residue field. Since \(j\) is odd, these
relations give \(\beta^2=-1\), whereas \(\beta^2+1=2\sqrt2\beta\)
is an odd-prime unit. The Pell terms of odd index are odd.

If \(a_n=x^2\), then \(x^2-dz^2=P_n-2i\). At a Gaussian prime
with \((d/\pi)_2=-1\), the valuation of this nonzero norm is even,
by the argument used in (1). The factors in (5) are coprime, so
each has even valuations for the corresponding symbol. On
conjugating the appropriate factors, the symbol on \(R_{n-2}\)
is \(\chi_-\) and the symbol on \(R_{n+2}\) is \(\chi_+\) in
both cases of (5).

**Characters and lifting.** Gaussian quadratic reciprocity gives
\[
\chi_+(R_{2h+1})=(-1)^h\left(\frac{Q_h+3P_h}{5}\right),\qquad
\chi_-(R_{2h+1})=(-1)^h\left(\frac{Q_h+4P_h}{5}\right).          \tag{6}
\]
Indeed the primary associates of \(d_\pm\) are \(-d_\pm\), and
\(-1\) is a square in \(\mathbb Z[i]\). Reciprocity reduces the
symbol to the primary associate of \(R_s\) at \(d_\pm\). Its
normalization includes a factor \(\pm i\) exactly when \(h\) is
odd, giving the sign \((-1)^h\), since \(i\) is nonsquare in
both residue fields of size 5. The values of \(i\) modulo
\(d_+,d_-\) are 2 and 3, respectively. Modulo 5 the state
\((Q_h,P_h)\) has period 12, since \(\beta^6\equiv-1\). Formula
(6) gives \((\chi_+(R_s),\chi_-(R_s))=(1,1)\) when \(3\nmid s\)
and \((-1,0)\) when \(3\mid s\).
The norm condition for \(R_{n+2}\) forces \(\chi_+(R_{n+2})=1\),
since (6) gives a nonzero character and all its \(-1\) primes
have even valuation. Hence \(3\nmid n+2\).

The symmetry of the quadratic symbol on primary elements also
follows by squaring the quartic reciprocity law.
[Stevenhagen, *Class Field Theory*, §3.14](https://websites.math.leidenuniv.nl/algebra/cft.pdf)

Equation (4) gives \(R_s\mid R_{sb}\) for odd \(b\). Indeed
\(\gamma-1\) is a unit at all odd primes of \(K\), since
\(\gamma-1=-i(\beta-i)\) and
\((\beta-i)(-\beta^{-1}-i)=-2(1+i)\). Both Gaussian terms have
odd norm. For any Gaussian prime \(\pi\) over an odd rational
prime \(p\) dividing \(R_s\), the same binomial argument as in (3)
gives
\[
v_\pi(R_{sb})=v_\pi(R_s)+v_p(b).                               \tag{7}
\]
The field \(K=\mathbb Q(\zeta_8)\) is unramified at odd primes,
and their residue degrees divide 2. A prime over \(p\) divides
\(R_{sp}\) precisely when it divides \(R_s\), by Frobenius in
(4). At most one Gaussian prime over \(p\) divides \(R_s\), since
\(\gcd(R_s,\overline{R_s})=1\). For this last assertion, a common
prime would divide \(2iP_h\) and \(Q_h\), whereas
\(Q_h^2-2P_h^2=(-1)^h\) and \(R_s\) has odd norm. In particular
the rational primes dividing that norm split in \(\mathbb Z[i]\).

If a prime \(\lambda\) over \(q\ne p\) divides \(R_{sp}/R_s\),
then (7) and (4) give \(\lambda\nmid R_s\) and
\(\gamma^{sp}=1\ne\gamma^s\) modulo a prime above \(\lambda\).
Hence \(p\mid q^2-1\) and \(q>p\).

**Descent for \(3\nmid s\).** Let \(S\) denote the relevant
index \(n-2\) or \(n+2\). Suppose an odd exponent of a Gaussian
prime \(\pi\) with the relevant symbol \(-1\) occurs in \(R_s\)
for a divisor \(s\) of \(S\) coprime to 3. Let \(p\) be the
rational prime below \(\pi\). Then \(p\ge7\), since every
rational prime dividing the odd norm splits in \(\mathbb Z[i]\),
and (6) excludes 5 from the norm for \(3\nmid s\). Equation (7)
and the even valuation at \(R_S\) force \(sp\mid S\). The
quotient \(R_{sp}/R_s\) has symbol \(+1\) by (6), and its only
Gaussian prime above \(p\) occurs once with symbol \(-1\).
There is a second prime with symbol \(-1\) and odd exponent
over a strictly larger rational prime \(q\). Its exponent in
\(R_{sp}\) is odd. Repetition would give infinitely many prime
divisors of \(S\).

**Divisors of \(n-2\) divisible by 3.** Suppose \(n-2=3T\)
with \(5\nmid T\), and put \(S=n-2\). Here \(T\) is odd.
For odd \(b\) coprime to 5 one has
\[
\chi_-(R_{3b}/R_3)=\left(\frac b5\right).                     \tag{8}
\]
To see it, use (4) to express the quotient as
\((-1)^a\beta^{-a}\sum_{j=0}^{b-1}\gamma^{3j}\), where
\(a=3(b-1)/2\). At a prime above \(d_-\), \(\gamma^3=1\)
and \(\beta^3=-i\). The quotient therefore reduces to
\((-i)^{(b-1)/2}b\). Its primary normalization has a factor
\(\pm i\) exactly when \((b-1)/2\) is odd, as seen from
\(R_{3b}/R_3\bmod2\). The two signs in its quadratic symbol
cancel, proving (8).

Suppose a prime \(p\mid T\) has \((p/5)=-1\). By (8),
\(R_{3p}/R_3\) has a Gaussian prime of odd exponent and symbol
\(-1\). Its rational prime \(q\) differs from 5, because \(d_-\)
has character zero and its conjugate is coprime to \(R_{3p}\).
It also differs from \(p\), since \(p\nmid P_3=5\)
and the Frobenius argument following (7) gives \(p\nmid P_{3p}\).
The order of \(\gamma\) at a prime above this witness divides
\(3p\) and fails to divide 3, so it is divisible by \(p\).
The argument after (7) gives \(q>p\). The odd exponent in
\(R_{3p}\) then forces \(q\mid T\) by (7).

Maintain an odd-symbol prime of odd exponent in \(R_s\) with
\(3\mid s\mid S\), above a rational prime \(q\mid T\). If
\((q/5)=-1\), apply the preceding step to \(q\) at the index
\(3q\), yielding a larger prime. If \((q/5)=1\), (7) gives
\(sq\mid S\) and (8) gives \(\chi_-(R_{sq}/R_s)=1\).
The prime above \(q\) occurs once in this quotient, so there is
a second odd-symbol prime of odd exponent above a larger one.
In both cases the new prime divides \(T\) by (7). The resulting
strict increase contradicts the finiteness of its prime factors.
Thus every prime factor of \(T\) has symbol \(+1\), which
also gives \(3\nmid T\).

Now take \(3\mid s\mid S\) and a Gaussian prime \(\pi\) over \(p\) with
\(\chi_-(\pi)=-1\) and odd valuation in \(R_s\). This prime is absent
from \(R_3=2+i\), an associate of \(d_-\), and its rational prime
satisfies \(p\ne3,5\). For \(p=3\), this follows from the splitting
of primes dividing \(N(R_s)=P_s\) proved above. For \(p=5\), only \(d_-\)
can divide \(R_s\), since \(d_-\mid R_s\) by (6) and
\(\gcd(R_s,\overline{R_s})=1\).
The parity at \(R_S\) forces \(sp\mid S\), so \(p\mid T\).
The preceding argument for primes with \((p/5)=1\) now yields a
larger prime of odd valuation at \(R_{sp}\) with the same character.
Iteration again contradicts finite support. In particular
\(\chi_-(R_s/R_3)=1\) when \(3\mid s\mid S\).
\(\square\)

For example, \(R_{17}=985+408i\) has an odd exponent at the prime
over 137 with \(\chi_-=-1\), and \(R_{19}=2378+985i\) has an odd
exponent at the prime over 37 with \(\chi_+=-1\). Thus every odd
square index \(n\ge3\) satisfies \(17\nmid n-2\) and
\(19\nmid n+2\).
Also, \(R_{21}=5741+2378i\) has an odd exponent at the prime over
45697 with \(\chi_-=-1\). This gives \(21\nmid n-2\) when \(5\nmid n-2\).
The [certificate](verify_unified_structure.py) checks each witness.

## 3. Mixed-unit norm identities

For odd \(n\), put \(\alpha=(1+\sqrt5)/2\), \(u=\alpha^2\),
\(\eta=\beta/u\), and \(\xi=\beta u\). If \(a_n=x^2\), then
\[
\begin{aligned}
(L_n+\sqrt2)^2-2\sqrt2\,x^2
  &=-\beta^{-n}(\eta^n-1)(\xi^n-1),\\
(L_n-\sqrt2)^2+2\sqrt2\,x^2
  &=\beta^{-n}(\eta^n+1)(\xi^n+1).
\end{aligned}
\]
Indeed \(L_n^2+2=u^n+u^{-n}\) and
\(2\sqrt2 P_n=\beta^n+\beta^{-n}\), so expansion gives both identities.
The left sides are norms from the quadratic extensions obtained by
adjoining \(\sqrt{2\sqrt2}\) and \(\sqrt{-2\sqrt2}\) to
\(\mathbb Q(\sqrt2,\sqrt5)\). A common prime divisor of the
two factors on either right side requires \(u^{2n}=1\) and
\(\beta^n=\pm u^n\) in its residue field, with the sign matching
the factor equation. A descent with these identities would need to
control these common factors and produce an odd-valuation prime with
the required quadratic character on each remaining odd branch.
