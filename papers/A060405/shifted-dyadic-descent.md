# Dyadic factors at a fixed valuation of the index offset

Let \(n_0\in\{3,-3,-1\}\), write \(n=n_0+k\) with
\(k=2^a m\), and suppose \(a\ge4\) and \(m\) is odd.
The [extended lifting certificate](extended-lifting.md) gives
\(a\ge14\) for a square index \(n\) with \(k>0\).
Use \(\alpha=(1+\sqrt5)/2\), \(\beta=1+\sqrt2\),
\(\eta=\beta/\alpha^2\), and \(\xi=\beta\alpha^2\).
For \(j\ge1\), set
\[
 d=2^j,\qquad C_j=L_{2d}+2Q_d.
\]

## Mixed and companion dyadic factors

The conjugates of \(\eta^d\) are
\(\eta^d,\xi^d,\eta^{-d},\xi^{-d}\). Pairing each with its
inverse gives
\[
 N_{\mathbb Q(\sqrt2,\sqrt5)/\mathbb Q}(\eta^d+1)
 =\big(\beta^d+\beta^{-d}+\alpha^{2d}+\alpha^{-2d}\big)^2
 = C_j^2.
\]
For \(j=0\), the norm of \(\eta+1\) is \(-1\) by the odd norm
formula in [coupled norm descent](coupled-norm-descent.md) §6.
The Lucas and Pell companion factors at \(j=0\) are both 1.

**Splitting lemma.** For \(j\ge3\), every prime divisor \(p\)
of \(C_j\) splits completely in \(\mathbb Q(\sqrt2,\sqrt5)\)
and satisfies \(p\equiv1\pmod{2^{j+1}}\).

Indeed \(C_1=13\), \(C_2=81\), and Lucas and Pell doubling show
\(C_j\) is odd and \(C_j\equiv1\pmod5\) for \(j\ge2\).
At an ideal above any \(p\mid C_j\), the order of \(\eta\)
is \(2^{j+1}\). If \((2/p)=-1\), the residue degree is two
and \(v_2(p^2-1)=3\), which precludes \(j\ge3\).
If \((2/p)=1\) and \((5/p)=-1\), Frobenius exchanges
\(\eta,\xi\), giving \(\eta^d=\xi^d=-1\). Hence
\(\beta^{2d}=\alpha^{4d}=1\). For \(p\equiv7\pmod8\),
this gives \(\beta=\pm1\) in \(\mathbb F_p\), incompatible
with \(\beta=1+\sqrt2\) at odd \(p\). For \(p\equiv1\pmod8\),
the identities \(\alpha^{p+1}=-1\) and \(\alpha^{4d}=1\)
give order four for \(\alpha\). Both elements of order four
lie in \(\mathbb F_p\), contradicting \((5/p)=-1\).
Thus the residue field is \(\mathbb F_p\), where the order
of \(\eta\) divides \(p-1\). In particular every prime of
\(C_j\) for \(j\ge3\) has character \(+1\) under the mod-16
character used in [rational norm descent](coupled-norm-descent.md).

Let \(p\mid C_j\) with \(j<a\), and choose a prime ideal
over \(p\) where \(\eta^d=-1\). The order of \(\eta\) is
\(2d\), so \(\eta^k=1\). Put \(t=\alpha^k\),
\(b=\alpha^{n_0}\), and \(c=\beta^{n_0}\) in this residue field.
Then \(\beta^k=t^2\) and
\[
 t^2 a_n=\frac{c t^4+c^{-1}}{2\sqrt2}+b t^3-b^{-1}t.
\]
The shifted square equation becomes
\[
 t^2(x^2-a_{n_0})=(t-1)
 \left(\frac{(t+1)(c t^2-c^{-1})}{2\sqrt2}+b t^2+b^{-1}t\right).
\]
In the signed identities of [coupled norm descent](coupled-norm-descent.md) §2,
the product on the right reduces to
\((\eta^{n_0}-\sigma)(\xi^{n_0}t^4-\sigma)\).
The factor \(\eta^{n_0}-\sigma\) is a unit because \(n_0\)
is odd and \(2d\ge4\). The two companion factors
\(L_d,Q_d\) correspond to \(\alpha^{2d}=-1,\beta^{2d}=-1\),
respectively, giving exact order \(4d\) for the indicated unit.

