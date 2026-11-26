# A positive-power window of prime exponents

This supplement replaces a polylogarithmic exponent window by a positive power of the endpoint bound. It is a counting theorem, not a proof of Kashihara's conjecture.

## 1. Statement and analytic input

Use the classical, unconditional least-prime theorem of Linnik in precisely this form: there are absolute constants K>=1 and L>=1 such that, for every q>=2 and every a coprime to q, there is a prime p congruent to a modulo q with

    p <= K q^L.

Fix any admissible pair K,L. No numerical value for either is asserted or used below. The theorem guarantees that such a pair exists, so the positive exponent range below is unconditional. This is not an assumption that the prime number theorem holds uniformly in polynomially growing moduli.

**Theorem.** Fix an integer base g>=2, and real constants

    0 < epsilon < 1/(4L+1),      0 < c < (log 2)/2.

Then, as X tends to infinity,

    #{(m,k): 2<=m<=X, 0<=k<m,
              R_(m,k) is an integer ell-th power for some prime
              ell <= X^epsilon}
       = O_(g,K,L,epsilon,c)(X^2 exp(-c log X/log log X)).

Thus there is an absolute positive exponent epsilon_0 for which a genuinely polynomially growing exponent window is controlled. The constants epsilon and c must be fixed before X varies. In particular, one cannot increase epsilon past the displayed range by changing other constants.

Among the first N decimal A001292 entries, for any fixed

    0 < eta < 1/(2(4L+1)),      0 < c' < (log 2)/4,

the count of powers with at least one prime exponent ell<=N^eta is

    O_(K,L,eta,c')(N exp(-c' log N/log log N)).

A composite power exponent is included whenever it has a prime divisor in the corresponding window.

We use the following already-proved ingredients from GROWING_PRIME_SIEVE.md:

1. For each fixed finite set of prime exponents, the endpoint-pair bound holds with any c<(log 2)/2.
2. In any fixed digit width d and cut k, the rotation has an affine-exponential modular extension F_p(m)=alpha_p(g^d)^m+beta_p m+gamma_p, with beta_p nonzero whenever p does not divide g(g^d-1).
3. For primes p=1 modulo ell with that eligibility condition, the simultaneous necessary ell-th-power conditions have exact density

       product_p (p+ell-1)/(ell p)

   and period dividing lcm_p p(p-1). Their count in an arbitrary valid interval I is at most its length times the density, plus the period. The density includes zero powers and handles overlapping periods by induction on the largest prime.

The local interval bound has absolute coefficient 1 on both its main term and its period error; it hides no exponent-dependent constant.

The first ingredient uses only a fixed-modulus prime number theorem, with all exponent-dependent constants allowed. The uniform growing-modulus input in this supplement is Linnik's least-prime theorem alone. The Siegel–Walfisz theorem in the previous supplement is not needed here.

Classical source: Yu. V. Linnik, “On the least prime in an arithmetic progression. I. The basic theorem; II. The Deuring–Heilbronn phenomenon,” *Matematicheskii Sbornik*, 15(57), 1944. Only the stated existence of absolute K,L is required; no optimization of L is claimed.

## 2. Many distinct eligible primes from a least-prime theorem

Fix a sufficiently large digit width d and any prime ell. By Bertrand's postulate there is a prime in each of (2d,4d) and (4d,8d). Choose one, called r, different from ell. Thus

    2d < r < 8d,       r != ell.

For each integer b with ceil(r/2)<=b<=r-1, use the Chinese remainder theorem to choose a residue a_b modulo ell*r satisfying

    a_b = 1 (mod ell),       a_b = b (mod r).

This is a reduced residue class: ell and r are distinct primes, 1 is nonzero modulo ell, and b is nonzero modulo r. Linnik's theorem supplies a prime p_b in that class with

    d < r/2 <= b <= p_b <= K(ell*r)^L <= M_(d,ell),
    M_(d,ell) := K(8 ell d)^L.

The primes p_b are distinct for distinct b, since their residues modulo r differ. They all satisfy p_b=1 modulo ell. There are (r-1)/2>=d of them.

At most

    log(g^d-1)/log d <= (log g)d/log d

of these primes divide g^d-1, since they are distinct and greater than d. For large d none divides the fixed base g. Consequently, for every prime ell, there are at least

    d - (log g)d/log d

distinct eligible primes of the indicated size. This assertion is uniform in ell. The least-prime theorem is applied to many different reduced classes, rather than being incorrectly treated as a lower bound for the number of primes in one class.

## 3. Choice of parameters and growing sieve length

Put H=log X. Select a real number alpha satisfying

    4L epsilon < alpha < 1-epsilon.

This is possible precisely because epsilon<1/(4L+1). Next choose a fixed real B>=1 large enough that

    alpha B/(2L(B+1)) > 2 epsilon.

The fixed positive margins are delta_0=1-alpha-epsilon>0 and
delta_1=alpha B/(2L(B+1))-2epsilon>0. They absorb any factors polynomial in log X.

Only widths d close to the largest width D need a sieve. More precisely, discard

    d <= D - D/sqrt(log D),

where D is the base-g digit length of floor(X). The discarded widths contain

    O_g(X^2 exp(-2(log g)D/sqrt(log D)))

