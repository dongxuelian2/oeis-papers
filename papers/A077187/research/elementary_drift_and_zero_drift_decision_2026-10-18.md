# A077187: elementary drift invariant and a sharper zero-drift test

**2026-10-18.** This is a continuation of \`unrestricted_order_dichotomy_2026-10-17.md\`.
**PROVED:** the invariant and finite decision reduction below. **OPEN:** the
unrestricted all-primes existence conjecture. Computations below are evidence,
not a proof for primes beyond the checked range.

## 1. An elementary nonzero-drift family

Let \(p\ge7\) be prime, \(p\ne11\), and
\[
r=\operatorname{ord}_p(10)=2^a5^cv,\quad (v,10)=1,\quad
S_d=(C_{10^d-1},\,10^{-D(10^d-1)}R_{10^d-1})\in\mathbb F_p^2.
\]
Write \(\Delta=(U,V)=S_{2r}-S_r\) when \(v\mid9\).

**Theorem.** If \(v\mid9\) (equivalently \(v=1,3,9\)), then
\[
\boxed{U+V=9\cdot 100^{-1}\pmod p\ne0.}
\]
Consequently the general two-offset drift theorem produces a divisible
mountain with \(k=10^{jr}\) or \(10^{jr}+1\), \(1\le j\le p\), for **every**
prime with \(\operatorname{ord}_p(10)=2^a3^b5^c\), \(0\le b\le2\),
with unrestricted \(a,c\). No cyclotomic norm, sieve or class-specific
certificate is needed for this subfamily.

**Proof.** For the full digit layer \(d\), put
\(q=10^d,\ L=10^{d-1},\ N=9L,\ B=q-1\) modulo \(p\), and
\(A=q^{9\cdot10^{d-1}}\). The exact affine map is
\[
 C'=AC+BS-J,\qquad
 Y'=A^{-1}(Y+LS+J),\qquad
 S=\sum_{h=0}^{N_{\rm int}-1}q^h,\quad
 J=\sum_{h=0}^{N_{\rm int}-1}h q^h
\]
where \(N_{\rm int}=9\cdot10^{d-1}\), and the sums are evaluated in
\(\mathbb F_p\). For \(d\ge E:=1+\max(a,c)\),
\(2^a5^c\mid10^{d-1}\), while \(v\mid9\); hence
\(r\mid9d10^{d-1}\), so \(A=1\).
If \(q\ne1\), then \(S=0\), and \(C'+Y'=C+Y\).
If \(q=1\), then \(S=N=9L\), giving
\[
 (C'+Y')-(C+Y)=(B+L)S=9L^2=9/100.
\]
Because \(v\mid9\), \(\operatorname{ord}_v(10)=1\), so the period
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))=r\). Exactly one
\(d\) among \(r+1,\dots,2r\) is divisible by \(r\). Every one of
these layers is stable. Summing their increments proves the identity.
It is nonzero for \(p\ge7\). The two slopes are \(10U+V\) and
\(1000U+V\), which cannot both vanish when \(p\nmid990\).
The already-proved two-offset theorem finishes the construction. QED.

*Scope:* This strengthens the *explanation*, not the set of primes already
covered by the earlier smooth-order theorem. It gives an independent
elementary replacement for the \(b\le2\) part.

## 2. Exact zero-drift algorithm without discrete logarithms

For arbitrary \(r\), let
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\) and
\(E=1+\max(a,c)\), as in the preceding notes.
Suppose \(\Delta=S_{2T}-S_T=(0,0)\).

**Proposition.** It suffices to check (i) the finitely many transient
digit lengths \(d<E\), with their original finite offset ranges, and
(ii) exactly the \(T\) digit lengths \(T+1\le d\le2T\).
In (ii), every zero of the window equation in the appropriate cyclic
subgroup is realized by a valid offset. In particular, no discrete
logarithm is needed to decide existence.

**Proof.** Every stable \(T\)-fold map has diagonal multiplier \(1\),
hence is a translation. The \(T\)-fold map from \(S_T\) to \(S_{2T}\)
is identity when \(\Delta=0\). All stable phase-shifted \(T\)-fold maps
are conjugate to this map through invertible affine layer maps, and
are therefore identity too. Thus \(S_{d+T}=S_d\) for \(d\ge E-1\).
The residues of \(q=10^d\) and \(L=10^{d-1}\) also repeat modulo \(T\).
Every stable digit window has an identical state and phase in the
reference range \(T+1,\dots,2T\); the exceptional windows \(d<E\)
are the only additional cases.

For a reference window let \((C,Y)=S_{d-1}\), \(q=10^d\bmod p\),
\(L=10^{d-1}\bmod p\), and \(k=10^{d-1}+n\).
If \(q\ne1\), write \(z=q^n\), \(h=r/\gcd(r,d)\), and set
\[
 A=qC+\frac{Lq}{q-1}+\frac{q}{(q-1)^2},\qquad
 B=Y-\frac{L}{q-1}+\frac{q}{(q-1)^2},\qquad
 H=-\frac{2q}{(q-1)^2}.
\]
The exact normalized mountain residue is
\[
 A z+Bz^{-1}+H,
\]
so a zero exists precisely when
\[
 Az^2+Hz+B=0,\quad z\ne0,\quad z^h=1\pmod p.
\]
This is just a quadratic (or linear when \(A=0\)), a modular
square-root test, and exponentiation; **no discrete log** is required
for existence. If \(q=1\), the criterion is
\[
 (L+n)^2+C+Y+L-L^2=0\pmod p,
\]
equivalently that \(L^2-L-C-Y\) is a quadratic residue (zero included).
The reference offset width \(9\cdot10^{d-1}>p-1\) because \(d>T\ge r\)
and \(p\mid10^r-1\). Therefore all residues \(n\bmod h\) or
\(n\bmod p\) occur within each reference window. QED.

**Caution:** the proposition is a per-prime *decision* procedure. If a
zero-drift prime had no root in its reference windows and no transient
witness, it would be a genuine counterexample. Neither the existence
nor the impossibility of such a prime has been proved.

## 3. Independent finite stress test (not universal proof)

\`drift_scan_general.cpp\` performs exact modular full-layer arithmetic,
computes \(\Delta\), checks the \(9/100\) invariant whenever \(v\mid9\),
and solves the resulting affine two-offset witness congruence.
Compiled with \`g++ -O3 -std=c++17\`, the command
\`./drift_scan_general 5000\` checked all **665 primes**
\(7\le p<5000,\ p\ne11\):
- **0 zero-drift primes**;
- **665** valid affine two-offset witnesses;
- the \(9/100\) identity passed in all applicable cases;
- sum of the examined periods \(T\) was **135,255,474**, maximum
  \(T=6,044,222\).

An independent Python comparison of the window-polynomial formula with
the direct within-window recurrence passed **5,250** cases on primes
below 250; see \`window_quadratic_audit.py\`.

## 4. Research gap and next move

The finite data support the hypothesis that drift never vanishes, but
no argument above proves this when \(v\nmid9\) and \(2^a5^c\nmid20\).
The target is a structural nonvanishing theorem for the general affine
monodromy translation, or an unconditional root theorem in the
zero-drift branch. In particular, increasing the prime scan limit
alone does not close the conjecture.
