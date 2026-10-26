# A086558: all-index existence and minimum formulas

Every positive index `n` has an `n`-digit integer beginning with `n` and
having the prime signature of `n`. The proof replaces the largest prime
factor of `n` by a prime in a carefully bounded interval. Dusart's explicit
prime-interval theorem covers `n>=17`; fifteen deterministic small prime
certificates finish the proof.

The exact all-index formula enumerates finite ordered tuples of the first
`t-1` prime factors and the distinct orderings of the exponent multiset. For
each tuple, an integer root and one `nextprime` operation supply the smallest
possible last prime. Taking the finite minimum gives the true sequence value.
Theorem 2 gives explicit bounds and proves minimality.

At every prime-power index `n=p^e`, the formula simplifies to
`nextprime(ceil((n*10^(n-d))^(1/e))-1)^e`, with exact integer roots and
`nextprime(x)` meaning the least prime strictly greater than `x`.

Run `python3 papers/A086558/verify.py` from the repository root.
Finite certificates are in `finite_witnesses.json`; `oeis.txt` contains update
drafts. The general formula is finite prime-parameter minimization and can
have large enumeration ranges.
