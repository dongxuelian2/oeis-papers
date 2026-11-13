# Fixed-squareclass finiteness and limits of leading-term approximation

This note assesses one possible global route. It proves exact approximation estimates and an unconditional fixed-squareclass finiteness statement for an early-cut region. The latter has an ineffective, nonuniform finite exceptional set. It does not identify a new individual exclusion, assert that no other moving-target theorem exists, or resolve Kashihara's conjecture.

## 1. Setup

Let d>=2, B=10^d, L=B/10, C=B-1, t=D(L-1), G=10^t, and

    A=C^2 W_(L-1)+LC+1.

Consider 2L<=m<=B-1 and L+7<=k<m. Put N=m-L+1, K=k-L+1>=8, J=kC+B, and M=mC+B. The exact identity is

    C^2 R_(m,k)=G J B^N+(A-GM)B^K-J.

Write H=t+dN=2q+e with e in {0,1}, and define

    Q=10^q,   alpha=sqrt(10^e J).

If R_(m,k)=y^2, set x=Cy. Then x/Q is rational with denominator supported on 2 and 5, and

    (B^(K-N+1))/32 <= alpha-x/Q <= 20 B^(K-N+1).       (1)

Thus the exact leading coefficient can be made a quadratic number of logarithmic height O(d), rather than one of height proportional to t. This representation escapes the nonnegligible-coefficient-height barrier for the canonical unrotated formula. A different issue remains.

## 2. Proof of the two-sided estimate

The decimal fraction W_(L-1)/G begins .123, so it is less than 1/8. Also t>=2d, LC+1<B^2, and B>=100. Hence

    0 < A/G < C^2/8+1 < B^2/8.

Since m>=2L and m<=B-1,

    B^2/5 < M < B^2,
    B^2/16 < M-A/G < B^2.

Let

    T=(GM-A)B^K+J.

We have B^2/10<J<B^2 and

    G B^2 B^K/16 < T < 2G B^2 B^K.

The rotation identity now gives x^2=J G B^N-T, so 0<x/Q<alpha and

    alpha-x/Q = T/[Q^2(alpha+x/Q)].

Use Q^2=G B^N/10^e and sqrt(10^e)B/sqrt(10)<alpha<sqrt(10^e)B. Bounding the denominator between Q^2 alpha and 2Q^2 alpha proves (1). This argument itself applies with x=C sqrt(R) whether or not R is a square; the square hypothesis supplies rationality.

## 3. Reduction of the rational denominator does not improve the exponent

The exact formula gives x^2=-J modulo B^K. For p=2,5,

    v_p(J)<log_p(B^2)<8d<=v_p(B^K).

Consequently, if x is an integer then 2v_p(x)=v_p(J). If g=gcd(x,Q), this implies

    g^2<=2^v_2(J) 5^v_5(J)<=J<B^2.

Write x/Q=p_0/Q_0 in lowest terms. Then Q/B<Q_0<=Q. Formula (1) therefore implies, uniformly in the stated range,

    -log|alpha-p_0/Q_0| / log Q_0
      = 2d(N-K-1)/(t+dN) + O(1/L).                  (2)

The absolute logarithmic height of alpha is (1/2)log(10^e J)=O(d), while log Q_0 is at least a positive constant times dL. Thus alpha has negligible height relative to the rational approximation. Its quadratic field, however, is not fixed across all targets.

The supplied exponent in (2) has maximum tending to 9/5, because

    t=(d-10/9)L+1/9,   N<=9L,   K>=8.

In fact (1) directly gives the exact inequality

    |alpha-p_0/Q_0| Q_0^2 > G B^(K-1)/320 > 1.

So this approximation never meets the ordinary Roth exponent >2 in the stated range. This is not merely a failure to estimate an error sharply: the error has a matching lower bound.

A Ridout-type bound for a fixed irrational alpha and denominators supported on {2,5} uses exponent >1, so could be relevant. For any fixed positive margin, (2) can exceed 1 only where

    d(N-2K-2)>t

with a corresponding positive proportional margin, up to the negligible O(d) terms coming from reduced denominator and constants. For example, at m=B-1 and 8<=K<=3L, the forced exponents are asymptotically at least 6/5. Conversely, K>=N/2 is outside this one-term Ridout-strength range. This method therefore would not cover all cuts even if a suitable uniform theorem were supplied.

If alpha is rational, the exact rational-square leading-term case is already addressed by the separate 2-adic obstacle (for K>=8). The approximation discussion concerns the irrational case.

## 4. The changing quadratic fields are a real feature of the parameter domain

At m=B-1, fix the associated e and let K range from 8 through 3L. There are 3L-7 cuts. The targets alpha have at least

    (3L-7)/2^omega(C) >= (3L-7)/(2 sqrt(C)) > sqrt(B)/10

distinct squareclasses, where omega counts distinct prime factors.

Indeed, gcd(J,C)=1 and J=1 modulo C. For a fixed positive squarefree s, write J=s z^2. Then gcd(sz,C)=1,

    z^2=s^(-1) modulo C,   1<=z<C.

