# Tail phases, window gauges, and a limitation of the first three windows

Date: 2026-10-18. The all-primes A077187 problem remains **OPEN**.
This note continues `zero_drift.md`. The tail reduction is **PROVED**
algebraically. The squareclass calculation below is a finite exact
**COMPUTATION_CERTIFIED** step. No new prime-search bound is used.

## 1. The state after p stable blocks

Let `p>=7`, `r=ord_p(10)=uv`, `u=2^a5^c`, `(v,10)=1`, and
`T=lcm(r,ord_v(10))`. Use `ord_1(10)=1`.
Write `F_i` for the actual i-digit layer map and `Fhat_i=F_(T+i)`
for its stable continuation. Choose `h=max(1,a,c)`, so `h<r` and
`F_i=Fhat_i` for `i>h`. All maps are invertible affine maps.
Composition is read right to left.

The stable block map is `G(x)=x+B`, with drift vector `B`.
Define the finite defect state

\[
W=\widehat F_1^{-1}\circ\cdots\circ\widehat F_h^{-1}
  \circ F_h\circ\cdots\circ F_1(0).
\tag{1}
\]

The actual first block ends at `G(W)=W+B`; subsequent blocks are
stable. Hence the state after `j` blocks is `W+jB`, and after `p`
blocks it is exactly `W`. This statement does **not** assume zero
drift. In the zero-drift case it holds after every block.

## 2. Removing the current multiplier preserves subgroup membership

Fix `1<=d<=h`, and put `q=10^d`, `L=10^(d-1)`. Since `d<r`,
`q!=1 mod p`. Define the following rational constants:

\[
\begin{aligned}
c_d&=L/(q-1)+1/(q-1)^2,& b_d&=-L/(q-1)+q/(q-1)^2,\\
\delta_d&=-q/(q-1)-1/(q-1)^2,& f_d&=q/(q-1)-q/(q-1)^2.
\end{aligned}
\]

With `alpha_d=10^(9d10^(d-1))`, the layer map is

\[
F_d(C,Y)=\bigl(\alpha_d(C+c_d)+\delta_d,
                    \alpha_d^{-1}(Y+b_d)+f_d\bigr).
\tag{2}
\]

Its stable continuation replaces `alpha_d` by `alphahat_d`.
Let

\[
X_d=\widehat F_{d+1}^{-1}\circ\cdots\circ\widehat F_h^{-1}
             \circ F_h\circ\cdots\circ F_1(0).
\]

Starting from `W`, the state before the d-th window is
`Fhat_d^(-1)(X_d)`; all earlier stable maps cancel in (1).
Consequently its centered coefficients are

\[
A=(X_{d,C}-\delta_d)/\widehat\alpha_d,\qquad
B=(X_{d,Y}-f_d)\widehat\alpha_d.
\]

The exact zero equation is `q A z^2-2q z/(q-1)^2+B=0`,
with `z` in `<q>`. Since `alphahat_d` is itself a power of `q`,
substitution `w=z/alphahat_d` is a bijection of that subgroup.
It gives the equivalent equation

\[
\boxed{q(X_{d,C}-\delta_d)w^2
 -\frac{2q}{(q-1)^2}w+(X_{d,Y}-f_d)=0,\qquad w\in\langle q\rangle.}
\tag{3}
\]

Thus the current and all preceding *stable multipliers* disappear.
The actual finite prefix remains, so this is not a proof that every
state is reachable. The windows after `pT` are long enough to traverse
the full subgroup. Quadratic degeneracies are retained in (3).

## 3. The exact tail phase order

Put `e_i=9i10^(i-1)`, `lambda=10^T mod r`,
`zeta=10^v` of order `u`, and `gamma=v^(-1) mod u`.
The Chinese remainder identities `lambda=0 mod u`, `lambda=1 mod v`
give

\[
\rho_i=\widehat\alpha_i/\alpha_i
 =10^{e_i(\lambda-1)}=\zeta^{-\gamma e_i}.
\tag{4}
\]

For any `d>=1`, the smallest smooth valuations in the tail are

\[
\min_{i>d}v_2(e_i)=d+[d\text{ odd}],\qquad
\min_{i>d}v_5(e_i)=d+[5\mid d+1].
\]

Indeed the first index attains the minimum unless it is divisible
by the relevant prime; then the next index attains the indicated
minimum. Every later index has at least that valuation. Set

\[
G_d=2^{d+[d\text{ odd}]}5^{d+[5\mid d+1]},\qquad
\theta=\zeta^{-\gamma G_d},\qquad
w_d=u/\gcd(u,G_d).
\]

Then `theta` has exact order `w_d`, and every remaining ratio is
`rho_i=theta^(e_i/G_d)` for `i>d`. Formula (3) therefore has a model
over `Q(theta)` involving only the actual rational prefix maps and
this tail phase. Appending layers for which `rho_i=1` cancels their
actual and stable maps. No dependence on `v` remains except the
choice of primitive root `theta` at reduction modulo `p`.

