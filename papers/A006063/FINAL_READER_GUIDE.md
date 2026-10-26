# A006063 — final reader's guide and audit (19 October 2026)

> **Primary result:** Every integer `n >= 173` admits a permutation `p` of
> `{1,...,n}` such that each `i+p(i)` is a perfect cube. This is proved
> by explicit **finite arithmetic certificates** and a **symbolic infinite
> induction**. The finite seed choices have **not** been eliminated.
>
> **Secondary result:** The exact small membership of A006063 and the
> eventual membership of A096680 follow from separate finite Hall,
> acyclicity and alternating-cycle certificates.
>
> **Open stronger direction:** The proposed 199-instance, four-cube
> involution theorem for the higher launch interval [467,665] is
> experimentally supported but **has no phase-wide noncomputational
> Hall/matching proof**. It is not a premise of the primary result.

**Start with [A006063_final_proof_map.pdf](A006063_final_proof_map.pdf)**:
a compact, ordered explanation of the proof and a ledger of which
statements are symbolic, finitely certified, or experimental.

## 1. Main theorem: required reading order

| Order | Source | What it actually proves | Dependency |
|---|---|---|---|
| 1 | [COMPRESSED_FINITE_PROOF.md](COMPRESSED_FINITE_PROOF.md) | 82 independent seed sizes, finite reflection closure, and proof dependency map | Finite seed data |
| 2 | [UNIMODULAR_BLOCK_FACTORY.md](UNIMODULAR_BLOCK_FACTORY.md) | Unified block-order matrix and integer Cramer-determinant construction for selected shapes | Shape roots/orders + positivity |
| 3 | [FORCED_REFLECTION_PEELING.md](FORCED_REFLECTION_PEELING.md) | Forced-neighbor proof of P(173)=P(174)=1 and P(175)=3 | Explicit finite peeling checks |
| 4 | [PARAMETRIC_BLOCK_TEMPLATES.md](PARAMETRIC_BLOCK_TEMPLATES.md), [BINARY_BLOCK_FAMILY.md](BINARY_BLOCK_FAMILY.md), [FIFTEEN_BLOCK_FAMILY.md](FIFTEEN_BLOCK_FAMILY.md), [TEN_BLOCK_FAMILY.md](TEN_BLOCK_FAMILY.md) | Six elementary algebraic families generating 25 seed sizes | Parameter inequalities and omitted zero blocks |
| 5 | [INTERVAL_OVERLAP_AVALANCHE.md](INTERVAL_OVERLAP_AVALANCHE.md) | Completely symbolic propagation from [173,364] to every n>=173 | The entire finite interval [173,364] |
| 6 | [verify_56_plus_forcing.py](verify_56_plus_forcing.py) | Independent exact-integer audit of the chosen 56 algebraic shapes, 25 template instances, 173 forced base and 192 interval lengths | Reproducibility only |

### 1.1 Finite ledger (not 57 independent computational cases)

The reduced main proof uses **56 root-word/output-block-order
shapes**, containing **784 generated input blocks**. Their matrix
determinants equal 1; each Cramer solution is a strictly positive
integer vector summing to its target size. The *same* general
formula supplies all these witnesses, but the 56 choices and
positivity checks are finite input data.

A separate forced-neighbor argument supplies **173**. The **six**
symbolic families supply another **25** concrete seed lengths.
Together these are **82** seeds: 22 below 173 and 60 inside [173,364].

Strictly increasing cubic suffix reflection then gives **26**
additional lengths below 173 and **132** lengths inside [173,364],
so every integer in the target interval is covered. In the
infinite tail, the overlap avalanche successively proves the
complete intervals [173,555], [173,826], ... without new cases.

The older 57-shape factory **also** proves the theorem, but is
redundant at 173. Historical atlases of 109, 82, 74, 70, 66,
60 and 57 rows are retained for audit and research history, not
separate assumptions of the reduced proof.

The central constructions are:

```text
M[j,i] = [i<j] + [pos_pi(i)<pos_pi(j)] + [i=j]
d[j]   = k[j]^3-1
M*l    = d
l[j]   = det(M with column j replaced by d), when det(M)=1
p(i)   = k[j]^3-i on input block j
```

```text
G(m), m+n+1=cube, 0<=m<n  => G(n)
G([a,b]), a+b+2<=cube<=2*b+2 => G([a,cube-a-1])
```

The last implication gives the uniform tail and needs no
matching search. **It does not imply the finite base interval**;
for example n=65 has overlapping cube-reflection domains but an
explicit Hall obstruction.

### 1.2 Exact scope of the word "computer-assisted"

* **Not computational in the infinite tail:** The interval
  avalanche is an algebraic induction.
* **Finitely certified, not case-free:** The 56 root/order choices
  and positivity conditions, plus the finite reflection ledger.
  An exact verifier is provided; the certificate is not a
  black-box call to a matching solver.
* **A theorem conditional on fully exposed finite evidence is
  not the same thing as an unconditional formula independent
  of finite data.** All write-ups must preserve this distinction.

## 2. Classification and multiplicity are separate arguments

**A006063 below 173.** There are 48 positive sizes with an explicit
valid permutation, and 124 negative sizes with an explicit
Hall-deficient subset; see
[exact_classification_below_173.json](certificates/exact_classification_below_173.json)
and [verify_extended.py](verify_extended.py).
Therefore `A006063(j)=j+124` for every `j>=49`.
The Hall certificates, not the existence avalanche, establish
that threshold 173 is sharp.

