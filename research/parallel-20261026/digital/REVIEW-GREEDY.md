# Independent review of A195608 and A079495, 2026-10-26

Reviewed the complete current `main.tex` and `verify.py` of both
papers, and independently reopened both official OEIS entries.
No mathematical or implementation blocker was found.

## A195608

The original equality and one-based evil-number convention agree
with the entry. The formula E(n)=2(n-1)+t(n-1) follows because each
binary pair contains precisely one evil integer. Pair sums of the
Thue-Morse bits give the stated two summatory formulas. Independently
checked both defect calculations: odd defect -2t(k), even defects
-4k,-2,0,4k-1. Only the claimed bit configurations yield equality.

Every three consecutive bits contain an aligned opposite-bit pair,
so zero runs have length at most two and consecutive zero positions
are separated by at most three. Translating zero runs through the
membership criterion proves the block/gap assertions. The block-start
calculation correctly requires m>1 and correctly identifies the OEIS
wording's undefined E(0) boundary. The verifier tests the original
summatory equality without using the explicit E(n) formula, compares
the saved 10000-term b-file, and uses a second substitution model.
Ran it successfully through one million indices.

## A079495

The official conjecture indeed concerns each residue and every base,
including composite bases. The strict triangle-inequality argument
uses digits 0 and 1 and therefore excludes every nontrivial character
without a primality assumption. Character orthogonality gives the
complete-block count; prefix blocks merely shift residues. The
digit decomposition has at most b-1 blocks at each scale, yielding
the claimed geometric discrepancy bound. Each of its three cases
is o(N), including rho=0. The inversion from counts to positions
correctly incorporates the zero initial term.

The integer convolution, prefix digit count, and binary selection
code follow the formulas exactly. The ternary eigenvalues are
±i/sqrt(3), giving the stated exact even/odd length formulas,
including k=0. The direct-digit verifier passed bases 2..16,
all prefix counts to 5000, all 63 published terms, and block
formula lengths through 100. This establishes implementation checks;
the asymptotic all-base claim rests on the complete proof above.

## A340138 (additional final review)

Reopened the official entry and confirmed the prose/program discrepancy:
the prose uses a(n-1), while the Mathematica program uses the last term
and supplies the initial pair 0,10. The manuscript explicitly follows
the program and all published data; its qualification is accurate.

The recurrence-of-a-root argument is complete: a permanently missing
M containing recurrent root r would force infinitely many distinct
choices <=M. The words r 0^L d, with r+d=s mod(b-1), give infinitely
many members of that forced class with every target digital root s,
including base 2 where the sole positive root is 1. Consequently every
positive root recurs and every positive integer is forced. Zero appears
exactly once initially. No finite computation is used as surjectivity
evidence. Pointer-based greedy implementation preserves leastness
because previously skipped candidates are permanently ineligible or
used. The separate repeated-digit-sum implementation and all 10000
official terms passed when independently rerun. No blocker found.
