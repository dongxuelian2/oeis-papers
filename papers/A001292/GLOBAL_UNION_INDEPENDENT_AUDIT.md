# Independent audit of the global exponent union

## Verdict

PASS. The global union argument in `GLOBAL_PERFECT_POWER_UNION.md`, together with the stated separately proved full-prefix fixed-exponent input, establishes for every integer `d>=2`, `B=10^d`, and `L=B/10`:

- Fewer than `330B` square pairs.
- Fewer than `11B^2/d` odd-prime-power pairs.
- Fewer than `17B^2/d` nontrivial perfect-power pairs.

All counts include every endpoint `L<=m<B` and every whole-integer prefix cut `0<=k<m`. They do not include cuts inside an integer. The cumulative consequences are `O(X)` for squares and `O(X^2/log X)` for odd-prime powers and all perfect powers. No nonexistence or literature-priority conclusion follows.

This audit independently checks the exponent union and its verifier. The determinant proof supplying the fixed-exponent estimates has a separate audit; its hypotheses and constants were matched here to the exact inputs used.

## General mathematical checks

1. **Full scope and injectivity.** Rotation preserves the digit length `D(m)` because the unmoved suffix starts with a nonzero digit. Thus a rotated value fixes `m`. Its last `w` digits recover a cut of width `w`. Across all widths a value can have at most `d` cuts, not necessarily one.

2. **No saturated local congruences.** The smooth-part estimate alone needs an additional precision argument. For `k>=12`, `D(k)>7w>2w log_2(10)` suffices. The cases `k=10,11` have the explicitly stated valuations. Therefore `v_p(W_k)<D(k)` for both `p=2,5`, justifying the forced root valuations.

3. **Compressed-root classes.** Dividing by `p^(e a_p)` fixes the root modulo `p^(s-(e-1)a_p)`. The local unit kernels have size one at 2 for odd prime `e`, and at most `c_e` at 5. CRT gives at most `c_e` classes modulo `M=10^s/z^(e-1)`. In the strong-late region, `0<y<M`; fixed `k,e` therefore gives at most `c_e` endpoints.

4. **The exponent covers are exhaustive.** Small exponents are `e<=d^2`; medium exponents are `d^2<e<=2B`, split by the strong-late condition; large exponents are `e>2B`. For medium non-strong solutions, every witnessing prime puts the pair in the same cut strip `k<B/d+2d`. It is correct to count this union once without a prime-count multiplier.

5. **Large exponents.** From `R<10^(dB)` and `e>2B`, the root satisfies `y<sqrt(B)` and the prime satisfies `e<4dB`. The count `d sqrt(B) pi(4dB)` includes the necessary width multiplicity factor `d` and is valid without assuming distinct pairs give distinct rotations.

6. **Prime-counting input.** Section 6 of `../a001292-odd-power-sparsity/ODD_PRIME_POWER_SPARSITY.md` correctly proves `theta(u)<=u log 4` by central binomial coefficients, then `pi(u)<4u/log u` for every real `u>1`. It imports no endpoint or cut restrictions from that earlier note.

7. **Uniform constants are analytic.** The inequalities in equation (15) hold for all integer widths, not merely the widths checked by code. For the degree-five polynomial bound, compare `d=2,3` and use `(1+1/d)^5<= (4/3)^5<10` for `d>=3`. The other bounds decrease from `d=2`. Using `log 10>23/10`, the normalized odd-power coefficient is at most `5762/575<11`, and adding `320d/B<=320/50` gives `9442/575<17`. The looser displayed coefficient `8+12/5+320/50=84/5<17` is also correct.

8. **Small cuts are counted once.** The cuts `0<=k<=9` contribute fewer than `10B` pairs in total. Adding these to the union of the main-domain odd powers and squares gives the all-power claim without double counting this allowance. The square count is separately below `(320+10)B`. For `d=2`, `sum(m for m in range(10,100))=4905<B^2/2`, covering all required cases without applying the fixed-prime input outside its stated scope.

9. **Cumulative bounds.** Summing complete digit-width blocks gives `sum 100^d/d=O(100^D/D)` and `sum 10^d=O(10^D)`. For the top width of `floor(X)`, `10^D<=10X` and `D` is comparable to `log X`. This proves the claimed bounds for arbitrary large `X`, not just powers of ten. The total pair count is `Theta(X^2)`, so the perfect-power pair density tends to zero.

## Verifier rerun

`python verify_global_perfect_power_union.py` completed successfully. Its recorded checks were:

- Prefix smooth parts and strict local precision for `10<=k<=10000`.
- 54,401 nonsaturated local right-side groups and 86,304 candidate root values, for primes 2 and 5 and exponents 3, 5, 7, 11.
- 44,850 exact rotations through endpoint 300, checking length and fixed-width cut recovery.
- Exact integer/rational coefficient inequalities for widths 2 through 2000.
- Prime-counting sanity checks through integer argument 200000 and small-prime sums through width 100.

These are finite corroboration, not a proof by exhaustive search. The uniform theorem follows from the written arguments. The verifier correctly labels that limitation. It does not rely on floating-point arithmetic for the constant inequalities; floating-point logarithms appear only in the finite prime-bound sanity check.

## Review corrections

The draft's factor-`d` robustness paragraph was removed because, although such a loss preserves the global `O(X^2/log X)` perfect-power conclusion, a factor `d` in the square input alone would not preserve the separate `O(X)` square conclusion. The final note has no such ambiguity. No substantive error was found in the exponent partition, compression, counting constants, or cumulative summation.
