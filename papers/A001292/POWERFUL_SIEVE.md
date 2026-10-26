# Powerful values of cyclic concatenations have density zero

Detailed companion to Section 3 of [the manuscript](main.pdf).

Qichao Wang (Hebei University of Technology) and Daoyu Dong
(University of Electronic Science and Technology of China), October 26, 2026.

## Theorem

Fix an integer base `g >= 2`. Let `W_m` concatenate the base-`g`
representations of `1,2,...,m`. Let `R_(m,k)` move its first `k` whole
integer blocks to the end, for `0 <= k < m`. An integer is **powerful**
if every prime dividing it occurs to exponent at least two.

As `X` tends to infinity,

\[
\boxed{\#\{(m,k):2\le m\le X,\ 0\le k<m,
 R_{m,k}\text{ is powerful}\}
 \ll_g \frac{X^2(\log\log X)^2}{\log X}.}                 \tag{1}
\]

Every nontrivial perfect power is powerful. Consequently, for OEIS
A001292,

\[
\boxed{\#\{n\le N:a(n)>1\text{ is a perfect power}\}
 \ll \frac{N(\log\log N)^2}{\log N}.}                    \tag{2}
\]

These terms have natural density zero. The argument treats every power
exponent together. It permits a sparse exceptional set; Kashihara's
assertion that this set is empty remains open. All logarithms are natural.

## 1. A uniform affine-exponential formula

Let `D(k)` count the digits of `W_k`, with `W_0=D(0)=0`. Moving the prefix
gives

\[
R_{m,k}=g^{D(k)}W_m-(g^{D(m)}-1)W_k.                      \tag{3}
\]

Fix the digit length `d` of `m`, and put

\[
B=g^d,\quad L=g^{d-1},\quad c=B-1,\quad
A=c^2W_{L-1}+Lc+1.
\]

For `L-1 <= m <= B-1`, writing `t=m-L+1`,

\[
c^2W_m=A B^t-((m+1)c+1),\qquad
D(m)=D(L-1)+dt.                                         \tag{4}
\]

Indeed, the first identity holds at `m=L-1`, and appending `m+1`
multiplies `c^2W_m+((m+1)c+1)` by `B`.
For fixed `k`, set `u=g^{D(k)}`. Substituting (4) into (3) gives

\[
R_{m,k}=\alpha B^m+\beta m+\gamma,                        \tag{5}
\]

with rational coefficients

\[
\begin{split}
\alpha&=\left(\frac{uA}{c^2}-g^{D(L-1)}W_k\right)B^{1-L},\\
\beta&=-\frac uc,\qquad \gamma=W_k-\frac{uB}{c^2}.
\end{split}
\]

For every prime `p` not dividing `g(B-1)`, the coefficients are defined
modulo `p^2`, and `beta` is a unit modulo `p`. The formula supplies a
periodic modular extension outside the digit interval, used only for
counting residue classes. The coefficient sizes do not enter the estimates.

## 2. Local densities, including overlapping periods

**Lemma 1.** Let `p` be prime with `p` not dividing `B`, and let
`f(n)=alpha*B^n+beta*n+gamma (mod p^2)`, where `beta` is a unit modulo `p`.
The condition `p | f(n)` and `p^2` not dividing `f(n)` has period dividing
`T_p=p^2(p-1)`. In each fixed phase modulo `p-1`, exactly `p-1` of the
`p^2` residue classes modulo `p^2` satisfy it. Its density is

\[
\rho_p=(p-1)/p^2.                                       \tag{6}
\]

**Proof.** Write `n=a+(p-1)s` in a fixed phase. Modulo `p`, the
exponential term is constant and the linear coefficient of `s` is
nonzero. Thus precisely one class `s (mod p)` gives `f(n)=0 (mod p)`.
Its `p` lifts change `n` by `p(p-1)h`. Euler's theorem makes the
exponential term constant modulo `p^2`; the linear term changes by
`beta*p*(p-1)*h`. Precisely one lift is zero modulo `p^2`, leaving
`p-1` with valuation one. Both terms have period dividing `T_p`. QED.

**Lemma 2.** For any finite set `S` of eligible primes, these conditions
have simultaneous density

\[
\rho(S)=\prod_{p\in S}\rho_p                             \tag{7}
\]

in a period dividing `lcm(T_p : p in S)`.

**Proof.** Induct on the largest prime `q` in `S`. The smaller-prime
conditions have a joint period `T` whose prime divisors are all less
than `q`, because each constituent is `p^2(p-1)` with `p<q`. Therefore
`q` does not divide `H=lcm(T,q-1)`.

Fix a class modulo `H`. The smaller-prime conditions are fixed, while
the Chinese remainder theorem lets `n (mod q^2)` vary freely. The phase
modulo `q-1` is fixed, so Lemma 1 gives a fraction `rho_q` in each such
class. Averaging multiplies the smaller-prime density by `rho_q`.
Projection from `H` to `T` preserves the uniform distribution. This
proves (7), including when a smaller prime divides a larger prime minus
one; pairwise coprimality of periods is not required. QED.

For an interval `I` of `h` consecutive integers, it follows that

\[
\#\{n\in I:\text{all conditions for }p\in S\}
 =h\rho(S)+O\!\left(\prod_{p\in S}p^3\right).            \tag{8}
\]

The absolute interval error is at most the joint period, which is at
most `prod p^2(p-1) < prod p^3`.

## 3. A finite sieve inequality

