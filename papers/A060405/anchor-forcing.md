# Four-anchor divisibility forcing for A060405

Let \(a_n=L_n+P_n\), extended to all integer indices. This note
reduces the square problem to four congruence branches and develops
a general lifting rule for all four, including the three nonzero
square anchors that are outside the scope of the zero-anchor
valuation argument in extension.md.

## Theorem 1. Four global branches

If \(a_n\) is an integer square, then
\[
n\equiv 3,-3,-2,-1\pmod {720720}.
\]

**Proof.** Let \(M=720720\). The original exact certificate leaves
the six residues \(3,360357,360363,720717,720718,720719\).
Modulo the prime \(q=2081\), the two recurrence matrices have
common period 2080, which divides \(2M\).
For each old residue \(r\), there are only two cases to test,
\(r\) and \(r+M\) modulo 2080. Modular matrix exponentiation gives

| \(r\) | \(a_r\bmod2081\) | \(a_{r+M}\bmod2081\) |
|---:|---:|---:|
| 3 | 9 | 2080 |
| 360357 | 760 | 1313 |
| 360363 | 1321 | 768 |
| 720717 | 2072 | 1 |
| 720718 | 5 | 1 |
| 720719 | 2079 | 0 |

The four entries in the second and third rows are quadratic
nonresidues: their 1040th powers modulo 2081 equal 2080.
Thus both exceptional classes are excluded for all integer indices.
The remaining classes are the four in the statement. QED.

## Theorem 2. Anchor lifting lemma

Consider any integral sequence with a finite period \(h_q\)
modulo each test prime \(q\). Suppose \(a_r\) is an integer square
and a candidate square index is known to satisfy \(D\mid n-r\).
For a prime \(p\), choose finitely many odd primes \(q\) with
\(h_q\mid pD\). Define
\[
C_{r,D,p}=\bigcap_q
\{t\in\{0,\ldots,p-1\}:a_{r+Dt}\text{ is a square modulo }q\}.
\]
If \(C_{r,D,p}=\{0\}\), then \(pD\mid n-r\).

**Proof.** Write \(n=r+Dk\). The period condition gives
\(a_n\equiv a_{r+D(k\bmod p)}\pmod q\) for every selected prime.
Since \(a_n\) is a square, \(k\bmod p\in C_{r,D,p}\).
The only possibility is zero. QED.

The lemma applies to any integer square anchor, not just a zero.
It also applies when \(p\mid D\), in which case it increases the
required exponent of \(p\). If distinct primes \(p_1,\ldots,p_s\)
are forced at the same \(D\), the resulting conclusions combine
to give \(D p_1\cdots p_s\mid n-r\).

### Persistence under stronger input divisibility

If a multiplier \(p\) is certified at \(D\) and \(D\mid E\),
either \(pD\mid E\), or the same moduli certify \(pE\).
Indeed, in the latter case \(E/D\) is invertible modulo \(p\),
and multiplication by it permutes the candidate values of \(t\).
Thus old forcing certificates remain usable during recursive
lifting. Any unbounded chain of certified divisors on a branch
implies \(n=r\) on that branch. For negative anchors this would
exclude the entire nonnegative branch.

## Theorem 3. Complete square classification through \(10^{322}\)

For every integer \(n\) with \(0\le n\le10^{322}\),
\[
a_n\text{ is a square}\quad\Longleftrightarrow\quad n=3.
\]

**Proof.** By Theorem 1 each possible square index has
\(D=M\mid n-r\) for exactly one anchor \(r\in\{3,-3,-2,-1\}\).
The four anchor values are respectively \(9,1,1,0\).

The certificate verify_anchor_forcing.py constructs exact periods
for all 9589 primes \(5<q<100000\). For each such prime, both
recurrence matrices have distinct nonzero eigenvalues over
\(\mathbb F_{q^2}\): their characteristic discriminants are 5
and 8. Consequently \(q^2-1\) is a common period. Removing factors
by modular matrix exponentiation gives a verified common period
\(h_q\).

At each round, group test primes by
\(f=h_q/\gcd(D,h_q)\), retaining prime multipliers \(f\le1000\).
For each group with at least two test primes, test all \(f\)
possible lifts using Euler's criterion; zero residues count as
squares. When the intersection is the singleton zero, apply
Theorem 2 with \(p=f\).
Combine the resulting distinct multipliers simultaneously.

Three rounds give the following exact certificate sizes:

| Anchor | Round 1: multipliers / digits | Round 2 | Round 3 |
|---:|---:|---:|---:|
| 3 | 53 / 109 | 82 / 314 | 20 / 365 |
| -3 | 43 / 86 | 92 / 312 | 20 / 365 |
| -2 | 46 / 93 | 72 / 263 | 25 / 323 |
| -1 | 52 / 107 | 86 / 321 | 21 / 374 |

The final divisors \(D_r\) all exceed \(10^{322}+3\).
For \(0\le n\le10^{322}\), the divisibility \(D_r\mid n-r\)
therefore implies \(n=r\). Only the anchor 3 is nonnegative,
and \(a_3=9\). QED.

The full integer \(D_r\) for each anchor is printed by the program.
The certificate uses exact integer arithmetic and tests complete
residue sets, without computing large terms of the recurrence.
The zero-anchor valuation certificate in extension.md independently
gives an even larger divisor for \(n+1\).

## Research frontier

The remaining global problem is whether each anchor admits an
unbounded chain of certified divisors, or whether another
index-dependent obstruction can exclude its nonzero offsets.
Finite congruence computations cannot eliminate a whole
neighborhood of an actual integer square anchor. The lifting
lemma isolates a sufficient arithmetic mechanism for the full
classification; its unboundedness is not established here.

## Reproduction

Run:

    python3 verify_anchor_forcing.py

The script also rechecks the original six-residue certificate.
