# A006716: support-15 classification and a new leading-three-digit gap theorem

**Research note, 2026-10-22.** Qichao Wang (Hebei University of Technology) and Daoyu Dong (University of Electronic Science and Technology of China). Research-only supplement; manuscripts and PDF files unchanged. No claim to prove the finiteness of A006716.

## 1. Complete root-support-15 classification

**Theorem (finite exhaustive certificate).** If x is a positive integer whose decimal square x² contains only the digits 1,4,9, and x has at most **15 nonzero decimal digits**, then x is one of the 17 already-listed roots in [OEIS A027675](https://oeis.org/A027675). In particular, **there is no solution with exactly 15 nonzero decimal digits**.

The exact-integer enumeration uses the proven low digit gap `e_(j+1) <= 2e_j+2`, the final high gap `e_r <= e_(r-1)+3`, sound decimal suffix conditions, and the independently certified high-pair mask in [verify_leading_pairs.py](verify_leading_pairs.py). Every branch is limited by a necessary, rigorously proved condition; no absolute numerical bound on x is imposed.

Six disjoint units-digit shards of [verify_sparse_roots_15.cpp](verify_sparse_roots_15.cpp) were exhaustively evaluated:

| units digit of root | final candidate roots checked | matching roots |
|---:|---:|---:|
| 1 | 49,279,049 | none |
| 2 | 31,005,983 | none |
| 3 | 26,618,526 | none |
| 7 | 109,344,650 | none |
| 8 | 51,037,871 | none |
| 9 | 29,875,589 | none |
| **Total** | **297,161,668** | **none** |

All six jobs passed on the [GitHub Actions run](https://github.com/dongxuelian2/oeis-papers/actions/runs/39760234703). The certificate pins these independent expected leaf counts and rejects any unlisted integer root. Combine this with the earlier complete support <=14 results in [LEADING_PAIRS_AND_SUPPORT14.md](LEADING_PAIRS_AND_SUPPORT14.md).

## 2. A new global restriction on the highest three nonzero root digits

**Theorem (top-three gap restriction).** Suppose x has at least three nonzero decimal digits, and every decimal digit of x² belongs to {1,4,9}. Let

```
e > p > q
```

be the three **highest** nonzero positions of x (units position 0). Set `g=e-p`, `h=p-q`. Then

```
g=1 => h<=3,
g=2 => h<=4,
g=3 => h=1.
```

Equivalently,

\[
\boxed{(e-p,p-q)\in
\{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1)\}.}
\]

**Proof.** The previous top-gap theorem forces `g<=3`. Let the highest two nonzero root digits be a and b, at positions e and p. If the third-highest nonzero root digit is at q with `h=p-q>=T`, then all lower digits combined are smaller than `10^(p-T+1)`. On dividing by `10^e` we obtain an exact enclosure:

\[
a+\frac b{10^g}\le \frac{x}{10^e}
<a+\frac b{10^g}+\frac{1}{10^{g+T-1}}.
\]

Writing `D=10^(g+T-1)` and `z=aD+b*10^(T-1)`, this means

\[
\frac{z^2}{D^2}\le\frac{x^2}{10^{2e}}<
\frac{(z+1)^2}{D^2}.
\]

When x² has at least eight digits, the normalized square in the middle lies in [1,100), and its *first eight significant digits* must be one of the 3^8 words from {1,4,9}. **For squares shorter than eight digits, the eight-digit-prefix argument is not applicable; the finite exceptional range x<=3162 is separately exhausted below.** Consequently the middle interval must intersect one of the finite intervals

\[
\left[\frac{P}{10^{8-j}},\frac{P+1}{10^{8-j}}\right),
\qquad j\in\{1,2\},
\]

where P runs over all 3^8 permitted eight-digit prefixes. All interval endpoints are rational. Intersection is possible **only if** both strict integer inequalities hold:

```
z^2*10^8 < (P+1)*10^j*D^2,
(z+1)^2*10^8 > P*10^j*D^2.
```

For each of the three threshold pairs `(g,T)=(1,4),(2,5),(3,2)`, the [independent exact Python audit](verify_top_three_gaps.py) checks all 81 pairs `1<=a,b<=9` and all `2*3^8` possible eight-digit prefix intervals; **every intersection is empty**. Therefore `g=1` excludes h>=4, `g=2` excludes h>=5 and `g=3` excludes h>=2. These are the asserted bounds for x² having at least eight decimal digits. If x² has fewer than eight digits then 1<=x<=3162. Exhausting these 3162 roots directly (using the same exact digit criterion) shows the **only** one with three or more nonzero root digits is x=212, with x²=44944 and (e-p,p-q)=(1,1), which is permitted. This finite check is included in [verify_top_three_gaps.py](verify_top_three_gaps.py). The theorem therefore holds for every x with at least three nonzero digits. QED.

**Scope:** The theorem applies to *every* A006716 integer square root having at least three nonzero digits, regardless of total length or support. It is a purely mathematical necessary condition involving the real magnitude of x² (the eight leading digits), not merely modular arithmetic.

The same inequalities can generate a more selective **top-three digit** mask for future higher-support exact searches, to avoid testing most final square-root candidates.

## 3. Research limits

The A006716 finiteness conjecture is still unresolved. The bounded-support result now excludes r=15 but cannot rule out the existence of roots with r>=16. The top-three-digit theorem provides an independent global restriction, and its proof is separate from the finite enumeration.

Reproduce:

```sh
python papers/A006716/verify_top_three_gaps.py
g++ -std=c++17 -O3 papers/A006716/verify_sparse_roots_15.cpp -o /tmp/a006716_r15
for u in 1 2 3 7 8 9; do /tmp/a006716_r15 "$u"; done
```
