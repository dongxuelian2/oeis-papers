# Proof audit

The key distinction is between an infinite visit class and a walk that
eventually leaves every finite collection of classes. The two cases are
handled separately in Lemmas 1 and 2.

| Step | Exact condition and justification |
| --- | --- |
| Legal continuation | The higher neighboring valuation class contains infinitely many labels, so a least unused eligible label always exists. |
| Infinite visits propagate | A neighbor visited finitely often has a fixed least unused label `M`. Every late departure from an infinitely visited class would choose a distinct label at most `M`, which is impossible. |
| Every label in an infinite class occurs | Selection within a class always uses its smallest unused label. Any permanently missing label bounds all later selections from that class. |
| Arbitrary seed | Let `K` be its largest normalized valuation. Classes above `K` have no initial holes, so the explicit queue formula applies there. The recurrence is used only at `k>=K+2`. |
| Escape and edge balance | Finitely many visits to every level imply that the level tends to infinity. For each cut `j>=K`, the path starts below it and ends above it, giving `U_j-D_j=1`. |
| Visit count | At an unseeded level `j>K`, each visit is an arrival. Therefore `c_j=U_(j-1)+D_j=U_(j-1)+U_j-1`. |
| Final departure | The last departure from level `k` must go upward. Its lower neighbor has already completed all visits; its upper neighbor has had at least `U_k-1` arrivals. |
| Greedy comparison | The chosen upper queue label is strictly smaller than the lower one. Equality is impossible for labels with different valuations. |
| Rounding | `lambda=b^d` makes `lambda^2/b` an integer. The strict inequality ending with `-1/b` therefore yields an integer bound ending with `-1`. |
| Descent | From two consecutive crossing counts bounded by `M>=1`, the next two are bounded by `F(M)<=M-1`. Positive integer counts cannot satisfy this indefinitely. |

The binary five-term block has a separate induction. Every newly reached odd
valuation is initially followed by a return to the previous even valuation.
On its second visit, its label is three times its base power, and its next
step necessarily enters the next new even valuation. The four subsequent
greedy comparisons give the exact block. This part of the note is stated
specifically for base two with unit jumps.

The finite verifier checks the full last-exit inequality on paths stopped
at their first arrival at a new binary level. The assumption that every
level has finitely many visits, which is used for the infinite contradiction,
is supplied by the mathematical proof rather than inferred from a finite run.
