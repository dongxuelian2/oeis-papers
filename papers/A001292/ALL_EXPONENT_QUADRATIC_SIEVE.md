# A sharper all-exponent bound for powerful rotations

This supplement improves the original uniform powerful-value estimate by one factor of log log X. Unlike the exponent-window supplements, it applies to every powerful rotation and hence to every nontrivial integer perfect power, with no restriction on its exponent. It remains an upper bound on the number of possible exceptions, not a proof that there are none.

## Theorem

For every fixed integer base g>=2,

    #{(m,k): 2<=m<=X, 0<=k<m, R_(m,k) is powerful}
       = O_g(X^2 log log X/log X).

A positive integer is powerful if every prime dividing it has valuation at least two. In particular every integer b^e with b>=2 and e>=2 is powerful, regardless of the size or prime divisors of e.

For decimal A001292, the corresponding count among the first N terms is

    O(N log log N/log N).

This replaces the manuscript's earlier upper bound O(N (log log N)^2/log N). The full integer conjecture remains open.

## 1. Uniform local data

We use the manuscript's exact affine-exponential formula on a d-digit interval. Write B=g^d and let

    N_d = g(g^d-1).

For each fixed cut k, the rotation has a modular extension

    F(n)=alpha B^n+beta n+gamma (mod p^2)

at every eligible prime p not dividing N_d, with beta nonzero modulo p. The coefficients depend on the width and cut, but all the following estimates do not.

Let E_p be the event that F(n) has valuation exactly one at p. This has period dividing p^2(p-1) and exact density

    rho_p=(p-1)/p^2.

The intersection for any finite set of eligible primes has density equal to the product of its rho_p, and period dividing the least common multiple of the individual periods. In particular, if s is the squarefree product of these primes, its count on an interval I of H integers equals

    H rho(s) + O(s^3),       rho(s)=product_{p|s} rho_p,

with absolute error at most s^3.

For completeness, the local count fixes n modulo p-1, chooses its unique root modulo p by the nonzero linear coefficient, and notes that among its p lifts exactly one vanishes modulo p^2. For joint counts, add a largest prime q to previous periods T. The integer lcm(T,q-1) has no factor q. Conditional on a residue modulo this integer, the root and lift argument gives exactly the same fraction rho_q. This proves the product law even when periods share prime factors. It is not an assumption of coprime periods.

Only arguments in the original digit interval, with n>k, are identified with rotations. The periodic extension is used solely for counting there.

## 2. Quadratic sieve weights, with the identity proved

Fix a real z>=2. All products in this section are squarefree and use only eligible primes. Define

    w(q)=product_{p|q} rho_p/(1-rho_p),
    G(z)=sum_{q<=z} w(q),
    G_q(v)=sum_{r<=v, gcd(r,q)=1} w(r).

All sums include 1, with rho(1)=w(1)=1. Set

    lambda_q = mu(q) product_{p|q}(1-rho_p)^(-1) G_q(z/q)/G(z)

for the eligible squarefree q<=z, and zero otherwise. Then lambda_1=1 and

    |lambda_q| <= product_{p|q}(1-rho_p)^(-1) <= q.

The first inequality uses G_q(z/q)<=G(z); the second follows prime by prime from (1-rho_p)^(-1)<=p.

We claim the exact quadratic identity

    sum_{q,r<=z} lambda_q lambda_r rho(lcm(q,r)) = 1/G(z).

Here is a derivation, so no unquoted sieve theorem is required. Put

    Y_s = sum_{q<=z, s|q} lambda_q rho(q),
    h(s)=1/w(s).

The identity rho(lcm(q,r))=rho(q)rho(r)/rho(gcd(q,r)) diagonalizes the left side as

    sum_{s<=z} h(s) Y_s^2,

because 1/rho(v)=sum_{s|v}h(s) for squarefree v. Mobius inversion on the finite divisor-closed support shows that the displayed lambda weights are equivalent to

    Y_s=mu(s)w(s)/G(z).

Explicitly, lambda_q rho(q)=sum_{s<=z, q|s}mu(s/q)Y_s; substitute s=qr to recover the weight formula. Therefore the diagonalized form is sum_s w(s)/G(z)^2=1/G(z), as claimed.

For any integer argument n which avoids every E_p, the sum of lambda_q over those q all of whose prime events occur is exactly lambda_1=1. For other arguments its square is nonnegative. Thus this square majorizes the indicator of avoiding all eligible events, and hence the indicator of a powerful rotation.

