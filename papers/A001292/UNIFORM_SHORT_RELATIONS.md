# Uniform exclusion of small rational hyperplanes

This is a structural lemma about any putative square solution. It allows the squareclass to vary, but does **not** prove that square solutions are finite or nonexistent. It does not apply a moving-target Subspace Theorem.

## Statement

Use the notation and exact identities of `ALL_CUT_FIXED_SQUARECLASS.md`, but assume only

    d >= 2, B = 10^d, L = B/10, C = B-1,
    2L <= m <= B-1, L+7 <= k < m,
    N = m-L+1, K = k-L+1,
    J = kC+B = a^2 s,

where a is a positive integer and s is a positive squarefree integer. In particular s need not be fixed. Suppose the corresponding rotation is a square, R=y^2. Put

    x = Cy, t = D(L-1), G = 10^t,
    t+dN = 2q+e, e in {0,1}, Q = 10^q,
    v = (x,aQ,a).

Then every nonzero integer relation

    b1*x + b2*aQ + b3*a = 0

has

    W := max(|b1|,|b2|,|b3|) > B^(N/4-3).            (SR)

Thus every rational hyperplane containing v has multiplicative projective height greater than B^(N/4-3), where the height of a rational hyperplane is the maximum absolute value of its primitive integer coefficients. Scaling v to a primitive vector does not change this assertion.

Unlike the Subspace-Theorem decay estimate, this lemma needs no positive delta in m >= (2+delta)L. The endpoint m=2L is included.

## Ingredients

The inherited identities and bounds remain valid for m>=2L:

    x^2 = 10^e*s*a^2*Q^2 - T,
    x^2+s*a^2 = F*B^K,
    0 < T < 2G*B^(K+2),
    0 < J=a^2*s < B^2,
    Q^2 = G*B^N / 10^e,
    8 <= K < N, N >= L+1.

Indeed the previous bound A/G<B^2/8 and M=mC+B>B^2/5 ensure T>0 at m=2L as well. Since t>=9 for d>=2 and e<=1, and t<dL<dN,

    B^(N/2) <= Q <= B^N.                             (2)

The estimates a^2<B^2 and s<B^2 will be used independently; a sharper joint estimate is unnecessary.

## The rational leading-root cases are locally impossible

If 10^e*s is a rational square, squarefreeness implies (s,e)=(1,0) or (10,1). Let r=v_2(J). Since J<B^2,

    r < 2d log_2(10) < 7d < dK.

The congruence x^2+J=0 modulo 2^(dK) consequently implies 2v_2(x)=r. For s=10, r=2v_2(a)+1 is odd, a contradiction. For s=1, dividing by 2^(2v_2(a)) leaves the sum of two odd squares divisible by 8: the remaining modulus exponent is dK-r>d>=2. That is impossible. Therefore 10^e*s is irrational as a square root for every putative solution under consideration.

## Proof of (SR)

Assume instead that a nonzero relation has W<=B^(N/4-3). If b1=0, then b2*Q+b3=0. Equation (2) implies Q>W, so b2=b3=0, contrary to the relation being nonzero. Hence b1!=0.

Squaring the relation and substituting the first identity gives

    a^2*((b2^2-10^e*s*b1^2)*Q^2
          +2*b2*b3*Q+b3^2) = -b1^2*T.               (3)

The coefficient b2^2-10^e*s*b1^2 is a nonzero integer by the preceding local argument. Also

    W^2/Q <= B^(-6),
    2*W^2*Q+W^2 < Q^2/2.

The second inequality follows directly from B>=100 and Q>=1. Consequently the absolute value of the bracket in (3) is greater than Q^2/2.

If K<=N/2, equation (3) now implies

    1/2 < b1^2*T/(a^2*Q^2)
         < 20*W^2*B^(K-N+2)
         <= 20*B^(-4) < 1/2,

a contradiction. Here 10^e<=10 and a>=1 were used when bounding T/Q^2.

If K>N/2, put D=gcd(B^K,Q). Both are powers of 10, so (2) gives

    D = 10^min(dK,q) >= B^(N/2).

Multiplying the second identity by b1^2 and again using the squared relation gives

    b1^2*F*B^K
       = a^2*((b2*Q+b3)^2+s*b1^2).

It follows that D divides the positive integer a^2*(b3^2+s*b1^2). But

    0 < a^2*(b3^2+s*b1^2)
        <= 2*B^4*W^2
        <= 2*B^(N/2-2)
        < D,

also a contradiction. This proves (SR).

## Height formulation and its effective dependence on eta

Let H be the maximum absolute coordinate of the primitive integer vector obtained from v. Because a*sqrt(s)=sqrt(J)<B,

    Q <= H < sqrt(10)*B*Q <= B^(N+3/2).

For any fixed 0<eta<1/4, if

    (1/4-eta)*N >= 3+(3/2)*eta,

then H^eta<=B^(N/4-3). Hence no nonzero rational relation has primitive coefficient height at most H^eta. This gives an explicit sufficient threshold in N, uniform in s,m,k. Since N>=10^(d-1)+1, it also gives an explicit sufficient width threshold. In particular, coefficient logarithmic heights O(d), or even o(log H), are excluded along any sequence of distinct solution triples in this range as d tends to infinity. Each bounded set of widths contains only finitely many triples, so an infinite set of distinct triples has such a subsequence; repeating a fixed triple is not covered by this asymptotic statement.

## Bounded-degree algebraic relations, even in varying fields