pairs, negligible compared with the claimed bound. On the remaining widths,

    d = (1+o(1))H/log g,       log d = log H + O_g(1),

uniformly. For each prime exponent ell<=X^epsilon choose

    t_(d,ell) = floor(alpha H / (2 log M_(d,ell)))

eligible primes supplied by Section 2. For all sufficiently large X this is a positive integer and is O_(g,K,L,alpha)(d/log d), uniformly in ell. It is thus smaller than the available d-O_g(d/log d) primes.

The resulting joint period satisfies the exact bound

    T_(d,ell) <= M_(d,ell)^(2t_(d,ell)) <= X^alpha.

Because p=1 modulo ell implies p>=ell+1, each local survival fraction obeys

    (p+ell-1)/(ell p) < 2/ell.

It follows that the joint density is at most

    (2/ell)^t_(d,ell).

This bound is useful for medium and large exponents. Small fixed exponents, especially ell=2, will use the sharper earlier theorem instead.

## 4. Large exponents: d^B <= ell <= X^epsilon

The floor in the definition of t must be retained. It gives

    t_(d,ell) log(ell/2)
       >= alpha H log(ell/2)/(2 log M_(d,ell)) - log(ell/2).

Uniformly for ell>=d^B,

    log(ell/2)/log M_(d,ell)
       >= B/(L(B+1)) - o(1),

since log M=L(log ell+log d)+O_(K,L)(1). Also log(ell/2)<=epsilon H. Therefore each density is at most

    X^(-alpha B/(2L(B+1)) + epsilon + o(1)).

There are at most X^epsilon prime exponents. Their total density is at most

    X^(-alpha B/(2L(B+1)) + 2 epsilon + o(1)),

which has a fixed negative exponent by the choice of B. This accounts both for the floor loss and for the number of exponents; omitting either would produce an unjustifiably larger window.

## 5. Medium exponents: Q < ell < d^B

Let Q>2 be a sufficiently large fixed integer, to be chosen shortly. All these exponents have

    t_(d,ell) >= s_d,
    s_d := floor(alpha H / (2 log(K(8d^(B+1))^L))).

Uniformly in the retained widths,

    s_d = (alpha/(2L(B+1))+o(1)) H/log H,

and s_d tends to infinity. Since 2/ell<1, the sum of their densities is bounded by

    sum_{n>Q} (2/n)^s_d
       <= (2/Q)^s_d (1+Q/(s_d-1)).

The last inequality follows from comparison with the integral of x^(-s_d); using the slightly larger bound including n=Q is harmless. Choose Q, once and for all, so large that

    alpha log(Q/2)/(2L(B+1)) > c.

The total medium-exponent density is then O(exp(-c H/log H)), with room to absorb the uniform error terms.

## 6. Period errors, small exponents, and the total count

For each retained width and cut, apply the interval bound separately to each medium or large exponent. Their combined period error is at most X^(alpha+epsilon). Summing over cuts and widths costs O_g(X), because

    sum_{d<=D} g^d = O_g(X).

Thus the total error is O_g(X^(1+alpha+epsilon)), polynomially smaller than the target bound since alpha+epsilon<1. The density main terms from Sections 4 and 5 multiply at most O(X^2) valid endpoint-cut pairs.

The finitely many prime exponents ell<=Q are handled together by the already-proved fixed-exponent theorem, with the specified c<(log 2)/2 (or an intermediate slightly larger constant). Q depends on the fixed parameters, never on X. Its potentially large fixed constants are allowed in the big-O constant. There is no illicit use of a fixed-exponent theorem with a growing set of exponents.

Combining small, medium and large exponents, period errors, and discarded widths proves the endpoint theorem.

For the sequence theorem, choose epsilon strictly between 2eta and 1/(4L+1). A complete endpoint block through X contains X(X+1)/2 distinct entries, and a partial block can be bounded by the complete one with X=O(sqrt(N)). Then N^eta<=X^epsilon for large N. Substitution halves the exponential constant, so any c'<(log 2)/4 is available.

## 7. Scope and remaining gap

This is a polynomially growing window, much larger than every fixed power of log log X. It remains strictly smaller than the entire possible range of prime exponents. An integer rotation b^ell with b>=2 only has the general size bound

    ell <= log R_(m,k)/log 2 < D(m) log g/log 2 = O_g(X log X).

No argument here controls all prime exponents between X^epsilon and this upper bound. The old all-exponent powerful-value estimate remains valid but weaker. Also, even the new small-exponent upper bound tends to infinity; it does not exclude isolated square or other power candidates.

The result does not provide an efficient numerical search: the least-prime constants and the auxiliary fixed cutoff Q may be large. Its purpose is an unconditional, uniform counting theorem with no hidden growing-modulus prime-distribution assumption.

## 8. Audit and provenance

This proof is new, not a reconstruction of an older file. The main 15-page source and PDF are unchanged. `verify_linnik_exponent_window.py` checks the finite CRT construction, distinctness of produced primes, removal of ineligible primes, exact joint local-density formulas, and finite instances of the density tail bound. It does not numerically verify Linnik's theorem or assert particular admissible numerical K,L.

Run next to the previously published `verify_growing_prime_sieve.py`:

    python verify_linnik_exponent_window.py

The output and JSON certificate accompany the proof. The mathematical argument above, not extrapolation from these tests, supplies the unbounded theorem.
