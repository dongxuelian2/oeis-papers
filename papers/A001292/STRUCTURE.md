# Exact power equations at integer-block boundaries

These are structural necessary conditions, **not a proof of Kashihara's
conjecture**. They retain the actual integer-block cut and apply to every prime
exponent. No bound on all the remaining parameters is asserted.

Put \(W_0=0\), \(D(0)=0\), and let \(D(k)\) count the decimal digits of \(W_k\).
If \(R=x^e>1\), and a prime \(p\) divides \(e\), then

\[
R=(x^{e/p})^p.
\]

Thus exclusion for every **prime exponent** suffices. This does not bound those
primes independently of \(R\).

## 1. Exact identities

Writing \(W_m=P10^{D(m)-D(j)}+Q\), with \(P=W_j\), gives

\[
R_{m,j}=Q10^{D(j)}+P
 =10^{D(j)}W_m-(10^{D(m)}-1)W_j.                 \tag{1}
\]

Here \(j\) counts whole integers, not digits. Every integer block starts with a
nonzero digit, so these operations preserve the full length \(D(m)\).

Fix \(d\ge1\), and write \(B=10^d\), \(L=10^{d-1}\), \(b=B-1\),

\[
A_d=b^2W_{L-1}+Lb+1,\qquad C_k=(k+1)b+1.
\]

For every \(L-1\le k\le B-1\), with \(t=k-L+1\),

\[
\boxed{b^2W_k+C_k=A_dB^t.}                    \tag{2}
\]

Indeed the left side at \(k=L-1\) is \(A_d\). On appending the next \(d\)-digit
integer, \(W_{k+1}=BW_k+(k+1)\), and direct subtraction shows that the left side
is multiplied by \(B\). This proves (2), including the empty appended interval.
The case \(d=1,k=0\) uses \(W_0=0\) and \(A_1=10\).

For all rotations it is useful to index by the **final integer** \(k\). Define

\[
F_{m,k}=(k+1)\Vert\cdots\Vert m\Vert1\Vert\cdots\Vert k,
\quad 1\le k\le m,
\]

where \(F_{m,m}=W_m\). Thus \(F_{m,k}=R_{m,k}\) for \(k<m\), while \(k=m\)
represents \(j=0\). Let \(T_{m,k}=(k+1)\Vert\cdots\Vert m\), taking
\(T_{m,m}=0\). In this paragraph \(d\) is the digit length of **\(k\)**; the
integer \(m\) may have more digits. Set

\[
H_{m,k}=A_d+b^2 T_{m,k}10^{D(L-1)}.
\]

Since \(F_{m,k}=T_{m,k}10^{D(k)}+W_k\) and
\(D(k)=D(L-1)+dt\), equation (2) gives

\[
\boxed{b^2F_{m,k}+C_k=H_{m,k}B^t,\qquad t=k-L+1.}       \tag{3}
\]

Equivalently \(H_{m,k}=b^2U+Lb+1\), where
\(U=T_{m,k}\Vert W_{L-1}\), and the concatenation with the empty word \(W_0\)
means \(U=T_{m,k}\). In particular \(H_{m,m}=A_d\). Formula (3) imposes no
same-digit-length assumption on the interval \(k+1,\ldots,m\).

If \(k\) and \(m\) both have \(d\) digits, the remaining concatenation can
also be eliminated exactly:

\[
b^2T_{m,k}=C_kB^{m-k}-C_m,\qquad
H_{m,k}=A_d+10^{D(L-1)}(C_kB^{m-k}-C_m).
\]

This follows by telescoping the same fixed-digit recurrence as (2).

## 2. Exact valuations of the coefficient

For every \(d\ge2\),

\[
\boxed{v_2(A_d)=d,\qquad v_5(A_d)=d-1.}               \tag{4}
\]

To prove this, put \(c=10^{d-1}\). Apply (2) for digit length \(d-1\) at its
last endpoint \(c-1\); there are \(9c/10\) integers in that digit block. An exact
polynomial subtraction yields

\[
(c-1)^2A_d
 =(10c-1)^2A_{d-1}c^{9c/10}
   -9c(10c^3-11c^2+12c-2).                         \tag{5}
\]

