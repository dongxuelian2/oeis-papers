# Square values of the Lucas–Pell sum (A060405)

Let \(L_0=2,L_1=1,L_{n+2}=L_{n+1}+L_n\) and
\(P_0=0,P_1=1,P_{n+2}=2P_{n+1}+P_n\).
Write \(a_n=L_n+P_n\), as in [A060405](https://oeis.org/A060405).

**Classification target.** Determine all \((n,x)\in\mathbb Z_{\ge0}^2\)
with \(a_n=x^2\). The candidate answer is \((3,3)\).

## Current square classification

The [four-anchor theorem](anchor-forcing.md) reduces every square index
to one of the four classes \(3,-3,-2,-1\pmod{720720}\).
The [composite-period lifting certificate](period-and-gap.md) then
forces \(n-r\) to be divisible by an explicit integer of at least 342
decimal digits, with the smallest of the four divisors exceeding
\(10^{341}+3\). Thus
\[
 0\le n\le10^{341},\quad a_n=x^2,\quad x\ge0
 \quad\Longleftrightarrow\quad(n,x)=(3,3).
\]
The [exact verification program](verify_composite_lifting.py) reproduces
this bound. The [zero-anchor valuation argument](extension.md) gives a
separate, stronger restriction for \(r=-1\).
The unrestricted square classification remains open.

## Exact periods and elementary gap principle

For \(h\ge1\), set \(G(h)=\gcd_{0\le j<4}(a_{h+j}-a_j)\).
The [period theorem](period-and-gap.md) gives
\[
 G(h)=
 \begin{cases}
 1&h\text{ odd},\\
 \gcd(L_k,2Q_k)&h=2k,\ k\text{ odd},\\
 \gcd(5F_k,2P_k)&h=2k,\ k\text{ even}.
 \end{cases}
\]
Here \(Q_k\) is the half companion Pell sequence. A modulus admits
period \(h\) precisely when it divides \(G(h)\).
This characterizes all congruence tests with a specified period.

The same note proves, without the Subspace Theorem, that for every
positive integer \(d\), every \(0\le r<4\) and every integer \(m_0\ge50\),
at most 14 indices \(m\in[m_0,m_0+\lfloor m_0/5\rfloor]\) satisfy
\(a_{4m+r}=dx^2\). This is a uniform effective gap principle, not an
upper bound on the last square index.

## Exact local square geometry

The [local geometry theorem](local-geometry.md) determines the square
conditions at all six primes dividing \(720720\). On the zero-anchor
branch \(n=720720t-1\), the primes \(2,3,7,11,13\) have exact
valuation and unit formulas in \(t\); at 5 there are two simple
analytic roots, \(0\) and a nonintegral \(\tau\in1+5\mathbb Z_5\),
with exact square criteria on both neighborhoods.
The [local certificate](verify_local_geometry.py) verifies the
matrix constants and lifts \(\tau\) modulo \(5^{24}\).
The other three anchors automatically satisfy the local square
condition at all six base primes.

The same note uses Baker–Brumer logarithmic independence to show
that each of the four anchor branches contains infinitely many
nonnegative indices passing the local square test at every prime
in any specified finite set, even when all prime powers are allowed.
A local proof of the unrestricted classification must therefore
use primes depending on the candidate index, or an independent
global argument.

## Variable-prime obstructions

The [Frobenius descent theorem](variable-primes.md) gives, for
even \(k\), primes \(p>5\), and \(e\ge1\),
\[
 a_{r+kp^e}\equiv L_{r+(5/p)^e k}+P_{r+(2/p)^e k}\pmod p,
\]
where the parentheses denote Legendre symbols. In particular
\(a_{r+kp^{2j}}\equiv a_{r+k}\pmod p\).
This allows a variable obstruction from primes dividing an index offset.

Combining the composite and zero-anchor divisibility certificates
gives final divisor lengths 429, 439, 342 and 3483 for the anchors
\(3,-3,-2,-1\), respectively. The
[exact witness certificate](verify_variable_primes.py) proves
square-class independence for the four mixed recurrence values
associated with each of these divisors. For indices \(r+D_rp^e\),
the variable test modulo the multiplier prime excludes a density
\(1/2\) of primes for either exponent parity and a density \(5/16\)
for both parities simultaneously.

For every fixed finite set of local primes there are infinitely many
indices in each anchor branch that pass the entire fixed set of tests
but fail this variable-prime test. Coverage of every nonzero offset
is not established; the uniform finite exclusion remains \(10^{341}\).

## Offset-prime limitations and global square-class constraints

The [offset-prime counterexample](smooth-support.md) shows that for
\(r\in\{3,-3,-2,-1\}\) and \(K=(N!)^2\), \(N\ge13\),
every prime divisor \(p\mid K\) satisfies \(a_{r+K}\equiv a_r\pmod{p^3}\).
For the nonzero anchors these are actual local squares at all such
primes. Thus the offset-prime nonresidue test alone cannot cover
all candidates, even after imposing any fixed forced divisor.

The same note gives an exact square-class criterion on the zero
anchor for fixed prime supports and sufficiently divisible offsets.
With \(h_2=48,\ h_3=24,\ h_5=3000,\ h_p=p(p^2-1)\) for \(p>5\),
let \(H_N=\operatorname{lcm}_{p\le N}h_p\), with prime \(p\).
The [certificate](verify_smooth_support.py) excludes every positive
\(N\)-smooth multiple \(k\) of \(H_N\) as a square offset
\(a_{k-1}\), for every \(13\le N\le100000\).

The [global square-class obstruction](forced-squareclass.md) requires
no smoothness assumption. Let \(F\) be the 832 previously forced
primes, \(D=720720\prod_{p\in F}p\), and
\(E=7\cdot11\cdot13\prod_{p\in F}p\).
Any square index on the zero anchor must satisfy
\(n+1=5^\delta E d y^2\), where \(d\) is positive squarefree,
coprime to \(D\), and has a prime divisor at least 9857.
Also \(d\equiv17\pmod{24}\) for \(\delta=0\), or
\(d\equiv13\pmod{24}\) for \(\delta=1\).
The [dual character certificate](verify_forced_signatures.py)
combines 838 local quadratic characters, and proves the exclusion
with an explicit separating vector involving 420 odd primes.
These are structural restrictions on unbounded indices; the full
square classification is still open.

## Archimedean separation

The [square-gap theorem](square-gap.md) proves that, for each fixed
positive integer \(d\),
\[
 \lim_{n\to\infty}\frac1n\log\min_{x\in\mathbb Z}|a_n-dx^2|
 =\tfrac12\log(1+\sqrt2).
\]
The squarefree kernel tends to infinity. In addition, combining the
fixed-exponent theorem below with the general Shorey–Stewart–Pethő
exponent bound yields finiteness of all perfect powers, without fixing
the exponent. The gap proof gives no effective index threshold.

## Higher-power separation

The [fixed-exponent gap theorem](power-gaps.md) extends the asymptotic
distance result to all fixed exponents \(k\ge3\), with a cubic resonance
on \(n=3m\). For every \(m\ge1\), the unique nearest cube to \(a_{3m}\)
is \((2P_m)^3\), at distance \(L_{3m}+3(-1)^mP_m>0\).
For all \(k\ge4\), and for cubes on the other two residue classes,
the logarithmic growth rate of the distance is
\((1-1/k)\log(1+\sqrt2)\).

## Quantitative square-index bound

The [quantitative count](quantitative-square-count.md) applies Evertse's
quantitative Subspace Theorem to seven conjugate coordinates.
Every exceptional hyperplane contains at most fourteen square indices
within each residue class modulo four, yielding the explicit global
bound \(10^{3739}\) on the number of square indices. Moreover, if the
normalized coefficients of such a hyperplane have logarithmic height
at most \(B\), every square index it contains satisfies
\(n\le2000(B+1)+3\). An effective bound for the heights of the exceptional
hyperplanes would give the missing effective index cutoff.

## Theorem 1 (finiteness for every fixed exponent)

For each fixed integer \(d\ge2\), only finitely many nonnegative indices
satisfy \(a_n=x^d\) for an integer \(x\).

**Proof.** Put \(\alpha=(1+\sqrt5)/2,\ \beta=1+\sqrt2\).
The Binet expressions give
\[
 a_n=\alpha^n+(-\alpha^{-1})^n
       +\frac{\beta^n-(-\beta^{-1})^n}{2\sqrt2}.
\]
The four distinct roots have a unique dominant root \(\beta>1\)
at the real place. Apply Theorem 2 of Corvaja and Zannier [1] to
\(g(Z,X)=X^d-Z\) over \(\mathbb Q(\sqrt2,\sqrt5)\).
If infinitely many integral powers occur, there is an arithmetic
progression \(n=r+ht\), \(h>0\), on which
\[
 a_{r+ht}=\left(\sum_{j=1}^s c_j\gamma_j^t\right)^d,
 \qquad t\ge0,
\]
with nonzero algebraic roots. Restrict further to a progression with
even step, and then to a further subprogression annihilating the
torsion of the finitely generated multiplicative group of all roots
on the two sides. Relabel its step as \(h\). The resulting group
generated by those roots is free abelian: taking a common multiple
of torsion orders as a new exponent gives a torsion-free subgroup.

The roots \(u=\alpha^h\) and \(v=\beta^h\) are multiplicatively
independent. Indeed, if \(u^p v^q=1\), the automorphism changing
\(\sqrt5\) to \(-\sqrt5\) and fixing \(\sqrt2\) sends \(u\) to \(u^{-1}\)
and fixes \(v\); division gives \(u^{2p}=1\), hence \(p=q=0\).

In the Laurent group algebra of the resulting free abelian group over
\(\overline{\mathbb Q}\), the left hand side corresponds to
\[
 F=A[u]+B[u^{-1}]+C[v]+D[v^{-1}],
\]
where all four coefficients are nonzero. Distinct group elements
give linearly independent exponential sequences on \(t\ge0\) by
the Vandermonde determinant. The hypothesized identity of sequences
therefore implies \(F=H^d\) in this Laurent polynomial ring.

Choose a real linear functional on the exponent lattice that gives
both \(u\) and \(v\) weight 1; their independence permits such a
functional. The highest-weight part of \(F\) is \(A[u]+C[v]\).
The highest-weight part of a product is the product of the
highest-weight parts, since the Laurent ring is a domain.
Consequently this binomial would be a \(d\)-th power.
But it is a unit times \(A+C[w]^k\), where \(w\) is a primitive
lattice direction and \(k\ge1\). Extend \(w\) to a lattice basis.
Over \(\overline{\mathbb Q}\), the polynomial \(A+Cz^k\) has
\(k\) distinct nonzero roots, so each corresponding irreducible
Laurent factor occurs to multiplicity 1. This contradicts
\(d\ge2\). Thus only finitely many indices can occur. QED.

This proves finiteness for each fixed exponent; it does not give an
effective upper bound for the last square index.

## Theorem 2 (global congruence restriction)

If \(a_n\) is a square, then
\[
 n\equiv 3,\ 360357,\ 360363,\ 720717,\ 720718,\ 720719
 \pmod {720720}.
\]
Equivalently, writing \(M=720720\), the allowed residues are
\(3,M/2-3,M/2+3,-3,-2,-1\) modulo \(M\).

**Proof.** For each modulus \(q\), iterate the state
\((L_n,L_{n+1},P_n,P_{n+1})\) modulo \(q\) from \((2,1,0,1)\).
The update is invertible (both component matrices have determinant
\(-1\)), and the first return to the initial state certifies a full
period. Retain exactly those residues whose sum is a square modulo
\(q\), including zero.

The attached [certificate](verify_sieve.py) uses the moduli
\(3,5,7,11,13,17,19,23,29,31,41,43,71,79,83,89,131,181,
197,199,281,307,467,521,631,881,911,991,1249,1321,16\).
Each certified period divides \(M\). Their simultaneous square-residue
conditions leave exactly the six residues above out of \(M\).
All operations are exact finite integer calculations. QED.

In particular \(a_3=9\) is the only square for \(0\le n<360357\).

## A limitation of finite congruence sieves

Extend the two recurrences backwards. The sums at indices
\(-3,-2,-1,3\) are \(1,1,0,9\), respectively.
For any finite collection of moduli, the combined state has a common
positive period \(T\). Every nonnegative index congruent to one
of those four indices modulo \(T\) passes all square-residue tests.
Therefore a finite periodic congruence sieve alone cannot establish
the complete nonnegative square classification. The remaining task
is to turn Theorem 1 into an effective exclusion, or to give a
direct argument excluding every other nonnegative index.

## Reproduction

Run from this directory:

    python3 verify_sieve.py

The certificate checks all 720720 residues and independently computes
the exact square indices up to 10000 using integer square roots.

## Reference

[1] P. Corvaja and U. Zannier, *Some New Applications of the Subspace
Theorem*, Compositio Mathematica 131 (2002), 319–340, Theorem 2,
p. 322. https://doi.org/10.1023/A:1015594913393
