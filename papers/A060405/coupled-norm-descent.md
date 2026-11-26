# Coupled norm descent as a finite-support problem

This note develops the odd-index norm identities into a coupled
order-and-valuation system. Unlike a descent that requires two factors
to be coprime, this system retains the possibility that odd valuations
in the two factors cancel. The desired global contradiction is the
nonexistence of a nontrivial finite prime-support model.

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

## 6. The global research target

The one-factor norm descent for even indices succeeds because
a quadratic character controls an entire quotient of a
divisibility sequence. The character forces a new prime with
strictly larger index relevance. In the mixed-unit odd-index
norms, a bad prime can instead appear in both factors and its
valuation can cancel. Equation (1) identifies the two exact
ways such a defect can be resolved: a parity condition on
the index, or activation of a second order constraint.
The next problem is to find a uniform arithmetic principle
governing these alternatives, possibly through quadratic
characters of cyclotomic factor ideals and their intersections.

A concrete sufficient target is a primitive-factor theorem
with **both** a quadratic-character condition and a constraint
on the order of the other unit. For an activated divisor \(s\mid n\),
one seeks an odd-valuation prime ideal in a factor of
\(\eta^s-1,\xi^s-1,(-\eta)^s-1\), or \((-\xi)^s-1\)
whose partner order is forbidden, or which generates another
order-and-parity implication. The three terminal vertices show
that this must be an escaping system of composite activations
and/or additional norm channels, rather than an individual edge
from every prime. The usual existence of a primitive divisor
alone does not give its quadratic character or its partner
order. The finite calculation in Section 4 neither proves nor
assumes such a uniform theorem.

This note supplies an exact local rule, a global finite-support
criterion and ten certified instances. It does not claim
that the graph has no finite nontrivial model, or that the
unrestricted square-index classification is complete.

## Reproduction

Run:

    python3 verify_norm_order.py
    python3 verify_norm_graph_limits.py

The verifiers use only the Python standard library and exact modular
arithmetic. They verify the witnesses without computing large sequence
values or enumerating candidate square indices.
