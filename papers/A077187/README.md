# OEIS A077187 — decimal mountain concatenations (partial results)

**Author:** Qichao Wang. **Updated:** 2026-10-18.
**Status:** computer-assisted, not externally peer reviewed. **The unrestricted A077187 conjecture remains OPEN.**

Let
\[
M(k)=1\Vert2\Vert\cdots\Vert k\Vert(k-1)\Vert\cdots\Vert1
\]
be the decimal mountain concatenation. This folder collects the current *partial* existence theorems and reproducible exact-integer certificates.

## Current proof status

Write `ord_p(10)=u*v`, where `u=2^a*5^c` and `gcd(v,10)=1`.
The integrated [affine/spectral paper](research/fixed_v_spectral_families.pdf)
and its [source](research/fixed_v_spectral_families.tex) contain these results:

| Scope | Status | Proof mechanism |
|---|---|---|
| `u` divides 20, arbitrary `v` | PROVED | Explicit square and subgroup witness; no drift assumption |
| `v` divides 9 | PROVED | Elementary invariant `U+V=9/100` |
| `v=11,33,99`, `a=0` | PROVED | Exact invariant `11*z*U-9*V=909*(z+1)/100` |
| `v=11,33,99`, `a>=1` | COMPUTATION_CERTIFIED | Ten quadratic norm obstructions and 11385 complete index exclusions |
| `v=7`, arbitrary `a,c` | COMPUTATION_CERTIFIED | Existing quadratic spectral certificate |

The small primes 3 and 11 have witnesses `M(3)=12321` and `M(2)=121`;
2 and 5 are impossible because the final digit is 1.
The new formulas and certificates received an
[independent audit](research/audit_spectral_update_2026-10-18.md).

The general phase theorem reduces `v` to `t=v/gcd(v,9)` before
compression. It subsumes the separately retained
[nine-torsion lift](research/nine_torsion_lift_v33_v99_2026-10-18.md).
For `v=11*3^b`, the exact multiplier defect also proves why the
22-phase mechanism stops at `b=2`; this is not an arbitrary cutoff.
The [linear continuation](research/involution_linear_continuation_2026-10-18.md)
supplies the Fourier calculation and separates the algebraic odd branch
from the computer-assisted even branch.

For the other main route, a [tail-phase reduction](research/zero_drift_continuation_2026-10-18.md)
shrinks the first-window field to order `u/gcd(u,20)`. It also certifies
that the first three windows after `p` blocks fail on a set of primes
of density `1/128` with `u=8`. This is an obstruction to that particular
construction, not to A077187 or to the unproved assertion conditional
on actual zero drift.

Reproduce the new checks from the repository root:

```sh
python papers/A077187/research/certify_involutive_families.py
python papers/A077187/research/audit_reduced_spectral.py
python papers/A077187/research/certify_fixed_v33_v99.py
python papers/A077187/research/audit_fixed_v33_v99.py
python papers/A077187/research/zero_drift_tail_gauge_2026_10_18.py --examples --symbolic
```

The finite identity tests check implementations; the general claims rest
on the written algebra and, where labelled, exhaustive exact certificates.
See [HANDOFF.md](research/HANDOFF.md) for the unresolved proof obligations.
The dated notes below preserve earlier results and their original scope;
the current status table supersedes earlier statements that `v=33,99`
are still open or require norm certificates in both parity branches.

## Earlier stage-8 certificate and its dependency boundary

For primes \(p\ge7\), let \(r=\operatorname{ord}_p(10)\).
The original project claimed the cumulative smooth-order family
\[
\boxed{r=2^a3^b5^c,\qquad a,c\ge0,\ 0\le b\le8
\quad\Longrightarrow\quad \exists k\ge1:\ p\mid M(k).}
\]
The stage-8 paper specifically treats **\(b=8\)**. The audit found that
the earlier `b<=7` certificate package is not present, so the cumulative
display must not be read as a closed proof supplied by this checkout.
The missing recurrence-to-coefficient derivation is now supplied in
[general_dynamics.md](research/general_dynamics.md); this does not recreate
the missing lower-stage certificates. The stage-8 arithmetic itself passed
the checks described in [audit_certificates.md](research/audit_certificates.md).
No least-k theorem or OEIS edit is claimed.

For \(b=8\), all **486 primitive phases modulo 729** were checked using exact cyclotomic norms and a GMP one-shot gcd sieve. Six phases had nontrivial gcd, with prime factors 52489, 328051, and 839809. Each factor's actual order phase differs from the phase at which the gcd appears; its actual-phase gcd is 1. Therefore no admissible prime makes both affine-drift coordinates vanish in this order class.

The novel computational simplification is the **cubic relative norm tower** reducing cyclotomic norm degrees
\[
486\to162\to54\to18\to6\to2\to1.
\]
For a cubic relative extension, the core identity is
\[
\operatorname{Norm}(A+xB+x^2C)=A^3+yB^3+y^2C^3-3yABC,\qquad x^3=y.
\]
The current research priority is a general drift or zero-reachability
mechanism, rather than another finite exponent layer.

## Materials

