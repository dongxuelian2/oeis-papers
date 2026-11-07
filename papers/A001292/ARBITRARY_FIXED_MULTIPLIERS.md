# Witness orders avoiding an arbitrary fixed digit-width multiplier

This extends the earlier witness theorem from widths3^h and2*3^h to u*3^h for every fixed positive multiplier u coprime to3. The witness is allowed to depend on u and the exponent. It is a general existence argument, not an extrapolation from a finite list of width progressions.

## Theorem

Fix u>=1 with gcd(u,3)=1 and a prime e>=5. There is a positive-density set of witness primes p for which r=ord_p(10)>1 satisfies

    gcd(r,6u)=1,
    r divides(p-1)/e.

Choose one such p. For all sufficiently large h, the width d=u*3^h has a positive certified endpoint proportion of whole integer-nonpower blocks whose rotations are e-th powers in Q_3, but neither squares nor cubes there.

The fixed-u and fixed-e quantifiers are essential: no threshold uniform in an unbounded u or e is claimed here. This does not cover every endpoint or assert that every width with small3-adic valuation is solved. The integer conjecture remains open.

## 1. A compatible cyclotomic congruence

Retain

    F=Q(zeta_e,10^(1/e),sqrt10),
    A=Q(zeta_e,sqrt10).

The preceding field calculation gives [F:Q]=2e(e-1) and

    Gal(F/Q)=(C_e semidirect C_(e-1)) times C_2.

Its commutator subgroup is exactly C_e: the cyclotomic factor acts nontrivially on the order-e subgroup, so the commutators generate that subgroup, while the quotient is abelian. Hence A is the maximal abelian subextension of F, with degree2(e-1).

Let S be the set of odd primes in {3,5} together with the odd prime divisors of u, excluding e. Define

    M=8*e^2*product_(ell in S) ell,
    C=Q(zeta_M).

The conductor M is divisible by e and40, so C contains A. Conversely F intersect C is abelian over Q and must be contained in A. Therefore

    F intersect C=A,
    [FC:Q]=e*phi(M).

Use CRT to choose the invertible residue a modulo M satisfying

    a=7 modulo8,
    a=1+e modulo e^2,
    a=-1 modulo ell for every ell in S.

This automorphism of C fixes zeta_e. It also fixes sqrt10: the quadratic character of2 is+1 at a=7 modulo8; the character of5 is+1 because a=4 modulo5 if e!=5, and a=1 modulo5 if e=5. Thus it fixes A. The identity on F and exponent-a automorphism on C are compatible on the intersection and define an automorphism sigma of FC.

The automorphism sigma is central. On F it is the identity; on the abelian cyclotomic field C it commutes with every automorphism. These two restrictions determine automorphisms of FC, so every commutator with sigma is trivial.

## 2. Chebotarev and avoidance of every factor of u

Unconditional Chebotarev applied to this central singleton gives rational primes of natural density

    1/[e*phi(M)]

having Frobenius sigma, with finitely many ramified primes omitted. Such primes split completely in F and satisfy p=a modulo M. In particular10 is both a square and an e-th power modulo p.

The order r=ord_p(10) is odd: p=7 modulo8 gives v_2(p-1)=1, and the square condition puts r inside (p-1)/2. Also p=2 modulo3, so3 does not divide r. For every odd prime ell|u other than e, the congruence p=-1 modulo ell gives ell not dividing p-1 and hence not dividing r.

If e divides u, the congruence p=1+e modulo e^2 gives v_e(p-1)=1. Since10 is an e-th power, r divides(p-1)/e, which is not divisible by e. This removes e from r too. Powers of2 in u are already handled by r being odd. Therefore gcd(r,6u)=1 in all cases, including e=5 and multipliers containing e. Finally r>1 because order1 would force p|9, inconsistent with the prescribed class.

This proves the witness theorem. It is not necessary for the different witness orders to be prime, and no assumption about prime factors of repunits is used.

## 3. Transfer to digit-width intervals

For d=u*3^h, the witness order is coprime to d. The proved composite-order progression lemma therefore applies: impose

    m=((10^d-1)/9)*d^(-1)-1 modulo r

to ensure r|D(m). On this progression the prefix is affine modulo p, and exactly(p-1)(e-1)/e residues modulo p are nonzero non-e-th-powers. They exclude integer e-th powers at every cut.

Combine with the endpoint classes of common3-adic valuation b=e^j<=h+1. This leaves e as the only possible integer prime exponent, while all rotations remain e-th powers in Q_3. The endpoint density factor and infinite valuation constant are

    eta=(p-1)(e-1)/(e*p*r),
    K_e=sum_(j>=1)4/3^(e^j+1).

With H=9*10^(d-1), the prior proof gives the certified count at least

    H*[eta*K_e-2*3^(-(h+2))-10*p*r*3^h/10^d].

The last term uses the actual d=u*3^h, not a worst-case replacement. For fixed u,e,p,r the errors tend to0 and eta*K_e>0. This establishes a positive proportion for all sufficiently large h. The required h also satisfies h+1>=e.

Neither endpoint parity nor width parity is imposed by the certificate. Even u gives even widths; odd u gives odd widths. This is a statement about the constructed endpoint subsets, not every endpoint of either parity.

After a witness is found, the displayed error bound provides a computable sufficient threshold. The existence proof guarantees that exhaustive witness search terminates. No uniform numerical first-witness bound, practical running time, or simultaneous u-dependent threshold is asserted in this supplement.

## 4. Exact illustrative witnesses

Each row lists u,e,p,r. All congruences, primality and exact orders are checked by the accompanying standard-library verifier.

    u    e    p       r
    1    5    1031    103
    2    5    1031    103
    5    5    1031    103
    25   5    1031    103
    103  5    14831   1483
    7    7    207719  14837
    35   7    207719  14837
    77   7    836879  59777
    13   13   808679  31103

In particular the earlier fifth-power witness of order103 does not work at multiplier103, while the new witness of order1483 does. Multipliers containing the exponent are handled explicitly, rather than silently excluded.

The statement for arbitrary fixed u follows from the maximal-abelian-field and Chebotarev proof, not from these nine rows. The u=1,2 examples overlap earlier material and are retained only as checks of specialization.

## 5. Scope and verification

The new ingredient is the compatible cyclotomic choice that makes the witness order avoid every factor of an arbitrary fixed multiplier. The linear recurrence and3-adic valuation construction are inherited. This is not a literature-priority claim or a solution of the global integer-power conjecture. Main manuscript/PDF remain unchanged.

The verifier checks the finite CRT classes, their quadratic-character compatibility, nine primes and exact orders, e-divisibility cases, and finite examples of coprimality with u*3^h. It does not computationally verify an infinite Chebotarev conclusion, construct all large endpoint blocks, or establish uniformity when u grows with h.

Run `python papers/A001292/verify_multiplier_witnesses.py`.