Here k<=4L-1 gives J<C^2, justifying 1<=z<C. There are at most 2^omega(C) roots because C is odd; this follows prime-power by prime-power and CRT. Distinct cuts give distinct J and z. Also 2^omega(C)<=tau(C)<=2sqrt(C). Multiplication by 10^e permutes rational squareclasses, so the count applies unchanged to alpha.

The square roots belonging to distinct rational squareclasses are linearly independent over Q. Thus a number field containing all these targets must have degree at least the displayed count. In particular no one fixed number field contains this entire parameter domain as d grows.

This does NOT prove that hypothetical perfect-power solutions themselves occupy infinitely many quadratic fields. Their distribution is unknown. It does show that applying a fixed-field moving-target theorem to all allowed cuts requires an additional reduction, which has not been provided.

## 5. Precisely checked literature hypothesis

Maculan, *Diophantine applications of Geometric Invariant Theory*, Memoires de la SMF 152 (2017), Chapter 2, Theorems 1.4 and 1.5, printed pp. 28-29, gives moving-target versions of Roth's theorem. Theorem 1.4 fixes a number field K and a finite extension K' containing the varying targets; it also requires their heights to be little-o of the approximating-point heights. Theorem 1.5 fixes K as well. The present alpha targets satisfy the small-height condition, but do not lie in one fixed field over the full parameter domain, as Section 4 proves.

Primary source: https://smf.emath.fr/system/files/2017-08/smf_mem-ns_152.pdf
DOI: https://doi.org/10.24033/msmf.460

This is a verified mismatch with these particular statements, not a claim that all moving-target or varying-field results have the same hypotheses. Nor does finiteness alone supply an effective finite verification threshold.

## 6. A valid unconditional companion: finiteness for each fixed squareclass

**Proposition.** Fix epsilon>0 and a positive squarefree integer s>1. Among the parameters in Section 1 satisfying

    rho := 2d(N-K-1)/(t+dN) >= 1+epsilon,
    10^e J = a^2 s for some positive integer a,

there are only finitely many with R_(m,k) an integer square. The bound on d is ineffective here and depends on s and epsilon.

**Proof.** Suppose infinitely many such square rotations exist. Since a fixed width contains only finitely many pairs (m,k), their d are unbounded. Pass to a subsequence along which d tends to infinity. With x=Cy and Q as above, put

    z=x/(aQ).

We have a<=sqrt(10)B and gcd(x,aQ)<=a gcd(x,Q)<aB. Since z tends to the fixed positive number sqrt(s), its logarithmic rational height satisfies

    h(z)=log Q+O_s(d),

and tends to infinity. Here the usual max-norm logarithmic height and Maculan's Euclidean archimedean height differ by at most (log 2)/2, which does not affect the argument. The two-sided bounds imply z differs from sqrt(s). The upper bound gives

    |z-sqrt(s)| <=20 B^(K-N+1)/a
                   <=20 exp(-(1+epsilon)(t+dN)log(10)/2).

Therefore its archimedean proximity to sqrt(s) is at least

    (1+epsilon)log Q-O_s(1).

For p=2,5, the valuation calculation in Section 3 gives 2v_p(x)=v_p(J). Taking valuations in 10^e J=a^2s, and using that s is squarefree, forces v_p(s)=e and v_p(a)=v_p(x). Hence

    v_2(z)=v_5(z)=-q.

The combined 2-adic and 5-adic proximity of z to infinity is exactly log Q.

One can now use the fixed-target Roth-Ridout theorem. To place the application directly in the primary statement cited above, take Maculan's Chapter 2 Theorem 1.5 with K=Q(sqrt(s)), with S consisting of all places above infinity, 2 and 5, and with three fixed targets

    sqrt(s), -sqrt(s), infinity.

For each of the two real embeddings, one of the first two targets is the positive real sqrt(s). After normalizing by [K:Q]=2, the sum of their archimedean proximities is at least (1+epsilon)log Q-O_s(1). At a place v over p, the infinity target contributes q*[K_v:Q_p]*log p. Its normalized finite-place contribution is exactly

    (1/2)*sum_(p=2,5) sum_(v|p) q*[K_v:Q_p]*log p
      =q*log10=log Q.

 Other local proximities are nonnegative. Thus the normalized total is at least

    (2+epsilon)log Q-O_s(1)
      > (2+epsilon/2)h(z)

eventually, because d=o(log Q). All target heights are constant and z is distinct from each target. This contradicts Theorem 1.5 and proves finiteness.

For s=1, the exact rational-square leading term is already excluded by the separate 2-adic argument when K>=8. Consequently, for any fixed epsilon>0, an infinite sequence of square counterexamples in the displayed early-cut region would necessarily have infinitely many distinct squareclasses, with each fixed squareclass occurring only finitely often.

This statement is genuinely global but is not a uniform finiteness theorem over all s. Taking a union over unrestricted s does not preserve finiteness. It neither treats all cuts nor excludes higher prime exponents. It is not an effective finite verification procedure.

