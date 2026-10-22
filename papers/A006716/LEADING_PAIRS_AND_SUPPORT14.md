# A006716: exact leading-pair interval certificate and support-14 classification

**Status, October 22, 2026.** Research note by Qichao Wang (Hebei University of Technology) and Daoyu Dong (University of Electronic Science and Technology of China). This certifies a *bounded root-support* classification, not finiteness of OEIS A006716. No priority over earlier OEIS numerical searches is claimed.

## 1. Rigorous six-digit leading-prefix restriction

Let `x` be a positive integer with at least two nonzero decimal digits and whose square has only digits `1,4,9`. Suppose its highest two nonzero decimal digits are `a` and `c` at positions `e>p`, and write `g=e-p`. The previously proved high-gap lemma gives `g<=3`.

We restrict to `x^2` of at least six digits (automatically true when its square root has at least 6 nonzero decimal digits).

Writing `x=a*10^e+t`, the second highest digit gives the **exact rational bounds**

```
a + c/10^g <= x/10^e < a + (c+1)/10^g.
```

Set `A=a*10^g+c`. Squaring gives

```
A^2/10^(2g) <= x^2/10^(2e) < (A+1)^2/10^(2g).
```

Because `x<10^(e+1)`, the normalized square lies below 100. If its first six significant digits form the integer `P`, then `P` is one of the `3^6` six-digit words over `{1,4,9}`. For `j=1` or `2` digits before the decimal point in the normalized square, the allowed prefix interval is

```
[P*10^(j-6), (P+1)*10^(j-6)).
```

Intersection between the two rational intervals is a **necessary** condition. It can be decided exactly, without a square root or floating point, by the two strict integer inequalities

```
A^2*10^(6-j) < (P+1)*10^(2g),
(A+1)^2*10^(6-j) > P*10^(2g).
```

Checking all `P` and both values of `j` leaves precisely the following permissible ordered pairs `(a,c)`:

| g | a (highest root digit) | Permissible c (next highest nonzero root digit) |
|---|---|---|
| 1 | 1 | 1,2,3,4 |
| 1 | 2 | 1,2 |
| 1 | 3 | 1,3,4,7,8 |
| 1 | 4 | 3,4 |
| 1 | 6 | 4,6,7 |
| 1 | 9 | 5,7,9 |
| 2 | 1 | 5,6,7,9 |
| 2 | 2 | 2,3,4 |
| 2 | 3 | 1,2,3,6,7,8 |
| 2 | 7 | 1,2,3,6,7 |
| 3 | 7 | **7,8** |

Every pair not listed is ruled out by the first six square digits **before examining any other root digits**. The case `g=3` notably forces `a=7` and `c in {7,8}`, strengthening the earlier high-gap lemma (which only gave `c>=7`).

This table is recomputed from scratch by [verify_leading_pairs.py](verify_leading_pairs.py), with **243 exact integer interval checks**. The table yields only **necessary conditions**: a permitted pair need not extend to a true integer square.

## 2. Complete classification through 14 nonzero root digits

**Theorem (computer-certified finite classification).** Let `nu_10(x)` be the number of nonzero decimal digits of a positive integer x. Then:

```
{x>0 : every digit of x^2 belongs to {1,4,9}, nu_10(x)<=14}
=
{1,2,3,7,12,21,38,107,212,31488,70107,387288,95610729,
 446653271,3148717107,21081079479,648070211589107021}.
```

In particular **the unique root with exactly 14 nonzero digits** is

```
648070211589107021,
whose square is 419994999149149944149149944191494441.
```

These are all the **17 previously known** A006716 roots (see its companion [OEIS A027675](https://oeis.org/A027675)). This result **does not** prove the global sequence finite: there might exist valid roots with 15 or more nonzero digits.

### Complete exhaustive certificate

The verified digit-gap bounds from [SPARSE_ROOTS.md](SPARSE_ROOTS.md) imply for root support `r=14`:

1. The units digit is one of `1,2,3,7,8,9`. The other digits give prohibited final square digits.
2. Every successive nonzero exponent `e_{j+1}` is at most `2e_j+2`.
3. For the final nonzero exponent, `e_14<=e_13+3`.
4. Given a partial root `x_j`, before adding the next root digit at exponent `e`, all digits of `x_j^2 mod 10^e` must already lie in `{1,4,9}`. No future increment divisible by `10^e` can change this remainder.
5. **Only when adding the final leading root digit**, apply the leading-pair table of section 1. It is not valid to apply that condition to an earlier, extendible prefix.
6. Every surviving complete root is squared using exact Boost.Multiprecision integers; all digits are checked. No arbitrary root magnitude bound is used.

This defines a finite, exhaustive tree. The six disjoint units-digit runs have the following final-leaf counts, **after the leading-pair sieve**:

| root units digit | complete candidate roots | accepted roots |
|---|---:|---:|
| 1 | 12,777,251 | 648070211589107021 |
| 2 | 8,035,316 | none |
| 3 | 6,905,447 | none |
| 7 | 28,348,050 | none |
| 8 | 13,228,782 | none |
| 9 | 7,748,312 | none |
| **Total** | **77,043,158** | **one** |

The program [verify_sparse_roots_14.cpp](verify_sparse_roots_14.cpp) accepts a units digit argument and checks the corresponding exact leaf count **and the complete set of successful roots**. The six runs can execute independently, in parallel. The [verify_leading_pairs.py](verify_leading_pairs.py) proof audit prevents an incorrect lookup table from silently excluding roots. The earlier [verify_sparse_roots_13.cpp](verify_sparse_roots_13.cpp) certifies all roots with 13 nonzero digits (none), and [verify_sparse_roots.cpp](verify_sparse_roots.cpp) covers 1 through 12 (16 accepted).

### Run

```sh
python papers/A006716/verify_leading_pairs.py
g++ -std=c++17 -O3 papers/A006716/verify_sparse_roots_14.cpp -o /tmp/a006716_r14
for u in 1 2 3 7 8 9; do /tmp/a006716_r14 "$u"; done
```

The GitHub Actions workflow `.github/workflows/a006716-support14.yml` runs each units-digit shard as a separate job.

## 3. Mathematical limitation

The result is a complete structural classification only **up to a fixed number of nonzero digits in the root**. A proof that there are finitely many such squares altogether must obtain a support-independent obstruction. Pushing the cutoff from 14 to 15 without stronger mathematics would be another finite computational step, not a solution to the conjecture.

The original A087354 TeX/PDF manuscripts and the A006716-related prior research papers have not been modified as part of this computation.
