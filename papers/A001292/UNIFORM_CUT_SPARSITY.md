# An effective square-count bound outside a central cut band

This note proves an elementary count that is **uniform over all squareclasses**. It does not prove that the count is zero. It uses no Roth, Ridout, or Subspace Theorem, and has no ineffective exceptional threshold.

## Theorem

Let `d >= 2`, `B = 10^d`, `L = B/10`, and `C = B-1`. Let `W_m` be the decimal concatenation `123...m`, and let `R_(m,k)` be the whole-integer rotation obtained by moving the prefix `123...k` to the end. Consider

    2L <= m <= B-1,       L+7 <= k < m.

Put

    t = D(L-1) = ((9d-10)L+1)/9,
    N = m-L+1,            K = k-L+1,
    H = t+dN,
    rho = 2d(N-K-1)/H,    tau = 2dK/H.

At this width, the number of pairs `(m,k)` for which `R_(m,k)` is an integer square and

    rho >= 1    OR    tau >= 1                            (T)

is at most

    (32d+44)B.

More specifically, the early region `rho >= 1` contains at most `(8d+6)B` such pairs, and the late region `tau >= 1` contains at most `(24d+37)B`. Their sum even gives `(32d+43)B`; the displayed theorem keeps one unit of slack in the constant.

The statement holds for every `d >= 2` and includes the natural boundary `rho=1` or `tau=1`, with no positive-margin condition. The squareclass of `k(B-1)+B` is unrestricted and may vary with both width and cut.

## 1. Exact identities and elementary estimates

Set

    G = 10^t,
    A = C^2 W_(L-1) + LC + 1,
    J = kC+B,            M = mC+B.

The inherited exact rotation identity is

    C^2 R_(m,k) = G J B^N + (A-GM)B^K - J.                (1)

Here `8 <= K < N`, `L+1 <= N <= 9L`, `t < dL`, and

    B^2/10 < J < B^2,     B^2/5 < M < B^2,
    0 < A/G < B^2/8.

For completeness, `W_(L-1)/G < 1/8` because its decimal expansion starts `.1234`. Also `t >= 2d` and `LC+1 < B^2`, so `A/G < C^2/8+1 < B^2/8`. The bounds on `J` and `M` follow directly from their ranges.

Define

    T = (GM-A)B^K + J.

Then

    0 < T < 2G B^(K+2),
    C^2 R_(m,k) = G J B^N - T,
    C^2 R_(m,k) = -J modulo B^K.                          (2)

Suppose now that `R_(m,k)=y^2`, with `y` a positive integer, and put `x=Cy`. Write

    H = 2q+e,     e in {0,1},     Q=10^q,
    alpha = sqrt(10^e J).

Equation (2) gives the one-sided approximation

    0 < alpha-x/Q
      = T / [Q^2(alpha+x/Q)]
      < 20 B^(K-N+1).                                    (3)

Indeed, `Q^2=GB^N/10^e` and `alpha > 10^(e/2)B/sqrt(10)`. In particular, the denominator in (3) exceeds `GB^N B/(sqrt(10)10^(e/2))`, which gives the constant 20.

Two useful uniform size bounds are

    dL/2 <= q < 5dL.                                     (4)

The lower bound follows from `N >= L+1` and `e <= 1`; the upper bound follows from `N <= 9L` and `t < dL`.

## 2. Local valuations fix the displayed numerator's 2-adic order

Let `n=dK`. For `p=2,5`, the congruence in (2) gives `x^2 = -J modulo p^n`. Moreover,

    v_2(J) < 7d,       v_5(J) < 3d,       n >= 8d,         (5)

because `J < 10^(2d) < 2^(7d)` and `J < 10^(2d) < 5^(3d)`.

Consequently

    2 v_p(x) = v_p(J)    for p=2,5.                       (6)

To see this, if `v_p(x^2)` differed from `v_p(J)`, the valuation of `x^2+J` would be their minimum, strictly less than `n`. If both valuations were at least `n`, this would contradict `v_p(J)<n`.

