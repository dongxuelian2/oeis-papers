# Independent audit of the full-prefix square enumeration

## Verdict and scope

No mathematical or implementation defect was found in the stable theorem and verifier. The at-most-eight-candidate characterization is complete for each cut k>=10 in the exact region R_(m,k)<H_k^2, with m>k. The advertised explicit subregion D(m)<=2D(k)-2digits(k) is valid. All cut-1000 certificate branches and counts were independently reproduced. Valuation, local-obstruction, and coverage counts were independently checked through cut 10000.

This is a characterization plus finite computation, not an infinite nonexistence theorem. The independent cut-10000 check described here is not a second complete root-enumeration run. The author completed the cut-10000 enumeration; its final counts and source hashes are recorded below, separately from the independent checks.

Audited implementation: `verify_late_prefix_candidates.py`.
SHA-256: `854f26ca8f401d482898bafcf73ce066db8e5c14f9ee423f7d285546309dbdbb`.

## Mathematical checks

### 1. Exact local compression and complete branch sets

If y^2 equals U modulo p^s with v_p(U)<s, then 2v_p(y)=v_p(U). Otherwise the valuation of y^2-U is smaller than s. Odd valuations therefore exclude all square rotations at the cut.

For v_p(U)=2a, division gives the unit congruence (y/p^a)^2=U/p^(2a) modulo p^(s-2a). Each unit-root class yields exactly one compressed y class modulo p^(s-a). Conversely, any such class really satisfies the original square congruence. The 2- and 5-primary compressed moduli are coprime, so CRT gives precisely their Cartesian product, modulo H=10^s/(2^a 5^b).

For 2^n, n>=3, the four roots are r, -r, r+2^(n-1), and -r+2^(n-1); these are distinct for an odd root. Small n=1,2 are separately enumerated. For 5^n, the two roots are r and -r. Therefore the total is at most eight, with no missing multiplicity from the original modulus 10^s.

### 2. Root-lifting arithmetic

The 2-adic step is correct despite the noninvertible derivative 2r. If r^2=U modulo 2^e and r is odd, set delta=((U-r^2)/2)r^(-1) modulo 2^t, where t=min(n,2e-2). Then 2r delta equals U-r^2 modulo 2^t and v_2(delta)>=e-1, so delta^2=0 modulo 2^t. Hence (r+delta)^2=U modulo 2^t. The starting precision e=3 advances strictly. This process only needs one valid final root because its four-element orbit gives all roots. It need not retain every previous representative modulo 2^e.

The 5-adic step uses the invertible derivative 2r and improves precision from e to min(n,2e). The seeds 1 and 2 represent the two possible square classes modulo 5; their negatives complete each pair. All divisions, modular inverses, and exponent changes in the code match these arguments.

### 3. Digit-length recovery and exact comparisons

A rotation after a whole-integer cut begins with k+1, so it has exactly D(m) digits. There is no leading-zero loss. D is strictly increasing. The width formula and its inverse correctly handle the end of a width, the first endpoint of the next width, and lengths not in the image of D. The explicit m>k test excludes cuts at or beyond a recovered endpoint.

If R_(m,k)=y^2<H^2, the positive root lies in [0,H) and must equal one of the least representatives. Thus every possible square is checked. Conversely, every successful exact equality is an actual square rotation and automatically lies below H^2. No root search, approximate logarithm, or rounding assumption enters this argument.

### 4. Guaranteed coverage and bounds

The inherited full-prefix valuation lemma was inspected. Its small-width exceptional cases and its estimates for the first seven terms or the later part of each width establish v_p(U)=v_p(J)<s, where J=k(10^w-1)+10^w. The smooth part divides J, and J<10^(2w). Consequently H^2>10^(2s-2w). A rotation with D(m)<=2s-2w is strictly below that quantity and hence is covered.

The reported coverage count is the exact number of pairs in this sufficient digit-count region. It is not asserted to count every endpoint in the larger exact region R<H^2. Locally obstructed cuts actually exclude all later endpoints, but only their guaranteed finite region is included in the count.

The same-width thresholds 53, 519, and 5139 were checked against the displayed formula. The general q>=0 extension is also correct: rotations strictly increase with m, so a common bound at endpoint M is valid. Its potentially enormous number of representatives is honestly disclosed.

## Independent computational tests

The tests in `verify_late_prefix_independent.py` use complete residue-square tables, literal decimal strings, direct integer square roots, and an independently accumulated digit-count list. They do not use the target's arithmetic-geometric prefix formula for comparison values. The checker imports the audited modular-root routines rather than implementing a second large-precision root constructor. Their output is independently checked for local solvability, exact class count, distinctness, range, and every square congruence; the mathematical argument above establishes that these checks prove completeness. Endpoint recovery and comparison values are independently implemented.

