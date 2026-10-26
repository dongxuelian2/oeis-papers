# A191981 — positive Lucas differences

[OEIS A191981](https://oeis.org/A191981): Ordered sequence of nonnegative differences f-5g, where f and g are Lucas numbers (A000032 beginning at 1).

The manuscript proves that every positive difference `L_i - 5 L_j` has a unique pair `(i,j)`, identifies all positive index pairs, and obtains the counting asymptotic `A(x) = (log_phi x)^2/2 + O(log x)`. It gives an exact three-block counting formula, direct residue-class unranking, and integer membership tests. The positive intersection with A191982 is exactly `{2,6,9,12,13,14,24,32,61} ∪ {3*L_n, 8*L_n : n>=6}`, with an exact counting formula and logarithmic growth.

- [Manuscript (PDF)](main.pdf) · [LaTeX source](main.tex)
- `rank.py`: exact counting, nth terms, residue substreams, and membership with unique witness.
- `intersection.py`: exact membership, counting and indexing for A191981 intersect A191982.
- `verify.py`: exact-integer checks of the published prefixes, uniqueness, counting, ranking and overlaps.
- `verify_intersection.py`: finite boundary-certificate checks and exhaustive overlap comparisons.

Run: `python verify.py`; `python verify_intersection.py`; `python intersection.py count 100000`; `python rank.py nth 100`; `python rank.py count 100000`; `python rank.py residue 30 --mod5 3`.
