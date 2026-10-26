# OEIS A006063 / A096680: cube-sum permutations

**Authors:** Qichao Wang (Hebei University of Technology); 董道豫 / Daoyu Dong (University of Electronic Science and Technology of China)
**Manuscript date:** October 19, 2026  
**Status:** six-page mathematical paper with eventual minimal-fixed-point involutions and exact finite certificates, prepared for independent review. This is a **computer-assisted finite-certificate proof**, **not** a case-free classification or a peer-reviewed publication.

## Main results

For a positive integer `n`, let `P(n)` count permutations `p` of `{1,...,n}` such that every `i+p(i)` is a perfect cube.

1. **Existence (A006063):** `P(n)>0` for every `n>=173`. Below 173, exactly the 48 sizes recorded in the paper are admissible; the other 124 sizes have explicit Hall-deficient witnesses. In OEIS notation, `A006063(j)=j+124` for `j>=49`.
2. **Multiplicity (A096680):** `P(173)=P(174)=1`, `P(175)=3`, and `P(n)>=3` for all `n>=175`. Below 173, multiple permutations occur exactly at `112,115,116,117,119,124,125,126,127,128,129,130,133`. Hence `A096680(j)=j+161` for `j>=14`.

**Eventual involutions (new theorem):** Every odd `n>=69603` has a cube-sum involution with the unique fixed point `4`; every even `n>=228028` has a fixed-point-free cube-sum involution. These bounds improve the archived research thresholds of 70001/230000. The proof uses strict odd-cube suffix reflections from the elementary seeds `p_7(i)=8-i` and `p_26(i)=27-i`, exact finite parity-interval closure (13 rounds over [69603,100001] and 12 rounds over [228028,303412]), and an integer cube-gap induction. The bounds are sufficient, **not claimed globally optimal**. The certificate requires no matching solver and is independent of the 56-shape existence atlas. This result allows the cube values to grow with `n`; it does not prove the separate finite-palette four-cube conjecture.

The infinite existence argument is purely symbolic. The finite basis still uses **56 determinant-defined root-word/order shapes (784 reflected blocks)**, **25 seed specializations from six symbolic block families**, and a separate forced-neighbor proof for **n=173**. These 82 seeds and 132 additional finite cubic-suffix reflections cover the complete interval `[173,364]`. The interval-overlap avalanche then covers every larger integer.

## Paper and supporting files

- **[main.pdf](main.pdf)** — final six-page **typeset mathematical paper** (the primary submission document).
- **[main.tex](main.tex)** — complete editable LaTeX source for the paper.
- **[certificates/finite_56_cubic_order_shapes.txt](certificates/finite_56_cubic_order_shapes.txt)** — the 56 independent algebraic seed parameter choices, with no precomputed interval endpoints.
- **[verify_56_plus_forcing.py](verify_56_plus_forcing.py)** — independent exact-integer verification of all 56 determinant instances, the 25 symbolic template seeds, forced 173, and the finite reflection closure.
- **[certificates/exact_classification_below_173.json](certificates/exact_classification_below_173.json)** — 48 explicit positive permutations and 124 explicit Hall-deficient sets.
- **[certificates/second_solutions.json](certificates/second_solutions.json)** and **[certificates/third_solutions.json](certificates/third_solutions.json)** — alternating-cycle witnesses used for multiplicity.
- **[verify_extended.py](verify_extended.py)** — full finite existence, nonexistence and multiplicity certificate checks.
- **[verify_eventual_involutions.py](verify_eventual_involutions.py)** — independent exact interval-union certificate for the two strengthened minimal-fixed-point involution tails.
- **[COMPRESSED_FINITE_PROOF.md](COMPRESSED_FINITE_PROOF.md)**, **[UNIMODULAR_BLOCK_FACTORY.md](UNIMODULAR_BLOCK_FACTORY.md)**, **[FORCED_REFLECTION_PEELING.md](FORCED_REFLECTION_PEELING.md)** and **[INTERVAL_OVERLAP_AVALANCHE.md](INTERVAL_OVERLAP_AVALANCHE.md)** — detailed supplementary arguments.
- **[research_monograph.tex](research_monograph.tex)** — archived extended mathematical research manuscript (historical, not the primary submission).
- **[RESEARCH_LOG.md](RESEARCH_LOG.md)** — historical research log, including additional experimental and structural directions.
- **[FINAL_READER_GUIDE.md](FINAL_READER_GUIDE.md)** — proof-dependency guide and independent audit summary.

## Reproduce the paper

From the `papers/A006063` directory:

```bash
python3 verify_56_plus_forcing.py
python3 verify_extended.py
python3 verify_eventual_involutions.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The main existence certificate does not rely on a general matching solver, floating-point computation, or historical endpoint-permutation atlases. The 124 negative Hall certificates and the finite multiplicity assertions have separate exact audits.

**Mathematical distinction:** the minimum of **60** new seeds under the restricted suffix-reflection-only closure (44 in `[173,255]`, 16 in `[339,364]`) is distinct from the **56** currently required algebraic shape certificates. The incorrect historical conflation with **57** was corrected.

## Scope and research status

The 199 experimentally successful **four-cube involution** instances on a higher interval are part of a distinct unfinished research program. Planarity and the near-bipartite/Hall reductions do not establish a uniform perfect matching theorem for that program, and are **not hypotheses** of the A006063 existence proof.

The extended monograph also contains independent results on counting, entropy and involutions; they are not required for the short submission and have not all undergone independent line-by-line review. Literature priority and external mathematical acceptance have not been established, and no OEIS edits are claimed in this PR.

## References

- [OEIS A006063](https://oeis.org/A006063)
- [OEIS A096680](https://oeis.org/A096680)
- [OEIS A096904](https://oeis.org/A096904)
- P. Hall, *On representatives of subsets*, Journal of the London Mathematical Society 10 (1935), 26–30.
