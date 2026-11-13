# Uniform odd-prime-power sparsity in the same-width rotation region

This note extends `UNIFORM_CUT_SPARSITY.md`. It also gives a shorter, stronger late-square argument. The assertions concern pairs `(m,k)`, not representations or distinct rotated values. All arguments are elementary and effective.

## 1. Notation and scope

Retain precisely the domain of the square note:

    d >= 2, B = 10^d, L = B/10, C = B-1,
    2L <= m <= B-1, L+7 <= k < m,
    t = D(L-1) = ((9d-10)L+1)/9,
    N = m-L+1, K = k-L+1, H = t+dN,
    G = 10^t, J = kC+B, M = mC+B,
    A = C^2 W_(L-1)+LC+1.

In particular `8 <= K < N <= 9L`, `t < dL`, and `H < dB`. The rotated integer `R=R_(m,k)` has exactly `H` decimal digits and ends in the `d`-digit block `k`. Consequently

    R mod B = k,                decimal_length(R) = H.       (1)

These facts use that the unrotated suffix begins with the nonzero digit of `k+1`, and that the moved prefix ends in `k`.

The inherited identity and estimates are

    C^2 R = G J B^N - T,
    T = (GM-A)B^K+J,
    0 < T < 2G B^(K+2),
    B^2/10 < J < B^2,
    C^2 R = -J mod B^K.                                   (2)

For an odd prime `ell`, define its early and late conditions by

    E_ell: ell*d*(N-K-1) >= H,
    L_ell: ell*d*K >= H.                                   (3)

Write

    c_ell = 5 if ell=5, and c_ell=1 otherwise,
    a_ell(d) = [ell/gcd(ell,d)] * [4+ceil(d log_ell 10)].    (4)

### Theorem A: fixed odd prime

For every odd prime `ell`, the number of admissible pairs with `R=y^ell`, for an integer `y>1`, satisfying `E_ell OR L_ell` is less than or equal to

    [a_ell(d)+c_ell+3] B.                                  (5)

The early count is at most `a_ell(d)B`; the entire late count is at most `(c_ell+3)B`.

For every prime `ell>=5`, every admissible pair satisfies at least one condition in (3). Thus (5) is an ALL-CUT bound on this precise endpoint/cut domain for each such prime. For `ell=3`, the pairs omitted by the early/late argument have

    (2N-t/d)/3 - 1 < K < (N+t/d)/3.                       (6)

This cube band is empty whenever `N >= 2t/d+3`, and in particular whenever `m>=3L`. A separate determinant argument in Section 9 removes the band entirely and proves the stronger all-cut bound

    # {admissible cube pairs} < 24B.                      (6a)

### Theorem B: union over all odd primes

Let `S_d` contain admissible pairs whose rotation is an `ell`th power for at least one odd prime `ell`. Then

    #S_d < 20 B^2/d.                                      (7)

Thus this odd-power set has density tending to zero among the `Theta(B^2)` admissible pairs. All cubes, including those in (6), are covered using Section 9. Neither theorem covers earlier endpoints `m<2L`, cuts `k<L+7`, or cuts in an earlier decimal-width block. Therefore (7) is not, by itself, a bound for all rotations with endpoint at most `B`.

## 2. Approximation and valuations for arbitrary odd prime exponent

Suppose `R=y^ell` and put `x=Cy`. Multiplying (2) by `C^(ell-2)` gives

    x^ell = C^(ell-2) G J B^N - C^(ell-2) T,
    x^ell = -C^(ell-2) J mod B^K.                         (8)

Write

    H = ell*q+r, 0 <= r < ell, Q = 10^q,
    alpha = (10^r C^(ell-2) J)^(1/ell).

Factoring the difference of the `ell`th powers and retaining the first positive term in the denominator gives

    0 < alpha-x/Q
      < C^(ell-2) T / (Q^ell alpha^(ell-1))
      < 2 * 10^((r+ell-1)/ell) B^(K-N+1)
      < 200 B^(K-N+1).                                    (9)

The middle inequality follows by using `C<B`, `J>B^2/10`, and the bound for `T` in (2). No irrationality assertion is used.

Let `n=dK`. As before,

    v_2(J)<7d, v_5(J)<3d, n>=8d.

Since `gcd(C,10)=1`, (8) forces

    ell*v_p(x) = v_p(J), for p=2,5.                       (10)

