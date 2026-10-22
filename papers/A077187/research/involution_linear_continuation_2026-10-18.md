# Involutive linear drift: two factors of 3 disappear, and all v dividing 99

Date: 2026-10-18. This note continues the exact involution theorem in
`involutive_spectral_degree_drop_2026-10-18.md`.

The main outcome is an existence theorem for every prime whose order
has coprime-to-10 part dividing 99. The odd smooth-part branch has a
new explicit nonzero invariant. The even branch uses the same ten
fixed norm integers already certified for `v=11`; no new cyclotomic
fields or norms are needed for `v=33,99`.

The unrestricted A077187 conjecture remains open. Status labels below
distinguish algebraic proofs from exhaustive exact computation.

## 1. Removing two factors of 3 from the phase space — PROVED

Let `p != 2,5` be prime and write

\[
r=\operatorname{ord}_p(10)=u v,\qquad
u=2^a5^c,\qquad (v,10)=1.
\]

Define

\[
d=\gcd(v,9),\quad t=v/d,\quad b_0=9/d,\quad
\ell=\operatorname{lcm}(t,\operatorname{ord}_t(10)),
\quad g=\gcd(r,\ell),\quad m=r/g,\quad T=m\ell.
\tag{1}
\]

Use `ord_1(10)=1`. In a stable digit layer `e`, the multiplier is

\[
A_e=10^{9e10^{e-1}}.
\]

Once `u | 10^(e-1)`, the exponent is divisible by `u*d`; hence
`A_e` belongs to the subgroup of order `t`, rather than merely the
subgroup of order `v`. With

\[
\zeta=10^m\quad(\text{order }g),\qquad
\eta=u^{-1}\pmod t,
\]

its phase is

\[
\boxed{A_e=\zeta^{(g/t)b_0\eta\,e10^{e-1}}.} \tag{2}
\]

To verify (2), write `10^(e-1)=u q` as an integer. Dividing the
original exponent by `u*d` gives `b_0*e*q`, and `q=eta*10^(e-1)
mod t`. Also `zeta^(g/t)=10^(r/t)=10^(u*d)` has exact order `t`.
All divisions modulo `t` are legitimate because `u` is coprime to `t`.

The order `t` is exact for the phase subgroup. Indeed `b_0=9/d` is
coprime to `t` by the definition of `d`, and so is `eta`. At the
stable phase `e=T+1`, formula (2) gives the primitive `t`th root
`(10^(u*d))^(b_0*eta)`. Thus the stable multipliers generate exactly
`mu_t`. In particular the factor 9 alone permits no further universal
reduction of the phase subgroup beyond (1).

Both `A_e` and its cumulative phase have period `ell`. The first
assertion follows from `t | ell` and `10^ell=1 mod t`. For the second,
it suffices to show

\[
E_\ell:=\sum_{j=1}^{\ell}j10^{j-1}\equiv0\pmod t. \tag{3}
\]

For the part of `t` coprime to 3, use

\[
81E_\ell=1+(9\ell-1)10^\ell
\]

and invert 81. For the 3-power part, first prove `3^n | E_(3^n)`
by induction. If `s=3^n`, then `10^s=1 mod 3s`, so

\[
E_{3s}=\sum_{k=0}^{2}10^{ks}
 \left(E_s+ks\sum_{j=1}^s10^{j-1}\right)
\equiv3E_s\equiv0\pmod{3s}.
\]

The starting case `s=1` is immediate. Partitioning any multiple of
`3^n` into blocks of that length proves its weighted sum is also
zero modulo `3^n`. This establishes (3) for `ell` and then for any
shifted block of `ell` layers.

The existing coset compression consequently holds with this smaller
`ell` and `g`. The `m` values of `q=10^e` in one phase class are the
roots of `q^m=zeta^j`. A block of length `T=m*ell` has multiplier 1
and is a translation in `(C,Y)`.

This lemma simultaneously explains the older smooth-order choice
`t=3^(b-2)` and why `v=11,33,99` should use the same phase space.
For an arbitrary `v`, it remains a compression lemma and does not
by itself establish nonzero drift.

## 2. The three involutive families share the same 22 phases — PROVED

Specialize to

\[
r=11w,\qquad w=3^b2^a5^c,\qquad b\in\{0,1,2\}.
\tag{4}
\]

In (1), `d=3^b`, `t=11`, `ell=22`, and

\[
g=\begin{cases}11,&a=0,\\22,&a\ge1,\end{cases}
\qquad m=r/g,\qquad
\gamma=w^{-1}\pmod{11}.
\]

Equation (2) is exactly

\[
A_j=\omega^{9\gamma j(-1)^{j-1}},\qquad
\omega=\zeta^{g/11},\qquad \zeta=10^m. \tag{5}
\]

