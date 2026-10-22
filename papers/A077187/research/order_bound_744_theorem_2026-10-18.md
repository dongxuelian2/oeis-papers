# A077187 — independently certified multiplicative orders up to 744

**2026-10-18. Status: exact finite computer-assisted theorem, not an
unrestricted-prime proof.**

## Theorem

Write \(M(k)=1\Vert2\Vert\cdots\Vert k\Vert(k-1)\Vert\cdots\Vert1\).

**Theorem (bounded multiplicative order).** Every prime \(p\) with
\[
 2\le\operatorname{ord}_p(10)\le744
\]
divides at least one \(M(k)\). The same conclusion holds for \(p=3\),
which has order 1; \(p=2,5\) cannot divide any \(M(k)\).
For \(p\ge7,\ p\ne11\), the witness may be chosen
\(k=10^{jT}\) or \(10^{jT}+1\), for \(1\le j\le p\) and
\[
r=\operatorname{ord}_p(10),\quad
r=2^a5^cv,\ (v,10)=1,\quad
T=\operatorname{lcm}(r,\operatorname{ord}_v(10)).
\]

**Important improvement over the preceding order <=500 note:** this theorem
depends only on the two elementary infinite-family arguments (finite-defect
\(2^a5^c\mid20\), and invariant \(v\mid9\)) plus **77 exact GCD
certificates**. It does *not* invoke the high-\(3\)-power cyclotomic
norm towers or their 486-phase sieve. Four former norm-dependent
order classes have been independently eliminated by the same GCD method.

The statement is a *finite cutoff* on the possible multiplicative order,
not a proof that all primes have this property.

## Exhaustive arithmetic partition

For \(2\le r\le744\), let \(u=2^{v_2(r)}5^{v_5(r)}\), \(v=r/u\).
Split all such integers into the following disjoint cases:

1. \(u\mid20\): the earlier finite-defect transfer yields a perfect
   square and an explicit witness (elementary infinite family).
2. \(u\nmid20\) and \(v\in\{1,3,9\}\): by the previously proved identity
   \(\Delta_C+\Delta_Y=9/100\ne0\pmod p\), so the two-offset
   linear construction yields a witness.
3. The **77 remaining exact orders**: certify their nonzero drift
   using the integer-ring GCD below.

