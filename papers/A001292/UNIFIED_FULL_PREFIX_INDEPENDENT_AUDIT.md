# Independent audit of the full-prefix extension

**Verdict: PASS for the claims and versions identified below.** The fixed-exponent argument has no omitted earlier-width cuts or early endpoints. Together with the independently checked exponent-union argument, it proves effective counting bounds for every whole-integer prefix rotation. It does not prove nonexistence of perfect powers.

## Audited statements

Let `B=10^d`, `L=B/10`, and let `R_(m,k)` move the whole-integer prefix `123...k` of `123...m` to the end.

- `UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md`: for every `d>=2`, fewer than `329B` square pairs with `L<=m<B` and `1<=k<m`. For `d>=3`, each odd prime `ell` has fewer than `(12 c_ell ell+9)B` such power pairs, where `c_5=5` and the other odd-prime constants are one. Before adding the nine small cuts, the constants are `320B` for squares and `12 c_ell ell B` for a fixed odd prime.
- `../a001292-global-union/GLOBAL_PERFECT_POWER_UNION.md`: allowing the unrotated cut `k=0`, every `d>=2` has fewer than `330B` square pairs, `11B^2/d` odd-prime-power pairs, and `17B^2/d` nontrivial perfect-power pairs. The respective cumulative orders are `O(X)`, `O(X^2/log X)`, and `O(X^2/log X)`.

The counts concern pairs, so possible duplicate rotated values are not silently identified. Cuts inside an integer's decimal representation are outside the definition.

## Mathematical checks

1. **All-prefix valuations.** The identity `c^2 W_k=a b^K-j` and `v_p(j)<wK` give `v_p(W_k)=v_p(j)` for both `p=2,5`, at every `k>=10`. The split into `K>=8`, `K<=7,w>=4`, and fourteen explicit small cases is exhaustive. Integrality of `a` suffices; no auxiliary valuation assertion about `a` is needed. The smooth-part bound is therefore `<10^(2w)`.

2. **No saturated local congruences.** The strict inequalities `v_p(W_k)<D(k)` are proved separately. This is essential: the weaker statement `D(k)>2w` would not follow from the smooth-part bound with the required base conversion. The final union proof repairs that issue using `D(k)>7w` for `k>=12` and direct checks for `k=10,11`.

3. **Exact identity and positive leading coefficient.** The quantities `F=10^s A-G C^2 W_k` and `T=10^s M-C^2 W_k` satisfy `C^2 R=F B^N-T`. For same-width cuts, `F=G(kC+B)`, without an extra factor `B^K`. For earlier-width cuts, separating the remaining suffix gives the claimed positive expression. Both cases yield `F>=C^2 10^(t-1)`.

4. **Signed corrections and real interpolation.** `T` may be negative. Every approximation and determinant bound uses its absolute value. The proof establishes positivity on the entire continuous interpolation interval, not just at integer solution points: `g>0` at the first admissible endpoint and `g'>0` throughout the interval.

5. **At most one inflection.** The two displayed derivative identities were rederived. For the normalized second-derivative expression, `Z<aQ^ell` and `b<ell aQ^ell` imply `H'<0` for every `ell>=2`. The case `ell=2` follows separately because its last term vanishes. Thus two strictly curved intervals suffice, including a possible inflection endpoint, with no missing exceptional point.

6. **Compressed roots.** For unsaturated valuations, one unit-root branch determines a residue modulo `p^(s-(ell-1)a_p)`, not merely modulo the original precision. The resulting decimal modulus is `10^s/z^(ell-1)` with at most eight square branches, five branches for exponent five, and one for every other odd prime. There is no extra smooth-factor multiplier in the branch count.

7. **Determinant and centered gap.** Strict curvature makes the three-point determinant nonzero. Nested integral powers of ten and a fixed compressed branch imply divisibility by `D Q_1`. The signed absolute error decreases with the endpoint. Comparing upper and lower determinant bounds cancels the remainder `r` exactly and gives the stated gap with loss `4ell`.

