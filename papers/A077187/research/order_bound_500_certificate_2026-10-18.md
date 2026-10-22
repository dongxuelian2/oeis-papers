# A077187: a 42-class order certificate without factoring repunits

**October 18, 2026 — rigorous finite computation conditional on code review.
The general all-primes conjecture remains open.**

## Main result

Let \(M(k)=1\Vert2\Vert\cdots\Vert k\Vert(k-1)\Vert\cdots\Vert1\)
and \(r=\operatorname{ord}_p(10)\) for a prime \(p\ge7,\ p\ne11\).
Define the 42-element finite set
\[
\begin{split}
\mathcal R=\{&
56,88,104,112,136,152,168,175,176,184,208,224,232,248,\\
&264,272,275,280,296,304,312,325,328,336,344,350,\\
&352,368,376,392,408,416,424,425,440,448,456,464,\\
&472,475,488,496\}.
\end{split}
\]

**Computer-assisted theorem (independent of the 3-power norm certificates).**
For every prime \(p\) with \(\operatorname{ord}_p(10)\in\mathcal R\),
there exists a positive integer \(k\) such that \(p\mid M(k)\).
More precisely, with
\[
v=\frac r{2^{v_2(r)}5^{v_5(r)}},\qquad
T=\operatorname{lcm}(r,\operatorname{ord}_v(10)),
\]
the witness is \(k=10^{jT}\) or \(10^{jT}+1\) for some \(1\le j\le p\).

Combining this independently certified finite set with the previously
established families \(2^{v_2(r)}5^{v_5(r)}\mid20\) and
\(r=2^a3^b5^c\ (b\le8)\), the cumulative manuscript claims existence
for **every prime having \(\operatorname{ord}_p(10)\le500\)**.
This combination depends on the independent validity of those preceding
families; the 42-class theorem itself does not.

## Construction in the composite integer ring

Fix an integer \(r\ge2\), put \(N=10^r-1\) and work entirely in
\(R=\mathbb Z/N\mathbb Z\). In this ring \(10^r=1\), and 10 has
**exact** order \(r\): for \(1\le h<r\),
\(0<10^h-1<10^r-1\), so \(10^h\ne1\pmod N\).

