# An explicit uniform window of growing prime exponents

The preceding Chebotarev supplement fixed e before sending h to infinity. Here an unconditional explicit least-prime bound makes the quantifiers uniform: one stated h threshold works for every prime e in a growing interval. This remains a construction of certified subsets, not an exclusion of all integer-power candidates.

## Theorem

Set A=301848 and P_e=(10e)^(A*e^2). One can choose a witness prime p_e<=P_e for every prime e>=5 so that the following holds simultaneously.

For every integer h>=32, every prime5<=e<=h+1, and either width

    d=3^h or d=2*3^h,

at least

    H/[2*3^(e+1)*P_e],    H=9*10^(d-1),

endpoints have certified whole blocks of integer nonpowers whose rotations all have3-adic valuation exactly e and are e-th powers in Q_3. They are neither squares nor cubes in Q_3. The endpoint subsets for different e are disjoint, since their valuations differ.

The witnesses can be chosen once for each e, independently of h. The threshold32 is deliberately coarse, not optimized. All bounds are unconditional and explicit, but enormously impractical. No assertion covers exponents outside5<=e<=h+1, all endpoints in these widths, or arbitrary other digit widths. The global integer conjecture remains open.

## 1. The effective input and its precise scope

We use Ahn and Kwon, *An explicit upper bound for the least prime ideal in the Chebotarev density theorem*, Annales de l'Institut Fourier69(3) (2019),1411–1458, Theorem1.1. For any nontrivial finite Galois extension L/K and prescribed conjugacy class, they provide an unramified degree-one prime of K with that Frobenius class and norm at most |Disc(L)|^12577. There is no GRH or sufficiently-large-discriminant restriction in this theorem. We use K=Q, so the norm is the rational prime itself.

Primary source: https://www.numdam.org/item/10.5802/aif.3274.pdf (Theorem1.1, journal page1413).

Only this external quantitative theorem is invoked; the following discriminant and interval calculations are supplied explicitly. The finite verifier does not purport to prove the external theorem.

## 2. A discriminant bound uniform in e

Use the previously constructed fields

    k=Q(zeta_e), K=k(10^(1/e)),
    F=K(sqrt10), C=Q(zeta_12), E=FC.

The earlier field-intersection proof gives [K:Q]=n=e(e-1), [F:Q]=2n and [E:Q]=8n. K and Q(sqrt10) are linearly disjoint; F and C are linearly disjoint. The required Frobenius is the identity on F and exponent11 on zeta_12, a central singleton.

The cyclotomic discriminant is D_k=e^(e-2). The relative field discriminant of K/k divides the polynomial discriminant ideal of X^e-10, whose generator up to sign is e^e*10^(e-1). The tower formula and norm to Q therefore give

    D_K <= e^(2e^2-3e)*10^((e-1)^2).

For linearly disjoint number fields L,M, the integral-basis product order gives D_(LM)<=D_L^[M:Q]*D_M^[L:Q]. Using Disc(Q(sqrt10))=40 and Disc(Q(zeta_12))=144 yields

    D_E <= D_K^8 *40^(4n)*144^(2n).

Since n<=e^2 and40^4*144^2<10^16,

    D_E <= e^(16e^2)*10^(24e^2)
         <=(10e)^(24e^2).

Apply the least-prime theorem to the designated Frobenius class. The resulting witness satisfies

    p_e<=D_E^12577 <=(10e)^(301848e^2)=P_e.

As proved in CHEBOTAREV_EXPONENT_WITNESSES.md, this prime has p_e=11 modulo12, and r_e=ord_(p_e)(10)>1 is odd, coprime to3, and divides(p_e-1)/e. The unramified condition excludes the bad ramified primes in the construction. In particular both stated digit widths are coprime to r_e.

## 3. A single valuation and its exact density

Use just valuation b=e, rather than the earlier infinite valuation union. The four endpoint classes

    m=3^e, 2*3^e, 3^e-1, 2*3^e-1 modulo3^(e+1)

give v_3(T_m)=e. Since e<=h+1, the inherited cubic congruence modulo3^(h+2) gives that same valuation for every rotation. Only the prime exponent e remains possible for an integer power.

For a witness p=p_e of order r=r_e, the endpoint condition

    m=((10^d-1)/9)*d^(-1)-1 modulo r

ensures r|D(m). On that endpoint progression, the prefix is affine modulo p with nonzero slope1/(1-10^d), and exactly(p-1)(e-1)/e residues modulo p are nonzero non-e-th-powers. This rules out the last possible integer exponent at every cut.

CRT gives the exact successful density

    alpha=4/3^(e+1) * (p-1)(e-1)/(e*p*r)

in a complete endpoint period

    M=3^(e+1)*p*r <3^(e+1)*p^2.

The constants in the affine formula can depend on d, but its nonzero slope makes the count exact for every such constant. Since(p-1)/p>=1/2, (e-1)/e>=1/2 and r<p,

    alpha>=1/[3^(e+1)*p].

On an interval of length H, discarding an incomplete period loses at most M successful endpoints. Thus the count is at least H*alpha-M. It is at least H/[2*3^(e+1)*p] whenever

    H>=2*3^(2e+2)*p^3.                         (1)

The stated theorem follows after replacing p by its upper bound P_e and proving (1) uniformly.

## 4. One explicit threshold for all e<=h+1

For h>=32 and e<=h+1,

    10e<=10(h+1)<=3^h,
    p<=P_e<=3^(A*h*(h+1)^2).

Also d>=3^h and

    H=9*10^(d-1)>=3^(3^h+1).

Therefore (1) follows from

    3^h >= 2h+4+3A*h*(h+1)^2.                 (2)

Inequality (2) holds at h=32 by exact integer arithmetic. It persists by induction: for h>=2 the cubic term's ratio is

    [(h+1)(h+2)^2]/[h(h+1)^2]
      =(h+2)^2/[h(h+1)]<3,

and the linear term also grows by a factor less than3. Thus the right side of (2) grows by less than3 per step, while the left side grows by exactly3. The elementary inequality10(h+1)<=3^h holds already at h=4 and also propagates by induction.

This proves the uniform threshold, with no e-dependent hidden constant or uncomputed exceptional threshold. The lower bound is positive. Counts for different e may be added if desired because the endpoint sets have distinct exact3-adic valuations; no joint independence of witness primes is required.

## 5. Meaning and limitations

This strengthens the earlier fixed-exponent result to a growing window with explicit quantifiers. The upper endpoint h+1 is dictated by the current3-adic precision argument using valuation e. We do not assert it is an intrinsic mathematical barrier, or that every possible integer prime exponent is at most h+1.

The bound is a theoretical guarantee, not a feasible algorithm for finding primes near P_e or constructing enormous endpoint blocks. No GRH, ineffective Siegel-type threshold, or unproved prime-supply hypothesis is used. The external12577 exponent is intentionally coarse; optimizing it is not necessary for the claimed window.

The main manuscript/PDF are unchanged, and the integer conjecture is not resolved.

## 6. Verification

The standard-library verifier checks the exact discriminant-constant inequality, A=24*12577, the h=32 base inequality, finite examples of the two induction inequalities, and all prime e<=h+1 for selected h using integer exponent comparisons. These finite checks audit the stated constants; the algebraic/discriminant and induction proofs supply the unbounded assertions.

Run `python papers/A001292/verify_uniform_effective_window.py`.