Indeed `b_0*u^(-1)=(9/d)*u^(-1)=9*w^(-1) mod 11`.
The phase gamma must therefore include the factor `3^b`; using only
`(2^a5^c)^(-1)` would be incorrect for the newly covered families.

Set `P_j=product_(i<j) A_i` and `tau=omega^(9gamma)`. Then

\[
\boxed{P_{2n}=\tau^n,\qquad P_{2n+1}=\tau^{-n}.} \tag{6}
\]

Use `1<=n<=11` for even indices and `0<=n<=10` for odd ones.
The sum of all 22 phases is zero, since each parity class traverses
all eleventh roots of unity.

## 3. Explicit Fourier evaluation of the remaining linear terms — PROVED

The involution theorem already proves `U_2=V_2=0`. Define

\[
X(c)=\begin{cases}c/(c-1),&c\ne1,\\1/2,&c=1,\end{cases}
\qquad S_\pm=\sum_{j=1}^{22}P_j^{\pm1}X(\zeta^j).
\]

The telescoping sum of `alpha_j=P_j^(-1)-P_(j+1)^(-1)` is zero.
The ascending linear coefficient is therefore

\[
U_1=-\frac9{10}S_- . \tag{7}
\]

For the descending coefficient, the spectral formula gives
`V_1=sum_j(P_(j+1)-P_j/10)X(zeta^j)`. The phase palindrome gives
`P_(j+1)=P_(22-j)`, while `X(c^(-1))=1-X(c)`, including `c=1`.
As `sum_j P_j=0`, this yields

\[
V_1=-\frac{11}{10}S_+ . \tag{8}
\]

The necessary Fourier sums are elementary. For `1<=A<=10`,

\[
\sum_{c^{11}=1}c^A X(c)=\frac{11}{2}-A. \tag{9}
\]

For `A=0` the sum is `11/2`, by pairing inverses and including the
half contribution at 1. Increasing `A` by one changes the sum by
`sum_(c^11=1,c!=1)c^A=-1`, proving (9).
For the negative coset, with no singular root,

\[
\sum_{c^{11}=-1}c^A X(c)=\frac{11}{2}
\quad(0\le A\le10),\qquad
\sum_{c^{11}=-1}c^{-A}X(c)=-\frac{11}{2}
\quad(1\le A\le10). \tag{10}
\]

The initial value follows from logarithmic differentiation of
`x^11+1`, and successive differences vanish. Negative exponents
follow from `c^11=-1`.

### 3.1. Odd smooth part: an explicit nonzero invariant

For `g=11`, choose the integer `A in {1,...,10}` with

\[
2A\equiv9\gamma\pmod{11},\quad z=\zeta^A,\quad D=11-2A.
\]

In (6), even indices give `P=c^A`, and odd indices give
`P=z*c^(-A)`. Equations (9) and (7)-(8) therefore yield

\[
\boxed{\begin{aligned}
U&=\frac{99}{200}(1+z^{-1})
       +\frac{9D}{20}m(1-z^{-1}),\\
V&=-\frac{81}{200}(1+z)
       -\frac{11D}{20}m(1-z).
\end{aligned}} \tag{11}
\]

The constant terms come from the two singular phase classes,
`j=11,22`, whose phases are `z,1`, respectively.
Eliminating the linear parameter in (11) gives the central identity

\[
\boxed{11zU-9V=\frac{909}{100}(z+1).} \tag{12}
\]

Here `z` has exact order 11, so `z+1!=0`. The only odd prime
divisors of `909=9*101` are 3 and 101; neither is admissible in (4),
because their orders of 10 are 1 and 4 respectively.
Thus the right side is nonzero for every prime in this branch,
and `(U,V)!=(0,0)` follows with **no norm computation or sieve**.

For reference, the old large odd-branch norms conceal the simple
closed form

\[
\left|\operatorname{Norm}\left(4000
  (U_1V_0-U_0V_1)\right)\right|
 =11\,(1818D)^{10}.
\]

This norm formula is explanatory only; the proof of nonzero drift
uses (12), not a prime factorization of its norm.

### 3.2. Even smooth part: a quadratic obstruction

For `g=22`, choose `A in {1,...,10}` with

\[
A\equiv9\gamma\pmod{11},\quad z=\zeta^A,\quad D=11-2A.
\]

The even indices traverse `c^11=1` and the odd indices traverse
`c^11=-1`. Equations (9)-(10) give

\[
S_+=D/2-11z/2,\qquad S_-=-D/2+11/(2z).
\]

There is one singular phase, with `P=1`. Consequently

\[
\boxed{\begin{aligned}
U&=\frac{99}{200}+\frac{9m}{20}(D-11z^{-1}),\\
V&=-\frac{81}{200}-\frac{11m}{20}(D-11z).
\end{aligned}} \tag{13}
\]

The linear resultant is particularly small:

