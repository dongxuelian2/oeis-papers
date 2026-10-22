# A077187 research handoff

Updated 2026-10-18. The user resumed the research and explicitly requested
**no further subagents**. Work proceeds in the existing PR #8. The unrestricted
all-primes existence problem is **NOT SOLVED**.

## Version and audit provenance

- Checkout: `E:/oeis/a077187`.
- Branch: `research/a077187-smooth-order-v3-le8-20261017`.
- PR: <https://github.com/dongxuelian2/oeis-papers/pull/8>.
- Original paused checkpoint: `5e5265c` (full prior handoff retained in Git).
- First updated PR merged at `bff7e96`; next update inspected and integrated
  through `dea3a4d`, whose source parent is `19af679`.
- Local pre-integration checkpoint: `1cfefd2`.
- The spectral audit was completed before the no-subagent instruction;
  all later integration, tail derivation and checks were done by the primary
  agent alone. No new agent was started or assigned work after that instruction.

## Closed results and proof boundaries

PROVED means a written algebraic proof; COMPUTATION_CERTIFIED means a
finite exact computation with a sufficient coverage bound. CONDITIONAL
and EXPERIMENTAL statements are not promoted to theorems.

1. **PROVED: arbitrary-order stable affine dynamics.** A valid period is
   `T=lcm(r,ord_v(10))` for `r=u*v`, `u=2^a*5^c`, `(v,10)=1`. Nonzero
   drift implies a witness at `10^(jT)` or `10^(jT)+1`, `1<=j<=p`.
   Small exceptions 3 and 11 are handled directly.
2. **PROVED: reduced spectral phase.** Put `delta=gcd(v,9)`, `t=v/delta`,
   `ell=lcm(t,ord_t(10))`, `g=gcd(r,ell)`, `m=r/g`. A stable block of
   length `m*ell` compresses into `ell` cosets in `Q(zeta_g)`. Stable
   multipliers generate exactly `mu_t`; the cumulative phase has period
   `ell`. This generalizes the updated PR's nine-torsion lift.
3. **PROVED: all u dividing 20, with arbitrary v.** Only the first layer
   differs from its stable continuation. After p blocks the drift cancels
   and the first-window equation is a square with a root in `<10>`.
   The explicit witness is `k=10^(pT)+n`,
   `n=(9*10^T-10) mod r`. This is now integrated in the spectral paper.
4. **PROVED: all v dividing 9.** Elementary invariant `U+V=9/100`.
5. **PROVED / COMPUTATION_CERTIFIED: all v dividing 99.** For
   `r=11*3^b*2^a*5^c`, `b<=2`, odd a=0 has an explicit nonzero invariant
   `11*z*U-9*V=909*(z+1)/100`. Even a>=1 reduces to ten fixed quadratic
   norms and 11385 exhaustive index checks, all raw gcds 1. The earlier
   remote certificate is retained as an independent computation; its
   counts 3850 and 3757 include the odd branches, explaining the difference.
6. **PROVED: exact higher-b boundary.** The updated PR proves
   `ord(A_(d+22*3^t)/A_d)=3^max(b-2-t,0)`. Thus for b>=3 the existing
   22-phase mechanism cannot be reused unchanged. This is not an OEIS
   counterexample.
7. **PROVED: tail-gauge reduction.** After cancelling the current layer
   multiplier, only later defect phases remain. The first window depends
   on phase order `u/gcd(u,20)`; a general d-th window has the exact
   tail order given in `zero_drift_continuation_2026-10-18.md`.
8. **COMPUTATION_CERTIFIED obstruction to three fixed windows.** For u=8,
   all three models are rational. Exact squareclass independence plus
   Chebotarev supplies a set of primes of density 1/128 for which their
   discriminants are all nonsquares. At p=617 this is checked directly.
   This concerns the first three windows after p blocks; it does not
   refute a statement conditional on actual zero drift or the all-primes
   conjecture. The written proof states all these restrictions.

## Integration and checks

