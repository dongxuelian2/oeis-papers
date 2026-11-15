# A growing window of power exponents

This new supplement extends GROWING_PRIME_SIEVE.md from each fixed exponent to a simultaneous, explicitly growing set of exponents. The conclusion is unconditional, but uses the Siegel–Walfisz theorem and consequently does not provide an effective numerical starting threshold. Kashihara's full integer conjecture remains open.

## Theorem

Fix an integer base g >= 2, a real A>0, and 0<c<(log 2)/2. As X tends to infinity,

    #{(m,k): 2<=m<=X, 0<=k<m,
              R_(m,k) is an integer ell-th power for some prime
              ell <= (log log X)^A}
       = O_(g,A,c)(X^2 exp(-c log X/log log X)).

This includes every integer power whose exponent has at least one prime divisor in the displayed window. It does not require all prime divisors of that exponent to lie there.

For decimal A001292, for every fixed A>0 and 0<c'<(log 2)/4, the analogous count among the first N sequence entries, with prime exponent ell <= (log log N)^A, is

    O_(A,c')(N exp(-c' log N/log log N)).

The constants are allowed to depend on A; this is not a theorem with A growing with X or N. In particular it cannot be used by choosing A separately for each candidate.

## 1. Uniform prime selection

We use the following standard form of the Siegel–Walfisz theorem: for every fixed B>0, uniformly for moduli q <= (log x)^B and residue classes coprime to q,

    pi(x;q,a) = Li(x)/phi(q) + O_B(x exp(-b_B sqrt(log x)))

for some b_B>0. The constants are in general ineffective. Applying this at x=Y and x=2Y gives, uniformly in the same range,

    pi(2Y;q,1)-pi(Y;q,1)
       = (1+o(1)) Y/(phi(q) log Y).

Here a fixed extra power in the allowable bound on q absorbs any fixed multiplicative constant in the modulus range. This standard fixed-logarithmic-range theorem, rather than a fixed-modulus asymptotic with unspecified dependence on q, is essential to the argument.

Reference: H. Davenport, *Multiplicative Number Theory*, 3rd edition, revised by H. L. Montgomery, Springer, 2000, treatment of the Siegel–Walfisz theorem. No unproved hypothesis on zeros of L-functions is used.

Fix real numbers B>0 and 0<a<(log g)/2. Choose a fixed integer C>log g+a+1. For each sufficiently large digit width d and every prime

    2 <= ell <= (log d)^B,

put Y=C ell d. Seek primes p in [Y,2Y] with p=1 modulo ell and p not dividing g(g^d-1).

Throughout this range log Y=log d+O_B(log log d), uniformly in ell. The Siegel–Walfisz theorem therefore gives at least

    (C-o(1)) d/log d

primes p in that interval congruent to 1 modulo ell: indeed the asymptotic count is

    (1+o(1)) C ell d / ((ell-1) log(C ell d)),

and ell/(ell-1)>=1. This use of uniformity is valid since ell<=(log d)^B<=(log Y)^B.

There are at most

    log(g^d-1)/log Y <= (log g) d/log d

distinct prime divisors of g^d-1 in that interval. For large d there are no prime divisors of the fixed base g there. Hence, uniformly in ell, we may select

    t_d = floor(a d/log d)

eligible primes P_(d,ell). The selection does not depend on the cut k. We require no effective value of the sufficiently large d.

## 2. Uniform local survival and period bounds

The affine-exponential rotation identity and exact joint-density lemma from GROWING_PRIME_SIEVE.md apply to each selected set. Namely, for fixed width and cut, the modular extension is

    F_p(m) = alpha_p (g^d)^m + beta_p m + gamma_p,

with beta_p nonzero for eligible p. The simultaneous ell-th-power conditions, including zero modulo each p, have exact density

    delta_(d,ell) = product_{p in P_(d,ell)} (p+ell-1)/(ell p)

and period dividing T_(d,ell)=lcm_{p in P_(d,ell)}p(p-1). In any valid endpoint interval I their count is at most

    |I| delta_(d,ell) + T_(d,ell).

The joint-density proof handles overlapping periods by adding primes in increasing order; no independence assumption between coprime moduli is needed. The local powers condition is necessary, not sufficient, for an integer power.

Because p>=C ell d,

    delta_(d,ell)
       <= ell^(-t_d) exp(t_d/(C d)).

