# Rook tours with equal or opposite endpoint columns

The paper proves Kurkov's November 2019 conjectures in [A001040](https://oeis.org/A001040) and [A001053](https://oeis.org/A001053). On an n-row, two-column board, directed Hamilton rook tours with endpoints in opposite columns number `2 n! A001040(n)`; those with endpoints in the same column number `2 n! A001053(n)`.

The proof counts tours by the number of moves between columns. It then proves the two resulting finite-sum recurrences by elementary factorial identities. The finite coefficient sums are credited to Paul Barry (2004) and Peter Bala (2013). Alekseyev's related 2024 proof concerns closed tours.

- [main.tex](main.tex), [main.pdf](main.pdf): the complete counting proof.
- `verify.py`: independent literal rook-graph Hamilton-path enumeration, finite sums, and recurrence checks.
- `b001040.txt`, `b001053.txt`: recurrence values for n=0..100.
- `oeis.txt`: proposed comments for both entries.

Run `python papers/A001040-A001053/verify.py`. Regenerate both tables with `python papers/A001040-A001053/verify.py --write-tables`.

The subset enumerator has exponential memory and time costs in the board size; its finite controls use n<=8. The proof applies to every positive n. Tours are directed, so reversing a tour counts separately. The n=0 values are recurrence initial conditions rather than tours of an empty board.
