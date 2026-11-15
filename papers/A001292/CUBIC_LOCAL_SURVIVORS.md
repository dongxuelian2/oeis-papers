# Integer nonpowers inside Q_3-cube blocks

Earlier Jacobi and3/13/37 square certificates used blocks that are squares in Q_3. This supplement gives an infinite family disjoint from those: all rotations are cubes in Q_3 but not squares there, yet none is an integer perfect power. The mechanism uses the cubic residue character at37 and an infinite union of power-of-three valuations, rather than a finite list of endpoints.

## Structural certificate

Let d be a decimal digit width, h=v_3(d), and b=3^r with r>=1 and b<=h. Suppose the d-digit endpoint m lies in one of the four classes

    m=2*3^b, 7*3^b, 2*3^b-1, or7*3^b-1 modulo3^(b+2).

Put f_d(m)=m(m+1)/2+11d modulo37. If f_d(m) is a nonzero noncube modulo37, every rotation in the block is an integer nonpower. All rotations are cubes in Q_3, not squares in Q_3, and noncube units in Q_37.

This is a sufficient criterion, not an equivalent classification. It does not address the global conjecture at every endpoint or at bounded h.

## Proof of the local and integer assertions

The inherited cubic congruence reduces, for h>=1, to

    10^(-D(k))*R_(m,k)=T_m modulo3^(h+2).

For the four displayed classes, T_m has exact3-adic valuation b and normalized unit congruent to1 or-1 modulo9. Indeed for m=3^b*u this unit is u/2 modulo9, and for m=3^b*u-1 it is -u/2 modulo9. Since b>=3, the omitted terms are divisible by9. The choices u=2 or7 modulo9 give exactly the desired units. Conversely these are precisely the four residue classes with valuation b and normalized unit±1 modulo9.

Since b<=h, the inherited congruence has enough precision to preserve the valuation and normalized unit modulo9. Also10^D(k)=1 modulo9. Hence every rotation has exact valuation b and normalized unit±1 modulo9.

A nonzero3-adic number is a cube if and only if its valuation is divisible by3 and its normalized unit is±1 modulo9. For sufficiency on units, the polynomial t+3t^2+3t^3 has derivative1 modulo3; Hensel lifting in (1+3t)^3=1+9(t+3t^2+3t^3) gives all units1 modulo9, and the negative sign is a cube too. Thus every rotation is a Q_3 cube. Its odd valuation b=3^r prevents it from being a Q_3 square.

Every prime exponent of an integer perfect power must divide that same valuation b, so the only possible prime exponent is3. The published37-prefix identity gives W_m=f_d(m) modulo37 because3 divides d. Moreover3 divides D(m), so37 divides the cyclic modulus. Finally10 is a cube modulo37, since10^12=1 modulo37 and the multiplicative group has order36. Therefore the cubic residue class of W_m is preserved by multiplication by10^D(k) at every cut. A noncube unit at37 excludes integer cubes, ruling out the last possible exponent.

Only the assertion10^12=1 is needed in that step; the explicit cube subgroup is

    {1,6,8,10,11,14,23,26,27,29,31,36}.

## Infinite valuation union and uniform density

For each a modulo37 let n_a be the number of residues x modulo37 such that T_x+11a is a nonzero noncube. The complete37-element phase count gives, for a=0,...,36,

    20,25,20,23,25,25,27,28,24,28,27,25,25,23,20,25,20,21,28,
    28,21,23,20,27,21,27,23,23,27,21,27,20,23,21,28,28,21.

This is an exact finite residue calculation, with20<=n_a<=28, not extrapolation from endpoint samples. It can be reproduced by cubing1,...,36 and evaluating the37 quadratics.

Define

    K=sum_{r>=1}4/3^(3^r+2)=0.01648348546693042896... .

Let B be the largest power of3 not exceeding h, h>=3, and put

    K_h=sum_{3<=b<=B, b a power of3}4/3^(b+2).

The endpoint classes for distinct b are disjoint because their T_m valuations differ. Their exact density is K_h and their joint period is3^(B+2). CRT with37 gives a certified density (n_(d mod37)/37)*K_h in a full period

    T=37*3^(B+2)<=333*3^h.

The omitted tail satisfies

    0<=K-K_h<=sum_{n>=3B}4/3^(n+2)
                 =(2/3)*3^(-3B)<=2*3^(-(h+2)).

For H=9*10^(d-1), d>=3^h, discarding an incomplete period loses at most T endpoints. Consequently the number certified is at least

    H*[(n_(d mod37)/37)*K
       -2*3^(-(h+2))-370*3^h/10^(3^h)].

In particular it is at least

    H*[(20/37)*K-O(3^(-h))],
    (20/37)*K=0.00890999214428671835... .

The estimates are uniform in d/3^h. They concern endpoint proportions within each stated digit-width interval, not a natural density over all sequence terms or widths. No finite sample is used to establish the infinite sum or limit.

## Scope and relation to prior results

The underlying cubic congruence and37-prefix quadratic are inherited. The new contribution is their combination with the cubic character at37, the power-of-three valuation endpoint family, and its infinite-union count. The family is genuinely outside all Q_3-square-block certificates discussed earlier, because every valuation here is odd. It is not outside every possible previous local method, and no claim is made that individual small endpoints were unknown.

No universal coverage or full integer classification follows. The main manuscript/PDF remain unchanged.

## Verification

The verifier exhausts the37 character phases and the endpoint roots at valuations3 and9, checks finite rational tail/period bounds, and directly computes selected prefixes at widths27,54,81. It does not enumerate all rotations in those large blocks or test arbitrarily high valuations individually. The whole-block and infinite-union assertions are proved above.

Run `python papers/A001292/verify_cubic_local_survivors.py`; the script imports the sibling matrix-prefix routine from `verify_antiperiodic_thirteen.py`.

For separated audit copies, place the already published sibling dependency on PYTHONPATH; it is not duplicated in this incremental supplement.
