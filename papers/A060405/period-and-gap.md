# Exact scalar periods, composite lifting, and an elementary gap principle

Write \(a_n=L_n+P_n\), with the conventions in README.md. Let
\(F_n\) denote Fibonacci numbers and \(Q_n\) the half companion Pell
numbers, \(Q_0=Q_1=1\), \(Q_{n+2}=2Q_{n+1}+Q_n\).

## 1. Exact maximal modulus for a prescribed period

For \(h\ge1\), define
\[
 G(h)=\gcd_{0\le j<4}(a_{h+j}-a_j).
\]

**Theorem 1.** An integer \(m\ge1\) admits \(h\) as a period of
the scalar sequence \(a_n\bmod m\) if and only if \(m\mid G(h)\).
Furthermore,
\[
 G(h)=
 \begin{cases}
 1,&h\text{ odd},\\
 \gcd(L_k,2Q_k),&h=2k,\ k\text{ odd},\\
 \gcd(5F_k,2P_k),&h=2k,\ k\text{ even}.
 \end{cases}
\]
In particular,
\[
 G(\gcd(h,j))=\gcd(G(h),G(j)).
\]

**Proof.** The characteristic polynomial of \(a_n\) is
\(f(X)g(X)\), where \(f=X^2-X-1\), \(g=X^2-2X-1\).
It has degree four and constant coefficient 1. Consequently four
consecutive initial equalities suffice to certify a period, including
backward indices, giving the first equivalence.

The identity \((X-2)f+(1-X)g=1\), applied to the shift operator,
recovers the two components as
\(L=(1-E)g(E)a,\ P=(E-2)f(E)a\).
Thus a period of \(a\) modulo any integer is exactly a simultaneous
period of its two components. Equivalently,
\[
 G(h)=\gcd(L_h-2,L_{h+1}-1,P_h,P_{h+1}-1).
\]

Use \(A=\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)\)
and \(B=\left(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\right)\)
with initial columns \(s_L=(2,1)^\mathsf T\) and
\(s_P=(0,1)^\mathsf T\). The columns \(s_P,Bs_P\) form a unimodular
basis, so a period of the Pell state is a period of the full matrix.
For odd \(h\), the determinant condition implies the modulus divides 2;
but \(B\bmod2\) has order two. Hence \(G(h)=1\).

For \(h=2k\) and either matrix \(C=A,B\), use
\[
 C^{2k}-I=C^k(C^k-C^{-k}).
\]
Multiplication by the unimodular matrix \(C^k\) preserves the gcd
of the entries of an integer column. For odd \(k\), Cayley–Hamilton
and \(\det C^k=-1\) give \(C^k-C^{-k}=(\operatorname{tr}C^k)I\).
The respective traces are \(L_k,2Q_k\), and both initial columns
are primitive. This proves the second case.

For even \(k\), the determinant is 1, so
\(C^k-C^{-k}=2C^k-(\operatorname{tr}C^k)I\).
The identities \(A^k=F_kA+F_{k-1}I\) and
\(B^k=P_kB+P_{k-1}I\) give
\[
 (A^k-A^{-k})s_L=F_k(2A-I)s_L=F_k(0,5)^\mathsf T,
\]
\[
 (B^k-B^{-k})s_P=P_k(2B-2I)s_P=P_k(2,2)^\mathsf T.
\]
Their column gcds are \(5F_k,2P_k\), proving the last case.

Finally, a modulus admits both periods \(h,j\) exactly when it admits
their gcd, by the Euclidean algorithm on shifts. Apply the period
criterion to obtain the strong divisibility identity. QED.

### Complete one-step test for a chosen multiplier

Suppose a square index satisfies \(n=r+Dt\), where \(a_r\) is
an integer square. For any positive multiplier \(b\), the strongest
restriction on \(t\bmod b\) obtainable from all square-residue tests
whose scalar periods divide \(bD\) is precisely
\[
 t\bmod b\in
 \{j\in[0,b): a_{r+Dj}\text{ is a square modulo }G(bD)\}.
\]
Indeed every such modulus divides \(G(bD)\), and \(G(bD)\)
itself is a permitted modulus. This identity includes prime powers
and exceptional moduli at 5, without needing to approximate the
set of available periods by a prime search.

The formula identifies the arithmetic input needed for unbounded
period lifting: common factors of two independent binary
recurrences, with additional quadratic-residue information.
Primitive-divisor results for either component individually do
not guarantee primitive *common* divisors. Neither Theorem 1
nor the finite computations prove unboundedness of the closure.

