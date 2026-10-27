# A003630: the inert-prime product

For the primes in [A003630](https://oeis.org/A003630), take the factor
`(p-1)/(p+1)` when `p=1 mod4`, and its reciprocal otherwise.
The manuscript proves Dimitris Valianatos's 2017 conjecture that the
product, in increasing prime order, equals `sqrt(3)/2`.

For every cutoff `X>=3`, the exact finite identity is

```
P(X) = (9/8) * L_X(1,chi_-3) / L_X(1,chi_4).
```

The factor `9/8` corrects the exceptional Euler factors at 2 and 3.
A proved prime-number-theorem estimate for arithmetic progressions
gives ordinary convergence of both prime-ordered Euler products.
The elementary integrals for their limiting values are
`L(1,chi_-3)=pi/(3*sqrt(3))` and `L(1,chi_4)=pi/4`.
The proof uses Theorem 1.2 of Bennett–Martin–O'Bryant–Rechnitzer,
*Explicit bounds for primes in arithmetic progressions*,
[arXiv:1802.00085v3](https://arxiv.org/abs/1802.00085v3).

The classification of inert primes as primes `5,7 mod12` is already
recorded with a proof in the OEIS entry, including Jianing Song's
2018 comment. The completed problem here is the separate product
conjecture. 

- [main.tex](main.tex) and [main.pdf](main.pdf): proof and canonical manuscript.
- `verify.py`: exact finite Euler-factor and source-data checks.
- `b003630-published.txt`: unchanged official 1000-term b-file,
  downloaded from https://oeis.org/A003630/b003630.txt on 2026-10-27.
- `oeis.txt`: update draft with the proof identity and manuscript link.

Run `python3 papers/A003630/verify.py` from the repository root.
It checks all 1000 official terms, independently tests the
quadratic-residue definition through one million, and checks the
rational identity at every prime cutoff through 10000. The
increasing-order convergence is established by the analytic proof;
numerical partial products are supplementary controls.
