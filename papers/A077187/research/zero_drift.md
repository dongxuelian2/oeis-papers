# Zero drift and the first transient digit layer

Research status: **PROVED** results below are algebraic; finite checks are listed
separately as **EXPERIMENTAL**. These notes do not prove the unrestricted
A077187 assertion. All residues are in the prime field, with `p != 2,5`.

## 1. Exact window formulas (PROVED)

For any prefix ending at `k`, write `C(k)=1||...||k`,
`R(k)=k||...||1`, `H(k)=10^(sum_{i<=k} digits(i))`, and `Y(k)=R(k)/H(k)`.
Appending the integer `k` of decimal length `e`, with `q=10^e`, gives

```
C(k) = q C(k-1) + k,
Y(k) = (Y(k-1) + k)/q,
M(k)/H(k-1) = q C(k-1) + k + Y(k-1).
```

Fix an `e`-digit window, put `L=10^(e-1)`, `k=L+n`, and let `(C0,Y0)` be
the state at `L-1`. If `q != 1`, define

```
A = C0 + L/(q-1) + 1/(q-1)^2,
B = Y0 - L/(q-1) + q/(q-1)^2.
```

Induction on the preceding recurrences gives

```
C(L+n-1) = q^n A - (L+n)/(q-1) - 1/(q-1)^2,
Y(L+n-1) = q^(-n) B + (L+n)/(q-1) - q/(q-1)^2.
```

Consequently, exactly,

```
M(L+n)/H(L+n-1) = q^(n+1) A + q^(-n) B - 2q/(q-1)^2.       (1)
```

The linear terms in `n` cancel. Thus, after the window is long enough to
contain every exponent modulo `ord_p(q)`, zero reachability is precisely

```
q A z^2 - [2q/(q-1)^2] z + B = 0,    z in <q>.             (2)
```

All degeneracies, including `A=0` or `B=0`, are retained in this polynomial
criterion. One must not divide by `A` without treating its vanishing.

When `q=1`, direct summation instead gives

```
M(k)/H(k-1) = k^2 + C0 + Y0 + L - L^2.                    (3)
```

Here `L=1/10`. Let `(Ce,Ye)` be the state at the end `10^e-1` of this
whole layer. Each coordinate increases by `9/200`; hence

```
M(k)/H(k-1) = k^2 + Ce + Ye.                              (4)
```

For a full window containing every residue modulo `p`, a zero exists if
and only if `-Ce-Ye` is a square (zero included).

## 2. A periodic block and its transient (PROVED)

Write

```
r = ord_p(10) = u t,   u=2^a 5^c,   gcd(t,10)=1,
T = lcm(r, ord_(9t)(10)),   lambda = 10^T mod r.
```

The choice of `9t` removes division-by-nine ambiguity in the cumulative
decimal length. Each full layer has affine diagonal transformation with
linear part `(alpha,alpha^-1)`, where

```
alpha_e = 10^[9 e 10^(e-1)],
D_e = e 10^e - (10^e-1)/9,
H_e = 10^D_e.
```

Its other parameters are `q=10^e`, `L=10^(e-1)`, and `N=9L`, reduced
modulo `p`. In a layer shifted by `T`, these latter parameters agree;
its multiplier is `alpha_e^lambda` since `T` is divisible by `r`.

When `u | 20`, all layers from `e=2` onward already have identical
actual and shifted multipliers: `20 | 9e10^(e-1)` for every `e>=2`
(at `e=2` the latter integer is 180, and for `e>=3` it is immediate),
while `10^T=1 mod t`. Thus only layer 1 can differ between the actual first
block and the stable block. Also the product of multipliers in a stable
block is 1. To check this without illicit division, use the integral
formula for `D_e`: `D_(2T)-D_T` is divisible by `u` because `10^T` is,
and by `t` because `10^T=1 mod 9t` and `T=0 mod t`.

The stable block is therefore a translation `G(z)=z+b` in the state
plane. This statement allows `b=0` and never presupposes nonzero drift.

## 3. Existence whenever u divides 20 (PROVED)

**Theorem.** If `p != 2,5` is prime and the 2,5-smooth part `u` of
`ord_p(10)` divides 20, then some mountain concatenation is divisible
by `p`. Equivalently, this covers all primes with
`v_2(ord_p(10)) <= 2` and `v_5(ord_p(10)) <= 1`, with no restriction on
the other prime factors or on their exponents.

For `p=3`, `M(3)=12321` supplies a witness. Assume henceforth `p!=3` so
the following divisions by 81 are valid.

Let `alpha=10^9` be the first actual layer multiplier, let
`alphabar=alpha^lambda` be its stable counterpart, and put
`rho=alphabar/alpha`. The first layer, where `q=10,L=1`, has form

```
C' = alpha (C + 10/81) - 91/81,
Y' = alpha^(-1) (Y + 1/81) + 80/81.
```

Replace `alpha` by `alphabar` for the stable layer. All subsequent
layers of the block coincide. Since the whole stable block has linear
part 1, the difference between the actual first block applied to zero
and the stable first block applied to zero is