In particular, `G_1=20`: the first-window phase field shrinks from
`Q(zeta_u)` to `Q(zeta_(u/gcd(u,20)))`. For `u|20`, the tail is empty,
`X_1=F_1(0)`, and (3) is the square already proved in `zero_drift.md`.
This both recovers that theorem and identifies its exact first-window
phase reduction. It does not force a root for larger `u`.

## 4. A rational model when u=8

Here `rho_2=rho_3=-1` and all later ratios are 1; `rho_1` is removed
by the gauge. Thus all three window models have rational coefficients.
For the first window, a further subgroup-preserving rescaling
`t=alpha_1*w=z/rho_1` gives

\[
10A t^2-\frac{20}{81}t+B=0,\qquad t\in\langle10\rangle,
\]
\[
A=\frac{10}{81}-\frac{219804400}{120758121\,10^{189}},\qquad
B=\frac1{81}+\frac{217557800\,10^{189}}{120758121}.
\tag{5}
\]

For a compact exact specification of all three models, start with
`X_3=F_3 F_2 F_1(0)` using rational maps (2). Recursively set
`X_(d-1)=Fhat_d^(-1)(X_d)` for `d=3,2`, using `rho_d=-1`.
Their discriminants are the fixed nonzero rational numbers

\[
\Delta_d=\frac{4q_d^2}{(q_d-1)^4}
 -4q_d(X_{d,C}-\delta_d)(X_{d,Y}-f_d).
\tag{6}
\]

`zero_drift_tail_gauge_2026_10_18.py` constructs these exact fractions.
The definitions (2), (6), and the initial state specify them without
factoring large integers or listing hundreds of digits.

**REFUTED:** the first three windows after `pT` always suffice.
For `p=617`, `r=88`, all three Legendre symbols `chi(Delta_d)` are
`-1`. None of these windows has a root even in the full field.
For `p=73,137,2393`, the first discriminant is a square, but neither
root belongs to `<10>`. These are exact failures of the specified
window construction, **not counterexamples to A077187**. In particular,
617 has nonzero drift and is covered by the established `v=11` theorem.

## 5. A positive-density obstruction to those three windows

The script checks, by integer square roots of reduced fractions, that
for every nonempty `S subset {1,2,3}` and every
`c in {1,-1,2,-2,5,-5,10,-10}`,

\[
\prod_{d\in S}\Delta_d/c\notin\mathbb Q^{\times2}.
\tag{7}
\]

All 56 exact tests pass. Together with independence of `-1,2,5`,
this certifies that the six displayed squareclasses have rank six.
Thus

\[
L=\mathbb Q(i,\sqrt2,\sqrt5,\sqrt{\Delta_1},
                         \sqrt{\Delta_2},\sqrt{\Delta_3})
\]

is multiquadratic of degree 64. Let `K=Q(zeta_16)`. Its largest
multiquadratic subfield is `Q(zeta_8)=Q(i,sqrt2)`: the Galois group
is `C4 x C2`, and its maximal exponent-two quotient has order four.
It follows that `L intersect K=Q(zeta_8)` and `[LK:Q]=128`.

Choose the automorphism of `L` fixing `i,sqrt2` and negating
`sqrt5` and all three `sqrt(Delta_d)`. Independence (7) makes this
choice possible. It agrees on the intersection with the automorphism
`zeta_16 -> zeta_16^9` of `K`, so they extend uniquely to `LK`.
This extension is abelian. The Chebotarev density theorem therefore
gives a set of rational primes of natural density `1/128` having
this Frobenius, after the finitely many ramified primes are excluded.
The theorem used is [Milne, Algebraic Number Theory, Theorem 8.31](https://www.jmilne.org/math/CourseNotes/ANT.pdf).

For these primes, `p=9 mod16`, `chi(5)=-1`, and all
`chi(Delta_d)=-1`. Thus `v2(p-1)=3`, while `p=2 or 3 mod5`
implies `5` does not divide `p-1`. Also `chi(2)=1`, so
`chi(10)=-1`; a nonsquare in a cyclic group has the full 2-part of
the group order. Therefore the smooth part of `ord_p(10)` is exactly
`u=8`, and all three windows in (3) fail.

**Conclusion of this argument:** a set of primes of density `1/128`
defeats the proposed three-window construction after `p` blocks.
This does not rule out other windows or nonzero-drift witnesses, nor
does it disprove an assertion conditional on *actual zero drift*.
The latter would require a relation between that condition and (6),
which has not been established.

## 6. Verification and the remaining gap

Run `python zero_drift_tail_gauge_2026_10_18.py --examples --symbolic`.
Seven specified primes compare the rational model against independent
modular full-layer inversion in all three windows. These are consistency
checks, not a prime scan used to infer a universal theorem. The script
asserts the `p=617` obstruction and all squareclass tests (7).

The remaining task is to prove either general nonzero drift or a
subgroup root in an actual zero-drift orbit. Tail phase reduction and
the sharp three-window obstruction narrow this task but do not solve it.
No larger fixed-window or prime cutoff is asserted as a substitute.
