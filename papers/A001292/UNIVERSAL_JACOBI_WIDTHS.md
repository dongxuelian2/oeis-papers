# Uniform Jacobi coverage at every high-3-valuation digit width

This supplement extends CYCLOTOMIC_JACOBI_UNION.md. It removes the restriction on the digit width modulo37, uses both locally surviving endpoint classes modulo27, and gives an explicit cutoff tradeoff. These are sufficient integer nonpower certificates, not a complete classification.

## Theorem and explicit bound

Let d be a decimal digit width, h=v_3(d)>=2, q=3^h and H=9*10^(d-1). Put

    Q_j=(10^(2*3^(j-1))+10^(3^(j-1))+1)/3.

Let 2<=J<=h. An endpoint m with d digits is certified if

    m=8 or18 modulo27,
    (W_m/Q_j)=-1 for some J<=j<=h.

Every certified block consists entirely of integer nonpowers, although all its rotations are squares in Q_3. There is no restriction on d modulo37.

For h>=J>=5, define

    E(h,J)=2^(-(h-J+1)) * (h+1)(h+2)(h+3)(h+4) / [J(J+1)(J+2)(J+3)].

The number of certified endpoints is at least

    (2H/27) * [1-E(h,J)-45/(37*3^h)].

A negative right-hand side is simply a vacuous lower bound. Every prime factor of every modulus tested exceeds 2*3^J.

Consequences, all uniform in d/q:

* For fixed J=5, the fraction of failures within the two endpoint classes is O(h^4*2^(-h)). The certified count is (2H/27)*(1-O(h^4*2^(-h))).
* For J=max(5,ceil(log_3(h))), once J<=h, the failure fraction is O(h^(4+log_3(2))*2^(-h)). All witness primes exceed 2h, hence eventually avoid any prescribed finite prime set.
* For fixed 0<theta<1 and J=ceil(theta*h), the failure fraction is O_theta(2^(-(1-theta)*h)), with every witness prime exceeding 2q^theta.

The proportions are in digit-width endpoint intervals and in the two stated congruence classes. They are not a density assertion about all A001292 entries or all digit widths. No assertion is made that every endpoint in those classes is eventually certified.

## Proof

The preceding supplements prove that the Q_j are pairwise coprime and coprime to30; every prime divisor has order3^j for10, and (10/Q_j)=1. They divide 10^d-1 and 10^D(m)-1 whenever j<=h, because q divides both d and D(m). Here

    D(m)=d(m+1)-(10^d-1)/9,
    v_3((10^d-1)/9)=h.

For 3|d the exact prefix congruence is W_m=T_m modulo27, where T_m=m(m+1)/2. Both roots of T_m=9 modulo27 are m=8,18. Thus W_m has 3-adic valuation2 and normalized unit1 modulo3. The cyclic modulus has valuation at least h+2>2, and10 is1 modulo9. The rotation identity therefore gives the same valuation and normalized residue for every rotation. All rotations are Q_3 squares; any integer prime-power exponent must divide2 and hence must be2. A negative Jacobi symbol at any Q_j excludes that last possibility for every rotation, since (10/Q_j)=1. This establishes the certificate without a condition at37.

On a fixed digit interval, W_m modulo Q_j is T_m+c_j for a constant c_j depending on d. The uniform character lemma already proved gives a failure fraction s_j (symbols0 or+1) satisfying

    s_j<=1/2+2/j.

It includes the degenerate-discriminant case and all prime multiplicities. CRT gives exact product failure fraction product s_j among residues satisfying either of the two endpoint classes modulo27. It is not a randomness assertion. For h>=J>=5,

    product_{j=J}^h s_j <= 2^(-(h-J+1)) product_{j=J}^h (j+4)/j = E(h,J).

The product telescopes exactly. All these tests have a common period dividing

    T=27 product_{j=2}^h Q_j
      =(10^q-1)/(37*3^(h-1)).

The certified density in a complete period is at least (2/27)(1-E). In any interval of length H the certified count is at least H times this density minus T, by discarding the incomplete period. Since d>=q,

    T/H <=10/(111q),
    T/(2H/27)<=45/(37q).

This proves the bound. The finite-class count itself is 2H/27+O(1), so the corresponding conditional failure proportions follow too. For logarithmic J, once h is large enough that ceil(log_3(h))>=5, use 2^J<=2*h^(log_3(2)); for linear J the rational product in E is bounded by a constant depending only on theta. The error3^(-h) is absorbed in each displayed asymptotic. The order property gives the asserted lower bound on witness primes.

## Exact compatibility with the37 square test

The new universal theorem need not pass the37 square test. We can describe precisely which of its endpoint residue classes do, rather than assuming d is a square modulo37. For 3|d,

    W_m=T_m+11d modulo37.

Put a=d modulo37, Delta=1-88a modulo37, and let r(a) be the number of b modulo37 for which T_b+11a is a nonzero square. Direct quadratic-character summation gives

    r(a)=18 if Delta is a nonzero square;
    r(a)=19 if Delta is a nonsquare;
    r(a)=0 if Delta=0 (equivalently a=8).

Indeed, for nonzero Delta the sum of Legendre symbols is -(2/37)=1 and the number of zeros is2 or0. Thus the number of positive signs is (38-number_of_zeros)/2. If Delta=0, the polynomial is one half times a square, and (2/37)=-1, so every nonzero value is a nonsquare.

Each admissible b combines with both endpoint classes modulo27 by CRT. As every Q_j for j>=2 is coprime to999, the same argument, using period999 product Q_j, proves at least

    (2*r(a)/999)*H*(1-E(h,J))-3*(10^q-1)/q

certified endpoints passing both Q_3 and Q_37 square tests. For any phase a!=8, this is (2*r(a)/999)*H*(1-o(1)) under the cutoff choices above. No nonzero Q_37-square class exists in phase a=8; the one zero class is not classified as a Q_37 square or nonsquare here. The universal nonpower theorem still applies in that phase. A varying sequence of digit widths may have varying r(a); the estimates remain uniform.

For the nonzero-square classes, 37 divides the cyclic modulus and10 is a square modulo37, so every rotation is a nonzero square modulo37 and therefore a square in Q_37. This is stronger compatibility than merely a prefix condition. It does not assert compatibility with every other local test.

## Novelty and finite verification

The previous union theorem used only m=666 modulo999 and required d to be a nonzero square modulo37; its particular cutoff was ceil(h/2). The present result certifies asymptotically a proportion2/27 of endpoints at every width with h tending to infinity, provides all37 phases explicitly, and supplies the cutoff/prime-size/error tradeoff. The global conjecture remains open. The main manuscript and PDF are unchanged.

The accompanying finite script exhausts the27 and37 residue calculations, checks the exact rational product formula at finitely many h,J, and tests selected endpoints and prefixes at selected actual widths. It does not enumerate those full digit intervals or every rotation; the uniform and whole-block assertions follow from the proof above.

Run from the repository root with `python papers/A001292/verify_universal_jacobi_widths.py`. The verifier imports the sibling modules `verify_cyclic_jacobi_certificate`, `verify_cyclotomic_jacobi_family`, and `verify_a001292`; keep those published scripts beside it, or add their directories to PYTHONPATH when auditing a separated working copy.
