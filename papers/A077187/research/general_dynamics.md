# General digit-layer dynamics and the missing smooth-order bridge

Date: 2026-10-17. This note supplies proofs independently of the unavailable
`stage7` reference. It does **not** prove the all-primes existence conjecture.

## 1. Exact layer recurrence — PROVED

Fix an odd prime `p != 5`, put `r = ord_p(10)`, and do field arithmetic in
`F_p`. Let `C_e` and `R_e` be the ascending and descending concatenations of
`1,...,10^e-1`, respectively. Write

\[
D_e=\sum_{h=1}^e9h10^{h-1}
 =\frac{1+(9e-1)10^e}{9},\quad H_e=10^{D_e},\quad Y_e=R_e/H_e.
\]

Here the quotient by 9 in the formula for `D_e` is an integer quotient,
not an inverse in `F_p`. In layer `e`, set

\[
L=10^{e-1},\quad N=9L,\quad q=10^e,\quad
\alpha=q^N,\quad S_0=\sum_{j=0}^{N-1}q^j,\quad
S_1=\sum_{j=0}^{N-1}jq^j.
\]

The ascending block is `B=(L+N-1)S_0-S_1=(q-1)S_0-S_1`;
the descending block is `A=LS_0+S_1`. Concatenation therefore gives

\[
C_e=\alpha C_{e-1}+B,\qquad Y_e=(Y_{e-1}+A)/\alpha. \tag{1}
\]

If `q != 1`, direct geometric summation yields

\[
\begin{split}
B&=(\alpha-1)-\frac9{10}\alpha\frac q{q-1}
                 +(\alpha-1)\frac q{(q-1)^2},\\
A&=(\alpha-\tfrac1{10})\frac q{q-1}
                 +(1-\alpha)\frac q{(q-1)^2}. \tag{2}
\end{split}
\]

If `q=1`, then `L=1/10`, `N=9/10` in the field, and

\[
A=B=9/200. \tag{3}
\]

No invertibility of `N`, `r`, or 9 was needed. For (3), only 2 and 5
must be invertible.

## 2. A correct period for arbitrary multiplicative order — PROVED

Factor `r=u v` with `u=2^a5^c`, `gcd(v,10)=1`, and define

\[
h=\operatorname{ord}_v(10),\qquad T=\operatorname{lcm}(r,h), \tag{4}
\]

with `h=1` when `v=1`. For every `e >= max(a,c)`,

\[
D_{e+T}\equiv D_e\pmod r. \tag{5}
\]

Indeed,

\[
9(D_{e+T}-D_e)
=10^e\{(9e-1)(10^T-1)+9T10^T\}.
\]

Modulo `u`, the factor `10^e` supplies every required factor of 2 and 5;
9 is invertible modulo `u`. To handle `v`, write `v=3^b w`, with
`gcd(w,30)=1`. We have `w | 10^T-1` because `h | T`, while

\[
v_3(10^T-1)=v_3(10-1)+v_3(T)=2+v_3(T)\ge 2+b.
\]

Thus `9v | 10^T-1`; also `v | T`, so the displayed difference is
divisible by `9v`. This proves (5) by the Chinese remainder theorem.
The elementary valuation equality follows by factoring `x^3-1` repeatedly
and noting that the residual exponent coprime to 3 changes no valuation.

Both `q_e` and `alpha_e=10^(D_e-D_(e-1))` repeat after `T` once
`e-1 >= max(a,c)`. Equations (2)-(3) show that the full affine maps (1)
also repeat. Over `T` consecutive layers their linear multiplier is 1
by (5). Since `T >= max(a,c)`, define

\[
(U,V)=(C_{2T}-C_T,\,Y_{2T}-Y_T).
\]

Identical affine maps are applied in every subsequent block, proving

\[
(C_{jT},Y_{jT})=(C_T,Y_T)+(j-1)(U,V),\qquad j\ge1. \tag{6}
\]

When `r=2^a3^b5^c`, `h=ord_(3^b)(10)` divides `r`, so `T=r`.
This proves the affine identity used in the current manuscript for its
stated smooth-order family without relying on `stage7`.

