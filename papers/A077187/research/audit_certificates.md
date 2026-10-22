# Independent audit of the stage-8 arithmetic certificate

Audit date: 2026-10-17. Baseline examined: commit
`a77866a4a34e83d6ad7c4f17c9ee07184864c31d` in PR #8. This audit concerns the
certificate chain in `papers/A077187`; it does not assert the unrestricted
A077187 conjecture or supply the missing general drift derivation.

## Conclusions and proof status

1. **PROVED (algebraic implications):** the displayed quadratic obstruction is
   a necessary condition for simultaneous zero drift, including all leading
   coefficient degeneracies; the cubic norm-tower identity and the one-shot
   smooth-order sieve are correct. Denominators and removal of the primes
   2, 3, and 5 cause no loss for the stage-8 order class.
2. **COMPUTATION_CERTIFIED (specified checks only):** the 486 norm files and
   table rows have the required phase coverage, positive stripped norms,
   correct exponent bounds, and stored-divisor consistency. Five selected
   full norms, one complete modular exponentiation/GCD, and the three direct
   decimal drift computations were independently rerun in this audit and
   passed. The complete 486-norm computation was deliberately not repeated.
3. **CONDITIONAL (baseline theorem as a self-contained repository proof):**
   the connection between the drift polynomial and the full decimal
   recurrence, and the affine-monodromy lemma, must be supplied as proofs.
   The baseline manuscript cites an unavailable `stage7` work for the latter;
   numerical cross-checks do not replace either derivation.
4. **CONDITIONAL (baseline cumulative claim):** this repository does not
   contain the cited proofs/certificates for all `0 <= b <= 7`. The stage-8
   arithmetic certificate alone cannot establish the README's cumulative
   `0 <= b <= 8` theorem.
5. No arithmetic counterexample or implementation error was found in the
   examined stage-8 coefficient, norm, and sieve code. This is a limited
   audit conclusion, not a claim that finite samples establish every formula.

## File and verification gaps

* `independent_relative_check.py` is listed in README.md but is absent from
  the baseline checkout. No delivered verification can be attributed to it.
* `audit_all_b8.py` does **not** recompute a GCD or a norm. It checks that the
  table's claimed `G` divides `N`, verifies exponent bounds, and compares the
  six nontrivial rows against a hardcoded dictionary. For a row claiming
  `G=1`, the divisibility check is automatic. It therefore checks consistency
  of supplied results, not the completeness of the prime exclusions.
* `verify_all.py` regenerates exactly five norms (phases 1, 202, 247, 547,
  698), not 486; it never launches the GMP sieve. Its concluding line
  `PASS ALL 486 certified phase rows` must be understood with this scope.
* The **full workflow** is stronger: it runs
  `generate_norms_parallel.py`, then `run_sieves.sh`, then `verify_all.py`.
  Thus the limitations of the final verifier do not invalidate a successful
  execution of that complete workflow. The coordinating audit inspected the
  dedicated stage-8 workflow run `39037140817`: it completed successfully on
  source commit `51c5b046a44e470ef578e15efa480d2a4d8e0460` and produced the
  baseline generated-artifact commit. The latest generic PR workflow is a
  separate workflow for another paper and cannot substitute for this run.
  This CI status was supplied by the coordinating audit; it was not fetched
  independently by this certificate-audit worker.
* The statement that six norms match a previous stage byte-for-byte is not
  supported by identified comparison files or a comparison script in this
  checkout. It should be removed or supplied with precise artifacts.

## Algebraic audit

### Quadratic obstruction, including degeneracies

Write `F=a+b m+c m^2` and `G=d+e m+f m^2`, and let

```
A = c*d-a*f,   B = c*e-b*f,   C = b*d-a*e.
```

The formal quadratic Sylvester resultant is `A^2-B*C`; this identity was
also checked with SymPy. More importantly, if a finite field element `m`
satisfies `F=G=0`, then

```
c*G-f*F = A+B*m = 0,
b*G-e*F = C-B*m^2 = 0.
```

Consequently `A^2-B*C=0`. This proof requires no division by `b`, `c`,
`e`, `f`, or `B`. It remains valid if either polynomial becomes linear,
constant, or identically zero modulo the prime. Common roots at infinity
can create extra resultant zeros, but extra zeros are harmless because
the argument uses only necessity. Thus degenerate leading coefficients do
not create a missed exception in this sieve.

