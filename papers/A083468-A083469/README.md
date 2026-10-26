# A083468 and A083469: universal nonvanishing and exact power-of-ten minima

**Status (2026-10-22):** Universal existence proved for both sequences; exact minima now proved on the infinite family n=10^r (r>=1). No all-index formula is claimed.

**Authorship:** Qichao Wang, Hebei University of Technology. This continuation preserves the historical author of the already accepted OEIS manuscript.

## Definitions

For a positive integer \(n\), write \(u\Vert v\) for decimal concatenation. OEIS [A083468](https://oeis.org/A083468) is the smallest multiple of \(n\) obtained by concatenating \(n\) consecutive positive integers in **decreasing** order, or zero if none exists. OEIS [A083469](https://oeis.org/A083469) equals A083468\((n)/n\).

## Theorem (reverse concatenations; in fact, arbitrary permutations)

Let \(\beta\ge2\) be even, \(n\ge1\), and let \(\pi:\{1,\ldots,n\}\to\{0,\ldots,n-1\}\) be any bijection. There exist positive integers \(d,k\) such that \(k,k+1,\ldots,k+n-1\) all have exactly \(d\) base-\(\beta\) digits and

\[
  n\mid (k+\pi(1))\Vert_\beta(k+\pi(2))\Vert_\beta\cdots\Vert_\beta(k+\pi(n)).
\]

Moreover, infinitely many choices of \(d\) are possible.

### Proof

Write \(n=qm\), where \(q\) is the largest divisor of \(n\) supported on primes dividing \(\beta\). Then \(\gcd(q,m)=1\), \(\gcd(m,\beta)=1\), and **\(m\) is odd**, because \(\beta\) is even.

Take an arbitrarily large digit length \(d\) so that

\[
q\mid\beta^d, \qquad \beta^d\equiv1\pmod m.
\]

Both conditions can be met simultaneously: the first holds for all sufficiently large \(d\), and the second holds when \(d\) is a multiple of the multiplicative order of \(\beta\) modulo \(m\) (vacuous for \(m=1\)). We can also require the interval

\[
\beta^{d-1}\le k\le\beta^d-n
\]

to contain at least one representative of every residue class modulo \(q\). Pick one satisfying

\[
k+\pi(n)\equiv0\pmod q.
\]

All \(n\) blocks then have exactly \(d\) digits. Set \(B=\beta^d\) and call their concatenation \(C\). Since \(q\mid B\), reducing the base-\(B\) polynomial for \(C\) modulo \(q\) leaves only its **last** block:

\[
C\equiv k+\pi(n)\equiv0\pmod q.
\]

Since \(B\equiv1\pmod m\), the order of the blocks disappears modulo \(m\):

\[
C\equiv\sum_{j=0}^{n-1}(k+j)=nk+\frac{n(n-1)}2\equiv0\pmod m.
\]

Indeed, \(m\mid n\) and \(m\) is odd, so \(m\) divides both terms. By the Chinese remainder theorem, \(n=qm\mid C\). Taking \(d\) arbitrarily large yields infinitely many distinct concatenations. \(\square\)

### Corollary (OEIS A083468 and A083469)

Take \(\beta=10\) and \(\pi=(n-1,n-2,\ldots,0)\). Then for every \(n\ge1\) there are infinitely many reverse concatenations of \(n\) consecutive positive integers divisible by \(n\). In particular,

\[
\boxed{\mathrm{A083468}(n)>0,\qquad\mathrm{A083469}(n)=\mathrm{A083468}(n)/n>0.}
\]

This is an existence theorem, **not** a minimality formula. The minima still require separate search or analysis.

## Exact minima on every power of ten

For every integer `r>=1`, put `N=10^r` and `B=10^(r+1)=10N`. We prove:

```
A083468(N) = concat(2N-1, 2N-2, ..., N)
           = sum((N+j)*B^j for j=0,...,N-1).
A083469(N) = A083468(N)/N.
```

This is an **exact minimum**, not a large constructive upper bound. In fact, for every integer base `b>=2` and `N=b^r`, the descending `N`-block concatenation ending at any positive integer `a` is divisible by `N` **if and only if `N|a`**. If the last block has fewer than `r` digits, its nonzero leading digit prevents the final `r` digits of the whole concatenation from being all zero; otherwise all preceding blocks vanish modulo `b^r`, leaving precisely `a mod N`. The concatenated number increases with the final block, hence `a=N` is the least possibility.

All `N` blocks in the minimum are `r+1` digits long. A closed arithmetic expression for the concatenation is

```
((2*N-1)*B^(N+1) - 2*N*B^N - (N-1)*B + N) / (B-1)^2.
```

For `N=10`: **A083468(10)=19181716151413121110** and **A083469(10)=1918171615141312111**. The independent verifier eliminates every shorter final block for `N=10,100,1000` and checks the exact geometric-sum formula.

This result supplements the original universal existence proof; it is not an all-index minimization theorem. Broader literature priority for the special-family formula has not been exhaustively checked.

## Explicit decimal witness algorithm

For fixed \(n\), let \(q=2^{v_2(n)}5^{v_5(n)}\), \(m=n/q\). Choose any sufficiently large \(d\) such that \(q\mid10^d\) and \(10^d\equiv1\pmod m\), and choose a multiple \(a\) of \(q\) in

\[
10^{d-1}\le a\le10^d-n.
\]

Then \((a+n-1)\Vert\cdots\Vert(a+1)\Vert a\equiv0\pmod n\). One explicit choice is

\[
a=q\left\lceil\frac{10^{d-1}}q\right\rceil,
\]

provided \(d\) is large enough that \(9\cdot10^{d-1}\ge q+n-1\). For the multiplicative-order constraint, a positive multiple of \(\mathrm{ord}_m(10)\) works when \(m>1\).

Example: \(n=4\), \(d=2\), \(a=12\) yields \(15\Vert14\Vert13\Vert12=15141312\), which is divisible by 4 (though not the minimal A083468\((4)=5432\)).

## Paper (PDF and LaTeX)

- [Read the revised proof with exact minimum theorem (main.pdf)](main.pdf).
- [LaTeX source (main.tex)](main.tex).
- To rebuild with a TeX installation: `pdflatex -interaction=nonstopmode -halt-on-error main.tex` (run twice to resolve references).

The paper includes the even-base arbitrary-permutation theorem, its reverse-concatenation corollary, the new exact power-of-ten minimum theorem, and a clear distinction between that restricted formula and general existence.

## Independent verification

Run `python verify_reverse_concatenation.py`. Checks include:

- the explicit witness construction and modular concatenation for every \(1\le n\le512\);
- direct exact-integer verification in compact cases;
- an independent brute-force minimum search reproducing the first 16 A083468 terms listed by OEIS;
- the A083469 quotient relation for the same 16 terms;
- exact power-of-ten minima and modular exclusion of every smaller final block for n = 10, 100, 1000.

The numerical checks support the implementation; **the theorem, not the finite tests, proves the universal statement.**

## Previous work and attribution

This corollary is already a direct consequence of the **Even-base AP divisibility** theorem (take common difference \(s=-1\)) in Qichao Wang, *Divisibility of Concatenated Arithmetic Progressions and Champernowne Prefixes*, [source and verification package](https://github.com/dongxuelian2/oeis-papers/tree/main/papers/A075000-A075002). The proof above makes the additional observation that, for consecutive integers, **any predetermined block permutation** is possible. No novelty assertion is made for this strengthening without a separate literature search.

OEIS: [A083468](https://oeis.org/A083468), [A083469](https://oeis.org/A083469). Original project methods: [three-term-decimal-concatenation-square-sum](https://github.com/dongxuelian2/three-term-decimal-concatenation-square-sum).

## Suggested OEIS comments (paste into the respective entries)

**A083468, COMMENTS:**

> For every n >= 1, a(n) > 0. In fact, infinitely many concatenations of n consecutive positive integers in decreasing order are divisible by n. This follows from the even-base arithmetic-progression divisibility theorem of Q. Wang (2026), by choosing base 10 and common difference -1. Proof and independent checks: https://github.com/dongxuelian2/oeis-papers/tree/main/papers/A083468-A083469

**A083469, COMMENTS:**

> For every n >= 1, a(n) is well-defined and positive: the reverse-concatenation existence theorem proves that A083468(n) > 0, and a(n) = A083468(n)/n (Wang, 2026). Proof: https://github.com/dongxuelian2/oeis-papers/tree/main/papers/A083468-A083469

These are proposed comments, **not yet submitted to OEIS**.