### An unrestricted period-r assertion is REFUTED

For `p=43`, `r=21`, formula (4) gives `T=42`. Exact recurrence produces

| e | C_e | Y_e |
|---|---:|---:|
|21|30|24|
|42|21|37|
|63|22|29|
|84|42|31|

The successive increments at multiples of 21 are `(34,13)`, `(1,35)`,
and `(20,2)`, modulo 43. They are unequal. This refutes extension of
the manuscript's period-r formula to arbitrary `r`; it does not refute
its smooth-order use. The increment between 42 and 84 is `(21,37)`.

## 3. Nonzero general drift gives a witness — PROVED conditional criterion

Suppose `p` does not divide 990 and `(U,V) != (0,0)` in (6). At `d=jT`,
`10^d=1 mod p`. Normalize a mountain by the power of 10 corresponding
to the digits strictly before its central integer. At the two choices
`k=10^d` and `k=10^d+1`, multiplication by nonzero constants gives
the expressions

\[
10C_d+Y_d+1,\qquad 1000C_d+Y_d+121. \tag{7}
\]

For the second formula, after adjoining `10^d`, the states are
`C'=10 C_d+1` and `Y'=(Y_d+1)/10`; the next center is 2 modulo `p`.
Multiplying `10C'+2+Y'` by 10 proves (7).

The slopes with respect to `j` are `10U+V` and `1000U+V`.
Their difference is `990U`. Since 990 is invertible, both vanish
only if `U=V=0`. At least one expression in (7) is a nonconstant
affine function on `F_p`, and hence vanishes for some `1 <= j <= p`.
In particular,

\[
k\le 10^{pT}+1. \tag{8}
\]

This is a theorem for **every order factorization satisfying its explicit
nonzero-drift hypothesis**. It is not a proof that this hypothesis holds
for all primes. The omitted primes have direct witnesses
`M(3)=12321` for `p=3`, and `M(2)=121` for `p=11`.

## 4. Smooth-order quadratic formulas derived from (1) — PROVED

Let

\[
r=3^b s,\quad s=2^a5^c,\quad b\ge2,\quad
t=3^{b-2},\quad m=9s,\quad r=mt,
\quad\zeta=10^m,\quad\gamma=s^{-1}\pmod t.
\]

For `t=1`, all sums indexed from 1 to `t-1` below are empty and no
choice of `gamma` is needed. Use the block of layers `r+1,...,2r`.
The start is beyond the 2/5 transient. The length of layer `e` satisfies

\[
N_e=9\cdot10^{e-1}\equiv m\gamma 10^{e-1}\pmod r,
\quad
\alpha_e=\zeta^{\gamma e10^{e-1}}. \tag{9}
\]

To justify the first congruence, divide the integer `N_e` by `m=9s`
and reduce the quotient `10^(e-1)/s` modulo `t`. It equals
`gamma 10^(e-1)` because `s` is invertible modulo `t`.

Put

\[
E_j=\sum_{h=1}^{j}h10^{h-1}\pmod t,\quad
\alpha_j=\zeta^{\gamma j10^{j-1}},\quad
\beta_j=\zeta^{\gamma E_j}.
\]

The congruences `10^t=1 mod t` and `E_t=0 mod t` imply that `alpha`
and `beta` have period `t`. For completeness, the second congruence
follows by induction through `t=1,3,9,...`: since `10^t=1 mod 3t`,

\[
E_{3t}=\sum_{k=0}^{2}10^{kt}
 \left(E_t+kt\sum_{h=1}^t10^{h-1}\right)
 \equiv3E_t+3t\sum_{h=1}^t10^{h-1}\equiv0\pmod{3t}.
\]

The first congruence follows from the same elementary 3-adic valuation
identity used in Section 2. As `r` is divisible by `t`, the cumulative
multiplier after `j` layers of this block is exactly `beta_j`.
Unrolling (1) therefore yields

\[
U=\sum_{e=r+1}^{2r}\beta_e^{-1}B_e,\qquad
V=\sum_{e=r+1}^{2r}\beta_{e-1}A_e. \tag{10}
\]

