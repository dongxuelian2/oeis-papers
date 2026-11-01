# Editorial working revision — 2026-11-01, second review

**AI-assisted editorial working draft, not a journal-ready submission.**
This revision implements the subsequent request to improve mathematical
self-containment, remove internal project commentary and repair typesetting.
Both authors must supply/verify their own final wording, approve the mathematics
and references, and accurately disclose AI assistance under their chosen
journal's policy. Removing preparation-status commentary from the article does
not establish that those author actions have been completed.

Base: `ca1712f68e5d11350bd74bb5dbf43d3a3fbe13ba` (latest `main` after the
previous review PR was merged). Branch: `edit/a006063-self-contained-20261101`.
The intervening historical citations, author names, affiliations, theorem
statements, hypotheses and numerical bounds are retained. The canonical source
is now `main.tex` **plus `appendix.tex`**; the canonical PDF remains `main.pdf`.

## Response to each requested change

| Request | Action and verification |
|---|---|
| Remove unexplained four-cube, old-atlas and historical-array contrasts | Removed from introduction, finite-base proof and reproduction discussion. The article discusses only constructions it actually uses. |
| Remove comparison with unpublished archived involution bounds | Removed 70001/230000 comparison. Retained the mathematically material statement that 69603/228028 are sufficient rather than sharp and that permitted cubes grow with the length. |
| Remove peer-review/priority-search status from mathematical prose | Removed. Author verification, priority and provenance tasks remain in audit documentation rather than the article. |
| Consolidate repeated defensive qualifications | One neutral computer-assisted finite-certificate methodology statement remains in the introduction. Removed repeated “case-free” contrasts and unrelated Pfaffian discussion. Retained the concrete Hall obstruction at 65 as mathematics, not a disclaimer. |
| Include all six algebraic families in the paper | Appendix A gives every length vector, output order, nominal cube-sum vector, parameter restriction and all 25 seed specializations, with proofs. Zero-block rules remain explicit; the opposite inequalities for Families V and VI and corrected Family VI nominal sums are preserved. |
| Include the complete critical peeling steps | Appendix B proves the three uniform bands and lists every later round for 173, 174 and 175, including their different fourth rounds, all singleton removals, residual ten-vertex graph and exact count. No omitted steps are delegated to Markdown notes. |
| Standardize proof-environment names | Replaced “Finite certificate” and “Explicit finite verification” headings with “Proof”. The two theorem-specific headings still begin with “Proof of Theorem”, conventionally. |
| Consolidate filenames, scripts and repository links | All rendered artifact paths and reproduction commands are in Section 8. Main proofs refer to appendices, mathematical data tables or Section 8. The multiplicity cycles' exact reference-permutation mapping is stated there. Bibliographic source URLs remain in References. |
| Remove LaTeX compilation from mathematical verification commands | Section 8 gives only the aggregate Python certificate command. PDF compilation remains a repository maintenance/check step, documented outside the mathematical verification block. |
| Check position-operator and indicator typography | Both occurrences of position already used the same upright `\pp=\operatorname{pos}` macro; no italic-position source defect was found. Retained it. Replaced the formula's legacy `{\bf1}` expressions with the `\one` macro and changed its previously unused definition from `\boldsymbol1` to `\mathbf{1}`; the original indicators were already bold, so this is syntax standardization, not a claim of a newly fixed unbolded digit. |
| Replace arithmetic-minus cycle notation | Both displayed nine-cycles now use `\sim`; the appendix's edge uses the same notation. |
| Remove crowded data-row box | Replaced `\fbox` by an ordinary centered display. |
| Modernize small tables | All new appendix tables and the parity-window table use booktabs rules without vertical lines. The original three-band table is now in Appendix B. |
| Prevent the reproduction-code orphan | Used `\Needspace` before the lead-in and code block; rendered pages checked. |
| Normalize prose comma spacing | Changed “uniqueness at 173,174” to “at 173 and 174”; normalized the paired exceptional lengths. Compact comma-separated vectors/sets retain ordinary mathematical punctuation. |

## Evidence and limits

The current exact checks are recorded separately from the first audit:

- `verification-editorial-20261101.json`: the primary runner, including the
  `main.tex` and `appendix.tex` source hashes.
- `workflow-editorial-20261101.json`: all Python command steps from the current
  A006063 workflow run locally; not a statement of remote CI status.
- `independent-editorial-20261101.txt`: fresh runs of the independent
  certificate and peeling implementations.
- `APPENDIX_REVIEW.md`: separate review of the actual appended mathematical
  formulas, assumptions and printed rounds, rather than an assertion that
  existing certificate programs parse LaTeX.
- `EDITORIAL_QA.md`: separate nine-page visual and point-by-point editorial review.
- `pdf-validation-editorial-20261101.json`: source/PDF identity and final
  compilation/visual checks.

The additional focused source-transcription check is reproducible with the
optional SymPy dependency already specified for the independent audit:

```bash
python3 papers/A006063/audit/check_appendix_math.py
```

Its output is `appendix-transcription-editorial-20261101.txt`. It parses only
Families V and VI, not the whole article; the separate report describes the
manual and computational coverage precisely.

Earlier files `INDEPENDENT_REVIEW.md`, `REVIEW.md`,
`verification-20261101.json`, `workflow-local.json` and `pdf-validation.json`
are historical evidence from the first review and its frozen source version.
They are not presented as new checks of the revised article. In particular,
the original review's missing-appendix and cycle-reference presentation issues
have been addressed here. The current `SUPPLEMENT.sha256` includes the new
appendix and current evidence, and is checked against a standalone extracted
supplement. The 56 determinant rows and 124 Hall sets remain bulk finite data
in that frozen supplement; “self-contained” here refers to the algebraic and
peeling arguments now printed in the article, not to elimination of those data.

No journal submission or email has been made by this editorial revision.
