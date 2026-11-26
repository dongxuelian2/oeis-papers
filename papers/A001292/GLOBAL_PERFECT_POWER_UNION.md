# Global exponent union from uniform fixed-prime counts

## Result and role

This note supplies the elementary exponent-union argument for **all whole-integer prefix rotations**, using the companion full-prefix determinant theorem. For every `d>=2`, with `B=10^d` and `L=B/10`, it proves

    # {perfect-power pairs: L<=m<B, 0<=k<m} <17 B^2/d,
    # {odd-prime-power pairs: L<=m<B, 0<=k<m} <11 B^2/d,
    # {square pairs: L<=m<B, 0<=k<m} <330 B.

Consequently the cumulative counts through endpoint `X` are respectively `O(X^2/log X)`, `O(X^2/log X)`, and `O(X)`. There is no same-width-cut or early-endpoint exclusion. The precise required inputs are stated below, keeping the global union proof separate from the fixed-exponent determinant proof. The companion proof and this exponent-union proof have passed an independent mathematical audit, including the full-prefix precision condition and all endpoint/cut coverage.

No nonexistence claim is made. The conclusion is a count of endpoint/cut pairs, not a bound on the number or size of all possible counterexamples.

## 1. Definitions and exact elementary facts

Let `W_j` be the integer obtained by concatenating `1,2,...,j` in decimal, and let `D(j)` be its number of digits. Put `W_0=D(0)=0`. For `0<=k<m`, move the entire prefix `1,2,...,k` to the end and call the result `R_(m,k)`. Thus `k=0` is the unrotated concatenation. We do not count `k=m` separately because that operation is the same as `k=0`.

For Sections 1–6, fix

    d>=3, B=10^d, L=B/10, L<=m<B, 1<=k<m.

Write

    H=D(m), s=D(k), w=decimal_length(k).

Because the suffix begins with the nonzero leading digit of `k+1`,

    decimal_length(R_(m,k))=H<dB,
    R_(m,k) = W_k (mod 10^s),
    R_(m,k) = k (mod 10^w).                            (1)

Also `s>=k`, `1<=w<=d`, and `D(m)` increases strictly with `m`. In particular, for fixed `k`, the rotations have strictly increasing decimal lengths, so distinct endpoints give distinct rotations and distinct positive `e`th roots.

## 2. Inputs from the all-cut determinant theorem

For a positive integer `a`, write `a_(2,5)=2^v_2(a) 5^v_5(a)`. The first input is

    (W_k)_(2,5) < 10^(2w), for k>=10.                  (S)

For fixed odd prime `e`, put

    c_e=5 if e=5, and c_e=1 otherwise.

The companion all-cut determinant theorem in [UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md](UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md) establishes the following inputs for `d>=3`, with `A=12` and `K=320`. We first leave these constants symbolic. The uniform fixed-prime input is

    # {(m,k): L<=m<B, 10<=k<m, R_(m,k)=y^e,
                y an integer >1}
       <= A c_e e B.                                  (F)

The assertion (F) is not being extended to `d=2`; that endpoint width is handled trivially at the end. Only (F) for `e<=d^2` is used. Thus the proof also works if this estimate is established only in that range. The square bound is

    # {(m,k): L<=m<B, 10<=k<m, R_(m,k) is a square}
       <= K B                                         (Q)

and will be used only when passing from odd powers to all perfect powers.

The constants are left symbolic until Section 6 to make their contribution transparent.

## 3. Full-prefix compression and the strong-late count

First check that the local valuations are strictly below the available precision. For `k>=12`,

    D(k)>7w.

For `w=2`, this follows from `D(k)=2k-9>=15>14`. For `w>=3`, use `D(k)>=k>=10^(w-1)>7w`; the last inequality holds at `w=3` and persists by induction. Since `2 log_2(10)<7`, (S) therefore implies

    v_p(W_k)<2w log_p(10)<=2w log_2(10)<7w<s.

For `k=10`, both relevant valuations of `W_10=12345678910` are 1 and `s=11`; for `k=11`, both valuations are zero. Hence for every `k>=10`,

    v_p(W_k)<s, for p=2,5.

Now suppose `R_(m,k)=y^e` for an odd prime `e`.

The congruence (1) therefore forces

    e v_p(y)=v_p(W_k), for p=2,5.                      (2)

If either valuation is not divisible by `e`, there are no solutions. Otherwise set

    z=2^v_2(y) 5^v_5(y), so z^e=(W_k)_(2,5)<10^(2w).

For each `p=2,5`, let `a_p=v_p(y)`. Divide the congruence modulo `p^s` by `p^(e a_p)`. Its unit-root solutions determine `y` modulo

    p^(s-(e-1)a_p).

