# A079495: all-base squared-digit-sum density and slope

Official source: <https://oeis.org/A079495>, accessed 2026-10-26.
The complete entry still conjectures density `1/b` and positional slope
`b` for squared digit sums modulo the base, including composite bases.
The related ordinary-digit-sum entry A079498 already has a proof;
we distinguish the two questions explicitly.

**Result:** for every fixed integer base `b>=2` and every residue `r`,
the count of `0<=n<N` with squared digit sum congruent to `r mod b`
equals `N/b+o(N)`. Consequently its jth position divided by j tends
to b. In particular A079495 has density 1/3 and slope 3.

The proof in [main.tex](main.tex) uses complete digit blocks and finite
Fourier inversion. Every nontrivial character contracts strictly
because its digit-0 and digit-1 phases differ. An arbitrary initial
interval splits into at most b-1 blocks of each size, giving an explicit
error bound that is o(N). This step proves natural density, beyond
just density along powers of the base.

[verify.py](verify.py) implements exact integer digit-convolution
counts and every-index sequence selection. It independently checks
all prefix counts through N=5000 in bases 2..16 by direct digit
extraction, all 63 official displayed terms, and exact ternary block
counts through length 100. Run `python3 verify.py`.

[oeis.txt](oeis.txt) is a proposed update, not an OEIS submission.
This resolves the density and slope question actually stated in the
entry; no claim of literature priority or an elementary nth-term
closed form is made.
