# Independent mathematical audit: A006063 / A096680

Reviewed frozen commit `515d60e46c49c3fdd00024dd0ba9c08a5bf14feb`, `papers/A006063`.
Review date: 2026-11-01 UTC. No repository code was imported or executed for the independent checks below; no tracked files were modified.

## Conclusion

The main existence, exact membership, multiplicity, and eventual parity-minimal involution theorems have a valid proof chain, subject to preserving and publishing the specified finite ancillary data. Independently implemented exact checks passed every essential finite obligation. One ancillary nominal polynomial identity is false as written but does **not** invalidate any constructed permutation or theorem; correct it before submission. One dependency clarification is important for independently reproducing the multiplicity proof.

This is evidence of mathematical correctness of the reviewed argument, not a claim of formal verification or a substitute for journal peer review. Novelty, priority, current OEIS content, journal suitability, authorship, and submission permissions are outside this mathematical audit.

## Findings

### 1. Correct false nominal sums (moderate exposition/algebra defect; theorem unaffected)

`TEN_BLOCK_FAMILY.md:29–39`, mirrored in `verify_57_plus_templates.py:139–145`, asserts that direct expansion of the universal prefix-sum identity gives a displayed ten-entry nominal sum vector. Entries 2, 4, 5, 6, 8 are not those polynomials. The correct vector is

```
(8, 15+12*alpha, 343,
 333-24*alpha-93*beta,
 174-49*beta,
 174+42*beta,
 512, 184+24*alpha+8*beta,
 343, 512).
```

For example, at alpha=beta=0, the second nominal sum is 15, not 8. The block has zero length at that parameter, explaining why the existing active-block verifier misses the discrepancy. For every **nonempty** block at the three allowed parameter pairs, the existing claimed sums agree with the actual sums. Thus this is not a counterexample to the construction. Recommended fix: replace the vector in the note and generator, and test all nominal sums before dropping zero blocks.

All other five families' identities were reviewed and independently expanded. The four-, five-, six-, and twelve-block identities hold as literal polynomial identities. The fifteen-block vector holds modulo alpha*beta=alpha, explicitly justified by its allowed binary parameters. No analogous error was found there.

### 2. Identify the reference permutations for cycle certificates (moderate reproducibility clarification)

`main.tex:196–198` mentions second/third-solution cycle archives but does not name their reference-permutation archive. A cycle alone is not a valid witness unless its reference p is specified. The actual check uses:

- Small cycles: the positive permutations from `exact_classification_below_173.json`.
- Tail cycles 175–364: `base_permutations.json`, indexed n−173.
- Exceptions 554,555: reflections under cube729 of that archive's unique permutations at174,173.

The new determinant/template witnesses need not equal these historical permutations termwise. State these references explicitly and list the base-permutation archive in the dependency ledger. The archive's permutations and every switched alternative passed independent validation; no missing witness or numerical defect was found.

### 3. Preserve a complete, pinned ancillary package (submission prerequisite)

`main.tex:120–135,149,182,196–198,258–266` deliberately sends essential finite details outside the manuscript. That is acceptable for a finite-certificate proof only when the publication actually delivers the complete frozen supplement. The root/order table, family notes, forced-peeling notes, small Hall/positive archive, base-permutation archive, alternating-cycle archives, and relevant verifiers must be packaged at a pinned version. The main existence construction genuinely does not need legacy endpoint atlases or a matching solver; the multiplicity certificate does use its separate historical reference permutations. Do not market the whole package as archive-free.

## Independent computational evidence

`independent_audit.py` imports only standard libraries and SymPy (tested 1.14.0), and reads the frozen certificate files. It contains new implementations, not wrappers around the repository verifiers.