Here the subscripts on `beta` are read modulo `t`.

Group the `r=mt` layers by `j=e mod t`. For fixed `1 <= j < t`,
their values of `q=10^e` run through all `m` distinct roots of
`q^m=zeta^j`. They are distinct because `m | p-1`. Write

\[
X_j=\frac{\zeta^j}{\zeta^j-1},\qquad
Z_j=\frac{\zeta^j}{(\zeta^j-1)^2}.
\]

Logarithmic differentiation of `X^m-zeta^j`, or direct partial
fractions, gives

\[
\sum_{q^m=\zeta^j}\frac q{q-1}=mX_j,\qquad
\sum_{q^m=\zeta^j}\frac q{(q-1)^2}=m^2Z_j. \tag{11}
\]

No root in these sums equals 1. One explicit derivation of the second
identity is to differentiate
`sum 1/(x-q)=m*x^(m-1)/(x^m-zeta^j)` at `x=1`, then use
`q/(q-1)^2=1/(q-1)+1/(q-1)^2`.

For the remaining group `j=t`, `alpha=beta=1` and `q` runs over all
`m`th roots of unity. Exclude `q=1` and pair each root with its inverse.
The identity `q/(q-1)+q^(-1)/(q^(-1)-1)=1` gives

\[
\sum_{q^m=1,\ q\ne1}\frac q{q-1}=(m-1)/2.
\]

It remains valid for the possible fixed root `q=-1`, whose summand is
`1/2`. Combining with (3), the group's contributions are

\[
U_{\rm res}=99/200-9m/20,\qquad
V_{\rm res}=-81/200+9m/20. \tag{12}
\]

Substitute (2), (11), and (12) in (10). This proves precisely

\[
\begin{split}
U={}&\frac{99}{200}-\frac9{20}m+
\sum_{j=1}^{t-1}\zeta^{-\gamma E_j}
\left\{m\left[(\alpha_j-1)-\frac9{10}\alpha_jX_j\right]
       +m^2(\alpha_j-1)Z_j\right\},\\
V={}&-\frac{81}{200}+\frac9{20}m+
\sum_{j=1}^{t-1}\zeta^{\gamma E_{j-1}}
\left\{m(\alpha_j-\tfrac1{10})X_j
       +m^2(1-\alpha_j)Z_j\right\}. \tag{13}
\end{split}
\]

These are the scalar coefficients used in `scalar_reference.py`, now
with an independent proof and an explicit derivation of their constant
terms. In particular this bridges the actual drift to the manuscript's
`b=8`, `t=729`, `m=9s` formulas.

For the integral group-ring form, put `w=zeta^j` of order `n=t/gcd(j,t)`.
Differentiate the polynomial identity
`1+x+...+x^(n-1)=(x^n-1)/(x-1)` before setting `x=w`. This gives

\[
h_j=\frac tn\sum_{l=0}^{n-1}l w^{l+1}
     =t\frac w{w-1}=tX_j,\qquad
j_j=w^{-1}h_j^2=t^2Z_j. \tag{14}
\]

Multiplying (13) by `D=200t^2` gives all four coefficient formulas
printed in `main.tex`, including the constants `U_0=99t^2` and
`V_0=-81t^2`. Every denominator is invertible for an admissible prime:
`p != 2,5`, and `t | p-1` entails `p` does not divide `t`.

## 5. A small smooth-order theorem requiring no norms — PROVED

For `r=2^a3^b5^c` with `b <= 2`, every layer after the 2/5 transient
has `alpha=1`: the exponent `9e10^(e-1)` is divisible by `r`.
At each layer with `q != 1`, formula (2) gives `A+B=0`.
There is exactly one layer with `q=1` in a block of length `r`, and
(3) gives its sum increment `9/100`. Consequently

\[
U+V=9/100\ne0\pmod p
\]

for `p != 3`. Section 3 supplies a witness for `p != 3,11`, and the
two explicit witnesses there handle those primes. This proves the
entire `b <= 2` subfamily without older-stage certificates. At `b=2`,
the same conclusion is also immediate from (13) with `t=1`.

