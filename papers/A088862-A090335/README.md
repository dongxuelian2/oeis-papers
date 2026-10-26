# A088862 and A090335: prefix-free divisor representations

For any base and any prescribed list of positive prime exponents, infinitely
many integers with that signature have prefix-free representations of every
divisor greater than one. This proves both recorded existence conjectures.

If the exponents sum to `r`, choose distinct primes in
`(b^(k-1/r), b^(k-1/(r+1)))`. Divisors with `i` prime factors have exactly
`ik` digits, and leading values from longer layers lie below every member
of shorter layers. Dusart's Proposition 6.8 supplies enough primes for
`k >= r^2+32`, giving a witness below `b^(r^3+32r)`.

- `main.tex`, `main.pdf`: statement, full proof, explicit bound and references.
- `verify.py`: integer interval construction, direct divisor/string checks,
  published data checks and exhaustive initial minima.
- `oeis.txt`: proposed comments and an indexing correction for editorial review.

Run `python3 papers/A088862-A090335/verify.py` from the repository root.

Both entries currently publish offset `1,2`, although their first listed value
`1` has zero prime factors and their examples use the factor count as the index.
The proof uses factor counts directly and covers zero as well as every positive
count. The proposed offset correction is documented separately from the theorem.
