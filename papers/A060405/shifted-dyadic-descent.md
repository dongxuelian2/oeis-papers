# Dyadic factors at a fixed valuation of the index offset

Let \(n_0\in\{3,-3,-1\}\), write \(n=n_0+k\) with
\(k=2^a m\), and suppose \(a\ge4\) and \(m\) is odd.
The [extended lifting certificate](extended-lifting.md) gives
\(a\ge14\) for a square index \(n\) with \(k>0\).
Use \(\alpha=(1+\sqrt5)/2\), \(\beta=1+\sqrt2\),
\(\eta=\beta/\alpha^2\), and \(\xi=\beta\alpha^2\).
For \(j\ge1\), set
\[
 d=2^j,\qquad C_j=L_{2d}+2Q_d.
\]

## Mixed and companion dyadic factors

The conjugates of \(\eta^d\) are
\(\eta^d,\xi^d,\eta^{-d},\xi^{-d}\). Pairing each with its
inverse gives
\[
 N_{\mathbb Q(\sqrt2,\sqrt5)/\mathbb Q}(\eta^d+1)
 =\big(\beta^d+\beta^{-d}+\alpha^{2d}+\alpha^{-2d}\big)^2
 = C_j^2.
\]
For \(j=0\), the norm of \(\eta+1\) is \(-1\) by the odd norm
formula in [coupled norm descent](coupled-norm-descent.md) §6.
The Lucas and Pell companion factors at \(j=0\) are both 1.

Let \(p\mid C_j\) with \(j<a\), and choose a prime ideal
over \(p\) where \(\eta^d=-1\). The order of \(\eta\) is
\(2d\), so \(\eta^k=1\). Put \(t=\alpha^k\),
\(b=\alpha^{n_0}\), and \(c=\beta^{n_0}\) in this residue field.
Then \(\beta^k=t^2\) and
\[
 t^2 a_n=\frac{c t^4+c^{-1}}{2\sqrt2}+b t^3-b^{-1}t.
\]
The shifted square equation becomes
\[
 t^2(x^2-a_{n_0})=(t-1)
 \left(\frac{(t+1)(c t^2-c^{-1})}{2\sqrt2}+b t^2+b^{-1}t\right).
\]
In the signed identities of [coupled norm descent](coupled-norm-descent.md) §2,
the product on the right reduces to
\((\eta^{n_0}-\sigma)(\xi^{n_0}t^4-\sigma)\).
The factor \(\eta^{n_0}-\sigma\) is a unit because \(n_0\)
is odd and \(2d\ge4\). The two companion factors
\(L_d,Q_d\) correspond to \(\alpha^{2d}=-1,\beta^{2d}=-1\),
respectively, giving exact order \(4d\) for the indicated unit.

## A criterion for simultaneous square residues

For an odd prime \(p\ne5\), let \(e_p\) be the maximum of the
two valuations at 2 of the orders of the Lucas and Pell
recurrence matrices modulo \(p\).

**Proposition.** Fix \(a\ge4\). Consider any finite collection
of moduli \(p^h\), where every \(p\) divides \(C_jL_{2^j}Q_{2^j}\)
for some \(1\le j<a\). Suppose \(e_p\le a+1\) for each \(p\)
that splits completely in \(\mathbb Q(\sqrt2,\sqrt5)\).
For each anchor \(n_0\), infinitely many positive \(n\) satisfy
\(v_2(n-n_0)=a\) and make \(a_n\) a square modulo every chosen
prime power. The offsets can also be taken divisible by any
prescribed odd integer.

**Proof.** The terms \(L_{2^j}\) and \(Q_{2^j}\) are odd.
The initial values \(L_2=Q_2=3\) and the doubling formulas
\(L_{2d}=L_d^2-2\), \(Q_{2d}=2Q_d^2-1\) show that
these terms and \(C_j\) are coprime to 5. For the latter
claim, \(C_1=13\), and for \(j\ge2\) one has \(L_{2d}\equiv
Q_d\equiv2\pmod5\).

