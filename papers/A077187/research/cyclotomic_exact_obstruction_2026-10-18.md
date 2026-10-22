# A077187: exact cyclotomic criterion for vanishing monodromy

**2026-10-18. PROVED reduction for arbitrary multiplicative orders.**
This is an equivalence for the *nonzero-drift method*, **not** a proof
that the drift is always nonzero or that the unrestricted OEIS conjecture
is solved.

## Theorem (primitive-divisor obstruction is exact)

For any integer \(r\ge2\), let \(N_r=10^r-1\) and
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\), where
\(r=2^a5^cv\) with \(\gcd(v,10)=1\).
Define \((U_r,V_r)\in(\mathbb Z/N_r\mathbb Z)^2\) as the exact translation
of the stable digit-layer \(T\)-period; equivalently,
\[
 (U_r,V_r)=S_{2T}-S_T
   =(F_{2T}\circ\cdots\circ F_{T+1})(0,0).
\]
Write
\[
 H_r=\gcd\bigl(\Phi_r(10),U_r,V_r\bigr).
\]

**Theorem.** The following conditions are equivalent:

1. For every prime \(p\) with \(\operatorname{ord}_p(10)=r\),
   the drift \((U_r,V_r)\bmod p\) is not \((0,0)\).
2. There is **no prime** \(p\nmid r\) dividing \(H_r\).
3. \(\operatorname{rad}(H_r)\mid\operatorname{rad}(r)\).
4. Removing all powers of prime factors of \(r\) from \(H_r\)
   leaves 1, equivalently the loop
   \`while gcd(h,r)>1: h//=gcd(h,r)\` terminates at \(h=1\).

In particular, if any prime \(p\nmid r\) divides \(H_r\), then
**it really is a simultaneous zero-drift prime of exact order \(r\)**.
This is not merely a contaminant of smaller multiplicative order.
Such a failure does **not** by itself disprove the existence of
a divisible mountain: the zero-drift subgroup-root alternative remains.

### Proof of the cyclotomic prime-order criterion

Let \(p\nmid10\), \(r\ge2\). We use the standard fact
\[
  p\mid\Phi_r(10),\quad p\nmid r
  \quad\Longleftrightarrow\quad
  \operatorname{ord}_p(10)=r.
\]
The right-to-left implication is immediate from the factorization
\(10^r-1=\prod_{d\mid r}\Phi_d(10)\) together with minimality
of \(r\): no earlier factor \(\Phi_d(10)\) for \(d<r\) can vanish.

For the other direction, set \(m=\operatorname{ord}_p(10)\).
Then \(m\mid r\), and \(p\mid\Phi_r(10)\). If \(m<r\), we show
\(p\mid r\), a contradiction. For \(n\) a positive multiple of \(m\),
the lifting-the-exponent identity (also for \(p=3\), since \(p\) is odd)
gives
\[
  v_p(10^n-1)=v_p(10^m-1)+v_p(n/m).
\]
Applying the Möbius inversion formula
\[
  v_p(\Phi_r(10))
   =\sum_{d\mid r}\mu(r/d)\,v_p(10^d-1)
\]
shows that if \(r>m\), any positive valuation on the left
requires \(p\mid r/m\), hence \(p\mid r\).
(Equivalently, the nonprimitive factors of \(\Phi_r(10)\)
can arise only at indices \(r/m\) which are positive powers of \(p\).)
Thus \(p\nmid r\) forces \(m=r\). Since \(r\ge2\), no prime dividing
\(\Phi_r(10)\) is 2 or 5, so the multiplicative order exists.

Reduction of the exact integer-ring state and layer maps
modulo any \(p\mid N_r\) gives the prime-field drift. A prime
with exact order \(r\) divides \(\Phi_r(10)\). Therefore it makes
both drift coordinates zero exactly when \(p\mid H_r\).
By the cyclotomic criterion, the primes in \(H_r\) **not** dividing
\(r\) are precisely the zero-drift exact-order primes.
This proves equivalence of (1)--(3); (3)--(4) is repeated gcd
removal, requiring no integer factorization. QED.

## Consequences for the research program

1. The earlier proposed universal assertion
   \(\operatorname{rad}(H_r)\mid\operatorname{rad}(r)\)
   is **exactly equivalent** to the assertion that the
   **two-offset, nonzero-drift construction succeeds at every prime
   of every order**. It is not equivalent to universal mountain
   divisibility: zero-drift primes, if any, might have other witnesses.
2. A genuine counterexample to universal nonzero drift can be
   certified without factoring \(10^r-1\): compute \(H_r\), strip
   factors of \(r\) by gcd, and if anything remains, factor the
   **smaller residual** to exhibit a prime \(p\) of exact order \(r\).
3. Conversely, a finite computation of \(H_r\) and gcd stripping
   certifies the nonzero-drift method for **all primes of exact
   order \(r\)**. No enumeration of those primes is required.

### Negative controls

- The full-repunit gcd \(G_{174}=G_{258}=189\) contains 7, which is
  **not** of exact order 174 or 258. The refined cyclotomic gcd is
  \(H_{174}=H_{258}=1\), removing this spurious obstruction.
- \(H_{272}=17\ne1\), but \(17\mid272\), hence there is **no**
  true order-272 zero-drift obstruction.
- The 35 new classes with \(745\le r\le1000\) have \(H_r=1\),
  a special stronger *finite* fact, not a universal identity.

**Open gap:** the uniform claim \(\operatorname{rad}(H_r)\mid
\operatorname{rad}(r)\) remains unproved. Establishing it for all
\(r\) would prove A077187 via the existing nonzero-drift
two-offset construction; disproving it would demand a separate
root analysis for the corresponding primes.