## A criterion for simultaneous square residues

For an odd prime \(p\ne5\), let \(e_p\) be the maximum of the
two valuations at 2 of the orders of the Lucas and Pell
recurrence matrices modulo \(p\).

**Proposition.** Fix \(a\ge4\). Consider any finite collection
of moduli \(p^h\), where every \(p\) divides \(C_jL_{2^j}Q_{2^j}\)
for some \(1\le j<a\), or divides \(C_a\).
Suppose \(e_p\le a+1\) for each \(p\)
that splits completely in \(\mathbb Q(\sqrt2,\sqrt5)\).
For each anchor \(n_0\), infinitely many positive \(n\) satisfy
\(v_2(n-n_0)=a\) and make \(a_n\) a square modulo every chosen
prime power. The offsets can also be taken divisible by any
prescribed odd integer.

**Proof.** The terms \(L_{2^j}\) and \(Q_{2^j}\) are odd.
The initial values \(L_2=Q_2=3\) and the doubling formulas
\(L_{2d}=L_d^2-2\), \(Q_{2d}=2Q_d^2-1\) show that
these terms and \(C_j\) are coprime to 5. For the latter
claim, \(C_1=13\), and for \(j\ge2\) one has \(L_{2d}\equiv
Q_d\equiv2\pmod5\).

It suffices to prove \(e_p\le a+1\) at the primes that
have residue degree two. If 2 is a nonsquare modulo \(p\),
then \(p\equiv3,5\pmod8\) and \(v_2(p^2-1)=3\). Both
recurrence matrices diagonalize over \(\mathbb F_{p^2}\).
If 2 is a square and 5 a nonsquare, then
\(\beta\in\mathbb F_p^\times\) and
\(\alpha^{p+1}=-1\) in \(\mathbb F_{p^2}\).
For \(p\equiv1\pmod8\), the order of \(\alpha\) has
valuation 2 at 2. For \(p\equiv7\pmod8\), the order of
\(\beta\) has valuation at most 1 at 2.
The splitting lemma and the values \(C_1=13,C_2=81\)
cover the mixed factors.
At a prime dividing \(L_d\) or \(Q_d\), the order of
the indicated unit is \(4d\). If \(p\equiv1\pmod8\),
only \(Q_d\) can vanish, and if \(p\equiv7\pmod8\),
only \(L_d\) can vanish. In both cases \(e_p\le j+2\).
The conjugate of each unit is its negative inverse, which
preserves these upper bounds on the valuations at 2.

Choose \(m\) divisible by the odd parts of the matrix orders
modulo all the chosen prime powers and by the prescribed odd
integer. The reduction kernels from modulus \(p^h\) to \(p\)
are \(p\)-groups, so the valuations at 2 of the orders are
unchanged. For such an odd \(m\), each matrix raised to
\(k=2^a m\) has order dividing two modulo \(p^h\).
Its eigenvalues modulo \(p\) are equal signs, because the
original eigenvalues are negative inverses and \(k\) is even.
The matrix is therefore that scalar sign modulo \(p\), and
the reduction kernel of odd order gives the same sign modulo
\(p^h\). Write the two signs as \(\delta_L,\delta_P\).
It follows that
\(a_n\equiv\delta_L L_{n_0}+\delta_P P_{n_0}\pmod{p^h}\).

If both signs are positive, this is \(a_{n_0}\).
A negative sign requires \(2\) to be a square modulo \(p\),
since otherwise \(e_p\le3\). If just the Lucas sign is
negative, the value is \(a_{-n_0}\in\{1,9,2\}\), a square
modulo every power of such a \(p\).
If the Pell sign is negative, the order of \(\beta\) has
valuation \(a+1\) at 2 and \(\beta\in\mathbb F_p^\times\).
Thus \(p\equiv1\pmod{2^{a+1}}\), and \(-1\) and 2 are
squares modulo every power of \(p\). The resulting values
\(-a_{n_0}\) or \(-a_{-n_0}\) are squares as well.
All positive odd multiples of the resulting odd modulus for
\(m\) are admissible. \(\square\)

## Exact range of the prime test

