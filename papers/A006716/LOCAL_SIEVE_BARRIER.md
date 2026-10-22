# A006716: length-uniform local-square abundance and the sieve barrier

Research note — October 22, 2026. Authors: Qichao Wang (Hebei University of Technology); Daoyu Dong (University of Electronic Science and Technology of China).

**Scope.** This is an elementary, self-contained *local* result about integers having only the digits `1,4,9`. It does **not** construct new integer squares and does **not** settle OEIS [A006716](https://oeis.org/A006716)'s conjectural finiteness. Results rely on standard elementary number theory, including Hensel lifting / the characterization of squares modulo prime powers. Literature novelty is not claimed.

## Theorem A: exact classification of local unit squares

Let `n>=3`. Among the `n`-digit integers whose digits belong to `{1,4,9}` and whose *last digit is odd*, the following are equivalent:

1. `W` is a quadratic residue modulo `10^n`.
2. `W ≡ 1 (mod 8)`.
3. The final three digits of `W` are precisely **441 or 449**.

Therefore exactly `2*3^(n-3)` of the length-n digit words with an odd final digit are squares modulo `10^n`, and **every such word has exactly eight distinct square roots modulo `10^n`**.

### Proof

The last digit is 1 or 9, so W is coprime to 10. Modulo 5, W is either 1 or 4, both nonzero quadratic residues. The standard odd-prime Hensel lifting criterion then shows W is a square modulo `5^n`.

An odd integer is a square modulo `2^n` for any `n>=3` precisely when it is 1 modulo 8. All decimal places at positions `i>=3` contribute a multiple of 8, so the residue modulo 8 depends only on the final three digits. Directly checking the 18 permitted final-three-digit combinations with last digit 1 or 9 shows that only 441 and 449 are 1 modulo 8. CRT proves the equivalences.

The number of such words is `2*3^(n-3)`: each higher digit is free. A unit of the form 1 modulo 8 has exactly four square roots modulo `2^n`; a nonzero quadratic residue has exactly two roots modulo `5^n`. CRT combines the choices into exactly eight roots modulo `10^n`. □

**Important limitation:** We classify **odd-ending words only**. Other words ending in 4 can also be squares modulo `10^n`; this theorem does not exclude or enumerate them. Being a square modulo `10^n` does not imply being an ordinary integer square.

## Theorem B: exponentially many local squares at *every sufficiently large length*

Fix an arbitrary positive integer `M` and write

```
M = 2^a * 5^b * m, gcd(m, 10)=1.
```

If `m=1`, for **every** `n>=3`, all `3^(n-3)` length-n words ending in 441 are quadratic residues modulo M.

If `m>1`, let `h = ord_m(10)`, and define the explicit integer

```
T = floor((m+13)/3).
```

For **every**

```
n >= 4 + (T-1)*h,
```

there exist **at least `3^(n-3-T)` distinct n-digit integers W**, all digits in `{1,4,9}`, all ending in 441, such that W is a square modulo M.

In fact, W can be chosen divisible by m, while its 2- and 5-primary quadratic-residue conditions hold automatically.

### Proof and explicit algorithm

The key elementary coin lemma is that **every integer r>=14 can be expressed as r=3u+8v with u,v nonnegative integers and u+v<=r/3**. Take `v` to be the unique integer in `{0,1,2}` satisfying `2v ≡ r (mod 3)` (since 8 is 2 modulo 3), and `u=(r-8v)/3`. Then u is nonnegative (the cases r=14 and r=15 can be checked directly; for r>=16 this is automatic), and `u+v=(r-5v)/3<=r/3`.

Reserve the T decimal positions (indexed from the units digit)

```
E = {3, 3+h, 3+2h, ..., 3+(T-1)h}.
```

The length bound guarantees these are all among positions `3,...,n-1` (outside the final 441), and `10^e ≡ 10^3 (mod m)` for every reserved position e.

Assign *arbitrarily* one digit from `{1,4,9}` to each of the other `n-3-T` higher positions. Initialize each reserved digit to 1 and keep the final three digits as 441, obtaining a baseline word `W_0`.

Because 10 is invertible modulo m, choose the unique residue `z` satisfying

```
z ≡ -W_0 * (10^3)^(-1)   (mod m), 0<=z<m.
```

Choose the unique integer r in `[14,m+13]` congruent to z modulo m:

```
r = 14 + ((z-14) mod m).
v = (2*r) mod 3,         u = (r-8*v)/3.
```

The coin lemma guarantees `3u+8v=r ≡ z (mod m)`, with `u+v<=floor((m+13)/3)=T`. Change u reserved digits from 1 to 4 and v others from 1 to 9. Each change adds `3*10^e` or `8*10^e`, and therefore

```
W ≡ W_0 + (3u+8v)*10^3 ≡ 0 (mod m).
```

Because the final three digits remain 441, W is 1 modulo 8 and 1 modulo 5. It follows that W is a square modulo every `2^a` and `5^b`. Since W is zero modulo m, it is also a square modulo m. CRT proves that it is a square modulo M.

Two different assignments to the nonreserved positions give different final integers, so all `3^(n-3-T)` constructed integers are distinct. The `m=1` case follows directly from the final-441 condition. □

**Quantitative improvement.** The first construction reserved 2m slots; using the elementary coin lemma reduces this to `T=floor((m+13)/3)`, approximately m/3 slots, and correspondingly improves both the explicit length threshold and the count of available words.

### Consequences

**Fixed finite sets of moduli are even weaker than they appear.** Given *any* finitely many positive moduli `M_1,...,M_t`, replace M by their least common multiple. For all sufficiently large n there are exponentially many n-digit `{1,4,9}` words passing *all* quadratic-residue tests modulo every `M_j` simultaneously. This is stronger than exhibiting one periodic family that passes tests only along an infinite subsequence of lengths.

**Even growing decimal moduli do not resolve the global problem.** From Theorem A, for *every* n>=3 there are `2*3^(n-3)` odd `{1,4,9}` n-digit numbers which are squares modulo `10^n`, a modulus itself growing exponentially with n. They need not be genuine integer squares. The obstruction to genuine squares is that a square root representative must be small enough that its square agrees with W as an integer, not just modulo `10^n`.

If `0<=x<10^(n/2)` and `0<=W<10^n`, then `x^2≡W (mod 10^n)` implies `x^2=W`. The local congruences alone provide roots modulo `10^n`, but do *not* guarantee that any root lies in this restricted real interval.

**This remains a negative methodological result, not progress on the finiteness conjecture itself.** To decide whether true A006716 squares extend arbitrarily far, one needs a genuinely global restriction or a construction that selects an appropriately bounded root.

## Verification

```sh
python papers/A006716/verify_local_sieve.py
```

The verifier enumerates all `{1,4,9}` words and all square residues modulo `10^n` for n=3,4,5, confirms the exact unit classification and eight-root count, and independently audits the constructive fixed-modulus theorem for M=1,...,100. The general assertions above follow from the proofs, not from extrapolation of these finite tests.

References: OEIS [A006716](https://oeis.org/A006716); standard criteria for quadratic residues of units modulo `2^n` and `5^n`; elementary multiplicative order and the Chinese remainder theorem.