8. **Endpoint-uniform counting.** With `h=N+t/d-4ell/(ell-1)`, the full endpoint interval satisfies `L/2<=h<10L` for `d>=3`. Alternating solution subsequences grow by factors greater than `ell`. This permits at most ten points per square group and six per odd-prime group. Multiplying by branches, remainders, and curvature intervals gives exactly `320` and `12 c_ell ell` per cut. The nine small cuts are counted trivially. Width two has only `4815` proper nonempty-cut pairs and is handled separately, rather than being silently included in the fixed-odd-prime assertion.

9. **Union over every prime exponent.** The threshold split at `P=d^2` and `E=2B` covers any witnessing odd prime. Small primes use the fixed-prime theorem. Medium strong-late roots inject into compressed residue classes. All remaining medium-prime pairs lie in one common cut strip and are counted once as a union, without an extra prime factor. Large exponents have `y<sqrt(B)` and `ell<4dB`; their multiplicity is bounded by `d`, not assumed to be one across different cut widths. These steps justify the full unbounded-exponent quantifier.

10. **Constants and cumulative scope.** The polynomial/geometric inequalities and the elementary prime-counting bound give the displayed constants. Adding `k=0` and the small cuts once gives `330`, `11`, and `17`. For width two there are only `4905` pairs including `k=0`. Summing complete endpoint-width blocks through an arbitrary `X` proves the cumulative bounds; the finitely many one-digit endpoints cause no gap.

## Reproducible finite corroboration

The author verifier `verify_unified_full_prefix.py` was reread and rerun successfully. Its output matched `unified-full-prefix-certificate.json`. It checks 4,991 prefix cases, 11,055 exact rotation/bound cases, all fourteen exceptional valuation pairs, 1,540 prime-power and 556 decimal compressed-root cases, 3,240 exact rational derivative evaluations, and centered bounds through width 1000. Its synthetic determinant cases are not claimed to be actual power rotations.

The independently written `verify_independent_full_prefix.py` also passes. Its certificate is `independent-full-prefix-certificate.json`, with captured output in `independent-full-prefix-verification.txt`. It separately checks:

- exact valuation equality with `j` for every `10<=k<=10000`;
- all 44,814 proper nonempty-cut rotation identities with `10<=m<=300`, including 20,709 earlier-width and 24,105 same-width cases;
- 2,518 cases with negative correction;
- 1,080 exact rational curvature checks, including exponents through 101 and both signs of the correction;
- the centered endpoint bounds for every width from 3 through 1000.

The union verifier `../a001292-global-union/verify_global_perfect_power_union.py` was also reread and rerun successfully. Its finite checks include 54,401 compressed-root fibers, 44,850 rotation/cut-recovery cases, exact width inequalities through 2000, and the elementary prime estimate through 200000.

These finite tests corroborate the algebra and catch implementation mistakes. The general theorem rests on the written arguments reviewed above, not on extrapolating finite searches or on numerically evaluating a purported universal symbolic identity.

## Audited SHA-256 versions

| File | SHA-256 |
|---|---|
| `UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md` | `c3f2e1c7d8419c9a611e95f9702dc9cd4be25e5f0411810fc36eb53740c76b33` |
| `verify_unified_full_prefix.py` | `dbb0f26929191426659de3ff09428c7b06fb3afb5ff803078d0e2f2cf9699572` |
| `verify_independent_full_prefix.py` | `fa753d51e12adee13cb1be98281974dc2f3e34c0c64faa4ef2e1d55329047f22` |
| `../a001292-global-union/GLOBAL_PERFECT_POWER_UNION.md` | `b75fb3140ce3673a1ca06f0ef090ec5c67f3feff05d6e58b24a0e6d9325bf28b` |
| `../a001292-global-union/verify_global_perfect_power_union.py` | `bc388cfdefe568e50252dacd1931e1cce774bf3e26986e0981a87ecb1f6fa64c` |

No remaining mathematical blocker was identified for these versions. No literature-priority claim or solution of the nonexistence conjecture is certified.
