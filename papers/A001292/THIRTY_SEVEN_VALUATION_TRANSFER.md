# Transferring the exponent restriction to37

Previous exponent constructions restricted integer exponents through a positive3-adic valuation. Here every rotation is a3-adic unit and passes the Q_3 power test for every prime exponent. A positive valuation at37 supplies the exponent restriction instead. This is an infinite valuation-union construction, not a finite list of exceptional endpoints.

## Theorem

Fix a prime e>=5 with e!=37. There is a witness prime p, with r=ord_p(10), such that for both s=1 and s=2 and all sufficiently large a, the digit width

    d=3*s*37^a

contains a positive certified endpoint proportion of whole integer-nonpower blocks having these properties:

* Every rotation has3-adic valuation0 and is an ell-th power in Q_3 for every prime ell.
* Every rotation is an e-th power in Q_37, but is neither a square nor a cube in Q_37.
* No rotation is a nontrivial integer perfect power.

The witness and threshold may depend on e. The width families have v_3(d)=1 exactly, even as a grows. Both even and odd digit widths occur, and no endpoint parity condition is imposed. This does not assert that every endpoint of either parity is certified. Nor does passing every prime-exponent test in Q_3 mean passing every composite-exponent test there.

## 1. A witness avoiding6*37

Apply ARBITRARY_FIXED_MULTIPLIERS.md with u=37 and the fixed exponent e. It gives p and r with

    gcd(r,6*37)=1,
    r divides(p-1)/e,
    p=2 modulo3,
    p=-1 modulo37.

The last congruence uses e!=37. Hence p,r,3,37 are pairwise coprime. In particular gcd(d,r)=1 at both displayed width families.

The composite-order progression lemma imposes

    m=((10^d-1)/9)*d^(-1)-1 modulo r.

Then r|D(m), and W_m is affine modulo p with nonzero slope1/(1-10^d) along this progression. Exactly(p-1)(e-1)/e nonzero residue values are not e-th powers. Their exact density among all endpoint residues modulo pr is

    eta=(p-1)(e-1)/(e*p*r).

Each such test excludes integer e-th powers at every cut because10 is itself an e-th power modulo p.

## 2. The inherited interval lift at37

The main manuscript's digit-interval reduction applies with the prime37 and P=3: ord_37(10)=3,10^3=1 modulo27,37 does not divide3, and V_3=33 modulo37. At d=3*s*37^a it gives, for every cut,

    10^(-D(k))*R_(m,k)
      =T_m+33*s*37^a modulo37^(a+1).

Fix b=e^j<=a-1, j>=1. Choose either of the two families

    m=37^b*v modulo37^(b+1),
    m=37^b*v-1 modulo37^(b+1),
    v=1,...,36.

These72 classes are exactly those with v_37(T_m)=b. Since b+1<=a, the correction33*s*37^a vanishes at the precision needed to preserve that valuation. Every rotation has exact37-adic valuation b.

As e is coprime to37*36, the e-th-power map is an automorphism of the37-adic unit group. Thus the valuation b=e^j makes every rotation an e-th power in Q_37. Its odd valuation is not divisible by3, so those rotations are not Q_37 squares or cubes.

Any integer prime exponent must divide the same valuation b and therefore must be e. Section1's finite-field non-e-th-power condition excludes that last possibility. This proves integer nonpower status for every cut.

The exclusion e!=37 matters: at that exponent the unit-power map is not an automorphism and would need additional conditions. No conclusion for e=37 is silently inferred here.

## 3. Why the3-adic tests all survive

Impose the independent endpoint condition m=1 modulo3. Every cyclic concatenation has the same digit sum modulo9, namely T_m. For m=1+3t,

    T_m=1+9*t*(t+1)/2=1 modulo9.

Thus every rotation is1 modulo9, a3-adic unit. It is a Q_3 square because its residue modulo3 is1; it is a Q_3 cube because its unit is1 modulo9. For every prime ell>=5, raising to the ell-th power is an automorphism of the3-adic unit group, since ell is coprime to6. Hence every prime-exponent local power test at3 succeeds.

This is stronger than merely belonging to a Q_3-square or Q_3-cube family, but it does not assert simultaneous roots in other local fields or roots for all composite exponents. The integer exclusion is supplied by the37 valuation and the distinct witness p.

## 4. An infinite union with positive endpoint density

Define

    K_(e,37)=sum_(j>=1)72/37^(e^j+1).

Let B be the largest power of e not exceeding a-1, assuming a>=e+1. Different b=e^j classes are disjoint because their triangular-number valuations differ. Their finite union has density

    K_(e,37,a)=sum_(e<=b<=B, b a power of e)72/37^(b+1).

The conditions modulo3,37^(B+1),r,p are pairwise coprime. Their exact certified density in a complete period is

    (eta/3)*K_(e,37,a).

A common endpoint period is T=3*p*r*37^(B+1)<=3*p*r*37^a. The omitted tail satisfies

    0<=K_(e,37)-K_(e,37,a)
       <=sum_(n>=eB)72/37^(n+1)
       =2*37^(-eB)<=2*37^(-a).

For H=9*10^(d-1), the period error satisfies

    T/H <= (10/3)*p*r*37^a/10^d.

Therefore the certified endpoint count is at least

    H*[(eta/3)*K_(e,37)
       -2*37^(-a)-(10/3)*p*r*37^a/10^d].

For each fixed e and witness p,r, the limiting coefficient is strictly positive and the errors tend to0 at both s=1,2. This proves the theorem. It is an endpoint count within specified digit intervals, not a natural density over all sequence terms or all widths.

## 5. A concrete fifth-power witness and scope

One exact witness for e=5 and u=37 is

    p=412031, r=41203.

The verifier checks primality, the exact order, gcd(r,6*37)=1, p=-1 modulo37 and r|(p-1)/5. The fifth-power construction is therefore available once a>=6, with a positive lower bound for all sufficiently large a. Availability of residue conditions and positivity of the interval lower bound are distinct statements; no unsupported small-a count is asserted.

The positive3-adic-valuation families in the earlier exponent supplements do not contain these blocks, whose3-adic valuation is0. The construction can overlap other previously known local exclusions, and no individual small endpoint is claimed as a new discovery. The new contribution is the transfer of the exponent restriction to37 while all prime-exponent Q_3 tests survive, together with the infinite valuation-union count.

The prime37 interval-lifting theorem and the witness-existence theorem are inherited and explicitly used. No new assertion about all endpoints, all widths, or literature priority is made. The global conjecture remains open and the main manuscript/PDF are unchanged.

## 6. Finite verification

The verifier checks the witness arithmetic, the72 valuation classes at selected b values, exact tail/period inequalities, the3-adic residue condition, and finite scalar recurrence examples. It does not construct prefixes at the enormous displayed digit widths or enumerate their rotations; the inherited interval-lifting theorem and the proof above establish those statements.

Run `python papers/A001292/verify_valuation_transfer.py`. The verifier uses only the Python standard library.
