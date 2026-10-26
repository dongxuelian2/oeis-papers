# A334595: Both XOR-triangle conjectures

The [official entry](https://oeis.org/A334595), accessed 2026-10-26,
conjectures record positions 1 and 2^m+1, and a(n)=1 exactly at powers
of two. Both statements hold at every index. The boundary is a
self-inverse Pascal transform modulo two. On L-bit inputs its
unique maximum is 2^L-2 at n=2^(L-1)+1 (L>=2); the inverse image
of output one is exactly the single leading bit. The paper gives
a finite binomial formula and characterizes each fixed-length image.
The linked MathOverflow thread's earlier binomial observation is
acknowledged; no priority for that standard transform is claimed.

`main.tex` gives the full proof; final `main.pdf` has 2 page(s).
Run `python3 papers/A334595/verify.py` from the repository root.
`VERIFICATION.txt` records the exact checks actually run. The unchanged
`b334595-published.txt` was downloaded from the official OEIS b-file
on 2026-10-26 for independent comparison. `oeis.txt` is an update draft,
not a submission to OEIS. Both LaTeX passes had no Warning, Overfull or
Underfull lines, and all final rendered pages were visually inspected.