**A096680.** Among the 48 smaller admissible sizes, exactly the
13 sizes `112,115,116,117,119,124,125,126,127,128,129,130,133`
have a certified second solution. The other 35 are certified unique
by absence of directed alternating cycles. The finite second- and
third-solution certificates for 175..364 (and 554/555) combine
with suffix reflection to give `P(n)>=3` for all `n>=175`,
while `P(173)=P(174)=1`. Thus
`A096680(j)=j+161` for `j>=14`.
The finite multiplicity statements remain computer-assisted.

The exceptional count `P(236)=512` and its non-involution
claim have a separate alternating-cycle decomposition in
[main.tex](main.tex), not a logical dependency of the main theorem.

## 3. Additional results and research branches

The extensive [main.tex](main.tex) also develops global graph
structure, renormalization, reflection trees, enumeration/entropy,
parity-minimal involutions, Waring-type constructions, taxicab
switching, exponential subsequence bounds and efficient
construction algorithms. **These are separate results or
conditional research statements, not premises of the short
A006063 existence proof.** They have not all been re-reviewed
line by line in this final consolidation.

The high-start four-cube program belongs in the following
separate order:

1. [FOUR_CUBE_PHASES.md](FOUR_CUBE_PHASES.md): 199 matching
   instances experimentally verified; phase III odd fixed
   point 108 is invalid and has been corrected.
2. [THREE_ROTATION_PLANARITY.md](THREE_ROTATION_PLANARITY.md):
   three explicit endpoint planar rotations and 26 face-word
   templates.
3. [SMALL_BIPARTITE_CORE.md](SMALL_BIPARTITE_CORE.md) and
   [BOUNDED_DEFECT_HALL_REDUCTION.md](BOUNDED_DEFECT_HALL_REDUCTION.md):
   deletion of 14/10/16 disjoint fixed edges reduces the
   problem exactly to bipartite matching plus a bounded
   exceptional-edge choice.
4. [PHASE_I_FOUR_HALL_PATTERNS.md](PHASE_I_FOUR_HALL_PATTERNS.md):
   94 cases reduced to four exceptional-edge selection patterns;
   existence of residual matchings is checked computationally.
5. [ODD_CUBE_PATH_QUOTIENT.md](ODD_CUBE_PATH_QUOTIENT.md),
   [DUAL_REFLECTION_PATHS.md](DUAL_REFLECTION_PATHS.md) and
   [PHASE_III_FORCED_CASCADE.md](PHASE_III_FORCED_CASCADE.md):
   exact modular/path/forced-edge structure, not a phase-wide
   Hall proof.

**Open problem in that branch:** Uniformly prove perfect matchings
for the three four-cube phases without relying on 199 separate
matching computations. Even if solved, it does *not* eliminate
the original 173..466 finite certificate obligations.

## 4. Final corrections and independent audits

A confusing numerical assertion in `main.tex` was corrected:
the minimum number of *new seeds* under the **restricted**
reflection-only rule, given the 48 known small positive sizes
and empty seed, is **60**, not 57. The proof itself counts
44 cases in [173,255] plus 16 in [339,364]; [256,338] requires none.
The different number **57** referred to the *historical*
algebraic shape set (since reduced to 56 plus forced 173).
These are **not interchangeable statements**.

Independent exact checks in the 19 October consolidation:
- 56/56 determinant matrices have determinant 1, all 784
  constructed block lengths are positive integers, and all
  block/cube identities and total sizes match.
- Forced-neighbor peeling leaves zero vertices at 173 and 174,
  and the stated ten-vertex core at 175.
- All 48 positive permutations for 1..172 are valid.
- All 124 negative Hall certificates have a strict deficit
  (between 1 and 6 in the checked table).
- The 13 smaller multiplicity certificates give genuine
  directed alternating cycles; the remaining 35 small
  positive instances are acyclic.
- The strict reflection-only closure needs exactly 60 new
  seeds (44+16); 132 target lengths follow by reflection.
- The 15-block witness at n=236 is bijective. Its alternating
  digraph has exactly nine nontrivial strongly connected components,
  each a chordless directed 5-cycle, and 191 singleton components;
  this independently confirms P(236)=2^9=512 and the exhibited
  non-involution obstruction.

**Important audit boundary:** These checks do not constitute
an independent line-by-line review of all ancillary results,
the full Pfaffian/chord-topology argument, every finite
multiplicity certificate, or literature priority.

**GitHub Actions:** On head `47d3f5a` prior to this final
consolidation, both PR workflows reported `action_required`,
not a successful completed run. Do not state CI or PDF tests
passed on the new commit until new runs have been inspected.

## 5. Recommended publication scope

For OEIS comments or a first review request, use the short
existence theorem, explicit finite-certificate format and
the small-membership classification. Discuss the A096680
multiplicity classification in a separate statement with
its own certificate dependency. Treat the high-start
involution program as open, and do not merge its
experimentally positive matches into the hypotheses of
A006063.

**Status:** Finite-certificate existence proof organized
for review. Not a claimed case-free theorem; independent
peer review and literature comparison remain appropriate.
