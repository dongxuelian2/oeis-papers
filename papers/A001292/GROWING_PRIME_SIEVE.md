# A growing-prime sieve for fixed power exponents

This is a new supplement to the A001292 manuscript, not a recovery of an earlier file. It proves a stronger counting bound for each fixed exponent. It does not prove that any individual block is free of integer perfect powers. Kashihara's conjecture remains open.

## Theorem

Fix an integer base g >= 2 and a prime exponent ell. For every real number 0 < c < (log ell)/2,

    #{(m,k): 2 <= m <= X, 0 <= k < m, R_(m,k) is an integer ell-th power}
       = O_(g,ell,c)(X^2 exp(-c log X / log log X)).

All logarithms are natural, and the assertion is asymptotic as X tends to infinity. Constants and the starting threshold may depend on g, ell and c. The same bound counts candidates passing the finite modular sieve constructed below; it does not require finding integer roots.

For decimal A001292, among the first N sequence entries, the number of ell-th powers is

    O_(ell,c')(N exp(-c' log N / log log N))

for every 0 < c' < (log ell)/4. In particular this applies to squares, with c' arbitrarily close to (log 2)/4. The same respective bounds, using the smallest prime exponent, hold for the union of any fixed nonempty finite set of prime exponents. Thus all perfect powers whose exponent has a prime divisor in a fixed finite set are covered.

These bounds are stronger than the manuscript's bound for all powerful values, but concern a smaller set. There is no uniform claim as ell grows with X.

## 1. Affine-exponential description

Write W_m for the base-g concatenation of 1,...,m and D(m) for its digit length. The rotation at the whole-integer cut k is

    R_(m,k) = g^D(k) W_m - (g^D(m)-1) W_k.

In a fixed d-digit interval put B=g^d, L=g^(d-1), C=B-1, and

    A = C^2 W_(L-1) + L C + 1.

The recurrence W_(m+1)=B W_m+(m+1) gives, for L-1 <= m <= B-1,

    C^2 W_m = A B^(m-L+1) - ((m+1)C+1),
    D(m) = D(L-1) + d(m-L+1).

For each fixed cut k, substitution gives

    R_(m,k) = alpha B^m + beta m + gamma,
    alpha = (g^D(k) A/C^2 - g^D(L-1) W_k) B^(1-L),
    beta = -g^D(k)/C,
    gamma = W_k - g^D(k) B/C^2.

At every prime p not dividing g(g^d-1), these coefficients are defined modulo p and beta is nonzero. This is a periodic modular extension for each fixed width and cut. We only identify it with the original concatenation inside that digit interval and for m>k.

## 2. Exact joint local-power density

Let P be a finite set of primes p congruent to 1 modulo ell. At each p suppose B and beta_p are nonzero modulo p, and set

    F_p(n) = alpha_p B^n + beta_p n + gamma_p (mod p).

The coefficients may vary with p. The simultaneous event that every F_p(n) is an ell-th power modulo p, including zero, has period dividing

    T = lcm_{p in P} p(p-1)

and density exactly

    delta(P) = product_{p in P} delta_p,
    delta_p = (p+ell-1)/(ell p).

Proof. The cyclic group of nonzero residues modulo p has (p-1)/ell ell-th powers; zero contributes one more. Fixing n modulo p-1 makes the exponential constant, and varying n modulo p makes the linear term a bijection. This gives delta_p.

For the joint assertion, add the primes in increasing order. For a new largest prime q, the previous period T_0 has no prime divisor as large as q. Put H=lcm(T_0,q-1); then q does not divide H. In each fixed class modulo H the previous conditions and the exponential modulo q are constant. Among the q lifts modulo qH, the value F_q is an affine bijection, so precisely 1+(q-1)/ell lifts are allowed. The conditional fraction is delta_q in every previous class. Induction proves the assertion even when a smaller prime divides a larger prime minus one. This is not an assumption of pairwise coprime periods.

In any interval I of integer arguments, the exact density and periodicity imply

    #{n in I: all local conditions hold} <= |I| delta(P) + T.

The error is at most one full period, including when |I|<T.

## 3. Choosing a growing set of eligible primes

Fix 0<a<(log g)/2. Choose a fixed real A_0>1 sufficiently large that

    (A_0-1)/(ell-1) > log g + a.

For all sufficiently large d, select

    t = floor(a d / log d)

