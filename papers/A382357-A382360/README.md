# A382357 permutation theorem and A382360 pairing formula

The greedy sequence of distinct positive integers whose adjacent 2-adic
valuations differ by one visits every positive integer. This proves the
permutation conjecture recorded in A382357.

The general theorem covers any integer base `b>=2`, any fixed valuation jump
`d>=1`, and every finite legal seed. The completed sequence lists exactly
the integers whose valuations lie in the seed's residue class modulo `d`.

The proof uses visits and edge crossings of the valuation levels. If every
level were visited finitely often, the walk would eventually escape upward.
Its last departures would force, in the binary case,

`4*U_k <= U_(k-2)+U_(k-1)+1`,

where every `U_k` is a positive integer. The maximum of two consecutive
counts strictly decreases after each pair of steps, a contradiction. An
infinite visit class propagates to all its neighbors and exhausts their queues.

For `t_j=A382360(j)`, the paper also proves `t_(2m+1)=t_(2m)+1` for every
`m>=0`. For `m>=1`, putting `x=4^m` and `t=t_(2m)` gives the exact block

`(a(t-1),a(t),a(t+1),a(t+2),a(t+3)) = (3*x/2,x,2*x,3*x,5*x/2)`.

Files:

- `main.tex`, `main.pdf`: complete mathematical proof and general theorem.
- `verify.py`: independent direct and queue generators, inverse positions,
  local blocks, finite last-exit audits and exact integer contraction controls.
- `published.json`: the displayed terms and inverse positions used for checks,
  with source URLs and the inspection date.
- `PROOF_AUDIT.md`: last-exit indexing, finite-seed treatment and the integer descent.
- `oeis.txt`: proposed comments and formulas with a fixed-commit PDF link.
- `verification.txt`: completed validation and PDF hash.

Run `python3 papers/A382357-A382360/verify.py` from the repository root.