For powers of 2, raising units to an odd prime power is a bijection. For powers of 5, the kernel has size at most `c_e`, since its unit group is cyclic of order `4*5^(n-1)`. The Chinese remainder theorem consequently puts all possible `y` in at most `c_e` residue classes modulo the integer

    M=10^s/z^(e-1).                                    (3)

Call a solution **strong-late** if

    s >= H/e+2w.                                      (4)

Then

    y z^(e-1) < 10^(H/e) 10^(2w) <= 10^s,

so `0<y<M`. For each fixed `k,e`, a residue class contributes at most one such `y`, and that root comes from at most one endpoint by (1). There are therefore fewer than `c_e B` strong-late pairs for fixed `e`.

This argument is independent of (F); it also handles exponents that are much larger than the endpoint width.

## 4. Partition the odd-prime exponents

Set

    P=d^2, E=2B.

For `d>=2` we have `P<E`. Let `U_d` count all pairs with `L<=m<B`, `10<=k<m` whose rotation is an odd-prime power. We cover this set in four pieces. Overlap causes no difficulty because only upper bounds are sought.

### Small exponents: e<=P

Using (F), and then summing over all integers rather than only primes,

    U_small <= A B sum_(odd prime e<=P) c_e e
             <= A B [P(P+1)/2 +20 I_(d>=3)].          (5)

The extra 20 is `(c_5-1)*5`; it is absent for `d=2`, because `P=4`.

### Medium exponents, strong-late: P<e<=E

Section 3 gives

    U_medium,strong < B pi(2B)+4B.                   (6)

The extra `4B` allows for the exceptional prime 5 even when it was already covered by (5).

### Medium exponents, not strong-late: P<e<=E

Failure of (4) and (1) give

    k <= s < H/e+2w < dB/P+2d = B/d+2d.              (7)

Every such pair lies in the **same cut strip**, irrespective of its witnessing prime. Counting the union of pairs directly therefore gives

    U_medium,not-strong < B^2/d+2dB.                  (8)

There is no prime-counting factor in (8). This is the critical feature of the decomposition.

### Large exponents: e>E

Since `y>=2` and `y^e=R<10^(dB)`,

    y<sqrt(B), e<dB log_2(10)<4dB.                   (9)

For each fixed pair `(y,e)`, the integer `R=y^e` fixes `m` uniquely, because its decimal length is `D(m)`. It fixes at most one cut of each width `w`, because the last `w` digits equal `k` by (1). There are at most `d` widths. Hence

    U_large < d sqrt(B) pi(4dB).                     (10)

The factor `d` is necessary in this argument: the same-width injection from the earlier note cannot be used unchanged when cuts of different widths are allowed.

Every odd-prime-power pair belongs to one of these four covers, for any chosen witnessing odd prime. Combining (5), (6), (8), and (10) yields

    U_d < A B [d^2(d^2+1)/2+20 I_(d>=3)]
          +B pi(2B)+4B+B^2/d+2dB
          +d sqrt(B) pi(4dB).                        (11)

## 5. An elementary and effective asymptotic bound

Use the elementary Chebyshev estimate

    pi(u)<4u/log u, for u>1.                         (12)

A self-contained proof is in Section 6 of `ODD_PRIME_POWER_SPARSITY.md`; it uses central binomial coefficients, not the prime number theorem. Since `log(2B)>d log 10` and `log(4dB)>d log 10`, (11) implies

    U_d < A B [d^2(d^2+1)/2+20 I_(d>=3)]
          +(1+8/log 10) B^2/d
          +(2d+4)B+(16/log 10)d B^(3/2).              (13)

All terms are `O(B^2/d)`, uniformly in `d`, because every fixed-degree polynomial in `d` is bounded by a constant times `10^d`, and `d^2/10^(d/2)` is bounded. This already proves

    U_d = O(B^2/d).                                   (14)

The cuts `1<=k<=9` contribute fewer than `9B` further pairs, even without imposing any power condition. Thus (14) holds for every proper nonempty whole-integer prefix cut, with no endpoint or cut-width exclusion.

## 6. Optional explicit constant

For every integer `d>=2`,

    d[d^2(d^2+1)/2+20 I_(d>=3)]/B <= 1/5,
    d^2/sqrt(B) <= 2/5,
    d/B <= 1/50,
    (2d^2+14d)/B <= 9/25.                            (15)

For the first inequality, the `d=2` value is `1/5`, the `d=3` value is `39/200`, and it decreases thereafter. Each summand `d^j/10^d` for `j<=5` decreases for `d>=3`, since `(1+1/d)^5<= (4/3)^5<10`. The second inequality decreases from `d=2`, because `(1+1/d)^2/sqrt(10)<1`; the last two are verified the same way.

Including both the nine small cuts and the unrotated case `k=0`, and using `log 10>23/10`, (13) and (15) give

    # {odd-prime-power pairs, allowing 0<=k<m}
       < [A/5+1+9/25+(8+32/5)/log 10] B^2/d
       < (A/5+8) B^2/d.                              (16)

