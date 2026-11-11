# Pre-submission technical review — 2026-11-01 (first review)

> Historical review: for the later self-containment/typesetting revision and
> current source/PDF checks, see [EDITORIAL_RESPONSE.md](EDITORIAL_RESPONSE.md).
> The original test and PDF reports cited below retain their earlier hashes.

**Decision:** the core A006063/A096680 proof chain and all essential finite
obligations passed this AI-assisted review and independent implementations.
The contribution is promising for **JIS**, conditionally; **this is not a
journal-ready manuscript or a human referee endorsement**. Both authors must
write/verify the final wording, check the mathematical package and references,
and supply an accurate AI-use disclosure. No journal submission has been made;
human author approval is outstanding.

## Version and changes

The frozen review base is
[`515d60e46c49c3fdd00024dd0ba9c08a5bf14feb`](https://github.com/dongxuelian2/oeis-papers/tree/515d60e46c49c3fdd00024dd0ba9c08a5bf14feb/papers/A006063).
Use the commit containing this review, not a moving branch, to reproduce the
revised package. `verification-20261101.json` fingerprints the executed source
and data. `SUPPLEMENT.sha256` identifies the core reading/reproduction package.
To verify or bundle it, from `papers/A006063`:

```bash
sha256sum -c audit/SUPPLEMENT.sha256
# Optional local archive (the manifest itself is added separately):
sed 's/^[0-9a-f]*  //' audit/SUPPLEMENT.sha256 > /tmp/cube-sum-files.txt
tar -czf /tmp/cube-sum-supplement.tar.gz -T /tmp/cube-sum-files.txt audit/SUPPLEMENT.sha256
```

The manifest is deliberately non-self-referential; preserve it with the files
and the final Git commit ID. It includes the current paper/PDF, core ancillary
notes, primary/independent audit data and code, and audit evidence, not the
historical research monograph. Re-running all 47 historical workflow commands
requires the full repository, rather than just this focused supplement.

Changes are technical, not a replacement article written on the authors' behalf:

- Correct five **nominal** entries in the ten-block family's sum vector. The old
  formulas were false at omitted zero-length blocks but correct on every live
  block. All existing witnesses and theorem statements are unchanged. The
  generator now verifies all ten nominal sums before deleting zero blocks.
- Check the manuscript's odd parity interval count (2961), not just coverage;
  reject duplicate or noninteger small-classification records explicitly.
- Add a standard-library runner, failure/mutation regression tests, SHA256
  evidence and a primary CI step; preserve the older research checks.
- Identify the multiplicity reference archive in the manuscript's ledger,
  remove obsolete PR #13 status, and correct singular “author” to plural.
  Rebuild the canonical PDF from that source. No author names, affiliations,
  theorem statements or claimed bounds are changed.
- Mark the old extended-manuscript reader guide as historical; distinguish
  its 57-shape compression from the current 56 shapes plus forced seed 173.

## Proof dependency map

| Obligation | Exact data / code | What establishes the claim |
|---|---|---|
| Reflected blocks | `main.tex` Sections 2–3 | Invariant suffix and rearranged blocks are bijections; matrix equation and Cramer's rule are symbolic |
| 56 algebraic seeds | `certificates/finite_56_cubic_order_shapes.txt`; `verify_56_plus_forcing.py` | 56 exact determinants equal 1; 784 positive integer lengths, correct totals and full permutations |
| 25 template seeds | `verify_57_plus_templates.py: parametric_rows`; four family notes below | Six formulas with permitted parameters; zero blocks deleted from both orders |
| Forced critical sizes | `FORCED_REFLECTION_PEELING.md`; `verify_forced_peeling.py` | Unique row/column deletions; empty residual at 173,174; exact ten-vertex residual permanent 3 at 175 |
| Entire finite interval | `verify_56_plus_forcing.py` | 82 seeds, increasing strict reflection closure; all 192 integers 173–364, plus 48 small positives |
| Infinite existence tail | `main.tex` Section 2; `INTERVAL_OVERLAP_AVALANCHE.md` | Initial cube 729, then an increasing cube-gap polynomial; not extrapolation from finite tests |
| Small classification | `certificates/exact_classification_below_173.json`; `verify_extended.py` | All 48 positive permutations and all 124 Hall deficits; exhaustive partition of 1–172 |
| Multiplicity | reference permutations and cycle files listed below | Directed alternating cycles produce distinct permutations; acyclicity proves uniqueness; symbolic reflection propagates the lower bound |
| Optional involution theorem | `verify_eventual_involutions.py`; `main.tex` Section 7 | Exact finite parity windows from seeds 7/26, then a separate symbolic odd-cube-gap induction |

The six families are specified in `PARAMETRIC_BLOCK_TEMPLATES.md`,
`BINARY_BLOCK_FAMILY.md`, `FIFTEEN_BLOCK_FAMILY.md`, and `TEN_BLOCK_FAMILY.md`.

### Reference permutations are part of the multiplicity certificate

A cycle alone is not a witness without its reference permutation. The two
cycle archives `second_solutions.json` and `third_solutions.json` use:

1. Small indices: positive records of `exact_classification_below_173.json`.
2. Tail indices 175–364: `base_permutations.json`, with zero-based index `n-173`.
3. Exceptions 554 and 555: cube-729 suffix extensions of the archived
   permutations at 174 and 173, respectively.

These references need not equal the determinant/template witnesses termwise.
The main existence checker is independent of historical endpoint/permutation
atlases; **the full multiplicity package is not archive-free**. The extended
checker also cross-checks `core_109.json` and `core_60_with_empty.json`; these are
redundant existence checks, not extra mathematical assumptions of the reduced
56-shape proof.

## Reproduction and actual evidence

From the repository root, with assertions enabled:

```bash
python3 papers/A006063/reproduce.py --report verification.json
# Optional separately implemented audit (SymPy 1.14.0 used here):
# python3 -m pip install -r papers/A006063/audit/requirements-independent.txt
python3 papers/A006063/audit/independent_audit.py
python3 papers/A006063/audit/check_peeling_tables.py
```

The primary runner uses only Python's standard library, tested here with
Python 3.12.14. It rejects optimized mode (`-O` / `PYTHONOPTIMIZE`) because the
underlying scripts use assertions. The seven regression tests include corrupted
permutations, shape sizes, Hall sets, duplicate records and cycles, plus direct
set enumeration against interval-union closure. A positive test alone is not
sufficient evidence that malformed input is rejected.

Results:

- Primary runner: all five stages passed, including seven regression tests;
  full output and source/data hashes in `verification-20261101.json`.
- Separate exact implementation: all 56/784 determinant/block checks, six
  templates, forced critical sizes, 48/124 Hall partition, finite reflection
  closure, all small uniqueness/multiplicity checks and all 192 tail/exception
  pairs of distinct alternatives passed. Pointwise shortest-path enumeration
  independently reproduces 2961/7047 parity intervals and both threshold windows.
  See `independent-checks.txt` and `INDEPENDENT_REVIEW.md`.
- All **47 Python command steps** in the updated A006063 workflow passed locally,
  including the historical research checks. `workflow-local.json` records each
  command, output, exit code and elapsed time. This is not a GitHub CI result;
  remote checks must be inspected on the published commit.
- Infinite claims were checked by reading the stated symbolic arguments;
  numerical guards to 100000 are implementation smoke tests, not universal proofs.

The six-page PDF was rebuilt twice with pdfLaTeX, with no final undefined
references, compilation warnings, overfull or underfull boxes; all six rendered
pages were visually inspected. `pdf-validation.json` records source/PDF hashes.
The installed TeX tree lacked its generated format and font map: these were
created only in ignored `build/` using the installed TeX/font files, not by
changing the manuscript or system packages.

`INDEPENDENT_REVIEW.md` records the frozen-base review and its then-open findings;
the technical corrections above resolve the nominal-vector issue and identify
the archive in the ledger. The full cycle-reference wording remains an author
action. `independent-checks.txt` is a fresh run of the portable checkers against
this revision's unchanged certificate data, not merely a copied old pass log.

The independent implementation imports **no repository verifier**; its optional
SymPy dependency is not part of the primary runner or required CI. Both reviews
are AI-assisted, not independent human peer review. Historical research files
were executed where included in CI but were not all reviewed line by line.

## Novelty, scope and journal choice

The sharp existence threshold 173 with all finite exceptions, and the complete
multiplicity-support classification with `P(n)>=3` from 175, are the main
contribution. Hall's criterion, alternating-cycle exchange and the permanent
model are background, not new general theorems. The count sequence is
[OEIS A096904](https://oeis.org/A096904); the authors should explicitly attribute
`P(n)` to it rather than leave that bibliography item uncited.

The live [A006063 entry](https://oeis.org/A006063), checked 2026-11-01, is approved
and credits Wang and Dong's eventual-membership proof on October 22, 2026.
It also documents Israel's earlier testing and Chandler's multiplicity correction.
This is OEIS incorporation, **not journal acceptance**. The full OEIS history
endpoint could not be retrieved. The live [A096680 entry](https://oeis.org/A096680)
defines the multiple-permutation sizes but did not cite the new classification.
No OEIS change is made in this revision.

Targeted exact-sequence/cube-sum literature searches found no competing proof of
this exact classification. This is not an exhaustive priority clearance.
Original Gardner pages and a final MathSciNet/zbMATH search remain for the authors.
Do not introduce precise historical claims from sources not actually inspected.
Hall's reference was confirmed against
[publisher metadata](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s1-10.37.26).

The parity-minimal involution result is valid and independent of the main
classification. Its thresholds 69603/228028 are sufficient, not optimal. Keep it
as a secondary theorem or move the detailed computation to an appendix if
needed for focus; this is an editorial choice, not a correction to the proof.
It does not prove the separate fixed-four-cube-palette research conjecture.

## Author actions before any submission

Current official sources, inspected directly on 2026-11-01:
[JIS instructions](https://cs.uwaterloo.ca/journals/JIS/) and
[INTEGERS instructions](https://math.colgate.edu/~integers/submit.html).
Recheck them immediately before a future submission; older INTEGERS search
snippets stated a broader AI ban that is not the current live policy.

1. **Both Qichao Wang and Daoyu Dong** must personally verify every theorem,
   finite certificate, program result, citation, authorship detail and final
   supplement. This review does not claim either has approved the revision.
2. Both journals require author-owned wording. JIS forbids LLM writing,
   rewriting or translation of manuscript text; it permits checked reference
   suggestions and proof help with detailed attribution. INTEGERS permits
   supportive AI but requires the narrative and wording to be the authors'.
   Approval of AI-generated prose alone does not turn it into author-written prose.
3. Write the final English narrative and specific disclosure themselves.
   Establish actual historical AI provenance (proof suggestions, searches,
   code/certificates, verification and draft wording). The present generic
   “computational assistance” paragraph does not disclose these categories.
   This revision's new audit reports, new tooling and technical fixes are
   AI-assisted. Unknown earlier provenance must not be guessed.
4. State the cycle-reference mapping above in their own manuscript wording;
   supply a frozen complete supplement and verify its source/PDF identity.
5. **JIS preparation:** 12pt, meaningful submission filename, clean source/logs,
   required accompanying files and real colleague proofreading. Its submission
   instructions ask for LaTeX rather than a PDF. The repository's mandatory
   `main.tex`/`main.pdf` pair is retained for review; it is not a JIS submission
   bundle. **INTEGERS:** initial PDF, MSC codes, keywords and compliance statement;
   journal template/source requirements apply as specified by that journal.
6. Confirm no simultaneous journal submission and obtain separate explicit
   authorization to send anything. This PR is technical preparation only.

No new manuscript narrative is provided as a shortcut around these requirements.
