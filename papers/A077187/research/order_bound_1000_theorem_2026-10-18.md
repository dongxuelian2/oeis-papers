# OEIS A077187 — certified multiplicative orders at most 1000

**2026-10-18. Status: bounded-order computer-assisted theorem.**
This research extension does **not** prove A077187 for arbitrary primes.

## Theorem

For every prime \(p\ne2,5\) with
\[
\boxed{\operatorname{ord}_p(10)\le1000},
\]
there exists \(k\ge1\) such that \(p\mid M(k)\), with
\(M(k)=1\Vert2\Vert\cdots\Vert k\Vert(k-1)\Vert\cdots\Vert1\).
For \(p\ge7,\ p\ne11\), one may take
\(k=10^{jT}\) or \(10^{jT}+1\), \(1\le j\le p\), where
\(r=\operatorname{ord}_p(10)\),
\(r=2^a5^cv\), \((v,10)=1\) and
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\).

The bound follows from two earlier *elementary* infinite-family lemmas
(\(2^a5^c\mid20\) or \(v\mid9\)), the 77 certified classes through
\(r=744\), and 35 new exact-order certificates in the interval
\(745\le r\le1000\). **No higher-3-power norm certificate is needed
for this bounded-order conclusion.**

## New lemma: the stable drift needs only one period

Let \(R_r=\mathbb Z/N_r\mathbb Z\), \(N_r=10^r-1\). Define full-digit-layer
affine maps \(F_d\) by
\[
 F_d(C,Y)=(A_dC+(q-1)S-J,\ A_d^{-1}(Y+LS+J)),
\]
where \(L=10^{d-1}\), \(q=10^d\), \(n=9L\),
\(A_d=q^n\), \(S=\sum_{j<n}q^j\), \(J=\sum_{j<n}jq^j\), all in \(R_r\).

**Lemma (single-period monodromy).** For every integer \(r\ge2\), write
\(r=uv\) as above and put \(E=1+\max(v_2(r),v_5(r))\). Let
\[
 T=\operatorname{lcm}(r,\operatorname{ord}_v(10)).
\]
The affine composition
\[
 {\cal P}_r=F_{2T}\circ F_{2T-1}\circ\cdots\circ F_{T+1}
\]
has **linear part exactly the identity in \(R_r^2\)**. Consequently
\[
 \boxed{(U_r,V_r):=S_{2T}-S_T={\cal P}_r(0,0)\pmod{N_r}.}
\]
The same equality holds after reduction to any prime \(p\)
with \(\operatorname{ord}_p(10)=r\).

**Proof.** Every layer has diagonal linear part
\(\operatorname{diag}(A_d,A_d^{-1})\). Its product over the stable block is
\(\operatorname{diag}(10^H,10^{-H})\), where
\[
 H=9\sum_{d=T+1}^{2T}d\,10^{d-1}.
\]
Since \(T+1\ge E\), every summand is divisible by
\(u=2^{v_2(r)}5^{v_5(r)}\). For \(v\), the facts
\(v\mid T\), \(10^T\equiv1\bmod v\), and
\[
 v\mid(10^T-1)/9
\]
hold: for prime factors other than \(3\) divide by \(9\) as a unit;
for \(3\), the lifting-the-exponent identity
\(v_3((10^T-1)/9)=v_3(T)\) applies. The exact summation identity
\[
 9\sum_{d=e}^{e+T-1}d10^{d-1}
 =(e+T-1)10^{e+T-1}-e10^{e-1}
   -\sum_{j=e}^{e+T-2}10^j
\]
then reduces to \(T10^{e-1}\equiv0\bmod v\), for \(e=T+1\).
Thus \(r\mid H\) and \(10^H=1\bmod10^r-1\).
The block is a translation. Applying it to the actual state \(S_T\)
and to \((0,0)\) gives the claimed identity. QED.

**Significance.** Unlike the previous \(S_{2T}-S_T\) algorithm, the
new certifier processes only the stable block of \(T\) layers,
starting from zero. It remains correct even though individual
layer maps need not themselves be \(T\)-periodic over the *composite*
ring \(R_r\).

## Exact integer-ring computation

Let \(h=r/\gcd(r,d)\). The \(d\)-digit layer has \(q^h=1\bmod N_r\).
To compute \(S,J,A\), reduce
\[
 n=9\cdot10^{d-1}\pmod{hN_r},
\]
then write the result \(n=th+b,\ 0\le b<h\).
With \(S_\ell=\sum_{i<\ell}q^i\) and
\(J_\ell=\sum_{i<\ell}iq^i\),
\[
 S=tS_h+S_b,\quad
 J=tJ_h+hS_h\binom t2+thS_b+J_b,\quad A=q^b.
\]
No division by \(q-1\) occurs. The short sums are evaluated by
binary doubling. All calculations use exact GMP integers.