If either valuation is not divisible by `ell`, there are no solutions. For fixed `d,k,ell`, the 2-adic order of `x` is fixed. Therefore distinct displayed denominator exponents `q` give distinct rationals `x/10^q`, whether or not those fractions are reduced.

## 3. Centered early gap

Fix `d,k,ell,r`. The early threshold is

    N >= N_0 = (ell*K+ell+t/d)/(ell-1).                    (11)

For successive solutions in increasing `N`, their `q` increase strictly and their denominators are nested. Their rational values are distinct by (10). Because both lie below the same target,

    1/Q_2 <= |x_2/Q_2-x_1/Q_1|
           < 200 B^(K-N_1+1).

Using `log_10(200)<5/2` and `r>=0` yields

    N_2 > ell*N_1 - ell*K - ell - t/d - 5ell/(2d).

Set

    c = N_0 + 5ell/[2d(ell-1)].

Then

    N_2-c > ell*(N_1-c),
    0 < c-N_0 <= 15/8 < 2.                               (12)

There are at most four integer values of `N` in `[N_0,N_0+4)`. For all remaining solutions `h=N-c>2` and `h<9L`. If there are `s>=1` remaining solutions, (12) implies

    ell^(s-1) < 9L/2 < B,

so `s <= ceil(d log_ell 10)`. This proves a bound of

    4+ceil(d log_ell 10)

for the fixed `(d,k,ell,r)` group. As `N` varies, `r=t+dN mod ell` takes at most `ell/gcd(ell,d)` values. There are fewer than `B` possible cuts, proving the claimed early bound.

## 4. Compressed congruence classes: a stronger late-root injection

For any solution, write

    v_2(J)=ell*a, v_5(J)=ell*b, z=2^a 5^b.

Then `z^ell` divides `J`, so

    z^ell <= J < B^2.                                    (13)

For a prime `p` in `{2,5}`, write `a_p=v_p(x)` and `s_p=n-ell*a_p>0`. After dividing the local congruence (8) by `p^(ell*a_p)`, the unit `x/p^a_p` satisfies a unit-root congruence modulo `p^s_p`. Each unit-root residue determines a single residue for `x` modulo

    p^(s_p+a_p) = p^(n-(ell-1)a_p).

All lifts modulo `p^n` belong to that same arithmetic progression. Thus it is unnecessary to count each lift as a distinct possible endpoint.

For odd `ell`, raising to the `ell`th power permutes the units modulo powers of 2. For powers of 5 the unit group is cyclic of order `4*5^(s_p-1)`, so a unit has at most `gcd(ell,4*5^(s_p-1))` roots: one if `ell!=5`, at most five if `ell=5`. The Chinese remainder theorem therefore puts every integer solution of (8) in at most `c_ell` residue classes modulo the COMPRESSED modulus

    D = B^K/z^(ell-1).                                   (14)

The modulus is an integer, since `n>ell*a` and `n>ell*b`.

The size bound from (8) is

    0 < x < (C^(ell-2)J)^(1/ell) 10^(H/ell)
            < B 10^(H/ell).

In the strong-late region

    K >= H/(ell*d)+3,

(13) gives

    x*z^(ell-1) < B^3 10^(H/ell) <= B^K,

and hence `0<x<D`. For fixed `d,k`, different endpoints give different `R`, and hence different `x`, because

    C^2 [R_(m+1,k)-R_(m,k)]
       = G C B^K [J B^(N-K)-1] > 0.

Thus there are at most `c_ell` strong-late endpoints per cut, and fewer than `c_ell B` strong-late pairs in total.

All other late pairs have

    H/(ell*d) <= K < H/(ell*d)+3.

For each endpoint this half-open interval contains at most three integers. Its contribution is less than `3B`, proving the late bound `(c_ell+3)B`.

### Square corollary

The same compression works for squares with at most eight unit-root combinations. Now `z^2<=J<B^2`, so `z<B`. The condition `K>=H/(2d)+2` already guarantees `x<D=B^K/z`. The boundary strip has at most two cuts per endpoint. Therefore the late-square count in the original note improves to at most `10B`; retaining that note's early argument gives at most `(8d+16)B` squares outside its central band. This is only a count improvement, not a nonexistence result.

## 5. Why early and late cover all cuts for primes at least five

The upper boundary of the early region is

    U = [(ell-1)N-t/d]/ell - 1,

