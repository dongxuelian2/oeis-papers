# Independent review of digital round 2, 2026-10-26

Read each main.tex and verify.py in papers/A136050, papers/A237930, and papers/A334595. No source edits made in the reviewed directories.

## A136050

For every twin-prime pair with lower member p>3, p+1 is divisible by 6, so p(p+2)=36m^2-1 is 8 modulo 9. Decimal digit sum preserves that congruence. The exception (3,5) is exactly handled. No infinitude assumption is introduced. The proof resolves the stated congruence globally.

Ran verifier: 5000 official terms, 342 independently trial-tested twin pairs through 20000, and 14870 noninitial pairs through 2000000 all pass. No correctness issue found.

## A237930

The supplementary quadratic-symbol formulas correctly classify the six unit residue classes modulo 84. In those classes (3/p)=1 and (7/p)=-1, contradicting 7*3^n=1 modulo p for every n. The treatment of exceptional primes 2,3,7 and the remaining multiplicative-order incidence criterion is correct; the proof does not overstate the six classes as all excluded primes.

Ran verifier: full CRT class check, Euler criterion for all relevant primes through 200000 (4513 excluded), 134995 independently traversed cycle residues below 5000, and all 1001 official terms pass. No correctness issue found.

## A334595

The orientation of the right-boundary vector agrees with the binomial transform on least-significant input bits. The Pascal matrix squares to the identity in characteristic two by the displayed binomial identity. This yields both the unit-value classification and the unique fixed-length maximum. The all-one output fails the leading-input-bit constraint for every L>=2; changing its final coordinate gives the unique next-largest output and valid input 2^(L-1)+1. This proves every record location without relying on finite checks.

Ran verifier: all 8191 official terms, records and unit values through 65535, and every vector through length 10 for self-inversion all pass. Minor test wording issue: the block-max check uses values.index(max(values))==1 but does not explicitly assert count==1; uniqueness is proved mathematically, and adding the count assertion would align the printed finite-audit claim exactly. No mathematical correctness issue found.

This review establishes consistency of the supplied proofs and controls, not literature priority or OEIS editorial acceptance.
