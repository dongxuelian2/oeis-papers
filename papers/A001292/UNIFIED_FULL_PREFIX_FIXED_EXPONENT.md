# Full-prefix congruences give global fixed-prime sparsity

This note treats every whole-integer cut, including cuts in an earlier decimal width and the initial part of the endpoint width. It is a counting theorem, not nonexistence. The proof is elementary and effective. No squareclass is fixed. No claim of literature priority is made.

## Theorem and exact scope

Write W_m for the decimal concatenation 123...m, D(m) for its number of digits, and R_(m,k) for the rotation moving the prefix 123...k to the end, with 1<=k<m. Fix an endpoint width d>=2 and put B=10^d, L=B/10.

For all endpoints and cuts

    L <= m <= B-1,     1 <= k < m,

there are fewer than 329B square pairs (m,k). For d>=3 and each fixed odd prime ell there are fewer than

    (12 c_ell ell + 9)B

pairs with R_(m,k)=y^ell, where c_5=5 and c_ell=1 for other odd primes. These counts are for pairs, not representations.

More precisely, for d>=3 and k>=10, the per-cut counts are at most 320 for squares and at most 12 c_ell ell for a fixed odd prime. The at most nine smaller cuts contribute fewer than 9B pairs in total, including their union over every exponent. For d=2, the entire cut-endpoint domain has 4815 pairs, less than the displayed square bound. The fixed-odd-prime bound is stated for d>=3; the small-width domain bound may be used separately when summing exponents. Thus no small-endpoint or earlier-width exclusions remain.

For earlier-width cuts alone, k<L, the same argument gives fewer than 41B squares, and fewer than (1.2 c_ell ell+9)B powers for a fixed odd prime. These latter constants are optional: the global bounds are the main statement.

## 1. A small smooth part for every prefix W_k with k>=10

Let w be the decimal width of k, b=10^w, l=b/10, c=b-1, K=k-l+1, and set

    a=c^2 W_(l-1)+lc+1,       j=kc+b.

The exact fixed-width concatenation identity is

    c^2 W_k = a b^K-j.                                  (1)

For completeness, (1) starts at k=l-1, where K=0 and j=lc+1. Induction uses W_k=b W_(k-1)+k and b[(k-1)c+b]-c^2 k=kc+b.

We prove, for p=2 and 5,

    v_p(W_k)=v_p(j),      v_p(W_k)<D(k).                 (2)

Consequently the 2,5-smooth part satisfies

    W_k,(2,5) := 2^v_2(W_k) 5^v_5(W_k) <= j < b^2.      (3)

For the first assertion it suffices to show v_p(a b^K)>v_p(j), since c is coprime to 10.

If K>=8, then j<b^2 gives v_2(j)<7w and v_5(j)<3w, while v_p(a b^K)>=wK>=8w.

For 1<=K<=7 write k=l+h with 0<=h<=6. If w>=4, then

    j=10l^2+(9+10h)l-h.

For h=0 this has both valuations w-1<wK. For 1<=h<=6, both valuations equal those of h, since v_p(h)<=2<w-1, and therefore are also less than wK. The integrality of a gives v_p(a b^K)>=wK, which is enough. No separate valuation formula for a is required.

The remaining fourteen cuts have the following directly evaluated valuation pairs, for both W_k and j:

    k=10,11,12,13,14,15,16:
      (1,1),(0,0),(3,0),(0,0),(1,0),(0,1),(2,0).
    k=100,101,102,103,104,105,106:
      (2,2),(0,0),(1,0),(0,0),(6,0),(0,1),(1,0).

Each of the fourteen displayed cases also satisfies v_p(j)<wK, so the same argument from (1) applies. This proves equality of valuations in (2) at every k>=10. To check v_p(W_k)<D(k), for w>=3 use D(k)>D(l-1)>=l>7w. For w=2,K>=8 use D(k)>=9+16>14; for the seven remaining width-2 cuts inspect the displayed pairs. This strict inequality rules out saturated local congruences. The special cuts k<=9 are not silently included in this lemma.

## 2. Anchor the exponential at the endpoint width

Put

    C=B-1, t=D(L-1)=((9d-10)L+1)/9, G=10^t,
    A=C^2 W_(L-1)+LC+1,
    N=m-L+1, M=mC+B,
    s=D(k), U=W_k, V_k=10^s,
    F=V_k A-G C^2 U,
    T(N)=V_k M-C^2 U.

The rotation and fixed-width concatenation identities give the exact formula

    C^2 R_(m,k)=F B^N-T(N).                            (4)

