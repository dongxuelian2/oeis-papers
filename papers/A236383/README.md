# A236383: existence and exact minima at every index

The [official entry](https://oeis.org/A236383), accessed 2026-10-26,
defines the least k such that k² concatenates equally long positive
integers x and y with y=x+n². It conjectures existence at every n.

This is proved uniformly, including indices divisible by 11. Let D
be the decimal digit count of 4(n+1)², and choose the least d>=D
with d odd and 5d+2n=0 mod11. Such d always lies in [D,D+21]. Put

```
C=(10^d+1)/11,
k=n+5C,
x=5(2n+5C)/11,
y=x+n².
```

The binomial congruence C=d mod11 proves integrality. Both x and y
have exactly d digits, and k²=10^d*x+y. This supplies an explicit
witness and a finite length bound for every index.

For each length 1..d, form all roots of k²=n² mod(10^length+1),
using explicit odd-prime-power lists and CRT. The digit inequalities
give exact integer-square-root endpoints. The minimum retained root
is the exact sequence value, and the first nonempty length suffices.
This formula retains finite arithmetic minimization; it is not an
elementary expression without a minimum.

Run `python3 papers/A236383/verify.py` from the repository root.
It reproduces the complete 245-term official b-file, compares all
659 attained minima from an independent exhaustive scan k=1..1000000,
checks local roots and CRT against direct residue enumeration, and
checks the explicit construction at large indices including powers
of 11 and a 101-digit integer. The new 300-term `b236383.txt` extends
the official range. `b236383-published.txt` is the unchanged official
b-file downloaded on 2026-10-26 for comparison.

`main.tex` gives the full proof; `oeis.txt` is an update draft and
has not been submitted to OEIS.

The final `main.pdf` is 2 pages. Both LaTeX passes completed without
Warning, Overfull or Underfull lines, and both rendered pages were
visually inspected after the final build.
