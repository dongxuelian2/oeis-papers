# Local square survivors for all primes up to twice the digit width

This supplement establishes a limitation of growing-prime tests, rather than another exclusion family. It constructs many endpoint indices whose same unrotated concatenation is a square in every Q_p with p<=2d, where d is the endpoint's digit width. It does not construct any integer square.

## Theorem

Let d tend to infinity through prime integers. Among the d-digit decimal endpoint indices m, the number satisfying

    m=1 modulo 120,
    W_m is a nonzero square modulo every prime 5<p<=2d

is

    (1+o(1)) 9*10^(d-1) delta_d,
    delta_d=(1/120) product_{5<p<=2d} (p-1)/(2p).

In particular, this number is

    10^d exp(-(2 log 2+o(1)) d/log d).

For each such m, the same integer W_m is a square in Q_p for EVERY prime p<=2d. These local square assertions hold at arbitrary p-adic precision. The count tends to infinity. Kashihara's integer perfect-power conjecture remains open.

## 1. Eligibility at prime digit widths

Put B=10^d. For p>5 with p<=2d, write r=ord_p(10). If p divided B-1, then r would divide the prime d, so r would be 1 or d. The first case would force p|9 and is impossible for p>5. In the second case d divides p-1. For an odd prime d and an odd prime p, this forces p>=2d+1: p=d+1 is even and greater than 2. This contradicts p<=2d.

Thus every prime 5<p<=2d is eligible for the affine-exponential prefix formula from the earlier supplements: on the fixed width,

    W_m=alpha_p B^m+beta_p m+gamma_p (mod p),
    beta_p=-(B-1)^(-1) !=0.

The coefficients depend on the width; no global periodicity of W_m is asserted.

## 2. Exact density and a much smaller common period

Start with m=1 modulo 120. Add the primes p>5 up to 2d in increasing order. The exact joint-density lemma gives a fraction (p-1)/(2p) for the nonzero square condition at p. Its induction is valid with the starting modulus 120 because its largest prime factor is 5. For each new prime p, the earlier period and p-1 have no factor p; fixing their least common multiple makes the exponential constant modulo p, and the p lifts give an affine bijection.

Therefore the joint conditions have density delta_d in the period

    Q_d=lcm(120, {p(p-1):5<p<=2d}).

The number of allowed classes is exactly Q_d delta_d. In a d-digit interval of length H_d=9*10^(d-1), their count is H_d delta_d+O(Q_d), with absolute implied constant at most 1.

Crucially, if y=2d, every p(p-1) with p<=y divides lcm(1,...,y). Both p and p-1 divide that least common multiple, and they are coprime. Also 120 divides it for y>=8. Hence

    Q_d divides lcm(1,...,2d),
    log Q_d <= psi(2d)=2d+o(d).

Here psi is the Chebyshev function and the displayed asymptotic is the ordinary prime number theorem. A product of the individual periods would give a substantially weaker bound; it is not used.

## 3. Main term dominates the full-period error

The ordinary prime number theorem and Mertens' product estimate give

    log delta_d
       =-(pi(2d)-3)log 2 + sum_{5<p<=2d}log(1-1/p)-log120
       =-(2 log 2+o(1))d/log d.

It follows that

    log(H_d delta_d)=d log10-O(d/log d).

Since log10>2, the ratio Q_d/(H_d delta_d) tends to zero exponentially in d. The interval count is therefore (1+o(1))H_d delta_d, proving the asserted asymptotics.

No theorem about primes in growing arithmetic progressions is involved. The inputs here are the ordinary prime number theorem and Mertens estimates.

## 4. Local squares at arbitrary precision

For p>5 the residue W_m is a nonzero square modulo p, so Hensel lifting makes W_m a square in Q_p. For the remaining primes use m=1 modulo120 and d>=3:

- W_m=1 modulo8, because the final d-digit integer block gives W_m=m modulo8. This is the criterion for an odd 2-adic unit to be a square.
- W_m=m(m+1)/2=1 modulo3, using decimal digit sums and m=1 modulo3. Thus W_m is a square in Q_3.
- W_m=m=1 modulo5, so W_m is a square in Q_5.

All these are unit squares. Consequently arbitrary powers of these primes, or their products via CRT, cannot exclude these same candidates by a necessary square-residue test.

## 5. What this does and does not establish

The finite-prime limitation theorem previously fixed a finite prime set before letting endpoints grow. Here the set includes EVERY prime up to 2d and grows with the endpoint size, on every sufficiently large prime-width block. The lower bound has a stretched-exponential survival factor, on the same d/log d scale that appears in the upper bounds for growing-prime square sieves.

This is not a claim of matching constants or of optimality for every sieve. It applies to unrotated candidates and the stated prime cutoff; larger primes, other integer information, or a different global argument may still exclude them. It does show why arbitrary p-adic precision at all primes p<=2d cannot alone yield a universal individual-square exclusion.

In particular, neither these local survivors nor the positive lower count supplies an integer counterexample. The upper bounds for actual integer powers and these lower bounds for local candidates are consistent.

## 6. Finite verification

The accompanying script computes the exact residue classes at prime widths 5, 7 and 11 by successive period lifting, checks the expected density and least-common-multiple bound, counts the actual endpoints, and independently verifies selected candidate prefix residues by matrix concatenation. The direct prefix tests cover only selected candidates, not every endpoint counted by the exact residue-class computation. The infinite theorem is established above, not inferred from these finite instances. The main manuscript and PDF are unchanged.
