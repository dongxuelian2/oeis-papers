# A136050: A digit-sum congruence for twin-prime products

The [official entry](https://oeis.org/A136050), accessed 2026-10-26,
conjectures that every noninitial term is 8 modulo 9. This holds
for every twin-prime pair: except (3,5), a pair is 6m-1,6m+1, so
its product is 36m²-1 and its digit sum is congruent to -1 modulo 9.
The proof neither assumes nor proves the infinitude of twin primes.
It settles the whole stated congruence, without claiming that every
positive integer congruent to 8 is attained.

`main.tex` gives the full proof; final `main.pdf` has 1 page(s).
Run `python3 papers/A136050/verify.py` from the repository root.
The official
`b136050-published.txt` was downloaded from the official OEIS b-file
on 2026-10-26 for independent comparison. `oeis.txt` is an update draft,
not a submission to OEIS. Both LaTeX passes had no Warning, Overfull or
Underfull lines, and all final rendered pages were visually inspected.
