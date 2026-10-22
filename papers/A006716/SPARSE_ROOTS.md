# A006716: complete classification of roots with at most 17 nonzero digits

**Authors:** Qichao Wang (Hebei University of Technology); Daoyu Dong (University of Electronic Science and Technology of China).

**Status:** A global, finite-certificate result for a precisely defined infinite class of roots. The theorem does **not** settle whether all of OEIS [A006716](https://oeis.org/A006716) is finite, and literature priority is not claimed. This independent research note does not change the existing paper or PDF.

## Theorem 1: decimal gap restriction on the square root

Suppose the *positive integer square* \(x^2\) has no decimal digit zero. Write the nonzero decimal positions of \(x\) as

\[
0=e_1<e_2<\cdots<e_r
\]

and its corresponding nonzero digits as \(c_i\in\{1,\ldots,9\}\).

Then

\[
\boxed{e_{j+1}\le 2e_j+2\quad(1\le j<r),\qquad e_r\le 2^r-2.}
\]

**Proof.** Because \(x^2\) has no zero digit (indeed, all A006716 digits are 1, 4 or 9), \(x\) cannot be divisible by 10, so \(e_1=0\). For consecutive nonzero positions \(e_j<e_{j+1}\), write

\[
x=t+10^{e_{j+1}}h,\qquad
0<t<10^{e_j+1}.
\]

The digits in positions between \(e_j+1\) and \(e_{j+1}-1\) in the root vanish. Therefore

\[
x^2\equiv t^2\pmod{10^{e_{j+1}}}.
\]

If \(e_{j+1}>2e_j+2\), then \(t^2<10^{2e_j+2}\), so the digit of \(x^2\) in position \(2e_j+2\) is zero. That position is below \(e_{j+1}\) and below the length of \(x^2\), a contradiction. Thus \(e_{j+1}\le2e_j+2\). Starting with \(e_1=0\), induction gives \(e_r\le2^r-2\). □

**Global consequence:** for every fixed integer \(r\), only finitely many A006716 squares can have a square root with at most \(r\) nonzero decimal digits. This is a genuine integer-square obstruction, not a modular-residue test. It excludes all arbitrarily spaced sparse-root patterns with bounded support size.


## Theorem 1b: an independent leading-square zero-gap obstruction

If an integer \`x\` with at least two nonzero decimal digits has zero-free square \`x^2\`, and the two *highest* nonzero decimal positions of \`x\` are \`p<e\`, then

\[
\boxed{e\le p+3.}
\]

**Proof.** Write \`x=a*10^e+t\`, with \`1<=a<=9\` and \`0<t<10^(p+1)\`. Suppose \`e>=p+4\`, so \`t<10^(e-3)\`. The part of the square below \`a^2*10^(2e)\` is

\[
C=2at10^e+t^2
 < 18\cdot10^{2e-3}+10^{2e-6}
 <10^{2e-1}.
\]

Thus the decimal digit of \`x^2\` in position \`2e-1\` is zero: the high term starts at position \`2e\`, while \`C\` is too small to reach position \`2e-1\`. This contradicts zero-freeness. □

The certificate uses this **additional necessary condition only when choosing the final (highest) nonzero digit of the root**. Applying it earlier to an intermediate partial root would not be justified, because later added high digits could change that square.

## Theorem 1c: gap-three leading-digit rigidity

The top-gap bound admits a sharper structural refinement. Suppose a positive
integer \(x\) has at least two nonzero decimal digits, its two highest nonzero
positions are \(p<e\), and \(e=p+3\). If **every digit of \(x^2\)** belongs to
\(\{1,4,9\}\), then:

\[
\boxed{\text{The leading digit of }x\text{ is }7,\quad
\text{the next nonzero digit is at least }7,\quad
x^2\text{ begins with }491.}
\]

**Proof.** Write \(x=a10^e+t\), with \(1\le a\le9\) and
\(0<t<10^{p+1}=10^{e-2}\). The remainder in the square is

\[
C=2at10^e+t^2<18\cdot10^{2e-2}+10^{2e-4}<10^{2e}.
\]

Hence \(a^2\) supplies the leading one or two digits of \(x^2\), with
no carry from \(C\) into position \(2e\). Among \(1^2,\ldots,9^2\),
only \(a=1,2,3,7\) give leading digits exclusively in \(\{1,4,9\}\).
If \(a\le3\), then \(C<6\cdot10^{2e-2}+10^{2e-4}<10^{2e-1}\),
so the digit in position \(2e-1\) is zero, a contradiction.
Thus \(a=7\).

Now \(C<14\cdot10^{2e-2}+10^{2e-4}<2\cdot10^{2e-1}\).
Since the digit at position \(2e-1\) is nonzero, it must be \(1\).
The two preceding digits are \(49\), hence the square begins with
\(491\).

Finally, if the next nonzero root digit were at most 6, then
\(t<7\cdot10^{e-3}\). This would imply

\[
C<98\cdot10^{2e-3}+49\cdot10^{2e-6}
<10^{2e-1},
\]

again forcing a zero. Therefore the next nonzero root digit is at
least 7. \(\square\)

This is a **necessary** leading-pattern restriction, not an
impossibility theorem for the gap-three case. Its validity does not
depend on the support bound \(r\le13\).

## Theorem 2: independent digit-sum bound

Let \(s_{10}(x)\) be the sum of the decimal digits of \(x\), and let \(\nu_{10}(x)\) be the number of its nonzero digits. If \(x^2\) is an \(n\)-digit member of A006716 and \(\nu_{10}(x)=r\), then

\[
\boxed{n\le s_{10}(x)^2\le81r^2,\quad
r\ge\left\lceil\frac{\sqrt n}{9}\right\rceil.}
\]

Indeed, the usual carry operation in base 10 cannot increase digit sum. Expanding the product of the two decimal digit polynomials yields the standard inequality \(s_{10}(ab)\le s_{10}(a)s_{10}(b)\), so \(s_{10}(x^2)\le s_{10}(x)^2\). As every output digit is at least one, \(n\le s_{10}(x^2)\), while \(s_{10}(x)\le9r\). □

This proves an asymptotic lower bound on root digit density (at least order \(\sqrt n\) nonzero root digits). The gap theorem gives sharper structural bounds for small fixed \(r\).

## Theorem 3: complete sparse-root classification through support 13

**Claim (finite, machine-verifiable certificate):** If \(x^2\) has only digits in \(\{1,4,9\}\) and \(x\) has **at most 13 nonzero decimal digits**, then and only then \(x\) belongs to the following list.

| \(\nu_{10}(x)\) | All possible integer roots \(x\) |
|---:|---|
| 1 | 1, 2, 3, 7 |
| 2 | 12, 21, 38, 107 |
| 3 | 212, 70107 |
| 4 | **none** |
| 5 | 31488 |
| 6 | 387288 |
| 7 | 95610729 |
| 8 | **none** |
| 9 | 446653271, 3148717107, 21081079479 |
| 10 | **none** |
| 11 | **none** |
| 12 | **none** |
| 13 | **none** |

Thus this infinite class of roots yields **exactly 16 distinct A006716 squares**. All correspond to already recorded OEIS terms; this is a *new form of completeness certificate for the bounded-root-support problem*, not discovery of new sequence terms.

### Why the exhaustive calculation is globally complete

For a root with exactly \(r\) nonzero digits, its least significant digit must be nonzero, and every next nonzero position must satisfy Theorem 1. This produces a *finite* tree of positional supports, regardless of root magnitude, with maximum position \(2^r-2\).

At a partial root \(t=\sum_{i=1}^j c_i10^{e_i}\), before adding a higher digit at exponent \(e\), every decimal digit of \(t^2\bmod10^e\) must lie in \(\{1,4,9\}\). That is because all subsequent root terms start at position \(e\) or higher, so they cannot change any digit of the square **below** position \(e\).

The verifier checks this necessary condition using exact integer arithmetic and prunes only a subtree whose low square digits are already invalid. When the chosen support reaches \(r\), it tests every digit of the **entire** exact integer square.

Accordingly the pruning is sound, the support bound exhausts all roots for the stated \(r\), and no assumption that the root is numerically small is used.

**Exact search audit:** for \(r=11\), the finite search visits 6,319,638 complete candidate roots after low-digit pruning and finds no square. Smaller depths are independently checked by the same verifier. For support 12, an additional **top-gap lemma** below restricts the final nonzero position and leaves 23,707,917 exact integer candidate roots, none of which passes the digit test. A second Python search explicitly enumerates and verifies the complete \(r\le4\) classification (171 candidates with \(r\le2\), 269,001 raw four-digit-support candidates).


### Support 13: independently recertified and excluded

A separate exact-integer C++ certificate, [verify_sparse_roots_13.cpp](verify_sparse_roots_13.cpp), again enumerates support 12 (agreeing on precisely **23,707,917** terminal candidates and no solution), then exhausts support 13, yielding precisely **91,475,739** terminal candidate roots and **no** admissible square. Both checks use the same logically necessary low-digit and final high-gap constraints as the original implementation, but check the fixed lower square digits by a decimal-string prefix test rather than divisions by large powers of 10. Every accepted terminal state is checked as an exact integer square; no floating-point arithmetic is used. The computation does **not** put an arbitrary upper limit on the size or length of the root. The mathematical completeness comes from Theorem 1 and Theorem 1b.

It follows that the **complete classification through 13 nonzero root digits still contains exactly the 16 roots in the table above**, and every A006716 square not already accounted for in these 16 values must have a square root with at least 14 nonzero digits. This lower bound is attained by the previously known value

\[
648070211589107021^2
=419994999149149944149149944191494441,
\]

whose root has exactly 14 nonzero decimal digits.

**Additional absolute digit-length bound.** Writing \(n=\operatorname{digits}(x^2)\), the low-gap theorem gives \(e_r\le2^r-2\). As \(x<10^{e_r+1}\), we obtain

\[
\boxed{n\le\min\{81r^2,\;2^{r+1}-2\}.}
\]

This is an inequality for genuine zero-free squares, not a statistical observation. The quadratic bound dominates asymptotically; the exponential bound can be stronger for smaller \(r\).

The [completed support-14 classification](LEADING_PAIRS_AND_SUPPORT14.md) now proves the **only** 14-sparse solution is the previously known `648070211589107021`. The supporting [C++ verifier](verify_sparse_roots_14.cpp) exhausts all possible root units-digit classes, with the high-pair sieve itself independently checked by [Python](verify_leading_pairs.py). It tests exactly **77,043,158** surviving complete roots across all six units classes.



### Support 14: unique solution and exact leading-pair sieve

The [complete support-14 note](LEADING_PAIRS_AND_SUPPORT14.md) derives a six-significant-digit high-prefix restriction by exact rational interval intersection. A separate small [Python audit](verify_leading_pairs.py) checks all 243 possible combinations of the three leading root-digit gaps and two high digits. In particular, if the top two nonzero root positions are separated by three, the top two digits must be **7 followed by 7 or 8**. This improves Theorem 1c.

Combining this with Theorems 1 and 1b gives a complete 6-way exact-root computation (root units digits 1,2,3,7,8,9), covering **77,043,158 terminal candidates** after high-prefix pruning. The only successful square root is

\[
\boxed{x=648070211589107021,\quad
x^2=419994999149149944149149944191494441}.
\]

Thus **all A006716 square roots with at most 14 nonzero decimal digits** are exactly the **17 terms** already listed in OEIS A027675; the classification has no arbitrary numerical search bound. The next case \(r=15\) is separately certified in [SUPPORT15_TOP_THREE.md](SUPPORT15_TOP_THREE.md); the full finiteness problem remains open.

Reproduce with

```sh
python papers/A006716/verify_leading_pairs.py
g++ -std=c++17 -O3 papers/A006716/verify_sparse_roots_14.cpp -o /tmp/a006716_r14
for u in 1 2 3 7 8 9; do /tmp/a006716_r14 "$u"; done
```


### Reproduce

```sh
g++ -std=c++17 -O3 papers/A006716/verify_sparse_roots.cpp -o /tmp/a006716_sparse
/tmp/a006716_sparse
g++ -std=c++17 -O3 papers/A006716/verify_sparse_roots_13.cpp -o /tmp/a006716_sparse13
/tmp/a006716_sparse13
python papers/A006716/verify_sparse_roots.py
```

The C++ certificate relies on Boost.Multiprecision arbitrary-precision *integer* arithmetic; it does not use floating point or probabilistic tests.

### Limitation and significance

The theorem rules out every **bounded-support** strategy for constructing infinitely many A006716 squares, including irregular, nonperiodic distributions of nonzero root digits. It does not bound the number of nonzero root digits in the general conjecture, and so does **not** prove A006716 finite. The known 36-digit term has the unique 14-sparse root `648070211589107021`, included by the new support-14 classification. The general problem for roots with **18 or more nonzero digits** remains open.

The digit-sum inequality itself is standard. The computation is a self-contained classification for this particular digit set, not a claim of priority over OEIS computational literature.

### Support 15: rigorous exclusion and further global top-three bounds

The [support-15 certificate and top-three theorem](SUPPORT15_TOP_THREE.md) exhausts all six possible root units digits, visits **297,161,668 final candidates** using only exact arithmetic, and finds **no** square. Thus the complete classification for square roots with **at most 15 nonzero decimal digits** remains precisely the **17 previously known OEIS roots**, with no artificial size cutoff.

The new **highest-three-nonzero-digit gap theorem** shows that if the highest positions are `e>p>q`, then `(e-p,p-q)` must lie in `{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1)}`. An [independent exact-rational audit](verify_top_three_gaps.py) excludes larger gaps by exhaustively checking the first 8 significant digits. This theorem holds for arbitrary support and supplies further pruning for future searches.

### Support 16: full classification with an exact triple-prefix mask

The new [support-16 certificate and proof note](SUPPORT16.md) classifies all roots with **exactly 16 nonzero decimal digits**: **zero solutions**, after **268,308,611 final candidates** across the six possible units digits. The new [C++ exact verifier](verify_sparse_roots_16.cpp) derives an independent high-three-digit prefix mask with exact integer interval arithmetic, rigorously bounds the highest root exponent by the digit-sum inequality, and prunes prefixes only when no future valid square can extend them. The [independent Python audit](verify_top_three_gaps.py) checks all high-three-digit masks and the short-square cases where an eight-digit-prefix test would not apply.

**Combining all certified supports r<=16, exactly the 17 previously known roots occur.** Support r>=18 and global finiteness are open. The [six-shard CI run](https://github.com/dongxuelian2/oeis-papers/actions/runs/39762036098) passed. No original TeX or PDF was changed.

### Support 17: complete classification and new universal gap bounds

The [support-17 certificate](SUPPORT17.md) excludes **all roots with exactly 17 nonzero decimal digits** by a six-shard complete exact-integer search of **1,034,989,170 terminal candidate roots**, finding no solutions. The [GitHub Actions run](https://github.com/dongxuelian2/oeis-papers/actions/runs/39764490169) passed all six shards. Thus the exact classification of **all A006716 square roots with support r<=17** still yields exactly the **17 previously known roots**. The new [global upper-span lemma](GLOBAL_HIGH_GAP.md) and [top-four-gap theorem](TOP_FOUR_GAP.md) prove independent, all-length necessary constraints for future support classes; the latter restricts the fourth-highest nonzero root position gap to **at most 7**. Root support r>=18 and global finiteness remain unresolved.
