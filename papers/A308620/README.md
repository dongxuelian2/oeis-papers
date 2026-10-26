# A308620: exact rational GF and order10 recurrence

[OEIS](https://oeis.org/A308620) retains conjectures for a rational
generating function and recurrence signature `(2,0,-2,1,2,-2,0,0,0,-1)`.
We derive both from the established exact state-count formula in
Burger–van der Merwe–van Vuuren, Theorem3, Eq4.2 (2012), inspected in
the [author-hosted primary paper](https://www.vuuren.co.za/papers/GamesPaths.pdf).

The recurrence holds for **n>=12**. At n=11 it predicts41 while
the correct value is42. This initial anomaly follows from the x^11
numerator term and is explicitly recorded instead of hidden.

[main.tex](main.tex) contains the complete formal summation proof.
`python3 verify.py` audits the established binomial formula and GF
through1000, all40official terms, the boundary exception, and a fully
independent binary-word enumeration of reversal classes through18.
No OEIS update has been submitted.
