# Digital and palindrome screening, 2026-10-26

Official OEIS entries were read directly on 2026-10-26. A search hit
alone was not treated as an unresolved problem. Dates below refer to
the relevant statement in the official entry, not a guessed discovery
date. The entries overlap in subject but each row is a distinct new
sequence outside the repository's already completed list.

| Official source | Precise question / status in entry | Assessment and outcome |
|---|---|---|
| [A048702](https://oeis.org/A048702) | Two conjectured formulas for binary even-length palindromes divided by three; two Maple formulas explicitly marked unproved. Entry by Antti Karttunen, 1999-03-07. | **Completed** all four for every index by a carry calculation and valuation-class count; general-base extension proved. Files in `papers/A048702/`. |
| [A393833](https://oeis.org/A393833) | Least K with exactly 2n+2 divisors and palindromic sorted proper-divisor residues modulo n; existence for every n is conjectured. Michel Lagneau, 2026-03-01. | **Completed** existence with K=2p^n, p=1 mod n. Elementary cyclotomic prime construction and finite bound give an exact finite arithmetic minimum formula. Files in `papers/A393833/`. |
| [A236383](https://oeis.org/A236383) | Least square root k for a square formed by concatenating equal-length x and x+n^2; existence conjectured. Michel Lagneau, 2014-01-24; definition corrected 2019-06-24. | **Completed** global existence using an odd d in one residue class mod22 and k=n+5(10^d+1)/11. Both digit inequalities proved; explicit length bound and prime-power/CRT finite minimum formula give exact all-index values. Files in `papers/A236383/`. |
| [A077739](https://oeis.org/A077739) | Least multiple of n starting/ending in n and with digit sum n; conjectured zeros exactly 11,17,19. Amarnath Murthy, 2002-11-20. | A digit-sum/remainder automaton gives an evaluator after a length bound, but the exact zero classification needs a global construction and handling overlaps. Deferred, unresolved. |
| [A077754](https://oeis.org/A077754) | Least multiple of n with >=2 nonzero digits and digit sum n; conjectured zeros 1,2,5,11 and multiples of 10. Amarnath Murthy, 2002-11-20; edited 2006-06-14. | Finite composition search is immediate, because digit count <=n. This alone does not prove the proposed all-index zero classification; deferred. |
| [A084017](https://oeis.org/A084017) | n-digit palindromic multiple of n with digit sum divisible by n; special leading-zero convention when 10 divides n. Conjectures no zero. Amarnath Murthy and Meenakshi Srikanth, 2003-05-23. | Simultaneous length, symmetry, divisibility and sum restrictions defeat the simple repeated-block construction. Deferred. Search and open returned different cached term corrections, reinforcing need for pinned source evidence before computing. |
| [A046385](https://oeis.org/A046385) | Least palindrome with n palindromic prime factors and no other factors; conjectured finite list complete. Hugo Pfoertner's statement, 2019-08-13. | Restricted-prime palindromic smooth-number finiteness problem; finite searches provide no global exclusion. Deferred as difficult. |
| [A395284](https://oeis.org/A395284) | Least semiprime with exactly n concatenation-of-prime-factor semiprime iterates; conjectured existence for every n. Philip Jameson, 2026-04-18. | Reverse chains impose primality/semiprimality constraints not addressed by a digit automaton. Deferred as difficult. |
| [A338968](https://oeis.org/A338968) | Largest prime formed from a 1-,2-,...,n-digit prime; conjectured existence and a prescribed maximal prefix. Bernard Schott, 2020-12-21. | Requires prime occurrence in sharply restricted digit sets; heuristic prime density is not a proof. Deferred as difficult. |
| [A344422](https://oeis.org/A344422) | Divisor-record palindromes conjectured even after 1 (2021-06-22), and divisible by 3 after 44 (2026-02-05). | Global divisor-record exclusion across all palindrome lengths; no proof from local digit properties. Deferred. |
| [A067523](https://oeis.org/A067523) | Least prime for each allowable digit sum, conjectured existence. Entry now links Lehmann, arXiv:2606.04677, on an explicit surjectivity threshold. | **Literature check required**, so not counted as a new unresolved claim. No claim of a new solution; the linked 2026 work may already settle the substantive question. |

## Completed-result checks

A048702: the independent palindrome definition, exact rational weighted
sum, floor sum, recurrence and second Maple expression agree for every
n=1..20000; the general theorem was checked in bases 2..12. All 1001
published b-file terms agree, and a direct scan below 2^18 verifies the
enumeration independently. None of these checks replaces the proof.

A393833: an independent divisor sieve through K=200000 gives seven
attained minima, all reproduced by the factor-pattern evaluator. All
13 values stated in the entry and comments are reproduced, and a
12-term consecutive table fills the missing index 10 with
51874849202. The witness construction is checked for n=1..100.

## Unfinished proof attempt: A077739

Writing n as a fixed prefix and suffix suggests a finite automaton on
remainder and digit-sum budget. With non-overlapping copies, the middle
budget is n-2*s_10(n); at n=11,17,19 it is negative. This does not alone
prove the three exceptions, because the definition permits overlapping
prefix and suffix copies. For large n a positive budget still needs a
uniform congruence construction with exactly that budget, so finite
search output must not be promoted to an all-index existence theorem.

## A236383: initially deferred route, then completed

For B=10^d and M=B+1, a candidate satisfies k^2-n^2=M*x with
B/10<=x and x+n^2<B. The obvious roots k=±n modulo M force x
near zero or B and do not solve the inequalities. Splitting M into
coprime factors and mixing signs by CRT can produce interior roots;
the completed proof uses the fixed factor 11. Choosing odd d with
5d+2n=0 mod11 gives C=(10^d+1)/11=d mod11 and the interior
root k=n+5C. The digit bounds follow once 10^d>4(n+1)^2, which
is possible with d at most D+21. This works even when 11 divides
n; no unproved factor-distribution claim is needed. The exact
root-list verifier reproduces all 245 official terms and all 659
minima from an independent scan k<=1000000.
