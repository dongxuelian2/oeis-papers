# A346644: exact minima for every index

[A346644](https://oeis.org/A346644) asks for the least positive integer `K`
whose divisor mean `sigma(K)/tau(K)` has reduced denominator `n`.
The [paper](main.pdf) proves existence and an exact finite arithmetic formula
for **every** `n`, including arbitrary composite indices.

The main reduction is a divisor-preserving normal form: every witness has a
divisor with the same denominator for which each exponent plus one has only
prime factors dividing `n`, and each local prime-power divisor mean is reduced.
Thus the odd part of every minimum is a square; for odd `n` the whole minimum
is a square.

To obtain an explicit bound, write `n=product q_i^a_i` in increasing prime order
and let `ell_i` be the i-th prime. Start with `U_0=1` and put

```
b_i = a_i + v_(q_i)(sigma(U_(i-1)))
U_i = U_(i-1) * ell_i^(q_i^b_i - 1).
```

Then `U_s` has denominator `n`. The proof is elementary: every prime factor of
`1+p+...+p^(q^b-1)` exceeds `q` whenever `p != 1 mod q`.

The all-index formula enumerates finite tuples of base primes bounded by this
witness. It allocates the prime factors of each exponent plus one in increasing
order. Multiplicative orders determine which bases can receive an allocation
and how much cross-factor cancellation must be compensated. Each stage branches
over explicit weak compositions. Every output has denominator `n`, and the
normal-form theorem ensures that the least witness appears. The minimum of
these candidates is `a(n)`; see the all-index minimum theorem in Section 4 of the paper
for the complete definitions. This is a **finite minimization formula**, not
an elementary expression without minimization.

At odd prime powers, the formula simplifies to

```
a(q^s) = min product ell_i(q)^(q^b_i-1),
```

over partitions `s=b_1+...+b_t`, `b_1>=...>=b_t>=1`, where `ell_i(q)` are the
increasing primes not congruent to `1 mod q`. Also `a(2^s)=2^(2^s-1)` and
`a(q)=2^(q-1)` for every prime `q`.

Examples: `a(30)=115200`, `a(40)=6480000`, `a(42)=1843200`, `a(45)=3600`,
`a(60)=4706440200`, `a(81)=57600`. At `n=30` the minimum has divisor count 90,
so permitting cancellation between distinct prime-power factors is essential.

## Reproduce

Only Python's standard library is needed. From the repository root:

```sh
python3 papers/A346644/minimum.py 30 40 42 45 60 81 --statistics
python3 papers/A346644/minimum.py --table 200
python3 papers/A346644/verify_minimum.py
python3 papers/A346644/verify.py
```

`minimum.py` uses the normal form and proved integer branch bounds to search
factorizations. It also includes the constructive normalization and a separate
`triangular_candidates` implementation of the formula for fixed prime tuples.
The [200-term table](b346644.txt) is reproduced by the audit; this table is a
computed consequence of the proof, not an independent verification of all terms.

Independent controls check normalization for every `K<=50000`, all 48 minima
occurring at `K<=1000000` using actual divisor sums and counts, all 39 published
terms, and equality of complete bounded candidate sets against direct
enumeration. Two hundred canonical elementary witnesses are checked as well.
The older `verify.py` retains the original construction and prime-power controls.

[oeis.txt](oeis.txt) is an update draft, not an accepted OEIS submission.
