# A237930: Six forbidden prime classes

The [official entry](https://oeis.org/A237930), accessed 2026-10-26,
conjectures that the sequence (7*3^n-1)/2 has no prime factor in
classes 11,13,23,61,71,73 modulo 84. All six exclusions are proved:
quadratic reciprocity gives (3/p)=1 and (7/p)=-1, incompatible with
7*3^n=1 modulo p. A finite multiplicative-order/discrete-log test
also gives the exact incidence condition for every other prime.
This does not claim that the six classes exhaust all excluded primes.

`main.tex` gives the full proof; final `main.pdf` has 2 page(s).
Run `python3 papers/A237930/verify.py` from the repository root.
The official
`b237930-published.txt` was downloaded from the official OEIS b-file
on 2026-10-26 for independent comparison. `oeis.txt` is an update draft,
not a submission to OEIS. Both LaTeX passes had no Warning, Overfull or
Underfull lines, and all final rendered pages were visually inspected.
