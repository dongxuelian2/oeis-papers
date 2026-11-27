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
\(t\equiv-1\pmod5\). The factors \(R_3\) and \(R_t\) divide
\(R_{3t}\) and are coprime, since \(N(R_3)=5\) and \(5\nmid P_t\).
For odd \(t\), the identity \(P_{3t}=P_t(8P_t^2-3)\)
gives the prime norm \((8P_t^2-3)/5\) for
\(R_{3t}/(R_3 R_t)\). The two factors \(R_t\) and
\(R_{3t}/(R_3 R_t)\) each have prime norm and
character \(\chi_-=1\), by (6) and (8) of the Gaussian descent.
The divisors \(1,3,t,3t\) of \(n-2\) therefore satisfy the
valuation tests. This criterion specifies a primality pattern
under which the three divisor tests agree.

## Reproduction

Run:

    python3 verify_norm_order.py
    python3 verify_norm_graph_limits.py

The verifiers use only the Python standard library and exact modular
arithmetic. They verify the witnesses without computing large sequence
values or enumerating candidate square indices.
