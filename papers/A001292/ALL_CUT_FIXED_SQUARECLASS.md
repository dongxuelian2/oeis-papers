# Combining real and p-adic approximation across the cut range

This supplement removes the early/late cut-fraction restriction from the previous fixed-squareclass theorem, within a precisely specified same-width range. It uses the three-dimensional p-adic Subspace Theorem, not a change of constants in the one-dimensional Roth-Ridout argument. The squareclass is still fixed before the width grows. The exceptional set is ineffective, and the full integer-power conjecture remains open.

## Theorem

Fix a positive squarefree integer s and a real number 0<delta<8. There are only finitely many triples (d,m,k) satisfying

    d>=2, B=10^d, L=B/10, C=B-1,
    (2+delta)*L<=m<=B-1,
    L+7<=k<m,
    J:=kC+B=a^2*s for some positive integer a,

for which the whole-integer rotation R_(m,k) is an integer square.

Thus for fixed s and delta, all sufficiently large widths have no such squares, uniformly over the displayed endpoints and cuts. No fixed early or late proportion of the cut range is omitted. This does not cover cuts before L+7, endpoints below (2+delta)L, unrestricted squareclasses, or higher prime exponents. The threshold depends on s and delta and is ineffective here.

## 1. Exact identities and bounds

Write

    t=D(L-1)=(d-10/9)*L+1/9, G=10^t,
    A=C^2*W_(L-1)+LC+1,
    N=m-L+1, K=k-L+1, M=mC+B.

The inherited identities are

    C^2*R=G*J*B^N+(A-GM)*B^K-J,
    C^2*R+J=F*B^K,
    F=G*J*B^(N-K)+A-GM.

Here 8<=K<N, N>=(1+delta)L, N<=9L, and t<dL. The earlier proof supplies

    B^2/10<J<B^2, 0<A/G<B^2/8, B^2/5<M<B^2,
    0<T:=(GM-A)*B^K+J<2G*B^(K+2), F>0.

Suppose R=y^2 and put x=Cy. Split t+dN=2q+e, e in {0,1}, and let Q=10^q. With

    u=sqrt(10^e*s), J=a^2*s,

we have

    x^2=u^2*(aQ)^2-T,
    x^2+s*a^2=F*B^K.

Along an infinite sequence one may fix the parity e. All algebraic coefficients below then remain fixed, depending only on s and e. Equivalently, apply the argument separately to e=0 and e=1 and take the finite union.

## 2. The product of three linear forms

Apply linear forms to the integral vector

    v=(X,Y,Z)=(x,aQ,a).

At the real place use the independent forms

    X-uY, Y, Z.

Since x+uY>=uY,

    |(x-uY)*Y*Z| <=T*a/u <=c_s*G*B^(K+3).

At each p in {2,5}, choose either square root of -s in the algebraic closure of Q_p and use the independent forms

    X-sqrt(-s)*Z, X+sqrt(-s)*Z, Y.

Their product at v is the rational integer

    (x^2+s*a^2)*aQ=F*B^K*aQ.

Because F and a are integers and Q is supported on {2,5},

    product_(p=2,5) |F*B^K*aQ|_p <=B^(-K)/Q.

Multiplication cancels the entire K-dependent factor:

    product_(v=infinity,2,5) product_(i=1,2,3) |L_(i,v)(v)|_v
      <=c_s*G*B^3/Q
      =c_s*10^((t-dN+e)/2+3d).                       (1)

This cancellation is what the earlier separate early/late estimates did not use.

## 3. Strict Subspace-Theorem decay and primitive vectors

Let H_0=max(x,aQ,a). Since 0<x<u*aQ and a<B/sqrt(s),

    Q<=H_0<=c_s*B*Q,
    log_10 H_0<=5dL+O_s(d).

On the other hand t-dN<=-delta*dL. Hence (1) is at most

    H_0^(-delta/20)

for all sufficiently large d, uniformly in the displayed m,k. Indeed its base-10 logarithm is at most -delta*dL/2+O_s(d), whereas (delta/20)*log_10 H_0<=delta*dL/4+O_(s,delta)(d).

