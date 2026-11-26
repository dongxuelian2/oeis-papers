# Near-complete conditional coverage with v_3(d)=1

This supplement gives an explicit finite-prime construction at bounded 3-adic digit-width valuation. It does not assume an infinite family of eligible primes. Its digit widths are extraordinarily large; the result is structural, not a practical search range.

## Certified finite data and theorem

The accompanying certificate lists324 distinct primes p<20000, none equal to37. For each it supplies positive integers r_p and s_p satisfying

    r_p odd, gcd(r_p,10)=1,
    10^r_p=1 modulo p,
    10^s_p=1 modulo9r_p,
    (2/p)=-1,
    v_3(lcm(3,r_p,s_p))=1.

Minimality of either exponent is not needed. Define the explicit integer

    L=lcm(111, all r_p, all s_p),
    T=999 product_p p,
    epsilon=product_p (p+3)/(2p).

The exact integer/rational verifier establishes:

    v_3(L)=1; 37|L;
    L has612 decimal digits;
    T has1233 decimal digits;
    L>=1233+200;
    epsilon<2^(-323).

Consider every digit width d=L*t with positive integer t not divisible by3. Thus v_3(d)=1 exactly, not tending to infinity. Put H=9*10^(d-1). Define the endpoint set A_d by

    m=8 or18 modulo27,
    T_m=m(m+1)/2 is a nonzero square modulo37.

There are36 allowed residue classes modulo999, of density36/999=4/111. At least

    (4H/111)*(1-2^(-322))

endpoints in this digit interval have a whole-block certificate excluding every integer perfect power. Every certified block is nevertheless a square block over both Q_3 and Q_37.

The failure fraction in a complete CRT period, conditional on A_d, is at most epsilon<2^(-323). The displayed endpoint-interval lower count includes the period error. It is phrased relative to (4/111)H, not as an exact percentage of the rounded finite count |A_d|.

Alternatively, dropping the37 square-compatibility condition gives at least

    (2H/27)*(1-2^(-322))

certified endpoints. All of these are Q_3-square blocks; no Q_37 compatibility is asserted for that enlarged family.

These are sufficient certificates on an explicit infinite progression of very large widths with fixed v_3(d). They do not cover every width with bounded v_3(d), nor classify the remaining endpoint classes or settle the full conjecture. The324-prime certificate is finite; no arbitrary-accuracy claim is inferred from it.

## 1. Eligibility of each prime for every rotation

For a d-digit endpoint m,

    D(m)=d(m+1)-(10^d-1)/9.

Since r_p and s_p divide d, the congruence10^s_p=1 modulo9r_p implies r_p|(10^d-1)/9. Thus r_p divides D(m). It follows that p divides both10^d-1 and10^D(m)-1. Also10 has odd order modulo p because its order divides the odd number r_p. Therefore (10/p)=1.

On this digit interval the concatenation recurrence reduces to

    W_m=T_m+c_p modulo p,

with a constant c_p depending on the entire width d. We do not compute or assume anything about that constant. By the rotation identity,

    R_(m,k)=10^D(k)*W_m modulo p.

Consequently any negative Legendre symbol (W_m/p) excludes integer squares for every rotation in the block.

## 2. A uniform character count including the exceptional constant

For any constant c modulo p let f(x)=x(x+1)/2+c. If its discriminant is nonzero modulo p, the standard quadratic-character identity gives

    sum_x (f(x)/p)=-(2/p)=1.

There are at most two zero values, so at least (p-3)/2 residues have negative symbol. If the discriminant vanishes, f is one half times a square after translation; since (2/p)=-1, all p-1 nonzero values have negative symbol. Hence in every case the fraction failing the negative-symbol test is at most

    (p+3)/(2p).

This deliberately selects primes with (2/p)=-1. It avoids, rather than ignores, the degenerate-constant obstruction described in JACOBI_VALUATION_UNION.md for unsuitable whole cyclotomic moduli.

The constants c_p can be correlated across primes. This is immaterial: their tests depend only on m modulo distinct primes. CRT gives the exact product of failure proportions in a complete period, bounded above by epsilon. All selected primes are coprime to999, so conditioning on the endpoint classes does not change that product. No randomness assumption is used.

## 3. Local squares and exclusion of every integer exponent

For h=v_3(d)=1, the published cubic formula still reduces to

    10^(-D(k))*R_(m,k)=T_m modulo27.

Both endpoint classes8 and18 give T_m=9 modulo27. Thus all rotations have exact3-adic valuation2, with normalized unit1 modulo3; all are Q_3 squares. Any integer prime-power exponent would have to divide2, and hence would have to be2. The negative Legendre symbol at any selected prime rules out this last exponent.

Because37 divides d and3 divides d, the published37-prefix formula simplifies to

    W_m=T_m+11d=T_m modulo37.

There are exactly18 residues modulo37 for which T_m is a nonzero square: its discriminant1 is nonzero, it has two roots, and its character sum is1. Both endpoint classes modulo27 combine with each such residue, giving36 classes modulo999. Since3 divides D(m), 37 divides the cyclic modulus; and10 is a square modulo37. Every rotation of those blocks is therefore a nonzero square modulo37 and a square in Q_37.

## 4. Uniform endpoint-interval error

All conditions have common period T=999 product_p p. The successful density in a complete period is at least (4/111)(1-epsilon). Discarding an incomplete period loses at most T successes, so the number certified is at least

    (4H/111)*(1-epsilon)-T.

Let K=1233 be the decimal digit length of T. Since d>=L>=K+200 and T<10^K,

    T/H <10^(-199)/9,
    T/((4/111)H) <(111/36)*10^(-199)<2^(-640).

The last numerical inequality can be checked by integer arithmetic. Combining epsilon<2^(-323) with this bound gives the stated1-2^(-322) lower count. Dropping the37 condition increases the endpoint density to2/27 and can only reduce the relative interval error, proving the second assertion.

## 5. Novelty and verification scope

The earlier infinite Jacobi unions required v_3(d) to grow. Here it stays exactly1. The ingredient is a finite, explicitly verified prime set with compatible width periods, not an unproved supply of infinitely many primes or a claim about unknown concatenation constants. The underlying quadratic reduction and CRT mechanism are inherited; the new contribution is the bounded-valuation compatible certificate and its quantitative conditional coverage.

The script verifies primality, all modular exponent conditions, the exact L and T, and the rational epsilon inequality without numerical approximation. It also exhausts small quadratic-character models and finite CRT counts. It does not construct prefixes at612-digit digit widths or enumerate their endpoint intervals; no such computation is claimed. The whole-block and infinite-progression conclusions follow from the proof. The main manuscript and PDF are unchanged.

Run `python papers/A001292/verify_bounded_valuation_crt.py` from the repository root. The verifier uses only the Python standard library and the accompanying JSON certificate.
