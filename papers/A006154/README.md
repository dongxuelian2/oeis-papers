# A006154: explicit eventual periods at every modulus

[A006154](https://oeis.org/A006154) counts ordered set partitions
into odd-sized blocks. We prove Peter Bala's 2023 conjecture of
eventual periodicity modulo every integer.

For `m>=2`, take the least common multiple of `phi(p^e)` over odd
prime powers exactly dividing m, together with `2^e` for its
power-of-two part. This is a period from index m. It divides
`2*phi(m)`, and divides `phi(m)` for odd m. The exact eventual
period modulo 10 is 4, with block `(1,2,7,2)` beginning at index 1.

The proof applies the derivation `D=c*d/ds+s*d/dc` to
`u=1/(1-s)`. In odd prime characteristic p, `D^p=D`; in characteristic 2,
`D^4=D^2`. Commuting-operator binomial lifting proves the
prime-power bounds, followed by the Chinese remainder theorem.
This extends the 2011 differential formula explicitly credited in
the official entry.

[main.tex](main.tex) and [main.pdf](main.pdf) are the canonical
manuscript. Run `python3 verify.py` for all 201 published terms,
literal ordered partitions through 8 elements, exact finite-ring
checks modulo 2 through 32 and explicit period controls. The source table
was downloaded from the official b-file on 2026-10-27.
