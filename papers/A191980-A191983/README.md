# A191980–A191983 — weighted Lucas sums and differences

This manuscript covers [A191980](https://oeis.org/A191980), [A191981](https://oeis.org/A191981), [A191982](https://oeis.org/A191982), and [A191983](https://oeis.org/A191983).

A191981: Ordered sequence of nonnegative differences f-5g, where f and g are Lucas numbers (A000032 beginning at 1).

The manuscript proves that every positive difference `L_i - 5 L_j` has a unique pair `(i,j)`, identifies all positive index pairs, and obtains the counting asymptotic `A(x) = (log_phi x)^2/2 + O(log x)`. It gives an exact three-block counting formula, direct residue-class unranking, and integer membership tests. The positive intersection with A191982 is exactly `{2,6,9,12,13,14,24,32,61} ∪ {3*L_n, 8*L_n : n>=6}`, with an exact counting formula and logarithmic growth. A191982 has exactly five multiply represented positive values, `{2,4,8,14,17}`, each appearing twice. These results yield exact counting and nth-term algorithms for A191982 and the union A191983. For A191980, there are exactly five multiply represented values `{16,23,38,62,91}`; its exact counting algorithm and the complete positive intersection with A191982 are established: fourteen exceptions `{6,8,9,12,16,19,22,24,26,31,34,44,52,138}` together with two disjoint families `{5*L_n+L_(n+7):n>=4}` and `{5*L_n+L_(n-3):n>=4}`. The intersection has an exact counting and nth-term algorithm, with `J(x)=2 log_phi(x)+O(1)`.

- [Manuscript (PDF)](main.pdf) · [LaTeX source](main.tex)
- `rank.py`: exact counting, nth terms, residue substreams, and membership with unique witness.
- `intersection.py`: exact membership, counting and indexing for A191981 intersect A191982.
- `count_union.py`: exact counting and unranking for A191982 and A191983.
- `sums.py`: exact counting, nth terms, and every index witness for A191980.
- `sum_difference_overlap.py`: complete A191980/A191982 positive intersection membership, exact counts, and unranking.
- `verify.py`: exact-integer checks of the published prefixes, uniqueness, counting, ranking and overlaps.
- `verify_intersection.py`: finite boundary-certificate checks and exhaustive overlap comparisons.
- `verify_duplicates.py`: five-collision classification checks and independent counting/rank tests.
- `verify_sums.py`: A191980 OEIS prefix, collision and rank tests, and infinite overlap identities.
- `verify_sum_difference_overlap.py`: 18 recurrence-inequality certificates at indices 8,9, finite exceptions, and an independent 240-index intersection join.

Run: `python verify_sum_difference_overlap.py`; `python sum_difference_overlap.py nth 100`; `python verify_sums.py`; `python sums.py nth 100`; `python verify.py`; `python verify_duplicates.py`; `python count_union.py union-nth 100`; `python verify_intersection.py`; `python intersection.py count 100000`; `python rank.py nth 100`; `python rank.py count 100000`; `python rank.py residue 30 --mod5 3`.
