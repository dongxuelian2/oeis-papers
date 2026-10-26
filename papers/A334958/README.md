# A334958: Exact alternating harmonic denominator formula

Official source: <https://oeis.org/A334958>, opened 2026-10-26. The relevant conjecture remains explicitly labelled in the inspected entry; no resolving later comment was found. This is not an exhaustive literature-priority claim.

**Completed result.** For H_n=sum(k=1..n,(-1)^(k+1)/k)=u/v in lowest terms, a(n)=n!/v. Hence a(n)=n!*product(p<=n,p^min(0,v_p(H_n))), proving the displayed valuation-product conjecture. Also n!/lcm(1,...,n) divides a(n).

**Scope and corrections.** The separate claims about infinitely many equalities and infinitely many ratio identities remain open here. This result completes the stated valuation-product problem, not every attached question.

The full elementary proof is in `main.tex` and `main.pdf`. `verify.py` uses only the Python standard library and independently compares the original definition with the proved formulas. `b334958.txt` contains 100 exact consecutive values. `oeis.txt` is a proposed update; it has not been submitted.

Run `python papers/A334958/verify.py` from the repository root. Large integer sizes and trial-division factorization can require substantial resources; no polynomial runtime in the bit length of the index is asserted. The proof establishes global scope independently of finite verification.

Final PDF: 2 page(s), compiled twice without warnings; every page rendered and visually checked.