### Integer coefficient representation

For `t=729`, `g=gcd(j,t)`, `n=t/g`, and `w=zeta^j`, `w` has exact order `n`.
The finite geometric identities give

```
sum(l*w^(l+1), l=0..n-1) = n*w/(w-1),
h_j = t*w/(w-1),
zeta^(-j)*h_j^2 = t^2*w/(w-1)^2.
```

In `sums(j)`, the map `l -> j*(l+1) mod t` is injective on `0..n-1`.
The cyclic convolution implements the square followed by the shift
`zeta^(-j)` exactly. Thus `H` and `H2` represent the manuscript's `h_j`
and `j_j`. This verifies the algebraic translation between the scalar
rational expressions and the group-ring sums; it does not prove their
initial derivation from decimal concatenation.

The uses of NumPy `int64` before reduction are safe at this fixed size.
Each `H` coefficient has absolute value below `t`, and each `H2`
coefficient is bounded by `g^2*n*(n-1)^2 < t^3`. Across fewer than `t`
summands, even the loose bound `400*t^4 < 1.2e14` for the quadratic
coefficient accumulation is far below `2^63`. The linear coefficients
are smaller. Subsequent convolutions in `ring_mul` and all norm-tower
convolutions use `dtype=object` and Python integers. The reduction
`zeta^486=-zeta^243-1`, together with `zeta^729=1`, is implemented
correctly on the degree ranges that these functions receive.

### Norm obstruction and cubic tower

When the two drift coordinates vanish and `p` is in the target order
class, `D=200*729^2` is invertible modulo `p`. The evaluated algebraic
integer `Q_gamma` vanishes under the map `zeta -> 10^(r/729)` to `F_p`.
Since this image has order 729, it is a root of `Phi_729`. The reduction
of the norm/resultant therefore vanishes modulo `p`. No division by a
leading coefficient is involved in this implication.

The relative extension at tower levels `n>=2` has degree three; with
`x^3=y`, multiplication of its three conjugates gives

```
Norm(A+x*B+x^2*C) = A^3+y*B^3+y^2*C^3-3*y*A*B*C.
```

`relative()` partitions coefficients by exponent modulo 3 and implements
this formula over the lower cyclotomic ring. At the bottom,
`Norm(a+b*zeta_3)=a^2-a*b+b^2`. A nonzero element has a positive norm in
this totally imaginary cyclotomic field. Removing factors 2, 3, and 5
cannot remove any prime in the target order family. The potential
zero-norm infinite loop in the standalone `tower_norm.py` stripping
loop is not reached for the supplied nonzero norms; the all-phase
generator explicitly asserts `N>0` before stripping.

### One-shot sieve and true phases

For `p|N` with `ord_p(10)=6561*s`, `s=2^a*5^c`, one has
`6561*s <= p-1 <= N-1`, hence `s <= W=floor((N-1)/6561)`.
The separately computed bounds `2^A <= W < 2^(A+1)` and
`5^C <= W < 5^(C+1)` imply `s | S=2^A*5^C`.
Since `S/s` is coprime to 3,

```
ord_p(10^(2187*S)) = 3.
```

Therefore every target prime divisor of `N` divides the one-shot GCD.
The code computes the floor logarithms exactly: GMP's base-2 size is
exact, and the base-5 bound uses integer multiplication. All supplied
norms have `W>=1`. The lemma does not assert that every GCD factor is a
genuine zero-drift prime; filtering by its actual phase is valid.

The three candidate primes were independently checked for primality and
exact multiplicative order. Their true-phase norm residues are nonzero:

| p | order of 10 | true phase | stripped true-phase norm mod p |
|---:|---:|---:|---:|
| 52489 | 26244 | 547 | 21241 |
| 328051 | 328050 | 452 | 195900 |
| 839809 | 52488 | 638 | 234413 |

This directly excludes these candidates using the stored actual-phase
norms, independently of the claimed actual-phase GCD values. All three
actual-phase norms were among the five norms regenerated in this audit.

## Reproduced evidence