The cubic in parentheses is \(2\pmod4\) and \(3\pmod5\). The second term in
(5) consequently has valuations \(d\) and \(d-1\). The first term has both
valuations at least \((d-1)9c/10>d\). Also \(c-1\) is a unit at both primes.
The unequal-valuation rule for a sum proves (4), without induction assumptions
on the valuations of \(A_{d-1}\).

An independent verification uses only the last two integer blocks. For
\(d\ge3\), \(W_{c-1}\equiv(c-2)c+(c-1)\equiv-c-1\pmod{c^2}\), so
\(A_d\equiv18c\pmod{c^2}\). Since \(v_2(c^2)>d\) and
\(v_5(c^2)>d-1\), this gives (4) again. The remaining case is
\(A_2=1209999989980\), whose valuations are 2 and 1.

For \(d\ge2\), \(D(L-1)>d\): for \(d=2\) it equals 9, and for \(d\ge3\) it is
at least \(10^{d-1}-1>d\). Therefore the extra term defining \(H_{m,k}\) has
strictly higher 2-adic and 5-adic valuations. Hence, uniformly for \(m\ge k\ge10\),

\[
\boxed{v_2(H_{m,k})=d,\qquad v_5(H_{m,k})=d-1.}        \tag{6}
\]

In particular \(H_{m,k}10^r\) is not a perfect power for any integer \(r\ge0\):
its two valuations are consecutive. This assertion concerns the coefficient
and does **not** exclude \(F_{m,k}\) in (3).

## 3. A necessary convergent for every exponent

**Proposition.** Suppose \(m\ge11\), \(1\le k\le m\), and \(F_{m,k}=x^e\)
with \(x\ge2\), \(e\ge2\). Use the parameters of (3), and write

\[
dt=en+s,\quad 0\le s<e,\quad Q=10^n,\quad
a=b^{e-2}H_{m,k}10^s,\quad c_0=b^{e-2}C_k.
\]

Let \(y=bx\), \(g=\gcd(y,Q)\), \(P=y/g\), \(q=Q/g\). Then

\[
\begin{gathered}
y^e=aQ^e-c_0,\qquad g^e\mid C_k,\qquad b\mid P,\\
q=2^u5^v,\qquad
0<a^{1/e}-\frac Pq<\frac{1}{2Q^e}\le\frac{1}{2q^2}.
\end{gathered}                                                   \tag{7}
\]

The number \(a^{1/e}\) is irrational, and \(P/q\) is one of its lower regular
continued-fraction convergents. The statement allows \(n=0\), so \(Q=q=1\).

**Proof.** Multiplying (3) by \(b^{e-2}\) gives the equation in (7). Since \(g\)
has only prime factors 2 and 5 and \(b\) has neither, \(g^e\mid c_0\) implies
\(g^e\mid C_k\), and division by \(g\) preserves \(b\mid P\).

We first check the strict bound

\[
H_{m,k}>b^2,\qquad \sqrt{H_{m,k}}>2C_k.                \tag{8}
\]

For \(d\ge2\), \(C_k\le B^2-B+1<B^2\) and \(H_{m,k}\ge A_d>b^2W_{L-1}\).
The elementary bound \(D(L-1)\ge2d+3\) holds at \(d=2\) directly, and for
\(d\ge3\) follows from \(D(L-1)\ge10^{d-1}-1\ge2d+3\). Thus
\(W_{L-1}\ge100B^2\), while \(b>B/2\). These inequalities give
\(H_{m,k}>25B^4>4C_k^2\).
For \(d=1\), \(k\le9\) and \(m\ge11\) imply \(T_{m,k}\ge1011\), so
\(H_{m,k}=81T_{m,k}+10\ge81901>4\cdot91^2\ge4C_k^2\).
This also proves \(H_{m,k}>b^2\).

Put \(\alpha=a^{1/e}\), \(z=y/Q>0\). Factoring \(\alpha^e-z^e=c_0/Q^e\)
over the positive reals gives

\[
0<\alpha-z
 <\frac{c_0}{\alpha^{e-1}Q^e}
 \le \frac{C_k}{\sqrt{H_{m,k}}Q^e}
 <\frac1{2Q^e}.
\]

