# A006716: universal bound of seven on the fourth-highest root gap

Authors: Qichao Wang (Hebei University of Technology); Daoyu Dong (University of Electronic Science and Technology of China). Research-only note, October 22, 2026. This is a theorem about *necessary* decimal structure, not a proof of A006716 finiteness.

## Theorem

Let x>0 be an integer with at least four nonzero decimal digits and assume **every decimal digit of x² lies in {1,4,9}**. Let the highest four nonzero root positions be

\[
e>p>q>s.
\]

Then

\[
\boxed{q-s\le7.}
\]

This bound is **independent of x, the total number of nonzero root digits, and the digit length of x²**.

## Proof

Put `g=e-p`, `h=p-q`, `t=q-s`. The [top-three gap theorem](SUPPORT15_TOP_THREE.md), itself proved with exact eight-digit prefix intervals, gives

```
(g,h) in {(1,1),(1,2),(1,3),(2,1),
          (2,2),(2,3),(2,4),(3,1)}.
```

The [independent global upper-span zero-gap lemma](GLOBAL_HIGH_GAP.md) gives

\[
t\le g+h+3.
\]

It is therefore enough to check finitely many possibilities:
`g∈{1,2,3}`, `h∈{1,2,3,4}`, the eight allowed pairs, and `1<=t<=g+h+3`.

Assume first that x² has **at least ten digits**. Write the four highest nonzero root digits as `a,b,c,d∈{1,...,9}`, occurring at `e,p,q,s`. Because all omitted lower root digits lie below `s`, we have the exact rational enclosure

\[
\frac zD\le\frac{x}{10^e}<\frac{z+1}D,
\quad D=10^{g+h+t},\quad
z=aD+b10^{h+t}+c10^t+d.
\]

Squaring produces `[z²/D²,(z+1)²/D²)` as a necessary enclosure for `x²/10^(2e)`. Since x² has at least ten digits and contains only 1,4,9, this interval **must intersect** one of the intervals

\[
\left[\frac{P}{10^{10-j}},\frac{P+1}{10^{10-j}}\right),
\quad j\in\{1,2\},\quad
P\in\{1,4,9\}^{10}.
\]

These are exact rational inequalities. For each `(g,h,t)` and `a,b,c,d`, the independent verifier [verify_top_four_gaps.py](verify_top_four_gaps.py) tests the interval intersection *without floating-point arithmetic*.

The resulting counts of allowed ordered digit quadruples are:

| (g,h) | counts at t=1,2,...,g+h+3 |
|---|---|
| (1,1) | 129,32,6,4,0 |
| (1,2) | 65,20,0,0,0,0 |
| (1,3) | 34,5,3,0,0,0,0 |
| (2,1) | 119,48,18,0,0,0 |
| (2,2) | 22,13,4,5,0,7,9 |
| (2,3) | 17,3,0,0,0,0,0,0 |
| (2,4) | 12,2,4,0,0,0,0,0,0 |
| (3,1) | 12,10,0,0,0,0,0 |

**Every candidate with `t>=8` is excluded**. Some configurations with `t=7` remain, so the ten-digit test does not prove a better bound.

If x² has **fewer than ten digits**, then `1<=x<=31622`. This finite range is exhausted independently by the same verifier using exact integer squaring; the only root with four or more nonzero digits whose square has only 1,4,9 is `x=31488`, with `x²=991494144` and `q-s=1`. Hence the bound also holds for every short-square case.

Both cases establish `q-s<=7`. □

## Application and limitations

Combined with the existing top-three gap table, this provides an *all-index, global, non-modular* necessary constraint on the leading **four** nonzero digits of any future A006716 square root. It can be used for sound early pruning of the support-17 search and all subsequent support classes.

It does not prove existence or nonexistence of arbitrarily large A006716 square roots. The finite classification currently proved separately is for root support at most 16; the support-17 search is maintained as an independent exact computation. The original A087354 manuscript and all PDFs are left unchanged.

To reproduce:

```sh
python papers/A006716/verify_top_four_gaps.py
```
