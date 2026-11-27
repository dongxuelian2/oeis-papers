# Exact local geometry at the square anchors

Write \(a_n=L_n+P_n\), extended to integer indices, and \(M=720720\).
The four-anchor theorem restricts square indices to
\(n\equiv r\pmod M\), where \(r\in\{3,-3,-2,-1\}\).
This note determines the complete local square conditions on these
branches at the six primes dividing \(M\), and gives a limitation
theorem for arbitrary finite sets of local primes.

## 1. Complete local analysis at the six base primes

Let
\[
 T=\operatorname{diag}\left(
 \begin{pmatrix}0&1\\1&1\end{pmatrix},
 \begin{pmatrix}0&1\\1&2\end{pmatrix}\right),\quad
 s=(-1,2,1,0)^{\mathsf T},\quad \ell=(1,0,1,0).
\]
For \(t\ge1\) put \(b(t)=a_{Mt-1}=\ell T^{Mt}s\).
For a nonzero \(p\)-adic number \(z\), write
\(u_p(z)=z/p^{v_p(z)}\).

**Theorem 1.** For \(p=2,3,7,11,13\) and every positive integer \(t\),
\[
 v_p(b(t))=e_p+v_p(t),\qquad
 u_p(b(t))\equiv c_p u_p(t)\pmod{p^{j_p}},
\]
where the exact constants are as follows.

| \(p\) | \(v_p(T^M-I)\) (minimum entry valuation) | \(e_p\) | \(c_p\) | \(j_p\) |
|---:|---:|---:|---:|---:|
| 2 | 4 | 4 | 7 | 3 |
| 3 | 3 | 4 | 2 | 1 |
| 7 | 2 | 2 | 3 | 1 |
| 11 | 2 | 2 | 7 | 1 |
| 13 | 2 | 2 | 5 | 1 |

Hence \(b(t)\) is a square in \(\mathbb Q_2\) precisely when
\(-t\) is a square in \(\mathbb Q_2\). At each of the other
four primes in the table it is a square precisely when
\(v_p(t)\) is even and \(u_p(t)\) is a quadratic nonresidue
modulo \(p\).

**Proof.** The table is certified by modular matrix exponentiation
modulo \(p^{12}\); the companion script checks every entry.
Set \(C=T^M-I\), and let \(d_p=v_p(C)\) denote the minimum
valuation of its entries. Since \(\ell s=0\),
\[
 b(t)=t\,\ell Cs+\sum_{j=2}^{t}\binom tj\ell C^j s.
\]
Using \(j\binom tj=t\binom{t-1}{j-1}\), each term in the sum
has valuation at least \(v_p(t)+j d_p-v_p(j)\).
For each odd prime in the table, \(d_p\ge2\), and for \(j\ge2\)
one has \(j d_p-v_p(j)\ge2d_p\) (use
\(v_p(j)\le j-2\) for odd \(p\) and \(j\ge2\)).
Thus the valuation is at least \(v_p(t)+e_p+1\).
For \(p=2\), \(4j-v_2(j)\ge7\), so the valuation is at least
\(v_2(t)+e_2+3\). The linear term therefore determines the
displayed valuation and leading unit. All \(e_p\) are even,
and \(2,3,7,5\) are nonresidues modulo \(3,7,11,13\),
respectively. The usual local square criteria prove the result. QED.

## 2. Two simple 5-adic roots

**Theorem 2.** There is a unique \(\tau\in1+5\mathbb Z_5\) such that
the analytic interpolation of \(b(t)\) vanishes at \(\tau\).
For all positive integers \(t\) the following formulas hold:
\[
\begin{array}{c|c|c}
t\bmod5 & v_5(b(t)) & u_5(b(t))\bmod5\\ \hline
0 & 3+v_5(t) & 3u_5(t)\\
1 & 3+v_5(t-\tau) & 2u_5(t-\tau)\\
2,3,4 & 3 & 2t(t-1)
\end{array}
\]
In particular \(b(t)\) is a square in \(\mathbb Q_5\) if and only if
one of the following disjoint alternatives holds:
* \(t\equiv0\bmod5\), \(v_5(t)\) is odd, and \(u_5(t)\) is a
  quadratic nonresidue modulo 5;