1. All56 matrices reconstructed directly from root words and output orders. SymPy exact `domain-ge` determinant and `DM` inverse give det=1 and784 strictly positive integral lengths. Full reconstructed permutations verified by sorted images and exact cube membership.
2. All six template families transcribed from their algebraic lengths/orders. Actual prefix sums computed afresh, including zero-length blocks; all25 resulting seed permutations valid and disjoint from56 determinant lengths.
3. Independent greedy forced-neighbor elimination gives empty residuals at173,174, hence uniqueness; at175 yields the stated ten-vertex residual. An independent bitmask permanent computes exactly3.
4. Independent strictly increasing suffix-reflection closure constructs48 admissible lengths below173 and all192 lengths173–364.
5. All48 positive records validated. All124 negative Hall sets checked against complete neighbor sets obtained by scanning every potential neighbor. Their disjoint union is exactly1–172 and positive indices agree with the closure.
6. Independent Kahn topological-sort algorithm confirms acyclicity for the35 unique small positive sizes and173,174; the other13 small sizes are exactly the displayed setE. Every archived alternating cycle independently switched and resulting permutation checked. At each190 sizes175–364 and at554,555, the two switched alternatives are distinct from each other and the base.
7. Independent pointwise shortest-path dynamic programming, **not interval-union arithmetic**, reconstructs all lengths reachable in at most13/12 strict odd-cube extensions. At seed7:2961 parity intervals and final[69603,100001]. At seed26:7047 parity intervals and final[228028,303412]. This independently confirms both table rows, including the odd interval count not asserted by the supplied verifier.
8. `check_peeling_tables.py` independently checks the actual stated simultaneous batches (not only a new peeling order): all batches173/174/175 and the three uniform bands for every173–181 are valid. Empty residuals at173/174 and exact ten-vertex set at175 reproduced.

Logs: `independent_audit.log`, `check_peeling_tables.log`, `check_symbolic.log`. The symbolic log is diagnostic: it records the nominal defect and permissible fifteen-block reductions, not an assertion-failure test.

## Manual proof-chain review

- Suffix reflection is a genuine permutation on the invariant suffix and preserves the old seed assignments. Strict m<n is used consistently.
- Interval avalanche uses a+b+2≤c≤2b+2 correctly, covering every new integer n and guaranteeing a≤m≤b and m<n.
- Initial729 step and subsequent cube-gap polynomial f(k)=k³−3k²−3k−347 have the stated values/differences, so the finite interval implies an unbounded tail.
- Reflected block rearrangement's input/output intervals and the matrix formula are correct. Det=1 is sufficient; no unstated general unimodularity theorem is needed. Deleting zero-length blocks is legitimate.
- Forced-neighbor elimination follows from both unique row and unique column availability, including loops. It preserves the exact permutation count, not merely involution counts.
- Hall-negative certificates prove nonexistence of general permutations. Symmetry does not silently turn the problem into undirected perfect matching.
- Alternating-cycle necessity uses p^{-1} composed with q correctly under the stated function convention; sufficiency preserves the image multiset. Acyclicity therefore proves uniqueness.
- Multiplicity propagation treats365–553 and exceptional554/555 separately, then uses n≥556 and c∈[n+176,2n] so175≤m<n. Polynomial lower bound and its forward difference are correct.
- Involution parity coordinate and strict interval-extension bounds are correct. Odd reflection cubes preserve parity, involutivity and the original fixed-point set. The two finite parity windows were independently checked. Past the caps, minimum odd roots57/83 follow from the stated thresholds; F_M initial values8351/35039 and forward difference6k²−36k+8 are correct. Strong induction closes both tails.
- The claimed OEIS indexing offsets follow arithmetically from48 small positive sizes and13 small multiple sizes, assuming the described sequence definitions and ordinary indexing.

## Editorial advice and limits

The additional involution result is mathematically sound and logically independent of the main exact classification. Moving it to an appendix might improve focus, but is not a mathematical necessity. The thresholds are only sufficient; neither this review nor the paper proves global sharpness. No uniform four-cube involution conjecture or broad experimental material in the research monograph was used to establish the main results. The review covers the full current `main.tex` proof and its essential ancillary identities/certificates, not every exploratory file in the directory.
