# Independent appendix transcription review — 2026-11-01

## Verdict

The revised mathematical appendices faithfully incorporate all six algebraic block families and the complete critical peeling rounds. No mathematical transcription defect or loss of assumptions remains in the reviewed source. The revised PDF renders the formulas and tables legibly, with no clipped mathematical content found in the reviewed appendix pages. This is an independent review of a research-draft editorial rewrite, not certification of journal compliance or author-written provenance.

## Source comparison

Read the complete revised `main.tex` and `appendix.tex`, comparing the latter with the independently prepared mathematical specification and the source family/peeling notes. Explicitly checked:

- Families I–VI: every length expression, output order, nominal-sum expression, total-length formula and all 25 parameter instances.
- Family IV: nonnegative optional blocks; positive w and h; cube requirements only for active optional blocks; all eight instance rows, including noncubic values on omitted blocks.
- Family V: binary alpha≤beta, alpha*beta=alpha, both choices of t, all six sizes, and each optional-block cubicity argument.
- Family VI: binary beta≤alpha (the opposite inequality from V), all three sizes, and the corrected nominal vector valid even on zero-length blocks.
- Peeling: all three uniform bands and their image intervals; every subsequent batch for173; distinct round4 at174 and175; every shared round5–19; exact residual ten-vertex set, loop, edge, chordless cycle, edge-sum list, and exact count3.
- Main-text references to the appendices, preservation of the finite-certificate proof qualification, and the explicit cycle/reference-permutation dependencies retained in Section8.

One minor wording correction was requested and applied: the173 check now subtracts each endpoint **from the cubes**, rather than subtracting cubes from the endpoint. This did not change the listed mathematics.

## Independent computation performed for this review

1. New `audit/check_appendix_math.py` reads the **actual revised LaTeX** expressions for Families V and VI, parses their length/order/sum vectors, expands the prefix-sum identity independently with SymPy, and checks equality on every allowed binary parameter pair, including omitted zero blocks. It also verifies nonnegativity and cubic active sums at every allowed t. Both families pass. This focused parser is not a complete LaTeX or proof parser; Families I–IV were checked by source comparison against the previously independently expanded identities.
2. Reran the independent `audit/check_peeling_tables.py`: all stated simultaneous batches at173,174,175 pass, with residual sizes0,0,10; the three bands pass for every173–181. This script checks a separately transcribed batch list, **not automatic extraction of the appendix**; the source-to-batch correspondence was checked manually above.
3. The original `independent_audit.py` is a certificate/data checker, not a LaTeX parser. Its prior results are not presented as automatic validation of this transcription.

Reproduce the focused source check from `papers/A006063` with `python3 audit/check_appendix_math.py`. The bundled editorial logs are `audit/appendix-transcription-editorial-20261101.txt` and `audit/independent-editorial-20261101.txt`; the latter records the separate independent finite-data check, not automatic LaTeX validation.

## Rendered mathematical content

Independently rendered PDF pages5–9 with Poppler and inspected the images. The appendices occupy pages5–8: all six family formulas,25 instances, complete peeling tables, and the residual nine-cycle are visible and legible. FamilyV spans pages6–7 without loss of context. The corrected VI coefficients and the opposite V/VI parameter inequalities render correctly. No clipping, overlap, missing entries or ambiguous rendered path-minus notation was found. Page9 contains references; their bibliographic accuracy is outside this appendix review.

## Reviewed artifact fingerprints

Final artifact hashes rechecked on 2026-11-01 after trailing-whitespace and comma-spacing-only source cleanup; appendix source unchanged. The portable focused checker was rerun successfully:

- `main.tex`: `a80fda55db9821c5176ec72e237190d84d855bb20af286010f24ce1e59cf6f38`
- `appendix.tex`: `ecbb8efbd275f56189b14db2167e9ba978a6cde661b153dc69c877ea98c1d7d8`
- `main.pdf`: `99034cdfc37b1bb0c943801732c689c06a098adb58000a4eb91a950f8ae84167`

Later layout-only rebuilds may change the PDF fingerprint; mathematical edits require corresponding review. No tracked source file was edited by this reviewer.
