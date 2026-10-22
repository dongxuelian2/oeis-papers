# A077187 — general-order two-offset construction (2026-10-17)

**PROVED conditional reduction and finite decision theorem. The unrestricted all-primes conjecture is OPEN.**

Define \(\displaystyle M(k)=1\Vert2\Vert\cdots\Vert k\Vert(k-1)\Vert\cdots\Vert1\). For a prime \(p\ge7\), \(p\ne11\), let

\[
r=\operatorname{ord}_p(10)=2^a5^cv,\quad (v,10)=1,\quad
E=1+\max(a,c),\quad T=\operatorname{lcm}(r,\operatorname{ord}_v(10)).
\]

Here \(\operatorname{ord}_1(10)=1\). Let \(S_e=(C_{10^e-1},Y_{10^e-1})\), where \(C\) is the increasing-prefix concatenation and \(Y_k=10^{-D(k)}R_k\) is the normalized reversed prefix. The full digit-layer maps \(F_e\) are affine, periodic from layer \(E\), and every stable \(T\)-layer product is a translation.

Put \(W=S_{pT}\) and \((U,V)=S_T-W\). Then

\[
S_{tT}=W+t(U,V)\pmod p,\qquad t\ge1.
\]

The finite-defect transfer computes \(W\) by \(2(E-1)\) affine maps, while \(S_T\) requires only \(T\) layers; computing \(S_{pT}\) by direct traversal is unnecessary. See the preceding file \`finite_defect_transfer_2026-10-17.md\`.

## Theorem: nonzero drift gives a two-offset witness, for ANY multiplicative order

If \((U,V)\ne(0,0)\), then for some \(1\le t\le p\) and \(j\in\{0,1\}\),

\[
\boxed{p\mid M(10^{tT}+j).}
\]

**Proof.** Write \(W=(C,Y)\), \(X=81C+10\), \(Z=81Y+1\), \(z=10^j\). At \(k=10^{tT}+j\), multiplication by an invertible power of 10 and \(81z\) turns the mountain residue into

\[
10Xz^2-20z+Z+81t(10Uz^2+V).
\]

At \(j=0,1\), the two slopes are proportional to \(10U+V\) and \(1000U+V\). If both vanish, subtracting yields \(990U=0\), forcing \(U=V=0\), since \(p\nmid990\). Choose the nonzero slope and solve linearly for \(t\pmod p\), taking \(1\le t\le p\). No restriction on prime factors of \(r\) was used. QED.

## Exact criterion if both drift coordinates vanish

If \((U,V)=(0,0)\), then

\[
\boxed{\exists k\ge1:\ p\mid M(k)\quad\Longleftrightarrow\quad
\exists 1\le k<10^{2T}:\ p\mid M(k).}
\]

For \(q=10^{e+1}\ne1\), the normalized mountain inside the \(e+1\)-digit window is \(Az+Bz^{-1}-2q/(q-1)^2\), \(z=q^j\), so it has offset period dividing \(r\). If \(q=1\), the residue is quadratic in \(j\), so it has period dividing \(p\). Zero drift makes all stable endpoint states periodic in \(e\) with period \(T\). Every phase occurs in a reference window with \(T\le e<2T\), and each reference window contains more than \(p\) offsets, since \(p\mid10^r-1\) and \(T\ge r\). Thus every later possible zero reappears below \(10^{2T}\).

Combining both branches, **any existing witness** admits the uniform bound \(k\le10^{pT}+1\). This is not a proof that a witness exists for every prime.

## Example: first-window failure does NOT prevent a witness

At \(p=313\),

\[
r=T=312,\quad W=(154,94),\quad(U,V)=(198,283),\quad(X,Z)=(277,103).
\]

The first \(pT\)-window quadratic has no subgroup root. For \(j=1\), its constant is \(211\) and the slope is \(267\pmod{313}\); choosing \(t=-211/267\equiv25\) gives

\[
\boxed{313\mid M(10^{7800}+1).}
\]

Independent direct iteration through all 7,800 digit layers confirms the exact congruence. Additional verification: 97 primes below 550 gave nonzero-drift witnesses; 74 of these were checked by a full digit-layer traversal; and 1,748 exact comparisons checked the general window residue formulas. These finite checks **do not prove** universal nonzero drift.

**Remaining gap:** exclude zero-drift root-free periodic orbits, or prove they still have witnesses. A general all-primes proof has not been obtained. The new theorem is a general-order sufficient criterion and can coexist with the smooth-order material in PR #8.