## 2. Composite-period constraint propagation

Let \(q>5\) be a test prime, and \(h_q\) a verified common
matrix period modulo \(q\). Given \(D\mid n-r\), put
\(f_q=h_q/\gcd(D,h_q)\). The square condition gives a relation
on \(t=(n-r)/D\):
\[
 t\bmod f_q\in
 R_q=\{j\in[0,f_q): a_{r+Dj}\text{ is a square modulo }q\}.
\]
The prime-multiplier argument in anchor-forcing.md is a special
case. Here we intersect relations with the same modulus and
propagate necessary conditions between all relations with
overlapping prime-power factors.

For each prime \(p\) occurring in some \(f_q\), use a domain of
residues modulo the largest occurring power \(s_p\) of \(p\).
Initially every residue is permitted. For a relation on
\(t\bmod f\), delete domain values whose projections modulo
\(p^{v_p(f)}\) are absent from that relation. Conversely delete
relation values with a projection absent from the corresponding
domain. Iterate until no deletion occurs. Every actual integer
solution remains in every relation and domain throughout.
If \(V_p\) is the surviving domain then
\(\gcd(s_p,\{v:v\in V_p\})\mid t\). These divisors for distinct
primes multiply. This proves the soundness of each simultaneous
update \(D\leftarrow D\prod_p\gcd(s_p,V_p)\).
The propagation need not determine every globally feasible residue.

**Theorem 2.** For \(0\le n\le10^{341}\), the only square term
of A060405 is \(a_3=9\).

**Proof.** Start from the four anchors in anchor-forcing.md
with \(D=720720\). Use the 9589 test primes \(5<q<100000\).
Keep \(1<f_q\le2000\), omitting singleton groups with \(f_q>128\)
as a resource filter. Perform the sound propagation just described
and repeat after multiplying \(D\) by the forced prime powers.

The exact certificate verify_composite_lifting.py gives the
following numbers of decimal digits in the divisors after each
nontrivial round:

| Anchor | Round 1 | Round 2 | Round 3 | Round 4 | Final |
|---:|---:|---:|---:|---:|---:|
| 3 | 132 | 379 | 426 | 429 | 429 |
| -3 | 121 | 373 | 436 | 439 | 439 |
| -2 | 113 | 303 | 342 | — | 342 |
| -1 | 129 | 366 | 436 | — | 436 |

All four final divisors exceed \(10^{341}+3\), which is
checked explicitly, rather than inferred just from digit counts.
In the stated nonnegative interval the necessary condition
\(D\mid n-r\) forces \(n=r\); only \(r=3\) is nonnegative.
Direct calculation gives \(a_3=9\). QED.

The same calculation reaches a fixed point for the chosen
prime list, resource filter and propagation algorithm; it
does not assert a fixed point for the unrestricted local problem.

## 3. An effective gap principle for all fixed square classes

The following result is independent of the Subspace Theorem and
uniform in the positive integer square-class parameter \(d\).

**Theorem 3.** Fix \(d\ge1\), \(0\le r<4\) and an integer
\(m_0\ge50\). The interval
\[
 m_0\le m\le m_0+\lfloor m_0/5\rfloor
\]
contains at most fourteen indices \(m\) for which
\(a_{4m+r}=d x^2\) with \(x\in\mathbb Z\).

Consequently, for \(N\ge200\), the number of indices
\(0\le n\le N\) in any fixed square class \(d\) is at most
\[
 200+56\left(1+
       \frac{\log(N/200)}{\log(6/5)}\right).
\]

**Proof.** Put
\(\alpha=(1+\sqrt5)/2,\ \beta=1+\sqrt2,\ c=1/(2\sqrt2)\).
For \(n\ge1\) the Binet expressions give
\(a_n=c\beta^n+\alpha^n+e_n\), with
\(|e_n|\le(1+c)\alpha^{-n}\).
The elementary inequality
\(0\le1+u/2-\sqrt{1+u}\le u^2/8\) for \(u\ge0\),
applied to \(u=(\alpha^n+e_n)/(c\beta^n)\), gives
\[
 \left|\sqrt{a_n}-\sqrt c\,\beta^{n/2}
   -(2\sqrt c)^{-1}(\alpha/\sqrt\beta)^n\right|<5\rho^n,
 \quad \rho=\alpha^2/\beta^{3/2}.
\]
In detail, \(0<\alpha^n+e_n<2\alpha^n\), and the error is bounded
by \((2c^{3/2})^{-1}\rho^n+
(1+c)(2\sqrt c)^{-1}(\alpha\sqrt\beta)^{-n}\).
The latter exponential base is smaller than \(\rho\) and the
sum of the constants is less than 5. Direct elementary
inequalities give \(\rho^4<1/4\).

