# OEIS papers

This repository contains OEIS-related mathematical papers, their sources, and
reproducibility materials.

- [A075000-A075002](papers/A075000-A075002/): proves the existence statements for
  OEIS A075000, A075001, and A075002.

- [A181373](papers/A181373/): an elementary constructive proof that every prime
  except 2 and 5 divides all digit rotations of some concatenation 123...m.
  Includes an explicit witness bound and verification program.

- [A075018](papers/A075018/): proves that the four-term descending concatenation
  is divisible by every positive modulus for infinitely many starting points.
  A stronger even-base theorem handles any fixed block count and ordering,
  independently of the modulus. Includes PDF, LaTeX and independent checks.
- [A077183-A077185](papers/A077183-A077185/): proves the 2005 conjecture
  that exactly the primes 2 and 5 fail to divide any descending decimal
  prefix k||...||1. Stronger theorem for all bases and primes,
  with two-page PDF, LaTeX and independently verified witness code.
- [A087354 (also A391022 and A391189)](papers/A087354/): proves all-index
  existence of squares obtained by concatenating arbitrarily many **strictly
  increasing distinct nonzero square blocks**. Complete two-page paper,
  compiled PDF, and independent integer-verification script.

- [A006063 / A096680 / A096904](papers/A006063/): exact cube-sum permutation membership and multiplicity classifications, 109 core witness certificates, Hall obstructions, and an exponential cube-root lower bound on permutation counts. Includes independent checks and a PDF research note.

## Authors of manuscripts not yet submitted to OEIS

The manuscripts for **A006063/A096680**, **A075018**, **A077183/A077185**
and **A087354** (including the related square-concatenation sequences)
are credited to Qichao Wang (Hebei University of Technology) and
Daoyu Dong / 董道豫 (University of Electronic Science and Technology of China).
Both authors appear on the LaTeX title pages and regenerated PDFs.

Previously accepted manuscripts (A075000-A075002, A181373 and
A083468-A083469) retain their original authorship and are unchanged.
The A077306 research note restates the accepted A075001 existence result
and is not a separate manuscript.

- [A069862](papers/A069862/): gives an **exact finite arithmetic minimum formula for every positive index**,
  using multiplicative-order phases, quadratic residue classes, CRT, and ceilings.
  The formula includes a finite minimum over explicitly computed candidates.
  Also proves infinitely many witnesses and the bound a(n)<10^n-n for n>=2,
  and gives simpler least-length formulas
  on two infinite families (including a(n)=n for decimal-smooth moduli and
  a(n)=2n-1 on a 7-denominator family), with a companion prime-power theorem.
  The a(n)=2 classification is prior work of David Wasserman (2005), A069860.
