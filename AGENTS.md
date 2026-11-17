# Repository instructions

## Zero-defensive-prose rule — mandatory

Apply this rule to all repository-authored English prose: README, mathematical research notes, `PROOF.md`, LaTeX exposition, documentation, pull-request descriptions, and code comments. Enforce it when auditing historical material and when writing anything new.

**Prohibited rhetorical constructions (including grammatical variants):**
- Chinese examples to recognize and eliminate in translated source material: `不是……`, `并不是……`, `不构成……`, `还没有做……`, `尚未……`, `而不是……`, `并未……`, `不意味着……`, `不代表……`, `不能据此……`, `这并不证明……`, `我们不声称……`, `不保证……`, `仅仅是……`.
- English equivalents to eliminate from authored explanations: `not a ...`, `is not ...`, `does not ...`, `do not ...`, `has not ...`, `have not ...`, `not yet ...`, `rather than ...`, `instead of ...`, `does not constitute ...`, `does not establish ...`, `does not imply ...`, `should not be interpreted as ...`, `we do not claim ...`, `no claim is made ...`, `merely ...`, `only a preliminary ...`, `beyond the scope ...`, `not intended to ...`.
- Delete disclaimers, self-exculpation, premature qualification, repetitive status caveats, and defensive contrasts. Do not relocate them to a different paragraph or replace them with synonyms serving the same rhetorical purpose. Zero such constructions are acceptable in explanatory prose.

**Required replacement style:** Lead with the actual theorem, deliverable, tested behavior, evidence, applicability conditions, exact scope, and concrete open mathematical question, using affirmative statements. Examples:
- `We prove the classification for n >= N under hypotheses H1 and H2.`
- `Verified cases: n = 2,...,7. General-case proof target: ...`
- `CI checks: 16 passed. Proof: Proposition 4. Research priority: external review.`
- `Algorithm: FPT for disjoint ordinary cardinality quotas. Next target: robust mixed-status source-SCC accessibility.`

**Mathematical truth takes precedence over stylistic cleanup.** Preserve essential logical negation in theorems, inequalities, counterexamples, constraints, source quotations, and executable code where changing it would alter correctness. In ordinary explanation, express boundaries by positive quantified scope and precise next objectives. If a claim is unsupported, correct or remove it; never invent evidence to avoid a negative sentence.

Before opening or updating a PR, review every added or modified paragraph for prohibited rhetoric and its semantic equivalents. Record the direct result and evidence; keep mathematical limitations in compact, exact statements of domain and open problems.

## Mandatory legacy research audit

- Review **every existing tracked research document**, not only the files that contain Chinese text. Audit definitions, quantifiers, hypotheses, edge cases, lemma dependencies, completeness of proofs, calculations, code-to-claim consistency, bibliographic accuracy, and all statements of novelty or scope. Resolve ambiguities and supply necessary missing definitions, arguments, examples, and references.
- Translate Chinese-language mathematics into accurate English without changing its meaning, preserving equations, labels, hypotheses, and all proof steps. If a purported proof has an actual gap, repair it rigorously if possible; otherwise identify the precise unresolved step and correctly classify the result as incomplete. Never silently upgrade evidence or invent conclusions.
- Organize corrections into focused per-repository PRs. Review the full diff for residual Chinese prose, broken mathematical links and citations, and unintended proof changes. Run existing relevant checks and provide proof-level review; automated language scans and tests alone are insufficient.
- Keep all future research files unambiguous and in English, including comments and manuscript prose. Avoid duplicative progress reports or unnecessary engineering scaffolding.

## Mandatory English-language policy

- English is the sole language for repository-authored explanatory prose. Write and maintain `README.md`, `AGENTS.md`, `PROOF.md`, research notes, Markdown documentation, manuscript exposition, source-code comments/docstrings, and pull-request descriptions in English. Use English for new or revised public-facing messages and instructions.
- Audit **all tracked Markdown files**, including nested directories and archives, for Chinese-language explanatory text. Translate existing Chinese proofs and documentation into precise, idiomatic mathematical English in dedicated PRs. Preserve definitions, hypotheses, quantifiers, equations, proof dependencies, numbering, cross-references, bibliographic details, code behavior, and the exact strength of every claim. Never silently shorten or reinterpret a proof during translation.
- Keep mathematical notation, source identifiers, and faithful quotations or official titles in their original form when required; provide an English explanation around any unavoidable original-language quotation. Do not leave mixed-language paragraphs, headings, tables, or code comments.
- Before completing a documentation PR, inspect every changed file for residual Chinese prose and broken links/references. Review mathematical equivalence against the original and run existing relevant checks. A character scan is a useful audit aid, not a replacement for reading or proof review.
- This requirement applies to all future contributions and edits, not only the present translation cleanup. Do not create new Chinese prose or alternate Chinese documentation copies. Keep English clear, direct, and technically specific; avoid defensive boilerplate and unsupported claims.