The coefficient F depends on d,k but not m. Two cases show it is positive and uniformly large.

If k>=L, put K=k-L+1. Identity (1), now at width d, yields

    F=G(kC+B)>G C^2/10.

If k<L, write W_(L-1)=U 10^(t-s)+V. Then

    F=10^s(C^2 V+LC+1).

For k<L-1 the suffix V is nonempty, has t-s digits, and starts with a nonzero digit. Therefore V>=10^(t-s-1). For k=L-1 it is empty, s=t, and LC+1>C^2/10. In both cases, and hence for all cuts,

    F >= C^2 10^(t-1).                                (5)

The weak inequality is convenient; the underlying bounds are strict.

Every W_k/10^s lies between zero and 1/8: for k<=3 inspect 0.1,0.12,0.123; for k>=4 the decimal begins 0.1234. Throughout L<=m<=B-1, including real m,

    0<M<B^2,       |T(N)|<B^2 10^s.                    (6)

Crucially T is allowed to be negative near the start of a width. It is linear in N, with slope C 10^s>0.

## 3. Full-prefix local congruences

Let ell=2 or an odd prime, suppose R=y^ell, and set x=Cy. Multiplying (4) by C^(ell-2) gives

    x^ell=C^(ell-2)F B^N-C^(ell-2)T(N),
    x^ell=C^ell U mod 10^s.                            (7)

For k>=10, (2) forces ell v_p(x)=v_p(U) for p=2,5. If either right side is not divisible by ell there is no solution for this cut. Otherwise put

    z=2^(v_2(U)/ell) 5^(v_5(U)/ell),
    D=10^s/z^(ell-1).

Then

    z^ell=W_k,(2,5)<10^(2w)<=B^2,                      (8)

and every solution x belongs to at most c_ell residue classes modulo D, where c_2=8, c_5=5, and c_ell=1 for other odd primes.

Indeed, after dividing a local congruence by p^(ell v_p(x)), its unit part has at most four roots at p=2 for ell=2, two at p=5 for ell=2, one at p=2 for odd ell, and gcd(ell,4*5^(n-1))<=c_ell at p=5. A unit-root class determines x modulo p^(s-(ell-1)v_p(x)). Combining these two compressed moduli gives D. All exponents are positive by (2).

## 4. At most one inflection, even when T is negative

Fix d,k,ell and r=dN mod ell. Set

    Q=10^((dN-r)/ell), a=10^r C^(ell-2)F,
    Z(Q)=C^(ell-2)T(N(Q))=b log Q+c_0,
    b=ell C^(ell-1)10^s/log B >0,
    f(Q)=[aQ^ell-Z(Q)]^(1/ell).

Here log in derivatives is natural, and c_0 is a fixed real constant. This is the exact curve x=f(Q) through solution points.

On the real interval between the first and last admissible endpoints for this cut, g(Q)=aQ^ell-Z(Q) is positive and g'(Q)>0. To see this in N, its derivative is a positive multiple of

    F (log B)B^N-C10^s.

If k<L, F/10^s>=LC+1 and N>=1. If k>=L, F/10^s=(kC+B)B^(-K) and N>=K+1. Either lower bound makes this derivative positive. At the smallest allowed integer endpoint m=max(L,k+1), g is C^ell times a positive rotation. Monotonicity proves positivity on the full real interval.

For any b>0, direct differentiation gives

    ell^2 f^(2ell-1)f''
      =ell aQ^(ell-2)[(2ell-1)b-ell(ell-1)Z]
        -[ell bZ+(ell-1)b^2]/Q^2.                     (9)

Thus f'' has the sign of

    H=(2ell-1)b-ell(ell-1)Z
        -b[ell Z+(ell-1)b]/(ell aQ^ell).

Differentiating with respect to log Q gives

    H'=-ell(ell-1)b+ell b Z/(aQ^ell)
                      +(ell-2)b^2/(aQ^ell) <0.         (10)

The strict inequality uses Z<aQ^ell from g>0 and b<ell aQ^ell from g'>0. For ell=2 the final term is zero and the first inequality already suffices.

Therefore f'' changes sign at most once. The curve can be partitioned into at most two intervals on each of which it is strictly convex or strictly concave. An inflection point may be assigned to either adjacent interval; strict curvature in the interior still rules out three collinear points. No extra count for the inflection is needed. In particular every triple of distinct solution points within one such interval has nonzero determinant.

## 5. The determinant gap

