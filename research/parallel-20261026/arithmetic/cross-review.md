# Independent proof and implementation cross-review

Reviewed 2026-10-26 against files in this branch; no changes made to the reviewed source directories.

## A214972 / A152009

Files: `papers/A214972-A152009/main.tex`, `verify.py`.

- The survivor-map composition is correct: after removal of the first survivor and deletion at positions in A, the new index map is j -> 1+b_j, so successive lists are iterates of this increasing map.
- The nonempty/infinite-complement domain is preserved. Nonempty A makes 1+b_j >= j+2 eventually; the output orbit therefore has infinitely many missing positive integers.
- The triangular prefix argument holds for arbitrary sets in the stated domain. If the first k deletions are triangular numbers, the T_k-th retained position is at least T_k+k=T_(k+1)-1. After one transform exactly k deletions occur below T_(k+1), so the following transform fixes the next coordinate. This proves the uniform 2k-1 bound, with preservation at intervening transforms.
- Arithmetic-progression complement ranks, the d=3 recurrence, and inversion of each threshold inequality are exact.
- Ran the verifier successfully: d=2..12 and n<=100000; all 26 published terms; 275 finite/periodic deletion sets through 11 transforms; first 100 fixed-point terms.
- No correctness issue found. A redundant floating-point membership assignment was reported to the author and removed in favor of the already present exact isqrt control.

## A248520 / A248521

Files: `papers/A248520-A248521/main.tex`, `verify.py`.

- Derivative f'(x)=(2/pi)*(u/sin u)^2 decreases with x. Its value pi/4 at x=2 supplies the strict increment bound for k>=2; k=1 is treated exactly.
- The telescoping counts, positive densities, and O(1) errors hold without an equidistribution assumption.
- Inverse cotangent gives the one-step formula. The strict bounds beta*N-alpha < Z(N) < beta*N+1 imply the stated L_n and U_n, containing two or three integers and always containing the n-th zero step.
- Taylor alternating remainders and their recurrence coefficients are correct; monotonic sine/cosine endpoints give the advertised rational cotangent quotient bounds. Exact exceptional boundaries are handled. The root-of-unity argument excludes every remaining integer cotangent/inverse boundary and proves refinement termination.
- Ran the verifier successfully: 471 A248520 and 469 A248521 official rows; direct differences through k=3000; exact large-index boundaries through n=10^30+57.
- No correctness issue found. Optional exposition suggestion: name the standard Machin identity used for the rational pi enclosure explicitly.

This review checks the arguments and supplied programs; it does not establish literature priority or constitute OEIS editorial acceptance.
