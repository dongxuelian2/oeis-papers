# A sharper polynomial exponent window from two primes

This new refinement uses the already-proved Linnik-window theorem. It is a sparsity result, not an exclusion of every integer power.

## Theorem

Let K>=1 and L>=1 be any admissible absolute constants in Linnik's least-prime theorem, as stated in LINNIK_EXPONENT_WINDOW.md. Fix g>=2 and

    0<epsilon<1/(4L-2),       0<c<(log 2)/2.

The number of pairs 2<=m<=X, 0<=k<m for which the rotation R_(m,k) is an integer ell-th power for some prime ell<=X^epsilon is

    O_(g,K,L,epsilon,c)(X^2 exp(-c log X/log log X)).

This improves the earlier sufficient restriction epsilon<1/(4L+1). There is no numerical claim for K or L. Their unconditional existence is the analytic input, not a uniform prime number theorem for growing moduli.

For the first N decimal sequence entries the analogous assertion holds for prime exponents ell<=N^eta whenever eta<1/(2(4L-2)), with any exponential constant c'<(log 2)/4.

## 1. A sharper periodic counting error

Suppose a set of integer arguments is periodic with period T and has A allowed residue classes modulo T. Put rho=A/T. For any interval I of H consecutive integers, divide it into floor(H/T) complete intervals of length T and one shorter interval. The latter contains at most A allowed residues, because no residue repeats. Consequently

    count(I) <= H rho + A = H rho + T rho.

The error is the number of allowed classes, not the whole period. This holds for every starting point, also when H<T. It is an upper bound only; no stronger discrepancy assertion is required.

## 2. Two eligible primes

Fix a large digit width d and a prime exponent ell. The CRT construction in Section 2 of LINNIK_EXPONENT_WINDOW.md supplies at least

    d-(log g)d/log d

distinct primes p satisfying

    p=1 modulo ell,       p does not divide g(g^d-1),
    d<p<=M,               M=K(8ell d)^L.

In particular two distinct eligible primes p and q are available for all sufficiently large d, uniformly in ell.

For a fixed cut, the exact local-power density lemma gives the simultaneous necessary ell-th-power conditions the density

    rho = ((p+ell-1)/(ell p)) ((q+ell-1)/(ell q)) < 4/ell^2

in the period T=lcm(p(p-1),q(q-1)). This includes zero powers and remains valid if the two periods have other shared factors, for example p divides q-1.

Both p-1 and q-1 are divisible by ell. Therefore

    T <= p(p-1)q(q-1)/ell <= M^4/ell.

The number A=T rho of allowed classes is an integer, and Section 1 gives the uniform interval bound

    count(I) <= 4|I|/ell^2 + 4M^4/ell^3
             = 4|I|/ell^2 + O_(K,L)(d^(4L) ell^(4L-3)).

No exponent-dependent implicit constant occurs here. The saving in the error uses both the common factor ell in the periods and the small fraction of allowed residues.

## 3. Summation

Choose a fixed delta satisfying

    0<delta<min(epsilon,1/(4L+1)).

The previously proved theorem already bounds all prime exponents ell<=X^delta with the desired c. We treat only X^delta<ell<=X^epsilon.

As before, put D equal to the base-g digit length of floor(X), and discard widths d<=D-D/sqrt(log D). Their total number of pairs is

    O_g(X^2 exp(-2(log g)D/sqrt(log D))),

negligible relative to the desired bound. On the remaining widths, d=O_g(log X), d tends uniformly to infinity, and the two-prime supply applies.

For each valid cut-width interval, summing the main densities over all large prime exponents, or even over all integers in that range, gives

    sum_{ell>X^delta} 4/ell^2 = O(X^(-delta)).

There are O(X^2) valid endpoint-cut pairs, so the total main contribution is O(X^(2-delta)).

Since L>=1, the power 4L-3 is at least 1. The interval errors sum to

    O_(K,L)(d^(4L) sum_{n<=X^epsilon} n^(4L-3))
       = O_(K,L)(d^(4L) X^(epsilon(4L-2))).

For each fixed d and k there is one valid endpoint interval. The number of these intervals, summed over widths, is at most sum_{d<=D}g^d=O_g(X). Hence the total error is

    O_(g,K,L)(X^(1+epsilon(4L-2)) (log X)^(4L)).

The fixed inequality epsilon(4L-2)<1 makes this polynomially smaller than X^2 exp(-c log X/log log X). The large-exponent main contribution is also polynomially smaller. Combining these bounds with the earlier theorem for small exponents proves the result.

For the sequence-index statement choose epsilon strictly between 2eta and 1/(4L-2), use X=O(sqrt(N)) for a complete block containing the first N entries, and take the endpoint exponential constant strictly between 2c' and (log 2)/2.

## 4. Scope, effectiveness and the remaining obstacle

This refinement invokes exactly the same unconditional Linnik theorem and earlier fixed-exponent counting theorem as the previous supplement. It introduces no new hypothesis about primes in progressions. It does not assert a numerical choice of K,L or an explicitly usable starting threshold.

The improved window remains much smaller than the crude possible upper bound O_g(X log X) on prime exponents. It does not yield a contradiction for an individual survivor. Nor does the one-prime version of this calculation provide the same large-exponent saving: its general local density is of order 1/ell rather than 1/ell^2, and summing that bound over a polynomial interval of prime exponents does not tend to zero. This last statement describes the limitation of this counting bound, not an impossibility theorem for every one-prime method.

The main manuscript and PDF are unchanged. The accompanying verifier checks exact joint counts, the shared-period divisor and the sharpened interval error on explicit finite examples. It does not prove Linnik's theorem computationally or solve the integer conjecture.