When the square input (Q) is available, every nontrivial integer perfect power is either a square or an odd-prime power. Adding (Q), and counting the small cuts and `k=0` only once, therefore proves

    # {perfect-power pairs: L<=m<B, 0<=k<m}
       < (8+A/5+K/50) B^2/d.                         (17)

For `A=12` and `K=320`, (16) is smaller than `11 B^2/d`, and (17) is smaller than `17 B^2/d`. Separately, (Q) plus the nine small cuts and `k=0` gives the square bound `<330B`.

For `d=2`, the total number of all pairs, including those that are not powers, is

    sum_(m=10)^99 m = 4905 < B^2/2.

This proves both stated odd-power and all-perfect-power bounds for `d=2`, without invoking (F). It also proves the square bound since `4905<33000`. No assumption is made that distinct pairs produce distinct integers.

## 7. Cumulative count through an arbitrary endpoint

Let `F(X)` count all pairs

    1<=m<=X, 0<=k<m,

for which `R_(m,k)` is a nontrivial integer perfect power. The finitely many one-digit endpoints contribute only a constant. Summing (17), or merely its asymptotic version, over endpoint digit widths gives

    F(X)=O(X^2/log X).                                (18)

Indeed, if `D` is the number of digits of `floor(X)`,

    sum_(2<=d<=D) 10^(2d)/d = O(10^(2D)/D).

Split the sum at `D/2`. For the upper part, bound `1/d` by `2/D` and sum a geometric series; the lower part is `O(10^D)` and is absorbed by the same bound. Finally `10^D<=10X` and `D` is comparable to `log X`.

The square bound sums to `O(X)`, since `sum_(d<=D)10^d=O(10^D)=O(X)`.

There are `Theta(X^2)` endpoint/cut pairs, so this is a density-zero theorem for perfect-power pairs among all whole-integer prefix rotations. It does not prove absence of perfect powers, put a finite upper limit on possible counterexamples, or settle the nonexistence conjecture. It also does not concern rotations that cut inside the decimal representation of an integer.

## 8. Sources, independent audit, and finite checks

- Full-prefix smooth-part estimate, unsaturated valuations, and uniform all-cut fixed-exponent theorem: [UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md](UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md), Sections 1–6.
- Elementary prime-counting bound: [ODD_PRIME_POWER_SPARSITY.md](ODD_PRIME_POWER_SPARSITY.md), Section 6. The previous note's endpoint/cut exclusions are not imported into this theorem; only its elementary prime estimate is used.
- Local companion verifier: `verify_global_perfect_power_union.py`. Its captured output and certificate are `global-perfect-power-union-verification.txt` and `global-perfect-power-union-certificate.json`.

The verifier checks the full-prefix smooth-part and precision inequalities for `10<=k<=10000`; 54,401 local compressed-root right-side groups involving 86,304 candidate root values; 44,850 rotations through endpoint 300 for decimal-length and cut-recovery assertions; exact rational constant inequalities through width 2000; and the elementary prime estimate at every integer argument through 200000. These are finite consistency checks, not a computational proof of the general theorem or an exhaustive perfect-power search. The general result rests on the arguments above and the separately proved determinant input.

The independent mathematical audit specifically checked the two potential pitfalls that do not occur in the same-width proof: the high-exponent multiplicity is at most `d`, not necessarily one, and the smooth-part bound alone requires a separate unsaturated-valuation argument before using the compressed-root lemma. Both are explicit here.

## 9. Relation to prior work and limits of novelty

Kashihara's *Comments and Topics on Smarandache Notions and Problems* (1996), p. 25, #30, Problem 2, is the source of the nonexistence question; see the [OEIS-hosted scan](https://oeis.org/A011772/a011772.pdf) and [A001292](https://oeis.org/A001292). The trivial value 1 is excluded throughout the perfect-power count.

Marco Ripà, [*On some conjectures concerning perfect powers*, version 3, revised 16 May 2022](https://vixra.org/pdf/2204.0139v3.pdf), Theorem 1 and Corollary 1, gives the endpoint classes m=2,3,5,6 modulo 9 and reports an all-exponent finite search through m=447. Those modular exclusions and the conjecture itself are prior work, not contributions of this note. That paper also discusses a probabilistic heuristic; such a heuristic is not an unconditional counting bound.

Relative to those sources, the result proved here is a uniform bound over all endpoints, all whole-integer cuts, and all prime exponents. Its substantive input is the companion full-prefix determinant argument; the present note supplies the exponent union without losing control of the growing exponent range. Neither the local unit-root facts nor the elementary prime-counting estimate is claimed as new. This comparison does not establish literature priority: no exhaustive literature review, first-result claim, or resolution of the original conjecture is asserted.