The middle inequality follows from \(10^s\ge1\) and

\[
\frac{b^{(e-2)/e}}{H_{m,k}^{(e-1)/e}}
 =\frac b{H_{m,k}}
   \left(\frac{H_{m,k}}{b^2}\right)^{1/e}
 \le\frac1{\sqrt{H_{m,k}}}.
\]

If \(\alpha\) were rational, the integral \(a\) would force \(\alpha\) to be an
integer. Then \(0<\alpha-y/Q\) would be at least \(1/Q\), contradicting the
strict bound just proved. Thus \(\alpha\) is irrational. Legendre's convergent
criterion applied to the reduced fraction \(P/q\) proves the proposition.
For \(d\ge2\), irrationality also follows independently from (6): the
valuations of \(a\) at 2 and 5 are \(d+s\) and \(d-1+s\).

All cases \(2\le m\le10\) can be checked directly for every prime exponent
less than the bit length of each rotation, as in the accompanying checker.
This is a finite boundary check, not a reduction of the unbounded problem.

## 4. Exact remaining obstruction

Even for \(j=0,e=2\), equation (2) asks to exclude

\[
((10^d-1)x)^2+C_m=A_d10^{d(m-10^{d-1}+1)}
\]

uniformly in \(d\) and \(m\). Consecutive valuations of the main term do not
control its distance from a square after subtracting \(C_m\). Proposition (7)
replaces a hypothetical power by a convergent with a restricted denominator;
it supplies no uniform bound or exclusion for these convergents as \(d,m,k,e\)
vary. Both the algebraic number and its height vary. Finiteness for one fixed
algebraic number, even if available, would not finish this task.

The suffix constraint alone also cannot close the gap. For instance \(W_{41}\)
is odd, \(W_{41}\equiv1\pmod8\), and \(W_{41}\equiv1\pmod5\). It has square
roots modulo every power of 10. The checker constructs an exact square ending
in the **entire** word \(W_{41}\); its coefficient in (3) still has valuations
2 and 1. Its extra prefix is arbitrary, so it is **not** an A001292
counterexample. Any successful use of (3) must exploit the exact prefix
\(T_{m,k}=(k+1)\Vert\cdots\Vert m\), beyond its size or its terminal suffix.

## Sources and checks

Run `python verify_structure.py`. It checks the old routines against literal
rotations, (2), (3), (5), coefficient valuations, the finite small cases, and
exact power extensions that test the bound in (7). The proofs above establish
the unbounded statements; finite tests do not.

The three theorems in [RESIDUE_EXCLUSIONS.md](RESIDUE_EXCLUSIONS.md) survive independent
algebraic checking: the mod-27 double sum, the valuation-2 square exclusion,
and the mod-13 block table. In the third theorem the affine transition matrix
has period dividing 78 modulo 13: its eigenvalues are \(10^d,1,1\); if
\(10^d=1\), its unipotent part has nilpotence index at most 3, less than 13.
This justifies dependence on the appended length modulo both 6 and 13.

The fixed-block summation and lifting identities in
[A075000--A075002](../A075000-A075002/A075000-A075002.tex) are compatible with
(2). Their existence theorem also explains a limitation: any fixed finite set
of congruence tests admits infinitely many unrotated prefixes divisible by
their common modulus, hence passing the zero-residue test for every exponent.
This is not evidence that any such prefix is a perfect power.

Literature checked on 2026-10-17:

- [OEIS A001292](https://oeis.org/A001292) defines whole-block cyclic rotations.
- Ripà, [arXiv:2205.10163v4](https://arxiv.org/html/2205.10163v4), proves the
  mod-9 exclusions and reports the finite check through \(m=447\). The paper's
  bound is \(10^{1235}\); the OEIS comment currently prints \(10^{1035}\).
- Ripà's [2025 GPT-5 paper](https://www.ai.vixra.org/pdf/2508.0054v1.pdf)
  treats the trailing-digit frequency question, not the perfect-power problem.
- Ripà's [2025 note](https://zenodo.org/records/17382562) treats rotation
  congruences and divisibility patterns. Its general periodicity assertions
  are not used in the proofs above.

No claim of literature-wide novelty or a complete solution is made.
