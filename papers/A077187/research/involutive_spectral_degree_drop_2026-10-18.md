# A077187: involutive cancellation of the quadratic spectral term

**2026-10-18. Fully algebraic theorem for fixed coprime parts
\(v\mid99\).** The theorem explains the exact degree drop observed
in the \(v=11\) infinite-family certificate; it does not, by itself,
prove nonzero drift for \(v=33\) or \(99\).

## Theorem (spectral degree drop under an involution)

Let \(p\ge7\) be a prime with \(r=\operatorname{ord}_p(10)=uv\),
where \(u=2^a5^c\) and \((v,10)=1\). Put
\[
\ell=\operatorname{lcm}(v,\operatorname{ord}_v(10)),\quad
g=\gcd(r,\ell),\quad m=r/g,\quad \zeta=10^m\bmod p.
\]
In the universal spectral compression of
\`fixed_v_spectral_compression_v7_2026-10-18.md\`, the two drift
coordinates are represented as degree-at-most-two polynomials
\(U(m)=U_0+U_1m+U_2m^2\) and
\(V(m)=V_0+V_1m+V_2m^2\) over
\(\mathbb Q(\zeta_g)\).

**If \(10^2\equiv1\pmod v\) (equivalently \(v\mid99\)), then**
\[
\boxed{U_2=V_2=0\quad\text{as cyclotomic algebraic numbers}.}
\]

### Proof

The case \(v=1\) is immediate since all stable multipliers are 1.
For \(v>1\), the stable multipliers have the finite phase formula
\[
A_j=\zeta^{(g/v)\gamma\,9j10^{j-1}},\qquad
\gamma=u^{-1}\pmod v,\qquad A_{j+\ell}=A_j.
\]
Since \(10^2\equiv1\pmod v\), we have
\(10^{-j-1}\equiv10^{j-1}\pmod v\). Hence
\[
\boxed{A_{-j}=A_j^{-1}} \qquad(j\bmod\ell).
\]
Also \(A_0=1\) and \(\prod_{j=1}^{\ell}A_j=1\).
Let \(P_j=\prod_{i=1}^{j-1}A_i\), with \(P_1=P_{\ell+1}=1\).
Pairing the tail of the full period with the inverse multipliers
gives the *palindromic phase*
\[
\boxed{P_{\ell+1-j}=P_j}
\quad\Longrightarrow\quad
P_{\ell-j}=P_{j+1}.
\]

Define \(\alpha_j=P_j^{-1}-P_{j+1}^{-1}\) and
\(\beta_j=P_{j+1}-P_j\). It follows that
\[
\alpha_{\ell-j}=-\alpha_j,\qquad
\beta_{\ell-j}=-\beta_j.
\]

The coefficient of \(m^2\) in the regular coset sum
\(F_2\) is
\[
f(c)=\frac{c}{(c-1)^2}\quad(c\ne1),
\]
and at \(c=1\) it is \(f(1)=-1/12\).
In every case
\[
\boxed{f(c^{-1})=f(c).}
\]
The spectral formula consequently gives
\[
U_2=\sum_{j=1}^{\ell}\alpha_j f(\zeta^j),
\qquad
V_2=-\sum_{j=1}^{\ell}\beta_j f(\zeta^j).
\]
The involution \(j\mapsto\ell-j\) sends
\(\zeta^j\) to its inverse and negates both coefficients.
Every pair therefore cancels, including fixed points where
\(\alpha_j=\beta_j=0\) in odd characteristic. Thus \(U_2=V_2=0\).
This is an exact cyclotomic identity, independent of \(u,p,m\).
QED.

## Scope and consequence

All possible \(v\mid99\) are
\[
v\in\{1,3,9,11,33,99\}.
\]
The cases \(v\mid9\) were already solved by an elementary explicit
drift invariant. The new \(v=11\) family is certified by fixed-degree
**linear** resultants. For \(v=33,99\), the same analytic argument
proves a linear spectral representation, reducing their future
elimination work; **it does not prove nonzero drift** for those
two families.

This illustrates the appropriate research strategy: first expose
symmetries in the bounded spectral cocycle; only afterwards calculate
the smaller resultant needed for an actual infinite family.
