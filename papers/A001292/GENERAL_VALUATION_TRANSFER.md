# General valuation transfer, including the missing exponent 37

This generalizes THIRTY_SEVEN_VALUATION_TRANSFER.md. The interval-lifting and witness-existence theorems are inherited; the new result is their transfer to every admissible prime q, and an explicit second prime that removes the previous restriction e!=37. It does not solve the global integer-power conjecture.

## 1. General theorem and quantifiers

Fix a prime q>=7, q!=5, and a positive integer P such that, with t=ord_q(10),

    3 divides P, t divides P, 10^P=1 modulo 9t, q does not divide P.

Fix a prime e>=5 coprime to q(q-1), and a positive integer s coprime to q. There is a fixed witness prime p and order r=ord_p(10) for which all sufficiently large a give a positive certified proportion of d-digit endpoints, where

    d=P*s*q^a.

Every rotation of each certified block is an e-th power in Q_q but is neither a Q_q square nor cube. Every rotation is a power in Q_3 for each prime exponent, yet no rotation is a nontrivial integer perfect power. These are specified subsets of endpoints, not all endpoints or all widths. The threshold and witness may depend on q,P,s,e. No growing-parameter uniformity is asserted.

## 2. Common valuation and the witness

Write C=V_P modulo q. The main manuscript's digit-interval theorem gives for every cut k

    10^(-D(k))*R_(m,k)=T_m+C*s*q^a modulo q^(a+1).

For b=e^j<=a-1, j>=1, impose either

    m=q^b*v or q^b*v-1 modulo q^(b+1), 1<=v<=q-1.

These are exactly 2(q-1) classes with v_q(T_m)=b. The correction vanishes modulo q^(b+1), so every rotation has exact valuation b. Since e is coprime to q(q-1), the e-th-power map is an automorphism of the q-adic unit group. Thus every rotation is an e-th power in Q_q, whereas b is odd and not divisible by 3, excluding local squares and cubes. The only possible prime integer-power exponent divides e^j and is therefore e.

Let u be the factor of P*s*q remaining after removing all powers of 3. ARBITRARY_FIXED_MULTIPLIERS.md supplies a positive-density set of primes p with

    gcd(r,6u)=1, r divides (p-1)/e.

Discard the finitely many p dividing 3*P*s*q. Then gcd(d,r)=1 for every a, and p,r,3,q are pairwise coprime. (As always, r divides p-1.) The composite-order progression lemma applies to

    m=((10^d-1)/9)*d^(-1)-1 modulo r.

On this progression W_m is affine modulo p with nonzero slope 1/(1-10^d). Exactly (p-1)(e-1)/e values are nonzero non-e-th-powers. Their endpoint density modulo pr is

    eta=(p-1)(e-1)/(e*p*r).

The condition r|D(m) and the fact that 10 is an e-th power modulo p make each such nonpower test valid at every cut. This excludes the only remaining integer exponent e.

Independently require m=1 modulo 3. Then T_m=1 modulo 9, and the same holds for every rotation by digit sums. Every rotation is a Q_3 square and cube, and is a Q_3 ell-th power for each prime ell>=5 by the unit-group automorphism. No claim about every composite exponent is intended.

## 3. Infinite valuation union and interval error

Put

    K_(e,q)=sum_(j>=1) 2(q-1)/q^(e^j+1),
    B=max{e^j : j>=1, e^j<=a-1}.

For a>=e+1 the finite union has exact density (eta/3) times the sum through B. The conditions are independent by CRT modulo 3, q^(B+1), p, r; the endpoint sets for different b are disjoint by their exact q-valuations. A common period is

    T=3*p*r*q^(B+1)<=3*p*r*q^a.

The omitted tail is at most the full geometric tail starting at eB:

    K_(e,q)-K_(e,q,a)<=2*q^(-eB)<=2*q^(-a).

For H=9*10^(d-1), any interval of H consecutive endpoints differs from its periodic density times H by at most T. Consequently the certified count is at least

    H*[(eta/3)*K_(e,q)-2*q^(-a)
        -(10/3)*p*r*q^a/10^d].

For fixed q,P,s,e,p,r the coefficient tends to the positive value (eta/3)*K_(e,q). This proves the assertion for all sufficiently large a. Once the witness is known, the displayed bound gives an effectively computable sufficient threshold, without any practical-size claim.

## 4. Which primes are admissible?

The stated P exists if and only if gcd(ord_q(10),10)=1. Necessity follows because 10^P must be a unit modulo 9t. For sufficiency one may take

    P=3*t*phi(9t).

Euler's theorem gives 10^P=1 modulo 9t. Also q does not divide P: t divides q-1, and every prime factor of phi(9t) is either a prime divisor of 9t or a divisor of ell-1 for a prime ell dividing 9t; all are smaller than q. This is a precise admissible-prime class, not a theorem for every prime. Smaller P may be used when available.

## 5. Removing e=37 with q=757

For q=757, the exact order of 10 is 27 and 10^27=1 modulo 243, so P=27 is admissible. Since

    757-1=756=2^2*3^3*7,

all primes e>=5 except 7 and 757 satisfy the unit automorphism hypothesis. In particular e=37 is allowed. An explicit witness is

    e=37, p=90947, r=1229.

Here p is prime, r is the exact order, gcd(r,6*757)=1, and r divides (p-1)/37. Therefore d=27*757^a and d=54*757^a give the claimed positive proportions for all sufficiently large a; a>=38 only ensures that the residue construction is available and is not itself a claim of a positive interval lower bound. These widths have v_3(d)=3 exactly.

Combining this with q=37,P=3 handles every fixed prime e>=5: use q=37 unless e=37, then use q=757. The q=37 branch is the previous result, not a new discovery. The two-prime selection removes the exception while preserving all prime-exponent Q_3 tests. It is not a single uniform threshold for every exponent, nor coverage of all endpoints.

## 6. Verification and limitations

The standard-library verifier checks primality and exact orders, both admissible P values, the explicit e=37 witness, 80 admissible-prime/P constructions for primes through 2000, 4,536 selected q-valuation residue classes at b=37,74,1369, the Q_3 congruence, exact tail/period inequalities, and scalar progression identities. The b=74 sample only checks the generic valuation-class identity; it is not asserted to be a power of e=37. It does not compute prefixes at d=27*757^a or enumerate their rotation blocks. Those enormous-width claims follow from the proved inherited interval lift and this argument. The main manuscript and PDF are unchanged; this is a proof supplement. No literature-priority claim is made.