Take eligible primes `P` at most `z`, write `lambda=sum_(p in P) rho_p`,
and let `K>=0` be even. Powerful values avoid every valuation-one event.
Bonferroni's inequality and (8) give

\[
\boxed{\#\{n\in I:f(n)\text{ is powerful}\}
 \le h\left(e^{-\lambda}+\frac{\lambda^{K+1}}{(K+1)!}\right)
       +(K+1)z^{4K}.}                                    \tag{9}
\]

To justify the main term explicitly, let `e_j` be the elementary
symmetric sums of the numbers `rho_p`. The even inclusion-exclusion
sum is at most `prod(1-rho_p)+e_(K+1)`, by the finite Bonferroni
remainder inequality applied to independent events with probabilities
`rho_p`. This is an algebraic inequality in these numbers. Moreover,
`prod(1-rho_p)<=exp(-lambda)` and `e_(K+1)<=lambda^(K+1)/(K+1)!`.
For each subset of size `j`, (8) costs at most `z^(3j)`, and there are
at most `z^j` subsets. Summation for `0<=j<=K` proves the error in (9).
It also bounds integers avoiding all the specified events if the
extension of `f` is only defined as modular data. All constants are
uniform in the coefficients and the interval endpoints.

## 4. The digit length and the primes grow together

For the fixed base `g`, choose

\[
\eta=\frac{\log g}{100},\quad
z=\exp\!\left(\frac{\eta d}{\log d}\right),\quad
K=2\lceil4\log d\rceil,
\]

and use the primes in `(d^2,z]` not dividing `g(g^d-1)`. For large `d`,
`z>d^2`. Omitted primes larger than `d^2` dividing `g^d-1` number at most
`log(g^d-1)/(2 log d)`, so their reciprocal sum is `O_g(1/(d log d))`.
Primes dividing the fixed base are eventually below `d^2`. Mertens'
prime reciprocal estimate consequently gives

\[
\begin{split}
\lambda
 &=\sum_{\substack{d^2<p\le z\\p\nmid g(g^d-1)}}
       \left(\frac1p-\frac1{p^2}\right)\\
 &=\log\log z-\log\log(d^2)+O_g(1)\\
 &=\log d-2\log\log d+O_g(1).                            \tag{10}
\end{split}
\]

Thus `0<lambda<=log d` for sufficiently large `d`, and
`exp(-lambda) <<_g (log d)^2/d`. Using `n! >= (n/e)^n` and `K>=8 log d`,

\[
\frac{\lambda^{K+1}}{(K+1)!}\le(e/8)^{K+1}\le d^{-8}.
\]

Also `K<=10 log d` eventually, whence

\[
\log((K+1)z^{4K})\le\log(K+1)+40\eta d
                  <\tfrac12 d\log g.
\]

Applying (9) to (5) proves the uniform estimate

\[
\#\{m\in I:R_{m,k}\text{ is powerful}\}
 \ll_g |I|\frac{(\log d)^2}{d}+g^{d/2},                  \tag{11}
\]

for every fixed `k` and every interval `I` inside `L<=m<=B-1` with
`m>k`. The constant and the threshold depend only on `g`.

## 5. Summing rotations and passing to sequence indices

Let `D` be the base-`g` digit length of `floor(X)`. For each `d<=D` and
each `k`, use the interval

\[
\max(g^{d-1},k+1,2)\le m\le\min(X,g^d-1).
\]

These intervals cover exactly the relevant pairs. There are at most
`g^d` choices of `k`, so the sum of the errors in (11) is
`sum_(d<=D) g^(3d/2) = O_g(X^(3/2))`. The blocks `d<=D/2` contain
`O_g(X)` pairs and may be bounded trivially. On the other blocks,
`(log d)^2/d << (log D)^2/D`, and there are `O(X^2)` pairs in total.
This proves (1).

Each block `m` supplies `m` distinct rotations. For `m` with `d>=2`
digits, the cyclic digit word has a unique occurrence of `1` followed
by `d-1` zeros, representing `g^(d-1)`. A run of `d-1` zeros must lie
inside one `d`-digit integer, since every integer block starts with a
nonzero digit. The marker cannot cross the cyclic join, whose next
digit is `1`. Its uniqueness forbids any nonidentity digit rotation
fixing the word. For `d=1`, the digits are distinct.

All rotations have the same digit length `D(m)`, which increases
strictly with `m`. The sequence through block `m=X` therefore has
exactly `X(X+1)/2` entries. Any sequence prefix ending inside the next
block is bounded by that full block. Taking `X` of order `sqrt(N)` in
(1) proves (2). QED.

## Checks and references

`verify_powerful_sieve.py` checks the local phase counts, simultaneous
densities with overlapping periods, literal rotation identities in five
bases, and the finite Bonferroni inequality. Equations (3)--(11), rather
than these finite checks, establish the asymptotic theorem.

- OEIS [A001292](https://oeis.org/A001292).
- Marco Ripà, *On some open problems concerning perfect powers*,
  [arXiv:2205.10163v4](https://arxiv.org/html/2205.10163v4), 2024 revision.
- F. Mertens, *Ein Beitrag zur analytischen Zahlentheorie*, Journal für
  die reine und angewandte Mathematik **78** (1874), 46--62,
  [doi:10.1515/crll.1874.78.46](https://doi.org/10.1515/crll.1874.78.46).
  Only the classical estimate `sum_(p<=y) 1/p = log log y + O(1)` is used.
