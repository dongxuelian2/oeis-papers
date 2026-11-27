# Coupled norm descent as a finite-support problem

The odd-index norm identities give a coupled system of order and
valuation constraints on the prime factorization of the index.
Section 6 uses the square equation to rule out cancellation at the
primes relevant to a rational norm descent and excludes several index
divisors for every odd square index.

## 1. A general norm-valuation rule

Let \(K\) be a number field, let \(\lambda_1,\ldots,\lambda_j\)
be algebraic units that are not roots of unity, and suppose that at
some positive integer \(n\) one has
\[
 U_n\prod_{i=1}^j(\lambda_i^n-1)^{b_i}
       =N_{K(\sqrt d)/K}(z_n)
\]
with \(U_n\) a unit and \(b_i\) nonnegative integers.
Fix a prime ideal \(\mathfrak p\) over an odd rational prime \(p\)
unramified in \(K\), at which \(d\) is a unit and a quadratic
nonresidue in the residue field. Define
\[
 h_i=\operatorname{ord}_{\mathfrak p}(\lambda_i),\qquad
 e_i=v_{\mathfrak p}(\lambda_i^{h_i}-1),\qquad
 I_i(n)=\mathbf 1_{h_i\mid n}.
\]
Then necessarily
\[
 \boxed{\sum_{i=1}^j b_i I_i(n)
                 (e_i+v_p(n))\equiv0\pmod2.}                 \tag{1}
\]
Here the \(b_i\) may be reduced modulo two.

**Proof.** A norm from the unramified quadratic extension at
\(\mathfrak p\) has even valuation. The order \(h_i\) divides
the size of the residue multiplicative group, so \(p\nmid h_i\).
If \(h_i\nmid n\), the corresponding valuation vanishes.
If \(n=h_i t\), the odd-prime binomial valuation formula in the
unramified local field gives
\[
 v_{\mathfrak p}(\lambda_i^n-1)
 =e_i+v_p(t)=e_i+v_p(n).
\]
Adding the valuations yields (1). The argument uses no
coprimality assumption between the factors.

For two factors, the complete list of necessary rules is:

| Active factors | Consequence |
|---|---|
| Neither | No condition |
| Only the first | \(v_p(n)\equiv e_1\pmod2\) |
| Only the second | \(v_p(n)\equiv e_2\pmod2\) |
| Both | \(e_1\equiv e_2\pmod2\) |

In particular, an odd valuation in an active factor can be
cancelled by the other factor only if its order also divides \(n\)
and its initial valuation has the same parity. When the initial
parities differ, simultaneous activation is forbidden regardless
of the exponent of \(p\) in \(n\).

Equation (1) also couples different norm identities and different
prime ideals above the same rational prime: they all refer to the
same integer \(v_p(n)\). Opposite requirements on its parity
give a contradiction without any bound on \(n\).

## 2. Application to A060405

Retain the notation
\[
 \alpha=(1+\sqrt5)/2,\quad\beta=1+\sqrt2,\quad
 u=\alpha^2,\quad\eta=\beta/u,\quad\xi=\beta u.
\]
For odd \(n\) with \(a_n=x^2\), the identities in
[norm-descent.md](norm-descent.md) give
\[
 \begin{split}
 (L_n+\sqrt2)^2-2\sqrt2\,x^2
   &=-\beta^{-n}(\eta^n-1)(\xi^n-1),\\
 (L_n-\sqrt2)^2+2\sqrt2\,x^2
   &=\beta^{-n}(\eta^n+1)(\xi^n+1).
 \end{split}
\]
Since \(n\) is odd, the second product is also
\(((-\eta)^n-1)((-\xi)^n-1)\).
Consequently (1) applies for each sign \(\sigma\in\{1,-1\}\)
with \(d=\sigma\,2\sqrt2\), \(\lambda_1=\sigma\eta\) and
\(\lambda_2=\sigma\xi\), at every prime ideal of
\(\mathbb Q(\sqrt2,\sqrt5)\) above \(p>5\) where \(d\) is a
quadratic nonresidue. The units multiplying the products
do not affect valuations.

For clarity, all orders and initial valuations are properties of
the fixed algebraic units in the residue field, independent of
the candidate index.

### Finite-support formulation

Write
\[
 n=\prod_{\ell\ {\rm prime}}\ell^{a_\ell},
 \qquad a_\ell\in\mathbb Z_{\ge0},\quad
 a_\ell=0\text{ for all but finitely many }\ell.
\]
The predicate \(h_i\mid n\) is exactly the conjunction of
\(a_\ell\ge v_\ell(h_i)\) over primes dividing \(h_i\).
Equation (1) gives constraints on these threshold predicates
and the parity of \(a_p\).

The earlier anchor reduction and even-index theorem restrict
all square indices to \(n\equiv3,-3,-1\bmod720720\).
In particular
\[
 a_2=a_5=a_7=a_{11}=a_{13}=0,\qquad
 a_3=1\text{ on the two }\pm3\text{ branches},\quad
 a_3=0\text{ on the }-1\text{ branch}.
\]
Thus any positive candidate other than \(3\) on the first two
branches, or \(1\) on the last, has a prime divisor exceeding
13. The value \(n=1\) does not belong to the last branch.

This formulation retains the dependence of the testing primes
on the candidate factorization; it is not a fixed finite
congruence sieve. The full system is necessary for a square
index, not sufficient for squareness.

## 3. Strictly increasing forcing edges

Let \(q>13\) and \(p>5\) be rational primes. Suppose there is
a choice of prime ideal and sign in Section 2 such that:
* one of the two orders is \(q\) and its initial valuation is odd;
* the other order is divisible by at least one of
  \(2,5,7,11,13\).

Then every square index in any of the three odd branches satisfies
\[
 q\mid n\quad\Longrightarrow\quad v_p(n)\equiv1\pmod2,
\]
and hence \(p\mid n\). Indeed, divisibility by \(q\) activates
exactly the first specified factor, since the other order
contains a forbidden prime. Equation (1) gives the assertion.
The same rule works with an order \(3q\) on the two branches
where \(v_3(n)=1\).

For \(p>5\), the residue field degree in the biquadratic field
is at most two. Hence \(q\mid p^2-1\). Since \(p,q\) are odd
and \(q>13\), this implies \(q<p\).
These implications therefore define a directed graph whose
edges strictly increase the rational prime.

**Finite-support escape criterion.** If every prime \(q>13\)
can start an infinite path in this graph (or can be proved
impossible as a prime divisor by another valid constraint),
then all three remaining branches are classified.

**Proof.** A nontrivial candidate contains at least one prime
\(q>13\). Every edge propagates divisibility of the same
integer \(n\). An infinite path forces infinitely many distinct
prime factors of \(n\), a contradiction. A path reaching a
forbidden vertex gives an immediate contradiction. Equivalently,
it suffices to show that no nonempty finite set of allowed
prime divisors can be closed under all valid forcing rules.
For the simpler graph consisting only of the above edges, the
stronger condition that every allowed vertex has at least one
outgoing edge is already sufficient, by taking the largest
prime divisor of a hypothetical candidate.

The escape criterion is a reduction, not a proof of the
outgoing-edge condition. In particular, that condition must
not be assumed from a finite sample of vertices.

## 4. Exact new edges

The attached [verifier](verify_norm_order.py) certifies the
following edges using split primes \(p\), so the residue field
is \(\mathbb F_p\). For each row it specifies a root of 2
and a root of 5 modulo \(p\), their Hensel lifts modulo \(p^2\),
the sign of the norm, both exact multiplicative orders, and the
nonzero unit \((\lambda^q-1)/p\bmod p\) of the active factor.
Euler's criterion checks the required quadratic character.
The nonzero unit certifies initial valuation exactly one.

| Source \(q\) | Target \(p\) | Sign \(\sigma\) | Orders of \(\sigma\eta,\sigma\xi\) |
|---:|---:|---:|:---|
| 29 | 1023991 | + | 170665, 29 |
| 31 | 311 | + | 31, 155 |
| 31 | 30071 | + | 15035, 31 |
| 53 | 6679 | + | 53, 371 |
| 61 | 1831 | + | 61, 915 |
| 61 | 7321 | − | 915, 61 |
| 71 | 569 | + | 142, 71 |
| 73 | 33289 | + | 73, 2774 |
| 97 | 3881 | − | 97, 485 |
| 6679 | 66791 | − | 6679, 33395 |

