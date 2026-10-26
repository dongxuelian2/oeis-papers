# Analytic, sieve and partition screening, 2026-10-26

All linked official pages were opened, including comments, formulas and references.
Rows refer to distinct entries; related entries are grouped as one research direction
in the batch summary. A conjecture label alone is not evidence of current novelty.

| Entry | Official question or observation | Outcome |
|---|---|---|
| [A214972](https://oeis.org/A214972) | Its unit jumps occur exactly at A152009. | Proved for every index, with generalization to every deletion modulus d>=2. |
| [A152009](https://oeis.org/A152009) | Proposed recurrence and triangular limit of repeated L-sieves. | Both proved. Convergence is deterministic on the natural nonempty, infinite-complement domain; stabilization bound 2k-1. |
| [A248520](https://oeis.org/A248520) | Constant-step cotangent positions have slope pi/(pi-2). | Proved with O(1) additive error and exact at-most-three-candidate formula. |
| [A248521](https://oeis.org/A248521) | Increasing-step cotangent positions have slope pi/2. | Proved with O(1) error and explicit inverse-cotangent term formula. |
| [A340424](https://oeis.org/A340424) | Partition triangle row sums equal n*p(n). | Elementary generating-function reduction identified, but mirror A245099 and standard partition derivative identity already encode it; not counted as new research. |
| [A245099](https://oeis.org/A245099/internal) | Mirror triangle uses cumulative divisor sums and partitions without 1. | Prior-result control for A340424; no separate new question claimed. |
| [A159633](https://oeis.org/A159633) | Eisenstein dimension formula labeled conjecture. | Excluded: the same page's program explicitly credits P. Humphries's 2014 proof. |
| [A232434](https://oeis.org/A232434) | Partition-weight recursion equals stabilized reversed-row limit. | Deferred: nontrivial q-triangle/partition bijection; no proof obtained. |
| [A272397](https://oeis.org/A272397) | Rogers-Ramanujan-type product/sum partition identity. | Deferred: substantial q-series identity with existing Kanade-Russell literature; no complete proof or current-literature audit obtained. |
| [A383115](https://oeis.org/A383115) | Summatory central-divisor-square-root statistic grows as 4*N^(3/2)/3. | Deferred: delicate divisor distribution; no proof obtained. |
| [A329369](https://oeis.org/A329369) | Biased-rook/excedance equivalence and inverse binary binomial transform. | Deferred: several existing results and a 2024 linked recursion answer require deeper attribution review. |
| [A214971](https://oeis.org/A214971) | Base-phi membership formulas and Fibonacci difference word. | Deferred: one older conjecture already explicitly proved; remaining claims require canonical base-phi representation review. |

For A340424, if P(q)=product(1-q^j)^(-1), then the no-1 partition g.f.
is (1-q)P(q), and cumulative sigma has g.f. (sum sigma(j)q^j)/(1-q).
Their product is qP'(q). This is a direct standard-identity consequence and
is retained as a screening note rather than advertised as a new independent theorem.

Exact-source follow-up searches for A214972/A152009 and A248520/A248521 returned
the official statements with no proof on those pages. This is not an exhaustive
literature-priority review. No official edits were submitted.
