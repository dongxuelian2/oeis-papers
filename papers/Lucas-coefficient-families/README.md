# Lucas coefficient families

For Lucas numbers `L_0=2, L_1=1` and Fibonacci numbers `F_0=0, F_1=1`, this paper proves two infinite coefficient-family theorems.

For every `r >= 1`, setting `q = 5 F_(2r)` makes each positive value `L_i - q L_j` uniquely represented. Its positive pairs are exactly `(2r+2,1)` and `i >= 2r+3, 1 <= j <= i-2r-2`, giving a triangular bounded-index count and logarithmic-squared growth. The case `q=5` extends the result for [A191981](https://oeis.org/A191981).

For every coefficient `q=L_m` (`m>=1`), both `q L_i-L_j` and `q L_i+L_j` contain infinitely many repeated values. More generally this holds for every positive integer quotient `q=L_m/L_h` with odd `m>h`, or `q=F_m/F_h` with even `m>h`; `q=2` is an additional explicit case. A unified Lucas difference identity constructs the collisions. A transfer lemma connects sum collisions and reversed-difference collisions under a unique-positive-difference hypothesis.

- [Paper PDF](main.pdf) | [LaTeX source](main.tex).
For **every integer coefficient** `q` (positive, zero, or negative), the paper also provides an explicit finite bound on the indices of any positive representation below a threshold, using the algebraic norm of `phi^d-q`. This yields fully exact set membership, representation multiplicity, distinct-value counting and nth-term algorithms for all three forms `S=L_i-qL_j`, `T=qL_i-L_j`, `P=qL_i+L_j`. For `q=0`, `S` and `P` each have infinitely many representations of each Lucas number. An additional proposition excludes simultaneous-shift positive collisions for every `q>=2`. **Every q>=2 has finitely many positive collisions in S_q**, and every collision's larger first index satisfies `k<=6*t`, where `t` is the least positive index with `L_t>200*(q+1)^4`. Therefore all collisions and global uniqueness can be decided exactly for any q>=2. In addition, each `S_q` has asymptotic distinct-value count `0.5*(log_phi x)^2+O_q(log x)`.

- `family.py`: exact count, nth positive term, admissible pairs, and explicit repeated witnesses.
- `all_integer.py`: universal integer-only computations for all three forms and every coefficient.
- `global_collisions.py`: proved complete collision and global uniqueness report for any q>=2.
- `ratio_collisions.py`: exact Lucas/Fibonacci quotient coefficients with collision witnesses.
- `verify.py`: independent brute-force checks over 30 coefficients of the collision-free family and 20 of the colliding family.
- `verify_all_integer.py`: 2,673 finite threshold audits across all signs and three expression forms, plus exact multiplicity and nth-term comparisons.
- `verify_global_collisions.py`: certified whole-infinite-sequence uniqueness classifications for coefficients 2 through 100 and independent enlarged-index checks.
- `verify_ratio_collisions.py`: exact identities and positive repeated witnesses for all tested quotient coefficients and the special case q=2.

Run `python3 verify.py && python3 verify_all_integer.py && python3 verify_ratio_collisions.py && python3 verify_global_collisions.py`; global example: `python3 global_collisions.py 25`; universal examples: `python3 all_integer.py S -4 count 1000`, `python3 all_integer.py T 7 witnesses 20`, `python3 all_integer.py P 13 nth 100`; examples: `python3 family.py coefficient 3`, `python3 family.py nth 1 100`, `python3 family.py repeat 2 15`.

A separate [A191980–A191983 manuscript](https://github.com/dongxuelian2/oeis-papers/pull/24) treats the special case `q=5` in greater detail.