Expanding and using the intersection counts gives, on every valid interval I,

    #{n in I: rotation is powerful}
       <= H/G(z) + sum_{q,r<=z}|lambda_q lambda_r| lcm(q,r)^3
       <= H/G(z) + z^10.

The last bound uses at most z^2 pairs, |lambda_q lambda_r|<=z^2, and lcm(q,r)^3<=z^6. The exact constant 1 can be replaced by an absolute constant without changing any conclusion.

## 3. A uniform lower bound for G

We establish the required estimate directly. Let y=z^(1/8), and temporarily restrict to squarefree products of eligible primes at most y, without restricting their size. Their total weight is

    P(y)=product_{p<=y, p not dividing N_d}(1+w(p))
        =product_{p<=y, p not dividing N_d}(1-rho_p)^(-1).

Normalize these weights to a probability distribution. The expected value of the logarithm of a product q is

    sum_{p<=y, p not dividing N_d} rho_p log p
       <= sum_{p<=y} (log p)/p <= 2 log y

for sufficiently large y, by the standard Mertens estimate for the last sum. Since 2 log y=(log z)/4, Markov's inequality gives probability at most 1/4 to q>z. Every product q<=z in this restricted construction is included in G(z). Hence

    G(z) >= (3/4)P(y).

The standard Mertens product estimate and the convergent correction rho_p=1/p-1/p^2 imply

    product_{p<=y}(1-rho_p)^(-1) >= C_0 log y

for an absolute positive C_0 and sufficiently large y. Removing ineligible primes multiplies this by

    product_{p<=y, p|N_d}(1-rho_p)
       >= product_{p|N_d}(1-1/p)
       = phi(N_d)/N_d.

Consequently

    G(z) >> (log z) phi(N_d)/N_d.

The familiar elementary bound phi(N)/N >> 1/log log(3N) is uniform in N. One may see it by splitting prime divisors at log N: Mertens bounds the product over smaller primes below by a constant divided by log log N; there are at most log N/log log N larger prime divisors, their reciprocal sum is O(1/log log N), and their product of 1-1/p is bounded below by an absolute positive constant. The bounded small N range is absorbed in the constant.

Since log N_d=O_g(d), we obtain, uniformly in d,

    G(z) >>_g (log z)/log d

for large d and z tending to infinity. No assumption about the distribution of the prime factors of g^d-1 has been made.

The only analytic inputs in this section are the classical Mertens estimates
sum_{p<=y}(log p)/p=log y+O(1) and product_{p<=y}(1-1/p)^(-1) asymptotic to e^gamma log y. No Linnik theorem, growing-modulus prime number theorem, or unproved zero hypothesis is used.

## 4. Width, cut and sequence summation

Choose

    z=g^(d/40).

Then log z is a fixed positive multiple of d, G(z)>>_g d/log d, and z^10=g^(d/4). The local bound becomes

    count(I) <<_g |I| (log d)/d + g^(d/4),

uniformly over all cuts and all valid subintervals of the width.

Let D be the digit length of floor(X). For fixed d and k the interval is

    max(g^(d-1),k+1,2) <= m <= min(X,g^d-1).

There are fewer than g^d cuts at width d. The summed errors are

    O_g(sum_{d<=D}g^(5d/4))=O_g(X^(5/4)).

Widths d<=D/2 contain only O_g(X) pairs and can be discarded trivially. For the remaining widths, (log d)/d=O(log D/D); there are O(X^2) pairs in total. This proves the endpoint bound. The finitely many small widths preceding any estimates' thresholds contribute only a constant.

Each endpoint m contributes m distinct rotations, and different endpoints have strictly increasing total digit lengths, as proved in the manuscript. The complete endpoint block through X therefore contains X(X+1)/2 terms. Enclosing a partial final block and substituting X=O(sqrt(N)) proves the sequence-index assertion.

## 5. Meaning and reproducibility

The result is uniform over all possible integer power exponents because it bounds the larger set of powerful values directly. It improves the original all-exponent estimate, but the upper bound still diverges. It neither contradicts the finite-prime local-square survivor theorem nor proves the absence of individual perfect powers.

The accompanying standalone verifier checks the rational quadratic weight identity and its diagonalization, the weight bounds, the Euler-weight truncation calculation, and explicit local event intersections. Finite tests audit identities; the asymptotic conclusion follows from the proof and stated Mertens estimates, not from numerical extrapolation. The original manuscript and PDF have not been modified by this separate supplement.
