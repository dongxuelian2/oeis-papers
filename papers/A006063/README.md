# Cube-sum permutations — OEIS A006063 / A096680 / A096904

Authors: Qichao Wang and Daoyu Dong.

## Canonical manuscript

- [Main paper (PDF)](main.pdf)
- [LaTeX source](main.tex) and [appendix](appendix.tex)

The paper gives the exact existence classification for cube-sum permutations, the eventual multiplicity theorem, and parity-minimal involution constructions. The classification has 48 admissible sizes below 173 and all sizes at least 173. The multiplicity result proves at least three solutions for every size at least 175.

## Verification

The main proof uses exact certificates in [certificates](certificates/) and Python verification programs. The checks in `reproduce.py` cover the finite basis, existence and nonexistence certificates, multiplicity, and eventual involutions.

From the repository root:

```sh
python3 papers/A006063/reproduce.py --report build/a006063-verification.json
```

To compile the manuscript:

```sh
cd papers/A006063
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Relevant OEIS entries: [A006063](https://oeis.org/A006063), [A096680](https://oeis.org/A096680), [A096904](https://oeis.org/A096904).
