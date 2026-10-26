# A005046: both conjectures proved

The [paper](main.pdf) proves both conjectures currently stated in the
[official entry](https://oeis.org/A005046):

- Eventual periodicity modulo every positive integer, using the finite module
  `(Z/mZ)[s,c]/(s^m,c^m-1)` and the operator `L=c*d/ds+s*d/dc+s`.
- The exact Bessel moment formula `a(n)=2/e * sum(k^(2n)*I_k(1), k>=1)`
  for every `n>=1`, with convergence justified before differentiation.

It also proves that modulo 10, the six-term block `1,4,1,9,6,9` repeats from
index 1. Polynomial cycle certificates modulo 2 and 5 prove this for all indices.
The general finite-state bound is coarse; it is not a claim of an efficient
algorithm for large moduli.

Run `python3 papers/A005046/verify.py`. It checks 132 stored official terms,
literal partitions of sets of at most 10 elements, finite differential modules
modulo 2 through 32 through index 250, exact polynomial cycle certificates,
and numerical Bessel sums for indices 1 through 12. The numerical check is
separate from the analytic proof. The stored official table is explicitly a
prefix of the 251-term b-file, not the entire file.

`oeis.txt` is a proposed update; nothing has been submitted to OEIS.