* \(t\equiv1\bmod5\), \(v_5(t-\tau)\) is odd, and
  \(u_5(t-\tau)\) is a quadratic nonresidue modulo 5.

The second root has the certified approximation
\[
 \tau\equiv9500531834602826\pmod{5^{24}}.
\]

**Proof.** For \(C=T^M-I\) the script verifies
\(v_5(C)=1\), \(v_5(\ell Cs)=5\),
\(\ell C^2s\equiv500\bmod625\), and
\(\ell C^3s\equiv0\bmod625\).
Consider the restricted power series
\[
 F(t)=\frac1{125}\sum_{j\ge1}\binom tj\ell C^j s .
\]
For \(j\ge4\), all polynomial coefficients of the \(j\)-th
summand before division by 125 have valuation at least
\(j-v_5(j!)\ge4\), tending to infinity with \(j\).
The first three summands satisfy the verified stronger
congruences above; \(2!\) and \(3!\) are units modulo 5.
It follows that \(F\in\mathbb Z_5\langle t\rangle\) and
\[
 F(t)\equiv4\binom t2=2t(t-1)\pmod5
\]
as a power series, not merely as a function on residue classes.
The two roots modulo 5 are simple. Hensel's lemma gives exactly
two roots in \(\mathbb Z_5\): zero (since \(F(0)=0\)) and \(\tau\).
For \(t\equiv0\bmod5\), the divided difference \(F(t)/t\)
is congruent to \(-2\) modulo 5. For \(t\equiv1\bmod5\),
\((F(t)-F(\tau))/(t-\tau)\equiv2\bmod5\).
These statements follow by factoring each power-series monomial
difference; the divided differences converge since the coefficients
tend to zero. The valuation and unit formulas now follow from
\(b(t)=125F(t)\). Since 2 and 3 are nonresidues modulo 5,
the local square criteria give the stated alternatives.
The script lifts \(\tau\) one base-5 digit at a time by testing
the congruence \(b(t)\equiv0\bmod 5^{k+3}\) for precision \(5^k\).

The root \(\tau\) is not an ordinary integer. For \(t\ge1\),
\(a_{Mt-1}>0\). For \(t\le-1\), \(Mt-1\) is negative odd and
\(a_{Mt-1}=P_{1-Mt}-L_{1-Mt}>0\):
\(P_3>L_3\), \(P_4>L_4\), and the recurrences preserve this
strict inequality for all later indices. Only \(t=0\) is an
integer root. QED.

## 3. The other three anchors at the base primes

**Theorem 3.** For every integer \(t\), every
\(p\in\{2,3,5,7,11,13\}\), and \(r\in\{3,-3,-2\}\),
\(a_{r+Mt}\) is a nonzero square in \(\mathbb Q_p\).

Indeed \(T^M\equiv I\bmod p\) for the odd primes, and
\(T^M\equiv I\bmod16\) for \(p=2\).
Thus \(a_{r+Mt}\equiv a_r\bmod p\) for each odd prime and
modulo 16 at 2, also for negative \(t\) since \(T\) is
unimodular. The anchor values are 9,1,1. All are nonzero
square residues at the relevant prime, except 9 at \(p=3\).
In that exception the verified matrix depth 3 gives
\(a_{3+Mt}\equiv9\bmod27\), so its valuation is 2 and its
unit is 1 modulo 3. This proves the claim.

## 4. Finite-prime limitation theorem

The earlier obstruction to finite periodic congruence sieves
can be strengthened to allow arbitrarily high powers of any
fixed finite set of primes.

**Theorem 4.** Let \(S\) be any finite set of rational primes,
and \(r\in\{3,-3,-2,-1\}\). There are infinitely many
nonnegative integers \(n\equiv r\bmod M\) such that \(a_n\)
is a square in \(\mathbb Q_p\) for every \(p\in S\).
For \(r=-1,-2,-3\), this statement also holds with squares
replaced by \(k\)-th powers for any fixed integer \(k\ge2\).

