# Final editorial polish — 2026-11-01

AI-assisted working-draft revision of base
`772d6d008c79d5b896ba4befea6acf261ca06d93`, after PR #28 merged.
This small follow-up addresses the subsequent editorial request; it does not
certify author-owned final wording, journal readiness or human approval.

| Request | Resolution |
|---|---|
| Remove duplicate 175 residual-graph discussion | Proposition 4.3 now explicitly cites Appendix B.3 and invokes count preservation. The complete ten-vertex graph, cycle, loop/edge and three-permutation proof appear once, in B.3. |
| Consistent edge notation | The sole remaining description uses `4\sim23`; the earlier dash-form description was removed with the duplication. |
| Simplify Boolean Family V lengths | Under the unchanged binary restriction `alpha<=beta`, use `l2=7-2*alpha-4*beta`, `l4=alpha`, `l9=48-45*beta` in the appendix, generator and accompanying note. The identity `alpha*beta=alpha` justifies each simplification. |
| Order the introduction roadmap | Sections 2–4, 5–6, 7, 8, then Appendices A and B. |
| Prefer eight pages if natural | The clean build remains nine pages, with references on page 9. No smaller fonts, altered margins, forced spacing or proof omissions were introduced to hit a page count. |

Validation:
- Two successful LaTeX passes, no final warnings, undefined references or
  overfull/underfull boxes; all nine pages visually checked.
- Primary finite-certificate runner passed; fresh source/data hashes and
  outputs are in `verification-polish-20261101.json`.
- All 47 Python workflow command steps and independent certificate/peeling/
  actual-LaTeX checks passed. Compact results, PDF/source hashes and actual
  independent outputs are in `polish-validation-20261101.json`.
- The old and new generators produce identical dictionaries of all 25 seed
  witnesses. All theorem, proposition and lemma statements, author details
  and the bibliography compare unchanged to the base.
- Separate mathematical and all-page editorial reviews are retained in
  `POLISH_MATH_REVIEW.md` and `POLISH_QA.md`.
- The current supplement manifest includes the revised source, PDF, code and
  evidence. Its extracted package was checked independently of the full checkout.

Earlier first-review and self-containment reports retain their historical
hashes; they are not relabeled as evidence for this revision. No journal
submission or email was sent by this update. Remote CI is a separate check
on the eventual published commit, not implied by the local results above.
