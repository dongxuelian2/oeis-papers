# Limits of offset-prime descent and saturated smooth-support obstructions

Put \(a_n=L_n+P_n\), with the two sequences extended to integer indices.
This note tests the proposed covering property of the variable-prime
descent and obtains an exact square-class criterion for the zero anchor.

## 1. Offset-prime covering fails

**Theorem 1.** For any \(N\ge13\), let \(K=(N!)^2\).
For each \(r\in\{3,-3,-2,-1\}\) and every prime \(p\mid K\),
\[
 a_{r+K}\equiv a_r\pmod{p^3}.
\]
For \(r=3,-3,-2\), \(a_{r+K}\) is a square in \(\mathbb Q_p\)
for every prime \(p\mid K\).
For every prescribed positive divisor \(D\), the construction has
\(D\mid K\) for all sufficiently large \(N\).

**Proof.** Use the recurrence matrices
\[
 A=\begin{pmatrix}0&1\\1&1\end{pmatrix},
 \qquad B=\begin{pmatrix}0&1\\1&2\end{pmatrix},
 \qquad T=\operatorname{diag}(A,B).
\]
For every prime \(5<p\le N\), both matrices are diagonalizable
over \(\mathbb F_{p^2}\), with nonzero eigenvalues. Thus
\(T^{p^2-1}\equiv I\pmod p\). Both \(p-1\) and \(p+1\) divide
\(N!\): for the latter, write \(p+1=2((p+1)/2)\) with two
distinct factors at most \(N\). Consequently \(p^2-1\mid K\).
Also \(p^2\mid K\), and \(p\nmid p^2-1\). Repeated binomial
expansion gives \(T^K\equiv I\pmod{p^3}\).

For \(p=2,3,5\), direct matrix arithmetic gives
\(T^6\equiv I\pmod2\), \(T^8\equiv I\pmod3\), and
\(T^{120}\equiv I\pmod5\). The divisibilities of \(K\) for
\(N\ge13\) likewise permit two further lifts in each case.
This proves the congruence, even for negative anchors,
because the matrices are unimodular.

The anchor values are \(9,1,1,0\), respectively. For the three
nonzero anchors the congruence modulo \(p^3\) suffices for the
local square criterion, including at 2 and at 3 (where the
valuation of 9 is two). Finally any fixed integer \(D\) divides
\(N!\) for \(N\ge D\). QED.

In particular the claim that every nonzero offset in a candidate
anchor class has a prime factor at which the sequence value is
a quadratic nonresidue is false. The constructed indices can
satisfy any earlier fixed forced-divisor constraint as well.
For the nonzero anchors, the known finiteness theorem implies
that, for sufficiently large \(N\), these positive integer
values are not global squares. Any prime of odd valuation
in such a value must exceed \(N\), and therefore cannot divide
its offset \(K\). This is a rigorous obstruction to a proof
restricted to the primes dividing the index offset.

## 2. A general local square-class criterion for the zero anchor

Let \(k>0\), so the index on the zero-anchor branch is \(n=k-1\).
Use \(s=(-1,2,1,0)^{\mathsf T}\) and \(\ell=(1,0,1,0)\);
then \(a_{k-1}=\ell T^k s\) and \(\ell s=0\).

**Lemma 2.** For a prime \(p\), choose \(h>0\), put
\[
 d=v_p(T^h-I),\qquad e=v_p(a_{h-1}),\qquad
 w_p=\begin{cases}3&p=2,\\1&p>2.\end{cases}
\]
Here matrix valuation means the minimum entry valuation.
Suppose \(d\ge1\) and \(2d-\mathbf 1_{p=2}\ge e+w_p\).
Set \(c_p=a_{h-1}/h\in\mathbb Q^\times\).
For every positive multiple \(k=ht\) of \(h\),
\[
 v_p(a_{k-1})=v_p(c_p)+v_p(k),\qquad
 u_p(a_{k-1})\equiv u_p(c_p)u_p(k)\pmod{p^{w_p}},
\]
where \(u_p(z)=z/p^{v_p(z)}\). Equivalently,
\[
 a_{k-1}\in\mathbb Q_p^{\times2}
 \quad\Longleftrightarrow\quad c_p k\in\mathbb Q_p^{\times2}.
\]

**Proof.** Put \(C=T^h-I\). Expanding \((I+C)^t\) gives
\[
 a_{ht-1}=t\,a_{h-1}+
 \sum_{j=2}^{t}\binom tj\,\ell C^j s.
\]
Since \(j\binom tj=t\binom{t-1}{j-1}\), the valuation of a
term with \(j\ge2\) is at least \(v_p(t)+jd-v_p(j)\).
For odd \(p\), \(v_p(j)\le j-2\) for \(j\ge2\); for \(p=2\),
\(v_2(j)\le j-1\). Thus the remainder is divisible by
\(p^{v_p(t)+2d-\mathbf 1_{p=2}}\), which by hypothesis is
at least \(p^{v_p(t)+e+w_p}\).
The leading term \(t a_{h-1}=c_pk\) determines both the
valuation and the square-determining unit residue. QED.