Python used: `C:/Users/29848/AppData/Local/Programs/Python/Python313/python.exe`,
with NumPy 2.2.5 and SymPy 1.14.0. No supplied source or certificate file
was changed by these checks; bytecode writing was disabled. The smaller
bundled runtime originally suggested lacked SymPy.

* All 486 file/row checks: complete, unique primitive phases modulo 729;
  `N>1`, `gcd(N,30)=1`, `G|N`, and both exact exponent intervals passed.
* Full regenerated norms: phases 1, 202, 547, 452, 638 matched exactly;
  stripped decimal lengths respectively 5805, 5797, 5794, 5806, 5792.
* Independently recomputed Python `pow` and `math.gcd` for phase 202:
  `G=328051` (approximately 18.4 seconds).
* Independent SymPy cyclotomic resultants agreed with the norm tower for
  30 seeded random integer vectors at conductors 3, 9, and 27.
* `check_direct_b8.py` passed, returning drift vectors
  `(45106,17218)`, `(60057,66998)`, and `(433423,436112)` for primes
  52489, 328051, and 839809, respectively.

The core norm and independent-resultant checks can be reproduced from
`papers/A077187` using the following Python code:

```python
import random
from pathlib import Path
import sympy as sp
import exact_b8_fast as e
from tower_norm import full_norm

for g in (1, 202, 547, 452, 638):
    N = full_norm(e.crosscheck(g), 6)
    for q in (2, 3, 5):
        while N % q == 0:
            N //= q
    assert N == int(Path(f'norm_gamma_{g}.txt').read_text())

x = sp.Symbol('x')
rng = random.Random(77187)
for n in (1, 2, 3):
    degree = 2 * 3**(n-1)
    phi = sp.cyclotomic_poly(3**n, x)
    for _ in range(10):
        cs = [rng.randint(-4, 4) for _ in range(degree)]
        Q = sum(c*x**i for i, c in enumerate(cs))
        assert int(sp.resultant(phi, Q, x)) == full_norm(cs, n)
```

These successful checks support the delivered finite arithmetic, while
leaving the missing symbolic decimal-to-drift derivation and the older
stage dependencies explicit. None supplies an all-primes existence proof.

## Supplement: independently audited new transient theorem

This section records work completed before the user's pause request on
2026-10-17. No new research or calculations were undertaken after that
request. It concerns new arguments developed during this session, not
claims already present at the baseline commit.

### Unit-order case: a direct return to the initial state

**PROVED and independently checked.** If `r=ord_p(10)` satisfies
`gcd(r,10)=1`, put `T=lcm(r,ord_(9r)(10))`. The complete decimal-layer
affine maps are periodic from the first layer, with period `T`. Indeed
their field parameters `10^(e-1)` and `10^e` repeat because `r|T`, and
their layer multiplier

```
alpha_e = 10^(9*e*10^(e-1)) mod p
```

repeats because `10^T=1 mod r`. The accumulated digit length is

```
D_E = (1+(9*E-1)*10^E)/9.
```

Using `10^T=1 mod 9r` and `r|T` gives `D_T=0 mod r`, so the complete
period has linear part the identity on `(C,Y)`. If its translation is
`b`, then `(C_(jT),Y_(jT))=j*b` since the initial state is zero. Taking
`j=p` returns both coordinates to zero.

For `K=10^(pT)-1`, its width is `pT`, so its final digit-block multiplier
is `q=10^(pT)=1 mod p`, and `K=0 mod p`. In general the mountain at a
completed prefix has

```
M(K)/H_K = C_K/q + Y_K - K/q.
```

Consequently `M(K)=0 mod p`. This proves the explicit witness
`k=10^(pT)-1` without separating zero from nonzero drift, using endpoint
slopes, or assuming a sufficiently long internal interval. It includes
`p=3`, where `r=T=1`; no division by 3 appears in the finite-field
argument (the displayed digit-length quotient is an integer identity).

Independent recurrence checks passed for all 24 primes below 500 with
`gcd(r,10)=1`. The first three period states agreed with `j*b`; for the
12 cases with `p*T<=100000`, the recurrence was additionally iterated all
the way to `p*T`, returning `(C,Y,H)=(0,0,1)` exactly.

