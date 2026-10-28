# Collisions in weighted Lucas sums and differences

[Paper (PDF)](main.pdf) · [LaTeX source](main.tex)

Let `L_n` be the Lucas numbers. The paper studies positive values of
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

The companion [A191980–A191983 paper](../A191980-A191983/main.pdf)
develops the OEIS case `q=5` in detail.
