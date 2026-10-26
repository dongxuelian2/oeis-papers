# A048702: all four unproved formulas

The [official entry](https://oeis.org/A048702), accessed 2026-10-26,
marks two formulas as conjectures and two Maple formulas as unproved.
All four are proved for every index in `main.tex`.

For any base `b >= 2`, let `P_b(n)` concatenate the digits of `n` and
their reversal, and let `A_b(n) = P_b(n)/(b+1)`. With
`L = floor(log_b(n))` and `v_b(i) = max{t: b^t divides i}`,

```
A_b(n) = b^L * sum(i=1..n, b^(-v_b(i)))
       = n*b^L - (b-1)*sum(j=1..L, b^(L-j)*floor(n/b^j)).
```

A carry calculation proves both identities and the recurrence, including
the block boundaries `n=b^L`. Counting valuation classes within a binary
block proves the remaining Maple expression. There is no finite
minimization or unresolved index in these formulas. A048702 is `b=2`.

Run `python3 papers/A048702/verify.py` from the repository root.
The verifier compares direct palindrome construction, exact rational
weighted sums, floor sums and recurrence for bases 2..12 and n=1..20000,
the second Maple formula in base 2, the 1001 official published b-file
terms, and an independent scan of all integers below `2^18`.

`b048702-published.txt` is the unchanged official b-file downloaded on
2026-10-26 from https://oeis.org/A048702/b048702.txt; it is evidence,
not a newly contributed table. `oeis.txt` is an update draft, not a
submission to OEIS.

The final `main.pdf` is 2 pages; both LaTeX passes completed without
Warnings, Overfull or Underfull boxes. Every rendered page was visually
inspected after the final build.