\[
4000z\,(U_1V_0-U_0V_1)
=9(891+40Dz-1331z^2). \tag{14}
\]

Thus simultaneous zero drift forces

\[
\boxed{1331z^2-40Dz-891=0.} \tag{15}
\]

The derivation of (13)-(15) is algebraic and exact. It does **not**
by itself show that the obstruction has no admissible roots.
The next section supplies a finite exact exclusion.

## 4. Complete even-branch exclusion — COMPUTATION_CERTIFIED

The ten values of `gamma` and the coordinate polynomials in (13)
are exactly those already certified for `v=11`, `g=22`.
Let `N_gamma` be their existing nonzero norm integers from
`certify_fixed_v11.py`. They can be regenerated without the spectral
compressor: if `A` is odd, `z` is primitive of order 22; if `A` is
even, it is primitive of order 11. In either case

\[
N_\gamma=
\left|\operatorname{Res}_x\left(
9(891+40Dx-1331x^2),\ \Phi_{\operatorname{ord}(z)}(x)
\right)\right|. \tag{16}
\]

Multiplication by `z` in (14) does not change the absolute norm.
The new script `certify_involutive_families.py` independently
recomputes all ten values from (16) and compares them to the old
integers. It also checks all twenty formulas (11) and (13) coefficient
by coefficient against the existing spectral compressor.

Suppose a true-order prime caused simultaneous zero drift. Reduction
of (14) shows `p | N_gamma`; the denominators in (13) divide 200 and
are invertible for every admissible prime. Moreover

\[
r=11\cdot3^b2^a5^c\mid p-1,\qquad
r<p\le N_\gamma,\qquad p\mid\Phi_r(10),\quad a\ge1.
\tag{17}
\]

For each `b=0,1,2` the script exhausts **all** pairs `a>=1,c>=0`
with `r<=N_gamma`, where the actual phase is

\[
\gamma=(3^b2^a5^c)^{-1}\pmod{11}.
\]

There is no arbitrary multiplicative-order cutoff: (17) supplies
the required finite upper bound. Modular cyclotomic evaluation uses
the exact identity

\[
\Phi_{11\,3^b2^a5^c}(X)
=\Phi_{22\,3^{[b>0]}5^{[c>0]}}
 \left(X^{2^{a-1}3^{\max(b-1,0)}5^{\max(c-1,0)}}\right).
\tag{18}
\]

The base polynomial has degree at most 80. All powers are evaluated
modulo the relevant `N_gamma`, so neither factorization of the large
norms nor construction of enormous repunits is involved.

Exact execution returned:

| b | Complete phase-aware indices | gcd(N_gamma, Phi_r(10)) |
|---|---:|---|
| 0 | 3887 | 1 in every case |
| 1 | 3796 | 1 in every case |
| 2 | 3702 | 1 in every case |
| Total | 11385 | no candidate factors |

The program asserts both every raw gcd and the three final counts.
This contradicts (17) for every possible simultaneous-zero case,
completing the even branch by a finite exact certificate.

## 5. Combined theorem, witnesses, and limitations

**PROVED / COMPUTATION_CERTIFIED, by branch:** for every prime `p!=2,5`
whose order can be written `r=2^a5^c*v` with `v | 99`, there exists
`k>=1` such that `p | M(k)`.

For `v | 9`, the elementary identity `U+V=9/100` over an `r`-layer
period proves the claim, apart from the directly handled `p=3`.
For `11 | v`, Section 3.1 proves the odd branch algebraically, and
Section 4 certifies the even branch. The stable-period two-offset
theorem then produces a witness among

\[
k=10^{jT}\quad\text{or}\quad10^{jT}+1,
\qquad 1\le j\le p.
\]

In the `11 | v` families take `T=22m`. In all cases the elementary
exceptions `p=3,11` have witnesses `M(3)=12321` and `M(2)=121`.
The manuscript should not describe the combined theorem as entirely
certificate-free: only its specified algebraic branches are.

The completed independent audit checked the explicit formulas, odd
invariant, stripping argument, all ten norms, the exhaustive sieve,
and its phase conditions. It also compared 27 modular cyclotomic
evaluations with full polynomial evaluations. See
`audit_spectral_update_2026-10-18.md`. The integrated manuscript is
`fixed_v_spectral_families.tex`.

**Remaining gap:** for general coprime part `v`, neither a nonzero
drift theorem nor a universal zero-drift witness theorem has been
proved. The stripping lemma reduces the phase space but does not
eliminate this gap. No further fixed-v enumeration is part of this
continuation.

## Reproduction

Run from the research directory with Python 3 and SymPy:

```text
python certify_involutive_families.py
```

The imports are local `certify_fixed_v7.py` (coefficient comparison)
and `certify_fixed_v11.py` (the ten existing norm integers).
