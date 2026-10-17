# OEIS A077187 — decimal mountain concatenations (partial results)

**Author:** Qichao Wang. **Date:** 2026-10-17.
**Status:** computer-assisted, not externally peer reviewed. **The unrestricted A077187 conjecture remains OPEN.**

Let
\[
M(k)=1\Vert2\Vert\cdots\Vert k\Vert(k-1)\Vert\cdots\Vert1
\]
be the decimal mountain concatenation. This folder collects the current *partial* existence theorems and reproducible exact-integer certificates.

## Proven subfamilies (subject to independent manuscript and code review)

For primes \(p\ge7\), let \(r=\operatorname{ord}_p(10)\).
Our cumulative result is the smooth-order family
\[
\boxed{r=2^a3^b5^c,\qquad a,c\ge0,\ 0\le b\le8
\quad\Longrightarrow\quad \exists k\ge1:\ p\mid M(k).}
\]
This folder's new result specifically treats **\(b=8\)**, assuming the earlier affine-monodromy lemma and lower-stage certificates. It does not prove existence for arbitrary prime-order structures, does not compute least \(k\), and does not update OEIS directly.

For \(b=8\), all **486 primitive phases modulo 729** were checked using exact cyclotomic norms and a GMP one-shot gcd sieve. Six phases had nontrivial gcd, with prime factors 52489, 328051, and 839809. Each factor's actual order phase differs from the phase at which the gcd appears; its actual-phase gcd is 1. Therefore no admissible prime makes both affine-drift coordinates vanish in this order class.

The novel computational simplification is the **cubic relative norm tower** reducing cyclotomic norm degrees
\[
486\to162\to54\to18\to6\to2\to1.
\]
For a cubic relative extension, the core identity is
\[
\operatorname{Norm}(A+xB+x^2C)=A^3+yB^3+y^2C^3-3yABC,\qquad x^3=y.
\]
The next stage would address \(b=9\) or develop a general mechanism for multiplicative orders with prime factors beyond \(2,3,5\).

## Materials

- [main.pdf](main.pdf) — two-page English partial-theorem paper (compiled from [main.tex](main.tex)).
- [candidate_table.tex](candidate_table.tex) — complete list of the six nontrivial gcd rows, typeset in the paper.
- [exact_b8_fast.py](exact_b8_fast.py), [tower_norm.py](tower_norm.py), [generate_norms_parallel.py](generate_norms_parallel.py) — exact formula and 486-norm computation.
- [norm_gamma_*.txt](.) — all 486 full integer norms (approximately 5,800 digits each).
- [one_shot_gmp_b8.cpp](one_shot_gmp_b8.cpp), [all_486_gmp.tsv](all_486_gmp.tsv) — full-range one-shot GMP gcd checks.
- [audit_all_b8.py](audit_all_b8.py), [independent_relative_check.py](independent_relative_check.py), [check_direct_b8.py](check_direct_b8.py), [verify_all.py](verify_all.py) — exact audits, independent finite-field checks and full digit-layer recurrences.

The source scripts use Python 3, SymPy and NumPy. The gcd program uses GMP and a C++17 compiler.

Reproducibility steps (from this directory):
1. `python generate_norms_parallel.py`
2. `c++ -O3 -std=c++17 one_shot_gmp_b8.cpp -lgmpxx -lgmp -o one_shot_gmp_b8`
3. `bash run_sieves.sh`
4. `python verify_all.py`
5. Compile `main.tex` twice with `pdflatex`.

All computational evidence supports the specified infinite subfamily only. The underlying formulas, software and final claims await external mathematical audit. No all-primes proof is claimed.