and the lower boundary of the late region is

    V = (N+t/d)/ell.

We have `U>=V` precisely when

    (ell-2)N >= 2t/d+ell.                                 (15)

For `ell>=5`, `N>=L+1` and `t/d<L` give

    (ell-2)N - (2t/d+ell)
      > (ell-2)(L+1) - (2L+ell)
       = (ell-4)L-2 > 0.

Therefore every cut is covered. When `ell=3`, the uncovered real interval is exactly (6), and (15) becomes `N>=2t/d+3`.

Finally `t/d <= L-1`: this is equivalent to `10L-1>=9d`, which holds for every `d>=2`. If `m>=3L`, then `N>=2L+1>=2t/d+3`, proving the stated sufficient endpoint threshold for cubes.

## 6. Elementary prime-counting estimate

We use the fully effective elementary bound

    pi(u) < 4u/log u, for u>1.                            (16)

Here and below an unbased logarithm is natural. A short proof is included to avoid requiring an analytic prime number theorem.

Let `theta(n)=sum_(p<=n) log p`. Strong induction gives `theta(n)<=n log 4`. For `n=2m`, every prime in `(m,2m]` divides `binomial(2m,m)`, whose logarithm is at most `2m log 2`. Add the induction bound for `theta(m)`. For `n=2m+1`, primes in `(m+1,2m+1]` divide `binomial(2m+1,m)`, which is less than `2^(2m)` because its two equal largest binomial coefficients together are smaller than the sum `2^(2m+1)`. Add the induction bound for `theta(m+1)`. The initial cases are immediate. The real-variable bound follows by taking floors.

Now split primes at `sqrt(u)`. There are at most `sqrt(u)` below that point, and every larger prime contributes more than `(log u)/2` to `theta(u)`. Therefore

    pi(u) <= sqrt(u)+2 theta(u)/log u
           <= sqrt(u)+4(log 2)u/log u
           < 4u/log u,

using `log u<sqrt(u)` for `u>1` and `1+4log 2<4`.

## 7. Sum all odd prime exponents without summing all early bounds

Set

    P=max(5,d), E=2B.

First cover all cube pairs by the bound `24B` from Section 9. For the remaining pairs, choose a witnessing prime exponent at least 5. We use four further overlapping covers; overcounting is harmless. Crucially, the third cover counts a union of PAIRS directly, not a sum over exponents.

### (i) Early solutions with ell<=P

For `ell>=3`, `ceil(d log_ell 10)<=3d`. Dropping both primality and the gcd improvement in the early estimate gives a total at most

    B(3d+4) P(P+1)/2.                                    (17)

### (ii) Late solutions with ell<=E

The late bound is `4B` for every odd prime other than 5, and `8B` for 5. Thus their total is at most

    4B pi(2B)+4B.                                        (18)

Counting 2 unnecessarily only enlarges this bound.

### (iii) Nonlate solutions with P<ell<=E

The failure of the late condition implies

    K < H/(ell*d) < B/ell < B/P.

The UNION of all such pairs is contained in the same fixed small-cut strip `K<B/P`. There are fewer than `B/P` possible integer cuts per endpoint and fewer than `B` endpoints, so its size is less than

    B^2/P.                                               (19)

There is no factor counting primes in this estimate.

### (iv) Solutions with ell>E

Since `R<10^H<10^(dB)` and `ell>2B`,

    2 <= y < 10^(d/2)=sqrt(B).

Also `ell<=log_2(R)<dB log_2(10)<4dB`, so there are at most `pi(4dB)` exponent choices. Each pair `(y,ell)` produces at most one admissible `(m,k)`: the integer `y^ell` fixes `k` by (1), and its decimal length fixes `N` and hence `m` by (1). Therefore this part has size less than

    sqrt(B) pi(4dB).                                     (20)

Every pair in `S_d` is covered. Cubes were covered separately. For any remaining pair, choose a witnessing prime exponent at least 5. If it is at most `P`, it is early or late by Section 5. If it lies between `P` and `E`, it is either late or in the common strip. If it exceeds `E`, use (20).

Combining the `24B` cube bound and (17)-(20) proves the more informative explicit bound

    #S_d < B(3d+4)P(P+1)/2 + 4B pi(2B)+28B
            + B^2/P + sqrt(B) pi(4dB).                   (21)

