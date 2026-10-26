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

| # | Proof package | Completed question / result |
| --- | --- | --- |
| 1 | [A048702](A048702/) | Binary-palindrome formulas, with an all-base carry and floor-sum theorem. |
| 2 | [A079495](A079495/) | Squared-digit-sum residue density and positional asymptotics for every base. |
| 3 | [A084043](A084043/) | Exact zero classification, constructive internal-palindrome existence, finite automaton minimum. |
| 4 | [A085124](A085124/) | Complete existence classification and exact finite minimum for simultaneous number/digit-product divisibility. |
| 5 | [A195608](A195608/) | Membership criterion and all three gap/block conjectures. |
| 6 | [A214972 / A152009](A214972-A152009/) | Exact jumps, L-sieve recurrence, and deterministic triangular stabilization. |
| 7 | [A236383](A236383/) | Universal concatenated-square existence and an exact finite arithmetic minimum. |
| 8 | [A248520 / A248521](A248520-A248521/) | Both cotangent asymptotics, bounded errors, and exact term formulas. |
| 9 | [A340138](A340138/) | Greedy digital-root permutation theorem in every base. |
| 10 | [A393833](A393833/) | Universal palindromic divisor-residue witnesses and exact finite minima. |
| 11 | [A005046](A005046/) | Eventual periodicity modulo every integer, exact period modulo 10, and Bessel moment conjecture. |
| 12 | [A092635](A092635/) | Euler-polynomial exponential formula and all three formal functional identities. |
| 13 | [A136050](A136050/) | Full twin-prime-product digit-sum congruence conjecture. |
| 14 | [A237930](A237930/) | All six forbidden prime classes and an exact incidence criterion for other primes. |
| 15 | [A260056](A260056/) | Column finite-difference conjecture and alternating-antidiagonal identity. |
| 16 | [A308090](A308090/) | Complete prime classification of the factorial gcd sequence. |
| 17 | [A308620](A308620/) | Conjectured rational generating function and corrected recurrence starting index. |
| 18 | [A334595](A334595/) | Both XOR-triangle conjectures: every record and every unit value. |
| 19 | [A334958](A334958/) | All-index valuation-product formula and divisibility statement; separate infinitude questions remain open. |
| 20 | [A357127](A357127/) | Complete nonunit prime pairing; counterexample to the gcd conjecture and exact replacement. |

Each directory contains the proof source, PDF, verifier, supporting data, and proposed OEIS update. Finite tests validate implementations; the proofs establish the stated universal claims. Some exact minimum formulas retain finite minimization.

Run all verification programs and compile all papers twice:

```sh
python3 papers/verify_batch_20261026.py
python3 papers/verify_batch_20261026.py --compile-papers
```