In particular, both valuations of `J` must be even. For fixed `d,k`, `v_2(x)=v_2(J)/2` is independent of `m`. Therefore two different exponents `q` cannot give the same rational number `x/10^q`: their 2-adic valuations are different. This handles possible cancellation in those rational numbers without assuming their displayed denominators are reduced.

## 3. Early cuts: a centered nested-denominator gap

Fix `d,k`, and fix the parity `e`. The target `alpha` in (3) is now fixed, although its squareclass is arbitrary. The early condition is equivalent to

    N >= N_0 := 2K+2+t/d.                                (7)

List the square solutions in this fixed `(d,k,e)` group in increasing order of `m`. Then their `q`, and hence their `Q`, increase strictly. All denominators are powers of ten, so for two consecutive terms `Q_1 | Q_2`. Their rational values are distinct by (6). Thus

    1/Q_2 <= |x_2/Q_2-x_1/Q_1|
           < 20 B^(K-N_1+1).

The constant is 20 rather than 40 because both approximants lie strictly below the same target: their distance is at most the larger of their two errors. Since `20 < 10^(3/2)`, taking base-10 logarithms and substituting `q_2=(t+dN_2-e)/2` gives

    N_2 > 2N_1-c,
    c := 2K+2+(t+3)/d = N_0+3/d.                         (8)

The bound uses `e>=0`. Crucially, the rational center satisfies `0 < c-N_0 <= 3/2` for every `d>=2`.

At most three integers `N` lie in the half-open interval `[N_0,N_0+3)`. For the remaining solutions put `h=N-c`; then `h>=3/2`, `h<9L`, and (8) says

    h_2 > 2h_1.                                         (9)

