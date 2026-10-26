# A340138: complete permutation proof

Official source: <https://oeis.org/A340138>, read in full 2026-10-26.
The comments still conjecture that the sequence permutes all
nonnegative integers.

**Indexing clarification:** the prose rule for `a(n+1)` refers to
`a(n-1)` despite giving only `a(1)`. Its Mathematica program uses
the last term, and its data agree with that program. We prove the
permutation statement for this published sequence: `a(1)=0`, and
`a(n+1)` is the smallest unused nonnegative integer containing the
digital root of `a(n)` among its decimal digits. Thus `a(2)=10`.
The source inconsistency is made explicit in the proof and update
draft; no unspecified alternative rule is silently initialized.

The proof in [main.tex](main.tex) works in every base `b>=2`:

- A root occurring infinitely often forces every number containing
  its digit to occur, by greedy minimality.
- Among those numbers are infinitely many of each digital root:
  use the words `r 0...0 d` with `r+d == s mod (b-1)`.
- Some root recurs infinitely by finiteness; the previous step
  forces every root to recur, hence every positive integer appears.

The process is always defined because infinitely many numbers contain
any fixed digit and only finitely many are used at a finite stage.
Together with distinctness and the initial zero, this proves the
full permutation assertion.

Run `python3 verify.py`: all 10,000 published terms, an independent
candidate scan in bases 2..16, and every root-propagation construction
for those bases are checked. The saved source b-file is
`b340138-published.txt`.
[oeis.txt](oeis.txt) is an update draft, not a submission.