Define the endpoints
\[
 S_d=(C_{10^d-1},10^{-D(10^d-1)}R_{10^d-1})\in R^2.
\]
The exact full \(d\)-digit layer recursion has \(L=10^{d-1}\),
\(q=10^d\), \(n=9L\), \(A=q^n\), and
\[
 S=\sum_{i=0}^{n-1}q^i,\qquad J=\sum_{i=0}^{n-1} i q^i,
\]
\[
 \boxed{C'=AC+(q-1)S-J,\quad
 Y'=A^{-1}(Y+LS+J).} \tag{1}
\]
**No division by \(q-1\)** is performed, since \(q-1\) need not be a unit
modulo \(N\). In contrast, \(A\) is always invertible modulo \(N\).

The number \(n\) is enormous at large digit length. This does *not*
require constructing \(10^{d-1}\) as a giant Python integer.

### Fast exact geometric sums

For \(h=r/\gcd(r,d)\), \(q^h=1\pmod N\).
Write \(n=th+b\), \(0\le b<h\). With
\(S_m=\sum_{i<m}q^i,\ J_m=\sum_{i<m}iq^i\), the identities
\[
\boxed{
 S_n=tS_h+S_b,\qquad
 J_n=tJ_h+hS_h\binom t2+thS_b+J_b
} \tag{2}
\]
hold in \(R\), because each complete \(h\)-block has the same \(q\)-powers.

Since \(N\) is odd, \(\binom t2\bmod N\) depends only on
\(t\bmod N\). Compute
\[
 n\bmod hN=9\cdot10^{d-1}\bmod hN,
\]
then obtain \(t\bmod N\) and \(b\) by division by \(h\).
The short \(S_h,J_h,S_b,J_b\) are computed using doubling, with
\[
 S_{a+b}=S_a+q^aS_b,\quad
 J_{a+b}=J_a+q^a(aS_b+J_b),
\]
in \(O(\log r)\) ring operations per digit layer.
Thus each fixed-\(r\) certificate is finite and efficient, with no
factorization of \(N\) and no modular inverses of \(q-1\).

Use (1) through \(2T\) layers, storing \(S_T,S_{2T}\), and define
\[
 U_r=C_{2T}-C_T,\quad V_r=Y_{2T}-Y_T,\qquad
 \boxed{G_r=\gcd(N,U_r,V_r).}\tag{3}
\]

If a prime has \(\operatorname{ord}_p(10)=r\), it divides \(N\);
reduction of (1) modulo \(p\) recovers the precise stable drift of the
prime-field theory. **Thus zero drift modulo \(p\) forces \(p\mid G_r\).**

## The complete 42-class certificate

The program \`certify_orders_le500.py\` uses no external packages.
For each \(r\in\mathcal R\), it computes (3), then verifies by repeated
gcd removal that **every prime divisor of \(G_r\) divides \(990r\)**.
This step factors neither \(G_r\) nor \(10^r-1\).

But \(\operatorname{ord}_p(10)=r\) implies \(r\mid p-1\), so \(p>r\).
For the present classes \(r\ge56\), any such \(p\) is greater than 11,
hence \(p\nmid990=2\cdot3^2\cdot5\cdot11\), and of course \(p\nmid r\).
Therefore \(p\nmid G_r\), and at least one drift coordinate is nonzero.
The general two-offset construction from the preceding notes yields a
mountain witness, completing the proof.

The exact GCD values collapse to a strikingly small list:
\[
\begin{array}{c|l}
G_r& r\\\hline
9&\text{all entries of }\mathcal R\text{ not listed in other rows}\\
27&408,456\\
99&88,176,184,352,368,440\\
153&272\\
189&168,336\\
297&264\\
351&312
\end{array}
\]
Here \(153=9\cdot17,\ 189=27\cdot7,\
297=27\cdot11,\ 351=27\cdot13\).
The additional factors \(7,11,13,17\) divide the relevant \(r\),
not the multiplicative-order-\(r\) primes under investigation.

The machine-readable complete 42-row table is pinned in
\`certify_orders_le500.py\`, with SHA-256 over lines \`r,T,G\n\`:
\`\`\`
6b4457a29bdf807ea748a96b8501c6af53c923629eeb323800389b40ae91af57
\`\`\`

Prime-field recurrence cross-checks (fully distinct from the large
composite-ring geometric-sum evaluator):
\[
\begin{array}{r|r|r|r}
r&p&U_r\bmod p&V_r\bmod p\\\hline
56&7841&7833&1704\\
88&617&405&356\\
112&113&112&56\\
152&457&284&321\\
184&2393&1886&1984\\
312&313&198&283
\end{array}
\]
All six matched the independent exact forward recurrence.

## Reproduction

From \`papers/A077187\`:
\`\`\`sh
python3 research/certify_orders_le500.py
\`\`\`
The script asserts all 42 rows, the support restriction
\(\operatorname{rad}(G_r)\mid\operatorname{rad}(990r)\),
the SHA-256 digest, and six modular reduction test vectors. It requires
only a standard Python installation. A dedicated GitHub Actions workflow
runs this check on changes to the certificate.

## False stronger conjecture and a refined cyclotomic target

It is **false** that the repunit gcd is always supported on
prime divisors of \(990r\). We found two exact counterexamples
*to that proposed strengthening*, not to A077187:
\[
\begin{array}{c|r|r|r}
r&T&G_r&\text{unexpected divisor}\\\hline
174&2436&189=27\cdot7&7\\
258&1806&189=27\cdot7&7
\end{array}
\]
Here \(7\nmid990r\), but \(\operatorname{ord}_7(10)=6\), a proper
divisor of 174 and 258. Hence these are merely **lower-order
contaminants**, not primes whose *exact* order is \(r\).

A cleaner approach is to take the **cyclotomic** rather than the
full repunit modulus,
\[
H_r=\gcd\bigl(\Phi_r(10),U_r,V_r\bigr).
\]
Every prime \(p\) of exact order \(r\) divides \(\Phi_r(10)\).
Therefore, a verified condition that every prime factor of \(H_r\)
divides \(r\) is sufficient for nonzero drift at *every* prime
of exact order \(r\), since \(r\mid p-1\). This avoids all
nonprimitive prime factors of \(10^r-1\) except those that also divide
the relevant cyclotomic value (typically order-index divisors).

Exact independent evaluations gave:
\[
\begin{array}{r|rrrrrrrrrr}
r&56&88&104&112&168&174&258&272&312&336\\\hline
H_r&1&1&1&1&1&1&1&17&1&1
\end{array}
\]
In particular \(\Phi_{174}(10)\) and \(\Phi_{258}(10)\) are
nonzero modulo 7, so the extraneous 7 disappears.

**Open direction.** Test, and if possible prove, the *refined*
uniform assertion
\[
\operatorname{rad}\gcd\bigl(\Phi_r(10),U_r,V_r\bigr)
\mid\operatorname{rad}(r).
\]
This is **not proved** for arbitrary \(r\), and may also have
counterexamples. If true, it would exclude all exact-order zero
drift and resolve the all-primes existence conjecture.
The 42-class theorem proved above does *not* require this speculation.