All ten implications apply on every odd anchor branch.
For example, \(53\mid n\) forces both \(6679\mid n\) and
\(66791\mid n\), each to odd valuation. Also, \(31\mid n\)
forces two distinct new primes \(311,30071\) into \(n\).
It follows, in particular, that no square index on these
branches can have largest prime factor in
\(\{29,31,53,61,71,73,97,6679\}\). These exclusions have no
upper bound on the index.

## 5. Three provable terminal vertices: why composite activation is needed

The simple outgoing-edge conjecture of Section 3 is false for these
two mixed-unit norms. It can be tested exhaustively for specific
source primes without a bound on the witness prime.

For any odd positive integer \(s\), the four Galois conjugates
of \(\eta\) are \(\eta,\xi,-\xi^{-1},-\eta^{-1}\). Therefore
\[
 \begin{aligned}
 N_{K/\mathbb Q}(\eta^s-1)
 &= (\eta^s-\eta^{-s})(\xi^s-\xi^{-s})\\
 &= (\beta^s-\beta^{-s})^2-(u^s-u^{-s})^2\\
 &= 4Q_s^2-5F_{2s}^2.
 \end{aligned}
\]
The same norm is obtained for \(\xi,-\eta,-\xi\) in place
of \(\eta\): swapping \(\eta,\xi\) is Galois conjugation,
and negation is conjugation followed by inversion of a unit
whose rational norm is one.

For \(q=17,19,23\) respectively the negative of this norm is
the rational prime in the following table.

| \(q\) | Unique possible witness prime \(p\) |
|---:|---:|
| 17 | 152278105612081 |
| 19 | 7288288224767761 |
| 23 | 16454995746349728961 |

The [exact certificate](verify_norm_graph_limits.py) proves
primality by giving the complete factorization of \(p-1\) and
an element of order \(p-1\) modulo each prime divisor of \(p\).
It also verifies that \(p\equiv1\bmod4\) and exhibits square
roots of 2, 5 and \(2\sqrt2\) for a chosen root of 2 modulo \(p\).
The first two roots imply complete splitting in \(K\).
Since \(-1\) is a square, both signs of \(2\sqrt2\) are squares
at every prime of \(K\) above \(p\).

An order \(q\) at any prime ideal would make that prime divide
one of the four algebraic numbers \(\lambda^q-1\), so its rational
prime must be the sole prime in the table. At that prime the
necessary quadratic nonresidue condition fails. Hence none of
these three vertices has an outgoing edge in the simple graph,
even with arbitrarily large witness primes. In fact no order
\(q\) at such a vertex can activate a bad-prime constraint from
these two norm identities at all.

This is an obstruction to the single-prime escape criterion,
not to the full coupled system. A composite divisor \(s\mid n\)
can activate an order which is not activated by any of its
prime factors separately. A rule can also combine the two
orders with parity requirements on the same rational prime.
A more general escape theorem should therefore concern finite
sets of prime-exponent thresholds, not just individual prime
vertices. The \(\pm3\) branches may in particular activate orders
\(3q\), which were not included in this terminal-vertex theorem.

## 6. Rational norm descent at primes congruent to 7 or 9 modulo 16

For positive odd \(s\), put
\[
 M_s=\left|N_{K/\mathbb Q}(\eta^s-1)\right|=5F_{2s}^2-4Q_s^2.
\]
The sign follows from \(0<\eta<1<\xi\) and the conjugates in Section 5.

**Theorem.** If \(n\) is a positive odd square index, then for
every divisor \(s\mid n\) and every prime \(p\equiv7,9\pmod{16}\),
the valuation \(v_p(M_s)\) is even. Every such prime dividing
\(M_s\) splits in \(\mathbb Q(\sqrt3,\sqrt5)\).

**Character of the odd part.** Every odd prime divisor of \(M_s\)
splits in \(\mathbb Q(\sqrt2)\). Suppose 2 is a nonsquare modulo \(p\)
and reduce in \(\mathbb F_{p^2}\) at a prime ideal dividing
\(\eta^s-1\). Then
\(\beta^s=u^s\) and \(\beta^{p+1}=-1\). If 5 is a nonsquare modulo
\(p\), then \(u^{p+1}=1\), contradicting that \(s\) is odd.
If 5 is a square or \(p=5\), then \(u\) is a square in
\(\mathbb F_p\), so \(u^{p+1}=u^2\) and
\((u^s)^2=(\beta^s)^{p+1}=-1\).
A square of order four in \(\mathbb F_p^\times\) requires
\(8\mid p-1\), whereas \(p\equiv3,5\pmod8\).

On \(\{1,7,9,15\}\subset(\mathbb Z/16\mathbb Z)^\times\)
let \(\chi\) take value \(+1\) at \(1,15\) and \(-1\) at \(7,9\).
The Fibonacci state modulo 8 repeats after 12 steps and the
companion Pell state after four steps. For odd \(s\), they give
\(Q_s^2\equiv1\pmod{16}\) and \(F_{2s}\equiv\pm1\pmod8\) when
\(3\nmid s\), or \(8\mid F_{2s}\) when \(3\mid s\).
Thus \(M_s\equiv1\pmod{16}\) when \(3\nmid s\), and
\(v_2(M_s)=2\) with \(M_s/4\equiv15\pmod{16}\) when \(3\mid s\).
The odd part of \(M_s\) has character \(+1\).

**Uniqueness over each prime of character \(-1\).** Let
\(p\equiv7,9\pmod{16}\) divide \(M_n\) for an odd square index \(n\).
Then \(p\ge7\) and \((2/p)=1\).
For either root \(r\) of 2 in \(\mathbb F_p\), the element \(2+r\)
is a nonsquare. Choose a primitive sixteenth root \(z\) with
\(r=z^2+z^{-2}\). The square root \(z+z^{-1}\) of \(2+r\)
belongs to \(\mathbb F_p\) precisely when Frobenius sends \(z\)
to \(z\) or \(z^{-1}\), equivalently \(p\equiv\pm1\pmod{16}\).

Suppose 5 is a nonsquare modulo \(p\). At a prime ideal
dividing \(\eta^n-1\) one has \(\beta^n=u^n\in\mathbb F_p\).
As \(u^{p+1}=1\), one gets \(u^n=\pm1\).
For \(p\equiv7\pmod{16}\), the relation
\(u^{(p+1)/2}=\alpha^{p+1}=-1\) gives
\(v_2(\operatorname{ord}(u))=v_2(p+1)\ge3\), which precludes
\(u^n=\pm1\) at odd \(n\).
For \(p\equiv9\pmod{16}\), both values of \(\beta^n=\pm1\) are
squares in \(\mathbb F_p\), so \(\beta\) is a square there.
Since \(\sqrt2\beta=2+\sqrt2\), the twist \(2\sqrt2\) is a
nonsquare in \(\mathbb F_p\). The positive-sign identity of Section 2
lies in \(\mathbb Q(\sqrt2)\) and then forces \(L_n+\sqrt2=0\)
in \(\mathbb F_p\). This gives \(L_n^2=2\), whereas \(u^n=\pm1\)
gives \(L_n^2=(\alpha^n-\alpha^{-n})^2\in\{0,-4\}\).
Hence \(p\) splits completely in \(K\).

Work in one of the residue fields \(\mathbb F_p\).
If \(\eta^n=\sigma\) or \(\xi^n=\sigma\) for \(\sigma\in\{1,-1\}\),
then \(\beta^n=\sigma u^n\) or \(\beta^n=\sigma u^{-n}\),
respectively. Thus \(\sigma\beta\) is a square in \(\mathbb F_p\)
and the twist \(\sigma\,2\sqrt2\) has the square class of
\(2\sqrt2\beta=2(2+\sqrt2)\), a nonsquare.
The corresponding identity in Section 2 forces
\(L_n+\sigma\sqrt2=0\).
If both \(\eta^n,\xi^n\) equal the same \(\sigma\), then
\(u^n=\pm1\), again giving \(L_n^2\in\{0,-4\}\) instead of 2.
If they equal opposite signs, one gets both
\(L_n+\sqrt2=0\) and \(L_n-\sqrt2=0\).
Thus at most one of \(\eta^n,\xi^n\) belongs to \(\{1,-1\}\).
The conjugate list in Section 5 shows that exactly one prime
ideal above \(p\) divides \(\eta^n-1\). At this ideal the
positive-sign norm is nonzero and has a unit partner. Its
nonsquare twist forces \(v_p(M_n)\) to be even. Also, \(w=\alpha^n\) satisfies
\(w^2+\sqrt2w-1=0\) in \(\mathbb F_p\), by \(L_n+\sqrt2=0\).
Its discriminant is 6, so \(p\) splits in \(\mathbb Q(\sqrt3)\).
By divisibility, the same splitting condition holds at each
prime of character \(-1\) dividing any \(M_s\) with \(s\mid n\).