## 7. Newton acceleration loses smooth denominators without improving the height exponent

Rational Newton iteration cannot repair the preceding
approximation. Put D=10^e J and alpha=sqrt(D), with D nonsquare. Under
the hypothetical square condition, the reduced initial approximation
r_0=p_0/q_0=x/Q satisfies

    C divides p_0, q_0 is supported on {2,5}, gcd(D,C)=1.

Indeed x=Cy, Q is a power of ten, and C is coprime to ten. Define
r_(j+1)=(r_j²+D)/(2r_j), always reducing to coprime positive p_j,q_j.

**Denominator claim.** C divides q_j for every j>=1. The unreduced
Newton numerator and denominator are

    A_j=p_j²+Dq_j², B_j=2p_jq_j.

For each prime ell dividing C, A_0=Dq_0² is a unit modulo ell, so no
ell factor of p_0 cancels from B_0. This gives C|q_1. Subsequently,
C|q_j and coprimality imply that p_j is a unit at every ell|C, and
A_j=p_j² is a unit modulo ell. All prime powers of C in q_j therefore
survive into q_(j+1). This proves the claim, including multiplicities.
Since every prime divisor of C lies outside {2,5}, every accelerated
approximation loses the original smooth-denominator hypothesis.

For example, take the actual width/cut coefficient d=2, k=17,
C=99 and D=10*(17*99+100)=17830. The synthetic initial approximation
r_0=297/2 satisfies the inherited divisibilities; its next two reduced
values are

    r_1=159529/1188,
    r_2=50613765361/379040904.

Both denominators contain 99. These rational inputs illustrate the
lemma; they are not asserted to come from a square rotation.

**Height claim.** Newton preserves the initial approximation exponent
asymptotically as d grows, uniformly in the number j of iterations. Since gcd(p_j,q_j)=1,

    gcd(A_j,q_j)=1,
    gcd(A_j,p_j)=gcd(D,p_j),
    gcd(A_j,B_j) divides 2D.

If alpha/2<=r_j<=2alpha, then p_j>=q_j because D>=B²/10>4,
and p_j²<=A_j<=5p_j², B_j<=2p_j². Thus, for the usual reduced
rational height,

    2h(r_j)-log(2D)<=h(r_(j+1))<=2h(r_j)+log5.

The exact error identity gives, with E_j=-log|r_j-alpha|,

    r_(j+1)-alpha=(r_j-alpha)²/(2r_j),
    log(alpha)<=E_(j+1)-2E_j<=log(4alpha).

Section 2 bounds |r_0-alpha|<=20B^(K-N+1)<=20, whereas
alpha>=B/sqrt(10); hence r_0/alpha tends to one uniformly as d grows.
All sufficiently large widths start in the displayed interval. Newton
maps that interval into [alpha,5alpha/4], so preserves it. Summing the
preceding recurrences with their geometric weights gives, for every j>=0,

    h(r_0)-log(2D)<=2^(-j)h(r_j)<=h(r_0)+log5,
    E_0<=2^(-j)E_j<=E_0+log(4alpha).

The constants are independent of j. As log D=O(d), h(r_0) has order at
least dL, and E_0/h(r_0) is bounded by Section 3, these bounds give

    E_j/h(r_j)=E_0/h(r_0)+O(log D/h(r_0))

uniformly for every j, including a choice of j growing with d. The
maximum initial exponent tends to 9/5 by Section 3. It therefore remains
strictly below the ordinary Roth threshold 2 regardless of the number
of Newton steps. Meanwhile the original {2,5}-denominator hypothesis
for the Ridout argument is explicitly lost. Allowing an allowed prime
set that changes with d is not an application of a fixed-prime-set
theorem. This terminates this particular acceleration argument; it
neither excludes the putative square nor addresses a different
Diophantine mechanism.

Run `python papers/A001292/verify_newton_target.py` for the exact integer
example and 96 reduced-denominator and height-bound checks.
The asymptotic height argument is proved above, not inferred from these
finite tests.

## 8. Finite audit and conclusion

The companion verifier checks 18 exact rotation identities and the integer inequalities used in Section 2 for widths 2 and 3. It also counts the squareclasses in Section 4: 23 classes among 23 cuts at d=2, and 292 classes among 293 cuts at d=3; the multiplicity bounds hold. These are finite audits of the ingredients, not searches proving the conjecture. The unconditional finiteness statement depends on the quoted Diophantine-approximation theorem, not on the computation.

The unrotated canonical representation has a positive coefficient-height ratio. The irrational leading-term representation removes that ratio, and yields the fixed-squareclass finiteness result above, but still leaves (a) an ordinary Roth exponent strictly below 2, (b) unboundedly many possible quadratic fields, (c) a late-cut region outside this one-term Ridout argument, and (d) ineffective and nonuniform exceptional thresholds. These are distinct, explicitly quantified limitations. No proof of the full conjecture follows.