### Smooth part dividing 20: one exceptional initial layer

**PROVED and independently checked.** Write
`r=u*v`, where `u=2^a*5^c` and `gcd(v,10)=1`. Assume `u|20`, equivalently
`a<=2` and `c<=1`. For `p!=3`, take

```
T = lcm(r, ord_(9v)(10)),
rho = 10^(9*(10^T-1)) mod p.
```

All parameters of layer `e+T` equal those of layer `e` except possibly
the layer multiplier. For `e>=2`,

```
20 divides 9*e*10^(e-1),
```

so the `u`-part of that exponent is already stable; the `v`-part repeats
because `10^T=1 mod v`. Thus every layer from `e=2` onward repeats after
`T`. Only the first layer differs from its stabilized counterpart; its
stabilized multiplier is `rho` times its actual multiplier.

The stable complete blocks have linear part the identity. For example,
`D_(jT)` is independent of `j>=1` modulo `r`: modulo `u` it is `9^-1`,
and modulo `v` it is zero. The integer quotient in the formula for
`D_E` is handled modulo `9v` before division, and 9 is invertible modulo
`u`. Hence the ratio of successive boundary values of `H` is one.

At the first layer, `q=10`, `L=1`. With `alpha=10^9`, its affine map is

```
C' = alpha*(C+10/81) - 91/81,
Y' = alpha^(-1)*(Y+1/81) + 80/81.
```

Replacing `alpha` by `rho*alpha` gives its stable version. Propagating
their difference through the identical remaining layers gives the
boundary defect

```
delta_C = (rho^(-1)-1)*10/81,
delta_Y = (rho-1)/81.
```

If the stable block translation is `b`, all positive block boundaries
satisfy `state_(jT)=delta+j*b`. Therefore `state_(pT)=delta` regardless
of whether the drift is zero. The original `r=2t` claim is recovered
with `rho=-1`, giving `delta=(-20/81,-2/81)`; its argument also applies
to `p=11` without an endpoint-slope exception.

In the next layer, let `k=10^(pT)+n`, `z=10^n mod p`. Direct finite
geometric sums from the seed `delta` give

```
M(k)/H_(k-1) = (10*z-rho)^2/(81*rho*z).
```

This identity was independently expanded and factored with SymPy; it
is valid for every integer `n` in this layer. Choosing

```
n = (9*10^T-10) mod r, with 0 <= n < r,
```

gives `z=rho/10` and therefore the explicit witness

```
k = 10^(pT) + n.
```

It lies in the required digit layer, since `n<r<=p-1` and that layer has
length `9*10^(pT)`. The exceptional denominator prime `p=3` is already
settled by the unit-order argument (also directly by `M(3)=12321`).

The independent recurrence check covered all 75 primes in `7..499`
whose smooth part divides 20, including every possible smooth part
`1,2,4,5,10,20`. It computed both boundary states at `T` and `2T` and
checked `2*state_T-state_(2T)=delta`; it also checked the proposed
exponent `n` gives `10*10^n=rho`. A separate earlier run checked all 25
primes below 500 of the form `r=2t`, `gcd(t,10)=1`. These calculations
support the algebraic proof; they are not its universal justification.

### Scope of the mechanism and paused work

The `u|20` upper limit is exact for the assertion that **only the first
layer differs from its stable counterpart**. The gcd of the integer
exponents `9*e*10^(e-1)` over all `e>=2` is 180, whose 2-and-5 part is
20. In particular the second exponent is 180, which is divisible by
neither 8 nor 25. Thus simply extending the same one-layer argument to
`8|u` or `25|u` is unjustified. This is a limitation of this proof
mechanism, not a counterexample to mountain-concatenation existence.

Before the pause, a more general finite-transient reduction had been
identified: if the actual and stable initial prefixes have affine
offsets `a` and `s`, and the stable prefix has linear part `L`, then
the full-block defect is `L^(-1)*(a-s)`. Taking `p` stable periods
eliminates the translation and reaches this defect. A general proof that
such a defect always yields a mountain zero was **not obtained**.
Explicit counterexample searches for naive extensions at smooth parts
8 and 25, and a general factorization beyond the one-layer case, were
not executed before the pause. No unrestricted all-primes theorem is
claimed.