- [main.pdf](main.pdf) — two-page English partial-theorem paper (compiled from [main.tex](main.tex)).
- [candidate_table.tex](candidate_table.tex) — complete list of the six nontrivial gcd rows, typeset in the paper.
- [exact_b8_fast.py](exact_b8_fast.py), [tower_norm.py](tower_norm.py), [generate_norms_parallel.py](generate_norms_parallel.py) — exact formula and 486-norm computation.
- [norm_gamma_*.txt](.) — all 486 full integer norms (approximately 5,800 digits each).
- [one_shot_gmp_b8.cpp](one_shot_gmp_b8.cpp), [all_486_gmp.tsv](all_486_gmp.tsv) — full-range one-shot GMP gcd checks.
- [audit_all_b8.py](audit_all_b8.py), [check_direct_b8.py](check_direct_b8.py), [verify_all.py](verify_all.py) — exact audits, independent finite-field checks and full digit-layer recurrences.

The source scripts use Python 3, SymPy and NumPy. The gcd program uses GMP and a C++17 compiler.

Reproducibility steps (from this directory):
1. `python generate_norms_parallel.py`
2. `c++ -O3 -std=c++17 one_shot_gmp_b8.cpp -lgmpxx -lgmp -o one_shot_gmp_b8`
3. `bash run_sieves.sh`
4. `python verify_all.py`
5. Compile `main.tex` twice with `pdflatex`.

All computational evidence supports the specified infinite subfamily only. The underlying formulas, software and final claims await external mathematical audit. No all-primes proof is claimed.


## Unrestricted-order research continuation (October 18, 2026)

The separate research notes do **not** extend the fully certified b=8 result
to all primes. They develop a general-order finite-defect transfer and
two-offset drift criterion, then prove the exact elementary invariant
\[
\Delta_C+\Delta_Y=9/100\pmod p\ne0
\]
for every prime \(p\ge7,\ p\ne11\), whose \(\operatorname{ord}_p(10)\)
has no prime factors outside \(2,3,5\) and has \(v_3\le2\).
This gives a proof of the low-\(3\)-adic-order class independent of any
cyclotomic norm certificates.

