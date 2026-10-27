# Lucas coefficient families

For Lucas numbers `L_0=2, L_1=1` and Fibonacci numbers `F_0=0, F_1=1`, this paper proves two infinite coefficient-family theorems.

For every `r >= 1`, setting `q = 5 F_(2r)` makes each positive value `L_i - q L_j` uniquely represented. Its positive pairs are exactly `(2r+2,1)` and `i >= 2r+3, 1 <= j <= i-2r-2`, giving a triangular bounded-index count and logarithmic-squared growth. The case `q=5` extends the result for [A191981](https://oeis.org/A191981).

For `q = L_(2r)`, both `q L_i - L_j` and `q L_i + L_j` contain infinitely many repeated values, with explicit identities. A transfer lemma connects sum collisions and reversed-difference collisions under a unique-positive-difference hypothesis.

- [Paper PDF](main.pdf) | [LaTeX source](main.tex).
- `family.py`: exact count, nth positive term, admissible pairs, and explicit repeated witnesses.
- `verify.py`: independent brute-force checks over 30 coefficients of the collision-free family and 20 of the colliding family.

Run `python3 verify.py`; examples: `python3 family.py coefficient 3`, `python3 family.py nth 1 100`, `python3 family.py repeat 2 15`.

A separate [A191980–A191983 manuscript](https://github.com/dongxuelian2/oeis-papers/pull/24) treats the special case `q=5` in greater detail.
