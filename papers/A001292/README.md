# OEIS A001292: rigorous residue-class exclusions for the Kashihara conjecture

**Status: partial rigorous results only (2026-10-16).** Kashihara's global conjecture is **not proved or disproved**. Novelty beyond the references below has **not** been established. These theorems exclude several infinite families of *blocks* `1,2,...,m` and **all of their cyclic rotations**. They do not determine which of the remaining rotations might be perfect powers.

## Problem and previous work

For each integer `m >= 1`, form the decimal word `W_m = 1 || 2 || ... || m`. Let `R_{m,j}` be the decimal integer obtained by cutting the first `j` entire positive-integer blocks and moving them to the end, for `0 <= j < m`. OEIS [A001292](https://oeis.org/A001292) is the increasing enumeration of all these cyclically rotated words. Kashihara's conjecture says that none except `1` is a nontrivial perfect power. Ripà (2022) excluded **all block permutations** for `m == 2,3,5,6 (mod 9)` by digit-sum valuation; this report studies previously unexcluded values `m == 0,8 (mod 9)`.

## Theorem 1: a universal mod-27 formula

Write `d = floor(log_10(m)) + 1` for the **integer decimal digit length**, and `D(m) = sum_{k=1}^m ell(k)` for the number of digits in `W_m` (where `ell(k)` is the decimal digit length of `k`). Then

\[
\boxed{W_m \equiv \frac{m(m+1)}2 + 9 d\left\lfloor\frac{m+1}3\right\rfloor\pmod{27}},
\qquad
\boxed{D(m)\equiv dm\pmod9}.
\]

**Proof.** Since `10^a = (1+9)^a == 1+9a (mod 27)` for all nonnegative integers `a`, expand every block according to its number of following digits:

\[
W_m=\sum_{k=1}^m k\,10^{D(m)-D(k)}
\equiv \frac{m(m+1)}2
  +9\sum_{r=1}^m \ell(r)\frac{r(r-1)}2\pmod{27}.
\]

Modulo `3`, the triangular number `r(r-1)/2` is `1` if `r == 2 (mod 3)` and otherwise `0`. Set `h = floor((m+1)/3)`, the number of `r <= m` with `r == 2 (mod 3)`. For `r`-digit lengths,

\[
\ell(r)=1+\sum_{a=1}^{d-1}\mathbf1_{\{r\ge10^a\}}.
\]

For each threshold `10^a`, the number of `r == 2 (mod 3)` in `1,...,10^a-1` is `(10^a-1)/3`, a multiple of `3` (because `10^a == 1 (mod 9)`). Hence

\[
\sum_{\substack{1\le r\le m\\r\equiv2\ (3)}}\ell(r)
\equiv dh\pmod3.
\]

This proves the first formula. Also `D(m) = dm - sum_{a=1}^{d-1}(10^a-1)`; every summand is a multiple of 9, proving the second formula. QED.

## Theorem 2: two infinite exclusions by 3-adic valuation

For every `m >= 2` satisfying **either**

1. `m == 9 (mod 27)`, with *any* decimal digit length; **or**
2. `m == 17 (mod 27)` and `d == 0 (mod 3)`, where `d` is the decimal digit length of `m`,

**none of the `m` cyclic rotations of `W_m` is a nontrivial perfect power**.

**Proof.** In either case Theorem 1 gives `W_m == 18 (mod 27)` and `3 | D(m)`. If `P` is the initial prefix of `j` whole blocks and its decimal length is `L`, the rotation identity is

\[
R_{m,j}=10^L W_m+P(1-10^{D(m)}).
\]

As `3 | D(m)`, `10^{D(m)} == 1 (mod 27)`; since `W_m == 18 (mod 27)` and `10^L == 1 (mod 3)`, we conclude

\[
R_{m,j}\equiv18\pmod{27}
\quad\text{for all }0\le j<m.
\]

For any integer `N == 18 (mod 27)`, `v_3(N)=2`. If `N = a^e` with `e >= 2`, this forces `e=2` and `v_3(a)=1`. But any such square equals `9u^2 == 9 (mod 27)` for `3 \nmid u`, not `18`. Thus `N` is not a perfect power. QED.

This strictly extends the mod-9 theorem from Ripà on A001292: both excluded classes lie in the previously unsolved `m == 0,8 (mod 9)` classes.

## Theorem 3: an independent infinite mod-13 exclusion

For each `t >= 0`, put

\[
  d=6t+3,\qquad m_t=10^{d}-10.
\]

If

\[
\boxed{t\equiv0,1,3,5,7,8\pmod{13}},
\]

none of the `m_t` cyclic rotations of `W_{m_t}` is a nontrivial perfect power.

**Proof.** First `d == 0 (mod 3)` and `m_t == 18 (mod 27)`. Theorem 1 gives `W_{m_t} == 9 (mod 27)`, hence `v_3(W_{m_t})=2`. The same exact valuation holds for every rotation because `3 | D(m_t)`, by the rotation identity. Therefore a perfect power, if any, would have to be a square.

Next we show the **exact symbolic formula**

\[
\boxed{W_{m_t}\equiv6+5t\pmod{13}}.
\]

Let `U_j` be the concatenation of *all* `j`-digit positive integers, from `10^{j-1}` through `10^j-1`. For `j >= 2`, there are `9*10^{j-1}` such integers, a multiple of 6. Since `ord_13(10)=6`, appending `U_j` leaves an existing prefix residue unchanged mod 13 and adds `U_j (mod 13)`. An affine-recursion or geometric-sum computation gives the following complete-block residues, periodic with period 6 for `j >= 2`:

| `j (mod 6)` | 2 | 3 | 4 | 5 | 0 | 1 |
|---|---:|---:|---:|---:|---:|---:|
| `U_j (mod 13)`, `j>=2` | 5 | 8 | 11 | 4 | 7 | 12 |

The period-6 claim follows rigorously because `10^{j+6} == 10^j (mod 13)` and the number of appended integers is congruent modulo both 6 and 13 for `j` and `j+6`. Each 6-block period adds `5+8+11+4+7+12 == 8 (mod 13)`. The prefix ending at `10^{d-1}-1` includes `U_1,...,U_{d-1}` and has residue `1+5+8t == 6+8t (mod 13)`.

The last, incomplete, `d`-digit block runs from `10^{d-1}` to `10^d-10`. It has `q=9(10^{d-1}-1)` (an odd number) of terms. Since `d == 3 (mod 6)`, each step multiplies the previous concatenation by `B=10^d == -1 (mod 13)` and adds the next integer. With `a=10^{d-1} == 9 (mod 13)`, the total transformation is

\[
x\longmapsto -x+\sum_{h=0}^{q-1}(-1)^h(a+h)
= -x+a+\frac{q-1}{2}
\equiv -x+12\pmod{13}.
\]

Thus `W_{m_t} == 12 - (6+8t) == 6+5t (mod 13)`.

The nonsquare residues modulo 13 are `{2,5,6,7,8,11}`. Exactly when `t == 0,1,3,5,7,8 (mod 13)`, `6+5t` is a nonsquare. The decimal total length `D(m_t)` is divisible by 3 because `m_t` is divisible by 9, and it is even because `d` is odd and `m_t` even: explicitly `D(m_t)= d m_t - sum_{a=1}^{d-1}(10^a-1)`, an even number. Thus `6 | D(m_t)` and `10^{D(m_t)} == 1 (mod 13)`.

Finally, `10 == 6^2 (mod 13)`; so for every rotation, `R_{m_t,j} == 10^L W_{m_t} (mod 13)` is again a nonzero quadratic nonresidue. This rules out squares, and the 3-adic valuation 2 rules out every power of exponent 3 or higher. QED.

## What remains open

- These are disjoint *infinite exclusions*, not a solution of Kashihara's conjecture.
- Cases `m == 1,4,7,8,0 (mod 9)` remain in general, except for the explicitly treated subfamilies.
- A finite modular sieve for arbitrary `m` (even a very long one) is not a global proof unless an actual finite period in `m`, across digit-length transitions, is proved.
- These claims concern cyclic rotations of **whole integer blocks**; extending the mod-27 statement to all arbitrary block permutations would be unjustified.
- Novelty search is preliminary. Compare Ripà (2022) and OEIS comments before a formal publication or a claimed first discovery.

## Verification

Run `python verify_a001292.py`. The script uses modular rolling concatenation, an independent formula check, selected full rotations, and a fast affine-block evaluator allowing astronomically large `m_t` to be tested modulo 13 without constructing their full decimal representation.

## References

- OEIS [A001292](https://oeis.org/A001292), Kashihara's conjecture and OEIS comments.
- Marco Ripà, *On some open problems concerning perfect powers*, [arXiv:2205.10163](https://arxiv.org/abs/2205.10163) (2022), especially the mod-9 exclusion.
- `dongxuelian2/three-term-decimal-concatenation-square-sum`, foundational radix-structure and modular methods: https://github.com/dongxuelian2/three-term-decimal-concatenation-square-sum
- `ddy314/math`, independent methods and audit context: https://github.com/ddy314/math
