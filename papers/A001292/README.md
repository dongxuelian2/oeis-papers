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
