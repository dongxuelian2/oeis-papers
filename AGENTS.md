# Repository instructions

These rules apply throughout `oeis-papers`. Keep the repository a clear, navigable collection of OEIS-related mathematical manuscripts and their supporting research.

## Root README: sequence index

- Keep `README.md` an **index, not a progress report**. Start with a short repository description and list the paper groups in ascending order of their **lowest OEIS A-number**.
- Group all OEIS entries addressed by the **same manuscript** in one item and link that item to its paper directory. Do not split one paper into several unrelated index items.
- Under each group, give each sequence number a direct `https://oeis.org/Axxxxxx` link and its original OEIS **Name** (`%N`) description. Check the live entry before adding or changing a description. Prefer the exact wording; when a description must be shortened for readability, preserve the mathematical definition and do not present a paraphrase as an exact quotation.
- The index should explain **what each sequence is** and include one concise **Result** line for each paper group, stating the proved mathematical contribution (for example, a conjecture resolved, an existence theorem, an exact formula, or a counterexample). Keep these statements faithful to the manuscript; do not turn the index into a progress log, computational-statistics report, or artifact inventory.
- Do not add boilerplate such as “Includes PDF, LaTeX and independent checks,” “complete manuscript,” or “reproducible verification.” These belong in individual paper directories if relevant.
- Do not introduce collective author sections, such as “Authors of manuscripts not yet submitted to OEIS,” or mix author-credit and submission-status discussions into the index. Each manuscript maintains its own authorship.
- Check numbering, links, group membership, and ordering whenever papers are added, moved, renamed, or combined. Do not omit existing indexed papers as a side effect of unrelated changes.

## Manuscripts and PDFs — mandatory

- **Every complete mathematical manuscript must include a committed, directly viewable PDF in its own paper directory.** The canonical paths are `papers/<paper-group>/main.tex` and `papers/<paper-group>/main.pdf` whenever the manuscript is LaTeX-based.
- **A manuscript change is not complete until its PDF has been rebuilt and committed to GitHub alongside the changed source.** This applies to theorem statements, proofs, authorship, bibliography, and layout changes. Do not finish with only a locally generated PDF, CI artifact, screenshot, or external download link.
- For an existing manuscript with a different established filename, preserve the established source/PDF pair unless consolidating the directory deliberately; the requirement is an actual tracked PDF corresponding to the current source.
- Compile the PDF from its checked-in sources, preferably twice to resolve cross-references. Require successful compilation and check the resulting PDF for nonempty content, complete pages, correct equations, author names, citations, and readable layout. Fix substantive reference/layout errors before committing.
- Ensure the PDF is not excluded by `.gitignore`. Verify that the GitHub branch/commit actually contains it and that relative links open the submitted PDF. When supplying an OEIS draft link, use a verified stable URL, ideally pinned to the commit containing that exact PDF.
- Keep generated auxiliary files (`.aux`, `.log`, `.fls`, `.synctex.gz`, temporary renderings, etc.) out of version control. Keep the canonical PDF.
- A working research note without a complete paper may remain explicitly marked `WIP` in its own directory. Do not call it a finished manuscript or add it as a finished paper without the PDF.

## Paper directory organization

- Use one directory under `papers/` per manuscript or tightly connected sequence group, named for its OEIS numbers (for example, `A006063/` or `A382357-A382360/`). Related sequences solved in one paper share source files and a single canonical manuscript.
- A complete paper directory normally contains `main.tex`, **`main.pdf`**, a focused `README.md` describing its main mathematical results, and any needed verification scripts, data tables, certificates, and OEIS submission drafts.
- Keep substantial proof details in the manuscript or a clearly named companion note. Keep the directory README useful as a short guide to the mathematics and file layout, not a chronological log of tool runs.
- Put test scripts, finite certificates, data, and auxiliary analyses in clearly named paths. Retain only files that are used, referenced, reproducible, or needed for the proof. Put historical explorations and superseded drafts in a labeled archive instead of mixing them with the current manuscript.
- Avoid multiple indistinguishable “final” PDFs, duplicated versions of a single paper, and temporary build outputs. Fix stale internal links when reorganizing files.
- Keep root-level material limited to the repository index, shared instructions, shared configuration, and genuinely cross-paper documentation. Put sequence-specific material in its paper directory.

## Manuscript length and readability

- **Make each paper as short and easy to read as the mathematics permits.** Prioritize a clear mathematical argument over page count, but remove unnecessary repetition, generic background, verbose commentary, administrative notes, and long verification narratives.
- Present the problem and principal results early. State notation and hypotheses close to their first use; explain the main proof idea before lengthy technical details where that improves comprehension.
- Organize the main text around a small number of meaningful lemmas and theorems, with a logical progression and short, direct proofs. Prefer a simple constructive argument or unified lemma over repetitive case-by-case exposition when both are rigorous.
- Include enough reasoning for a mathematician to verify each essential inference. **Never shorten a paper by omitting necessary hypotheses, nontrivial proof steps, edge cases, or the precise role of computer-assisted certificates.**
- Put extensive enumerations, large tables, raw logs, exploratory attempts, implementation details, and independent audits in supplementary files, linking to them from the manuscript only when necessary for the logical proof.
- Use standard mathematical notation consistently. Keep formulas, displays, examples, and tables where they actually clarify the argument; avoid redundant definitions and restating the same theorem in several places.
- Keep the introduction and abstract concise and substantive. Give a direct conclusion rather than repeating a discussion of scope, limitations, or the contents of the repository.
- Check the compiled PDF as a reader would: legible equations, reasonable spacing, minimal cross-reference friction, and no unnecessary sections. Readability and correctness take precedence over an arbitrary page limit.

## Mathematical claims and verification

- Separate proved results, computer-assisted conclusions, finite experiments, conjectures, and work in progress. State precisely which claims use finite certificates or external results.
- Verify claims at the appropriate level: check symbolic deductions, boundary conditions, index offsets, base cases, certificates, and representative numeric terms. A successful finite test does not by itself prove a universal statement.
- Preserve known attribution and manuscript coauthors. Credit earlier OEIS comments, published results, and prior proofs when a result overlaps them. Do not mark an OEIS edit as accepted or a paper as published without verification.
- Where numerical data or a `b`-file is supplied, keep it consistent with the theorem and the sequence indexing. Maintain a documented command for regenerating computational artifacts.
- Prefer exact integer/rational verification when practicable, and record meaningful test commands and results close to the relevant manuscript. Avoid inflating the root README with test counts.

## Updating and finishing a task

When adding or changing a paper:

1. Read the existing directory and current OEIS entries; identify whether the sequences already belong to an existing paper group.
2. Update the mathematical source, companion notes, code, and test data that actually need changes.
3. Run the relevant checks; **rebuild, inspect, and commit the current PDF** if the manuscript is complete or its source changed.
4. Update that paper's README and OEIS draft when their content changes; update the root README only when the indexed groups or official sequence descriptions change.
5. Check directory cleanliness, links, authorship, manuscript/PDF consistency, and that the working changes are committed and pushed to the intended branch.
6. In the final report, identify the substantive changes, tests actually run, PDF path, branch/commit, and any genuinely unresolved mathematical issues.

## Writing style

- Use concise, factual, affirmative engineering and mathematical prose. State theorems, constructions, definitions, evidence, and real limitations directly.
- Avoid repetitive defensive statements, self-justification, filler, exaggerated novelty claims, and repeated notices that a PDF or verifier exists.
- Preserve important correctness and provenance details without surrounding every claim with disclaimers.