**Descent.** Suppose \(p\equiv7,9\pmod{16}\) has odd valuation
in \(M_s\) for a divisor \(s\mid n\). Since \(\eta^s-1\) divides
\(\eta^n-1\), uniqueness applies at \(p\). The binomial valuation
formula gives \(v_p(M_n)=v_p(M_s)+v_p(n/s)\), so \(sp\mid n\).
The positive integer \(M_{sp}/M_s\) has odd-part character \(+1\)
and valuation one at \(p\). It has a prime divisor \(q\ne p\)
of character \(-1\) and odd valuation. By uniqueness, \(q\)
splits completely and the unique ideal above \(q\) dividing
\(\eta^{sp}-1\) is new at \(sp\), since multiplying the index
by \(p\) preserves the valuations at old ideals above \(q\).
Thus \(v_q(M_s)=0\), and \(\eta^s\) has exact order \(p\) in
\(\mathbb F_q^\times\). Hence \(q>p\) and
\(v_q(M_{sp})=v_q(M_{sp}/M_s)\) is odd. Iterating from \((sp,q)\)
forces infinitely many distinct primes to divide \(n\). \(\square\)

### Consequences and remaining arithmetic target

The witnesses in Section 4 have odd valuation at primes
\(p\equiv7,9\pmod{16}\). Through the conjugate list in Section 5
and uniqueness above, each such valuation equals \(v_p(M_s)\)
when \(s\mid n\) and \(n\) is an odd square index.
Consequently each of
\[
 29,\ 31,\ 53,\ 61,\ 71,\ 73,\ 97,\ 6679
\]
is excluded as a divisor of \(n\).
The [witness at 51511](unified-norm-classification.md) for
\(s=51\) also excludes \(17\mid n\) when \(n\equiv\pm3\pmod{720720}\).

A sufficient global target is to exhibit, for each remaining
candidate \(n>10^{902}\), a divisor \(s\mid n\) and a prime
\(p\equiv7,9\pmod{16}\) dividing \(M_s\) that has odd valuation
or is inert in \(\mathbb Q(\sqrt3)\) or \(\mathbb Q(\sqrt5)\).
The examples \(M_{17},M_{19},M_{23}\) in Section 5 give prime
indices \(s\) at which a witness must come from another divisor
of the candidate or from another norm identity.

## 7. Joint rational and Gaussian divisor tests