Let \(U=\alpha^4,V=\beta^2\), and
\[
 W=\{V,V^{-1},UV,U/V,V/U,(UV)^{-1}\}.
\]
These six distinct positive units are permuted by the Galois group of
\(K=\mathbb Q(\sqrt2,\sqrt5)\). The units \(U,V\) are multiplicatively
independent: conjugating \(U^iV^j=1\) by the automorphism inverting
\(U\) and fixing \(V\) gives \(U^{2i}=1\), and then \(i=j=0\).

For an index in the stated square class write \(x\ge0\).
The approximation above becomes
\[
 |x-A V^m-B(U/V)^m|<5\,4^{-m},
\]
where \(A=\sqrt{c/d}\,\beta^{r/2}\) and
\(B=(2\sqrt{cd})^{-1}(\alpha/\sqrt\beta)^r\).
The constant is uniform because \(d\ge1\).

Consider the determinant of any seven row vectors
\((x_i,(w^{m_i})_{w\in W})\), with all \(m_i\) in the interval.
It is an algebraic integer \(\Delta\in K\); every Galois automorphism
permutes its last six columns, so \(\Delta^2\in\mathbb Z\).
Factor \(w^{m_0}\) from each unit column. Their product is 1.
Subtract \(A V^{m_0}\) times the scaled \(V\)-column and
\(B(U/V)^{m_0}\) times the scaled \(U/V\)-column from the first
column. Its entries now have absolute value at most \(5\,4^{-m_0}\).
All other entries are \(w^{m_i-m_0}\).
For \(H=\lfloor m_0/5\rfloor\), the product of the columnwise
maximal absolute values of the six unit columns is at most
\((U^2 V)^H<300^H\), since \(UV,V,U/V\) are the three units
larger than one. The Leibniz formula thus gives
\[
 |\Delta|< 7!\,5\,4^{-m_0}300^{\lfloor m_0/5\rfloor}<1.
\]
The final inequality follows from \(25200\cdot300^{10}<4^{50}\)
and \(300<4^5\). Therefore \(\Delta=0\).

If there are at least seven indices, their row vectors all lie in
a proper \(K\)-linear subspace, hence in one hyperplane
\(c_0X+\sum_{w\in W}c_wZ_w=0\).
If \(c_0=0\), the resulting exponential polynomial has at most
five distinct real zeros by Rolle's theorem. In general, a
nonzero combination of \(k\) distinct positive exponential bases
has at most \(k-1\) real zeros: divide by one exponential, differentiate
and use induction and Rolle's theorem.

If \(c_0\ne0\), write \(x=\sum_w b_w w^m\) and use the original
equation \(a_{4m+r}=dx^2\). The resulting exponential polynomial
has at most fifteen bases, since the squared exponent pairs in
\((U,V)\) lie in \(\{-2,-1,0,1,2\}\times\{-2,0,2\}\), which
also contains the four original Binet exponent pairs.
It is nonzero: otherwise independence of the bases implies
a Laurent polynomial identity
\[
 C_1u+C_2u^{-1}+C_3v^2+C_4v^{-2}=dH(u,v)^2
\]
with all \(C_i\ne0\). Assign weights 2 and 1 to \(u,v\).
The highest-weight part on the left is \(C_1u+C_3v^2\),
which has an irreducible factor of multiplicity one over
\(\overline{\mathbb Q}\) in the Laurent polynomial ring.
It cannot be the square of the highest-weight part on the right
times \(d\). Thus the nonzero exponential polynomial has at most
fourteen zeros. This proves the interval bound.

Partition \(m\ge50\) into successive integer intervals of the
displayed type. Each next interval starts at a value strictly
greater than \(6/5\) times the preceding starting value.
For each residue \(r\), at most \(1+\log(N/200)/\log(6/5)\)
such intervals meet \(4m+r\le N\). There are at most 200 indices
with \(m<50\), and four choices of \(r\). The count follows. QED.

The gap principle is effective and uniform in \(d\), but controls
clusters of solutions rather than the position of an isolated
square index. It does not replace an effective upper bound on
the last square index.

## Reproduction

Run:

    python3 verify_composite_lifting.py

The program verifies the exact period formula for the first 1000
positive periods, rechecks the original four-branch certificate,
then reproduces the complete composite-period propagation.