eligible primes in [d,A_0 d], all congruent to 1 modulo ell and not dividing g(g^d-1).

Such a selection exists: the prime number theorem in the fixed arithmetic progression 1 modulo ell gives

    #{d <= p <= A_0 d: p=1 (mod ell)}
       = ((A_0-1)/(ell-1)+o(1)) d/log d.

Distinct primes at least d dividing g^d-1 number at most

    log(g^d-1)/log d <= (log g) d/log d.

For large d no prime divisor of the fixed base g lies in this interval. Subtracting the upper bound for omitted primes leaves more than t primes. Only the standard prime number theorem in a fixed arithmetic progression is used; no uniformity in ell or in a growing modulus is assumed.

For this set P_d,

    T_d <= product p(p-1) <= (A_0 d)^(2t),
    log T_d <= (2a+o(1))d.

Moreover,

    log delta(P_d)
      = -t log ell + sum log(1+(ell-1)/p)
      = -a(log ell) d/log d + o(d/log d),

since the sum is O_ell(t/d). The primes can be chosen independently of k. Therefore the preceding interval bound is uniform over every cut k and every subinterval of valid endpoints in this width.

## 4. Summing over cuts and widths

Let D be the base-g digit length of floor(X). Given the c in the theorem, choose a so that

    c log g / log ell < a < (log g)/2.

Choose theta with 2a/log g < theta < 1. For large d, T_d <= g^(theta d). For every fixed k, the valid endpoint interval is

    max(g^(d-1),k+1,2) <= m <= min(X,g^d-1).

The local sieve bounds the ell-th powers in it by its length times delta(P_d), plus T_d. There are fewer than g^d cuts for width d. Summing the period errors over d<=D gives

    O_(g,theta)(g^((1+theta)D)) = O_(g,theta)(X^(1+theta)).

A fixed number of small widths contributes only a constant. Discard also all widths

    d <= D - D/sqrt(log D).

They contain O_g(X^2 exp(-2(log g)D/sqrt(log D))) endpoint-cut pairs, negligible compared with the target bound. On all remaining widths d/D tends to one uniformly, so

    delta(P_d) = exp(-(a log ell/log g + o(1)) log X/log log X).

There are O(X^2) pairs in total. The strict inequality in the choice of a absorbs the uniform o(1), and the polynomially smaller period errors are also negligible. This proves the theorem.

The same summation applies to the locally surviving candidates themselves. It does not use a converse from congruences to integer powers.

## 5. Sequence index and finite sets of exponents

As established in the main manuscript, each endpoint m contributes m distinct rotations, and different endpoint blocks have strictly increasing digit lengths. Thus the complete block count through X is X(X+1)/2. A partial final block can be bounded by the complete block through X=O(sqrt(N)). Substitution halves the constant in the stretched-exponential factor and gives the stated range c'<(log ell)/4.

For a fixed finite set E of prime exponents, add the finitely many counting bounds and use the smallest log ell. A positive integer which is a q-th power for composite q is an ell-th power for every prime ell dividing q. No claim about all perfect powers follows unless the remaining prime exponents can also be controlled.

## 6. Meaning and remaining obstacle

The fixed-finite-prime limitation theorem in FINITE_PRIME_LIMIT.md leaves positive lower density of local squares for every fixed prime set. The theorem here escapes that restriction by choosing approximately d/log d primes depending on the digit width. Their individual sizes are O_(g,ell)(d), hence O_(g,ell)(log X). The growing joint period stays smaller than a full width interval, while the exact product of local survival fractions decays.

This establishes a quantitative globally averaged constraint, not a finite certificate excluding all rotations. Even the square upper bound still tends to infinity. It leaves exceptional candidates and does not bound the power exponents uniformly. In particular, it proves neither that each endpoint has a nonpower certificate nor that no square occurs.

## 7. Reproducibility and provenance

`verify_growing_prime_sieve.py` is a new independent finite audit. Run:

    python verify_growing_prime_sieve.py

It checks exact joint densities (including zero powers and overlapping periods), validates the affine-exponential rotation formula against direct modular concatenation in bases 2, 3 and 10, and checks finite prime selections and period bounds. The generated JSON certificate and text output accompany this proof. These computations audit identities and finite examples; the asymptotic theorem relies on the proof above and the standard fixed-progression prime number theorem, not on extrapolating numerical tests.

The original 15-page manuscript and its PDF are unchanged by this supplement.