**Corollary.** For every fixed \(a\ge14\) the preceding proposition
applies to all primes \(p\le10^8\) from the layers \(1\le j<a\)
and from \(C_a\).
In particular, the prescribed odd integer can be
\(720720/16\), or the odd part of the larger forced divisor for
the chosen anchor.

The [certificate](verify_shifted_dyadic.py) checks this as follows.
A possible exception must split completely and satisfy
\(p\equiv1\pmod{2^{16}}\). For each such prime up to \(10^8\),
it computes \(e_p\) by removing the odd part of \(p-1\) from
the matrix orders. An exception would have \(14\le a\le e_p-2\)
and consequently \(1\le j\le e_p-3\) for the companion factors
and \(1\le j\le e_p-2\) for the mixed factor. The certificate
tests these ranges by doubling modulo \(p\). It finds zero
exceptions among the 80 primes tested.

The local coverage question for this approach is whether
the deeper order condition \(e_p\ge a+2\) can supply
obstructions uniformly in \(a\ge14\). For the families above,
this condition confines the search to completely split primes
with \(p\equiv1\pmod{2^{a+2}}\).

## A reciprocity character on the mixed factors

For \(j\ge3\) and \(p\mid C_j\), define
\(\chi_\alpha(p)=(\alpha\bmod p\,/\,p)\) by choosing either
root of \(X^2-X-1\) over \(\mathbb F_p\). The splitting lemma
gives \(p\equiv1\pmod{16}\), and the two roots are negative
inverses, so their quadratic characters agree.

**Theorem.** For every \(j\ge3\),
\[
 \prod_{p\mid C_j}\chi_\alpha(p)^{v_p(C_j)}=-1.
\]
In particular \(C_j\) has a prime of odd valuation at which
\(\alpha\) has the full 2-primary order available in
\(\mathbb F_p^\times\).

**Proof.** In \(J=\mathbb Q(\sqrt{-5})\), set
\[
 w_j=2Q_{2^{j-1}}+F_{2^j}\sqrt{-5}.
\]
Lucas and Pell doubling give
\[
 C_j=4Q_{2^{j-1}}^2+5F_{2^j}^2=N_{J/\mathbb Q}(w_j).
\]
Indeed for \(d=2^j\) one has \(L_{2d}=5F_d^2+2\)
and \(2Q_d=4Q_{d/2}^2-2\).

Let \(E=J(i)=\mathbb Q(i,\sqrt5)\) and
\(W=E(\sqrt\alpha)\). The nontrivial automorphism of \(E/J\)
sends \(i\) to \(-i\) and \(\alpha\) to \(-\alpha^{-1}\).
Sending \(\sqrt\alpha\) to \(i/\sqrt\alpha\) gives a lift
whose square sends \(\sqrt\alpha\) to \(-\sqrt\alpha\).
The same computation with either possible sign shows that
\(\sqrt\alpha\) cannot already belong to \(E\).
Thus \(W/J\) is cyclic of degree four. The two quadratic
steps use units \(-1,\alpha\), so their defining
discriminants are units away from 2. The extension \(W/J\)
is therefore unramified at every odd prime.

Each rational \(p\mid C_j\) splits completely in \(E\).
At a prime of \(J\) above such a \(p\), its Frobenius in
\(\operatorname{Gal}(W/J)\) is in the order-two subgroup
fixing \(E\). Identify the identity and nonidentity there
with \(+1,-1\), respectively. In this identification the
Frobenius equals \(\chi_\alpha(p)\), by reduction of
\(X^2-\alpha\). The Artin symbol of \((w_j)\) is consequently
\(\prod_{p\mid C_j}\chi_\alpha(p)^{v_p(C_j)}\).
The same symbol is obtained from \((\overline{w_j})\).