Also p<=2C ell d and ell<=(log d)^B, so uniformly in ell,

    log T_(d,ell)
       <= 2 t_d log(2C ell d)
       <= (2a+o(1))d.

Choose theta with 2a/log g<theta<1. For all sufficiently large d, every period is at most g^(theta d), uniformly over the exponent window.

## 3. Taking the union of exponents

The exponent windows need not have disjoint survivors; the union bound suffices. For t=t_d>1,

    sum_{prime ell <= (log d)^B} ell^(-t)
       <= sum_{n=2}^infinity n^(-t)
       <= 2^(-t) + integral_2^infinity x^(-t) dx
       = 2^(-t)(1+2/(t-1)).

Thus the sum of local survival densities is at most

    exp(t_d/(C d)) 2^(-t_d)(1+2/(t_d-1))
       = exp(-(a log 2+o(1)) d/log d).

For each cut k and each valid endpoint interval I, the number of rotations which are ell-th powers for at least one prime ell in this width window is therefore at most

    |I| exp(-(a log 2+o(1)) d/log d)
       + (log d)^B g^(theta d).

The error includes the period error for every exponent, not just one exponent. This is the step missing from a merely pointwise fixed-exponent theorem.

## 4. Global endpoint and sequence counts

Choose a with

    c log g/log 2 < a < (log g)/2.

Let D be the base-g digit length of floor(X), and in the width argument use B=A+1. Widths d<=D-D/sqrt(log D) contain

    O_g(X^2 exp(-2(log g)D/sqrt(log D)))

pairs and may be discarded. On the remaining widths, d/D tends uniformly to one and, for sufficiently large X,

    (log log X)^A <= (log d)^(A+1).

Thus every prime exponent in the global window is included in the local width window. There are O(X^2) pairs altogether. Summing the main term gives the theorem because

    d/log d = (1+o(1)) (log X)/(log g log log X).

There are fewer than g^d cuts at width d. The total period error is

    O_(g,B,theta)((log D)^B g^((1+theta)D))
       = O_(g,B,theta)((log log X)^B X^(1+theta)),

which is smaller than the asserted bound since theta<1. A bounded initial range of widths has only finitely many pairs and causes no issue, even though the threshold furnished by Siegel–Walfisz is ineffective.

For the sequence-index statement, the main manuscript identifies the complete rotation count through endpoint X as X(X+1)/2. Bound a partial final block by the complete one and take X=O(sqrt(N)). Use the endpoint theorem with a slightly larger fixed window exponent (for example A+1) so it contains (log log N)^A. The substitution halves the allowed exponential constant, proving c'<(log 2)/4.

## 5. What remains uncontrolled

This proves a simultaneous growing-exponent result, not just a diagonal restatement of separate fixed-exponent bounds. The allowable window is explicit: every fixed power of log log X.

It still does not cover all prime exponents. If a rotation equals b^ell with b>=2, its total digit length only gives the crude upper bound

    ell <= log_g(R_(m,k)) log g/log 2
          < D(m) log g/log 2
          <= m * (base-g digit length of m) * log g/log 2
          = O_g(X log X).

The range from (log log X)^A up to this bound is not handled by the uniform theorem. Further, even the proved upper bound for the small-exponent window tends to infinity and does not eliminate exceptional individual candidates. Neither arbitrary choice of A after X is specified nor arbitrary-precision testing at a fixed finite set of primes bridges this gap.

The earlier all-exponent powerful-value bound remains available for the whole set, but is weaker. No assertion here improves that all-exponent bound, excludes every square, or resolves Kashihara's conjecture.

## 6. Finite checks and provenance

The proof above is new. The 15-page main manuscript and PDF are unchanged. Run:

    python verify_uniform_exponent_window.py

The verifier checks growing-window prime selections, exact rational bounds on the sum of local densities, and integer bounds for the joint periods. It uses `primes` from the previously published `verify_growing_prime_sieve.py`; that earlier verifier checks the underlying exact joint-density identity and direct rotation formula separately. The fresh JSON certificate and text output record the finite instances.

Finite computations do not verify the Siegel–Walfisz theorem or establish a numerical threshold for the asymptotic result. Those are respectively an invoked standard theorem and a deliberately unstated, ineffective threshold.
