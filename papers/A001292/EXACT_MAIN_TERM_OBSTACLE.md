# Why an exact-power main term does not give a new global exclusion here

This is a limitation of one proposed method, not a limitation of all global methods. It does not settle Kashihara's conjecture.

Write W_j for the decimal concatenation of 1,...,j, with W_0=0, and D(j) for its total digit length. The whole-integer rotation is R_(m,k)=10^(D(k))W_m-(10^(D(m))-1)W_k.

Fix d>=2, B=10^d, L=10^(d-1), C=B-1, G=10^(D(L-1)), and

    A=C^2 W_(L-1)+LC+1.

Let L+7<=k<m<=B-1, K=k-L+1>=8, and N=m-L+1. The exact same-width formulas are

    C^2 W_k=A B^K-(kC+B),
    C^2 R_(m,k)=G(kC+B)B^N+(A-G(mC+B))B^K-(kC+B).

The natural leading term is the positive rational number

    F=G(kC+B)B^N/C^2.

## Proposition

1. F is never a rational ell-th power for an odd prime ell.
2. If F is a rational square, then R_(m,k) is not a square in Q_2.

Thus, in this range of cuts, forcing this particular leading term to be an exact rational power and then invoking an archimedean gap cannot furnish a new square exclusion beyond the 2-adic obstruction. This does not say that every nonsquare rotation is a nonpower: other prime exponents still need exclusion.

## Proof of the odd-exponent assertion

Put J=kC+B. Since B=1 modulo C, gcd(J,C)=1; also gcd(10,C)=1. At each prime p dividing C, the valuation of F is exactly -2v_p(C). If F were an ell-th power for odd prime ell, all v_p(C) would be divisible by ell. Thus C would be an integer ell-th power.

In fact 10^d-1 is not an odd-prime power. If ell is neither 2 nor 5, exponentiation by ell is a bijection on the units modulo 10^d. A positive root t with t^ell=10^d-1 would therefore satisfy t=-1 modulo 10^d, impossible since 1<t<10^d-1. If ell=5, reduction modulo 2^d gives t=-1 modulo 2^d, because fifth powering is a bijection on that unit group. Thus t>=2^d-1>10^(d/5) for d>=2, again impossible. For the displayed inequality, use 2^d-1>=(3/4)2^d and check it at d=2; its ratio to 10^(d/5) then increases with d. This proves assertion 1.

## Proof of the square assertion

Since G B^N is a power of 10 and C^2 is a square, F being a rational square implies

    J=10^e t^2,       e in {0,1},       t a positive integer.

Indeed, all prime valuations outside 2 and 5 must be even, and the parities at 2 and 5 must agree. Write v=v_2(J). Since k<B,

    0<J<B^2,       v<2d log_2(10)<7d.

The integer A satisfies v_2(A)>=0, while v_2(B^K)=dK>=8d. For d>=2 this implies dK-v>=3 (the valuations are integers). Thus the first exact formula, divided by 2^v and reduced modulo 8, yields

    v_2(W_k)=v,
    W_k/2^v = -(J/2^v)/C^2 (mod 8).

If e=1, v is odd, so W_k is not a 2-adic square. If e=0, v is even and J/2^v is an odd square; C is odd, so W_k/2^v=-1=7 modulo 8, again not a 2-adic square.

Finally, the rotation ends with the complete prefix W_k. Since

    D(k)=D(L-1)+dK>=9+8d>v+3,

its difference from W_k is divisible by 2^(v+3). Equivalently, the defining rotation formula gives R_(m,k)=W_k modulo 2^D(k). Hence R_(m,k) has the same obstructing 2-adic valuation and unit as W_k. This proves assertion 2.

## Boundaries and interpretation

The condition K>=8 is a simple sufficient bound, not asserted optimal. The first few cuts of a width, cuts in earlier widths, nonexact algebraic leading terms, other rearrangements, and methods using several approximations are not ruled out. No assertion is made that a 2-adic square is an integer square. No new individual integer counterexample or proof of the full conjecture is supplied.

The negative result explains why several apparent infinite families obtained by a near-square gap argument are mathematically redundant. It prevents counting them as new progress and identifies where a genuinely different global argument would have to depart from this setup.

## Finite audit

Run `python verify_exact_main_term_obstacle.py` for 99,958 prefix-identity checks modulo 2^64 at widths 2 through 5. It also identifies 11 rational-square main-term cases, chooses one valid endpoint for each, and checks the rotation identity and its obstructing 2-adic valuation/unit. These are finite modular checks and selected endpoint tests, not an exhaustive test of all rotations. The unbounded propositions follow from the proofs above.
