# A006716: exact classification of roots with at most 17 nonzero digits

Authors: Qichao Wang (Hebei University of Technology) and Daoyu Dong (University of Electronic Science and Technology of China). Research certificate, October 22, 2026. **No full finiteness theorem** for A006716 and **no new OEIS member** is claimed. Manuscripts and PDFs remain unchanged.

## The result

**Theorem (computer-certified finite classification).** Let \(\nu_{10}(x)\) be the number of nonzero decimal digits of a positive integer x. If every digit of \(x^2\) is in \(\{1,4,9\}\) and \(\nu_{10}(x)\le17\), then x belongs to the 17 square roots previously reported in OEIS A027675. In particular, there are **no A006716 square roots with exactly 17 nonzero decimal digits**.

The preceding support classes r<=16 were independently proved by the separate complete certificates indexed in [SPARSE_ROOTS.md](SPARSE_ROOTS.md). The new r=17 exclusion was independently enumerated in six disjoint units-digit classes by [verify_sparse_roots_17.cpp](verify_sparse_roots_17.cpp):

| final root digit | exact terminal candidate count | successful roots |
|---:|---:|---:|
| 1 | 171,650,208 | none |
| 2 | 107,967,008 | none |
| 3 | 92,701,557 | none |
| 7 | 380,875,967 | none |
| 8 | 177,741,697 | none |
| 9 | 104,052,733 | none |
| **Total** | **1,034,989,170** | **none** |

Each shard's full GitHub Actions job passed in [run 39764490169](https://github.com/dongxuelian2/oeis-papers/actions/runs/39764490169). The source now pins the observed exact leaf counts and **fails** if any matching root is encountered. An optional [alternative gap-pruned program](verify_sparse_roots_17_gap.cpp) separately checks the largest units-7 shard, using the subsequently proved universal fourth-gap bound, in [its own CI workflow](../../.github/workflows/a006716-support17-gap.yml). Its counts need not agree because the pruning strategies differ; its **set of successful roots** must agree.

## Why the enumeration is complete

Let the nonzero root positions be \(0=e_1<e_2<\cdots<e_r\), and let the root digits at those positions be nonzero.

1. The root must have final digit in \(\{1,2,3,7,8,9\}\), since its square's last decimal digit must be one of \(\{1,4,9\}\).
2. The proven *low-digit gap theorem* gives \(e_{j+1}\le2e_j+2\), bounding the complete search tree without any guessed root magnitude.
3. The *high-digit gap theorem* restricts the last nonzero position to at most three after the previous one.
4. For each partial root \(p\), any later root digit added at exponent \(e\) changes no digit of \(p^2\pmod{10^e}\). Reject a branch only if one of these **fixed** digits is outside \(\{1,4,9\}\).
5. The [exact top-three leading-digit masks](verify_top_three_gaps.py) are generated from rational intervals for the first eight significant square digits, not from floating point or a heuristic. They provide additional **necessary** constraints when inserting the highest root digits and one level earlier.
6. The standard digit-sum inequality bounds the length of a valid square by \(81r^2\), hence bounds the root's highest exponent by \(\lfloor(81r^2-1)/2\rfloor\). This bound is proved for all genuine solutions, not assumed experimentally.
7. Every terminal root is squared using exact Boost.Multiprecision arbitrary-precision integers, and **every digit** of the square is checked.

The algorithm checks **all** possible supports and digit choices that are not already excluded by one of these rigorously necessary conditions. Six disjoint units-digit branches cover all roots.

## A further global theorem from this research

The separate [universal upper-span lemma](GLOBAL_HIGH_GAP.md) gives

\[
e_j-e_{j+1}\le e_1-e_j+3
\]

for decreasing nonzero root positions \(e_1>\cdots>e_r\), with a stronger +2 bound if the highest root digit is at most 3. The [ten-digit leading-prefix theorem](TOP_FOUR_GAP.md) strengthens the highest-four-position condition to

\[
e_3-e_4\le7
\]

for **all** A006716 roots with at least four nonzero digits. Applying the upper-span recurrence then gives

\[
e_j-e_{j+1}\le2^j \quad(j\ge4).
\]

These inequalities are support-independent. The alternative gap-pruned checker uses them to corroborate the difficult r=17 units-7 class, and they offer a concrete reduction for future r>=18 searches.

## Reproduction

```sh
g++ -std=c++17 -O3 papers/A006716/verify_sparse_roots_17.cpp -o /tmp/a006716_r17
for u in 1 2 3 7 8 9; do /tmp/a006716_r17 "$u"; done
python papers/A006716/verify_top_four_gaps.py
python papers/A006716/verify_high_gap.py
```

The six-shard full run is defined in `.github/workflows/a006716-support17.yml`, and the independent global theorem audits are in their separate GitHub Actions workflows.

**Limitations.** The next unsolved sparse-root class is r=18. Nothing above proves whether A006716 as a whole is finite. Pushing the support bound by one is an exact finite calculation, whereas the global gap lemmas are reusable analytical restrictions.