The [Gaussian descent](norm-descent.md#2-a-gaussian-factorization-for-the-odd-indices)
forces even valuations at the relevant Gaussian primes for every
divisor of \(n\pm2\) on the three odd anchor classes. The total
Gaussian character is \(+1\) for divisors coprime to 3. For
\(3\mid s\mid n-2\) on the \(-1\) branch, the quotient
has \(\chi_-(R_s/R_3)=\left(\frac{s/3}{5}\right)=1\).
The terminal inputs \(17,19,23\) of the rational norm test are
each detected when used as an index in the Gaussian tests:
\(n=17\) has \(s=19\mid n+2\), \(n=19\) has \(s=17\mid n-2\),
and \(n=23\) has \(s=21\mid n-2\).

**Conditional compatibility on the zero-anchor branch.**
Suppose \(n\equiv-1\pmod{720720}\) is a positive prime, and set
\(t=(n-2)/3\), \(z=n+2\). If all six integers
\[
 t,\quad z,\quad M_n,\quad P_t,\quad P_z,\quad
 \frac{8P_t^2-3}{5}
\]
are prime, the rational norm test of Section 6 and both Gaussian
divisor tests admit \(n\).

Indeed, \(M_n\equiv1\pmod{16}\) and \(M_1=1\), so the divisors
of \(n\) satisfy the rational norm condition. Since \(z\ne3\)
and \(N(R_z)=P_z\) is prime, the factor of \(R_z\) has
character \(\chi_+(R_z)=1\). On the other side
\(t\equiv-1\pmod{15}\). The factors \(R_3\) and \(R_t\) divide
\(R_{3t}\) and are coprime, since \(N(R_3)=5\) and \(5\nmid P_t\).
For odd \(t\), the identity \(P_{3t}=P_t(8P_t^2-3)\)
gives the prime norm \((8P_t^2-3)/5\) for
\(R_{3t}/(R_3 R_t)\). The two factors \(R_t\) and
\(R_{3t}/(R_3 R_t)\) each have prime norm and
character \(\chi_-=1\), by (6) and (8) of the Gaussian descent.
The factor \(R_3\) has character zero. The divisors \(1,3,t,3t\)
of \(n-2\) therefore satisfy the valuation tests.
This criterion specifies a primality pattern
under which the three divisor tests agree.

## 8. A tangent norm at the zero anchor

The following norm identity has a factor indexed by
\((n+1)/2\), the offset from the zero anchor divided by two.
It gives a variable-prime condition for those offsets.

Write \(n=2j+1\), \(k=j+1\), \(s=\sqrt2\), and set
\[
 \theta=\frac{2+s}{8},\quad d=2-s,\quad
 b=4\theta,\quad h=d-1,\quad \gamma=\frac34+\theta.
\]
Define, over \(\mathbb Q(\sqrt2)\),
\[
 \begin{aligned}
 g&=L_j+F_j=2F_k,\\
 \ell&=(2\theta-1)(L_k-2Q_k)+\frac52F_k-P_k,\\
 z_2&=2F_j+\frac{d}{h^2}(\ell-2\gamma g).
 \end{aligned}
\]

**Proposition.** For every odd \(n\),
\[
 a_n-5d\left(\frac{3\beta}{4s}g\right)^2=\ell z_2.
 \tag{9}
\]
If \(n\ge1\) is a square index and the residue characteristic
of a prime ideal \(\mathfrak p\) is greater than 5, then
at every \(\mathfrak p\) where \(5d\) is a quadratic
nonresidue, \(\ell\) and \(z_2\) have even valuations.
Consequently a single odd valuation of \(\ell\) at such
a prime excludes the candidate.
On the zero-anchor branch \(k\) is even. If
\(\mathfrak p\mid\ell\) at one of these prime ideals, its
rational prime divides \(F_k\). Reducing the units at any
prime above \(\mathfrak p\) in \(K\) gives
\[
  \alpha^k=\varepsilon,\qquad
  \beta^k\in\{\varepsilon,-\varepsilon\beta\},
  \qquad \varepsilon\in\{1,-1\}.
 \tag{10}
\]
In particular the rational prime divides
\(\gcd(F_k,P_k Q_{k-1})\).

**Proof.** Suppress the index \(j\) on \(L,F,P,Q\).
Addition gives \(a_{2j+1}=L_jL_{j+1}+2P_jQ_{j+1}\), since
the constants from \(L_j L_{j+1}=L_{2j+1}+(-1)^j\) and
\(2P_jQ_{j+1}=P_{2j+1}-(-1)^j\) cancel. Expanding the two
next terms gives
\[
 a_{2j+1}=\tfrac12L^2+\tfrac52LF+4P^2+2PQ.
\]
Subtract \(\theta(L^2-5F^2)\) and add
\(4\theta(Q^2-2P^2)\). These changes cancel by the
Lucas and Pell norm identities. The result is the
ternary quadratic form
\[
 (\tfrac12-\theta)L^2+\tfrac52 LF+5\theta F^2+dZ^2,
 \qquad Z=bQ+P,
\]
using \(db=1\) and \(4-8\theta=d\).

The state at \(j=-1\) has \(L=-1,F=1,Z=1-b\)
and is isotropic for this form. Substitute
\(L=g-F\) and \(Z=z+(1-b)F\). The \(F^2\) term drops out,
and the form becomes
\[
 (\tfrac12-\theta)g^2+dz^2+2F(\gamma g+h z).
\]
Using \(F_{k-1}=(L_k-F_k)/2\),
\(P_{k-1}=Q_k-P_k\), and \(Q_{k-1}=2P_k-Q_k\)
shows that \(\gamma g+h z=\ell\) as defined above.
Substituting \(z=(\ell-\gamma g)/h\) gives
\[
 a_{2j+1}=\left(\tfrac12-\theta+\frac{d\gamma^2}{h^2}\right)g^2
           +\ell \left(2F+\frac d{h^2}(\ell-2\gamma g)\right).
\]
Here \(h=-\beta^{-1}\) and
\(\tfrac12-\theta+d\gamma^2/h^2=45d\beta^2/32\).
This proves (9).

For a square index the right side of (9) is the norm
of \(x+(3\beta g/(4s))\sqrt{5d}\) from the quadratic
extension. The element \(5d\) is nonsquare in
\(\mathbb Q(\sqrt2)\), because it has valuation one
at the prime above 5. Both factors are nonzero at a
positive square value. The quantities \(\ell,z_2,3\beta g/(4s)\)
are integral at the stated primes and \(3\beta/(4s)\) is a unit.
At these prime ideals the
norm has even valuation by reduction of the two squares
after removing their common prime power.
If both factors vanished modulo \(\mathfrak p\), (9)
and the nonsquare twist would force \(g=0\) there.
Then \(z_2=0\) gives \(F=0\), and \(g=0\) gives \(L=0\),
contradicting \(L^2-5F^2=4(-1)^j\) modulo \(\mathfrak p\).
Thus at least one of the two valuations is zero, and both are even.

If \(\mathfrak p\mid\ell\), the same nonsquare condition
forces \(g=0\) in the residue field, hence \(F_k=0\).
For even \(k\) this gives \(\alpha^k=\varepsilon\) and
\(L_k=2\varepsilon\). Put \(W=\beta^k\).
Since \(Q_k=(W+W^{-1})/2\) and
\(P_k=(W-W^{-1})/(2s)\), the equation \(\ell=0\) becomes
\[
 d(W-\varepsilon)^2=s(W-\varepsilon)(W+\varepsilon).
\]
The alternatives are \(W=\varepsilon\) and
\(W=\varepsilon(d+s)/(d-s)=-\varepsilon\beta\).
The first gives \(P_k=0\), and the second gives
\(\beta^{k-1}=-\varepsilon\) and \(Q_{k-1}=0\).
This proves (10). \(\square\)

**Ramified places of the tangent norm.** Suppose \(n\ge0\),
\(n\equiv-1\pmod{720720}\), \(v_2(n+1)\ge14\), and \(a_n\)
is a local square at 2 and 5. Then \(\ell\) is a square in
\(\mathbb Q_2(\sqrt2)\) and is a local norm at 5 for the
quadratic twist \(5d\). Consequently the product of the
quadratic norm characters of \(\ell\) over the unramified
odd places is \(+1\).

For 2, write \(k=2^v m\) with \(m\) odd. Then \(3\mid m\),
and the local square condition gives \(m\equiv3\pmod8\)
by the [exact dyadic valuation](shifted-dyadic-descent.md).
Doubling in the two recurrences gives, for \(v\ge2\),
\[
 L_k\equiv2\pmod {2^{2v+2}},\quad
 v_2(Q_k-1)=2v,\quad
 \frac{F_k}{2^{v+2}}\equiv-m\pmod4,\quad
 \frac{P_k}{2^v}\equiv3m\pmod8.
\]
For the Lucas congruences, \(L_{2m}=L_m^2+2\),
\(4\mid L_m\), and \(L_{2j}-2=(L_j-2)(L_j+2)\)
at even \(j\). The doubling formula \(F_{2j}=F_j L_j\)
starts from \(F_{2m}/8\equiv-m\pmod4\), checked on
\(m=3,9,15,21\bmod24\) using the Fibonacci period modulo 32.
For the Pell congruences, \(Q_{2m}=2Q_m^2+1\equiv3\pmod8\),
\(Q_{2j}-1=2(Q_j-1)(Q_j+1)\) at even \(j\), and
\(P_{2j}=2P_jQ_j\). The formula for \(P_k\) starts from
\(P_{4m}/4\equiv3m\pmod8\), checked on \(m=1,3,5,7\bmod8\)
using the Pell period modulo 32.
The rational part \(((5/2)F_k-P_k)/2^v\) is congruent to
\(3m\equiv1\pmod8\). The remaining part of \(\ell/2^v\)
is \(-d(L_k-2Q_k)/(4\cdot2^v)\), of valuation \(2v-1\)
in \(\mathbb Q_2(\sqrt2)\) with uniformizer \(\sqrt2\).
The rational part is a square in \(\mathbb Q_2\), and a relative
perturbation of valuation greater than 4 preserves its square
class by Hensel's lemma. Also \(2^v\) is a square in
\(\mathbb Q_2(\sqrt2)\).

For 5, write \(k=60h\), put \(w=v_5(h)\), and write
\(h_0=h/5^w\). The sequence values at 60 give
\[
 5F_{60}-2P_{60}\equiv375,\qquad L_{60}-2\equiv500
 \pmod{625}.
\]
Use \(v_5(\log\alpha^{60})=3/2\) and
\(v_5(\log\beta^{60})\ge2\) in the corresponding quadratic
extensions of \(\mathbb Q_5\). These valuations follow by
taking fifth powers of \(\alpha^{12}=161+72\sqrt5\) and
\(\beta^{12}=19601+13860\sqrt2\). In the differences
of the two exponential series for \(F_{60h}\) and \(P_{60h}\),
all terms after the linear one have degree at least three.
In the sums for \(L_{60h}-2\) and \(Q_{60h}-1\), the first
term has degree two and all later terms have degree at least
four. The bound \(v_5(j!)\le j/4\) then gives
\[
 \frac{5F_k-2P_k}{5^{w+3}}\equiv3h_0,\qquad
 \frac{L_k-2Q_k}{5^{2w+3}}\equiv4h_0^2\pmod5.
\]
Thus for \(w\ge1\), \(v_5(\ell)=w+3\) and its unit is
rational modulo 5. For \(w=0\), the local square condition
on \(a_n\) requires \(h\equiv1\pmod5\), since
\(h=6006(n+1)/720720\). The unit of \(\ell\) is then
\(4-d=2+\sqrt2\) after dividing by \(5^3\).
At the prime above 5, the ramified quadratic norm character
of \(5^e u\) for \(5d\) is the quadratic character of
\(u(-d)^e\) in \(\mathbb F_{25}\).
Both \(d\) and \(2+\sqrt2\) have norm 2 to \(\mathbb F_5\)
and are nonsquares. When \(w=0\) the two characters cancel.
When \(w\ge1\), the [local square condition](local-geometry.md#2-two-simple-5-adic-roots)
requires \(w\) odd, so \(e=w+3\) is even and the rational
unit is a square in \(\mathbb F_{25}\).
This proves the local norm condition at 5. The twist \(5d\)
is positive at both real embeddings, so the product assertion
follows from Hilbert reciprocity.
[Milne, *Class Field Theory*, Chapters III and V](https://www.jmilne.org/math/CourseNotes/CFT.pdf)

**Tangent witness on the zero-anchor branch.** Let \(D_{-1}\)
be the extended forced divisor, with \(v_2(D_{-1})=14\).
Let \(H\) be the least common
multiple of the odd part of \(D_{-1}\) and the odd parts of
\(1,\ldots,1000001\), and put \(S=2^{202}H\). Choose
\(c\) with \(cH\equiv1\pmod8\). The congruences
\[
 n\equiv-1+3cS\pmod {8S},\qquad
 n\equiv2717483\pmod{4q},\qquad q=1002899
\]
give infinitely many positive indices with \(D_{-1}\mid n+1\),
\(v_2(n+1)=202\), and \((n+1)/2^{202}\equiv3\pmod8\).
Indeed \(q\) is prime, every odd prime factor of \(D_{-1}\) is below
30000 by the two lifting certificates, and both residues are
\(-1\bmod4\).
The index agrees with \(-1\) modulo the matrix periods at
each prime at most \(10^6\), so \(a_n\) is zero modulo all
of them.

The prime \(p=2q+1=2005799\) splits in \(K\), as
\((2/p)=1\) and \(p\equiv4\bmod5\). Thus both matrix periods
divide \(p-1\). Take the prime specified by
\(\sqrt2\equiv938842\pmod p\).
The certificate gives \(\ell\equiv0\), \(F_k\ne0\), and
\(5d\) a nonresidue there for \(k\equiv1358742\pmod{p-1}\),
the class imposed by \(n\bmod4q\). This contradicts (10)
for every index in the progression.

**Splitting and the companion phase.** The extension
\(\mathbb Q(\sqrt2,\sqrt{5d})/\mathbb Q\) is the twist of
\(\mathbb Q(\zeta_{16})^+\) by the quadratic character of
\(\mathbb Q(\sqrt5)\). In detail, \(\sqrt d\) also generates
the real cyclotomic extension over \(\mathbb Q(\sqrt2)\),
since \(d(2+s)=2\). Take a quartic cyclotomic character
\(\psi\) modulo 16 with square \((2/\,\cdot\,)\). In the
compositum with \(\mathbb Q(\sqrt5)\), the character
\(\psi(5/\,\cdot\,)\) cuts out the field generated by
\(\sqrt{5d}\) and \(s\): the kernel fixes \(s\), and on its
stabilizer the action on \(\sqrt{5d}\) is the product of
the two actions on \(\sqrt d\) and \(\sqrt5\).
Thus for \(p>5\) the twist is nonsquare at the primes over \(p\)
if \(p\) is inert in \(\mathbb Q(\sqrt2)\), or if \(p\) belongs
to one of the two split classes
\[
 \big(p\bmod16,(5/p)\big)\in
 \big(\{1,15\}\times\{-1\}\big)
 \ \cup\
 \big(\{7,9\}\times\{+1\}\big).
\]
For inert \(p\), the Frobenius for the quadratic extension
over \(\mathbb Q(\sqrt2)\) is the square of an order-four element.
For split \(p\) its character is \(\psi(p)(5/p)\).

When \(n\) is a square index on the zero-anchor branch, a
nonsplit prime dividing \(z_2\) also forces \(F_k=0\) modulo \(p\).
With \(W=\beta^k\) and \(\alpha^k=\varepsilon=\pm1\), one has
\(2F_{k-1}=2\varepsilon\) and \(d/h^2=2+s\).
Thus \(z_2=0\) gives \(\ell=-d\varepsilon\) in the residue field.
The equation for \(4W(\ell+d\varepsilon)\) is
\[
 0=(W+\varepsilon)\big(d(W+\varepsilon)-s(W-\varepsilon)\big).
\]
It gives \(W=-\varepsilon\) or \(W=\varepsilon\beta\).
Thus a nonsplit prime of either factor divides
\(\gcd(F_k,P_kQ_{k-1})\).
The \(Q_{k-1}\) phases require \(p\) to split in \(\mathbb Q(\sqrt2)\),
since \(2P_{k-1}^2\equiv1\pmod p\).
Under conjugation of \(\sqrt2\), \(W\) becomes \(W^{-1}\), and
the phase \(W=-\varepsilon\beta\) for \(\ell\) becomes the
companion phase \(W=\varepsilon\beta\) at the conjugate prime.

## 9. A dual norm of the Lucas term

Write \(T_n=2L_n^2-1\) for odd \(n\). The Pell norm identity
gives a rational norm form of the
[dual splitting-curve identity](unified-norm-classification.md#1-complete-classification-of-monomial-splitting-curves):
\[
 (\beta^n+\sqrt2 L_n)^2-2\sqrt2\,\beta^n a_n=T_n.
 \tag{11}
\]
Indeed the first square is \((Q_n+\sqrt2 a_n)^2\), and
subtracting the second term gives
\(Q_n^2+2a_n^2-4P_na_n=2L_n^2-1\).
If \(a_n=x^2\), equation (11) represents \(T_n\) as the norm
of
\[
 Q_n+\sqrt2 x^2+\sqrt2\,x\beta^{(n-1)/2}\sqrt{2+\sqrt2}
\]
from \(\mathbb Q(\zeta_{16})^+\) to \(\mathbb Q(\sqrt2)\), where
the superscript \(+\) denotes the maximal real subfield.

**Prime-factor test.** Every prime \(p\mid T_n\) splits in
\(K=\mathbb Q(\sqrt2,\sqrt5)\). If \(n\) is a square index, then
\[
 p\equiv7,9\pmod {16},\quad p\mid T_n
 \quad\Longrightarrow\quad v_p(T_n)\equiv0\pmod2.
 \tag{12}
\]
In fact \(T_n=10F_n^2-9\) is coprime to 30. Its congruences
\(2L_n^2\equiv1\) and \(10F_n^2\equiv9\pmod p\) give the
splitting in \(K\). At either prime of \(\mathbb Q(\sqrt2)\)
above \(p\), \(2+\sqrt2\) is a nonresidue precisely for
\(p\equiv7,9\pmod {16}\), by the action of Frobenius on
\(\zeta_{16}+\zeta_{16}^{-1}\). A norm from this unramified
quadratic extension has even valuation. This applies also if
\(p\mid x\). For example, \(T_{13}=41\cdot13241\) has
\(v_{41}(T_{13})=1\), while \(T_7=41^2\) passes (12).

**Transfer to the mixed field.** The factors
\(\alpha^n-\sqrt2\) and \(\alpha^n+\sqrt2\) have relative norms
\(1-\sqrt2 L_n\) and \(1+\sqrt2 L_n\) to \(\mathbb Q(\sqrt2)\).
Their absolute norms are both \(-T_n\). For each prime \(p\mid T_n\)
there is exactly one prime of \(K\) above \(p\) dividing
\(\alpha^n-\sqrt2\). In fact the two choices of \(\alpha^n\) at
\(p\) are \(u\) and \(-u^{-1}\), and precisely one has square 2,
since \(2\ne2^{-1}\pmod p\). The sign of \(\sqrt2\) then specifies
the prime uniquely. Its valuation is \(v_p(T_n)\).
At this prime the quadratic characters of \(\alpha\) and
\(\sqrt2\) coincide, since \(n\) is odd. When \(p\equiv\pm1\pmod {16}\),
the character of \(\beta\) also agrees, by
\(\sqrt2\,\beta=2+\sqrt2\).

The dyadic norm character of \(\alpha^n-\sqrt2\) for
\(K\mathbb Q(\zeta_{16})^+/K\) is determined by the local norm
\(N_{K/\mathbb Q}(\alpha^n-\sqrt2)=-T_n\), by compatibility of
local reciprocity with norms. Here \(K\) has a single place above
2: adjoining \(\sqrt5\) is unramified quadratic at 2, and adjoining
\(\sqrt2\) is ramified quadratic. The real cyclotomic field has
totally ramified dyadic completion, whose intersection with the
completion of \(K\) is \(\mathbb Q_2(\sqrt2)\).
The character is trivial exactly
when \(T_n\equiv\pm1\pmod {16}\), by the cyclotomic character of
conductor 16 on odd units. For every odd \(n\), the Lucas
recurrence modulo 4 gives either \(L_n\) odd or \(4\mid L_n\).
Thus \(T_n\equiv1\) or \(-1\pmod{16}\), respectively.
The total multiplicity of primes in (12) is therefore even
for every odd \(n\).
[Milne, *Class Field Theory*, Chapters I and V](https://www.jmilne.org/math/CourseNotes/CFT.pdf)

**Relation to the Gaussian fibration.** The corresponding Lucas
square completion is
\[
 (a_n+\sqrt5 F_n)^2-4\alpha^n a_n=P_n^2+4=P_{n-2}P_{n+2}.
 \tag{13}
\]
The first equality follows from \(\sqrt5 F_n=2\alpha^n-L_n\)
and \(\alpha^n(\alpha^n-L_n)=1\).
If \(a_n=x^2\), equation (13) is a norm from
\(\mathbb Q(\sqrt5,\sqrt\alpha)\) to \(\mathbb Q(\sqrt5)\).
At a common prime divisor \(p\) of the two right sides, \(p\) splits
in \(K(i)\), since \(P_n^2\equiv-4\pmod p\). If \(a_n=x^2\) and both
right sides have odd valuation at \(p\), the two norm equations require
\(p\equiv1\pmod {16}\) and \(\alpha\) to be a square modulo either
prime of \(\mathbb Q(\sqrt5)\) above \(p\). These conditions follow
separately from the two norm equations.

The two separate norm-membership tests over their respective
base fields are equivalent to their odd-prime parity tests.
Indeed, both quadratic extensions are unramified at odd finite
places: for (11) this follows from the cyclotomic conductor,
and for (13) from the fact that \(\alpha\) is a unit. At every
real place each right side is positive and is a local norm.
Each base field has only one dyadic place. Once all the other
local norm characters are trivial, Hilbert reciprocity makes the
dyadic character trivial there as well. The quadratic local-global
norm theorem then gives the two independent norm representations.
Equations (11) and (13) with their prescribed coordinates in
terms of a common \(x\) impose the original square equation.
[Milne, *Class Field Theory*, Chapter VIII, Theorem 3.1](https://www.jmilne.org/math/CourseNotes/CFT.pdf)

The independent memberships also allow nonsquare values
when the Gaussian norm from Section 2 of [the norm descent](norm-descent.md#2-a-gaussian-factorization-for-the-odd-indices)
is used in place of (13). For instance \(n=5\) has \(a_5=40\) and
the two representations
\[
 \begin{aligned}
 241&=(7-16\sqrt2)^2-(2+\sqrt2)(16-12\sqrt2)^2,\\
 29-2i&=(7+4i)^2-(1+2i)(5+i)^2.
 \end{aligned}
\]
On the three remaining branches, let \(n\) satisfy the local
square conditions at 2 and 5. The separate Gaussian and dual
norm memberships then hold exactly when their parity tests
hold at every odd place of residue characteristic other than 5.
Indeed the local square roots yield the prescribed norm
representations at 2 and 5, including both Gaussian primes
above 5. All other finite places are unramified for the
respective quadratic extensions. The
Gaussian base field has a complex infinite place, and the
dual right side is positive. Again the quadratic local-global
norm theorem gives the independent memberships.

There is also a factorization difference. For every odd \(b>1\),
\(X^b-2\) is irreducible over \(K\). At the dyadic prime of \(K\),
every root has valuation \(2/b\) in the normalization in which
2 has valuation 2. The constant term of a degree-\(d\) monic factor
would have integral valuation \(2d/b\), forcing \(b\mid d\).
Thus for \(n=sb\) the polynomial in \(\alpha^{2s}\) that gives
\(\alpha^{2n}-2\) stays irreducible over the mixed field.

**Witness beyond the extended sieve.** Let \(D_3\) be the forced
divisor for the anchor \(3\) from the [extended certificate](extended-lifting.md),
with \(v_2(D_3)=14\).
Let \(H\) be the least common multiple of the odd part of \(D_3\)
and the odd parts of \(1,\ldots,1000001\). Put \(S=2^{201}H\).
Take \(p=2002919\), with \(p-1=2q\) for the prime \(q=1001459\).
The two congruences
\[
 n\equiv3+S\pmod {2S},\qquad n\equiv1413907\pmod {p(p-1)}
\]
have infinitely many positive solutions by the Chinese remainder
theorem. The two moduli have gcd 2, since all odd prime factors
of \(D_3\) are at most 2000 by the lifting cap, and the two residues
are odd. Every solution has \(D_3\mid n-3\), \(v_2(n-3)=201\),
and \(a_n\equiv9\pmod t\) for every prime \(t\le10^6\).
For \(t>5\) each matrix period divides one of \(t-1\) and
\(2(t+1)\), both of which divide \(S\). For \(t=2,3,5\) the
periods divide the base modulus \(720720\), which also divides \(S\).

Here \(p\equiv4\pmod5\), so the Lucas characteristic polynomial
splits into distinct roots modulo \(p^2\) by Hensel's lemma.
The Lucas matrix \(A\) satisfies \(A^{p(p-1)}=I\bmod p^2\).
At the displayed residue the certificate gives
\(T_n\equiv108083p\bmod p^2\). Thus every solution has
\(v_p(T_n)=1\), and (12) excludes it since \(p\equiv7\pmod {16}\).

## 10. The Gaussian tangent norm at the zero anchor

Write \(n=2k-1\), and put
\[
 X=5F_k-2P_k,\qquad Y=L_k-2Q_k,\qquad
 D=1+2i,\qquad
 \widetilde\ell=DY-X,\qquad
 \widetilde z=P_k-DQ_k-\widetilde\ell/4.
\]
Then
\[
 D a_{2k-1}-9P_k^2=\widetilde\ell\,\widetilde z.
 \tag{14}
\]
This identity uses the same two differences \(X,Y\) as the
tangent norm in Section 8. An addition formula with rational
coefficients is
\[
 a_{2k-1}=5F_kF_{k-1}+2P_kQ_{k-1}.
 \tag{15}
\]
Indeed the two terms are \(L_{2k-1}+(-1)^k\) and
\(P_{2k-1}-(-1)^k\), respectively. Write \(P=P_k,Q=Q_k\).
The equality of the Lucas and scaled Pell norm identities gives
\[
 Y^2+4QY=(X+2P)^2/5-8P^2 .
\]
Substitute \(F_{k-1}=(L_k-F_k)/2\) and \(Q_{k-1}=2P-Q\) in
(15), and use this displayed equality to obtain
\[
 a_{2k-1}=\tfrac12 XY+PY+Q(X-2Y)-\tfrac12 Y^2.
\]
On expanding the right side of (14), the difference from
\(Da_{2k-1}-9P^2\) is, up to sign,
\[
 -\tfrac54(Y^2+4QY)+XP+X^2/4-9P^2=0,
\]
where \(D^2-2D=-5\).

If \(n\) is a square index, let \(\mathfrak q\) be a prime of
\(\mathbb Q(i)\) of rational residue characteristic \(p>5\)
such that \(D\) is nonsquare modulo \(\mathfrak q\).
Both factors in (14) have even valuations at \(\mathfrak q\).
Indeed they are integral there. Their product is the negative
norm of \(3P_k+x\sqrt D\) and is nonzero since \(a_{2k-1}>0\).
If both factors were zero in the residue field, the nonsquare
condition would force \(P_k=0\), and \(\widetilde z=0\) would
then give \(Q_k=0\), contrary to \(Q_k^2-2P_k^2=(-1)^k\).

Assume further that \(k\) is even, as on the zero-anchor branch.
Vanishing of either factor at \(\mathfrak q\) gives \(P_k=0\),
and hence \(Q_k=\beta^k=\varepsilon=\pm1\) in the residue field
of any prime above \(\mathfrak q\) in \(K(i)\). Put \(U=\alpha^k\).
If \(\widetilde\ell=0\), then
\[
 (U-\varepsilon)
 \big(D(U-\varepsilon)-\sqrt5(U+\varepsilon)\big)=0 .
\]
If \(\widetilde z=0\), use \(\widetilde\ell=-4D\varepsilon\)
to interchange \(U-\varepsilon\) and \(U+\varepsilon\).
Since \((D+\sqrt5)/(D-\sqrt5)=-i\alpha\), the two phase sets are
\[
 \begin{array}{c|c}
 \widetilde\ell=0 & U\in\{\varepsilon,-i\varepsilon\alpha\}\\
 \widetilde z=0 & U\in\{-\varepsilon,i\varepsilon\alpha\}.
 \end{array}
\]
The denominators are units at \(p>5\), because the rational
norm of \(D^2-5\) from \(\mathbb Q(i)\) is 80.
The first phase in each row gives \(F_k=0\), and the second
gives \(F_{k-1}=0\), since \(k-1\) is odd. Thus every such
prime divides \(\gcd(P_k,F_kF_{k-1})\).

For the two signs define \(X_\pm=5F_k\pm2P_k\) and
\(Y_\pm=L_k\pm2Q_k\). The two tangent identities apply the
same linear form to both signs:
\[
 \begin{aligned}
 2(2+\sqrt2)\ell &=(2+\sqrt2)X_--Y_-,&
 2z_2&=Y_+-(2+\sqrt2)X_+,\\
 \widetilde\ell&=DY_--X_-,&
 4\widetilde z&=X_+-DY_+ .
 \end{aligned}
\]
These expressions follow from the definitions in Section 8
and \(d(2+\sqrt2)=2\).
At a square index with even \(k\), suppose a rational prime
\(p>5\) is nonsplit for both quadratic twists at primes above \(p\)
in their respective base fields. Then the minus factor of
either identity and the plus factor of the other have disjoint
support at those primes. If both vanished, the phase restrictions
would give \(F_k=P_k=0\) and \(\alpha^k,\beta^k\in\{1,-1\}\)
at a prime of the mixed field. The minus factor would require the
two signs to agree, and the plus factor would require them to differ.
Indeed, for \(F_k=P_k=0\) both linear forms reduce to a unit
times \(Y_-\) or \(Y_+\), which are rational modulo \(p\).

On the zero-anchor branch, \(\widetilde z/(-D)\) is a local
square at 2 and at both primes above 5. At 2, the divisibility
of \(P_k,X,Y,Q_k-1\) from Section 8 gives
\(\widetilde z\equiv-D\pmod{2^{v_2(k)-1}}\), and \(D\)
is a unit. At 5, \(60\mid k\), the same section gives
\(5^3\mid X,Y\), \(5^4\mid Q_k-1\), and
\(5^2\mid P_k\) by the valuation of \(\log\beta^{60}\).
Thus \(\widetilde z+D\) is divisible by \(5^2\) at both
primes above 5, whereas \(D\) has valuation at most one.
The local square assertions follow by Hensel's lemma.
The element \(-D\) is a norm from \(\mathbb Q(i,\sqrt D)\).
When \(a_n\) is locally square at 2 and 5, (14) likewise
makes \(\widetilde\ell\) a local norm at those places.
The product of its norm characters over the other finite
places is \(+1\) by Hilbert reciprocity.

The two rational tangent norms satisfy the relation
\[
 \begin{aligned}
 N_{\mathbb Q(\sqrt2)/\mathbb Q}(2\sqrt2\,\ell)
   &=Y^2-2(X-Y)^2,\\
 N_{\mathbb Q(i)/\mathbb Q}(\widetilde\ell)
   &=4Y^2+(X-Y)^2.
 \end{aligned}
\]
The first plus twice the second is \(9Y^2\).
Consequently a rational prime \(p>5\) divides both norms
precisely when \(p\mid X,Y\). The equality
\(Y^2+4QY=(X+2P)^2/5-8P^2\) then gives \(P=0\)
and \(F_k=0\) modulo \(p\). For even \(k\), this forces
\(\alpha^k=\beta^k=\pm1\) with the same sign.
Thus all common prime support above 5 belongs to this
simultaneous period condition.

The two tangent forms arise from the rank-three members
of the following quadratic pencil. With \(j=k-1\), suppress
subscripts \(j\) on \(L,F,P,Q\) and add
\(\lambda[(L^2-5F^2)-4(Q^2-2P^2)]\) to
\(\frac12L^2+\frac52LF+4P^2+2PQ\).
The determinants of the \((L,F)\) and \((P,Q)\) blocks
are \(-5\lambda(\frac12+\lambda)-25/16\) and
\(-4\lambda(4+8\lambda)-1\). Their simple roots are
\((-1\pm2i)/4\) and \((-2\pm\sqrt2)/8\), respectively.
Each block has rank at least one, and the two sets of roots
are disjoint. These are the four rank-three members, all other
members at finite \(\lambda\) having rank four.

**A Gaussian witness.** Put \(p=8035529\), \(q=1004441\), so
\(p=8q+1\), and use the prime of \(\mathbb Q(i)\) specified by
\(i\equiv2990643\pmod p\). At
\(k\equiv6113696\pmod {p-1}\) the exact certificate gives
\(\widetilde\ell=0\), \(P_k\ne0\), and \(D\) nonsquare.
The prime splits in \(K\), as \(p\equiv1\pmod8\) and
\(p\equiv4\pmod5\), so both matrix periods divide \(p-1\).
With \(S,c\) as in the witness in Section 8, impose
\(n\equiv-1+3cS\pmod{8S}\) and \(n\equiv12227391\pmod{16q}\).
The moduli have gcd 16 and both residues are \(-1\pmod{16}\).
This gives infinitely many indices at depth 202 that pass
the same sieve through \(10^6\) and are excluded by (14).

**Sign phases at high valuations.** Suppose \(n=2k-1\) and
\(v_2(2k)\ge3\). At a prime above \(p>5\), if
\((\alpha^{2k},\beta^{2k})=(-1,1)\) then \(a_n\equiv2\);
if \((\alpha^{2k},\beta^{2k})=(1,-1)\) then \(a_n\equiv-2\).
Neither case supplies a quadratic nonresidue in its rational
residue field. In the first, nonresiduosity would require
\(p\equiv3,5\pmod8\). The 2-part of the order of every element
of \(\mathbb F_{p^2}^{\times}\) is then at most 8, so
\(\alpha^{2k}\) cannot be \(-1\). In the second, nonresiduosity
would require \(p\equiv5,7\pmod8\). For \(p\equiv5\) the same
order argument applies to \(\beta\); for \(p\equiv7\),
\(\beta\in\mathbb F_p^\times\) and \(v_2(p-1)=1\), which
again precludes \(\beta^{2k}=-1\).

## 11. Common square-root valuations in the norm equations

Suppose \(n\ge3\) is an odd square index and \(a_n=x^2\).
The inert-place norm calculations constrain the same integer \(x\).
In fact, at each indicated prime \(p>5\) the following equalities hold:
\[
 \begin{array}{c|c|c}
 \text{prime condition}&\text{source valuation}&\text{value}\\ \hline
 \pi\mid R_{n\pm2},\ \chi_\pm(\pi)=-1
   &v_p(P_{n\pm2})&2\min(v_p(x),v_p(F_n))\\
 p\mid T_n,\ p\equiv7,9\pmod{16}
   &v_p(T_n)&2\min(v_p(x),v_p(Q_n))\\
 p\mid M_n,\ p\equiv7,9\pmod{16}
   &v_p(M_n)&2\min(v_p(x),v_p(L_n^2-2)).
 \end{array}
 \tag{18}
\]
Here \(\pi\) is a Gaussian prime over \(p\) and the signs
refer to the two factors in Section 2 of [the norm descent](norm-descent.md#2-a-gaussian-factorization-for-the-odd-indices).

For the first row, after the conjugation in that factorization
the relevant prime divides \(P_n-2i=x^2-d_0z_0^2\), where
\(L_n+2i=d_0z_0^2\) and \(d_0\) is a nonsquare unit.
Its valuation is \(2\min(v_p(x),v_\pi(z_0))\). It is positive,
so \(L_n+2i=0\bmod\pi\), and \(L_n-2i\) is a unit there.
Since \((L_n+2i)(L_n-2i)=5F_n^2\), this gives
\(v_\pi(z_0)=v_p(F_n)\). The coprime Gaussian factorization
identifies the source valuation with \(v_p(P_{n\pm2})\).

For the second row, use the norm in (11). At a prime over
\(p\) its two coordinates are \(Q_n+\sqrt2 x^2\) and a unit
times \(x\). The minimum of their valuations is
\(\min(v_p(Q_n),v_p(x))\): adding \(\sqrt2 x^2\) leaves the
valuation of \(Q_n\) unchanged when it is less than \(v_p(x)\),
and preserves the lower bound \(v_p(x)\) otherwise.

For the third row, use the unique prime of \(K\) above \(p\)
that divides \(\eta^n-1\), as proved in Section 6.
In the positive-sign norm the partner \(\xi^n-1\) is a unit
and the twist \(2\sqrt2\) is a nonsquare unit. The valuation
is twice the minimum of \(v_p(x)\) and the valuation of
\(L_n+\sqrt2\). The latter equals \(v_p(L_n^2-2)\), since
\(L_n-\sqrt2\) is a unit there.

Let \(B_G,B_T,B_M\) be the products of the full \(p\)-powers in
the respective three rows, using each rational prime once
for each row where it occurs. Then their prime supports are
pairwise disjoint and
\[
 B_GB_TB_M\mid a_n .
 \tag{19}
\]
Indeed the three rows force \(L_n^2\equiv-4,1/2,2\pmod p\),
respectively. These residues are pairwise distinct for \(p>5\),
and each source valuation is at most \(2v_p(x)\).

**Concurrent order constraints.** In the first row of (18),
\(\alpha^{2n}=\beta^{2(n\pm2)}=-1\) modulo primes over \(p\).
The odd parts of the two unit orders divide \(n\) and
\(n\pm2\), respectively, and are coprime. This is a condition
on every such prime dividing \(R_s\) for \(s\mid n\pm2\),
because (4) of the Gaussian factorization shows that \(R_s\)
divides \(R_{n\pm2}\).
For example, \(7\mid n-2\) is excluded: \(R_7=12+5i\) has
valuation two above \(13\) at \(i\equiv8\pmod{13}\), where
\(1-2i\equiv11\) is a nonresidue. The prime 13 is inert in both
quadratic fields, and the unit orders divide 28 with valuation
two at 2.
Neither has order four, since substituting a root of \(X^2+1\)
into its quadratic unit polynomial is possible only in
characteristic 5 or 2, respectively. Thus both have odd
order part 7, contradicting the coprimality condition.
Likewise, if \(p\equiv1\pmod8\) and \((5/p)=1\), such a
Gaussian prime cannot occur. In that case the character
of \(1\pm2i\) is the character of \(\alpha\), by
\((\alpha\pm i)^2=\alpha(1\pm2i)\). A nonsquare \(\alpha\)
has 2-primary order at least eight modulo \(p\), whereas
\(\alpha^{2n}=-1\) at odd \(n\) gives 2-primary order four.

In the dual row, the valuation forces \(Q_n=0\bmod p\).
At the prime of \(K\) with \(\alpha^n=\sqrt2\), one then has
\(L_n=1/\sqrt2\), \(P_n=-L_n\), and \(\beta^n=-1\).
Thus at the prime \(p=2002919=2q+1\) of Section 9, no index with
\(p\mid T_n\) can be a square index, even if the valuation of
\(T_n\) is even. The order of \(\beta\) in \(\mathbb F_p^\times\)
is divisible by \(q\), since \(\beta\ne\pm1\) and \(q\) is prime.
But \(\alpha^{2n}=2\) in the specified residue field precludes
\(q\mid n\).

The exact verifier exhibits this improvement at depth 201.
With the same \(S\) as in Section 9, impose \(n\equiv3+S\bmod2S\)
and
\[
 n\equiv2901680796375\pmod {p^2(p-1)}.
\]
The latter modulus is a Lucas period modulo \(p^3\), and the
residue gives \(T_n\equiv113915p^2\pmod {p^3}\).
The moduli have gcd 2, so this gives infinitely many positive
indices that pass the sieve through \(10^6\) and have
\(v_p(T_n)=2\). The dual row of (18) excludes all of them.

## 12. A single shifted tangent identity for all odd anchors

Let \(r\) be odd and write \(n=r+2k\). Put
\(\Delta=a_{r+2k}-(-1)^k a_r\). For a parameter \(d\)
define the two linear factors
\[
 \begin{aligned}
 H_-&=d(L_k-2Q_k)+5F_rF_k+2Q_rP_k,\\
 H_+&=d(L_k+2Q_k)+5F_rF_k-2Q_rP_k.
 \end{aligned}
\]
Then
\[
 \begin{aligned}
 H_-H_+={}&4d\Delta
 +5\big((d-L_r)^2+4\big)F_k^2\\
 &-8\big((d+P_r)^2-\tfrac12\big)P_k^2 .
 \end{aligned}
 \tag{22}
\]
The addition formulas give
\[
 \Delta=5F_kF_{k+r}+2P_kQ_{k+r}
 =\tfrac52 L_r F_k^2+\tfrac52 F_r L_kF_k
    +4P_rP_k^2+2Q_rP_kQ_k .
\]
The first equality follows by multiplying the Binet
differences for the Fibonacci factors and the Binet
difference and sum for the Pell factors. The second follows
from \(2F_{k+r}=L_rF_k+F_rL_k\) and
\(Q_{k+r}=Q_rQ_k+2P_rP_k\).
Expanding
\[
 H_-H_+=(dL_k+5F_rF_k)^2-(2dQ_k-2Q_rP_k)^2
\]
and using \(L_k^2-4Q_k^2=5F_k^2-8P_k^2\) gives (22).
The coefficients of \(F_k^2\) and \(P_k^2\) use
\(L_r^2-5F_r^2=-4\) and \(Q_r^2-2P_r^2=-1\), respectively.

For \(d=L_r+2i\), (22) gives the Gaussian identity
\[
 H_-H_+=4d\Delta-4\big(2(a_r+2i)^2-1\big)P_k^2.
 \tag{23}
\]
For \(d=-P_r+\sqrt2/2\), it gives
\[
 H_-H_+=4d\Delta+5\big((d-L_r)^2+4\big)F_k^2.
 \tag{24}
\]
Conjugating gives the other two choices of \(d\) at the
rank-three members. On the zero-anchor branch
\(a_r=0\), these are the two fixed twists of Sections 8 and 10.
For \(r=\pm3\) and even \(k\), the twisted square target
in (23) is
\[
 W_{r,k}=a_r+\frac{2(a_r+2i)^2-1}{L_r+2i}P_k^2.
\]
At a Gaussian prime of residue characteristic \(p>7\)
dividing \(H_-\) or \(H_+\), a square index requires
\(W_{r,k}\) to be a square in the residue field, including
the zero residue. With the same even \(k\) on \(r=\pm3\),
equation (24) gives the corresponding test at primes above
\(p>7\) in \(\mathbb Q(\sqrt2)\) with target
\(a_r-\frac{5((d-L_r)^2+4)}{4d}F_k^2\). The only primes to
exclude when forming the two quotients for general odd \(r\)
divide \(10F_r^2\) and \(2Q_r^2\), respectively, by taking
norms of \(d\) and accounting for the denominator at 2.

For \(r=\pm3\), a prime \(p>7\) inert in the coefficient
field of either identity cannot give a nonresidue. In the
quadratic residue field, the irrational part of \(d\) is
nonzero, so \(H_\mp=0\) implies \(L_k\mp2Q_k=0\) and
\(5F_rF_k\pm2Q_rP_k=0\). Squaring and using the norm
equations gives \(5F_k^2=8P_k^2\) and
\(4(10F_r^2-Q_r^2)P_k^2=0\) modulo \(p\). Since
\(10F_r^2-Q_r^2=-9\), both \(P_k,F_k\) vanish and each
target reduces to \(a_r\), which is a square.

**Witnesses at the two nonzero anchors.** The following
data are certified by exact modular exponentiation. In
each row \(p=8q+1\), both \(p,q\) are prime, \(i=i_0\bmod p\),
and the residue \(k\equiv k_0\pmod{p-1}\) gives
\(H_-=0\bmod p\) with \(W_{r,k}\) a nonresidue.
\[
 \begin{array}{r|r|r|r|r|r}
 r&p&q&i_0&k_0&W_{r,k}\bmod p\\ \hline
 -3&8015849&1001981&7705988&2193968&1336023\\
  3&8059049&1007381&7557665&8053768&5802682
 \end{array}
\]
For each \(r\), define the odd integer \(H\) as in Section 9
using \(D_r\) and put \(S=2^{201}H\). The certificate verifies
\(v_2(D_r)\le201\), so \(D_r\mid S\). The two congruences
\[
 n\equiv r+S\pmod{2S},\qquad n\equiv r+2k_0\pmod{16q}
\]
are compatible. Their moduli have gcd 16, since \(q>1000001\)
and the odd prime factors of \(D_r\) are at most 2000.
Both residues are \(r\bmod16\). Every positive solution
has \(D_r\mid n-r\), \(v_2(n-r)=201\), and passes the
square-residue tests at every prime at most \(10^6\).
The second congruence fixes \(k=(n-r)/2\bmod(p-1)\).
Both matrix periods divide \(p-1\), as each \(p\) splits
in \(K\). Thus (23) excludes every index in both progressions.

## Reproduction

Run:

    python3 verify_norm_order.py
    python3 verify_norm_graph_limits.py
    python3 verify_unified_structure.py

The verifiers use only the Python standard library and exact modular
arithmetic. They verify the witnesses without computing large sequence
values or enumerating candidate square indices.