```
D_C = (rho^(-1)-1) 10/81,
D_Y = (rho-1)/81.                                        (5)
```

Indeed the first-coordinate difference before the remaining layers is
`(alpha-alphabar)10/81`, which the remaining layers multiply by
`alphabar^(-1)`; the second-coordinate calculation is its inverse.
Consequently the state at the end of block `j`, for every `j>=1`, is

```
(C_(jT),Y_(jT)) = D + j b.                               (6)
```

Take `j=p`. The translation disappears in characteristic `p`, leaving
exactly the state `D`, regardless of whether the drift `b` vanishes.
The next window has decimal length `pT+1` and modular parameters
`q=10,L=1`. Substitution of (5) into (1) gives

```
A = 10/(81 rho),       B = rho/81,
M(L+n)/H(L+n-1) = (10z-rho)^2/(81 rho z),   z=10^n.       (7)
```

Because `rho` is a power of 10, `rho/10` belongs to `<10>`. Thus the
double root `z=rho/10` is always admissible. More explicitly choose

```
n = least nonnegative residue of 9 lambda - 10 modulo r,
k = 10^(pT) + n.                                        (8)
```

This is in the stated window because `0<=n<r<p` and its length is
`9*10^(pT)>p`. Equations (7)--(8) prove `p | M(k)`.

This proof resolves the zero-drift case in this whole order family and
also dispenses with a nonzero-drift test there.

The extension from `u|10` to `u|20` was supplied by the general-dynamics
research agent and independently checked by the audit agent before the
user paused this research. It uses only the strengthened divisibility
in Section 2. The saved script's completed witness checks cover `u|10`;
no additional numerical checks of the `u|20` extension were run after
the pause request.

If `gcd(r,10)=1`, there is no transient at all: `rho=1,D=0` and every
layer is periodic from the beginning. In this case the simpler witness
`k=10^(pT)-1` works: the endpoint state is zero, `k=0 mod p`, and its
digit base is 1 modulo `p`.

## 4. What the q=1 test does not prove (REFUTED/OPEN)

The claim that every sufficiently long `q=1` layer contains a zero is
**REFUTED**. For `p=11,e=2`, exact layer recurrence gives
`(C2,Y2)=(4,5)`, so (4) is `k^2+9`; its negative constant is 2, a
nonsquare modulo 11. The interval 10--99 covers all residues, yet has
no zero. Another example is `p=13,e=6`, with state `(10,1)` and again
negative constant 2, a nonsquare modulo 13.

These examples do not refute a statement conditional on actual zero
drift; their actual drifts are nonzero.

Even the transient-corrected q=1 route can fail. For `r=2t` with
`gcd(t,10)=1`, `rho=-1`, so (5) is `D=(-20/81,-2/81)`. Its q=1 test
asks whether 22 is a square. This need not hold (for example modulo
19), although (7) always gives a zero in the following q=10 window.
This explains why retaining subgroup windows is stronger than looking
only at q=1 layers.

For zero drift in a general stable period, let `S_i` be the finitely
many sums `Ce+Ye` at phases with `q=1`, and let `h=T/r`. The number of
roots counted over these phases is exactly

```
h + sum_i chi(-S_i),                                     (9)
```

where `chi` is the quadratic character, with `chi(0)=0`. Guaranteeing a
zero is equivalent to proving this number positive. No applicable
nontrivial character-sum estimate has been established: the `S_i` are
states of the coupled layer recurrence, not values of a known rational
function of uniformly bounded degree. Polynomial interpolation alone
does not supply such a bound. Also `h` can equal 1, when there is no
averaging benefit at all.

## 5. A stronger state-plane coverage proposal fails (REFUTED)

For a fixed stable period and an arbitrary initial pair `(C,Y)`, every
choice of the subgroup parameter `z` in (1) specifies an affine line
of initial pairs that hit zero. A `q=1` window specifies `(p+1)/2`
parallel lines, one per distinct square residue.

These lines need not cover the whole state plane. For `p=37`,
`r=T=3`, one period has `q=10,100,1`. The two nontrivial bases each have
order 3, hence contribute at most three lines each; the last window
contributes 19. The union has at most `25*37 < 37^2` points. Therefore
some states avoid zero throughout the period, even if every window
is fully sampled. Any successful argument must use the restrictions
on the actual reachable state, as (5)--(7) do.

## 6. Experiments and remaining obstruction

**EXPERIMENTAL:** `zero_drift_probe.py --bound 1000` examined every prime
`7<=p<=1000` with the exact period above, and compared the states at
`T` and `2T`. No simultaneous zero drift was found. This is only a
finite observation and is not used to prove the theorem.

**OPEN:** If `u` does not divide 20, multiple initial layers may differ
from the stable periodic block. The defect then composes several
distinct affine layer maps. Formula (5), and hence its forced double
root (7), is no longer justified. Proving that this actual defect
hits one of the subgroup windows is a sharply stated remaining
reachability question. No all-primes claim follows from these notes.
