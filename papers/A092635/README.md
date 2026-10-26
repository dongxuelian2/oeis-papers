# A092635: exponential coefficient formula and all3functional conjectures

[Official source](https://oeis.org/A092635), read 2026-10-26, retains
the2015 Euler-polynomial exponential proposal and2024 triple of
reciprocal/substitution identities. We prove all of them globally.

For formal `G(x)=sum a(n)x^n`, its log is obtained from the classical
Stirling expansion and equals `sum b(n)x^n/n`, where
`2/(1+exp(4z))=sum b(n)z^n/n!`. Consequently the proposed all-index
coefficient recurrence is exact. For `H(x)=xG(x)` we prove:

- `H(x)*H(-x)=-x^2`;
- `H(x)=-H(-x/(1+4x))`;
- `H(x)*H(x/(1-4x))=x^2`.

Oddness of log G proves the first; the exact gamma-ratio identity
`F(t)*F(t-1/2)=(t-1/2)/t` proves the third; the second follows.
The entire proof uses formal asymptotic series and does not assume
convergence or evaluate gamma at negative arguments.

Run `python3 verify.py`: all301published coefficients are checked
both by Euler recursion and independently by the exact gamma shift
recurrence, followed by exact formal identity checks through degree100.
[main.tex](main.tex) gives the full proofs. No OEIS update was submitted.
