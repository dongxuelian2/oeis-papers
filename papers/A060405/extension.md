# Sparse congruence lifting and recursive prime forcing

Write \(a_n=L_n+P_n\), and extend both recurrences to integer indices.
The initial certificate gives six possible residue classes modulo
\(M=720720\). This note strengthens the finite exclusion and proves
additional local structure on the branch \(n\equiv-1\pmod M\).

## 1. Square classification through \(10^{18}\)

**Theorem.** For every integer \(0\le n\le10^{18}\), \(a_n\) is a square
if and only if \(n=3\).

Proof. If the current list of surviving residues is \(R\subset[0,D)\)
and a new square-residue condition has period \(h\), set
\(f=h/\gcd(h,D)\). The complete list of candidates modulo
\(\operatorname{lcm}(D,h)=fD\) is
\[
 \{r+jD:r\in R,\ 0\le j<f\}.
\]
Retain a candidate exactly when its value passes the new modular test.
The state period is certified by return to the initial state under
an invertible recurrence.

Starting with the six classes modulo \(M\), the 30 additional moduli in
EXT of verify_extension.py give 722 surviving classes modulo
3020727790080000. These contain exactly 239014 indices in the desired
interval. The 26 moduli in TAIL eliminate every one except 3.
Directly \(a_3=9\). All calculations use finite exact modular arithmetic.
The attached executable certificate verifies the counts and the final
singleton. QED.

## 2. A local prime-forcing lemma

Use the block diagonal matrix
\[
 T=\operatorname{diag}\left(
 \begin{pmatrix}0&1\\1&1\end{pmatrix},
 \begin{pmatrix}0&1\\1&2\end{pmatrix}\right),
 \qquad s=(-1,2,1,0)^{\mathsf T},
 \qquad \ell=(1,0,1,0).
\]
Then \(a_{-1+k}=\ell T^k s\) and \(\ell s=0\).

**Lemma.** Let \(p\) be an odd prime and \(h\ge1\) such that
\(T^h\equiv I\pmod p\) and \(v_p(a_{h-1})=1\).
For every positive integer \(t\),
\[
 v_p(a_{ht-1})=1+v_p(t),\qquad
 \frac{a_{ht-1}}{p^{1+v_p(t)}}\equiv
 \frac{a_{h-1}}p\frac{t}{p^{v_p(t)}}\pmod p.
\]
In particular, if \(a_{ht-1}\) is a square, \(v_p(t)\) is odd.

Proof. Write \(T^h=I+pB\) with integral \(B\).
The binomial theorem and \(\ell s=0\) give
\[
 a_{ht-1}=t\,a_{h-1}+
 \sum_{j=2}^t\binom tj p^j\ell B^j s.
\]
Since \(j\binom tj=t\binom{t-1}{j-1}\), each summand has valuation
at least \(v_p(t)+j-v_p(j)\ge v_p(t)+2\) for odd \(p\).
The first summand has valuation \(v_p(t)+1\), proving both claims. QED.

## 3. Recursive forced divisors of \(n+1\)

Suppose \(a_n\) is a square and \(n\equiv-1\pmod M\).
Start with \(D=M\). For any odd prime \(p\nmid D\), choose
\(h=\gcd(D,p^2-1)\). If
\[
 T^h\equiv I\pmod p,\qquad a_{h-1}\not\equiv0\pmod{p^2},
\]
then \(h\mid n+1\) and \(p\nmid h\). The lemma forces \(p\mid n+1\),
indeed to odd valuation. Thus replace \(D\) by \(pD\). Every such
replacement preserves the necessary condition \(D\mid n+1\).
Multiple qualifying primes can be added simultaneously.

The certificate searches the primes \(17\le p<30000\) using modular
matrix exponentiation. Five successive rounds yield:

| Round | New distinct primes | Digits of forced divisor |
|---:|---:|---:|
| 1 | 38 | 112 |
| 2 | 263 | 1102 |
| 3 | 338 | 2438 |
| 4 | 161 | 3098 |
| 5 | 32 | 3230 |

**Corollary.** Every square index in the residue class \(-1\bmod M\)
has \(n+1\) divisible by the explicitly reproducible 3230-digit
integer \(D\), whose factorization includes 832 distinct primes
in \([17,30000)\), all occurring to odd valuation in \(n+1\).
In particular \(n+1>10^{3229}\).

This forcing procedure is a closure under a sufficient local
divisibility rule, not an assumption about the distribution of primes.
The five rounds are finite certificates. Proving that a closure
without the prime search cutoff must be infinite would exclude this
entire branch; that statement remains open in this work.

## 4. Exact 2-adic condition on the same branch

The matrices satisfy \(T^{48}\equiv I\pmod{16}\), and
\(a_{47}\equiv16\pmod{128}\), as checked by exact modular
exponentiation. For \(t\ge1\), write \(T^{48}=I+16B\).
In the binomial expansion of \(a_{48t-1}\), the terms with \(j\ge2\)
are divisible by \(2^{v_2(t)+7}\), because
\(4j-v_2(j)\ge7\). The linear term therefore gives
\[
 v_2(a_{48t-1})=4+v_2(t),\qquad
 \frac{a_{48t-1}}{2^{4+v_2(t)}}\equiv
 \frac{t}{2^{v_2(t)}}\pmod8.
\]
Consequently \(a_{48t-1}\) is a square in \(\mathbb Q_2\) exactly
when \(t\) is a square in \(\mathbb Q_2\): its valuation is even
and its odd part is 1 modulo 8. This applies to the entire
\(-1\bmod M\) branch since \(48\mid M\).

## Verification

Run `python3 verify_extension.py` in this directory. The program uses
only the Python standard library. It checks the original modular
certificate, the sparse CRT lifting, the complete interval exclusion,
the two 2-adic matrix identities and the five rounds of prime forcing.
The full nonnegative square classification still requires a global
argument for the remaining indices; the fixed-exponent finiteness
theorem alone supplies no effective upper bound.
