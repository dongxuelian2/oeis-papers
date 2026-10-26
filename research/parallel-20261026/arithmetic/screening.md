# Arithmetic screening, 2026-10-26

All links below were opened directly on official OEIS on 2026-10-26; each inspected entry still states the indicated conjecture/question and contains no later proof or solved-status comment resolving it. This records the visible source status, not a literature-wide novelty claim.

| Entry | Official stated question (paraphrased) | Decision and obstacle/result |
|---|---|---|
| [A084043](https://oeis.org/A084043) | Palindromic multiple containing n internally exists iff 10 does not divide n | **Proved all indices**, elementary padded palindromic block; exact pair-automaton minimum |
| [A085124](https://oeis.org/A085124) | Positive digit-product multiple exists for all 7-smooth n not divisible by 10 | **Proved all indices**, zero-free p-adic suffix + block repetition; exact DFA minimum |
| [A077739](https://oeis.org/A077739) | Prefix/suffix-n multiple with digit sum n has zeros only at 11,17,19 | Deferred: fixed sum limits useful positions; construction must handle small-budget modular restrictions |
| [A077754](https://oeis.org/A077754) | Zero-free digit-sum-n multiple has zeros only at 1,2,5,11 and multiples of 10 | Deferred: zero-free and fixed total digit sum prevent block repetition |
| [A076070](https://oeis.org/A076070) | Digits of the next n integers can always be permuted to a multiple of n | Deferred: rigid multiset needs a uniform permutation argument |
| [A162657](https://oeis.org/A162657) | Every n occurs as reduced denominator of sigma(m)/m | Deferred: prime-valuation interactions in sigma prevent immediate independent construction |
| [A225562](https://oeis.org/A225562) | Every n can be the n-th largest divisor of an integer | Deferred: requires exact divisor rank, not merely many divisors |
| [A085057](https://oeis.org/A085057) | Minimum equal-size factorial product ratio is always factorial's squarefree part | Deferred: balanced subset prime-valuation conditions; numerical evidence is not a proof |
| [A110545](https://oeis.org/A110545) | Least harmonic index whose numerator or denominator is divisible by n is <=n | Deferred: simultaneous cancellation across harmonic denominators |

Results and verifiers: `papers/A084043/README.md`, `papers/A084043/verify.py`, `papers/A085124/README.md`, `papers/A085124/verify.py`.

These constructions settle the precise displayed conjectures globally and supply exact finite minimum algorithms. They do not claim elementary closed forms without finite minimization, or that checking a finite table itself solves an infinite conjecture. OEIS edits have not been submitted.
