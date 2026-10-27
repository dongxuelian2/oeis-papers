# Norm restrictions on stationary Lucas collisions

Let \(L_0=2,L_1=1\), \(F_0=0,F_1=1\), and \(L_{n+2}=L_{n+1}+L_n\).
Write \(\alpha=(1+\sqrt5)/2\), \(\beta=(1-\sqrt5)/2\), so
\(\alpha\beta=-1\). The results below refine the finite stationary-pattern
criterion of the coefficient manuscript.

## 1. Necessary square-norm equation

**Proposition.** Suppose \(q\ge2\), \(i<k\), \(j<\ell\), and
\[
qL_{n+k}-L_{n+\ell}=qL_{n+i}-L_{n+j}
\]
holds for every \(n\ge0\). Put \(h=k-i\), \(e=\ell-j\), and
\[
C(d)=L_d-1-(-1)^d \quad(d\ge1).
\]
Then
\[
\boxed{e>h,\qquad j\equiv i\pmod2,\qquad q^2 C(h)=C(e).}
\]

*Proof.* Rearrange as
\(q(L_{n+k}-L_{n+i})=L_{n+\ell}-L_{n+j}\).
Independence of the two Binet exponentials yields
\[
q\alpha^i(\alpha^h-1)=\alpha^j(\alpha^e-1),\qquad
q\beta^i(\beta^h-1)=\beta^j(\beta^e-1).
\]
The algebraic norm of \(\alpha^d-1\) is
\[
(\alpha^d-1)(\beta^d-1)=1+(-1)^d-L_d=-C(d).
\]
Taking norms gives
\(q^2(-1)^i C(h)=(-1)^j C(e)\).
As both \(C(h)\) and \(C(e)\) are positive, \(j-i\) is even
and \(q^2C(h)=C(e)\). The latter implies \(e>h\), because
\(q\ge2\) and \(C\) is nondecreasing, strictly increasing
from index \(2\) onward. This proves the proposition.

The norm equation is a necessary condition. Exact equality at
two consecutive shifts and positivity remain to be tested.

## 2. Complete classification when both index gaps are even

The double-angle identities yield
\[
C(2r)=L_{2r}-2=
\begin{cases}
L_r^2,&r\text{ odd},\\
5F_r^2,&r\text{ even}.
\end{cases}
\]

**Proposition.** For even gaps \(h=2r\), \(e=2m\),
where \(m>r\ge1\), there exists a positive stationary
collision in \(T_q\), with integer \(q\ge2\), **if and only if**
\(r,m\) have the same parity and
\[
q=
\begin{cases}
L_m/L_r\in\mathbb Z,&r,m\text{ odd},\\
F_m/F_r\in\mathbb Z,&r,m\text{ even}.
\end{cases}
\]

*Proof.* The norm equation is \(q^2C(2r)=C(2m)\).
Opposite parities would require a rational square to equal
five times a rational square, which is impossible.
Equal parity gives the displayed quotient. Conversely,
\[
L_{n+2r}-L_n=
\begin{cases}
L_rL_{n+r},&r\text{ odd},\\
5F_rF_{n+r},&r\text{ even}
\end{cases}
\]
establishes, for each integral quotient,
\[
qL_{n+m-r}-L_n=qL_{n+m+r}-L_{n+2m}>0
\]
for all \(n\ge1\). The gaps are exactly \(2r\) and \(2m\).
Increasing \(n\) gives infinitely many distinct repeated
positive values.

Thus the Lucas/Fibonacci integer-quotient families in the
current manuscript **exhaust all stationary identities in
which both index gaps are even**.

## 3. Restrictions involving odd gaps

For odd \(d\), \(C(d)=L_d\). For every \(r\ge1\),
\(C(4r)=5F_{2r}^2\). The Lucas residues modulo five
have the repeating nonzero cycle \(1,3,4,2\).
Therefore one odd gap and one gap divisible by four
cannot satisfy the norm equation: the valuations at five
would have opposite parity.

If the gaps have opposite parity, their even member must
be congruent to \(2\pmod4\). In that case the norm equation
forces the odd-index Lucas term involved to be a perfect
square. This follows since an integer which is the square
of a rational is the square of an integer.

For two odd gaps the remaining norm equation is
\[
L_e=q^2L_h,\qquad e>h\ge1,\qquad h,e\text{ odd}.
\]
The norm equation alone is not treated as a complete
criterion for this case.

## 4. Exact norm-pruned search

Use the proved bound
\[
t=\min\{n\ge1:L_n>200(q+1)^4\},\qquad K=12t+1.
\]
The complete stationary window in the manuscript implies
\[
1\le h=K-i<3t,\qquad 1\le e=\ell-j\le7t.
\]
For \(q\ge2\), \(q^2C(h)\ge4\), while \(C(e)\)
is strictly increasing for \(e\ge3\). Consequently,
**each candidate first gap \(h\) determines at most one
second gap \(e\)** via \(q^2C(h)=C(e)\).

For \(e\ge3\), the function \(j\mapsto L_{j+e}-L_j\)
is strictly increasing for \(j\ge1\). Binary search
therefore finds the only possible \(j\) satisfying
\[
q(L_K-L_{K-h})=L_{j+e}-L_j.
\]
The algorithm then checks parity, the next shifted equality
and positivity. The original finite stationary theorem
makes this procedure both necessary and sufficient.

The implementation **norm_stationary.py** uses exact integer
arithmetic. After generating Lucas numbers and the norm
lookup table, it requires \(O(t\log t)\) index comparisons;
the bit cost also depends on the integer lengths.
The independent regression script **verify_norm_stationary.py**
compares full pattern lists to the original direct search
for every \(q=2,\ldots,200\), verifying all five further
shifts per pattern. It finds only **26 norm-compatible gap
pairs** among those 199 coefficients, with precisely the
same **19** coefficients having infinite collisions.

These results are an additional research note and verifier.
The two existing manuscript PDFs are unchanged.