There is also an elementary trace consequence. Let E be any number field of degree D, allowed to depend on the solution. Suppose coefficients beta_1,beta_2,beta_3 in E, not all zero, satisfy

    beta_1*x + beta_2*aQ + beta_3*a = 0.

Write h(beta) for the absolute logarithmic Weil height, including h(0)=0, and let h0=max_j h(beta_j). Then

    6D*h0 + 3 log D > (N/4-3)*log B.                 (4)

To prove this, choose j0 with beta_j0!=0, divide the relation by beta_j0, and take Tr_(E/Q). The resulting rational coefficients

    c_j = Tr_(E/Q)(beta_j/beta_j0)

satisfy c_j0=D, so the rational relation is nonzero. The standard height inequalities for products, quotients and sums, and invariance under conjugation, give

    h(c_j) <= D*h(beta_j/beta_j0)+log D
           <= 2D*h0+log D.

If c_j=p_j/q_j in lowest terms with q_j>0, clearing all three denominators yields a nonzero integer relation of coefficient maximum at most

    exp(3*max_j h(c_j)) <= D^3*exp(6D*h0).

Apply (SR) to obtain (4). No choice of an integral basis, discriminant estimate, fixed number field, or external Diophantine theorem enters this argument.

Consequently, for a uniformly bounded D, algebraic relations with coefficient logarithmic heights O(d), or o(log H), are impossible along any sequence of distinct solution triples as d tends to infinity. The requirement is a bound on a **common field containing the three coefficients**; an individual degree bound must first be converted to a bound on their compositum. This proves the needed type of small-coefficient linear nondegeneracy if a suitable moving-field theorem were available. It does not furnish that theorem.

## What is still missing

For a fixed squareclass, the usual p-adic Subspace Theorem supplies finitely many fixed rational subspaces, and the lemma is another way to eliminate them. If squareclasses vary, neither the ordinary theorem nor the word "absolute" automatically supplies a common finite collection. A proof must still justify an applicable moving-field theorem, or give another argument forcing a sufficiently small rational relation. The lemma does not supply that missing theorem.

The companion `verify_uniform_short_relations.py` performs finite exact checks of the identities and numerical inequalities used above. It does not prove the universal lemma by computation and does not enumerate square solutions.

## Separate literature check: the precise unfilled application

Vojta's primary exposition, *Nevanlinna Theory and Diophantine Approximation* (1999), Theorems 7.6 and 7.7, states a moving-target Subspace Theorem over a fixed number field k. It also requires linear nondegeneracy over the field of moving coefficient functions. Small coefficient heights alone are not its hypotheses. Source: https://library.slmath.org/books/Book37/files/vojta.pdf . The original joint result is Ru and Vojta, *Inventiones Mathematicae* 127 (1997), 51–65; publication verified at https://math.berkeley.edu/~vojta/bib.html .

Evertse and Ferretti, *A further improvement of the Quantitative Subspace Theorem*, *Annals of Mathematics* 177 (2013), 513–590, makes the approximating points algebraic in its Absolute Parametric Subspace Theorem, but retains a fixed system of linear forms and associated twisted heights. Its finite collection of exceptional subspaces is supplied for that fixed data. The quantitative bounds do not by themselves turn separate finite collections, one for each squareclass, into one common collection. Sources: https://annals.math.princeton.edu/2013/177-2/p04 and https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p04-p.pdf .

For the present forms the coefficient field Q(sqrt(10^e*s),sqrt(-s)) has degree at most four, but varies with s. Infinitely many distinct positive squareclasses cannot all have their square roots in one number field. The missing step is therefore an applicable theorem for these varying coefficient fields with the required exponent, not the small-coefficient nondegeneracy established above. This check does not assert that no such theorem could exist or that no alternate argument could work. The withdrawn Yamada arXiv:math/0307203 preprint is not used.

## Separate counterexample to an invalid general uniformization

The assertion "slowly varying bounded-degree forms with a small product put all points in finitely many fixed rational subspaces" is false without further hypotheses, even if every coefficient is rational and every form value is nonzero. This is **not** a counterexample to the rotation problem or to a correctly stated moving-target theorem.

For integers r>=3 put

    n_r = 10^r, Q_r = 10^(r!),
    w_r = (n_r*Q_r+1, Q_r, n_r), H_r=n_r*Q_r+1.

At infinity use the independent forms (X-n_r*Y,Y,Z), and at each of 2 and 5 use (X-Z/n_r,Y,Z). The archimedean product is n_r*Q_r. The product at 2 and 5 together is (n_r^2*Q_r^2)^(-1), since their form values are n_r*Q_r, Q_r and n_r. Hence the total product is

    1/(n_r*Q_r) <= H_r^(-1/2).

Their coefficient logarithmic heights are at most r log(10)=o(log H_r), and w_r is primitive. All form values are nonzero.

Nevertheless, a fixed relation b1*X+b2*Y+b3*Z=0 would give

    (b1*n_r+b2)*Q_r+b1+b3*n_r=0.

If b1!=0 the first term eventually dominates. If b1=0 but b2!=0, it again dominates. If b1=b2=0 then b3=0. Thus no fixed proper rational subspace contains infinitely many of these points, and no finite union contains all of them.

Their moving relation is X-n_r*Y-Z/n_r=0. This is precisely the type of small moving relation that a legitimate moving-target theorem must address and that (SR) excludes for the putative rotation solutions.