By (16), and using `P>=d`,

    #S_d < B(3d+4)P(P+1)/2 + 28B
            + (32/log 10 + 1) B^2/d
            + (16/log 10) B^(3/2).                      (22)

For completeness, all constants can be absorbed uniformly without an unspecified threshold. For every `d>=2`,

    d(3d+4)P(P+1)/(2B) <= 3,
    28d/B <= 14/25,
    d/sqrt(B) <= 1/5.

The first has value 3 at `d=2`, is directly checked at `d=3,4`, and decreases for `d>=5`, where it is a degree-four polynomial divided by `10^d`. The other two sequences decrease from `d=2`. Dividing (22) by `B^2/d` now gives an upper bound

    3 + 14/25 + 1 + (32+16/5)/log 10 < 20,

which proves (7). The last strict inequality can, for example, be checked using the rational lower bound `log 10 > 23/10`.

## 8. Scope and interpretation

- Theorem A is `O_ell(d*10^d)` for each fixed odd prime and covers ALL cuts in the declared domain for every prime at least 5. Section 9 gives the stronger all-cut cube bound `24B`.
- Theorem B is a single effective all-odd-exponent, all-cut union bound `O(10^(2d)/d)`, with constant 20, throughout the declared endpoint/cut domain. It is not merely a list of fixed-exponent examples.
- This is not a global all-rotation theorem: the endpoint and cut exclusions in Section 1 remain material. Combining it with bounds for other regions requires separately proved coverage of those regions.
- Neither theorem proves zero examples, bounds the largest endpoint of a possible counterexample, or resolves the integer-power conjecture.
- The compressed-root lemma is independent of any squareclass classification. All squareclasses and all admissible valuations of `J` are handled simultaneously.


## 9. A three-point determinant removes the cube band

This section proves (6a) independently of the early/late split. Fix `d,k` and a residue `r=H mod 3` that occurs among cube solutions. Set `Q=10^((H-r)/3)` and `x=Cy` as before. For continuous `Q` between any two such solution points, write

    x = f(Q) = [aQ^3-T(Q)]^(1/3),
    a=10^r C J,
    T(Q)=C[(G M(Q)-A)B^K+J]=b log Q+c,
    b=3 G C^2 B^K/log B > 0,
    N(Q)=(3 log Q/log 10-t+r)/d.

The constants `a,b,c` are fixed within this group. This continuous formula agrees with every integer solution. Throughout an interval between solution points, `N>=K+1`, the inherited size estimates remain valid, and

    T(Q)/(aQ^3) < 20 B^(K-N) <= 20/B <= 1/5.

Thus `f` is positive and twice differentiable throughout that interval. Moreover,

    T(Q)/b
      = [M(Q)-A/G+J/(GB^K)] log B/(3C)
      > B log B/40 > 5/6,                                (23)

because `M>B^2/5`, `A/G<B^2/8`, `C<B`, and `B>=100`.

For clarity, the general derivative identity for

    f(Q)=[aQ^ell-T(Q)]^(1/ell), T(Q)=b log Q+c

is

    ell^2 f^(2ell-1) f''
      = ell a Q^(ell-2)[(2ell-1)b-ell(ell-1)T]
        - [ell b T+(ell-1)b^2]/Q^2.                       (24)

It follows by differentiating `g=aQ^ell-T` and expanding
`ell*g*g''-(ell-1)*(g')^2`. For `ell=3`, (23) makes both terms on the right of (24) strictly negative. Thus `f` is strictly concave. In particular, no three solution points `(Q_i,x_i)` with distinct `Q_i` are collinear.

Take three cube solutions in increasing order, and form

    Delta = det((1,Q_1,x_1),(1,Q_2,x_2),(1,Q_3,x_3)).

For cubes the compressed-root lemma has `c_3=1`. Consequently the three integers `x_i` belong to the same residue class modulo `D=B^K/z^2`, where `z^3=J_(2,5)`. Also `Q_1` divides every `Q_i`. Subtracting the first row from the other two shows that the nonzero integer `Delta` is divisible by `D Q_1`. Hence

    |Delta| >= D Q_1.                                    (25)

Let `delta_i=alpha Q_i-x_i`. By (9),

    0 < delta_i < 200 Q_i B^(K-N_i+1).

The right side decreases with `N_i`, since `Q_i` is a fixed positive constant times `B^(N_i/3)`. Replacing the last column of the determinant by `-delta_i` and bounding its three terms yields

    |Delta| < 400 Q_3 Q_1 B^(K-N_1+1).                  (26)