By [Artin reciprocity](https://www.jmilne.org/math/CourseNotes/CFT.pdf),
this ideal symbol is the inverse of the local symbol of
\(w_j\) at the unique prime of \(J\) over 2. Indeed \(w_j\)
has odd norm, every other finite place is unramified,
and the archimedean place is complex.
In the dyadic completion \(J_2\), an element of
\(1+32\mathcal O_{J_2}\) is a fourth power: with
\(v(2)=2\), the polynomial \(X^4-u\) at \(X=1\) has
\(v(1-u)\ge10>2v(4)=8\). Hence the local symbol of a
unit depends only on its residue modulo 32.

For \(j\ge4\), the identities
\(Q_{2d}=2Q_d^2-1\), \(L_{2d}=L_d^2-2\), and
\(F_{2d}=F_d L_d\) give
\[
 Q_{2^{j-1}}\equiv1\pmod{16},\qquad
 L_{2^j}\equiv-1\pmod{32},\qquad
 F_{2^j}\equiv(-1)^{j-4}F_{16}\pmod{32}.
\]
The starting residues are \(Q_8=577\), \(L_{16}=2207\),
and \(F_{16}=987\). Thus \(w_j\) is congruent to \(w_4\)
or \(\overline{w_4}\) modulo 32, and both give the same
Artin symbol. Finally \(C_3=3361\) and \(C_4=6202561\)
are primes, with \(\chi_\alpha(C_3)=\chi_\alpha(C_4)=-1\)
by the [exact certificate](verify_shifted_dyadic.py). \(\square\)

There is also a character \(\chi_5(p)=(\sqrt5\bmod p\,/\,p)\)
on the same primes. Choose a primitive fifth root \(\zeta\)
with \(\zeta+\zeta^{-1}=\alpha^{-1}\) in
\(\overline{\mathbb F}_p\). Then
\(((\zeta-\zeta^{-1})/i)^2=\alpha\sqrt5\).
Frobenius acts on this square root by \(+1\) when
\(p\equiv1\pmod5\) and by \(-1\) when \(p\equiv-1\pmod5\).
Since \(C_j\equiv1\pmod5\), multiplication over its prime
factors gives
\(\prod_{p\mid C_j}\chi_5(p)^{v_p(C_j)}=-1\) as well.

## A square obstruction one layer above the offset valuation

Suppose \(a\ge4\), and let \(p\mid C_{a+1}\) satisfy
\(v_2(p-1)=a+2\) and \(\chi_\alpha(p)=-1\).
Choose the prime above \(p\) at which \(\eta\) has order
\(2^{a+2}\), and let \(h\) be the odd part of the order of
\(\alpha\) there. Then for all odd \(m\) divisible by \(h\),
\(a_{n_0+2^a m}\) is a quadratic nonresidue modulo \(p\) for
each of the three anchors \(n_0\).

Indeed, put \(t=\alpha^{2^a m}\) and \(v=\beta^{2^a m}\)
in \(\mathbb F_p\). Both are fourth roots of unity of order
four. For \(t\), this follows from \(\chi_\alpha(p)=-1\)
and \(h\mid m\). For \(v\), use
\(v=\eta^{2^a m}t^2=-\eta^{2^a m}\).
Writing \(\varepsilon=v/t\in\{1,-1\}\), the Binet expressions
give
\[
 a_{n_0+2^a m}=\frac{t}{\sqrt2}
   \left(\sqrt{10}F_{n_0}+\varepsilon Q_{n_0}\right)
 \quad\text{in }\mathbb F_p.
\]
Here \(t\) and \(-1\) are squares since \(p\equiv1\pmod{16}\).
Moreover \(\sqrt2\beta=2+\sqrt2\) is a square by reduction of
the sixteenth-root identity in
[rational norm descent](coupled-norm-descent.md) §6. Thus
\(\sqrt2\) has the square class of \(\beta\), which is
nonsquare since \(\beta/\alpha^2=\eta\) has full 2-primary order.

For \(n_0=\pm3\), \(F_{n_0}=2\), \(Q_{n_0}=\pm7\), and the
parenthesized expression is \(2\sqrt{10}\pm7\), with square
class \(1\) by the identities
\((\sqrt5\pm\sqrt2)^2=7\pm2\sqrt{10}\).
For \(n_0=-1\), \(F_{n_0}=1\) and \(Q_{n_0}=-1\).
The two values \(\sqrt{10}\pm1\) have the same square class
because their product is \(9\), and
\[
 (\sqrt{10}+1)\alpha\beta
    =\left(\frac{\beta^2+\sqrt5}{2}\right)^2.
\]
Thus the full value has the square class of \(\alpha\)
on the \(-1\) branch and of \(\beta\) on the other two.
Both classes are nonsquare.

For instance, \(p=590232001\) divides \(C_5\), has
\(v_2(p-1)=6\), and has \(\chi_\alpha(p)=-1\). Here
\(a=4\) and the odd part of \(p-1\) is \(9222375\).
The [certificate](verify_shifted_dyadic.py) checks this prime
and the three nonresidues for \(m=9222375\).
For \(a=23\), the prime \(167772161=5\cdot2^{25}+1\)
divides \(C_{24}\). At this prime \(\alpha\) has exact
order \(2^{25}\), so \(h=1\). The proposition excludes
every offset with \(v_2(n-n_0)=23\) on each of the
three branches.

A second direct test treats \(a=20\) on the two branches
\(n_0=\pm3\). Their allowed offsets are divisible by
\(720720\), hence \(11\mid m\). Modulo \(p=230686721\),
the Lucas and Pell matrices both have period dividing
\(44\cdot2^{20}\). The only multiplier residues to check
are therefore \(m=11,33\pmod{44}\). The certificate
checks a nonresidue at both offsets for both anchors.

The uniform application of the one-layer obstruction
requires a prime with the stated valuation at 2 and
with odd order divisor \(h\mid m\) for each candidate.

## The odd part of the mixed residue period

Let \(j\le a\), \(j\ge3\), and \(p\mid C_j\). At the chosen
prime above \(p\), use the definitions of \(t,b,c\) above and
set \(\delta=1\) for \(j<a\), \(\delta=-1\) for \(j=a\).
Since \(m\) is odd, \(\beta^k=\delta t^2\). The square test
is governed by the quadratic character of
\[
 G(t)=\frac{\delta(c t^4+c^{-1})}{2\sqrt2}
      +b t^3-b^{-1}t.
\]
This quartic has an odd-multiplicity root over
\(\overline{\mathbb F}_p\). Otherwise it would be a square
\((\lambda t^2+\mu t+\nu)^2\) over that field. Comparing the
cubic and linear coefficients gives \(\nu/\lambda=-b^{-2}\).
The leading and constant coefficients then give
\(c^{-2}=b^{-4}\), or \(\eta^{n_0}=c/b^2=\pm1\), impossible
because \(\eta\) has order \(2^{j+1}\) and \(n_0\) is odd.
The nonzero constant coefficient shows that every root is
nonzero.

Fix an odd divisor \(D_0\) required to divide \(m\), and let
\(h\) be the odd part of the multiplicative order of \(\alpha\)
in \(\mathbb F_p^\times\). Fixing a compatible residue of \(m\)
modulo the power of 2 in the order of \(\alpha^{2^a}\) fixes
its 2-primary component. As the remaining residue of \(m\)
varies subject to \(D_0\mid m\), the values of \(t\) form a
coset of a subgroup of cardinality \(h/\gcd(h,D_0)\).

For any coset \(J\) of a subgroup of \(\mathbb F_p^\times\),
the classical multiplicative Weil bound gives
\[
 \left|\sum_{t\in J}\left(\frac{G(t)}p\right)\right|\le4\sqrt p.
\]
Indeed, express the coset indicator as the average of the
characters trivial on the subgroup, multiplied by their
values at a representative. With \(\omega\) a character of
order \(p-1\), each complete sum over \(\mathbb F_p^\times\)
has summand \(\omega(t^i G(t)^{(p-1)/2})\) for
\(0\le i<p-1\). At the odd-multiplicity nonzero root,
the multiplicity of this polynomial is nonzero modulo
\(p-1\), so the Weil bound for order \(p-1\) applies.
The polynomial has at most five distinct roots,
including a possible root at zero. If \(i>0\), the term at
zero vanishes. If \(i=0\), at most four roots occur and
removing the term at zero gives the bound \(3\sqrt p+1\).
Both bounds give the displayed estimate.

In particular, if \(h/\gcd(h,D_0)>4\sqrt p\), then for
each fixed 2-primary residue class of the multiplier,
some \(m\) produces \(a_n\) square modulo \(p\).
This constrains a single-prime square-residue obstruction
from either a lower mixed layer or the boundary layer.
It leaves the simultaneous square tests at several primes
as an arithmetic condition on the shared odd residues.

The multiplicative estimate is due to [André Weil, *On Some Exponential Sums*](https://doi.org/10.1073/pnas.34.5.204).

Run \(\texttt{python verify_shifted_dyadic.py}\) from this directory.
