# A346644: all denominators and exact prime-power minima

Write `n=2^a*m` with odd `m`, and set `u=2^a`, `A=2^u-1`, `h=m*A`.
Choose an odd prime `p=-1 mod n` using Dirichlet's theorem. Then
`K=2^(u-1)*p^(h-1)` has `sigma(K)/tau(K)=S/n`, where
`S=1+p+...+p^(h-1)=1 mod n`. Its reduced denominator is exactly `n`.

For odd prime `q`, let `ell_i(q)` be the increasing primes not congruent to
`1 mod q`. The exact minimum at `n=q^s` is

`min over partitions s=b_1+...+b_t, b_1>=...>=b_t>=1 of`
`product ell_i(q)^(q^b_i-1)`.

For the remaining prime-power family, `a(2^s)=2^(2^s-1)`. In particular,
`a(q)=2^(q-1)` for every prime `q`. The proof removes unnecessary factors
from any competing integer, then sorts the surviving exponents.

Examples: `a(9)=36`, `a(25)=1296`, `a(81)=57600`.

Run `python3 papers/A346644/verify.py` from the repository root.
The verifier checks universal witnesses, all 39 displayed terms, and prime-power
minima against an independent divisor sieve. `oeis.txt` contains update drafts.
