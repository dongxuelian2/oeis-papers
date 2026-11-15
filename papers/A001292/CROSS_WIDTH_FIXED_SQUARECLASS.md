# A total-digit window for fixed-squareclass finiteness across a width boundary

The previous three-dimensional theorem assumed that endpoint m and cut k had the same digit width. Here the expansion is anchored at the CUT width instead. An exact tail identity extends the result to the smaller endpoints of the next digit width, which the earlier theorem did not cover. The squareclass remains fixed; this is not a uniform result over all squareclasses or a proof of the integer-power conjecture.

## Theorem

Fix a positive squarefree integer s and 0<epsilon<1. For each cut width w>=2 put

    B=10^w, L=B/10, C=B-1, V=B-L,
    t=D(L-1), E=D(m).

There are only finitely many triples (w,m,k) for which R_(m,k) is an integer square and

    L+7<=k<=B-2, m>k,
    J:=kC+B=a^2*s for a positive integer a,
    2t+epsilon*wB<=E<=2wV-epsilon*wB.                 (1)

The endpoint is not required to have w digits. The threshold is ineffective and may depend on s and epsilon. If a displayed parameter range is empty it contributes no triples.

## 1. An exact expansion anchored at the cut

Set G=10^t and

    A=C^2*W_(L-1)+LC+1,
    K=k-L+1, so 8<=K<=V-1.

The fixed-width prefix identity for k is

    C^2*W_k=A*B^K-J.

The rotation identity therefore gives, for EVERY m>k,

    C^2*R_(m,k)=J*10^E+H*B^K-J,
    H=G*C^2*W_m-A*(10^E-1).                          (2)

If m<B, let N=m-L+1. Then E=t+wN and the known fixed-width formula gives

    H=A-G*(mC+B), |H|<2G*B^2.                       (3)

If m>=B, let P=D(B-1)=t+wV and split the prefix at that boundary:

    W_m=W_(B-1)*10^(E-P)+U, 0<=U<10^(E-P).

At the boundary, C^2*W_(B-1)=A*B^V-J_end with J_end=C^2+B. Substitution in (2) gives

    H=A+G*(C^2*U-J_end*10^(E-P)).                    (4)

Here E-P>=w+1. Since A/G<B^2/8 and J_end-C^2=B, H<0, and

    |H|<G*J_end*10^(E-P)<2B^2*10^(E-wV).

Thus, in both cases, with

    M_star=max(t,E-wV),

we have

    |H|<2B^2*10^M_star,
    |H*B^K-J|<3B^(K+2)*10^M_star.                   (5)

This tail estimate is the new ingredient. It explicitly controls the extra digits after the cut's full width has ended.

## 2. Simultaneous product and the two-sided window

Suppose R=y^2, x=Cy, and write E=2q+e, Q=10^q, e in {0,1}. Fix a parity subsequence and set u=sqrt(10^e*s). For the integer vector

    (X,Y,Z)=(x,aQ,a),

use exactly the same fixed algebraic linear forms as in ALL_CUT_FIXED_SQUARECLASS.md: at infinity, X-uY,Y,Z; at p=2,5, X-sqrt(-s)Z,X+sqrt(-s)Z,Y.

The archimedean product, by (5) and x+uY>=uY, is at most

    c_s*B^(K+3)*10^M_star.

Also E>D(k)=t+wK, so 10^E is divisible by B^K. Equation (2) implies that x^2+J is an integer multiple of B^K. Therefore the product at 2 and 5 is at most B^(-K)/Q, and the combined product is at most

    c_s*B^3*10^(M_star-E/2).                         (6)

The harmless factor 10^(e/2) is absorbed in c_s. Both inequalities in (1) are used:

    M_star-E/2=max(t-E/2,E/2-wV)<=-epsilon*wB/2.

## 3. Uniform direction, height, and exceptional subspaces

The error in the main term satisfies

    |H*B^K-J|/(J*10^E)<=30*B^K*10^(M_star-E).

If m<B, then M_star=t and E=t+wN with N>K, so this is at most 30/B. If m>=B, then M_star=E-wV and K<=V-1, giving the same bound. Consequently, uniformly throughout the theorem's range,

    X/Y -> u, Z/Y=1/Q -> 0                         (7)

as w grows. This explains why the single cut k=B-1 was excluded: for that boundary cut K=V, the bound does not tend to zero after the endpoint crosses into the next width. No conclusion for that cut is silently inferred.

For sufficiently large w, (7) and a<B/sqrt(s) imply H_0=max(X,Y,Z)<=c_s*BQ. The upper window bound gives

    log_10 H_0<=wB+O_s(w).

Together with (6), this makes the product at most H_0^(-epsilon/4) eventually. Dividing by gcd(x,a) gives a primitive vector without increasing the combined product, exactly as proved in the earlier supplement; its norm is at least Q and at most H_0.

The p-adic Subspace Theorem therefore puts the primitive vectors in finitely many proper rational subspaces, separately for the two parities. Each subspace has a nonzero rational relation b_1X+b_2Y+b_3Z=0. If u is irrational, (7) implies b_1=b_2=0 and then b_3=0, a contradiction for an infinite sequence with w tending to infinity.

If u is rational, squarefreeness forces (s,e)=(1,0) or (10,1). Since x^2=-J modulo B^K, J<B^2 and K>=8, the same elementary 2-adic argument as before excludes both cases: odd valuation for s=10, or an odd square equal to minus an odd square modulo 8 for s=1.

For bounded w, (1) bounds E=D(m) and hence m, so there are only finitely many triples. Repeated projective vectors cannot yield unbounded widths because Y/Z=Q and the lower window bound forces Q to infinity. This proves the theorem.

We use the same verified source and hypotheses as before: Evertse, *The p-adic Subspace Theorem* (May 2011), Theorem 1.1, r=n=3, with fixed algebraic-over-Q coefficients and primitive integer vectors: https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf . Its finiteness statement is not an effective exceptional threshold.

## 4. Previously uncovered smaller endpoints

Fix any real c with 1<c<9/5, and fix s. Then only finitely many square rotations satisfy

    10^w<=m<=c*10^w,
    10^(w-1)+7<=k<=10^w-2,
    k(10^w-1)+10^w=a^2*s.

To check (1), put B=10^w. Uniformly for this endpoint range,

    E/ (wB) lies between 1+o(1) and c+o(1),
    2t/(wB)->1/5, 2wV/(wB)=9/5.

These follow directly from the digit-count formula for the (w+1)-digit endpoint. Choose a fixed positive epsilon smaller than both 4/5 and 9/5-c. Then (1) holds for all sufficiently large w.

For example, the whole range B<=m<=3B/2 is permitted with a suitable fixed margin. These endpoints are in the SMALLER part of their (w+1)-digit interval, and the cuts lie in the PREVIOUS width. The prior same-width theorem did not apply to these triples. This is not a claim about cuts in the new width, cuts in all earlier widths, or every endpoint below twice the new lower boundary.

## 5. Limitations and verification

The new result preserves fixed-squareclass and ineffective-threshold quantifiers. The union over unrestricted s is not justified. It only concerns integer squares, and it excludes neither all remaining squares nor all other prime-exponent powers.

The accompanying verifier checks both exact branches of the anchored identity, including endpoints beyond the width boundary, the tail bounds, limiting-direction ingredients, and rational window inequalities at selected widths. It does not compute exceptional subspaces or establish finiteness by enumeration. The main manuscript and PDF remain unchanged.
