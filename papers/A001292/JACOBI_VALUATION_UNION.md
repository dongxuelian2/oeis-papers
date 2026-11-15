# Combining all power-of-two 3-adic valuations

The earlier uniform-width supplement used valuation2. Here the previously proved power-of-two valuation criterion is combined with an infinite endpoint-class count and the growing cyclotomic union. This is a new infinite counting consequence, not a new assertion of the already established individual certificate.

## Theorem

Define the absolute constant

    C=sum_{r>=1} 2/3^(2^r+1)=0.08240615276287088518... .

Let d be a decimal digit width, h=v_3(d), q=3^h and H=9*10^(d-1). Uniformly in d/q, as h tends to infinity, at least

    H*(C-O(h^4*2^(-h)))

endpoints have an entire block of integer nonpowers, although every rotation in each certified block is a square in Q_3. This improves the earlier endpoint proportion2/27, without re-counting those valuation2 classes as new.

No modulus37 compatibility is asserted. The result is a lower bound within each indicated digit-width interval, not a natural density over all widths or sequence entries. It does not address bounded h or settle the global conjecture.

## Endpoint classes and inherited cubic identity

The manuscript's uniform cubic congruence, valid for h>=1, states

    10^(-D(k))*R_(m,k)
      =T_m+(3d/2)*(m^3-m+9)-9dm*T_k modulo3^(h+4).

Both correction terms vanish modulo3^(h+2): the first uses 3|(m^3-m+9). Thus every normalized rotation is T_m modulo3^(h+2), including the prefix at k=0.

For b=2^r with r>=1 and b<=h+1, take either class

    m=2*3^b modulo3^(b+1),
    m=3^b-1 modulo3^(b+1).

In each class T_m has exact valuation b and T_m/3^b=1 modulo3. Conversely these are precisely the two classes modulo3^(b+1) with those properties: if 3 divides m, write m=3^b*u and solve u/2=1 modulo3; if 3 divides m+1, write m+1=3^b*u and solve -u/2=1 modulo3. Each other residue has a different valuation or normalized unit.

Consequently every rotation has exact valuation b and normalized unit1 modulo3. The factor10^D(k) changes neither fact. Since b is even, all rotations are Q_3 squares. Any integer prime-power exponent must divide b=2^r, hence must be2.

The classes for different b are disjoint because their T_m valuations differ. Let B be the largest power of2 not exceeding h+1, and put

    A=3^(B+1),
    S_h=sum_{2<=b<=B, b a power of2}2/3^(b+1).

The union of all these endpoint classes is periodic modulo A and has exact density S_h. The omitted tail satisfies

    0<=C-S_h<=3^(-2B)<=3^(-(h+2)).

Indeed the next possible valuation is2B>h+1, and summing over every integer b>=2B only enlarges the tail.

## Cyclotomic certificates and the deliberate omission of the top modulus

Put Q_j=(10^(2*3^(j-1))+10^(3^(j-1))+1)/3. The previous cyclotomic supplements prove that these are pairwise coprime and coprime to3, every prime factor has order3^j for10, and (10/Q_j)=1. Each Q_j for j<=h divides the cyclic modulus10^D(m)-1 and10^d-1. A negative symbol (W_m/Q_j) therefore excludes squares for every rotation. Combined with the power-of-two valuation, it excludes all integer powers.

On a fixed digit interval, W_m=T_m+c_j modulo Q_j. Uniformly in c_j, the proved character lemma bounds the failure fraction (symbols0 or+1) by s_j<=1/2+2/j. This includes degenerate discriminants and all multiplicities in Q_j.

For h>=6, use only Q_J,...,Q_(h-1), where 5<=J<=h-1. Omitting Q_h is essential to the interval estimate below when the 3-adic endpoint modulus A grows. CRT makes the character failure fraction exactly the product of the s_j, independently of the endpoint classes modulo A. Hence the certified density in a complete period is at least

    S_h*(1-E(h-1,J)),
    E(t,J)=2^(-(t-J+1))*(t+1)(t+2)(t+3)(t+4)/[J(J+1)(J+2)(J+3)].

If this lower bound is negative, it remains valid but vacuous. The actual density is of course nonnegative.

All conditions have a common period dividing

    T=A*product_{j=2}^{h-1}Q_j
      =3^(B-h+3)*(10^(q/3)-1)/999.

This identity follows by telescoping the cyclotomic factors. Since B<=h+1 and d>=q,

    T/H <= (810/8991)*10^(-2q/3) <10^(-2q/3).

Discarding an incomplete period loses at most T certified endpoints. Using S_h<=1 and the tail bound gives the explicit endpoint lower bound

    H*[C-E(h-1,J)-3^(-(h+2))-10^(-2q/3)].

For J=5, E(h-1,5)=O(h^4*2^(-h)), proving the theorem. The small exceptional values of h are irrelevant to this asymptotic assertion.

A growing cutoff is possible too. For J=max(5,ceil(log_3(h)))<=h-1, the same proof gives an error O(h^(4+log_3(2))*2^(-h)); every prime factor of every tested modulus exceeds2*3^J>=2h. Thus this slightly weaker rate obtains witnesses eventually outside every fixed finite prime set. It does not say the blocks pass every square test at those fixed primes; only Q_3 compatibility is established here.

## Scope, new contribution and finite audit

The individual power-of-two valuation certificate was already in JACOBI_POWER_TWO_VALUATIONS.md. The new content is the union of infinitely many endpoint valuation classes, its limiting constant C, and a period-fitting argument that omits the largest cyclotomic factor. Simply multiplying the previous endpoint modulus by a growing power of3 without this change would not justify the same negligible interval error.

The addition beyond the valuation2 proportion is C-2/27, approximately0.0083320786888. All these are sufficient certificates. No claim is made that every endpoint outside or inside the stated classes has been classified.

The finite verifier checks selected finite valuations and exact rational identities, then selected actual prefix calculations. It does not prove the infinite limit by experiments or check every rotation individually. The whole-block and unbounded assertions follow from the proof. The main manuscript and PDF remain unchanged.

Run from the repository root with `python papers/A001292/verify_jacobi_valuation_union.py`. It requires the sibling published modules `verify_cyclic_jacobi_certificate`, `verify_cyclotomic_jacobi_family`, and `verify_a001292`; separated audit copies must add their directories to PYTHONPATH.

## Why the same uniform-character argument does not immediately handle bounded h

A natural replacement is N=Phi_(ell^j)(10)=sum_{i=0}^{ell-1}x^i, with x=10^(ell^(j-1)), ell an odd prime other than3, and j>=2. Here N is odd and N=1 modulo8, since x is divisible by8. Therefore (2/N)=1. There is a constant c modulo N with 8c=1 modulo N. For this constant,

    t(t+1)/2+c=(2t+1)^2/8 modulo N.

Its Jacobi symbol is always0 or+1, never-1. Thus there can be no positive uniform lower bound for the negative-symbol proportion over all constants c for these moduli. This is exactly the kind of uniformity used in the present proofs; it cannot simply be transferred to this replacement family.

This counterexample does not show that the actual concatenation constant equals that bad constant, and does not rule out a method using additional information about it, different moduli, or other global tools. It identifies a concrete missing ingredient for extending the current argument to bounded v_3(d), not a proof that such an extension is impossible.
