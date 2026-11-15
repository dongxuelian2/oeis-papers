# Witnesses for every prime exponent at least five

The preceding progression lemma assumed an appropriate finite-field witness. This supplement proves unconditionally that such witnesses exist for every prime e>=5, after allowing a composite multiplicative order. The conclusion supplies nonpower families for each exponent; it does not say that every integer rotation is a nonpower or solve the global conjecture.

## Theorem

For each fixed prime e>=5, there is a positive-density set of primes p such that, with r=ord_p(10),

    gcd(r,6)=1, r>1,
    r divides (p-1)/e.

A specific subset of such witness primes has natural density1/[8e(e-1)] among the rational primes. Fix any one of these witnesses. At every sufficiently large h, the constructions below give a positive proportion of certified endpoint blocks at each of the digit widths

    d=3^h and d=2*3^h.

Every rotation in each certified block is an e-th power in Q_3, but neither a square nor a cube in Q_3, and is not any nontrivial integer perfect power. Endpoint parity is unrestricted by the construction. These statements concern certified subsets, not all endpoints of either parity.

The exponent e and witness p are fixed before h tends to infinity. The proportion and threshold may depend on e and p; no uniformity for growing exponents is claimed.

## 1. Composite orders in the linear progression lemma

The proof in LINEAR_PRIME_EXPONENT_CERTIFICATE.md does not need the witness order to be prime. Let p not divide30 be prime, let r=ord_p(10)>1 satisfy gcd(r,3)=1, and let e>=5 be a prime with r|(p-1)/e. Take a width d with gcd(d,r)=1. Put

    R_d=(10^d-1)/9,
    a_d=R_d*d^(-1)-1 modulo r.

On m=a_d modulo r, r divides D(m), so p divides the cyclic modulus. Set B=10^d modulo p; it has exact order r and is not1. Appending r integers gives

    W_(m+r)=W_m+r/(1-B) modulo p.

Thus W_m=m/(1-B)+c_d modulo p on the progression. All inverses in this display exist: r divides p-1, and B!=1. The residue R_d modulo r can also be evaluated using the inverse of9 since gcd(r,3)=1; no assumption that10 is invertible modulo r is needed.

Exactly (p-1)(e-1)/e nonzero residues modulo p are not e-th powers, independently of c_d. CRT with the single endpoint class modulo r gives the exact density

    eta=(p-1)(e-1)/(e*p*r)

in a full endpoint period modulo pr. Since10 is an e-th power modulo p, each negative e-th-power test persists at every cut.

Combine this with the four endpoint classes having v_3(T_m)=b=e^j<=h+1, where h=v_3(d), as in the previous supplement. The inherited cubic congruence makes every rotation have exact valuation b. All3-adic units are e-th powers because e is coprime to6. Every possible integer prime exponent must divide b and hence must be e, which the test at p excludes.

The disjoint valuation union and interval estimate therefore remain valid with r replacing q. In particular, for

    K_e=sum_{j>=1}4/3^(e^j+1),
    H=9*10^(d-1),

the certified endpoint count is at least

    H*[eta*K_e-2*3^(-(h+2))-10*p*r*3^h/10^(3^h)]

whenever h+1>=e and gcd(d,r)=1. This is eventually a positive fraction, since eta*K_e>0. The estimates are uniform in d/3^h for fixed e,p,r subject to the coprimality condition.

## 2. A Galois extension with independent congruence conditions

Fix a prime e>=5. Let

    K=Q(zeta_e,10^(1/e)),
    F=K(sqrt10),
    C=Q(zeta_12).

The field K is the splitting field of X^e-10 and has degree e(e-1). Indeed2 is unramified in Q(zeta_e); at any prime ideal over2, the valuation of10 is1. The polynomial X^e-10 is Eisenstein there, so it has degree e over Q(zeta_e). Its Galois group has the standard semidirect-product structure C_e semidirect C_(e-1).

Every quadratic quotient of this group kills its odd-order normal subgroup C_e. Therefore K has exactly one quadratic subfield,

    Q(sqrt(e*)), where e*=(-1)^((e-1)/2)*e.

In particular sqrt10 is not in K. Thus F has degree2e(e-1), and its three quadratic subfields are

    Q(sqrt(e*)), Q(sqrt10), Q(sqrt(10e*)).

For e>=5 none is Q(i), Q(sqrt3), or Q(sqrt(-3)), the three quadratic subfields of C. Because C is biquadratic, any nontrivial intersection F intersect C would contain a quadratic subfield. Hence F intersect C=Q. Both fields are Galois, so they are linearly disjoint and

    Gal(FC/Q)=Gal(F/Q) times Gal(C/Q),
    [FC:Q]=8e(e-1).

The element that is the identity on F and sends zeta_12 to zeta_12^11 is central and has a singleton conjugacy class.

## 3. Chebotarev and the order properties

Apply the unconditional Chebotarev density theorem: in a finite Galois extension, unramified rational primes with Frobenius in a specified conjugacy class have natural density equal to the class size divided by the group order. Here it gives density1/[8e(e-1)] for primes with the preceding central Frobenius.

Outside the finitely many ramified primes, such a p splits completely in F and satisfies p=11 modulo12. Splitting in Q(zeta_e) gives p=1 modulo e; splitting X^e-10 gives an e-th root of10 modulo p; and splitting Q(sqrt10) makes10 a square modulo p. Therefore

    r=ord_p(10) divides (p-1)/e and (p-1)/2.

Since p=3 modulo4, (p-1)/2 is odd, so r is odd. Since p=2 modulo3,3 does not divide p-1 and hence does not divide r. Also r>1, because order1 would force p|9, excluded by the congruence. Removing any of the finitely many primes dividing30e leaves the same density. This proves the witness theorem.

In particular r is coprime to both3^h and2*3^h for every h. Section1 now applies at both displayed digit widths. This proves the main theorem without GRH, an Artin primitive-root assumption, or a conjecture about prime factors of repunits.

No explicit uniform bound for the first witness or for the threshold in h is asserted. For each fixed e, simple enumeration of primes with the modular power tests terminates by the existence theorem; this observation is not a practical complexity bound. Once a witness p and its order r are known, the explicit interval-error bound gives a computable sufficient threshold for h.

## 4. Explicit finite examples

The following witnesses are checked by exact arithmetic; the orders include composite examples.

    e    p       ord_p(10)
    5    1031    103
    7    6203    443
    11   3191    29
    13   7151    275
    17   239     7
    19   43283   1139
    23   106031  2305
    29   36947   637
    31   49787   803

The finite table is illustrative and independently verifiable; the assertion for all primes e>=5 follows from the Galois/Chebotarev proof, not extrapolation of this list. The earlier fifth-power instance is retained as one example, not claimed again as new.

## 5. Scope and verification

The new contribution relative to the prior conditional lemma is the composite-order generalization and the unconditional witness-existence argument. Standard Kummer, cyclotomic and Chebotarev results are applied with explicit intersection hypotheses; no literature-priority claim is made.

The construction does not cover all possible exponents in a single block: its valuation e^j deliberately leaves one possible prime exponent, then excludes it. Nor does it cover every endpoint or eliminate the global conjecture's remaining cases. The main manuscript/PDF are unchanged.

The standard-library verifier checks all nine primes and exact orders, quadratic/e-th-power memberships, composite-order scalar recurrence examples, exact finite-field counts, and finite coprimality/tail consequences. It cannot computationally prove Chebotarev or an infinite supply of primes; those are addressed by the proof above.

Run `python papers/A001292/verify_chebotarev_exponent_witnesses.py`.