## 6. The exact freedom inside a digit window — PROVED

At the start of digit length `d`, let `L=10^(d-1)`, `q=10^d`,
`C=C_(d-1)`, and `Y=Y_(d-1)`. A center `k=L+n` has `0 <= n < 9L`.
Before its center, the normalized mountain residue is

\[
F(n)=q C_n+(L+n)+Y_n,
\]

where `C_n,Y_n` are the states after adjoining the first `n` numbers
of this layer. If `q != 1`, geometric summation and cancellation of
the linear terms in `n` give

\[
F(n)=a q^n+b q^{-n}-\frac{2q}{(q-1)^2}, \tag{15}
\]

with

\[
a=q\left(C+\frac L{q-1}+\frac1{(q-1)^2}\right),\qquad
b=Y-\frac L{q-1}+\frac q{(q-1)^2}.
\]

Thus a sufficiently long window contains a solution exactly when

\[
a z^2-\frac{2q}{(q-1)^2}z+b=0
\quad\hbox{has a root }z\in\langle q\rangle. \tag{16}
\]

The interval is sufficiently long as soon as `9L >= ord_p(q)`.
Equation (16) remains valid when `a=0` or `b=0`; one must still
exclude the root `z=0`, since it does not belong to the subgroup.

If `q=1`, the same calculation using arithmetic progressions yields

\[
F(n)=(L+n)^2+C+Y+L-L^2. \tag{17}
\]

Here a sufficiently long window (`9L >= p`) has a solution exactly
when `-(C+Y+L-L^2)` is a square, allowing zero, in `F_p`.

Equations (15)-(17) expose an obstruction to the proposed additional
low/high-digit parameters: for `q != 1`, the residue `n mod p`
**cancels completely**. Within one window the apparent two parameters
`n mod p` and `q^n` reduce to just `q^n`. The special `q=1` windows
provide a quadratic parameter, not an arbitrary linear parameter.

## 7. What remains open

**CONDITIONAL:** for a general prime with zero drift for period (4),
one would need to prove that at least one periodic window satisfies
(16) or (17). The proofs above do not establish that. They also do not
prove that the general drift is always nonzero.

**EXPERIMENTAL identity checks:** `general_dynamics_check.py` implements
geometric moments by binary composition and imports none of the existing
coefficient code. It checks the affine identity for all 51 primes from
3 through 250 other than 5, checks the window identities against direct
single-integer state updates through center 300, and checks (13) for
eight representative smooth-order primes through `b=8`. Its `p=43`
table is an exact finite counterexample to the unrestricted period-r
claim. The finite checks supplement the proofs; they cannot establish
all-primes existence.

## 8. A larger constructive theorem from the transient defect — PROVED

This section records a completed derivation obtained after Sections 1-7.
It supersedes the nonzero-drift requirement for this particular family.
Write `r=u v` as in Section 2. Suppose

\[
u\mid20,\quad\text{equivalently}\quad v_2(r)\le2,
\quad v_5(r)\le1. \tag{18}
\]

There is no restriction on any other prime factor of `r`, including the
exponent of 3. For `p != 3`, choose `delta mod r` by the Chinese remainder
conditions

\[
9\delta\equiv1\pmod u,\qquad\delta\equiv0\pmod v,
\quad h=10^\delta\in\mathbb F_p^* . \tag{19}
\]

When `u=1` the first condition is vacuous. Define a periodic extension
of the powers `H_e` by choosing the exponent `bar D_e mod r` from

\[
\overline D_e\equiv9^{-1}\pmod u,\qquad
\overline D_e\equiv D_e\pmod v,
\quad\overline H_e=10^{\overline D_e}. \tag{20}
\]

