# A214972 and A152009: exact jumps and deterministic L-sieve convergence

[The paper](main.pdf) proves three statements from the official entries:

- [A152009](https://oeis.org/A152009) satisfies `s(1)=1`, `s(r+1)=floor((3s(r)+3)/2)` for every r.
- [A214972](https://oeis.org/A214972) counts these thresholds: `a(n)=#{r:s(r)<=n}`. Its jumps occur exactly at the A152009 terms.
- Iterating the L-sieve converges coordinatewise to the triangular numbers. For any nonempty deletion set with infinite complement, its first k coordinates are triangular after at most `2k-1` transforms. The proof needs no randomness. Inputs which delete every remaining position do not define an infinite transform and are explicitly outside this natural domain.

The proofs use the complement-rank map `F_A(j)=1+b_j`, where b_j is the j-th position not deleted. The L-sieve terms are exactly `F_A^(r-1)(1)`. The jump identity generalizes to deleting positions congruent to 1 modulo any integer d>=2.

Run `python3 papers/A214972-A152009/verify.py` from the repository root. Independent checks cover direct recurrence and literal list deletion for d=2..12 and n<=100000, all 26 published A152009 values, 11 iterations on 275 finite or periodic deletion sets, and 100 triangular fixed-point terms. The official b-file prefix is attributed in its file header. Finite checks support the implementations; the full claims follow from the proofs.

`oeis.txt` is an update draft, not a submitted or accepted OEIS update.
