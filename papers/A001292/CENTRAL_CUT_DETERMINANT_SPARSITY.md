# An elementary all-cut square-count bound within one decimal width

The elementary determinant argument below removes the central-cut exception in `UNIFORM_CUT_SPARSITY.md`. It is uniform over the squareclass of the cut parameter. No Subspace Theorem, approximation theorem, or ineffective exceptional threshold is used.

## Theorem

Let `d >= 2`, `B=10^d`, and `L=B/10`. Let `W_m` denote the decimal concatenation `123...m`, and let `R_(m,k)` be the integer obtained by moving its whole-integer prefix `123...k` to the end. The number of pairs satisfying

    2L <= m <= B-1,       L+7 <= k < m,
    R_(m,k) is an integer square

is less than

    32 B (1 + floor(log_2(18d))).                       (T)

In particular it is `O(B log d)`. There is no early/late condition on the cut. The central band from the earlier note is included in its entirety. All constants and thresholds here are effective.

Summing over decimal widths gives `O(X log log X)` pairs with endpoint `m<=X` **in precisely the stated parameter ranges**. This does not count cuts in earlier digit widths, cuts `k<L+7`, or endpoints `m<2L`. It is a sparsity theorem, not nonexistence, and not a solution of the integer-power conjecture.

## 1. Exact setup and the approximation bound

Set

    C=B-1,   t=D(L-1)=((9d-10)L+1)/9,   G=10^t,
    A=C^2 W_(L-1)+LC+1,
    N=m-L+1,   K=k-L+1,
    J=kC+B,   M=mC+B.

The exact identity inherited from the prior notes is

    C^2 R_(m,k) = G J B^N - (GM-A)B^K - J.              (1)

Thus `8<=K<N`, `L+1<=N<=9L`, and

    B^2/10 < J < B^2,   0 < A/G < B^2/8.

Put

    T_N=(GM-A)B^K+J.

Throughout the domain,

    0 < T_N < 2G B^(K+2).                              (2)

Suppose `R_(m,k)=y^2`, and write

    x=Cy,   t+dN=2q+e,   Q=10^q,   e in {0,1},
    alpha=sqrt(10^e J).

Then

    x^2=alpha^2 Q^2-T_N,   x^2=-J modulo B^K,           (3)
    0 < alpha-x/Q < 20 B^(K-N+1).                     (4)

For clarity, (4) follows by factoring the difference of squares:

    alpha-x/Q = T_N / [Q^2(alpha+x/Q)].

Use `Q^2=GB^N/10^e`, `alpha>10^(e/2)B/sqrt(10)`, and (2). The resulting coefficient `2 sqrt(10) 10^(e/2)` is at most 20; the other inequalities are strict.

## 2. At most eight congruence branches, not eight times a smooth factor

Fix `d,k`. Put `n=dK`. Since `J<B^2`,

    v_2(J)<7d<n,   v_5(J)<3d<n.

For any square solution, (3) therefore forces

    2v_p(x)=v_p(J)             for p=2,5.              (5)

If either valuation is odd, this cut has no square solutions. Otherwise write

    v_2(J)=2a,   v_5(J)=2b,   z=2^a 5^b < B,
    r=2^(n-a)5^(n-b)=B^K/z.

All possible `x` belong to at most eight residue classes **modulo r**.

Indeed, put `a_p=v_p(J)/2`. Dividing `x^2=-J modulo p^n` by `p^(2a_p)` gives a unit-root equation modulo `p^(n-2a_p)`. There are at most four unit roots for `p=2`, and at most two for `p=5`. Multiplication by `p^(a_p)` specifies the residue of `x` modulo `p^(n-a_p)`. The Chinese remainder theorem now gives at most `4*2=8` classes modulo `r`. This is different from counting all roots modulo `B^K`, which would give a bound `8z` and lose uniformity in this argument.

## 3. Strict concavity eliminates every zero determinant

Continue to fix `d,k`, and also fix `e`. For the moment allow `N` to vary continuously over

    max(L+1,K+1) <= N <= 9L.

Define `Q=10^((t+dN-e)/2)` and the positive real curve

    F(Q)=sqrt(alpha^2 Q^2-T_N).

The expression under the square root is positive throughout this interval: by (2),

    T_N/(GJB^N) < 20 B^(K-N) <= 20/B <= 1/5.

The estimates used in (2) remain valid for real `N` in this interval, since `M=(N+L-1)C+B` is still between its endpoint bounds.

Let

    a_0=GC B^K > 0.

As a function of `N`, `T_N=a_0 N+b_0` for a constant `b_0`. Therefore, as a function of `Q`,

    T_N=lambda log Q+mu,   lambda=2a_0/log B > 0.       (6)

Here and below `log` in a derivative calculation is the natural logarithm. Direct differentiation gives

    4 F(Q)^3 F''(Q)
      = alpha^2(6lambda-4T_N)
        -lambda(2T_N+lambda)/Q^2.                     (7)

Both terms on the right are negative. To verify the only nontrivial condition, note that

    T_N/a_0 = m+B/C-A/(GC)+J/(GC B^K)
            > B/5-B^2/(8C)
            > B/20 >= 5,

where `B^2/(8C)<3B/20` holds for `B>=100`. In contrast,

    (3lambda/2)/a_0 = 3/log B < 1.

Thus `T_N>3lambda/2`, and (7) proves `F''(Q)<0` throughout the interval.