The current paper is `fixed_v_spectral_families.tex` and its PDF. It includes
reduced phases, explicit Fourier sums, odd/even proof separation, the u|20
witness, the existing v=7 theorem, and the new sharp 3-adic boundary.
README now leads with the audited current scope instead of an unsupported
cumulative lower-stage claim. `main.tex` remains the historical stage-8 paper.

Completed local checks:

- `certify_involutive_families.py`: all 20 explicit coordinate identities,
  ten quadratic norms, complete counts `[3887,3796,3702]`, every gcd 1.
- `audit_reduced_spectral.py`: 20 selected independent phase/coset/full-layer
  identities; these are consistency checks, not an infinity proof.
- Updated PR `certify_fixed_v33_v99.py`: all 3850+3757 indices, every gcd 1.
- Updated PR `audit_fixed_v33_v99.py`: 15 full-layer comparisons and
  252 exact 3-adic defect checks.
- `zero_drift_tail_gauge_2026_10_18.py --examples --symbolic`: seven specified
  prime comparisons in all three windows, the p=617 obstruction, and all
  56 rational squareclass tests.
- The existing v=7/v=11 norm scripts and independent field audits passed
  the separate spectral audit; no large stage-8 rerun was needed.
- Updated manuscript compiled twice with pdflatex and its rendered pages
  were visually inspected. No unresolved references or overfull boxes.

The updated PR source commit `19af679` has successful nine-torsion and PDF
jobs (runs 39101285574 and 39101285587). Its PDF bot head `dea3a4d` has
`action_required` PR runs, which are not mathematical test failures.
A new reduced-phases CI workflow reproduces the new scripts. Later CI
status must be checked on the actual pushed revision.

## Remaining mathematical task

No proof yet establishes nonzero drift for arbitrary v, nor subgroup-root
existence conditional on actual zero drift when u does not divide 20.
The first-window phase reduction does not force a root, and using three
fixed windows is now provably insufficient without additional structure.
A successful continuation must use a relation imposed by actual zero drift,
a uniform phase-cancellation mechanism, or a different witness construction.
Do not default to b=9, larger prime scans, or additional numerical cutoffs.

The original stage-8 arithmetic audit is in `audit_certificates.md`.
The b<=7 certificate package is still absent; the local coefficient bridge
in `general_dynamics.md` repairs the derivation but not those missing data.
The historical cumulative claim is therefore not a closed proof supplied
by this checkout. Earlier counterexamples and failed routes remain recorded
in `zero_drift.md` and the new tail note.

Reproduction uses Python 3 with SymPy; the tail checks use only the standard
library. See README for exact commands. A final all-primes theorem has not
been claimed, and the goal must not be marked complete.


## October 18 continuation after the user's update: whole-period orbit norms

**PROVED:** The local \(d\)-digit window equation
\(Az^2+Hz+B=0,\ z^h=1,\ h=\operatorname{ord}_p(10^d)\)
has the exact cyclic-group norm
\[
\operatorname{Res}_z(z^h-1,Az^2+Hz+B)
=A^h+B^h-\operatorname{tr}
 \left(\begin{smallmatrix}-H&-AB\\1&0\end{smallmatrix}\right)^h.
\]
This holds with degenerate coefficients and is invariant under the
subgroup gauge \(A\mapsto A(10^d)^s,\ B\mapsto B(10^d)^{-s}\).
It is computable in \(O(\log h)\) via matrix powering. The \(q=1\)
singular-window norm is \(2K(1-(-K)^{(p-1)/2})\).

**PROVED:** With the improved reduced period
\(T=\operatorname{lcm}(r,\operatorname{ord}_{v/\gcd(v,9)}(10))\),
if the true stable drift \(\Delta_p=S_{2T}-S_T\) is zero,
all states repeat every \(T\) layers. Multiply the complete
orbit norms for the \(T\) windows \(T+1,\ldots,2T\);
call the resulting scalar \(\mathfrak O_p\).
Then \(\mathfrak O_p=0\) if and only if some stable digit window
contains a divisible mountain; any such witness recurs infinitely
often. Since these windows are longer than \(p\), all subgroup
offsets are attained. Early windows \(1\le d\le T\) are a
separate finite check.