**Proof.** Choose a positive multiple \(h\) of \(M\) such that
\(T^h\) is congruent to the identity modulo sufficiently high powers
of every prime in \(S\); this is possible because \(T\) is
invertible modulo all those powers. For the nonzero anchors,
\(a_{r+ht}\) can be kept in an arbitrarily small neighborhood of
\(a_r\) in every \(\mathbb Q_p\), for all integral \(t\).
The nonzero \(k\)-th powers form an open subgroup of
\(\mathbb Q_p^\times\) (for example by Hensel's lemma applied
near 1), and the relevant \(a_r\) is itself a \(k\)-th power.
This proves the statement for these anchors.

For the zero anchor, put
\(\alpha=(1+\sqrt5)/2,\ \beta=1+\sqrt2\) and \(c=1/(2\sqrt2)\).
At any \(p\in S\), choose an embedding of the biquadratic number
field into an algebraic closure of \(\mathbb Q_p\).
By increasing \(h\) by a common multiple if necessary, we may
assume \(\alpha^h,\beta^h\) lie in the disk where the \(p\)-adic
logarithm and exponential are inverse, and \(h\) is even.
The analytic interpolation
\[
 f_p(t)=\ell\exp(t\log(T^h))s\in\mathbb Q_p
\]
near \(t=0\) has \(f_p(0)=0\) and, by the Binet expressions,
\[
 f'_p(0)=\sqrt5\log(\alpha^h)
           -\frac1{\sqrt2}\log(\beta^h).
\]
The two logarithms are linearly independent over \(\mathbb Q\).
A rational relation would yield an integer relation, and applying
the exponential (or injectivity of the logarithm on its disk)
would give a multiplicative dependence of \(\alpha^h,\beta^h\).
Those units are multiplicatively independent: conjugating a
relation in the biquadratic number field by the automorphism
inverting \(\alpha^h\) and fixing \(\beta^h\) forces the first
exponent, and then the second, to be zero.
The Baker–Brumer theorem [1] extends the logarithmic linear
independence from \(\mathbb Q\) to algebraic coefficients.
Consequently \(C_p=f'_p(0)\ne0\).

For all sufficiently small nonzero \(t\) in \(\mathbb Q_p\),
\(f_p(t)/(C_pt)\) lies in the open subgroup of \(k\)-th powers,
because it converges to 1. Choose
\(t_p=C_p^{-1}p^{kN_p}\) with \(N_p\) sufficiently large.
Then \(f_p(t_p)\) is a nonzero \(k\)-th power.
By continuity there is an open neighborhood of \(t_p\) contained
in \(\mathbb Z_p\) on which the same holds. This neighborhood
contains an entire residue class of ordinary integers modulo a
power of \(p\). The Chinese remainder theorem combines these
classes for the primes in \(S\) into one integer arithmetic
progression. Taking its arbitrarily large positive members \(t\)
gives the required indices \(n=-1+ht\). For integral \(t\),
the analytic interpolation agrees with the matrix recurrence.
QED.

This rules out completing any of the four branches using a
fixed finite prime set, even if every prime power is allowed.
The theorem does not rule out a variable-prime argument, in which
the obstructing prime is allowed to depend on the candidate index.

## Verification

Run:

    python3 verify_local_geometry.py

The certificate checks all matrix constants, the 24-digit 5-adic
root and the valuation/unit formulas on 569 sample indices.
The analytic arguments establish the formulas at all indices,
independently of the sample tests.

## Reference

[1] A. Brumer, On the units of algebraic number fields,
Mathematika 14 (1967), 121–124.
For a modern statement see S. Dasgupta, Ranks of matrices of
logarithms of algebraic numbers I, Essential Number Theory 2
(2023), Theorem 1.2. https://msp.org/ent/2023/2-1/ent-v2-n1-p05-p.pdf
