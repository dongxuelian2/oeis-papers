# A195608: complete binary membership and structural conjectures

For one-based evil numbers `E(n)=A001969(n)`, this entry enumerates all
`n>=1` with `4*sum(E(1)..E(n))=E(n)*E(n+1)`.

Let `t(k)=popcount(k) mod 2`. We prove for **every** index:

- `2k+1` belongs exactly when `t(k)=0`;
- `2k` belongs exactly when `t(k-1)=t(k)=0` (`k>=1`).

This resolves all three structural questions in the [official entry](https://oeis.org/A195608):
the gaps are exactly 1, 4, 6; the maximal consecutive blocks have length
1 or 3; every block start `m>1` satisfies `E(m+1)-E(m-1)=5`.
The initial block `{1}` needs a boundary qualification: `E(0)` is undefined
under the official one-based indexing, so the third conjecture cannot
literally include that block.

[main.tex](main.tex) contains the complete proof; [oeis.txt](oeis.txt)
is an update draft, not a submitted or accepted OEIS change.

Run `python3 verify.py` for an independent direct summatory-identity
audit through one million indices, binary-substitution validation,
all 10,000 terms of the saved published b-file, and all complete blocks
and block starts in the audited interval. The external b-file is kept
at `b195608-published.txt` with
its source and retrieval date recorded in the screening ledger.

This is an all-index characterization and proof of the entry's stated
conjectures, not an elementary expression for its nth term without
binary parity or sorted enumeration.