The argument of Section 2 proves that `bar H_e` has period `T` from
`e=0` onward, and `bar H_0=h`. Set
`bar alpha_e=bar H_e/bar H_(e-1)` and define the stable layer maps by
(2)-(3), replacing `alpha` by `bar alpha`.
For a `q=1` phase, `e` is divisible by `r`, so
`D_e-D_(e-1)=9e10^(e-1)` is divisible by `r`. The two continued
exponents therefore agree modulo `v`; they also agree modulo `u`
by definition (20). Thus `bar alpha=1` there, consistently with (3).
It is not necessary to assert that the individual continued powers
equal `h` at every such phase.

The actual and stable `H_e` agree for every `e>=1`. In fact their
difference modulo `u`, after multiplication by the invertible 9, is
`(9e-1)10^e`. This is divisible by 5 for every `e>=1`. It is divisible
by 4 because at `e=1` it equals 80, while for `e>=2` the factor `10^e`
already contains 4. Condition (18) suffices. Modulo `v` agreement is
part of definition (20).

Consequently the actual and stable maps differ only in layer 1.
At this layer `q=10`, and (2) simplifies to

\[
B(\alpha)=\frac{10}{81}\alpha-\frac{91}{81},\qquad
A(\alpha)=\frac{80}{81}\alpha+\frac1{81}.
\]

The actual multiplier is `h` times the stable multiplier. Solving
`stable_map(D)=actual_map(0)` gives the explicit state

\[
\mathcal D=
\left(\frac{10(h-1)}{81},\frac{h^{-1}-1}{81}\right). \tag{21}
\]

Each complete stable period is a translation, since its multiplier is
`bar H_T/bar H_0=1`. Write its translation vector as `b`. At each
positive period boundary the actual state is therefore

\[
(C_{jT},Y_{jT})=\mathcal D+j b. \tag{22}
\]

Taking `j=p` gives state `mathcal D`, whatever `b` is; this argument
does not need to classify zero and nonzero drift.
In the following digit window, let `k=10^(pT)+n`, and put `z=10^n`.
Substitute (21) into (15), with `q=10` and `L=1 mod p`:

\[
F(n)=\frac{100h z+h^{-1}z^{-1}-20}{81}
     =\frac{(10hz-1)^2}{81hz}. \tag{23}
\]

Because `h` belongs to `<10>`, choose `0<=n<r` with

\[
n\equiv-\delta-1\pmod r.
\]

Then `z=(10h)^(-1)` and (23) vanishes. The chosen `n` lies in the
digit window, and hence

\[
\boxed{k=10^{pT}+n,\quad 0\le n<r,\quad p\mid M(k)}. \tag{24}
\]

For `p=3`, use `M(3)=12321`. This completes an all-primes theorem
subject to (18), including orders with arbitrary factors outside
`{2,3,5}` and unbounded 3-adic valuation. The arithmetic derivation is
complete. The independent certificate-audit agent checked this mechanism
and recorded its completed verification in `audit_certificates.md`.
Manuscript integration was still pending when the user requested a stop.

## 9. Saved boundary of the unfinished transient argument

**CONDITIONAL / unresolved:** (18) does not cover `v_2(r)>=3` or
`v_5(r)>=2`. For `u=8`, agreement of actual and stable `H_e` fails at
the intermediate boundary `e=2`, since `(9e-1)10^e=1700` has 2-adic
valuation 2. It holds at `e=1` (value 80) and at every `e>=3`.
For `u=25`, an extra mismatch already occurs at `e=1`, since 80 has
5-adic valuation 1; it disappears for `e>=2`. These extra boundary
defects produce compositions involving two different digit-layer
parameters `q`, so the single-window square (23) has not been proved.

**EXPERIMENTAL diagnostic, not a theorem:** a direct exact-field
calculation of the defect for `p=73`, `r=u=8` gave `(71,29)`.
For this state the `q=10`, `L=1` expression (15) has no zero among
`z in <10>`. For `p=137`, `r=u=8`, the computed defect was `(2,34)`,
again with no root in that first window. These observations warn
against extending (23) unchanged; they do not disprove existence in
another window or after another number of periods. They were produced
by a separate exploratory calculation, not included in the checked
test suite, and have not received independent audit.

Research was stopped at the user's explicit request. No further
experimentation or claimed extension beyond (18) was undertaken.