Set
\[
 G_r=\gcd(N_r,U_r,V_r).
\]
If \(p\) has exact order \(r\) and zero drift, necessarily \(p\mid G_r\).
The program verifies *every* prime divisor \(q\mid G_r\) has
\(\operatorname{ord}_q(10)\ne r\), using complete trial division of
the small computed GCD. Hence zero drift is impossible for that class,
and the two-offset theorem constructs a divisible mountain.

## New 35 exact order certificates

\[
\begin{array}{r|r|r@{\quad}r|r|r}
r&T&G_r&r&T&G_r\\\hline
752&17296&9&760&6840&9\\
775&2325&9&776&9312&9\\
784&2352&9&792&792&891\\
808&808&909&816&816&459\\
824&14008&9&825&1650&27\\
832&2496&9&840&840&189\\
848&11024&9&850&6800&9\\
856&45368&9&864&864&243\\
872&23544&9&875&5250&9\\
880&880&99&888&888&999\\
896&2688&9&904&12656&9\\
912&2736&27&920&10120&99\\
925&2775&9&928&6496&9\\
936&936&1053&944&27376&9\\
950&8550&9&952&5712&9\\
968&968&1089&975&1950&27\\
976&14640&9&984&4920&27\\
992&14880&9&&&
\end{array}
\]

Unlike the previously rejected assertion that every repunit GCD
is supported on prime divisors of \(990r\), this proof uses the **actual
multiplicative orders** of its factors. Examples of lower-order
contamination:
\[
\begin{array}{c|r|r}
r&G_r&\text{extraneous factor and its actual order}\\\hline
808&909=9\cdot101&\operatorname{ord}_{101}(10)=4\\
816&459=27\cdot17&\operatorname{ord}_{17}(10)=16\\
840&189=27\cdot7&\operatorname{ord}_{7}(10)=6\\
888&999=27\cdot37&\operatorname{ord}_{37}(10)=3\\
936&1053=81\cdot13&\operatorname{ord}_{13}(10)=6\\
968&1089=9\cdot121&\operatorname{ord}_{11}(10)=2
\end{array}
\]
None of those factors has order \(r\).
The complete sorted triple-list SHA-256 is
\`\`\`
f4098f7f7113f0941c5423a33de3e9bf0c0a335c2e4d901b28851fab1495cddc
\`\`\`
computed on lines \`r,T,G_r\n\`. The source file itself pins each row.

## Independent checks and reproduction

A separate field-level recurrence (not calling the composite-ring GMP
routine) verifies:
\[
\begin{array}{r|r|r|r|r}
r&p&T&U_r\bmod p&V_r\bmod p\\\hline
856&857&45368&789&388\\
936&937&936&61&281
\end{array}
\]
Both primes have exact order as claimed, and both satisfy the
two-offset linear witness congruence.

From \`papers/A077187/research\`:
\`\`\`sh
g++ -O3 -std=c++17 single_period_order_1000.cpp -lgmpxx -lgmp -o order1000
./order1000
python3 audit_order_1000_prime_field.py
\`\`\`
Combine with the existing \`certify_orders_le500.py\` and
\`certify_orders_le744.py\` to audit all **112 non-elementary
order classes** in \(2\le r\le1000\).

This result does not prove the conjecture for *unbounded* multiplicative
orders. The unbounded nonzero-drift question, or the general root
criterion in the zero-drift case, remains open.


## Stronger finite cyclotomic certificate: all 35 gcds equal 1

An independent computation evaluates \(\Phi_r(10)\) by the Möbius
product, using **only Python's standard library**, and checks
\[
\boxed{\gcd(\Phi_r(10),G_r)=
\gcd(\Phi_r(10),U_r,V_r)=1
\qquad\text{for all 35 new }r.}
\]
This is stronger than checking the actual orders of small factors of
\(G_r\): it excludes **every** prime factor of \(\Phi_r(10)\) as a
simultaneous drift zero, without any factorization of \(G_r\).

Reproduce after compiling and running the C++ program:
\`\`\`sh
./order1000 > order1000_rows.tsv
python3 audit_cyclotomic_order_1000.py order1000_rows.tsv
\`\`\`
The script first authenticates the exact 35-row SHA-256, then computes
\[
\Phi_r(10)=\prod_{d\mid r}(10^d-1)^{\mu(r/d)}
\]
using *exact integer numerator and denominator products* and tests each
gcd. It does not call the GMP routine or use prime factorization.
This finite assertion has been checked separately before committing.
It should **not** be generalized to all orders: among previous
classes, \(r=272\) has
\(\gcd(\Phi_{272}(10),U_{272},V_{272})=17\ne1\).
The weaker target that any nontrivial cyclotomic gcd has prime factors
dividing \(r\) remains unproved for unbounded \(r\).
