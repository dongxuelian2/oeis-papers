# A087354: certified exact minima at n=20..25

**Authors:** Qichao Wang (Hebei University of Technology); Daoyu Dong / 董道豫 (University of Electronic Science and Technology of China).

This is a **separate exact-minimum supplement** to the all-index existence paper in `main.tex`. It is *not* an all-index closed formula. All values below are perfect squares, with an exact partition into the stated number of nonzero-square blocks.

| n | a(n) | sqrt(a(n)) | decimal digits | status |
| --- | ---: | ---: | ---: | --- |
| 20 | 111125911149919941444 | 10541627538 | 21 | new exact value |
| 21 | 444411911999914911441 | 21081079479 | 21 | confirmation of OEIS comment |
| 22 | 11199444494448114419449 | 105827427893 | 23 | new exact value |
| 23 | 144949449149149194448144 | 380722272988 | 24 | new exact value |
| 24 | 1111425414199449191191449 | 1054241629893 | 25 | new exact value |
| 25 | 41914991191911941194149136 | 6474178804444 | 26 | new exact value |

## Proof reduction

Any decimal concatenation of n nonzero squares has **at least n digits**. The values in the table supply witnesses with no more than n+1 digits. Therefore it is enough to exhaust only the n- and (n+1)-digit cases to certify these particular minima; at n=21 the displayed witness already has n digits.

For exactly n digits, all blocks must be from `D={1,4,9}`. For exactly n+1 digits, there must be **exactly one** two-digit block from `E={16,25,36,49,64,81}` and all other n-1 blocks are from D. In formal-language notation, the full candidate sets are

```
W(n,n)   = D^n
W(n,n+1) = union_{j=0}^{n-1} D^j E D^(n-1-j)
```

A decimal prefix p of d digits in an L-digit number has all its completions inside

```
[p*10^(L-d), (p+1)*10^(L-d)-1].
```

The branch can be excluded **exactly** if the ceiling of the square root of the left endpoint exceeds the floor of the square root of the right endpoint (or the right endpoint truncated to the known candidate upper bound). This gives a complete branch-and-bound search with no probabilistic assumptions. All accepted leaves are verified to be perfect squares. A separate block partition check validates the upper bounds.

A concrete 20-block witness is

```
10541627538^2 =
1 | 1 | 1 | 1 | 25 | 9 | 1 | 1 | 1 | 4 |
9 | 9 | 1 | 9 | 9 | 4 | 1 | 4 | 4 | 4
= 111125911149919941444.
```

The length-20 search finds zero squares, and length-21 finds no admissible square below this candidate. Likewise, the searches establish the remaining table entries.

## Reproduce

```sh
python papers/A087354/verify_minima.py
python papers/A087354/verify_minima.py --extended
g++ -std=c++17 -O3 papers/A087354/verify_minima.cpp -o /tmp/a087354_minima
/tmp/a087354_minima
pdflatex -interaction=nonstopmode -halt-on-error minima.tex
```

The Python script uses only exact integer `math.isqrt`; the independent C++ verifier uses exact 128-bit arithmetic with a corrected square-root estimate (the estimate alone is never trusted). The `--extended` switch performs the slower full n=25 Python exhaustion; the C++ complete six-index audit is quick. The paper source is `minima.tex`, separate from the existing `main.tex`.

**Limitations:** No formula valid for arbitrary n is claimed. The digit-length reduction works for these indices because witnesses of at most n+1 digits exist; it must not be extrapolated to all n without a proof. No OEIS entry has been edited.

Source: https://oeis.org/A087354 (accessed 2026-10-22).
