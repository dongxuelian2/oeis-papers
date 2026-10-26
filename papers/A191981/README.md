# A191981 — positive Lucas differences

[OEIS A191981](https://oeis.org/A191981): Ordered sequence of nonnegative differences f-5g, where f and g are Lucas numbers (A000032 beginning at 1).

The manuscript proves that every positive difference `L_i - 5 L_j` has a unique pair `(i,j)`, identifies all positive index pairs, and obtains the counting asymptotic `A(x) = (log_phi x)^2/2 + O(log x)`. It gives an exact three-block counting formula, direct residue-class unranking, integer membership tests, and two infinite families in A191981 intersecting A191982 (and hence A191983). It also explains the initial zero.

- [Manuscript (PDF)](main.pdf) · [LaTeX source](main.tex)
- `rank.py`: exact counting, nth terms, residue substreams, and membership with unique witness.
- `verify.py`: exact-integer checks of the published prefixes, uniqueness, counting, ranking and overlaps.

Run: `python verify.py`; `python rank.py nth 100`; `python rank.py count 100000`; `python rank.py residue 30 --mod5 3`.