**AUDITED:** a standalone standard-library script reproduces
49 exact finite-field windows, independently comparing the
transfer-matrix norm with direct within-window roots and checking
singular windows and gauge invariance. Dedicated GitHub Actions
job passed.

**OPEN, not inferred from the identities:** Prove
\(\Delta_p=0\implies\mathfrak O_p=0\), or prove that
\(\Delta_p\ne0\) universally for all \(p\ge7,\ p\ne11\).
The orbit-norm target uses the **whole** stable period and is not
contradicted by the audited three-fixed-window failure.
A generic affine periodic cocycle need not force that implication;
the special arithmetic of decimal block forcing must enter.

Files:
- \`lucas_orbit_norm_zero_drift_2026-10-18.md\`
- \`audit_lucas_orbit_norm.py\`
- \`.github/workflows/a077187-lucas-orbit-norm.yml\`

No new subagents were launched. The unrestricted problem remains OPEN.


## Further October 18 results: quantitative phases and double norms

**PROVED (singular half-phase theorem).**
Write \(\Delta=(U,V)\) for the reduced stable drift and
\(\sigma=U+V\). For every prime \(p\ge7,\ p\ne11\)
with \(\sigma\ne0\), **exactly \((p+1)/2\)** classes of
\(j\bmod p\) have a divisible mountain inside the entire
\(jT\)-digit singular layer; in fact exactly \(p\) pairs
\((j,k\bmod p)\) solve its square relation.
This follows from
\(k^2+C_{jT}+Y_{jT}
=k^2+C_T+Y_T+(j-1)\sigma\).

**PROVED (anti-diagonal alternative).**
If \(\sigma=0\) but \(\Delta\ne0\), then the
\(r=\operatorname{ord}_p(10)\) offsets
\(k=10^{jT}+n\) have exactly \(r-\varepsilon_r\)
nonzero slopes in \(j\), where
\(\varepsilon_r=[r\text{ odd}]\). Every phase carries
at most two roots of the associated nonsingular quadratic,
so at least \(\lceil(r-\varepsilon_r)/2\rceil\)
distinct phase classes yield witnesses.

**PROVED (Fermat–Lucas double norm).**
In the first stable post-boundary window, define
\(Q_j(z)=(A+10jU)z^2+Hz+B+jV\), \(H=-20/81\).
For \(r\ge3\), with
\(\mathcal R(j)=\operatorname{Res}(z^r-1,Q_j(z))\),
\[
\prod_{j\in\mathbb F_p}\mathcal R(j)
= \mathcal R(0)(1-U^{p-1})(1-V^{p-1}).
\]
This follows from
\(\prod_j(a+jb)=a(1-b^{p-1})\) and the
fact that a nonzero polynomial \(10Uz^2+V\) cannot
vanish on all \(r\ge3\) roots. It is an exact
algebraic packaging of the nonzero drift case;
**when drift is zero it supplies no new vanishing**.

**CONJECTURAL empirical observation:** exact repunit-ring
experiments for all \(2\le r\le300\), plus seven other
orders, found
\[
\gcd(10^r-1,U_r+V_r)=\gcd(10^r-1,U_r,V_r).
\]
A general proof or counterexample remains to be found.
Do not cite it as an established lemma or infer
nonzero drift for unrestricted orders.

Files:
- \`quantitative_witness_phases_and_scalar_gcd_2026-10-18.md\`
- \`audit_quantitative_witness_density.py\`
- \`audit_fermat_lucas_double_norm.py\`
- \`probe_scalar_gcd.cpp\`
- \`.github/workflows/a077187-phase-density.yml\`

The dedicated checks passed on the original version and the
expanded double-norm version is undergoing CI at this update.
No subagents were used. The global all-primes A077187 conjecture
is still OPEN.

**Priority for further research:** establish a relation
specific to the *actual zero-drift decimal concatenation
cocycle* that forces one whole-period Lucas orbit norm to
vanish. Neither the scalar GCD pattern nor a nonzero-drift
phase-count estimate is such a relation.


## October 18: exact projective collision geometry for stable witnesses

**PROVED:** On the first nonsingular window after a stable block,
the local mountain polynomial has the form
\[
Q_j(z)=a(z)+jb(z),\quad
a=Az^2+Hz+B,\quad b=10Uz^2+V,\quad
H=-20/81,\quad z\in\mu_r.
\]
A root with \(b(z)\ne0\) determines the unique successful
period phase \(j=-a(z)/b(z)\). A common subgroup root of
\(a\) and \(b\) instead succeeds for **every** \(j\bmod p\).

**PROVED:** Put \(\alpha=10U,\ \beta=V,\ D=A\beta-B\alpha\)
and \(\Lambda=D^2+H^2\alpha\beta\). If \(\Delta\ne0\)
and no universal root exists, all collisions of
distinct eligible offsets are governed by
\[
\iota(z)=-(Dz+H\beta)/(D-H\alpha z).
\]
Its projective matrix \(M\) satisfies \(M^2=\Lambda I\).
If \(\Lambda=0\), the rational phase function reduces
to an injective fractional-linear map.
If \(\Lambda\ne0\), the number of distinct successful
period phases has the exact expression
\[
N=(r-n_0)-(e-f)/2,
\]
where \(n_0=\deg\gcd(X^r-1,b)\),
\(e=\deg\gcd(P,F)-\deg\gcd(P,F,b)\),
\(f=\deg\gcd(P,J)-\deg\gcd(P,J,b)\),
\[
F=(-DX-H\beta)^r-(D-H\alpha X)^r,\quad
J=-H\alpha X^2+2DX+H\beta.
\]
This yields \(\lceil(r-n_0)/2\rceil\le N\le r-n_0\).
All degenerate cases are handled separately.

**AUDITED:** standard-library program tests 360 synthetic
finite-field configurations and 12 genuine original
decimal-layer drift vectors against independent
direct phase enumeration; dedicated GitHub Actions CI PASS.

Files:
- \`mobius_phase_involution_2026-10-18.md\`
- \`audit_mobius_phase_involution.py\`
- \`.github/workflows/a077187-mobius-phase.yml\`

**Scope:** This is a sharpened *nonzero-drift witness-structure*
theorem, not a proof for the \(\Delta=0\) branch. At zero drift,
the phase function loses its nonconstant parameter, and neither
its Möbius involution nor the Fermat–Lucas additive norm
forces a mountain. The unrestricted conjecture remains OPEN.
Do not resume large finite-prime or multiplicative-order scans
as a substitute for the missing arithmetic zero-drift relation.


## October 18: structural u=8 singular-window obstruction (latest)

**PROVED:** For every prime with
\(r=\operatorname{ord}_p(10)=8v,\ (v,10)=1\), let
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\) and
\(\rho=10^{9(10^T-1)}\), a primitive eighth root mod \(p\).
The exact finite-defect state \(W=S_{pT}\), *regardless
of whether the drift vanishes*, satisfies
\[
W_C=-10/81+a\rho^{-1},\qquad W_Y=-1/81+b\rho,
\]
where the fixed rational constants are
\[
a=10/81-219804400/(120758121\cdot10^{189}),\quad
b=1/81+217557800\cdot10^{189}/120758121.
\]
The mountain equation for the **singular window of digit length
\(pT\)** is exactly \(k^2+W_C+W_Y=0\).
Thus its success is equivalent to one quadratic-residue test
in the fixed quartic field \(\mathbb Q(\zeta_8)\), independent
of the size and factors of \(v\).

**PROVED:** For \(E=-11/81+a\zeta_8^{-1}+b\zeta_8\),
\[
\operatorname{Norm}_{\mathbb Q(\zeta_8)/\mathbb Q}(E)
=(a^2-b^2)^2+(2ab-121/6561)^2.
\]
Modulo 23 the coefficients \(a,b,c=-11/81\)
are \(10,22,1\), so this norm reduces to the quadratic
nonresidue 7. Hence \(E\) is **not** a rational multiple
of a square in \(\mathbb Q(\zeta_8)\).
This is an algebraic barrier to extending the \(u\mid20\)
perfect-square proof to \(u=8\) by a constant rescaling.

**AUDITED:** a standalone exact Fraction-polynomial program
computes the three-layer defect in \(\mathbb Q[X]/(X^4+1)\),
then independently checks seven original modular recurrences
for true smooth order part 8. Both singular-window outcomes
occur: \(p=313,7841\) have nonsquare \(-W_C-W_Y\);
\(p=73,137,233,617,2393\) give squares.
Dedicated \`a077187-u8-trace-norm.yml\` CI PASS.

**OPEN:** the u=8 singular test is not a universal
mountain existence theorem; the failing primes still have
other divisible mountains via nonzero drift. No proof here
settles the case of a *genuine zero-drift* prime whose
singular character is negative. The unrestricted A077187
conjecture remains OPEN. Next research should seek a
relation tying the stable monodromy to this fixed
cyclotomic character, or a different full-cycle root
mechanism, not expand fixed finite-prime cutoffs.

Files: \`u8_singular_norm_structure_2026-10-18.md\`,
\`audit_u8_singular_trace_norm.py\`,
\`.github/workflows/a077187-u8-trace-norm.yml\`.


## Oct 18 latest: all-order defect Duhamel flux and rigorous phase obstruction

**PROVED:** Exact layerwise Duhamel formula for the
finite-defect state \(W=S_{pT}\), for **any**
\(r=\operatorname{ord}_p(10)=uv\), \(u=2^a5^c\),
\((v,10)=1\). With \(h=\max(a,c)\), the original
prefix states \((C_{i-1},Y_{i-1})\), and
\(\rho_i=\widehat A_i/A_i\),
\(P_{i-1}=\prod_{j<i}\widehat A_j\),
\[
W_C=\sum_{i=1}^hP_{i-1}^{-1}
(\rho_i^{-1}-1)(C_{i-1}+c_i),\quad
W_Y=\sum_{i=1}^hP_{i-1}
(\rho_i-1)(Y_{i-1}+b_i).
\]
The sum \(W_C+W_Y\) factors termwise as
\((\rho_i-1)(Z_i-\rho_i^{-1}X_i)\), with
\(X_i=(C_{i-1}+c_i)/P_{i-1}\) and
\(Z_i=P_{i-1}(Y_{i-1}+b_i)\).
This gives a **local-impulse flux representation**
without reversing the full affine prefix. It is
distinct from, and does **not** restrict by itself,
the stable translation \(\Delta\).

**PROVED for \(u=8\):**
the already established \(W_C,W_Y\) formulas
yield \((W_C+10/81)(W_Y+1/81)=ab\),
so all primitive-eighth-root defect states lie on
a fixed hyperbola and the first-window discriminant
\((20/81)^2-40ab\) is independent of the phase.

**PROVED GALOIS LIMITATION:** the singular-window
trace \(E(\rho)=W_C+W_Y\) has rational norm \(N\)
with \(N\bmod41=26\), a quadratic nonresidue at
a prime splitting in \(\mathbb Q(\zeta_8)\).
Therefore \(K(\sqrt N)/\mathbb Q\) has Galois group
\((\mathbb Z/2)^3\); a rational-prime set of
Chebotarev density \(1/8\) has p≡1 mod8 and
\(\chi_p(N)=-1\).
Among **four formal conjugate phases** at such p,
both square and nonsquare characters occur.
The *actual* phase selected by \(r=8v\)
may have either value. There is **no**
actual-prime counterexample or density theorem
for real failures of A077187.

**AUDITED and CI PASS:** 16 true-order prime
fields via independent Duhamel, stable-prefix
inversion and (for short T) original two-period
recursion; conjugate-phase signs at p=41,73,97,137.
Files \`finite_defect_duhamel_flux_and_u8_galois_2026-10-18.md\`,
\`audit_defect_duhamel_flux.py\`,
\`.github/workflows/a077187-duhamel-flux.yml\`.

**OPEN:** bridge the arithmetic condition
\(\Delta=0\) to a forced root in one stable window;
a direct rational-square rescue at the \(pT\)-digit
singular window is ruled out as a universal
phase-independent argument. Do not confuse
formal phase density with true order-specified
decimal phases. A077187 remains OPEN.


## October 18 latest: universal cutoff-window conjugacy, two rigorous single-window no-go densities

**PROVED (all smooth parts).** Let
\(r=\operatorname{ord}_p(10)=uv,\ u=2^a5^c\),
\(h=\max(1,a,c)<r\) and the full stable period \(T\).
The state just before the \((pT+h)\)-digit interval is
\(\widehat F_h^{-1}F_h(S_{h-1})\).
Writing \(A_h,\widehat A_h\) for its actual and
stable layer multipliers, the ratio
\(\rho_h=\widehat A_h/A_h\) belongs to
\(\langle10^h\rangle\).
The shifted window's quadratic, after
\(z=\rho_h y\), is exactly the **original**
\(h\)-digit early-prefix polynomial
\[
10^h(C_{h-1}+c_h)y^2-
{2\cdot10^h\over(10^h-1)^2}y+
(Y_{h-1}+b_h)=0,\qquad y\in\langle10^h\rangle.
\]
This is an *unbounded-order* window equivalence;
no assertion that this window has a root is made.
The stability cutoff \(h\) need not be the last
genuinely discrepant layer.

**PROVED (u=4: density 1/32 of necessary window switching).**
For \(h=2\), the exact fixed rational quadratic
has discriminant
\(\mathcal D_2=-669867392724508459/15125000\).
At the split prime \(41\equiv1\bmod40\) the
value is 12, a nonresidue. Thus a Chebotarev
class of exact natural density \(1/32\)
(\(p\equiv29\bmod40,\ (\mathcal D_2/p)=-1\))
has smooth order part \(u=4\) and **cannot**
have a mountain in its \((pT+2)\) window.
The earlier \(u\mid20\) proof supplies another
window witness for every such p, demonstrating
necessary window switching within a solved family.

**PROVED (u=8: density 1/32 of first post-defect failure).**
The \(q=10\) window right after \(pT\) has the
phase-free subgroup polynomial
\(10ay^2-(20/81)y+b\), with fixed rational
discriminant \(\mathcal D=(20/81)^2-40ab\).
At split prime \(401\equiv1\bmod80\),
\((a,b,\mathcal D)=(146,228,24)\) and
\((24/401)=-1\). This makes \(\sqrt{\mathcal D}\)
independent of \(\mathbb Q(\zeta_{80})\), yielding
an **exact density \(1/32\)** of actual
\(p\equiv57\) or \(73\bmod80\) with smooth
order part \(u=8\) and no root anywhere
in that specified \(q=10\) digit interval.
This is the single-window projection of the
older, more demanding *three-window* density
\(1/128\) obstruction; neither addresses an
actual all-mountain counterexample.

**AUDITED, CI PASS:**
- \`terminal_defect_universal_orbit_gauge_2026-10-18.md\`
- \`audit_terminal_defect_gauge_u4.py\`, CI \`a077187-terminal-defect-gauge.yml\`
  (9 genuine u4 prime-field comparisons; split 41 certificate).
- \`u8_single_window_density_one_thirtysecond_2026-10-18.md\`
- \`audit_u8_positive_density_window_failure.py\`, CI \`a077187-u8-window-density.yml\`
  (8 genuine u8 cases; split 401 certificate).

**NEXT, still OPEN:** exploit a specific **cross-constraint**
from true \(\Delta_p=0\) to force a root in
a different stable window, or prove universal
nonzero drift. The above *failure of fixed
windows* demonstrates why a single-window
argument alone cannot settle A077187.
