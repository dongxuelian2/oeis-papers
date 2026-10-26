# Round2 screening: combinatorics, recurrences and greedy sequences

Official complete pages accessed 2026-10-26. Existing round1 ledgers
were read first to avoid re-counting their46 screened entries. We
selected three new targets and stopped selection after completing them.
No claim of exhaustive literature priority or OEIS acceptance is made.

| Entry / official source | Precise question or source-status finding | Decision |
|---|---|---|
| [A260056](https://oeis.org/A260056) | Column-k difference of order k+2 vanishes for all rows; alternating antidiagonal sums equal A004524 shifted by3. Both explicitly labeled conjectures. | **Completed both globally.** Exact polynomial column formula gives minimal difference order. Bivariate GF substitution proves every antidiagonal. |
| [A308620](https://oeis.org/A308620) | Conjectured rational GF and order10 recurrence signature for path-game state counts. | **Completed globally from established exact count.** Recurrence starts n>=12; n=11has one-unit anomaly. Both formula and starting index are proved. |
| [A092635](https://oeis.org/A092635) |2015 Euler-polynomial exponential GF proposal and2024 triple of reciprocal/substitution conjectures for formal asymptotic coefficients. | **Completed all globally.** Classical Stirling expansion identifies logGF; exact gamma shift and odd logarithm prove all3functional identities. |
| [A091524](https://oeis.org/A091524) |2024 conjecture a(n)=sqrt(A028982(n)/A006337(n)). | Excluded as effectively already encoded: A006337's2025 sorted-union type characterization and this entry's two complementary Beatty positions immediately supply the identity. No new theorem claimed. |
| [A028982](https://oeis.org/A028982) | Increasing union of squares and twice squares, needed to audit the previous conjecture. | Related-source control only; no new unresolved claim selected. |
| [A006337](https://oeis.org/A006337) |2025 comment identifies sequence as the type word of sorted N union sqrt(2)N. | Prior-result control for A091524; excludes a misleadingly fresh-looking conjecture. |
| [A248025](https://oeis.org/A248025) | Greedy digital-root/leading-digit sequence is stated as a permutation. | No unresolved question is stated; no new proof count merely for repeating the definition. |
| [A338191](https://oeis.org/A338191) | Greedy digital-root/last-digit sequence contains all positive integers not divisible by10. | Complete page supplies induction via blocks a(81k+j)=90k+a(j). Excluded as already proved. |
| [A377091](https://oeis.org/A377091) | Four conjectures for greedy integer square-difference path: surjectivity, deviation bound, limsup constant, filled intervals. | Deferred: complete page explicitly says still open (2026); local graph connectivity does not prove greedy surjectivity or asymptotic bounds. |
| [A084068](https://oeis.org/A084068) | First occurrences of levels in alternating irrational-floor partial sums equal this recurrence sequence. | Deferred: requires a complete renormalization/first-passage argument; checking convergent indices alone does not prove no earlier hit. |
| [A352849](https://oeis.org/A352849) | Least unused integer coprime to previous two terms is a permutation. | Deferred. Missing-prime-power argument succeeds, but does not prove a missing composite with several prime factors appears. No partial result counted. |
| [A253074](https://oeis.org/A253074) | Greedy nonprime adjacent sums give a permutation of nonnegative integers. | Excluded: complete page contains Devlin/Artamonov proof and Hasler's2019 simplified proof. |
| [A060014](https://oeis.org/A060014) | Sum of permutation orders eventually periodic modulo every modulus. | Excluded: complete page explicitly cites Skirrow's August31,2026 proof, not visible in older search snippet. |

## Primary-source evidence and exact scope

A308620's physical game-state interpretation is not inferred from a
40-term fit. The author-hosted primary paper
<https://www.vuuren.co.za/papers/GamesPaths.pdf> was downloaded and
read (Theorem3, Eq4.2 and its Q/R/S run-composition proof on printed
pages7–8). It proves precisely the binomial count used by OEIS's
Maple implementation. We retain its attribution and derive the
subsequent GF/recurrence conjectures independently. The n=11exception
is explicit throughout the paper, README and OEIS draft.

A092635 uses the classical logarithmic Stirling expansion from the
primary reference <https://dlmf.nist.gov/5.11.E1>. The new entry-specific
proof treats generating functions formally, and uses only positive-t
asymptotic expansions. It never infers analytic convergence or evaluates
the gamma expression at negative arguments.

A260056's conjectured recurrence follows from an all-column formula,
not a finite-order guess per sampled column. The same formula proves
that the stated finite-difference order is minimal.

## Independent audit outcomes

- A260056: all10000published flattened entries (100complete rows),
  direct trinomial rows versus polynomial columns for n<=100,k<=40,
  all corresponding differences and antidiagonals through100.
- A308620: established binomial count versus exact rational GF through
  n=1000; all40official terms; direct binary state/reflection-orbit
  enumeration through length18; exact n=11defect and recurrence n>=12.
- A092635: all301official coefficients separately reconstructed from
  Euler-polynomial recursion and exact gamma-shift coefficient recursion;
  all3functional identities through degree100 by rational operations.

All three final PDFs are two pages, compiled twice without warnings,
undefined references or over/underfull boxes, and all six pages were
rendered and visually checked. Source and PDF files are in their
respective papers/A-number directories. None was submitted or pushed.
