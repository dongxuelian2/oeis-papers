# A115038, A115039 and A115041: an elementary correction

The three entries repeat one existence conjecture: every prime `p` can be
written `y^k-x^2`. For odd `p`, use `x=(p-1)/2`, `y=(p+1)/2`, `k=2`.
For `p=2`, use `5^2+2=3^3`. This is an elementary difference-of-squares
identity; the three entries encode one question.

For every odd prime, the square solution is unique. Every improvement to
the least `x` therefore comes from an odd prime exponent. Theorem 2 gives a
finite exact minimum formula over explicit root intervals, and the note gives
finite formulas for the maximal exponent and corresponding base.

Run `python3 papers/A115038-A115041/verify.py` from the repository root.
The verifier compares the formula with independent direct scans at the first
200 primes, and checks all three sequences against their first 20 published terms.
`oeis.txt` contains proposed comments.