It suffices to prove \(e_p\le a+1\) at the primes that
have residue degree two. If 2 is a nonsquare modulo \(p\),
then \(p\equiv3,5\pmod8\) and \(v_2(p^2-1)=3\). Both
recurrence matrices diagonalize over \(\mathbb F_{p^2}\).
If 2 is a square and 5 a nonsquare, then
\(\beta\in\mathbb F_p^\times\) and
\(\alpha^{p+1}=-1\) in \(\mathbb F_{p^2}\).
For \(p\equiv1\pmod8\), the order of \(\alpha\) has
valuation 2 at 2. For \(p\equiv7\pmod8\), the order of
\(\beta\) has valuation at most 1 at 2.
At a prime dividing \(C_j\), Frobenius exchanges
\(\eta,\xi\), so \(\eta^d=\xi^d=-1\). Hence
\(\beta^{2d}=\alpha^{4d}=1\), giving \(e_p\le j+2\).
At a prime dividing \(L_d\) or \(Q_d\), the order of
the indicated unit is \(4d\). If \(p\equiv1\pmod8\),
only \(Q_d\) can vanish, and if \(p\equiv7\pmod8\),
only \(L_d\) can vanish. In both cases \(e_p\le j+2\).
The conjugate of each unit is its negative inverse, which
preserves these upper bounds on the valuations at 2.

Choose \(m\) divisible by the odd parts of the matrix orders
modulo all the chosen prime powers and by the prescribed odd
integer. The reduction kernels from modulus \(p^h\) to \(p\)
are \(p\)-groups, so the valuations at 2 of the orders are
unchanged. For such an odd \(m\), each matrix raised to
\(k=2^a m\) has order dividing two modulo \(p^h\).
Its eigenvalues modulo \(p\) are equal signs, because the
original eigenvalues are negative inverses and \(k\) is even.
The matrix is therefore that scalar sign modulo \(p\), and
the reduction kernel of odd order gives the same sign modulo
\(p^h\). Write the two signs as \(\delta_L,\delta_P\).
It follows that
\(a_n\equiv\delta_L L_{n_0}+\delta_P P_{n_0}\pmod{p^h}\).

If both signs are positive, this is \(a_{n_0}\).
A negative sign requires \(2\) to be a square modulo \(p\),
since otherwise \(e_p\le3\). If just the Lucas sign is
negative, the value is \(a_{-n_0}\in\{1,9,2\}\), a square
modulo every power of such a \(p\).
If the Pell sign is negative, the order of \(\beta\) has
valuation \(a+1\) at 2 and \(\beta\in\mathbb F_p^\times\).
Thus \(p\equiv1\pmod{2^{a+1}}\), and \(-1\) and 2 are
squares modulo every power of \(p\). The resulting values
\(-a_{n_0}\) or \(-a_{-n_0}\) are squares as well.
All positive odd multiples of the resulting odd modulus for
\(m\) are admissible. \(\square\)

## Exact range of the prime test

**Corollary.** For every fixed \(a\ge14\) the preceding proposition
applies to all primes \(p\le10^8\) in the layers \(1\le j<a\).
In particular, the prescribed odd integer can be
\(720720/16\), or the odd part of the larger forced divisor for
the chosen anchor.

The [certificate](verify_shifted_dyadic.py) checks this as follows.
A possible exception must split completely and satisfy
\(p\equiv1\pmod{2^{16}}\). For each such prime up to \(10^8\),
it computes \(e_p\) by removing the odd part of \(p-1\) from
the matrix orders. An exception would have \(14\le a\le e_p-2\)
and consequently \(1\le j\le e_p-3\). The certificate tests
that finite range by doubling modulo \(p\). It finds zero
exceptions among the 80 primes tested.

The local coverage question for this approach is whether
the deeper order condition \(e_p\ge a+2\) can supply
obstructions uniformly in \(a\ge14\). For the families above,
this condition confines the search to completely split primes
with \(p\equiv1\pmod{2^{a+2}}\).

Run \(\texttt{python verify_shifted_dyadic.py}\) from this directory.
