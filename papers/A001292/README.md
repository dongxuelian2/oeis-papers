# A001292: cyclic concatenations and perfect powers

Kashihara's integer perfect-power conjecture remains open. The [15-page manuscript](main.pdf) and [LaTeX source](main.tex) prove the following local equivalences and global exclusions.

## Uniform 18-cut equivalence over Q_3

For every endpoint m >= 10007, some whole-block rotation of 1||2||...||m is a prime-exponent power over Q_3 if and only if one of these 18 cuts is:

0, 1, 2, 3, 4, 5, 8, 9, 11, 15, 19, 22, 30, 100, 106, 109, 1000, 10006.

The theorem has no restriction on the decimal digit length. Its proof uses exact normalized-prefix residues and a lifting lemma valid for every valuation, rather than extrapolating a finite numerical search.

For digit length d with h = v_3(d) >= 2, Theorem 12 gives a complete finite polynomial test using

G = m(m+1)/2 + (d/4)[135 - 21(m^3-m)] modulo 3^(h+5).

For fixed h, the classification depends only on m modulo 3^(h+5) and (d/3^h) modulo 27. It is an equivalence, not just a sufficient test.

The explicit complete local exclusion counts are:

- h = 1: 131 classes modulo 243.
- h = 2: 133 classes modulo 243.
- h = 3: 3673 classes modulo 6561.
- h = 4: 3674 classes modulo 6561.

Every locally excluded block is excluded from integer perfect powers. A locally soluble rotation is not an integer counterexample. The 18-cut theorem does not reduce the global integer conjecture to these 18 cuts.

## Retained global results

- A uniform density-zero bound O(N (log log N)^2 / log N) for powerful values among the first N sequence entries, in every fixed integer base.
- General boundary-prime valuation and character obstructions, with exact finite certificates.
- A lower density greater than 0.95599527150 among digit lengths d whose complete boundary m = 10^d - 1 has no perfect-power rotation.
- Arbitrarily high coverage of whole rotation blocks along suitable progressions of digit lengths. This is not a proof for every digit length.

## Reproducible verification

The consolidated new audit is:

    python verify_recovered_uniform.py

It checks the exact 18-prefix certificate, 24 valuation signatures through n = 10000 with every z and unit c modulo 81, 1,619,892 literal-prefix cut comparisons, 18 complete h=4 residue sets, and 944,784 independent matrix rotation comparisons at eight digit lengths. These finite checks support the infinite arguments in the manuscript; they do not replace them.

The existing verifier commands remain available:

    python verify_a001292.py
    python verify_structure.py
    python verify_local_primes.py
    python verify_boundary_valuations.py
    python verify_general_boundary_primes.py
    python verify_digit_intervals.py
    python verify_boundary_characters.py
    python verify_powerful_sieve.py
    python verify_three_adic_intervals.py
    python verify_three_adic_sufficient_extension.py
    python verify_density_refinement.py
    python verify_h2_local_equivalence.py
    python verify_h2_reverse_independent.py
    python verify_h3_local_equivalence.py
    python verify_h3_residues_independent.py

[Fresh consolidated output](verification-recovered-uniform.txt) and [verification notes](VERIFICATION.txt) distinguish the current reruns from earlier audits. [Publication metadata](publication.json) records the source and PDF hashes.

## Supplement: additional prime families and a precise limitation

[Whole-block prime obstructions and surviving local powers](PRIME_FAMILIES.md) supplies full proofs and reproducible certificates for:

- Complete uniform-valuation-one classifications at 7, 11 and 13.
- New 31/41 families reaching even digit lengths and odd endpoints, including blocks whose rotations are all squares over Q_3 but are all integer nonpowers.
- Exact conditional-CRT intersections and coverage fractions, with shared parity and residue conditions accounted for.
- Infinite families where the same unrotated member is simultaneously a square, or a seventeenth power, at all eight listed local fields. These are local survivors, not integer counterexamples, and demonstrate why that finite collection of primes cannot finish the conjecture.

The supplement is separate from the unchanged 15-page manuscript. Its proof scope, commands, fresh outputs and recovery/portability provenance are documented within it. Kashihara's integer conjecture remains open.

## General limitation for every fixed finite prime set

