# A006716: global sixth-highest nonzero root-gap theorem

Research note, 2026-10-22. This is an all-length necessary condition on integer squares restricted to decimal digits 1,4,9; it does not resolve the A006716 finiteness conjecture.

## Theorem

If a positive integer x has at least six nonzero decimal digits and every digit of x² is in {1,4,9}, and its six highest nonzero positions are e1>e2>e3>e4>e5>e6, then

\[
\boxed{e_5-e_6\le6}.
\]

No arbitrary upper bound on x or its total nonzero digit count is required.

## Complete proof certificate

Write g=e1-e2, h=e2-e3, t=e3-e4, u=e4-e5, v=e5-e6. The earlier top-three, top-four, and top-five theorems, together with the global high-span bound, force (g,h) to one of eight possibilities, t<=7, u<=5, and v<=g+h+t+u+3.

Let a,b,c,d be the highest four nonzero root digits, D=10^(g+h+t), and z=aD+b10^(h+t)+c10^t+d. The first-ten-digit exact prefix interval sieve permits precisely 603 leading-four configurations.

Append the fifth digit f in {1,...,9} with gap u, setting D5=D*10^u and z5=z*10^u+f. The first-fourteen-digit interval sieve permits precisely 2322 leading-five configurations.

For a proposed sixth gap v, every lower root digit lies strictly below the sixth position. Therefore the normalized root lies in the exact rational interval

\[
\left[\frac{z_5 10^{v-1}}{D_5 10^{v-1}},
\frac{z_5 10^{v-1}+1}{D_5 10^{v-1}}\right).
\]

The square of this interval must intersect a prefix interval belonging to a 16-digit word over {1,4,9}. All such intersections are tested using exact integer divisions and a deterministic digit-DP successor algorithm in [verify_top_six_gaps.py](verify_top_six_gaps.py). The number of surviving configurations is:

| Sixth gap v | Surviving configurations |
|---:|---:|
| 1 | 2322 |
| 2 | 702 |
| 3 | 200 |
| 4 | 56 |
| 5 | 19 |
| 6 | 3 |
| >=7 | 0 |

The three survivors at v=6 are (g,h,t,u,a,b,c,d,f) equal to (1,1,1,1,3,1,4,8,8), (1,1,3,2,2,1,2,1,6), and (2,3,1,1,7,1,9,9,5).

This excludes every sixth gap v>=7 whenever x² has at least sixteen decimal digits.

For the finite exceptional case x² shorter than sixteen digits, the verifier exhausts every root 1<=x<=floor(sqrt(10^15-1))=31,622,776 using exact integer squaring. The only A006716 root in this range with at least six nonzero digits is x=387288, with sixth gap 1. This completes the proof for all positive integers.

## Sharpened global recurrence

Let d_j=e_j-e_(j+1) for descending root positions and S_j=e1-e_j. The earlier results give d1+d2<=6, d3<=7, d4<=5, d5<=6. Hence S6<=24. The universal upper-span lemma says d_j<=S_j+3 for j>=6, implying S_(j+1)+3<=2(S_j+3). Induction yields

\[
\boxed{d_j\le27\cdot2^{j-6}\qquad(j\ge6)}.
\]

This is strictly better than the earlier bound 21*2^(j-5) for j>=6. It provides a proven early-pruning rule for future exact searches, but does not prove A006716 finite.

All exact tests passed in [GitHub Actions run 39770626224](https://github.com/dongxuelian2/oeis-papers/actions/runs/39770626224). Manuscripts and PDF files remain unchanged.

Reproduce with: python papers/A006716/verify_top_six_gaps.py.