If there are `r' >= 1` remaining solutions, then

    2^(r'-1) < 6L < 2^(4d),

so `r' <= 4d`. Adding the possible three initial solutions yields at most `4d+3` per `(d,k,e)` group. There are two parities and fewer than `B` possible cuts. Therefore the early square count is at most

    (8d+6)B.                                            (10)

No irrationality assumption on `alpha` was used. No lower bound for an algebraic approximation was used either: this is a gap/count argument, not a nonexistence argument.

## 4. Late cuts: inject into roots in one complete residue interval

For every square under consideration, (2) gives

    x < sqrt(J) 10^(H/2) < B 10^(H/2).

First consider the strong part of the late region,

    K >= H/(2d)+1.

Then `dK-H/2 >= d`, and hence

    0 < x < B^K.                                        (11)

For fixed `d,k`, different endpoints `m` give different `x`. Indeed (1) gives

    C^2 [R_(m+1,k)-R_(m,k)]
      = GC B^K [J B^(N-K)-1] > 0.                        (12)

All such `x` satisfy `x^2 = -J modulo B^K`. By (11) and (12), the strong-late square count for this cut is at most the number of roots of that congruence in a complete residue system.

The remaining late pairs satisfy

    H/(2d) <= K < H/(2d)+1.

For each endpoint `m`, this half-open interval has length one and contains at most one integer `K`. There are fewer than `B` endpoints. Thus this boundary strip contributes fewer than `B` pairs in total, whether square or not.

Write `J_(2,5)=2^v_2(J)5^v_5(J)`. If either valuation is odd, there are no roots. Otherwise put

    z = sqrt(J_(2,5)) = 2^a 5^b,       z < B.

For `p^n`, a root of a number of valuation `2a<n` has valuation `a`. Dividing by `p^(2a)` reduces to a unit-root congruence modulo `p^(n-2a)`, and each unit root has exactly `p^a` lifts modulo `p^(n-a)`. A unit has at most four square roots modulo a power of 2 and at most two modulo a power of 5. In the present range, (5) even gives `n-v_2(J) >= 3`.

The Chinese remainder theorem therefore gives

    # {x modulo B^K: x^2 = -J} <= 8z.                    (13)

The modulus depends on `k`, but the right side does not. It remains to sum this bound over the cuts.

## 5. Sum the local root counts uniformly over all squareclasses

Let `I` be the interval of possible cuts `L+7 <= k <= B-2`. It has length less than `B`. For each `z=2^a5^b`, the divisibility condition

    z^2 | kC+B

selects exactly one residue class of `k` modulo `z^2`, since `gcd(C,10)=1`. Its count in `I` is at most `B/z^2+1`.

On the subset of cuts for which both valuations of `J` are even, the value `z=sqrt(J_(2,5))` is an integer less than `B`. Grouping by this exact value and then relaxing equality to divisibility gives

    sum_(k in I; v_2(J),v_5(J) even) sqrt(J_(2,5))
      <= sum_(z=2^a5^b < B) z * #{k in I: z^2 | kC+B}
      <= B sum_(a,b >= 0) 1/(2^a5^b)
         + sum_(2^a5^b < B) 2^a5^b.                      (14)

The first sum is `5/2`. Let `h` be the largest integer with `5^h < B`, equivalently `floor(log_5(B-1))`. For each of the `h+1` possible values of `b`, the sum over `a` is less than `2B`. Thus

    sum_(k in I; v_2(J),v_5(J) even) sqrt(J_(2,5)) < B(9/2+2h).

Combining this with (13) bounds the strong-late square count by

    B(36+16h) < (24d+36)B,                               (15)

since `h < d log_5 10 < 3d/2`. Adding the fewer than `B` pairs in the boundary strip gives a bound of `(24d+37)B` for the entire late region, without fixing or even enumerating squareclasses.

Adding (10), (15), and the boundary-strip bound proves the theorem. The early and late regions are actually disjoint, since

    rho+tau = 2d(N-1)/H < 2,

but disjointness is not needed for the upper bound.

## 6. Exact scope and what remains open

The result counts pairs `(m,k)` at one width. It does not assert that their rotated decimal values are distinct, and does not need that assertion. It is not a bound on the largest width admitting a square. An `O(d10^d)` bound may still allow square examples at infinitely many widths.

The excluded central band consists of the parameters with

    N-1-H/(2d) < K < H/(2d).

This untruncated real band has exact width `t/d+1`, independent of `m`; this is not a count of admissible integer cuts. Neither this band, endpoints `m<2L`, cuts `k<L+7`, nor higher prime powers are covered.

The method is elementary and effective but does not supply uniform nonexistence across squareclasses. It does not resolve Kashihara's integer-power conjecture or claim any new specific counterexample exclusion beyond the finite audits below.

Summing over widths gives `O(X log X)` square pairs in **precisely these specified early/late regions** with endpoint `m <= X`, for `X >= 1`. Indeed, if `D` is the number of decimal digits of `floor(X)`, then `10^D <= 10X` and the sum is less than `(100/9)(32D+44)X`. This is not an upper bound for all square rotations with endpoint at most `X`.

## 7. Sources and finite audit

The exact identity and approximation setup are inherited from the earlier PR supplements:

- `IRRATIONAL_TARGET_ASSESSMENT.md`, Sections 1-3.
- `ALL_CUT_FIXED_SQUARECLASS.md`, Section 1.

The new ingredients here are the centered fixed-cut nested-denominator gap, the complete-residue-interval injection and one-cut boundary strip for late cuts, and the smooth-divisor summation. They include the natural threshold without any positive margin. They do not rely on the ineffective theorems in those source notes. “New” means new in this development; no literature-priority claim has been checked.

The companion `verify_uniform_cut_sparsity.py` uses only the Python standard library. It audits the exact rotation and congruence identities, the relevant integer inequalities, elementary prime-power root counts by brute force at small moduli, the smooth-divisor sum at small widths, and all admissible width-2 pairs. Its certificate records the finite scope. The general result rests on the proof, not on computation.

The completed audit contains 3,432 rotation checks (all 3,400 admissible width-2 pairs and 32 width-3 samples), 3,664 prime-power/CRT root-count checks, smooth-divisor sums and late boundary-strip counts at widths 2, 3, and 4, and centered-gap/threshold checks for widths 2 through 1,000. No square occurs among the audited width-2 pairs. This last finite observation is not the reason the uniform count holds.
