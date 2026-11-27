# Square-index exclusion through \(10^{902}\)

**Theorem.** For \(0\le n\le10^{902}\), \(L_n+P_n\) is a square
exactly when \(n=3\), and \(L_3+P_3=9\).

**Proof.** The [four-anchor theorem](anchor-forcing.md) gives
\(n\equiv r\pmod{720720}\) with \(r\in\{3,-3,-2,-1\}\).
The [norm descent](norm-descent.md) excludes \(r=-2\) at every
nonnegative index.

Use the [composite-period propagation](period-and-gap.md) on the
three odd classes. Start from \(D=720720\) for \(r=3,-3\) and
from the [3230-digit divisor](extension.md) for \(r=-1\).
The test set consists of the 78,495 primes \(5<q<10^6\).
For each recurrence matrix modulo \(q\), the eigenvalues have
order dividing \(q-1\) in the split case. In the inert case
each eigenvalue \(\lambda\) satisfies \(\lambda^{q+1}=-1\)
because Frobenius swaps the two roots and the determinant is
\(-1\). Thus \(2(q+1)\) is a period in this case. Trial removal
of prime factors, with modular matrix exponentiation, gives
the matrix orders, and their least common multiple is a period
for \(a_n\bmod q\).

In each round, retain every relation with residual period
\(2\le h_q/\gcd(h_q,D)\le2000\), including residual periods
represented by a single prime. Each eliminated residue is excluded
by Euler's criterion or by projection to a prime-power component
of a certified relation. The verifier obtains these divisor lengths.

| Anchor | Starting digits | After round 1 | After round 2 | After round 3 |
|---:|---:|---:|---:|---:|
| \(3\) | 6 | 455 | 897 | 903 |
| \(-3\) | 6 | 451 | 901 | 904 |
| \(-1\) | 3230 | 3760 | 3777 | 3777 |

For each odd anchor the verifier checks \(D+r-1\ge10^{902}\).
It also gives \(v_2(D)=14\) on every odd anchor, so every
nonzero square-index offset from its anchor is divisible by \(2^{14}\).
Consequently the only possible nonnegative index in range is
\(n=r=3\). Direct evaluation gives \(L_3+P_3=4+5=9\). \(\square\)

Run `python verify_extended_lifting.py` to reproduce the exact
integer calculations and the [valuation exclusion](shifted-dyadic-descent.md#exclusion-of-every-offset-valuation-from-14-through-200)
through depth 200. The remaining global problem is to exclude square
indices above this range with \(v_2(n-r)\ge201\).