The machine-checkable partition is:
\`\`\`python
assert [r for r in range(2,745)
        if not (20 % (r // remove_twos_and_fives(r)) == 0
                or remove_twos_and_fives(r) in (1,3,9))] == sorted(
                    [r for r,t,g in OLD_ROWS + NEW_ROWS])
\`\`\`
The executable uses a clearer equivalent expression, with no undefined
functions; see \`certify_orders_le744.py\`.

The 77-class exact certificates comprise:

- **42** original exact-order certificates at \(r\le500\), pinned
  in \`certify_orders_le500.py\`.
- **31** new exact-order certificates at \(501\le r\le744\).
- **4** independent replacement certificates for the smooth-order
  classes \(r=216,432,648,675\) (formerly covered by higher
  \(3\)-power cyclotomic norms).

## Exact finite certificate construction

Fix \(r\), put \(N_r=10^r-1\), and work in the composite ring
\(\mathbb Z/N_r\mathbb Z\). Here 10 is invertible and has *exact*
order \(r\), because \(0<10^h-1<N_r\) for \(1\le h<r\).

For the \(d\)-digit layer put \(q=10^d\),
\(L=10^{d-1}\), \(n=9L\),
\(A=q^n\), \(S=\sum_{i=0}^{n-1}q^i\),
\(J=\sum_{i=0}^{n-1}iq^i\). The ascending/normalized
descending state changes by
\[
 C'=AC+(q-1)S-J,\qquad
 Y'=A^{-1}(Y+LS+J). \tag{1}
\]
All operations are in \(\mathbb Z/N_r\mathbb Z\), with only the
invertible quantity \(A\) divided by. In particular, no inverse
of \(q-1\) is assumed.

Compute \(S,J,A\) by splitting \(n=th+b\) with
\(h=r/\gcd(r,d)\), \(0\le b<h\), since \(q^h=1\):
\[
 S=tS_h+S_b,\qquad
 J=tJ_h+hS_h\binom t2+thS_b+J_b,\qquad A=q^b. \tag{2}
\]
Obtain \(n\bmod(hN_r)\) by modular exponentiation, derive
\(t\bmod N_r\), and evaluate the short sums by logarithmic-time
doubling. Since \(N_r\) is odd, \(\binom t2\pmod{N_r}\) is well
defined using \(2^{-1}\). Thus no astronomically long digit
concatenation or factorization of \(N_r\) is performed.

Let
\[
 (U_r,V_r)=S_{2T}-S_T,\qquad
 G_r=\gcd(N_r,U_r,V_r). \tag{3}
\]
Any prime \(p\) of *exact* order \(r\) divides \(N_r\) and reduces
(1)--(3) to the prime-field drift construction. Hence zero drift
would imply \(p\mid G_r\).

All \(G_r\)'s in the 77 rows are small enough for **complete integer
trial division** (in fact at most 729 in the present table).
The certifier tests \(\operatorname{ord}_q(10)\ne r\) for **every**
prime divisor \(q\) of every \(G_r\), using modular powering.
Thus none of these divisors can be the claimed exact-order prime.
This excludes zero drift, so the general two-offset lemma supplies
a mountain witness.

The GCD values from the four independent replacement cases are
\[
\begin{array}{c|c|r}
r&T&G_r\\\hline
216&216&243=3^5\\
432&432&243=3^5\\
648&648&729=3^6\\
675&675&243=3^5
\end{array}
\]
This finite computation alone is not a substitute for the
higher-\(3\)-power *infinite subfamily* theorem, which remains
separately certified in the main PR manuscript.

### New exact-order classes, 501 through 744

\[
\begin{array}{r|r|r@{\qquad}r|r|r}
r&T&G_r&r&T&G_r\\\hline
504&504&567&520&1560&9\\
525&1050&27&528&528&297\\
536&17688&99&544&544&153\\
550&550&99&552&6072&297\\
560&1680&9&568&19880&9\\
575&12650&9&584&584&657\\
592&1776&9&608&5472&9\\
616&1848&99&624&624&351\\
632&8216&9&650&1950&9\\
656&3280&9&664&27224&9\\
672&672&189&680&1360&9\\
688&14448&9&696&4872&189\\
700&2100&9&704&704&99\\
712&7832&99&725&20300&9\\
728&2184&9&736&8096&99\\
744&3720&27&&&
\end{array}
\]

Notice \(G_{696}=189=3^3\cdot7\), despite \(7\nmid990\cdot696\).
The strict support-on-\(990r\) conjecture is false. Nevertheless
\(\operatorname{ord}_7(10)=6\), so this extra factor is **not** an
exact-order-\(696\) zero-drift prime. This is why the program checks
the actual order of each GCD prime divisor rather than assuming the
stronger, false support property.

SHA-256 of the **sorted 35 additional** \`r,T,G_r\n\` rows:
\`\`\`
211b961ab1c7c1762aa39df1e16415a0e56296ef5b4a1a9a9ffbec3d305d5aa3
\`\`\`
The original 42 rows have an independent pinned hash in
\`certify_orders_le500.py\`.

## Cross-method validation

\`audit_order_744_prime_field.py\` uses direct prime-field formulas,
independently of the composite-ring evaluator. It checks exact
orders and the full \(2T\)-layer drift:

\[
\begin{array}{r|r|r|r|r}
r&p&T&U\bmod p&V\bmod p\\\hline
584&1753&584&1438&1332\\
664&1993&27224&1889&1956\\
696&13921&4872&13258&9689
\end{array}
\]

The certifier also checks consistency of the two-offset affine
witness condition. These independently obtained checks are not used
as a replacement for the integer-ring proof.

## Reproduction and status

From the repository root:
\`\`\`bash
python3 papers/A077187/research/certify_orders_le500.py
python3 papers/A077187/research/certify_orders_le744.py
python3 papers/A077187/research/audit_order_744_prime_field.py
\`\`\`
No third-party Python packages are needed for these three steps.
The GitHub Actions \`a077187-order-bound.yml\` repeats them.

**Proof boundary:** the finite \(r\le744\) theorem follows after
auditing the two elementary lemmas and exact code. For unbounded
multiplicative orders, we still do not know whether nonzero drift
always holds, or whether an arbitrary zero-drift orbit necessarily
admits a subgroup-root witness. A full proof of A077187 is not claimed.