- 94,507 exhaustive unit-congruence cases: all unit residues modulo 2^n for n<=14 and modulo 5^n for n<=7.
- 300 high-precision known-square tests, including exponents up to 40001, with both reduced and unreduced inputs.
- 10,304 exhaustive decimal congruence cases through modulus 10^4. Both the compressed representatives and their expansions to all roots modulo 10^s were checked.
- 2,101 prefix identities checked against literal decimal concatenation.
- 88,895 digit lengths checked for both exact inversion and largest endpoint below a digit bound.
- Every branch disposition in the cut-1000 certificate checked against direct string-spliced rotations.
- All 3,554 pairs in the small cut-10-through-99 guaranteed region independently tested with integer square roots.

Independently reproduced cut-1000 counts:

- 406,544 guaranteed pairs.
- 26,623 guaranteed pairs at 65 locally surviving cuts.
- 520 root branches; 329 digit-gap rejections; 191 exact comparisons; no endpoint-at-or-before-cut rejections; no squares.
- 35 locally surviving cuts whose guaranteed region crosses a decimal-width boundary.

The publication-named independent program was rerun successfully and completed in about 5.7 seconds. Its only change from the original checker was the output filename. Results are in `late-prefix-independent-audit-results.json`; the reproducible log is `late-prefix-independent-audit-log.txt`.

## Independent cut-10000 local and coverage audit

The separate `verify_late_prefix_coverage_10000.py` completed all 9,991 direct valuation-identity and smooth-bound checks for cuts 10 through 10000. It also independently classified local solvability and counted the guaranteed endpoint regions:

- 42,672,235 guaranteed pairs in total.
- 2,932,566 guaranteed pairs at 688 locally surviving cuts.
- 4,442 odd-valuation cuts; 4,861 unit-obstructed cuts.
- 5,504 branches predicted from local solvability.
- 369 locally surviving cuts whose guaranteed region crosses a width boundary.

The publication-named coverage checker was also rerun successfully; its only change was the output filename. Results are in `late-prefix-independent-coverage-10000-results.json`. They verify the coverage and local filters, not the final cut-10000 digit-gap and equality-test dispositions.

## Required qualifications when reporting

Keep the strict exact-region condition R<H^2 and the m>k endpoint condition. Describe D(m)<=2D(k)-2digits(k) as a guaranteed sufficient region, not as its exact boundary. Treat any observed zero-square count as finite. Do not describe this result as a solution to the infinite square-rotation or perfect-power conjecture, as a proof for odd powers, or as a literature-priority claim.

## Added exact endpoint observation

The author's added rule using e=digits(H^2-1) and M0=max{m:D(m)<=e} is correct. If D(M0)<e, every eligible endpoint is below H^2. If D(M0)=e, only M0 requires comparison: after one decrement the digit count is smaller than e, hence the rotation is at most 10^(e-1)-1<=H^2-1. The M0<=k guard correctly detects an empty domain. This does not change the root-enumeration algorithm.

For every cut 10 through 1000 with even valuations (549 cuts), the rule was checked against literal-string rotations at the final included and first excluded endpoints. All passed. See `late-prefix-independent-exact-endpoint-results.json`.


## Final author run, independently checked metadata, and pinned files

The final author-generated `late-prefix-10000-certificate.json` reports 5,504 root branches, 3,830 digit-gap rejections, 1,674 exact comparisons, no endpoint-at-or-before-cut rejections, and no square survivors. Its run time was 669.601 seconds. All local-obstruction and guaranteed-coverage summary fields agree with the independent cut-10000 checker. The certificate has 688 cut records with eight branches apiece; recounting its recorded branch dispositions gives exactly the reported 3,830 and 1,674 totals. These consistency checks do not independently repeat those 1,674 integer comparisons.

The scope distinction is intentional:

- Through cut 1000: full certificate reconstruction and independent literal-string comparison checks, with the audited root routines validated as described above.
- Through cut 10000: independent valuation identities, smooth-part bounds, local solvability, and guaranteed-coverage counts; final certificate structure/count consistency. The complete cut-10000 root enumeration and integer comparisons were performed by the author, not duplicated by this audit.

After the author confirmed that the numerical paragraph and verifier were final, the following file hashes were read and matched against that confirmation:

- `LATE_PREFIX_POINTWISE_ENUMERATION.md`: `13a4383958cd6d93034dcbee1ec7f5e0291ef3550d30f434891133e004c61ab8`.
- `verify_late_prefix_candidates.py`: `854f26ca8f401d482898bafcf73ce066db8e5c14f9ee423f7d285546309dbdbb`.
- `late-prefix-10000-certificate.json`: `c9450c52142130e8b42b1e46c0fa1615f22841e30e492386669d13d23989c929`.

The proof uses the same-directory repository dependencies `UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md` and `EXACT_MAIN_TERM_OBSTACLE.md`. These filenames, the finalized numerical paragraph, and the exact-region endpoint paragraph were reviewed. All artifact references in this audit are relative filenames.

Reproduce the independent checks from the directory containing the artifacts:

    python verify_late_prefix_independent.py > late-prefix-independent-audit-log.txt
    python verify_late_prefix_coverage_10000.py > late-prefix-independent-coverage-10000-log.txt

The cut-1000 certificate and `verify_late_prefix_candidates.py` must be present for the first command. The coverage checker is standalone. No external upload or network access was used.
