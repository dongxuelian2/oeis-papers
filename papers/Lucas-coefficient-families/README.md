# Weighted Lucas sums and differences: coefficient classification and four OEIS sequences

[Paper (PDF)](main.pdf) · [LaTeX source](main.tex)

Let `L_n` be the Lucas numbers. The single manuscript studies positive values of
`S_q = L_i - q L_j`, `T_q = q L_i - L_j`, and `P_q = q L_i + L_j`
for integer `q` and positive indices `i,j`.

For every `q >= 2`, `S_q` has only finitely many repeated positive values,
and all collision indices are at most `6t`, where `t` is the first
index for which `L_t > 200(q+1)^4`. The family `q = 5F_(2r)`
has unique positive differences for every `r >= 1`.

The coefficients giving infinitely many repeated values in `T_q`
and `P_q` are **exactly**:

- Integer `L_m/L_r` with odd `m > r >= 1`.
- Integer `F_m/F_r` with even `m > r >= 2`.
- `L_(6r+3)/2` for `r >= 0`.

Every finite collision is parametrized by two Lucas gaps:
`q = (L_b-L_a)/(L_d-L_c)`, with `a < b` and `c < d`.
The sign of `L_a L_d - L_b L_c` distinguishes collisions in
`S_q` (positive sign) and `T_q` (negative sign); their union
classifies collisions in `P_q`. A collision witness, if one
exists, occurs with all indices at most `13t+1`.
The paper also covers zero, unit, and negative coefficients.


## Four OEIS sequences at q = 5

The same manuscript gives complete results for
[A191980](https://oeis.org/A191980) (sums),
[A191981](https://oeis.org/A191981) (positive differences),
[A191982](https://oeis.org/A191982) (reversed positive differences),
and [A191983](https://oeis.org/A191983) (their nonnegative union).

- A191981 has unique positive representations.
- A191982 has exactly five repeated positive values: \`2, 4, 8, 14, 17\`.
- A191980 has exactly five repeated values: \`16, 23, 38, 62, 91\`.
- The complete intersection \`S_5 ∩ T_5\` comprises nine exceptions and the families \`3L_n\`, \`8L_n\` (\`n>=6\`).
- The complete intersection \`P_5 ∩ T_5\` comprises fourteen exceptions and the two families \`5L_n+L_(n+7)\`, \`5L_n+L_(n-3)\` (\`n>=4\`).
- Exact counting and unranking formulas cover all four sequences and both intersections.

The original q=5 [integer verification scripts](../A191980-A191983/)
remain separate for auditing; they are not a second paper.


## Full-index formulas and growth

The manuscript gives finite-minimum formulas for every OEIS term using
the exact counting functions and explicit Lucas-number upper bounds.
A191981, A191982 and A191983 start with zero; A191980 starts with 6.
Each bound has a Lucas index of order \(\sqrt n\).

With \(\varphi=(1+\sqrt5)/2\), the precise growth laws are
\[
\log_\varphi a_{191981}(n)=\sqrt{2n}+O(1),\qquad
\log_\varphi a_{191982}(n)=\sqrt{2n}+O(1),
\]
\[
\log_\varphi a_{191980}(n)=\sqrt n+O(1),\qquad
\log_\varphi a_{191983}(n)=\sqrt n+O(1).
\]
The current formulas are exact finite minima; closed-form expressions
without a minimum remain a separate research target.

## Verification

The verification scripts remain in this directory:

- `verify.py`, `verify_ratio_collisions.py`: constructed families.
- `verify_global_collisions.py`, `verify_stationary_collisions.py`: rigorous finite cutoffs.
- `verify_norm_stationary.py`, `verify_explicit_infinite.py`: independent stationary and coefficient-family classifications.
- `verify_signed_gap.py`, `verify_all_global_unique.py`: finite collision spectra and all three forms.
- `verify_all_integer.py`: exact counts, multiplicities, and finite-value computations.

The reference implementations are `family.py`, `all_integer.py`,
`global_collisions.py`, `stationary_collisions.py`,
`norm_stationary.py`, `explicit_infinite.py`,
`signed_gap.py`, `all_global_unique.py`, and `ratio_collisions.py`.
The [GitHub Actions workflow](../../.github/workflows/lucas-coefficients.yml)
runs the full verification suite and compiles the manuscript.

