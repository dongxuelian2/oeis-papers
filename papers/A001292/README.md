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