[The finite-prime limitation theorem](FINITE_PRIME_LIMIT.md) proves that, for any fixed finite set of primes, a positive-lower-density set of endpoint indices has the same unrotated concatenation locally square at every chosen prime. This is not an integer-square construction. It shows why necessary local square tests at a fixed finite set, even at arbitrary precision, cannot exclude every candidate.

For the eight primes in the supplement, every odd digit length not divisible by 5 has exactly 27000 such endpoint classes modulo 152672520. The full proof handles overlapping prime periods correctly and gives an explicit positive lower-density bound. A new independent verifier and exact output accompany the proof.

## Growing-prime sieve: stronger sparsity for fixed exponents

[The growing-prime sieve theorem](GROWING_PRIME_SIEVE.md) uses about d/log d primes of size O(d) in each d-digit block. For each fixed prime exponent ell, it bounds the number of ell-th-power rotation pairs through endpoint X by X² exp(−c log X/log log X), for every c < (log ell)/2. The corresponding sequence-index bound is N exp(−c' log N/log log N), for c' < (log ell)/4.

This escapes the restriction to a fixed finite prime set and improves the earlier powerful-value bound for squares or any fixed finite set of exponents. It does not cover all growing exponents uniformly and does not exclude every integer candidate. The conjecture remains open. The full proof and standalone finite-audit script are new; the main manuscript and PDF are unchanged.

## Uniformly growing exponent window

[The uniform-exponent supplement](UNIFORM_EXPONENT_WINDOW.md) extends the preceding fixed-exponent theorem: for every fixed A>0 it simultaneously counts all prime exponents ell≤(log log X)^A, with the same square-level bound X² exp(−c log X/log log X), c<(log 2)/2. The proof invokes the unconditional Siegel–Walfisz theorem and explicitly allows an ineffective starting threshold. It controls the sum of all exponent-dependent period errors.

The remaining larger prime exponents, and exceptional individual candidates even in the controlled window, are not excluded. The full conjecture remains open. The new verifier checks 102 exponent selections in nine growing windows, including exact rational density and period bounds.

## Polynomially growing exponent window via Linnik

[The Linnik-window supplement](LINNIK_EXPONENT_WINDOW.md) proves a larger unconditional range: prime exponents ell≤X^epsilon, for every fixed epsilon<1/(4L+1), where L is any admissible absolute exponent in Linnik's least-prime theorem. No numerical L or K is asserted. The bound remains X² exp(−c log X/log log X), c<(log 2)/2.

The proof constructs many distinct eligible primes by CRT and the least-prime theorem, then separately treats fixed, medium and large exponents. It accounts for both floor losses and all exponent-dependent period errors. This does not reach the full possible exponent range O(X log X) or exclude individual surviving powers; the conjecture remains open. Thirty CRT constructions and nine exact density-tail checks accompany the full argument.

## Sharper window from two primes

[The two-prime refinement](TWO_PRIME_REFINEMENT.md) improves the sufficient exponent-window restriction to epsilon<1/(4L−2), preserving the same strong sparsity bound. The proof uses the shared factor ell in two local periods and bounds the interval error by the number of allowed residue classes. It introduces no new analytic hypothesis and still leaves the full integer conjecture open.

The standalone verifier checks 12 exact joint-period cases and 3600 interval bounds. The theorem and the finite checks have distinct roles: the latter audit the periodic counting identities, not the infinite Linnik theorem.

## Improved bound covering every power exponent

[The quadratic-sieve supplement](ALL_EXPONENT_QUADRATIC_SIEVE.md) improves the uniform count of all powerful rotations to O_g(X² log log X/log X). Consequently, all nontrivial integer powers among the first N decimal entries satisfy O(N log log N/log N), with no restriction on their exponents.

The proof derives the exact quadratic weight identity, bounds its error uniformly in the cut and width, and estimates the denominator using Mertens products and an elementary weighted truncation. This improves the earlier all-exponent bound by one factor of log log N, but does not eliminate individual candidates or resolve the conjecture. The standalone verifier, exact certificate and output accompany the proof; the main manuscript and PDF remain unchanged.

## Growing-prime local square survivors

[The growing local-survivor theorem](GROWING_LOCAL_SURVIVORS.md) proves that, for every sufficiently large prime digit width d, there are 10^d exp(−(2 log 2+o(1))d/log d) endpoints whose same unrotated member is a square in Q_p for every prime p≤2d. These are local squares at arbitrary precision, not asserted integer squares. This gives a limitation of necessary square tests even when the set of tested primes grows.

The script computes exact residue classes and endpoint counts at widths 5, 7 and 11, then directly checks only selected candidate prefixes (773 prime checks). It does not directly check every candidate at each width. The asymptotic theorem follows from the proof, ordinary prime number theorem and Mertens estimates, not from extrapolating those samples. The integer conjecture remains open.

## Limitation of an exact-power main-term strategy

[The exact-main-term obstacle](EXACT_MAIN_TERM_OBSTACLE.md) shows that a natural same-width leading term cannot be a rational odd-prime power. If it is a rational square, and the cut is at least seven integers beyond the width's start, the rotation already fails the 2-adic square test. Thus forcing this term to be an exact power and using adjacent-power gaps produces no new square exclusion in that range.

This is a limitation of that specific method, not a general global impossibility result or a proof of the integer conjecture. Earlier-width cuts, the first few cuts, and nonexact algebraic approximations remain outside its scope. The standalone finite audit distinguishes modular identity checks from selected endpoint tests.

## Whole-block Jacobi certificates

[The cyclic Jacobi criterion](CYCLIC_JACOBI_CERTIFICATE.md) gives a sufficient certificate excluding every integer perfect power in a block even when all its rotations are squares over Q_3. It uses the Jacobi symbol of the normalized prefix modulo the cyclic modulus with its 3-part removed, without factoring that modulus.

Ten exact endpoint certificates beyond endpoint 5000 cover 51,939 rotations. The script checks the ten hypotheses, 50 selected cuts and, when available, ten SymPy cross-checks; the entire-block conclusion follows from the proof, not exhaustive testing of every rotation. Each certified block has common gcd exactly9. This is neither an infinite classification nor a resolution of Kashihara's conjecture.

## Power-of-two valuations and a complete finite certificate scan

[The extended Jacobi criterion](JACOBI_POWER_TWO_VALUATIONS.md) allows the common 3-adic valuation to be any 2^r with r≥1, subject to the stated hypotheses. The complete certificate-condition scan of endpoints 5001–10000 finds 94 successful blocks covering 706,590 rotations: 84 valuation-2 blocks and ten valuation-4 blocks. These totals include the earlier ten blocks, so the addition is 84 blocks and 654,651 rotations.

The run checks 188 selected cuts and cross-checks 206 preliminary Jacobi symbols with SymPy. It does not individually test every rotation for being a power: whole-block coverage follows from the theorem. Failed certificate conditions do not classify the remaining endpoints, and no infinite family or asymptotic success rate is inferred from the finite scan.

## An infinite growing-modulus Jacobi family

[The cyclotomic Jacobi theorem](CYCLOTOMIC_JACOBI_FAMILY.md) proves that, in each sufficiently large prime-power digit width d=3^h, at least a proportion 1/1998−o(1) of endpoints yield entire blocks of integer nonpowers. All their rotations are nevertheless squares over Q_3 and Q_37. Every prime factor of the growing certificate modulus exceeds 2d.

The infinite assertion follows from the character-counting proof, including the degenerate-discriminant case. The script checks 40 small-modulus character cases, the complete nine-digit congruence-restricted scan (450764 certified endpoints), and 30 selected prefix calculations across widths 9,27,81. It does not enumerate the larger widths or individually test all rotations. The lower proportion is within the stated digit-width blocks, not a density claim over all sequence entries. The full conjecture remains open.

## A union covering nearly all of a surviving endpoint class

[The cyclotomic Jacobi union](CYCLOTOMIC_JACOBI_UNION.md) extends the infinite family to digit widths d with h=v_3(d) tending to infinity and d a nonzero square modulo37, including even widths d=4*3^h. In the endpoint class m=666 modulo999, a proportion 1-O(2^(-h/2)) has a whole-block nonpower certificate, although every rotation remains a square over Q_3 and Q_37. The estimate is uniform in d/3^h and follows from exact CRT counts and a telescoping period, not an independence heuristic. All primes used exceed 2 sqrt(3^h).

The finite script checks nine exact CRT models, 200 selected endpoints at each of widths 9,27,36,81,108, and 21 selected exact prefixes. Sample rates do not establish or estimate the asymptotic theorem. This is conditional coverage in one endpoint class, not a density statement for all sequence entries or a resolution of the full conjecture. The main manuscript and PDF are unchanged.

## All high-3-valuation digit widths and an explicit cutoff tradeoff

[Uniform Jacobi coverage](UNIVERSAL_JACOBI_WIDTHS.md) removes the restriction on the digit width modulo37. At every digit width d with h=v_3(d) tending to infinity, it certifies asymptotically a proportion2/27 of endpoints, using both m=8 and18 modulo27. Every certified rotation is an integer nonpower but a square over Q_3. Exact37 phase counts separately identify which classes also pass Q_37; that compatibility is not asserted in all phases.

An explicit product bound permits a faster O(h^4*2^(-h)) residual for fixed cutoff, or a growing cutoff whose witness primes tend to infinity. The finite audit checks all27 and37 residues, 4656 exact rational product identities, 1600 sampled endpoints and48 selected exact prefixes. Infinite coverage and whole-block exclusion follow from the proof, not the samples. These remain sufficient conditions; the global conjecture is open and the main manuscript/PDF are unchanged.

## Union over power-of-two valuations

[The valuation union](JACOBI_VALUATION_UNION.md) combines all admissible valuations b=2^r, giving an endpoint proportion C-O(h^4*2^(-h)), where C=sum 2/3^(2^r+1)=0.08240615276287… and h=v_3(d) tends to infinity. All certified blocks are integer nonpowers but Q_3-square blocks. The individual valuation criterion was known in the earlier supplement; the new content is the infinite union count and its controlled interval error, obtained by omitting the largest cyclotomic modulus.

This increases the earlier2/27 endpoint proportion by approximately0.008332078689. It does not cover bounded h or imply Q_37 compatibility. A separate exact counterexample explains why replacing the3-power moduli by other odd-prime-power cyclotomic moduli does not preserve a uniform negative-character bound for arbitrary constants; it does not classify the actual concatenation constant.

The finite script checks exhaustive roots at valuations2,4,8;45 rational identities;800 sampled endpoints;32 selected exact prefixes; and300 selected residues for three counterexample moduli. Infinite and whole-block claims follow from proof, not samples. The global conjecture remains open; the main manuscript and PDF are unchanged.

## A bounded-valuation infinite width progression

[The bounded-valuation CRT certificate](BOUNDED_VALUATION_CRT.md) uses324 explicitly verified primes and a fixed612-digit integer L. Every width d=L*t with3 not dividing t has v_3(d)=1. Within36 endpoint classes modulo999, the certified count is at least (4H/111)*(1-2^(-322)); all corresponding blocks are integer nonpowers but squares over Q_3 and Q_37. Dropping37 compatibility gives a count at least (2H/27)*(1-2^(-322)).

This supplies a concrete bounded-v_3(d) family, rather than extrapolating the earlier high-valuation limit. It is structural: the widths are extraordinarily large. The construction uses a fixed finite prime set and does not establish arbitrary-accuracy coverage, every bounded-valuation width, or the global conjecture.

The standard-library verifier checks324 prime/period certificates, exact rational bounds,36 endpoint classes,353 exhaustive quadratic-constant models and six complete CRT models. It does not construct actual prefixes at those enormous widths. The main manuscript and PDF are unchanged.

## An effective antiperiodic13 family

[The antiperiodic13 theorem](ANTIPERIODIC_THIRTEEN.md) works at every digit width d=3+6a, starting at d=3. For even endpoints, W_m=m/2+5(a+1) modulo13. Combining a nonresidue value with m=8 or18 modulo27 gives12 explicit classes modulo702, certifying (2/117)H endpoints up to an absolute counting error at most12. All rotations are integer nonpowers, Q_3 squares and Q_13 nonsquare units.

This handles infinitely many widths with v_3(d)=1 without the preceding huge common width period. It differs from the older13-adic valuation-one family because these endpoints are units modulo13. The older family already included some antiperiodic widths; the new claim is the explicit linear formula and combined certificate, not the first use of that phase. The proof is uniform; it does not claim the small endpoints were absent from earlier computations.

The standard-library script checks all six matrix phases,13 width classes,450 direct even three-digit prefixes,42 selected larger-width prefixes and8084 individual rotations from15 certified three-digit endpoints. The global conjecture remains open, and the main manuscript/PDF are unchanged.

## Every odd width, including no factor of3

[The all-odd-width13 theorem](ALL_ODD_WIDTH_THIRTEEN.md) extends the explicit certificate to every odd digit width d>=3, including v_3(d)=0. The endpoint requirements are m=18 modulo27, m even, and a stated linear expression modulo13 being a nonresidue. There are six classes modulo702 at each width, giving H/117 endpoints up to absolute error6. Every certified block is an integer nonpower, a Q_3-square block and a Q_13-nonsquare unit block.

The new width phases are d=1 and5 modulo6. At d=3 modulo6, the old extra endpoint class remains available and gives the earlier12-class total. The proof uses a mod27 identity valid without a width-valuation hypothesis; old boundary translations and existing local ingredients are explicitly reused. It makes no assertion about even widths or the remaining endpoints.

Finite checks cover39 width phases,99999 general mod27 prefixes,15151 linear prefixes,48 selected larger-width prefixes and35082 modular rotations. The unbounded statements follow from proof, not sample extrapolation. The main manuscript/PDF are unchanged and the conjecture remains open.

## An effective37 certificate at every width

[The all-width37 theorem](ALL_WIDTH_THIRTY_SEVEN.md) supplies explicit linear phases for widths d=1,2 modulo3. Together with the inherited quadratic phase, it certifies endpoints at every digit width d>=2, including even widths and odd endpoints. Require m=18 modulo27 and the stated37 residue to be a nonsquare; every rotation is then an integer nonpower but a Q_3 square. At widths coprime to3 there are18 classes modulo999. The remaining phase has17,18 or36 classes, so every width has at least17 sufficient classes.

For odd widths the exact union with the13 certificate has20*n_d+222 classes modulo25974, where n_d is the37 negative-residue count. Count phases and actual endpoint-class phases are distinguished. The new ingredients are the two linear37 phases and their combinations; the old mod27 identity, boundary translation and quadratic phase are credited as inherited.

Finite checks cover111 width phases,111 representative odd-width union count phases,33333 direct prefixes,48 selected larger prefixes and3357 individual modular rotations. This does not classify all endpoints or solve the conjecture; the main manuscript/PDF are unchanged.

The accompanying independent scalar verifier additionally checks1596 prefixes through width400, all1443 odd-width class phases, and3357 literal integer rotations, confirming exact periods222 and2886 for counts and classes respectively.

## Cubic local survivors outside the square-block families

[The cubic local-survivor theorem](CUBIC_LOCAL_SURVIVORS.md) uses valuations b=3^r, r>=1, and a noncube residue at37. Every certified rotation is a cube in Q_3 but not a square there, yet no rotation is an integer power. These blocks are disjoint from the preceding Q_3-square-block families. The inherited cubic and37 prefix formulas are explicitly reused.

An infinite union of four endpoint classes per admissible valuation gives a uniform endpoint lower proportion tending to at least0.0089099921442867 as h=v_3(d) tends to infinity. This is a proved infinite valuation count, not extrapolation from a finite endpoint search. It does not handle all remaining classes or bounded h, and the full conjecture stays open.

The script exhausts all37 character phases and roots at valuations3 and9, checks98 exact tail/period inequalities, and verifies12 selected prefixes at widths27,54,81. Whole-block and unbounded conclusions follow from proof. The main manuscript/PDF are unchanged.

## A small-period equivalence for valuation-three cube blocks

[The fixed-valuation cubic classification](FIXED_VALUATION_CUBIC_CLASSIFICATION.md) proves that all rotations have exact3-adic valuation3 and are Q_3 cubes precisely when W_m=±27 modulo243 and27 divides D(m). Necessity needs only cuts0,1,2. A complete27-by243 phase table classifies this particular local type at every digit width; it does not classify all cube valuations or integer powers. The proof also gives the corresponding criterion at any specified positive valuation divisible by3.

Combining the table with the37 noncube test yields effective integer exclusions at v_3(d)=0,1,2 as well as higher values. For d=1 modulo3 it gives48 classes modulo8991, density16/2997 up to absolute error48. The d=0 modulo27 row overlaps the old b=3 family and is explicitly acknowledged.

The verifier checks27 full matrix phases, the boundary-cycle identity,6561 table cells,99999 direct endpoints and101385 modular rotations at three selected certified endpoints. No finite test is presented as a global conjecture classification. The main manuscript/PDF remain unchanged.

An independent scalar verifier additionally checks all local cells and999 combined width count phases, with49284 modulo37 prefix phase checks. Both proof corrections from review were incorporated: the cut-two normalization uses D(2)=2, and all finite density counts refer to the certified subset.

## A progression certificate beyond squares and cubes

[The prime-exponent progression lemma](LINEAR_PRIME_EXPONENT_CERTIFICATE.md) uses a witness prime of odd prime order q without requiring q to divide the digit width. Instead a single endpoint class modulo q forces the cyclic length to be divisible by q, and the prefix becomes linear along that progression. Verified suitable primes give exact e-th-power exclusion counts; the theorem does not claim witnesses exist for every e.

The explicit instance e=5,p=1031,q=103 combines with valuations5^r. It gives integer-nonpower blocks that are fifth powers in Q_3 but neither squares nor cubes there, disjoint from the earlier local-square and local-cube families. The construction permits both width and endpoint parities, requires103 not dividing d and sufficiently large v_3(d), and proves an infinite valuation-union lower bound. It does not classify all even widths or odd endpoints.

Finite verification covers306 q-step identities across102 phases,147 exact tail/period inequalities,12 selected prefixes and48 selected modular cuts. Whole-block and infinite assertions follow from proof. The main manuscript/PDF are unchanged; the global conjecture remains open.

An additional independent verifier checks408 complete affine counts,29520 valuation residues, all12 supplied prefixes and120 selected cuts including digit boundaries and m-1.

## Unconditional witnesses for each prime exponent at least five

[The Chebotarev witness theorem](CHEBOTAREV_EXPONENT_WITNESSES.md) removes the earlier witness-existence gap. For each fixed prime e>=5, an explicit Galois-field argument gives a positive-density set of witness primes whose10-order is odd and coprime to3. The progression lemma extends to composite orders, so it applies at both d=3^h and d=2*3^h.

For each fixed exponent and chosen witness, this yields positive-proportion certified blocks for sufficiently large h: their rotations are e-th powers in Q_3 but no integer perfect powers. This is an existence theorem for families indexed by every prime e>=5, not a uniform statement with growing e, an exclusion of every endpoint, or a solution of the integer conjecture. The proof is unconditional; no first-witness bound is asserted.

The finite verifier checks nine explicit exponents, including composite witness orders,135 scalar recurrence identities and2700 width coprimality checks. The assertion for all prime exponents follows from the field-intersection and Chebotarev proof, not those examples. The main manuscript/PDF are unchanged.

## An explicit growing-prime window

[The uniform effective-window theorem](UNIFORM_EFFECTIVE_EXPONENT_WINDOW.md) upgrades the fixed-exponent statement: for every h>=32, every prime5<=e<=h+1 has a certified positive endpoint count at both d=3^h and d=2*3^h. Ahn–Kwon's unconditional least-prime theorem and an explicit discriminant bound give p_e<=(10e)^(301848e^2); the interval comparison has no hidden exponent-dependent threshold.

Each exponent has its own subset with exact3-adic valuation e, so subsets for different e are disjoint. This is not an exclusion of all endpoints or of exponents outside the stated growing window. The numerical bounds are theoretical and extremely impractical. No GRH is assumed.

The verifier audits exact constants, the h=32 base,9999 finite induction cases and412 prime/window comparisons. The cited theorem plus the written induction and discriminant proof justify the unbounded result. Main manuscript/PDF remain unchanged; the integer conjecture is open.

## Arbitrary fixed width multipliers

[The fixed-multiplier witness theorem](ARBITRARY_FIXED_MULTIPLIERS.md) constructs witness orders coprime to6u for any fixed positive u with3 not dividing u and any fixed prime e>=5. It handles u containing e by forcing exactly one e factor in p-1 and then removing it from the order through the e-th-power condition. A compatible cyclotomic Frobenius supplies a positive-density prime set.

The previous endpoint construction consequently applies to d=u*3^h for all sufficiently large h, including both parities of u. The witness and threshold may depend on u and e; this is not a uniform statement for u growing with h or an exclusion of all endpoints. The examples include u=103, where the old fifth-power witness of order103 fails and a new order1483 works.

Nine explicit witnesses and900 finite coprimality checks pass. The arbitrary-fixed-u conclusion follows from the field-intersection and Chebotarev proof rather than these examples. Main manuscript/PDF remain unchanged and the integer conjecture is open.