**Theorem 3 (fixed finite support).** Let \(S\) be a finite set
of primes. For each \(p\in S\), suppose a period \(h_p\)
satisfying Lemma 2 has been certified. Write
\[
 H=\operatorname{lcm}_{p\in S} h_p,\qquad
 d_S=\prod_{\substack{p\in S\\v_p(c_p)\ \mathrm{odd}}}p.
\]
For a positive integer \(k\) divisible by \(H\) and having no
prime factors outside \(S\), the value \(a_{k-1}\) is a local
square at every \(p\in S\) if and only if both
\[
 k=d_S y^2\quad (y\in\mathbb Z_{>0}),\qquad
 c_p d_S\in\mathbb Q_p^{\times2}\quad(p\in S).
\]
In particular if one of the latter local tests fails, no
such offset \(k\) can produce a global square, regardless
of its size or the exponents of its prime factors.

**Proof.** By the lemma, local squareness requires
\(v_p(k)\equiv v_p(c_p)\pmod2\) for all \(p\in S\).
The support hypothesis makes this equivalent to the first
displayed condition. Multiplication by \(y^2\) does not change
any local square class. Applying the lemma again establishes
the equivalence. If \(H\) has support outside \(S\) there
are no offsets satisfying the hypotheses in the first place. QED.

## 3. Infinite-family exclusion with an exact certificate

For a bound \(N\ge13\) define \(S_N=\{p:p\le N,\ p\text{ prime}\}\).
Choose
\[
 h_2=48,\quad h_3=24,\quad h_5=3000,\qquad
 h_p=p(p^2-1)\quad(p>5).
\]
Let \(H_N=\operatorname{lcm}_{p\in S_N}h_p\).

**Theorem 4.** For every integer \(13\le N\le100000\), no
positive integer \(k\) satisfying
\[
 H_N\mid k,\qquad \text{every prime factor of }k\text{ is }\le N
\]
has \(a_{k-1}\) a square. In particular this holds for every
\(N\)-smooth positive multiple of \((N!)^2\).

**Proof.** The companion program verify_smooth_support.py
checks the hypotheses of Lemma 2 for all 9592 primes at most
100000, by exact matrix exponentiation modulo \(p^8\).
The only primes in this range with even valuation \(v_p(c_p)\)
are \(2,3,5,19,307\). Thus the unique possible rational square
class \(d_{S_N}\) is the product of all primes up to \(N\)
except those five (omitting any that exceed \(N\)).

For each prime prefix with largest prime at least 13,
the program evaluates \(u_p(c_p d_{S_N})\) at the first
16 primes, using only those in the prefix. At least one
is a nonsquare unit in every case. There are precisely
9587 distinct prefixes; their first obstructing primes
are counted by the following certificate:

| First obstruction | Number of prefixes |
|---:|---:|
| 2 | 7173 |
| 3 | 1209 |
| 5 | 579 |
| 7 | 293 |
| 11 | 142 |
| 13 | 85 |
| 17 | 53 |
| 19 | 22 |
| 23 | 11 |
| 29 | 11 |
| 31 | 1 |
| 37 | 5 |
| 41 | 2 |
| 43 | 1 |

The counts sum to 9587. Theorem 3 excludes every offset
in every tested family. Every integer \(N\) between
successive primes gives the same prime prefix, so this
covers the full stated interval of bounds.

Finally \(H_N\mid(N!)^2\). For \(p>5\), \(p^2-1\mid(N!)^2\)
as shown above, and \(p\) is coprime to \(p^2-1\) and divides
\(N!\). The three small-prime divisibilities hold already
at \(N=13\). This proves the last assertion. QED.

Each family in Theorem 4 contains arbitrarily large offsets.
It is an exclusion of whole infinite families, not a finite
index search. The theorem requires the indicated divisibility
by \(H_N\); it makes no assertion about all \(N\)-smooth offsets
without that condition.

The same computation gives \(h_2=48\), \(v_2(c_2)=0\) and
\(u_2(c_2)\equiv3\pmod8\). Thus for every positive multiple
\(k\) of 48,
\[
 a_{k-1}\in\mathbb Q_2^{\times2}
 \quad\Longleftrightarrow\quad k\in3\mathbb Q_2^{\times2}.
\]
In particular square offsets on the zero branch are excluded
by the full 2-adic test, even though their Legendre tests in
Theorem 1 all pass.

## 4. Further-prime constraints

The square-class criterion also gives a necessary condition
when extra primes are allowed in the offset. If \(H\mid k\),
write its squarefree kernel as \(d_S d_{\rm out}\) with
\(d_{\rm out}\) coprime to all primes in \(S\).
A global square requires the parity of valuations at \(S\)
used in Theorem 3, and additionally
\[
 c_p d_S d_{\rm out}\in\mathbb Q_p^{\times2}
 \qquad(p\in S).
\]
These are a specified vector of quadratic characters of
\(d_{\rm out}\) at the odd primes in \(S\), together with a
unit class modulo 8 if \(2\in S\). They constrain the extra
odd-valuation prime factors, rather than just divisibility of
the offset. They do not exclude arbitrary large outside primes:
quadratic reciprocity and the Chinese remainder theorem allow
a prime with any prescribed consistent set of these signs.

## Reproduction

Run:

    python3 verify_smooth_support.py

The script verifies all 9587 prefix exclusions and independently
checks the exact valuation and leading-unit formula at 189
sample multiples. The proof of the formula is independent of
the sample tests.

The unrestricted square-index problem remains unresolved. The
uniform finite exclusion through \(10^{341}\) from earlier work
is unchanged.