Keep r fixed and restrict to one compressed residue class modulo D and one curvature interval. For three solutions N_1<N_2<N_3, form

    Delta=det((x_1,Q_1,1),(x_2,Q_2,1),(x_3,Q_3,1)).

It is a nonzero integer, divisible by DQ_1: subtract the common x residue times the last column from the first column; Q_1 divides every Q_i because r is fixed. Hence

    |Delta|>=DQ_1.                                     (11)

Let E_i=t+dN_i and alpha=a^(1/ell). Factoring the difference of ellth powers, (5)-(6) give

    |alpha Q_i-x_i|
      <= C^(ell-2)|T(N_i)|/(alpha Q_i)^(ell-1)
      < (B^2/C)10^((ell-1)/ell)10^[s-(ell-1)E_i/ell]
      < 11B 10^[s-(ell-1)E_i/ell].                     (12)

The constant uses B>=100, B/C<=100/99, and 10^((ell-1)/ell)<10. The right side decreases with N_i, irrespective of the sign of T. Subtract alpha times the Q column in Delta, and bound the coefficients of the resulting error column. Their absolute values sum to 2(Q_3-Q_1)<2Q_3. Therefore

    DQ_1 < 22B 10^[s-(ell-1)E_1/ell] Q_3.

Substitute D=10^s/z^(ell-1) and Q_i=10^((dN_i-r)/ell). The fixed remainder r cancels exactly, giving

    dN_3 > ell dN_1+(ell-1)t
                  -ell log_10(22Bz^(ell-1)).           (13)

By (8) and log_10(22)<2, for d>=2 the final term divided by d is less than

    ell + ell log_10(22)/d+2(ell-1) <4ell.

Consequently

    N_3 > ell N_1+(ell-1)t/d-4ell.                     (14)

Set h=N+t/d-4ell/(ell-1). Then every triple in the group satisfies h_3>ell h_1.

## 6. Counting all cuts and all endpoint positions

For d>=3 and ell>=2,

    L/2 <= h <10L.                                     (15)

Indeed, N>=1, 4ell/(ell-1)<=8, and t/d-7>=L/2. The last inequality follows from

    (1/2-10/(9d))L >=7-1/(9d),

which holds at d=3,L=100 and increases thereafter. The upper bound follows from N<=9L and t/d<L.

Order all solutions in one fixed (d,k,ell,r,compressed branch,curvature interval) group. By (14), the odd-indexed h values increase by a factor greater than ell, as do the even-indexed values. If either subsequence has j points, then ell^(j-1)<20.

For squares, j<=5, so a group has at most ten points. Multiplying by at most eight branches, two remainders and two curvature intervals gives at most 320 points for the cut.

For odd primes, j<=3, so a group has at most six points. Multiplying by c_ell branches, at most ell remainders and two curvature intervals gives at most 12 c_ell ell points for the cut.

There are fewer than B cuts. The k<=9 strip has fewer than 9B pairs regardless of power status. This proves the global bounds for d>=3. For d=2, the whole domain contains sum_(m=10)^99 (m-1)=4815 pairs, which is smaller than the square bound 32900. The fixed-odd-prime statement is deliberately restricted to d>=3; no finite power search is needed or used. A bound for a union over all exponents can absorb the width-2 domain separately.

## Scope and verification

Summing the square bound over widths gives O(X) square pairs with m<=X and every whole-integer cut 1<=k<m. For example, if X>=10 and D is its decimal width, the count is less than 36+(32900/9)X, by summing 329*10^d for 2<=d<=D and using 10^D<=10X. The 36 covers all one-digit endpoint pairs without a power test.

The square statement has no omitted endpoints, cut widths, squareclasses, or leading cuts. The odd-prime statement is per exponent; a union over unbounded exponents requires a separate argument. The result allows infinitely many perfect-power rotations and does not resolve the nonexistence conjecture.

The companion Python verifier checks the fourteen exceptional valuation pairs, the width-2 parameter-domain size, selected exact identities, compressed-root classes, and exact rational evaluations of the derivative identities. These finite checks support the proof; they do not establish the general determinant argument by enumeration.

The completed finite audit passes 4,991 prefix smooth-part and unsaturation checks through k=5000; 11,055 exact rotation/bound checks (5,800 earlier-width and 5,255 same-width, including 2,543 negative corrections); all fourteen small valuation cases; 1,540 prime-power and 556 decimal compressed-root cases; 3,240 rational derivative-identity evaluations; 120 synthetic determinant-divisibility and 45 synthetic error-bound cases; and centered bounds at widths 3 through 1000.