If v is not primitive, divide by g=gcd(x,aQ,a)=gcd(x,a). Under this division, the product in (1) is multiplied by

    g^(-3)*|g|_2^(-3)*|g|_5^(-3)
      =(g_{2,5}/g)^3<=1,

where g_{2,5} is the largest divisor of g supported on {2,5}. The primitive norm H=H_0/g is no larger than H_0, so the required inequality also holds with H^(-delta/20). Moreover H>=Q because g divides a, and Q tends to infinity with d.

The p-adic Subspace Theorem now places all sufficiently large primitive vectors in finitely many proper rational linear subspaces of Q^3. We use its standard form with three independent algebraic linear forms at each of infinity,2,5. All coefficients are algebraic over Q. At the finite places they need not belong to Q_p itself; the algebraic closure is allowed, and their products here are rational.

Source: J.-H. Evertse, *The p-adic Subspace Theorem* (May 2011), Theorem 1.1, the r=n=3 case, attributed there to Schlickewei (1977): https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf . The conclusion is a finite union of proper rational subspaces; it does not by itself give finiteness of vectors or an effective exceptional bound.

## 4. Eliminating the exceptional subspaces

The identity and the bound for T give, uniformly for every K<N,

    0<T/(G*J*B^N)<20*B^(K-N)<=20/B.

Consequently

    X/Y -> u, Z/Y=1/Q -> 0

as d tends to infinity. Suppose a fixed proper rational subspace contained infinitely many solution vectors. Choose a nonzero rational relation

    b_1*X+b_2*Y+b_3*Z=0

vanishing on it and pass to widths tending to infinity. Dividing by Y and taking limits gives b_1*u+b_2=0. If u is irrational, b_1=b_2=0, and the exact relation then forces b_3=0 because Z>0, a contradiction.

The rational-u cases are impossible already. Since s is squarefree, u rational implies s=1,e=0 or s=10,e=1. From x^2=-J modulo B^K and J<B^2 we have 2v_2(x)=v_2(J), because v_2(J)<7d<dK. If s=10, v_2(J)=2v_2(a)+1 is odd, a contradiction. If s=1, division by 2^(2v_2(a)) gives an odd square congruent to the negative of an odd square modulo 8: dK-2v_2(a)>=3, since J<B^2 and K>=8. This is impossible. These are inherited local obstructions, not new global exclusion families.

Thus every exceptional rational subspace contains only finitely many relevant solution vectors with unbounded widths. A fixed bounded set of widths has finitely many possible endpoints and cuts. This proves the theorem. Repeated projective vectors cannot cause a hidden problem: their ratio Y/Z=Q is fixed, while Q tends to infinity with d.

## 5. Consequences and unresolved scope

The theorem also holds for a fixed finite set of squareclasses. Hence an infinite sequence of integer-square counterexamples in this same-width region would have to escape every fixed finite set of squareclasses of J=k(10^d-1)+10^d.

Unlike the preceding one-dimensional result, this conclusion has no early/late cut-fraction gap. It still does not justify taking a union over ALL s. The known growth of candidate squareclasses is not a claim that square counterexamples exist, and this theorem does not uniformly bound their possible squareclasses.

The interval restriction m>=(2+delta)L is important: the decay in (1) uses dN-t>=delta*dL. No fixed negative height exponent follows from this estimate when that margin vanishes. No conclusion for arbitrary lower endpoints or earlier-width cuts is inferred.

The theorem concerns squares. Even a complete square exclusion would leave other prime exponents in the integer-power conjecture. No effective finite search bound is supplied, and no individual new rotation is claimed to have been excluded by computation. The main manuscript and PDF remain unchanged.

## 6. Finite verification

The verifier checks the exact identities, positivity and product-bound ingredients for selected endpoints and cuts, including cuts near both ends, and tests primitive-vector scaling and the elementary margin arithmetic. It does not compute the ineffective exceptional subspaces or verify the theorem by searching. The infinite conclusion rests on the proof and the cited Subspace Theorem.
