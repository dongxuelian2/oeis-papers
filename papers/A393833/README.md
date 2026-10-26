# A393833: every index exists, with exact finite minima

The [official entry](https://oeis.org/A393833), accessed 2026-10-26,
asks for the least integer with `2n+2` positive divisors whose sorted
`2n+1` proper-divisor residues modulo `n` form a palindrome. It
conjectures existence for every positive `n`.

This conjecture is proved. Choose any odd prime `p = 1 (mod n)` and
put `K=2*p^n`. Its proper divisors are `1,2,p,2p,...,p^n`, whose
residues alternate `1,2,...,1`. No prime-distribution theorem is
needed: for `n>=2`, every prime factor of `Phi_n(2n)` has order `n`
and is an odd prime congruent to one modulo `n`. Use `p=3` for `n=1`.

The least such odd prime `p_n` gives an explicit bound `B_n=2*p_n^n`.
All minima are determined by a finite arithmetic formula: enumerate
ordered multiplicative partitions `prod(f_i)=2n+2`, increasing prime
tuples, products `prod(q_i^(f_i-1)) <= B_n`, and retain precisely those
whose sorted proper-divisor residues are palindromic. Take the minimum.
This expression retains finite minimization; no elementary closed
expression for all minima is asserted. The new proof establishes a
finite bound and excludes zero at every index.

`verify.py` implements a complete factor-pattern search, with proved
prime bounds from the minimum possible remaining exponent sum and the
necessary congruence `K / smallest_prime = 1 (mod n)`. Published terms
initialize some upper bounds only after their factorizations are
independently checked as valid witnesses; all smaller candidates are
still excluded by enumeration.

Run `python3 papers/A393833/verify.py` from the repository root. It
compares the search with an independent divisor sieve through 200000,
checks all 13 minima stated in the official entry and its comments,
checks the witness construction at n=1..100, and regenerates/checks the
table `b393833.txt` for n=1..12. In particular it determines the absent
index `a(10)=51874849202=2*11^10`. The table is not an OEIS submission.

`main.tex` contains the full proof and the precise finite formula;
`oeis.txt` is an update draft, not a submission to OEIS.

The final `main.pdf` is 2 pages; both LaTeX passes completed without
Warnings, Overfull or Underfull boxes. Every rendered page was visually
inspected after the final build.