- [Elementary invariant and refined zero-drift decision](research/elementary_drift_and_zero_drift_decision_2026-10-18.md)
- [Exact finite scan, no floating point](research/drift_scan_general.cpp):
  compile with \`g++ -O3 -std=c++17\` and run with argument \`5000\`.
- [Independent within-window and subgroup-root audit](research/window_quadratic_audit.py):
  run \`python research/window_quadratic_audit.py\`.

Finite evidence: 665 checked primes below 5000 (excluding \(p=11\)) all
had nonzero drift. The square-root/subgroup test rigorously decides any
individual zero-drift prime, if encountered; **the universal existence
conjecture remains open.**


## Exact repunit-ring order certificates, October 18 continuation

A second **independent computational theorem** now covers all primes whose
multiplicative order of 10 belongs to 42 specific previously uncovered
order classes \(r\le500\). For each such \(r\), arithmetic is performed
directly modulo \(N_r=10^r-1\), without factoring that integer. The
difference of two exact digit-layer states gives \((U_r,V_r)\); the full
gcd \(G_r=\gcd(N_r,U_r,V_r)\) has prime factors dividing \(990r\).
Since a prime of exact multiplicative order \(r\) must exceed \(r\),
none of those primes can have zero drift, so the general two-offset
witness theorem applies.

Together with earlier proved smooth-order / \(u\mid20\) classes, this
gives the **cumulative** existence result for all primes satisfying
\(\operatorname{ord}_p(10)\le500\), subject to those earlier certificates'
independent review. The new 42-class result itself does not depend on
their validity.

- [Mathematical proof, full class list and exact gcd table](research/order_bound_500_certificate_2026-10-18.md).
- [Self-contained standard-library Python certifier](research/certify_orders_le500.py).
- Run \`python3 papers/A077187/research/certify_orders_le500.py\` from repository root.
- GitHub Actions: \`.github/workflows/a077187-order-bound.yml\`.

The unrestricted all-primes OEIS problem remains **open**: certification
for all \(r\le500\) is a finite order-bound theorem, not a proof for
unbounded multiplicative orders.


### Cyclotomic refinement and negative controls

The tempting extension
\(\operatorname{rad}(G_r)\mid\operatorname{rad}(990r)\) for *all*
\(r\) is false: at \(r=174,258\), one finds \(G_r=189=27\cdot7\),
although \(7\nmid990r\). These are not counterexamples to the mountain
conjecture because \(\operatorname{ord}_7(10)=6\), not 174 or 258.

Working modulo \(\Phi_r(10)\) filters such lower-order prime factors.
For ten independent check cases, the refined gcd
\(\gcd(\Phi_r(10),U_r,V_r)\) is 1 except at \(r=272\), where it is 17,
a divisor of \(r\). See
[cyclotomic spot checker](research/audit_cyclotomic_spots.py) and
[mathematical explanation](research/order_bound_500_certificate_2026-10-18.md).
This is a finite observation, not an all-order theorem.


## Improved self-contained bounded-order theorem: \(\operatorname{ord}_p(10)\le744\)

The earlier cutoff of 500 is now superseded by an **independently
certifiable cutoff of 744**, using 77 exact-order gcd certificates
together with two elementary infinite-family lemmas (\(u\mid20\)
and \(v\mid9\), where \(r=u\,v\) is split into its \(2,5\)-smooth
and coprime-to-10 parts). Thus the bounded-order result **no longer
depends on the high-\(3\)-power cyclotomic norm tower**.

- [Bounded-order theorem, full proof and results](research/order_bound_744_theorem_2026-10-18.md).
- [Typeset research note source](research/order_bound_744.tex);
  [compiled PDF](research/order_bound_744.pdf) (generated by CI).
- [35 additional exact GCD rows](research/certify_orders_le744.py)
  (31 genuinely new classes + four former norm-dependent cases).
- [Independent direct prime-field audit](research/audit_order_744_prime_field.py)
  at exact orders 584, 664, 696.
- [Original 42-row certificate](research/certify_orders_le500.py).

Reproduce with Python 3 and no third-party packages:
\`\`\`sh
python3 papers/A077187/research/certify_orders_le500.py
python3 papers/A077187/research/certify_orders_le744.py
python3 papers/A077187/research/audit_order_744_prime_field.py
\`\`\`

The apparent obstruction at \(r=696\), \(G_r=189=3^3\cdot7\),
is not a counterexample: \(\operatorname{ord}_7(10)=6\ne696\).
The computational certificate checks the exact multiplicative order of
*every* prime factor of *every* small gcd, not merely whether the
factor divides \(990r\).

**The unrestricted all-primes existence conjecture is still open.**
This finite-order result is conditional on mathematical review of
the two elementary arguments and on independent reproduction of
the exact-arithmetic programs.


## Latest bounded-order theorem: \(\operatorname{ord}_p(10)\le1000\)

**Supersedes the earlier cutoffs of 500 and 744.**
We certify every prime \(p\ne2,5\) with
\(\operatorname{ord}_p(10)\le1000\) using two previously established
elementary infinite-family lemmas and **112** complete, exact
order-class certificates. The 35 newly added classes are
\(745\le r\le1000\). The unrestricted all-primes problem remains OPEN.

New theoretical ingredient: the \(T\)-layer stable affine product has
identity linear part over \(\mathbb Z/(10^r-1)\), so its translation
(the two-coordinate drift) can be computed from a zero initial state in
**one stable period**, without running all \(2T\) layers.

More strongly, for every one of the 35 new classes,
\[
\gcd(\Phi_r(10),U_r,V_r)=1.
\]
This is verified by a separate standard-library Python program,
after exact C++/GMP computation of
\(G_r=\gcd(10^r-1,U_r,V_r)\).
It **does not** assert universal cyclotomic coprimality: \(r=272\)
is an existing exception with cyclotomic gcd 17.

- [Detailed theorem and proof](research/order_bound_1000_theorem_2026-10-18.md)
- [New LaTeX manuscript](research/order_bound_1000.tex) and
  [PDF](research/order_bound_1000.pdf) (generated by GitHub Actions)
- [Single-period GMP exact certifier for 35 new classes](research/single_period_order_1000.cpp)
- [Independent field-level audit](research/audit_order_1000_prime_field.py)
- [Independent cyclotomic-coprimality audit](research/audit_cyclotomic_order_1000.py)

Commands from \`papers/A077187/research\`:
\`\`\`sh
python3 certify_orders_le500.py
python3 certify_orders_le744.py
g++ -O3 -std=c++17 single_period_order_1000.cpp -lgmpxx -lgmp -o order1000
./order1000 > order1000_rows.tsv
python3 audit_order_1000_prime_field.py
python3 audit_cyclotomic_order_1000.py order1000_rows.tsv
\`\`\`

All 35 exact new tuples are embedded in the certifier, and its
SHA-256-pinned output is validated in CI. As before, this finite
computer-assisted theorem is subject to independent code and
mathematical review; **nothing here proves A077187 for unbounded
multiplicative orders**.


## New unrestricted-order structural work (18 October)

The finite cutoff of 1000 remains valid, but the latest work targets
an **unbounded-order mechanism** rather than further extending the
cutoff. See
[order-inflation and scalar-GCD note](research/order_inflation_and_scalar_gcd_2026-10-18.md)
and [exact reference auditor](research/audit_scalar_gcd_and_inflation.py).

**Proved for every formal order \(r\):** if \(p\mid10^r-1\), its
actual multiplicative order is \(s\mid r\), and
\(T_t=\operatorname{lcm}(t,\operatorname{ord}_{v_t}(10))\), then
\[
\Delta_r=(T_r/T_s)\Delta_s\pmod p .
\]
In particular,
\[
\operatorname{rad}\gcd(10^r-1,3T_r)
\mid\operatorname{rad}\gcd(10^r-1,U_r,V_r),
\]
and both drift coordinates are divisible by 9 over the full
integer repunit ring. The note proves these assertions and an
equivalence between the **missing reverse radical inclusion** and
nonzero true-order drift for all primes.

**New conjecture, NOT a theorem:** exact finite computations
for all \(2\le r\le180\), plus selected higher orders through
\(r=4624\), give
\[
\gcd(10^r-1,U_r,V_r)
=\gcd(10^r-1,U_r+V_r)
=\gcd(10^r-1,9T_r).
\]
If the weaker global bound
\(\gcd(10^r-1,U_r+V_r)\mid9T_r\) could be
proved for arbitrary \(r\), it would imply that the drift
is nonzero for every prime of exact order \(r\), and hence
settle the existence conjecture. **This implication is proved;
its hypothesis is not.**

Reproduce the finite scalar and inflation tests via
\`python3 papers/A077187/research/audit_scalar_gcd_and_inflation.py\`.
A separate GitHub Actions workflow runs the test automatically.


The same finite audit also confirms the **stronger single-offset slope**
identity \(\gcd(10^r-1,10U_r+V_r)=\gcd(10^r-1,9T_r)\)
for \(2\le r\le180\), with selected higher-order samples.
A universal proof of even its weaker divisibility form
would force the \(k=10^{jT_r}\) (no \(+1\)) construction
to work for all primes \(p\ge7\) except \(11\), which already
has the short witness \(M(2)=121\).
This remains a conjectural route, not a claimed theorem.


## Exact primitive-order cyclotomic obstruction (October 18)

A new *unbounded-order structural equivalence* sharpens the zero-drift
problem. For each \(r\ge2\), let \((U_r,V_r)\) be the stable-period
translation modulo \(10^r-1\), and put
\[
H_r=\gcd\bigl(\Phi_r(10),U_r,V_r\bigr).
\]
Then **all primes of exact order \(r\) have nonzero drift if and only if**
\[
\boxed{\operatorname{rad}(H_r)\mid\operatorname{rad}(r).}
\]
This follows from the cyclotomic primitive-order property: the primes
dividing \(\Phi_r(10)\) but not \(r\) are precisely the primes
with \(\operatorname{ord}_p(10)=r\). Repeated gcd removal against \(r\)
decides the criterion without factoring \(10^r-1\).

This is a **reduction**, not proof that the criterion holds at all \(r\).
If it fails, the surviving prime factors would be genuine zero-drift
primes, but might still divide other mountain concatenations.

- [Full theorem and proof](research/cyclotomic_exact_obstruction_2026-10-18.md)
- [Exact primitive-order decision and nine test cases](research/exact_cyclotomic_obstruction.py)
- [Dedicated CI](../../.github/workflows/a077187-exact-obstruction.yml)

No claim of an unrestricted A077187 proof is made.


## Structural continuation: two-way block words and integrable windows

[Global structure and proofs (October 18)](research/global_block_hyperbola_structure_2026-10-18.md)
reframes the unbounded-order research **without extending the finite
order cutoff**:

- The exact stable drift over \(\mathbb Z/(10^r-1)\) is simply the
  pair of residues of all integers \(10^T,\dots,10^{2T}-1\)
  concatenated in *increasing and decreasing* order. True-order
  zero drift is equivalent to simultaneous divisibility of these two
  explicit block words.
- Inside each fixed-width digit layer, polynomial centered coordinates
  obey \(X\mapsto qX,\ Z\mapsto q^{-1}Z\) and preserve \(XZ\).
  The normalized mountain condition becomes the intersection
  \(qX+Z=2q\) with that invariant hyperbola (with \(q=1\)
  treated as a separate unipotent layer).
- Reflection of a full consecutive-number block cancels the weighted
  first moment exactly:
  \(C'+AY'-AC-Y=(L+q-1)\sum_{i<m}q^i\).
  This explains the earlier \(9/100\) invariant when the layer
  multipliers are all 1, **without** assuming that the varying twists
  cancel for arbitrary multiplicative orders.
- A nonzero drift gives **at least \(r-\gcd(r,2)\) distinct fixed-offset
  witness families**, each containing infinitely many divisible
  mountains. This strengthens the former two-offset sufficient
  criterion quantitatively but does not rule out zero-drift primes.

A deliberately small independent check is in
[structural audit](research/audit_global_block_geometry.py), with
dedicated [GitHub Actions workflow](../../.github/workflows/a077187-global-geometry.yml).
A further **exact whole-period identity** (Theorem E in the same note)
decomposes, for any scalar \(\lambda\), the drift combination
\(\lambda U_r+V_r\) into a reflected-block baseline and an explicit
position-phase mismatch:
\[
\lambda U_r+V_r=\sum_d P_d\bigl[
(L_d+q_d-1)\Sigma_d+(\lambda\Theta_d^{-1}-1)B_d\bigr],
\qquad \Theta_d=P_d^2A_d .
\]
This is valid for **every** \(r\), over the composite ring.
The earlier \(v\mid9\) proof is exactly the case where
the \(\lambda=1\) mismatch vanishes. The general mismatch is
**uncontrolled**, not tacitly zero. The new
[short twisted-flux audit](research/audit_twisted_reflection.py)
checks it independently on five small orders.

The principal remaining mathematical gap is the **global interaction
of layer interfaces and the position-phase mismatch**, not the
locally integrable within-layer recurrence. The all-primes conjecture
remains open.


## Latest: fixed-coprime-order spectral compression and two new INFINITE families

A new **general structural theorem** shows that for any fixed coprime
part \(v\) of \(r=\operatorname{ord}_p(10)=2^a5^cv\),
the full stable drift, despite spanning
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\) digit layers,
reduces to at most
\[
\ell=\operatorname{lcm}(v,\operatorname{ord}_v(10))
\]
cyclotomic phase classes. Both drift coordinates are polynomials
of degree at most two in \(m=r/\gcd(r,\ell)\), with coefficients in
a cyclotomic field of degree at most \(\varphi(\ell)\) **independent
of unbounded \(a,c\)**. The formulas include all \(q=1\) singular
layers exactly, whose two reflected block contributions equal \(9/200\).

The new **computer-assisted infinite-order-class theorems** assert
\[
\boxed{\operatorname{ord}_p(10)
=7\cdot2^a5^c\ \text{or}\ 11\cdot2^a5^c
\quad\Longrightarrow\quad p\mid M(k)\text{ for some }k.}
\]
These are **not** merely finite \(r\le1000\) checks. For \(v=7\),
twelve fixed degree-six quadratic resultants and 4532
factorization-free cyclotomic exclusions close the class. For \(v=11\),
twenty fixed degree-ten *linear* resultants (the quadratic coefficients
vanish exactly) and 3943 phase-aware exclusions close the class.
Each norm is pinned; no target primes are enumerated or giant
repunit factorizations used.

- [Unified typeset paper](research/fixed_v_spectral_families.tex)
  and [compiled PDF](research/fixed_v_spectral_families.pdf)
  (produced by GitHub Actions).
- [Generic spectral derivation and complete \(v=7\) theorem](research/fixed_v_spectral_compression_v7_2026-10-18.md).
- [Linear-degeneracy derivation and complete \(v=11\) theorem](research/fixed_v11_linear_spectral_theorem_2026-10-18.md).
- [Exact quadratic norms and elimination](research/certify_fixed_v7.py).
- [Exact linear norms and elimination](research/certify_fixed_v11.py).
- [Independent field-level checks: \(v=7\)](research/audit_fixed_v7.py)
  and [\(v=11\)](research/audit_fixed_v11.py).

Independent GitHub Actions workflows
\`.github/workflows/a077187-fixed-v7.yml\` and
\`.github/workflows/a077187-fixed-v11.yml\`
have passed both symbolic proofs and direct field cross-checks.
The unrestricted all-primes conjecture is **still OPEN**, as the
uniform elimination has not been proved for arbitrary coprime part \(v\).


### A further analytic simplification for \(v\mid99\)

The exact quadratic degree drop for \(v=11\) is now explained by
[a pure involutive-symmetry proof](research/involutive_spectral_degree_drop_2026-10-18.md).
Whenever \(10^2\equiv1\pmod v\), the stable phase multipliers obey
\(A_{-j}=A_j^{-1}\), and the cumulative phases satisfy
\(P_{\ell+1-j}=P_j\). The quadratic coset weight is symmetric under
\(\zeta\mapsto\zeta^{-1}\); its weighted contributions cancel in pairs.
Consequently \(U_2=V_2=0\) **for every \(v\mid99\)**, including
\(v=33,99\). This is an unconditional structural theorem, but
**the nonzero-drift result for \(v=33,99\) remains open**.


## Nine-torsion lift: complete \(v=33\) and \(v=99\) infinite families

A new [nine-torsion spectral lifting lemma](research/nine_torsion_lift_v33_v99_2026-10-18.md)
shows that when \(v_0\) is coprime to 30 and its phase
period \(\ell_0=\operatorname{lcm}(v_0,\operatorname{ord}_{v_0}(10))\)
is prime to 3, multiplying \(v_0\) by 3 or 9 does **not**
increase the dimension of the stable spectral cocycle.
The new smooth-index parameter becomes
\(n=r/\gcd(r,\ell_0)\), with phase
\(\gamma'=(su)^{-1}\bmod v_0\), \(s\in\{3,9\}\),
\(u=2^a5^c\). A period of \(T\) digit layers is thus
folded into just \(\ell_0\) cosets.

For \(v_0=11\), \(\ell_0=22\). This yields **two new
computer-assisted infinite order-family theorems**:
\[
\boxed{\operatorname{ord}_p(10)=33\cdot2^a5^c
\text{ or }99\cdot2^a5^c
\Longrightarrow \exists k:p\mid M(k),\ a,c\ge0.}
\]
The 20 pre-existing exact \(v=11\) linear resultant norms
apply **unchanged**. The new phase-aware sieve independently
checks all 3,850 admissible indices for \(v=33\) and 3,757
for \(v=99\), and finds
\(\gcd(N_{g,\gamma},\Phi_r(10))=1\) in every case.
No new algebraic norms, large-order cutoff, or enumeration of target
primes is needed.

- [Lifting theorem and full proof](research/nine_torsion_lift_v33_v99_2026-10-18.md)
- [Exact norm-reuse and 7,607-index exclusion](research/certify_fixed_v33_v99.py)
- [15 independent prime-field recurrence checks](research/audit_fixed_v33_v99.py)
- [Updated unified manuscript](research/fixed_v_spectral_families.tex)
  and [compiled PDF](research/fixed_v_spectral_families.pdf)

The dedicated \`.github/workflows/a077187-v33-v99.yml\`
reproduces the original 20 exact norms and the new exclusions.
Together the certified fixed-coprime-order families are now
\(v\in\{7,11,33,99\}\), with no restriction on \(a,c\).
The unrestricted A077187 conjecture for arbitrary \(v\) is **OPEN**.


### Sharp 3-adic limit of the 22-phase argument

An additional exact group-theoretic lemma proves that for
\(r=\operatorname{ord}_p(10)=11\cdot3^b2^a5^c\), \(b\ge1\),
and \(A_d=10^{9d10^{d-1}}\) on stable digit layers,
\[
\operatorname{ord}(A_{d+22\cdot3^t}A_d^{-1})
=3^{\max(b-2-t,0)}
\]
for every \(t\ge0\). This identifies a **precise obstruction**
to extending the current 22-phase norm reuse beyond \(b=2\):
for \(b\ge3\), 22 steps leave a genuine residual \(3^{b-2}\)
phase. See the proof in
[nine-torsion lifting note](research/nine_torsion_lift_v33_v99_2026-10-18.md).
The new families are complete for \(0\le b\le2\);
larger \(b\) remains a mathematical open case, not a counterexample.


## Exact Lucas orbit norm for the zero-drift branch (October 18 continuation)

After reviewing the new \`HANDOFF.md\`, the continuation avoids the
refuted fixed-three-window route and instead treats the **whole stable
period** of digit windows at once.

For any nonsingular digit layer, let the local mountain equation be
\(Q(z)=Az^2+Hz+B\), \(z\in\langle 10^d\rangle\), and
\(h=\operatorname{ord}_p(10^d)\). A new general theorem proves
\[
\operatorname{Res}(z^h-1,Q(z))
=A^h+B^h-\operatorname{tr}
 \begin{pmatrix}-H&-AB\\1&0\end{pmatrix}^{h}.
\]
It holds for all degenerate coefficients and is invariant under
\(A\mapsto A(10^d)^s,\ B\mapsto B(10^d)^{-s}\).
It is a genuine cyclic-orbit norm evaluable by
\(O(\log h)\) matrix powering, requiring **no discrete logarithm,
square root, or subgroup enumeration**.
For singular \(10^d=1\) layers the corresponding complete-field
product is \(2K(1-(-K)^{(p-1)/2})\).

Using the updated reduced stable period
\(T=\operatorname{lcm}(r,\operatorname{ord}_{v/\gcd(v,9)}(10))\),
define \(\mathfrak O_p\) as the product of the \(T\) local norms
for digit lengths \(T+1,\ldots,2T\). If the two-coordinate stable
drift is **zero**, then
\[
\mathfrak O_p=0
\iff
\text{some (hence infinitely many) stable digit windows
contain a divisible mountain.}
\]
This is an exact **per-prime criterion**, not a universal
vanishing theorem. The still-open sufficient implication
\(\Delta_p=0\implies\mathfrak O_p=0\) needs a new algebraic
relation between actual window states. It is *not* a repeat
of the disproved three-window conjecture.

- [Mathematical derivation, Lucas transfer matrix, whole-period criterion](research/lucas_orbit_norm_zero_drift_2026-10-18.md)
- [Independent 49-window audit](research/audit_lucas_orbit_norm.py)
- Dedicated CI: \`.github/workflows/a077187-lucas-orbit-norm.yml\` (passed)

This complements the proven infinite subfamilies and preserves the
unrestricted all-primes problem as OPEN.


## New general witness-density theorem and Fermat–Lucas double norm

[Complete algebraic proof, October 18 continuation](research/quantitative_witness_phases_and_scalar_gcd_2026-10-18.md).

Let \(r=\operatorname{ord}_p(10)\),
\(T\) the **reduced** stable period,
and \((U,V)\) the stable translation. Put
\(\sigma=U+V\).

- **PROVED:** If \(\sigma\ne0\), **exactly \((p+1)/2\)**
  of the \(p\) block-number phases \(j\bmod p\) have a
  divisible mountain in their \(jT\)-digit *singular*
  layer. The square law is
  \(M(k)/10^{D(k-1)}
  =k^2+C_T+Y_T+(j-1)\sigma\). This gives infinitely
  many different witnesses in every successful phase class.
- **PROVED:** If \(\sigma=0\) but \((U,V)\ne0\),
  the first post-boundary window has exactly
  \(r-\varepsilon_r\) offsets with nonzero affine phase
  slope, where \(\varepsilon_r=0\) if \(r\) is even and
  \(1\) if odd. Since each phase can have at most two
  such offsets, at least
  \(\lceil(r-\varepsilon_r)/2\rceil\) **distinct**
  block phases yield divisible mountains.
- **PROVED (Fermat–Lucas double norm):** For the post-boundary
  polynomial \(Q_j(z)=(A+10jU)z^2+Hz+(B+jV)\),
  \(H=-20/81\), \(z^r=1\), and \(r\ge3\),
  \[
    \prod_{j\in\mathbb F_p}
    \operatorname{Res}_z(z^r-1,Q_j(z))
    =
    \operatorname{Res}_z(z^r-1,Q_0(z))\,
    (1-U^{p-1})(1-V^{p-1}).
  \]
  The right-hand idempotent equals 1 **only** at exact
  zero drift. This explains algebraically why nonzero drift
  supplies many block-phase witnesses, while the
  zero-drift problem remains a separate open condition.

**EXPERIMENTAL / CONJECTURAL, not a theorem:** exact repunit
ring tests at \(2\le r\le300\), with seven further spot
tests, found
\(\gcd(10^r-1,U_r+V_r)=\gcd(10^r-1,U_r,V_r)\).
This is explicitly *not* assumed in any proof.
[Standalone GMP falsification probe](research/probe_scalar_gcd.cpp)
can search for counterexamples.

Independent scripts:
[audit witness phase density](research/audit_quantitative_witness_density.py)
and [audit double norm](research/audit_fermat_lucas_double_norm.py).
A dedicated small CI workflow runs both plus bounded scalar probes.

**Remaining open:** whether all true zero-drift primes have a
stable-window root. No unrestricted all-primes proof is claimed.


## Exact Möbius phase-incidence theorem (October 18 continuation)

A new [projective phase-involution proof](research/mobius_phase_involution_2026-10-18.md)
goes beyond the former two-offset or half-phase lower bounds.
For a nonsingular stable window the local condition has
\[
Q_j(z)=(A+j\alpha)z^2+Hz+(B+j\beta)=0,\quad
z\in\mu_r,\quad \alpha=10U,\ \beta=V.
\]
When drift is nonzero, eligible offsets \(z\) determine unique
successful phases \(j=-[Az^2+Hz+B]/[\alpha z^2+\beta]\).
All collisions between **distinct** eligible offsets are controlled
by a single projective involution:
\[
\iota(z)=-\frac{Dz+H\beta}{D-H\alpha z},
\qquad D=A\beta-B\alpha.
\]
Its matrix squares to \((D^2+H^2\alpha\beta)I\).
If this scalar vanishes and no offset is an all-phase root,
the phase map is injective. Otherwise the exact number of
successful phases is
\[
N=(r-n_0)-(e-f)/2,
\]
where \(n_0,e,f\) are degrees of explicitly given
**finite-field polynomial GCDs**, not results of enumerating
cycles or subgroup elements. A common zero of the numerator
and slope on \(\mu_r\) makes **all \(p\) phases** successful.
Consequently nonzero drift gives
\(N\ge\lceil(r-\gcd(2,r))/2\rceil\), often strictly more.

The [independent standard-library audit](research/audit_mobius_phase_involution.py)
compares polynomial-GCD counts with direct finite-field
phase enumeration for **360 synthetic situations and 12
genuine decimal-concatenation state vectors**.
Dedicated \`.github/workflows/a077187-mobius-phase.yml\` CI **PASSED**.

**Boundary:** at true zero drift, the phase map is constant or
undefined; the projective theorem alone does not imply any
stable-window root. The unrestricted A077187 conjecture stays OPEN.


## Fixed-degree singular-window reduction for any smooth part \(u\)

A new *general algebraic theorem* uses the exact finite-defect
transfer \(W=S_{pT}\), without assuming zero drift. For
\(r=\operatorname{ord}_p(10)=uv\), \(u=2^a5^c\),
the entire singular \(pT\)-digit window obeys
\[
\frac{M(k)}{10^{D(k-1)}}=k^2+W_C+W_Y\pmod p.
\]
Its existence criterion is one square test on an element of the
fixed cyclotomic field \(\mathbb Q(\zeta_u)\), of degree
\(\varphi(u)\), with at most \(\varphi(u)\) choices for the
phase \(v^{-1}\bmod u\). This degree is **independent of
unbounded coprime part \(v\)**. This is a sufficient
window criterion, not a universal theorem forcing a square.

## Zero-drift continuation: fixed quartic trace at smooth order part \(u=8\)

[Exact algebraic note](research/u8_singular_norm_structure_2026-10-18.md)
derives the finite-defect state \(W=S_{pT}\) **without assuming
that the stable drift vanishes**, for every prime with
\(\operatorname{ord}_p(10)=8v\), \((v,10)=1\).
With \(\rho\) a primitive eighth root determined by the
early stable multiplier defect, one obtains
\[
W_C+W_Y=-11/81+a\rho^{-1}+b\rho,
\]
where \(a,b\in\mathbb Q\) are explicitly fixed constants,
independent of unbounded \(v\). The full singular digit window
at \(d=pT\) has the particularly simple mountain equation
\(k^2+W_C+W_Y=0\). Thus this window succeeds exactly when
\(-W_C-W_Y\) is a square modulo \(p\).

The field norm of \(E=-11/81+a\zeta_8^{-1}+b\zeta_8\) is
\[
(a^2-b^2)^2+(2ab-121/6561)^2.
\]
It is **not** a rational square: its reduction modulo 23
is the quadratic nonresidue 7. Hence
\(E\notin\mathbb Q^\times(\mathbb Q(\zeta_8)^\times)^2\).
The \(u=8\) singular-window squareclass is genuinely
cyclotomic, unlike the earlier \(u\mid20\) elementary
perfect-square witness.

[Independent algebraic and seven-prime audit](research/audit_u8_singular_trace_norm.py)
verifies the exact quartic-state calculation and
shows both successful and unsuccessful singular-window
examples (notably \(p=313,7841\) fail this window).
The dedicated \`a077187-u8-trace-norm.yml\` CI passes.
This is a fixed-degree structural obstruction, **not**
a proof of the universal zero-drift existence implication.


## Exact layerwise finite-defect flux and u=8 Galois phase mixing (Oct 18)

[New general mathematical note](research/finite_defect_duhamel_flux_and_u8_galois_2026-10-18.md).

**PROVED, for arbitrary multiplicative orders:** write
\(r=uv\), \(u=2^a5^c\), \(h=\max(a,c)\), and
let \(\rho_i=\widehat A_i/A_i\) be the first \(h\)
actual/stable multiplier ratios. With
\(P_{i-1}=\prod_{j<i}\widehat A_j\),
\(c_i=L_i/(q_i-1)+1/(q_i-1)^2\),
\(b_i=-L_i/(q_i-1)+q_i/(q_i-1)^2\),
and the original prefix state \((C_{i-1},Y_{i-1})\),
the finite-defect state \(W=S_{pT}\) satisfies
\[
\begin{aligned}
W_C&=\sum_{i\le h}P_{i-1}^{-1}(\rho_i^{-1}-1)(C_{i-1}+c_i),\\
W_Y&=\sum_{i\le h}P_{i-1}(\rho_i-1)(Y_{i-1}+b_i).
\end{aligned}
\]
Consequently its scalar trace is an exact sum
of **local defect fluxes**
\[
W_C+W_Y=\sum_i(\rho_i-1)
\left[P_{i-1}(Y_{i-1}+b_i)
-\rho_i^{-1}P_{i-1}^{-1}(C_{i-1}+c_i)\right].
\]
This replaces long affine inverse composition by
a transparent weighted finite sum and recovers
the known \(u\mid20\) one-defect theorem.

For \(u=8\), the explicit state from the preceding
note satisfies the new **fixed hyperbola identity**
\((W_C+10/81)(W_Y+1/81)=ab\).
The first nonsingular window therefore has rational
discriminant \((20/81)^2-40ab\), independent of
the primitive eighth-root phase. In contrast,
the singular-window square character depends on
\(E(\rho)=-11/81+a\rho^{-1}+b\rho\).

**PROVED (Galois phase obstruction):** the rational norm
\(N=\operatorname{Norm}_{\mathbb Q(\zeta_8)/\mathbb Q}(E)\)
is nonsquare modulo the **split** prime \(41\)
(\(N\bmod41=26\)). Thus
\(\mathbb Q(\zeta_8,\sqrt N)/\mathbb Q\)
is multiquadratic of degree eight. By Chebotarev,
a set of rational primes of density \(1/8\) has
\(\chi_p(N)=-1\) and \(p\equiv1\bmod8\).
For each such prime, among the **four formal eighth-root
conjugates**, at least one singular-window square test
succeeds and at least one fails. This is **not**
a density statement about the specific phase selected
by the decimal cocycle and gives **no counterexample
to A077187**.

[Independent standard-library audit](research/audit_defect_duhamel_flux.py):
16 true-order prime fields, direct affine-prefix inversion,
global-period consistency for shorter periods,
and four split-prime Galois phase tests;
dedicated \`.github/workflows/a077187-duhamel-flux.yml\`
**CI PASS**. The remaining obstacle is a *specific
cross-constraint* between finite defect and true zero
stable drift. The unrestricted conjecture stays OPEN.


## Latest structural results: terminal-cutoff orbit conjugacy and single-window density obstructions

Two new proved notes continue the **zero-drift / finite-defect
structure** without increasing any order cutoff:

**[Universal stable-cutoff orbit gauge](research/terminal_defect_universal_orbit_gauge_2026-10-18.md).**
For \(r=2^a5^cv\), put \(h=\max(1,a,c)\).
The *entire* late digit-length-\((pT+h)\) window has a
divisible mountain exactly when the **original**
\(h\)-digit window's fixed rational quadratic has a
root in the *full* subgroup \(\langle10^h\rangle\):
\[
10^h(C_{h-1}+c_h)y^2-
\frac{2\cdot10^h}{(10^h-1)^2}y
+(Y_{h-1}+b_h)=0.
\]
The subgroup-preserving gauge uses the actual/stable
\(h\)-th layer multiplier ratio; the coefficients depend
only on the finite original decimal prefix and on \(h\),
**not** on the unbounded coprime factor \(v\).
The threshold \(h\) may exceed the last truly different
layer (for \(u=4\), only layer 1 differs but \(h=2\)).

For \(h=2\) the exact rational discriminant is
\[
-\frac{669867392724508459}{15125000}.
\]
It is a nonsquare modulo the fully split prime
\(41\equiv1\bmod40\), with value \(12\).
A Chebotarev argument therefore proves **exact
natural density \(1/32\)** of primes
\(p\equiv29\bmod40\) with smooth order part \(u=4\)
for which the **\((pT+2)\) window fails**,
although the old \(u\mid20\) proof guarantees
another divisible mountain.

**[Phase-free u=8 first-window obstruction](research/u8_single_window_density_one_thirtysecond_2026-10-18.md).**
The first full post-defect \(q=10\) equation is
\(10ay^2-(20/81)y+b=0\) on \(\langle10\rangle\),
after an exact multiplicative-subgroup gauge.
Its rational discriminant has value \(24\), a
nonsquare, at the completely split prime
\(401\equiv1\bmod80\). Hence an **exact
natural-density \(1/32\)** set of actual primes
\(p\equiv57\) or \(73\bmod80\), with smooth order
part \(u=8\), defeats this entire window.

These are **single-window** density results,
consistent with the previously certified stronger
\`zero_drift_continuation_2026-10-18.md\`
theorem that a density-\(1/128\) set defeats
**three** fixed early windows at once.
None concerns the actual \(\Delta=0\) branch
strongly enough to establish a mountain
counterexample, and the unrestricted conjecture
is still OPEN.

Small independent standard-library CI audits:
[audit terminal gauge and genuine u4 primes](research/audit_terminal_defect_gauge_u4.py)
and [audit u8 phase-free quadratic](research/audit_u8_positive_density_window_failure.py).
Both dedicated GitHub Actions jobs passed.