These rules apply throughout `oeis-papers`. Keep the repository a clear, navigable collection of OEIS-related mathematical manuscripts and their supporting research.

## Root README: sequence index

- Keep `README.md` an **index, not a progress report**. Start with a short repository description and list the paper groups in ascending order of their **lowest OEIS A-number**.
- Group all OEIS entries addressed by the **same manuscript** in one item and link that item to its paper directory. Do not split one paper into several unrelated index items.
- Under each group, give each sequence number a direct `https://oeis.org/Axxxxxx` link and its original OEIS **Name** (`%N`) description. Check the live entry before adding or changing a description. Prefer the exact wording; when a description must be shortened for readability, preserve the mathematical definition and do not present a paraphrase as an exact quotation.
- The index should explain **what each sequence is** and include exactly one concise **Result** line for each paper group, stating the proved mathematical contribution (for example, a conjecture resolved, an existence theorem, an exact formula, or a counterexample). Keep these statements faithful to the manuscript; do not turn the index into a progress log, computational-statistics report, or artifact inventory.
- **Use the established structure for every group:** a bold linked group title, one indented bullet per OEIS entry giving its linked sequence number and OEIS Name, followed by a single indented `- **Result:** We proved ...` bullet. Preserve this order and keep a blank line between groups.
- In the **Result** line, state what was actually proved, constructed, classified, calculated, or disproved. Prefer the precise theorem, range of validity, exceptional cases, formula, or explicit bound over a generic statement such as "studied the sequence" or "made progress." Keep it to one or two readable sentences when possible, with mathematical notation in Markdown code spans as needed.
- When one paper covers multiple sequences, summarize the shared mathematical contribution once, without repeating the result for every individual sequence. Distinguish existence from exact minima, finite arithmetic procedures from closed forms, and complete classifications from partial results; do not imply stronger conclusions than the paper establishes.
- Preserve existing `(published)` labels and add or change them only after checking the actual OEIS publication/acceptance status. Never conflate a theorem proved in the repository with a result published on OEIS.
- **README example** (retain the official descriptions; the result summarizes the manuscript):

  ```markdown
  - **[A001040 / A001053](papers/A001040-A001053/)**
    - [A001040](https://oeis.org/A001040): a(n+1) = n*a(n) + a(n-1) with a(0)=0, a(1)=1.
    - [A001053](https://oeis.org/A001053): a(n+1) = n*a(n) + a(n-1) with a(0)=1, a(1)=0.
    - **Result:** We proved Kurkov's endpoint-refined rook-tour conjectures for every positive board size: the numbers of directed Hamilton tours with endpoints in opposite and equal columns are respectively `2*n!*A001040(n)` and `2*n!*A001053(n)`.
  ```
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

## Standard LaTeX paper layout

- Use [`papers/A006063/main.tex`](papers/A006063/main.tex) as the default typesetting reference for mathematical manuscripts, including those in OEIS sequence groups. When a task requests only layout changes, preserve mathematical statements, proofs, formulas, citations, and authorship.
- The default document class is `\documentclass[9pt]{extarticle}`. Use T1 encoding, `lmodern`, `amsmath`, `amssymb`, `amsthm`, `microtype`, and `geometry` with `margin=0.78in`. Add `mathtools` and other math/table packages only when useful. Configure `hyperref` with readable blue hyperlinks.
- Follow A006063 for the normal `\title`, `\author`, `\date`, `\maketitle`, and abstract layout; show each actual author's affiliation in smaller type below their name. Do not add a separate title page, forced compacting with `\linespread` or negative `\vspace`, or ornamental title styling.
- Number main sections and subsections, and use a section-numbered shared theorem counter (`\newtheorem{theorem}{Theorem}[section]`, followed by other theorem-like environments sharing `[theorem]`). Use standard equation labels, proof environments, and compact reference formatting.
- Keep the same conventional 9pt density and page geometry as A006063, while ensuring displayed equations remain readable and no content runs past the margins. If the mathematics calls for specialized formatting, make the smallest local adaptation and document material exceptions.
- Rebuild the manuscript PDF after every source or layout change, inspect the final output for page breaks, equation overflow, labels, references, and the actual appearance, and commit the PDF to the paper directory alongside the source.

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
4. Update that paper's README and OEIS draft when their content changes. Update the root README whenever indexed groups, official sequence descriptions, verified publication status, or a paper's substantive mathematical results change; follow the fixed group/Name/Result format above.
5. Check directory cleanliness, links, authorship, manuscript/PDF consistency, and that the working changes are committed and pushed to the intended branch.
6. In the final report, identify the substantive changes, tests actually run, PDF path, branch/commit, and any genuinely unresolved mathematical issues.

## Writing style

- Use concise, factual, affirmative engineering and mathematical prose. State theorems, constructions, definitions, evidence, and real limitations directly.
- Avoid repetitive defensive statements, self-justification, filler, exaggerated novelty claims, and repeated notices that a PDF or verifier exists.
- Preserve important correctness and provenance details without surrounding every claim with disclaimers.
