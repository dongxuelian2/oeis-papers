# A006716: fifth-highest nonzero root gap is at most 5

Research note, 2026-10-22. This is a universal necessary condition on ordinary integer squares with digits restricted to 1,4,9; it is not a finiteness proof.

## Theorem

If a positive integer x has at least five nonzero decimal digits and every decimal digit of x² is in {1,4,9}, then its five highest nonzero positions e1>e2>e3>e4>e5 satisfy

\[
\boxed{e_4-e_5\le5.}
\]

There is no restriction on the root's total size or support count.

## Proof

Put g=e1-e2, h=e2-e3, t=e3-e4 and u=e4-e5. The previously established top-three theorem restricts (g,h) to

(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (2,4), (3,1).

The top-four theorem gives t<=7, and the universal upper-span gap lemma gives t<=g+h+3 and u<=g+h+t+3.

Let a,b,c,d be the four highest nonzero root digits and define

\[
D=10^{g+h+t},\quad z=aD+b10^{h+t}+c10^t+d.
\]

The exact enclosure for the normalized root is

\[
z/D\le x/10^{e_1}<(z+1)/D.
\]

Requiring that the first TEN decimal digits of its square belong to {1,4,9} leaves exactly 603 possible configurations (g,h,t,a,b,c,d). These are enumerated independently using integer-only digit-DP prefix interval tests in [verify_top_five_gaps.py](verify_top_five_gaps.py).

If the fifth root gap is u, all remaining root digits contribute less than 10^(e4-u+1). Therefore the **sharper exact enclosure** is

\[
\frac{z10^{u-1}}{D10^{u-1}}\le
\frac{x}{10^{e_1}}<
\frac{z10^{u-1}+1}{D10^{u-1}}.
\]

For all 1<=u<=g+h+t+3, the square of this interval must intersect an interval corresponding to a permitted 14-digit square prefix. All interval intersections are computed by exact integer divisions and a digit-DP successor algorithm. The numbers of surviving configurations for each fifth gap are:

| u | Surviving top-four configurations |
|---:|---:|
| 1 | 593 |
| 2 | 179 |
| 3 | 49 |
| 4 | 8 |
| 5 | 2 |
| >=6 | 0 |

At u=5, the only remaining cases are (g,h,t,a,b,c,d)=(2,1,1,7,2,9,9) and (2,1,3,3,7,4,3). Thus u>=6 is excluded for every square with at least 14 digits.

Finally, a square with fewer than 14 digits has root at most floor(sqrt(10^13-1))=3,162,277. The same independent verifier exhausts all these roots using exact integer multiplication; the only acceptable roots with support at least five are 31488 and 387288, each with u=1. This establishes the theorem for all sizes. QED.

## Exact prefix-intersection lemma

For normalized squared interval [z²/D²,(z+1)²/D²), one of the permitted K-digit leading-square words P over {1,4,9} must produce an interval [P*10^(j-K),(P+1)*10^(j-K)), where j=1 or 2.

A necessary and sufficient test for intersection is that the integer interval

\[
\left[
\left\lfloor\frac{z^2 10^{K-j}}{D^2}\right\rfloor,\;
\left\lceil\frac{(z+1)^2 10^{K-j}}{D^2}\right\rceil-1
\right]
\]

contain at least one K-digit integer formed from 1,4,9. The verifier obtains the least allowed K-digit integer at least the left endpoint using exact digit dynamic programming and checks it against the right endpoint. No approximation or floating-point computation is required.

## Meaning and limitations

This is a support-independent *necessary* restriction. It strengthens the previously proved fourth-highest gap bound of 7 and the upper-span lemma, and it can be used as an exact pruning rule for r=18 and later root-support searches. It does not discover a new OEIS term or settle the A006716 finiteness conjecture. Original TeX/PDF files remain unchanged.

Reproduction command:

    python papers/A006716/verify_top_five_gaps.py
