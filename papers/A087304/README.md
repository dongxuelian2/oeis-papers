# A087304: existence and an exact finite minimum recurrence

Every positive integer has infinitely many nontrivial multiples preserving its
nonzero digit product, in every base. Write `n=q*m`, where `q` is supported on
the base primes and `m` is coprime to the base. Choose `q | b^s` and a repunit
`R_t` divisible by `m`. Then `(n*b^(j*t)+R_(j*t))*b^s` is a valid witness for
every positive `j`.

The decimal minimum has an exact finite digit recurrence. States track the
remainder modulo `n`, the unused digit-product factor, and a finite automaton
excluding the words `digits(n)0*`. The shortest accepting word has at most
`n*tau(P)*(digits(n)+2)` digits. The recurrence and its minimality proof are in
`main.tex`; `verify.py` evaluates it in increasing length and lexicographic order.

The familiar repunit argument for moduli coprime to ten is already recorded in
A340204. The decimal shift identity is credited to Chai Wah Wu in A087304.

Run `python3 papers/A087304/verify.py` from the repository root.
`oeis.txt` contains the proposed update. The minimum recurrence is a finite
state formula, with finite minimization over transitions.
