# Twenty completed OEIS problems, 2026-10-26

This batch contains **20 independent completed problem directions across
22 OEIS entries**. Paired encodings count once. Several conjectures within
one direction also count once. The results range from short elementary
identities to constructive existence and exact finite minima.

“Completed” refers to the precise question in the table. It does not mean
that every unrelated observation attached to an entry is proved. In
particular, A334958's separate infinitude questions and A357127's record-prime
observation remain open here. A357127 includes a negative resolution and a
proved correction, not a proof of the false conjecture.

The user requested waiting until twenty completions before considering a PR.
This package is prepared locally; no batch PR or OEIS update has been submitted.

| # | Proof package | Completed question / result |
| --- | --- | --- |
| 1 | [A048702](../../papers/A048702/) | Binary-palindrome formulas, with an all-base carry and floor-sum theorem. |
| 2 | [A079495](../../papers/A079495/) | Squared-digit-sum residue density and positional asymptotics for every base. |
| 3 | [A084043](../../papers/A084043/) | Exact zero classification, constructive internal-palindrome existence, finite automaton minimum. |
| 4 | [A085124](../../papers/A085124/) | Complete existence classification and exact finite minimum for simultaneous number/digit-product divisibility. |
| 5 | [A195608](../../papers/A195608/) | Membership criterion and all three gap/block conjectures. |
| 6 | [A214972 / A152009](../../papers/A214972-A152009/) | Exact jumps, L-sieve recurrence, and deterministic triangular stabilization. |
| 7 | [A236383](../../papers/A236383/) | Universal concatenated-square existence and an exact finite arithmetic minimum. |
| 8 | [A248520 / A248521](../../papers/A248520-A248521/) | Both cotangent asymptotics, bounded errors, and exact term formulas. |
| 9 | [A340138](../../papers/A340138/) | Greedy digital-root permutation theorem in every base. |
| 10 | [A393833](../../papers/A393833/) | Universal palindromic divisor-residue witnesses and exact finite minima. |
| 11 | [A005046](../../papers/A005046/) | Eventual periodicity modulo every integer, exact period modulo 10, and Bessel moment conjecture. |
| 12 | [A092635](../../papers/A092635/) | Euler-polynomial exponential formula and all three formal functional identities. |
| 13 | [A136050](../../papers/A136050/) | Full twin-prime-product digit-sum congruence conjecture. |
| 14 | [A237930](../../papers/A237930/) | All six forbidden prime classes and an exact incidence criterion for other primes. |
| 15 | [A260056](../../papers/A260056/) | Column finite-difference conjecture and alternating-antidiagonal identity. |
| 16 | [A308090](../../papers/A308090/) | Complete prime classification of the factorial gcd sequence. |
| 17 | [A308620](../../papers/A308620/) | Conjectured rational generating function and corrected recurrence starting index. |
| 18 | [A334595](../../papers/A334595/) | Both XOR-triangle conjectures: every record and every unit value. |
| 19 | [A334958](../../papers/A334958/) | All-index valuation-product formula and divisibility statement; separate infinitude questions remain open. |
| 20 | [A357127](../../papers/A357127/) | Complete nonunit prime pairing; counterexample to the gcd conjecture and exact replacement. |

Every directory contains a complete proof, PDF, standard-library verifier,
source attribution, and a proposed OEIS update clearly marked unsubmitted.
Independent cross-reviews are recorded in the directional research folders.
Finite tests validate implementations; the proofs establish universal claims.
Some exact minima retain finite minimization and may be expensive. They are
not described as elementary closed forms without minimization.

Run the entire package from the repository root:

```sh
python3 research/parallel-20261026/verify_batch.py
python3 research/parallel-20261026/verify_batch.py --compile-papers
```

The second command compiles every paper twice in temporary directories and
rejects all LaTeX warnings and overflow. Recorded results are in
[VERIFICATION.txt](VERIFICATION.txt) and [LATEX-VERIFICATION.txt](LATEX-VERIFICATION.txt).
The workflow is prepared for future CI; local passes are not remote CI passes.

## Selection and next batch

The two rounds inspected **87 distinct official entries**, including supporting
comparison entries; the first round accounted for 46. Second-round full-entry
ledgers and rejected candidates are recorded in the arithmetic, digital,
greedy, and analytic `*-round2` folders. Later official proofs, existing
counterexamples, and closely equivalent known results were excluded from the
completion count. This is a focused source check, not a literature-wide
originality claim.

The next batch can start with these uncounted candidates, each requiring a
fresh full-source and literature check before a new-completion claim:

| Candidate | Proposed next attack |
| --- | --- |
| [A295462](https://oeis.org/A295462) | Legendre valuations and binary carry constraints for the conjectured parity classification. |
| [A374446](https://oeis.org/A374446) | Functional-equation recurrence plus a sign invariant to characterize every zero coefficient. |
| [A000436](https://oeis.org/A000436) | Modular finite differential structure, with the stronger period-divides-phi condition still to prove. |
| [A048896](https://oeis.org/A048896) | Lucas parity sums and exact factorial-sum numerator identities; audit the newest claim too. |
| [A110034](https://oeis.org/A110034) | Fibonacci partial-sum identity and correction of the displayed recurrence coefficient. |
| [A025527](https://oeis.org/A025527) | Totient quotient from equal prime support; simple candidate, inspect for an existing proof before counting. |

These are a queue, not six further solved problems. No existing proof or
screened-out entry is relabeled as a new result to increase the total.
