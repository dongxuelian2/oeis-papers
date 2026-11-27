# A global square-class obstruction from 838 local characters

Let \(a_n=L_n+P_n\) be A060405. This note strengthens the
zero-anchor branch \(n\equiv-1\pmod{720720}\) without imposing
a smoothness or saturation assumption on the candidate offset.

## Theorem

Let \(F\) be the set of 832 primes obtained by the five forcing
rounds in extension.md, with the search restricted to primes
\(17\le p<30000\). Put
\[
 D=720720\prod_{p\in F}p,\qquad E=7\cdot11\cdot13\prod_{p\in F}p.
\]
For any nonnegative square index \(n\equiv-1\pmod{720720}\),
write \(k=n+1\). Then \(D\mid k\), and there is a positive
squarefree integer \(d\), coprime to \(D\), and \(\delta\in\{0,1\}\)
such that
\[
 k=5^\delta E d\,y^2
 \qquad (y\in\mathbb Z_{>0}).
\]
Moreover \(d\equiv17\pmod{24}\) if \(\delta=0\), and
\(d\equiv13\pmod{24}\) if \(\delta=1\).
The integer \(d\) has a prime divisor at least 9857.

In particular every such square index has an additional prime
of odd valuation in \(n+1\), outside the support of the previously
certified 3230-digit forced divisor \(D\). The new assertion holds
for arbitrarily large indices; it is not a finite search for squares.

## 1. Exact local square classes

Write \(T=\operatorname{diag}(A,B)\), with the recurrence matrices
in smooth-support.md. For each forced prime \(p\in F\), the
forcing certificate supplies a positive integer \(h_p\mid D\)
with \(p\nmid h_p\), \(T^{h_p}\equiv I\pmod p\) and
\(v_p(a_{h_p-1})=1\).
Set \(c_p=a_{h_p-1}/h_p\). Lemma 2 of smooth-support.md
applies with \(e=1\) and matrix depth at least one. It proves
\[
 a_{k-1}\in\mathbb Q_p^{\times2}
 \quad\Longleftrightarrow\quad c_p k\in\mathbb Q_p^{\times2}
 \qquad(h_p\mid k).
\]
In particular, \(v_p(c_p)=1\) and \(v_p(k)\) must be odd.
The unit residue of \(c_p\) is computed exactly modulo \(p\)
from \(a_{h_p-1}\) modulo \(p^2\).

The same lemma applies at the base primes \(2,3,7,11,13\)
using \(h_p=48,24,336,1320,2184\), respectively, all of
which divide 720720. The verified valuation parities of
\(c_p\) are \(0,0,1,1,1\), respectively.
At 2 its unit is 3 modulo 8; at 3 its unit is 2 modulo 3.

Let \(S=F\cup\{2,3,7,11,13\}\).
The valuation conditions at \(S\) force the squarefree kernel
of \(k\) to have the form \(5^\delta E d\) with \(d\) coprime
to \(D\). No condition at 5 is needed here: both possibilities
for its valuation parity are retained. Thus all candidates
satisfy
\[
 c_p5^\delta E d\in\mathbb Q_p^{\times2}\qquad(p\in S).
\]
The exact certificate gives \(E\equiv3\pmod8\) and
\(E\equiv1\pmod3\). The unit conditions at 2 and 3 give
\(d\equiv17\pmod{24}\) for \(\delta=0\), and
\(d\equiv13\pmod{24}\) for \(\delta=1\).

## 2. The binary linear system

For any positive odd integer \(u\) coprime to all primes in
\(S\), define a character vector \(\chi(u)\in\mathbb F_2^{838}\).
The first two bits are
\[
 \mathbf1_{u\equiv3\bmod4},\qquad
 \mathbf1_{u\bmod8\in\{3,5\}}.
\]
The remaining 836 bits, ordered by increasing odd prime
\(p\in S\), are zero or one according as the Legendre
symbol \((u/p)\) is \(+1\) or \(-1\).
These bits are additive under multiplication of integers
coprime to \(S\), since the defining quadratic characters
are multiplicative.

Define a target vector \(b\) by the same characters of
the local units \(u_p(c_p)u_p(E)\), using the corresponding
unit at each place. The valuation conditions have already
been satisfied by \(E\). The remaining unit conditions
are exactly
\[
 \delta\chi(5)+\sum_{q\mid d}\chi(q)=b.
\]
This equivalence holds for the tests at \(S\), not for the
full global square problem.

## 3. Exact separating certificate

Suppose every prime divisor of \(d\) is less than 9857.
The eligible columns are \(\chi(5)\) and \(\chi(q)\) for
each prime \(q<9857\) with \(q\nmid D\).
The independent verification program
verify_forced_signatures.py reconstructs the five rounds
of forced primes, evaluates the local units and all eligible
columns, and obtains:
* 838 rows and 836 eligible columns, including the column for 5;
* column rank 835;
* a target vector of Hamming weight 379;
* a dual vector \(w\) of Hamming weight 420 with
  \(w\cdot b=1\), but \(w\cdot\chi(q)=0\) for every
  eligible column.

The dual vector is stored as a hexadecimal integer, with
the least significant bit corresponding to the first
character. The program checks every dot product directly.
It also verifies that both bits for the prime 2 are zero
in \(w\), so the obstruction can equivalently be expressed
as a single Jacobi character involving 420 distinct odd
test primes. In particular that character has value
\(-1\) on \(d\), while it has value \(+1\) on 5 and all
eligible outside primes less than 9857.

Taking the dot product of the necessary linear system with
\(w\) produces the contradiction \(0=1\).
Therefore \(d\) contains at least one prime divisor
\(q\ge9857\), as claimed. Its valuation in \(k\) is odd
by the definition of the squarefree kernel.

The certificate also checks that adding the column for
9857 makes this particular binary linear system consistent.
This does not supply a square index; it identifies the
exact limit of this bound with these fixed local conditions
and unrestricted use of the eligible squarefree factors.

## Reproduction

Run:

    python3 verify_forced_signatures.py

This uses only the Python standard library and the exact
matrix routines in verify_smooth_support.py. It checks the
complete forced-prime construction and the separating dual
certificate without constructing the large recurrence values.

The full square classification remains unresolved. The new
constraint is independent of an upper bound on \(n\).
