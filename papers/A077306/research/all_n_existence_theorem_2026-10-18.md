# OEIS A077306: a constructive nonvanishing theorem for every index

**Status: alternative explicit elementary construction (October 18, 2026). This is an ALREADY SOLVED OEIS existence problem, not a novel independent conjecture.**

[OEIS A077306](https://oeis.org/A077306) is the smallest positive
integer divisible by \(n\) that consists of the decimal concatenation
of **exactly \(n\) consecutive positive integers**, or 0 if none exists.

## Theorem

For every integer \(n\ge1\), the defining set of A077306 is nonempty.
In fact, there exist infinitely many integers \(k\ge1\) for which

\[
\boxed{n\mid \operatorname{concat}(k,k+1,\ldots,k+n-1).}
\]

More concretely, write
\[
n=s m,\qquad s=2^\alpha5^\beta,\quad\gcd(m,10)=1.
\]
Let \(d\) be any sufficiently large positive integer satisfying

\[
\boxed{s\mid10^d,\qquad 10^d\equiv1\pmod m,\qquad
 9\cdot10^{d-1}>n+s.}\tag{1}
\]

When \(m=1\), the middle condition is vacuous. Such \(d\) exist:
take a sufficiently large multiple of
\(\operatorname{ord}_m(10)\), with
\(\operatorname{ord}_1(10):=1\).
Set

\[
\boxed{k=10^d-n-s+1.}\tag{2}
\]

Then the decimal integer obtained by concatenating
\(k,k+1,\ldots,k+n-1\) is divisible by \(n\).

### Proof

The last member of the block is

\[
k+n-1=10^d-s.
\]

By the third inequality in (1),
\[
10^{d-1}<k\le k+n-1<10^d.
\]
(Also \(s\ge1\), ensuring the last strict inequality.)
Thus **all \(n\) integers have precisely \(d\) decimal digits**.

Write \(q=10^d\), so the concatenation has the exact integer form

\[
N=\sum_{j=0}^{n-1}(k+j)q^{n-1-j}.\tag{3}
\]

Modulo \(s\), \(q\equiv0\). Every summand except
the last vanishes, giving

\[
N\equiv k+n-1=10^d-s\equiv0\pmod s.\tag{4}
\]

Modulo \(m\), \(q\equiv1\), so

\[
N\equiv\sum_{j=0}^{n-1}(k+j)
=nk+\frac{n(n-1)}2\pmod m.\tag{5}
\]

Now \(m\mid n\) and \(m\) is odd. Therefore
\(m\mid n(n-1)/2\), as 2 is invertible modulo \(m\)
(or directly, \(n(n-1)/2=m\cdot[s(n-1)/2]\)
with the bracket interpreted modulo the odd modulus).
Thus \(N\equiv0\pmod m\).

As \(\gcd(s,m)=1\), (4)--(5) imply \(n=sm\mid N\).
There are arbitrarily many admissible \(d\), and
their \(k\)'s strictly grow, hence infinitely many
different such concatenations. QED.

### Concrete illustration

For \(n=12=4\cdot3\), take \(d=2\), so
\(10^2\equiv0\pmod4\), \(10^2\equiv1\pmod3\).
Equation (2) gives \(k=100-12-4+1=85\).
Thus
\[
N=85\Vert86\Vert87\Vert\cdots\Vert96.
\]
Modulo 4 only the last two-digit block matters,
and \(96\equiv0\pmod4\).
Modulo 3 the concatenation reduces to the ordinary
sum \(85+\cdots+96=1086\equiv0\pmod3\).
Hence \(12\mid N\).

### General principle and reuse

The proof uses the same *uniform digit-window /
smooth-prime decomposition / Chinese remainder*
mechanism developed for decimal concatenation
research, but **does not need** any of the difficult
zero-drift monodromy machinery for A077187.

In base \(B\), a direct analogue works for any
\(n=s m\) where every prime divisor of \(s\) divides
\(B\), \(\gcd(m,B)=1\), and **\(m\) is odd**.
Indeed a sufficiently large \(q=B^d\) satisfies
\(s\mid q\) and \(q\equiv1\pmod m\), after which
the same proof applies. For decimal \(B=10\),
the coprime part \(m\) is automatically odd.

This proves that **A077306 has no zero terms**.
It does not identify the **smallest** concatenation
for each \(n\); the construction is an explicit,
usually nonminimal witness.

### Reproducibility

Run, from the repository root:

    python3 papers/A077306/research/audit_universal_witness.py

The audit independently computes the modular digit
concatenations for \(1\le n\le1000\) and checks
the proposed \(k\), both mod its smooth part and
its coprime part. This is a verification of the formula,
**not** the logical basis of the all-\(n\) theorem.

### Priority and cross-reference clarification

OEIS A075001 asks for the *least starting index* k of a
length-n consecutive-integer concatenation divisible by n.
Its all-n existence conjecture **was already proved and credited
to Qichao Wang (2026) in A075001**, before this note.
OEIS A077306 asks for the *least concatenated integer* arising
from the same starting-index search; its positivity is therefore
logically equivalent to A075001 positivity. OEIS A075000 records
the corresponding smallest concatenated integer divided by n.

This short CRT construction is an **alternative, explicit proof**
and yields a convenient closed-form witness and infinitely many
witnesses, **not an additional independent solved OEIS problem**.
Do not claim new priority or submit it as an uncredited proof of an
open conjecture. Existing proof: https://oeis.org/A075001 .
