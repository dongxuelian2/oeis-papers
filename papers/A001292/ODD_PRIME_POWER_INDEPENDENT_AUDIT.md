# Independent audit of the odd-prime-power sparsity proof

**Verdict: PASS.** The saved proof establishes an effective elementary bound

    # {admissible (m,k): R_(m,k)=y^ell for some odd prime ell} < 20 B^2/d,

where `d>=2`, `B=10^d`, `L=B/10`, `2L<=m<B`, and `L+7<=k<m`.
All cubes are included. The previously omitted cube-central band is removed by the all-cut `<24B` cube count in Section 9.

## Audited files

- Proof: `ODD_PRIME_POWER_SPARSITY.md`
- Proof SHA-256: `0073143f4acaca32bd361577600d8cb568f44bdec8c2911f5e53f4644bb83deb`
- Independent finite checker: `verify_odd_prime_power_sparsity.py`
- Checker SHA-256: `7b0eb9c09a6a5395c95804710b1801267621009f5839573a6b0299862d5e58d0`
- Finite output: `odd-prime-power-certificate.json` and `odd-prime-power-verification.txt`
- Certificate and captured-output SHA-256: `228fa57bb5e81ad518e4f57a41717c1634f839021e50f49e0fe590c483ea8edc`

The inherited exact identities and square determinant method were also read in `UNIFORM_CUT_SPARSITY.md` and `CENTRAL_CUT_DETERMINANT_SPARSITY.md`.

## Formal proof checks

1. **Approximation and valuations.** The transformation `x=Cy`, the coefficient `C^(ell-2)`, the bound `0<alpha-x/Q<200 B^(K-N+1)`, and the forced valuations `ell*v_p(x)=v_p(J)` for `p=2,5` are correct. Fixed `r=H mod ell` gives nested integral powers of ten; the fixed 2-adic numerator order prevents coincident rational approximants.
2. **Early fixed-exponent count.** The center shift is at most `15/8`, four initial integer endpoints suffice, and the remaining centered gaps multiply by more than `ell`. The number of residue groups is at most `ell/gcd(ell,d)`.
3. **Compressed late congruences.** The correct modulus is `D=B^K/z^(ell-1)`, not `B^K`. There is one branch unless `ell=5`, when there are at most five. The strong-late size inequality gives `0<x<D`, and strict growth in `m` supplies the required injection. The remaining half-open strip has at most three integer cuts per endpoint.
4. **All-cut coverage for primes at least five.** The inequality `(ell-2)N>2t/d+ell` holds throughout the declared domain. The cube exception of the early/late argument is correctly identified and later independently covered.
5. **Elementary prime counting.** The even and odd binomial-coefficient induction establishes `theta(u)<=u log 4`. Splitting at `sqrt(u)`, using `log u<sqrt(u)`, gives `pi(u)<4u/log u` for every real `u>1`. No prime number theorem is used.
6. **Low/middle/high exponent union.** Only low-prime early counts are summed. The common nonlate strip `K<B/P` counts pairs directly, with no extra prime factor. For high exponents, `y<sqrt(B)` and `ell<4dB`; each representation `(y,ell)` determines at most one pair `(m,k)` because the last `d` decimal digits determine `k` and the decimal length determines `m`. Duplicate representations can only overcount.
7. **Cube determinant.** The scaled `T(Q)` and derivative identity (24) are correct. The ratio `T/b>5/6` gives strict concavity, excluding zero determinants. The compressed modulus and nested denominators imply `D Q_1` divides the determinant. Its error-column estimate gives `N_3>3N_1-t/d-11`. The proof now explicitly records the elementary numerical step `3 log_10(400)<8`, equivalent to `400^3<10^8`. The center satisfies `L/4<=h<9L` including `d=2`. Each alternating subsequence has at most four terms, proving `<24B` cubes.
8. **Uniform constants.** The added cube cover changes the linear remainder from `4B` to `28B`. The final coefficient is

       3 + 14/25 + 1 + (32+16/5)/log(10)
       = 19.847165762994464... < 20.

   The polynomial/exponential width inequalities hold at the initial widths and decrease thereafter. The bound is uniform for every `d>=2`.

9. **Combined perfect powers and width sum.** Section 11 correctly reduces every nontrivial integer perfect power to a prime exponent, combines the odd-prime theorem with the separate square bound, and sums only the declared same-width domains. Splitting the width sum at `D/2` gives `sum_(2<=d<=D) 10^(2d)/d=O(10^(2D)/D)`. Since `10^D<=10X` and `D` is comparable to `log X`, the scoped cumulative bound is `O(X^2/log X)`. The square term is absorbed because `d log d/10^d` is bounded.

The final audit corrected one harmless strictness typo in the high-exponent paragraph: `ell<=log_2(R)` follows from `y>=2`; the subsequent upper bounds remain strict. No substantive mathematical correction was needed.

## Reproducible finite corroboration

Run `python verify_odd_prime_power_sparsity.py` in this directory. The actual final file was read and rerun after the author confirmed it was stable. It uses only the Python standard library and passed:

- 34,366 nonzero local-target classes checking valuations and compressed root-branch counts, for exponents 3, 5, 7, 11, 13 and small powers of 2 and 5.
- 360 exact rational instances of the general derivative algebra, for exponents 2 through 31.
- The cube-center and union-constant inequalities at all widths 2 through 1,000, using exact integer/rational arithmetic.
- The prime-counting inequality at all integers 2 through 200,000, using a direct sieve.
- Exact rotation identities, the positive-error bound, and the local congruence for all 3,400 admissible width-2 pairs.
- Decimal-length and final-block identification for the same 3,400 admissible width-2 rotation pairs.

The derivative checks are exact test instances, not a symbolic universal verification. The code does not claim an exhaustive search for all perfect powers or replace any all-width proof. In particular, the width-2 injection check does not assert that those rotations are not perfect powers.

## Scope guardrails

This is a sparsity theorem for pairs in the specified same-width endpoint/cut region. It is not nonexistence. It neither bounds the largest possible counterexample nor covers endpoints `m<2L`, cuts `k<L+7`, or earlier-width cuts. It is not by itself a theorem about every rotation or a solution of the integer-power conjecture. Square powers require the separate square theorem; they are not part of the odd-prime theorem unless also odd powers.