Consequently any three distinct points of the curve are noncollinear. In particular, for any three square solutions with the same `d,k,e`, ordered by increasing `N`,

    Delta = det [ x_1  Q_1  1 ]
                [ x_2  Q_2  1 ]
                [ x_3  Q_3  1 ]                       (8)

is nonzero. This is the necessary obstruction check: a small determinant alone would not give a count if arbitrarily many solutions could lie on one rational line.

## 4. Congruence divisibility and the centered triple gap

Restrict further to one of the at most eight residue classes modulo `r`. Because the parity `e` is fixed, the integer powers of ten satisfy

    Q_1 | Q_2 | Q_3.

If `beta` is the common residue of the `x_i` modulo `r`, subtracting `beta` times the third column from the first column in (8) shows that its first column is divisible by `r`. Its second column is divisible by `Q_1`. Since the determinant is a nonzero integer,

    r Q_1 <= |Delta|.                                  (9)

Put `delta_i=alpha Q_i-x_i`. By (4),

    0<delta_i<20 Q_i B^(K-N_i+1)
                <=20 Q_1 B^(K-N_1+1)=E_1.

The latter inequality follows from

    Q_i B^(-N_i)=10^((t-e)/2) B^(-N_i/2).

Subtracting `alpha` times the second column from the first in (8), and expanding the determinant, gives

    |Delta|
      <= delta_1(Q_3-Q_2)+delta_2(Q_3-Q_1)
         +delta_3(Q_2-Q_1)
      <2E_1 Q_3
      =40 Q_1 Q_3 B^(K-N_1+1).                        (10)

Combining (9), (10), and `r=B^K/z` yields

    Q_3 > B^(N_1-1)/(40z) > B^(N_1-2)/40.

Since `Q_3=10^((t+dN_3-e)/2)`,

    N_3 > 2N_1-t/d-4-(2log_10(40)-e)/d
        > 2N_1-t/d-6.                                (11)

For the last strict inequality, `d>=2`, `e>=0`, and `40<100` suffice. There is no `K` in this gap inequality. The real and local factors `B^K` cancel.

Set

    h=N-t/d-6.

Then every triple in the fixed `(d,k,e,beta)` group satisfies

    h_3>2h_1.                                        (12)

## 5. Counting the triples

First suppose `d>=3`. At the first possible endpoint,

    h >= L+1-t/d-6
       =10L/(9d)-5-1/(9d)
       >=L/(2d).                                     (13)

Indeed, this is equivalent to `11L>=90d+2`; it holds at `d=3`, and thereafter follows immediately by induction from `L=10^(d-1)`. Also `h<9L` throughout the domain.

List the solutions in one fixed group in increasing order. The odd-indexed sequence of `h` values doubles strictly by (12), and so does the even-indexed sequence. If either sequence has `s>=1` terms, then

    2^(s-1) < 9L/(L/(2d))=18d.

It follows that

    s <= 1+floor(log_2(18d)).

Each group therefore has at most `2(1+floor(log_2(18d)))` solutions. There are at most eight residue classes, two parities, and fewer than `B` cuts. This proves (T) for `d>=3`.

For `d=2`, the entire admissible domain contains only

    sum_(m=20)^99 (m-17)=3400

pairs, without imposing the square condition. This is less than the stated bound `32*100*(1+floor(log_2 36))=19200`. Thus the theorem holds for every `d>=2`; this small-width observation is a count of the domain, not a finite search used to justify the general theorem.

An alternative completely uniform centered estimate, if desired, is

    h >= L/(10d)       for every d>=2.

It follows from `L>=5d`, which gives `91L>=450d+10`. The same proof, with no separate width-2 case, gives the slightly looser count `32B ceil(log_2(90d))`. In particular the earlier preliminary bound `128dB` follows from `90d<2^(4d)` for `d>=2`.

## 6. Cumulative bound and exact scope

Let `D` be the number of decimal digits of `floor(X)` and suppose `D>=2`. Since the logarithmic factor in (T) is increasing with `d`, summing over complete widths gives the explicit bound

    (3200/9) X (1+floor(log_2(18D))).                  (14)

Here we used `sum_(d=2)^D 10^d <10^(D+1)/9` and `10^D<=10X`. This proves the stated `O(X log log X)` asymptotic for the specified pairs.

The conclusion permits infinitely many square rotations, and it permits infinitely many occupied squareclasses. It excludes neither all remaining squares nor higher powers of other prime exponents. No inference is made about cuts in earlier digit widths or the initial part of an endpoint width.

The new ingredients relative to the previous elementary early/late count are the reduced root-branch modulus, strict concavity of the exact square-root curve, and the three-point determinant gap. “New” refers to this development, not a literature-priority claim.

## 7. Finite audit

`verify_central_cut_determinant.py` audits the inherited identity and approximation inequalities; the exact polynomial differentiation identity underlying (7); branch compression at small moduli; determinant divisibility and the error-column determinant bound on synthetic examples; the centered lower bounds and counting constants at widths 2 through 1000; and all 3400 admissible width-2 pairs plus selected width-3 pairs. Its certificate distinguishes these finite checks from the proof of the theorem.

The completed finite audit checks all 3400 width-2 pairs (including 410 central-band pairs), 42 selected width-3 pairs, 3154 prime-power and 979 decimal CRT compressed-branch cases, 2993 root valuations, the exact concavity polynomial identity, 504 synthetic nonzero determinant/divisibility cases, 12 synthetic error bounds, and centered constants at widths 2 through 1000. Synthetic cases are explicitly not claimed to be actual square rotations.