Indeed, the absolute values of the three coefficients sum to `2(Q_3-Q_1)<2Q_3`. Combining (25)-(26), cancelling `Q_1 B^K`, and using `z^2<B^(4/3)`, gives

    1 < 400 z^2 Q_3 B^(1-N_1),
    N_3 > 3N_1-t/d-7-3 log_10(400)/d
          > 3N_1-t/d-11,                                (27)

where `d>=2` and `3 log_10(400)<8` (equivalently `400^3<10^8`) were used in the last step. Set

    c_0=(t/d+11)/2, h=N-c_0.

Then every three successive solutions satisfy `h_3>3h_1`. Furthermore

    L/4 <= h < 9L.                                      (28)

For `d=2`, `L=10`, `t/d=9/2`, and the smallest possible `h` is `11-31/4=13/4>L/4`. For `d>=3`, `L>=100` and `t/d<L`, so `h>L/2-9/2>=L/4`. The upper bound is immediate.

Apply (27) separately to the odd-indexed and even-indexed solutions. Each subsequence increases by a factor greater than 3 at each step and stays within the bounds (28). If it contains `s` terms,

    3^(s-1) < 36.

Hence `s<=4`. There are at most eight solutions in the fixed `(d,k,r)` group, at most three residue values `r`, and fewer than `B` possible cuts. This proves the all-cut cube bound `<24B`. As throughout the note, this is an effective counting theorem and not a nonexistence statement.

## 10. Sources and finite verification

The exact rotation identity, notation, and elementary size estimates are inherited from `UNIFORM_CUT_SPARSITY.md`. The determinant method is also used for squares in `CENTRAL_CUT_DETERMINANT_SPARSITY.md`; Section 9 supplies the complete cubic adaptation rather than assuming that the square argument automatically extends. Earlier identities and context appear in `IRRATIONAL_TARGET_ASSESSMENT.md` and `ALL_CUT_FIXED_SQUARECLASS.md`. No literature-priority claim is made.

The companion `verify_odd_prime_power_sparsity.py` uses only the Python standard library. Its certificate and captured output record the exact finite checks: local compressed-root classes, the rational derivative identity, width-dependent constants, the elementary prime-counting inequality, decimal-length/final-block injectivity, and exact rotation identities. These checks corroborate finite instances. The general theorems rest on the proofs above, not on computation, and the verifier does not claim to exhaust odd prime powers at all widths.

## 11. Combined perfect-power corollary, with unchanged scope

The square theorem in `CENTRAL_CUT_DETERMINANT_SPARSITY.md` bounds ALL square pairs in the same domain by

    32 B (1+floor(log_2(18d))).

Every nontrivial integer perfect power has a prime exponent divisor: if `R=y^n`, `y>1`, `n>=2`, and a prime `ell` divides `n`, then `R=(y^(n/ell))^ell`. Combining the square theorem with Theorem B therefore bounds all nontrivial integer perfect-power pairs in the declared domain by

    20 B^2/d + 32 B (1+floor(log_2(18d))).                 (29)

In particular this is `O(B^2/d)`. No new restriction is imposed on the exponent or the cut beyond the endpoint/cut domain in Section 1.

Let `F(X)` count only such pairs with `m<=X`, where at each width `d` the restrictions are still

    d>=2, 2*10^(d-1)<=m<=10^d-1,
    10^(d-1)+7<=k<m.

Then, as `X` tends to infinity,

    F(X)=O(X^2/log X).                                    (30)

For completeness, let `D` be the number of digits of `floor(X)`. The main width sum obeys

    sum_(2<=d<=D) 10^(2d)/d = O(10^(2D)/D).

To prove this, split at `d=D/2`. On the upper part, use `1/d<2/D` and sum a geometric series. On the lower part, dropping `1/d` gives `O(10^D)`, which is also `O(10^(2D)/D)`. The square term in (29) is absorbed by `O(10^(2d)/d)` because `d log d/10^d` is bounded. Finally `10^D<=10X` and `D` is comparable to `log X`.

Both (29) and (30) retain the endpoint and cut exclusions stated above. They are NOT upper bounds for all rotated concatenations with endpoint at most `X`, do not prove nonexistence of perfect powers, and do not resolve the integer-power conjecture.
