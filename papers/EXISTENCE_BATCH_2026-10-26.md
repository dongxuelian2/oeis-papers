# Existence and minimum results, October 26, 2026

This batch addresses five existence questions recorded as conjectures in eight
OEIS entries. Each note includes its LaTeX source, compiled PDF, a standard-library
Python verifier, and a proposed OEIS update. The manuscripts follow the
repository's joint credit to Qichao Wang and Daoyu Dong.

| Entries | Existence result | Minimum result |
| --- | --- | --- |
| [A088862 / A090335](A088862-A090335/) | Every prime signature has infinitely many representatives with prefix-free divisor representations, in every base; an explicit witness bound is supplied. | The notes establish existence and a bound. The general least-value problem remains open here. |
| [A087304](A087304/) | Infinitely many nontrivial multiples preserve the nonzero digit product. | Exact all-index finite digit recurrence with a proved state-count bound. |
| [A086558](A086558/) | Every index has a number with its prescribed length, prefix and prime signature. | Exact all-index finite prime-parameter minimum; one integer root and one next-prime operation suffice at prime-power indices. |
| [A346644](A346644/) | Every positive integer occurs as the reduced denominator of the mean of an integer's divisors. | Exact partition formula at every odd prime-power index; `a(2^s)=2^(2^s-1)`, hence `a(q)=2^(q-1)` for every prime `q`. |
| [A115038 / A115039 / A115041](A115038-A115041/) | The shared conjecture follows from the standard difference-of-squares identity and `5^2+2=3^3`. | Exact finite minimum over odd prime-power candidates; both companion values follow. |

The finite minimum formulas specify bounded ranges or a bounded number of
recurrence steps and prove that every smaller eligible value is represented.
The A087304 formula works by digits rather than successive multiples. The
A086558 formula reduces the final prime choice to `nextprime`, while its
other prime parameters range over finite explicit intervals. These are finite
minimization formulas. The displayed closed families are identified separately.

The A346644 partition theorem gives, for example, `a(81)=57600`, verified
independently against every smaller positive integer. The A115038 identity
is elementary and its three sequence encodings count as one question.

## Source checks

All sources below were inspected on October 26, 2026.

- [A088862](https://oeis.org/A088862) and [A090335](https://oeis.org/A090335)
  record their existence as conjectural. Their names, formulas and examples
  use the prime-factor count, while both published offsets and synthesized
  b-files start at index 1 with value 1 (zero factors). The notes use the
  actual factor count and propose aligning the offset with that count.
- [A087304](https://oeis.org/A087304) records the nonvanishing conjecture.
  Its existing shift identity is credited to Chai Wah Wu. The standard
  coprime repunit construction in [A340204](https://oeis.org/A340204) is
  explicitly credited; the new note extends it to the nonzero digit product.
- [A086558](https://oeis.org/A086558) records the nonvanishing conjecture.
  The proof uses [Dusart's 2010 paper, Proposition 6.8](https://arxiv.org/abs/1002.0442v1)
  for every real `x>396738`. The same proposition supplies the explicit
  prime clusters for the prefix-code theorem.
- [A346644](https://oeis.org/A346644) records the denominator-existence
  conjecture. The existence proof uses
  [Dirichlet's theorem](https://arxiv.org/abs/0808.1408v2).
- [A115038](https://oeis.org/A115038), [A115039](https://oeis.org/A115039)
  and [A115041](https://oeis.org/A115041) repeat the same existence conjecture.

The status descriptions refer to the statements recorded in these entries.
The proofs and literature references accompany the proposed updates for review.

## Screening decisions

Existing repository results A075000--A075002, A075018, A077183/A077185,
A083468/A083469, A087354, A181373 and A069862 were excluded from the new targets.

[A336893](https://oeis.org/A336893) was excluded because its entry already
contains a 2020 existence proof. [A038664](https://oeis.org/A038664),
[A117545](https://oeis.org/A117545) and [A088508](https://oeis.org/A088508)
were left outside this batch: their general existence questions require
respectively prescribed consecutive-prime gaps, prime values of cyclotomic
polynomials, and divisibility properties of the digits of pi. No complete
proof for these questions was obtained in this session.

## Reproduction

From the repository root:

```bash
python3 papers/A088862-A090335/verify.py
python3 papers/A087304/verify.py
python3 papers/A086558/verify.py
python3 papers/A346644/verify.py
python3 papers/A115038-A115041/verify.py
```

All verifiers use the Python standard library and exact integers for the
claimed finite certificates and minima. The A086558 verifier additionally
checks logarithmic inequalities numerically as regression controls; the
paper proves their infinite range analytically. Each `main.tex` can be
compiled twice with `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.
The new workflow runs all five verifiers and compiles all five papers.

The complete local results are recorded in [the verification record](EXISTENCE_BATCH_VERIFICATION_2026-10-26.txt).
