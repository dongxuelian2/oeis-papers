# Cube-sum permutations: global principles independent of the 173 cutoff

**Research note — 2026-10-18.** Companion to [main.tex](main.tex) and
[PR #13](https://github.com/dongxuelian2/oeis-papers/pull/13).

For every n >= 1, let P(n) count permutations p of [n] such that
i + p(i) is an integer cube for every i. Set P(0)=1 as a convention.
Write C={8,27,64,125,...}.

The following results put the all-length existence question inside
a wider combinatorial and algebraic theory. Some underlying results
(Hall, permutation cycle covers, determinant/permanent modulo 2)
are classical; the special cube-sum consequences and the displayed
four-interval affine construction are the objects documented here.
Nothing in Sections 1–4 assumes a computer-aided verification of the
sharp threshold 173.

## 0. Eventual existence from one seven-element seed

This is an alternative proof of eventual existence that deliberately **does not aim for the sharp 173 cutoff**.

The only initial witness is the reversal `p=(7,6,5,4,3,2,1)` with `i+p(i)=8`. Under a cube-reflection step, any valid length `m` gives a valid length

```
n=k**3-m-1, provided m<n.
```

Let `R_0={7}`, and for `j=0,...,6` define

```
R_(j+1)= R_j union {k**3-m-1 :
                        m in R_j, k>=2,
                        m<k**3-m-1<=10975}.
```

Seven finite rounds suffice; their cardinalities are exactly

```
j       0    1    2    3     4     5     6     7
|R_j|   1   21  189  995  3280  6588  8533  8924
```

and `R_7` contains the **entire integer interval [8915,10975]**. An independent checker represents each reachable set as a union of integer intervals. The number of disjoint intervals after each round is `1,21,186,870,2077,2037,1031,770`; at stage 7 its last interval is exactly `[8915,10975]`. Both witnesses are executable bounded-integer arithmetic, not matching searches.

**Infinite induction.** For every `n>=10976`, let `k` be the smallest integer with `k**3>=n+8916`, and put `m=k**3-n-1`. Then `k>=28` and `m>=8915`. If `k=28`, `k**3<=2*n` because `n>=10976`. If `k>=29`, minimality gives

```
2*n-k**3 >= k**3-6*k*k+6*k-17832 >= 1685 > 0.
```

Therefore `8915<=m<n`, and strong induction supplies a valid permutation at `m`, extended to `n` by reflection. Thus

```
P(n)>0 for every n>=8915.
```

Moreover `m=O(n**(2/3))` under the chosen least-cube rule, so direct construction uses `O(log log n)` reflection layers and `O(n)` output operations.

This theorem is **not claimed to be fully computation-free**: it uses a finite seven-round integer check. Its advantage is that the finite premise concerns one simple seed and an elementary reflection-closure calculation, with no 173..364 permutation certificates or bipartite matching routines.

Two independent checkers:
- `python papers/A006063/one_seed_eventual.py` (pointwise integer reflection closure, actual constructed permutations)
- `python papers/A006063/one_seed_interval_proof.py` (symbolic union-of-intervals arithmetic)

### Exact reflection-history counting and uniform entropy

Let `F(n)` count the **different permutations** produced by strict
reflection histories starting from the one length-7 seed. These histories
are injectively encoded by their final permutations, because the last
value of the final permutation equals `m+1`, uniquely identifying
the previous length `m`.

The resulting exact recurrence is

```
F(7)=1,
F(n)=sum(F(m) for 7<=m<n with m+n+1 an integer cube),  n>7.
```

`F(n)<=P(n)` always, and the seven-round theorem proves
`F(n)>=1` for every `n>=8915`. Using `s` distinct largest cubes
and the same polynomial gap estimate, let `rho_s` be determined by
`sum(rho_s**(-h) for h=1..s)=1`, and take
`B_s=max(2*s*s+4*s-1,2*s+27)`. Then

```
F(n) >= rho_s**((floor(cuberoot(2*n))-B_s)/2)
                                            for n>=8915.
liminf log(F(n))/(2*n)**(1/3) >= log(2)/2.
```

This is a **uniform exponential-cube-root lower bound for the tiny
single-seed reflection-generated subfamily alone**, not merely for the
full set of legal permutations. Its derivation uses the seven-round
integer certificate and algebraic inequalities but none of the
A006063 sharp-threshold matching data.

Reproduce finite exact counts with:
`python papers/A006063/reflection_tree_counts.py`.

### Connection to restricted signed Waring representations

Represent lengths by the odd coordinate `x=2*n+1`. Every
reflection step `m -> n=k**3-m-1>m` becomes

```
x_next = 2*k**3 - x,
x_next > x.
```

Therefore an `r`-step reflection path from an arbitrary starting length
`a` is equivalent to an alternating signed sum of `r` cubes:

```
2*n+1 = (-1)**r * (2*a+1)
        + 2*sum((-1)**(r-j) * k_j**3 for j=1..r)
```

**with the essential extra constraint** that every intermediate odd
coordinate strictly increases. For `a=7` and exactly seven steps,

```
n+8 = k_7**3-k_6**3+k_5**3-k_4**3
      +k_3**3-k_2**3+k_1**3.
```

This opens an additive-number-theoretic route independent of matching
theory: proving that all sufficiently large integers have a seven-cube
alternating representation satisfying the intermediate inequalities
would yield a *uniform seven-step construction*. Finite interval
experiments suggest this may hold, but it is **not proved**;
the certified all-`n>=8915` construction currently uses
`O(log log n)` reflection layers.

### Reflection entropy has exactly cube-root order

Fix one seed `p`, and consider paths of strictly increasing reflection lengths `n_0<n_1<...<n_r=n`. Every step uses the cube `c_j=n_(j-1)+n_j+1`, and

```
c_(j+1)-c_j = n_(j+1)-n_(j-1) > 0.
```

Thus **the cubes in each path are strictly increasing**, and the ordered root set (subset of roots 2..floor(cuberoot(2n))) uniquely determines the path and the permutation. The single-seed reflection count obeys

```
F(n) <= 2**(floor(cuberoot(2*n))-1).
log F(n) = Theta(n**(1/3))  as n->infinity.
```

For a fixed collection of S starting permutations, the corresponding upper bound is `S*2**(K(n)-1)`. Pure reflection from finitely many seeds consequently has **zero entropy per permutation position**, in sharp contrast with the exponential-in-n families produced by disjoint three-cycles.

**Bounded-depth barrier.** At most r reflections give at most `sum(comb(K(N)-1,j) for j=0..r)` different lengths <=N. For fixed r<=2 this is `o(N)`; for r=3 it is `N/3+O(N**(2/3))`. A fixed-seed uniformly cofinite reflection construction therefore needs **at least four steps**. Whether the observed seven-round upper bound extends unconditionally to all large n is an open signed-Waring-type question.

Reproduction: `python papers/A006063/reflection_entropy_barrier.py`.

### Arithmetic codegrees and stronger Hall obstruction localization

Two distinct left vertices `i,j` can share a right neighbor only when two cubes differ by `|i-j|`. As `a**3-b**3=(a-b)*(a*a+a*b+b*b)`, the common-neighbor count is **at most tau(|i-j|)**. Define `D=max(tau(d),1<=d<n)` and let `delta`, `Delta` be the extreme vertex degrees. Cauchy-Schwarz on the neighbor multiplicities gives the exact global inequality

```
|N(S)| >= |S|*delta**2/(Delta+(|S|-1)*D).
```

For all `n`, the degrees obey `delta>=(2**(1/3)-1)*n**(1/3)-1` and `Delta<=floor(cuberoot(2*n))`, while `D=O_epsilon(n**epsilon)` for every fixed positive `epsilon`. Thus every Hall-deficient subset (independent or not) must have **size at least `c_epsilon*n**(2/3-epsilon)`** once n is sufficiently large. Coupled with boundary localization, an obstruction must be both arithmetically large and nearly full diameter; this still does **not** rule all of them out.

Reproduction: `python papers/A006063/arithmetic_expansion_audit.py`.

### A global involution tail with a designated fixed point

The single-seed reflection theorem proves more than eventual existence
of arbitrary cube-sum permutations. The seed at length 7 is
`p(i)=8-i`, a legal involution with `p(4)=4`.
Every reflection extension acts by a second involution on a *disjoint
new interval*. Thus its direct sum with the old permutation remains
an involution, and position 4 never changes.

Let `I_4(n)` count cube-sum involutions on [n] that fix 4. Then

```
I_4(n) >= F(n) > 0                      (every n>=8915)
liminf(log(I_4(n))/(2*n)**(1/3)) >= log(2)/2.
```

So the one-seed reflection tree gives many legal involutions at
**every sufficiently large length**, without using the sharp
existence threshold or any matching searches. This also proves the
undirected cube-sum graph has a spanning loop/dimer cover for all
n>=8915. The result contrasts with the independently certified
exception n=236, where P(236)=512 but not one valid involution exists.

The proof requires *no additional computational premise*: it is the
involution invariant of the previously verified reflection closure.
Audit: `python papers/A006063/involution_tail_audit.py`.

### Fibonacci upper bound: sharper than root-set counting

Let `K=floor(cuberoot(2*n))` and `F(n)` be the seven-seed strict-reflection count. A cubic identity shows that for **every predecessor** arising from cube `(K-j)**3`,

```
2*m <= (K-2*j)**3 - 6*j*j*(K-j) - 2 < (K-2*j)**3,
K(m) <= K-2*j-1.
```

Thus the possible predecessor root-height drops are at least
`1,3,5,7,...`. Define `B_2=B_3=B_4=1` and
`B_k=B_(k-1)+B_(k-2)` for `k>=5`. A strong induction using the
exact tree recurrence gives the uniform **Fibonacci majorant**

```
F(n) <= Fib_(K(n)-2)       whenever K(n)>=3,
F(n) <= 1                 when K(n)=2.
```

Consequently the known coefficients for the *single-seed* growth obey

```
(log(2))/2 <= liminf(log(F(n))/(2*n)**(1/3))
             <= limsup(log(F(n))/(2*n)**(1/3))
             <= log(phi),  phi=(1+sqrt(5))/2.
```

Unlike the earlier coarse upper estimate `2**(K(n)-1)`,
the Fibonacci bound accounts for how much cube-root height each
reflection consumes. This is a genuinely tighter global bound, and
the exact limiting coefficient remains an open problem.
The refreshed `reflection_entropy_barrier.py` verifies the
Fibonacci majorant and the strict predecessor height inequalities
at every length up to 12,000.

## Taxicab switching: exponentially many *involutions* without finite certificates

A new purely algebraic global principle produces **exponentially many legal involutions**, not merely arbitrary cube-sum permutations. For any fixed exponent `d>=2`, take four *perfect d-th powers* `A,B,C,D` with

```
A+B=C+D
(3*A)/2 <= C < B/2.
```

For every integer u>=1 put `T=u**d`, `N=(B-A)*T` and start from the two-block involution

```
p(i)=A*T-i   on [1,A*T-1]
p(i)=B*T-i   on [A*T,(B-A)*T].
```

For each `s=1,...,H=floor((A*T-1)/2)`, take four vertices

```
a=s,       b=A*T-s,
c=C*T-s,   d=(B-C)*T+s.
```

The vertex quadruples are disjoint. Their baseline dimers `(a,b)` and
`(c,d)` have perfect-power sums `A*T,B*T`, whereas the alternative
dimers `(a,c)` and `(b,d)` have perfect-power sums `C*T,D*T`.
Each switch preserves the involution property and changes exactly four
permutation entries. Switching arbitrary subsets gives

```
I_d((B-A)*u**d) >= 2**floor((A*u**d-1)/2),
limsup log(I_d(n))/n >= A*log(2)/(2*(B-A)) > 0.
```

The encoding multiplies all binary Hamming distances by exactly **4**.
A particularly small cubic example is the taxicab identity

```
17**3 + 39**3 = 26**3 + 36**3.
I_3(54406*u**3) >= 2**floor((4913*u**3-1)/2).
```

The identity `99**3+172**3=120**3+163**3` is another example,
giving the stronger optional coefficient `970299*log(2)/8236298`;
neither is asserted optimal. The general theorem does not depend on
the sharp cutoff or any finite matching certificate.

The independent `taxicab_involution_audit.py` checks both integer
identities and the disjoint dimer-switch inequalities. A separate
local implementation fully materialized and verified both original
and modified 54,406-element involutions, all sums being cubes.

### Inverse-paired tensorization: exact involution fiber count

Independent perfect-power fibers can also be paired to create genuine
**involutions**, even when some base permutations are not involutive.
In the previous tensor map, a position `(i,r)` maps to
`(p_r(i),L+1-r)`, so the lifted map is an involution exactly when

```
p_(L+1-r) = inverse(p_r)                 (r=1,...,L).
```

Since `L=t**d` is odd and the inverse of a legal power-sum permutation
is also legal, its **exact** number of involutive middle-block lifts is

```
I_d(M) * P_d(M)**((L-1)//2).
```

Consequently, **if** legal involutions exist at all sufficiently large
lengths, and some M has `I_d(M)>=1` and `P_d(M)>=2`, then

```
limsup_n log(I_d(n))/n >= log(P_d(M))/(2*M+1) > 0.
```

Complete the shifted middle interval by a legal involutive prefix of
size `A=(L-1)//2` and the shortest admissible perfect-power reflection
on the suffix. This is a general implication from finite ordinary
multiplicity to exponential involution multiplicity, conditional only
on eventual involution existence. The earlier taxicab construction
gives an **unconditional** exponential family without this assumption.

`inverse_fiber_involution_audit.py` independently verifies the
inverse-fiber equation with a legal 316-element reference involution and
a different legal, non-involutive five-cycle-switched permutation.

## Parity-optimal involutions and uniform minimal-fixed-point entropy

The previously proved eventual involution existence theorem can be
strengthened to the **minimum possible number of fixed points**, with no
reference to the sharp threshold 173:

```
odd  n>=70001:  valid cube-sum involution with exactly 1 fixed point (4)
even n>=230000: valid cube-sum involution with exactly 0 fixed points.
```

Two very small seeds suffice: `p(i)=8-i` on `[1,7]` is an involution
fixing only 4; `p(i)=27-i` on `[1,26]` is a fixed-point-free involution.
A reflection through an **odd cube** `c=k**3` preserves parity and
introduces **no new fixed point**, because its reflection center `c/2`
is nonintegral.

**Finite exact step (no matching algorithms).** Use only odd cube roots
in the recurrence `n=k**3-m-1>m`. The length-7 seed reaches all 15,001
odd lengths in `[70001,100001]`, and the length-26 seed reaches all
36,001 even lengths in `[230000,302000]`. The last unreachable
same-parity lengths before those regions are 69,601 and 228,026,
respectively. This is checked by two independent direct integer
implementations, and `parity_minimal_involutions.py` reconstructs
actual permutations and checks the involution equation and exact fixed
point sets.

This finite coverage is also certified **independently by symbolic parity-interval algebra**: `parity_interval_proof.py` encodes each parity length as `t=(n-p)/2` and performs the exact interval reflection `t -> (k**3-1-2*p)//2 - t` through odd cube roots. After **12 simultaneous rounds**, the odd/even reachable sets have 41,057/121,707 lengths in 2,997/7,047 merged intervals, respectively, and each target interval is contained in one merged interval. This avoids checking any full matching or even iterating through all individual reachable lengths during the closure step.

**Infinite step.** For odd n>100001 or even n>302000, let M be the
respective lower endpoint 70001 or 230000 and choose the least **odd**
root k with `k**3>=n+M+1`. Let `m=k**3-n-1`. Then m has the same parity
as n, m>=M, and `m<n`. The last inequality uses

```
2*n-k**3 >= 2*(k-2)**3-k**3-2*M
          = k**3-12*k*k+24*k-16-2*M.
```

The polynomial is increasing for k>=57; in the odd case k>=57 and
its value at 57 is 7555>0. For even n>302000 the minimum k is
at least 83, and its value at 83 is 31095>0. Induction finishes the
construction for every larger same-parity n.

An additional arithmetic strengthening is immediate: for **every even n>=230000**, the fixed-point-free matching can be chosen so that **every edge sum is an odd cube**, thereby pairing odd indices with even indices. For **every odd n>=70001**, exactly the original seven seed positions have the even cube sum 8; every index i>=8 has an odd cube sum. This is an exact global structural constraint, not just an asymptotic density statement.

**Uniform lower bound on the count.** Let `J_min(n)` count legal
involutions with no fixed point when n is even, or with the *sole*
fixed point 4 when n is odd. The proof also establishes

```
liminf_{n->infinity} log(J_min(n))/(2*n)**(1/3) >= log(2)/4.
```

Indeed, count odd-cube-only reflection histories from each parity
seed. For s odd roots `q,q-2,...,q-2(s-1)` and
`K(n)=floor(cuberoot(2*n))`, exact cube-gap inequalities imply
`K(m_j)>=K(n)-4(j+1)` for sufficiently large n. The s-branch
recursion has a geometric growth root `rho_s`, satisfying
`sum(rho_s**(-h) for h in 1..s)=1`, so it gives a lower bound with
exponent `(K(n)-B_s)/4`. Letting s->infinity yields the coefficient
`log(2)/4`.

These stronger global structural results need only finite
**arithmetic reachability**, not the much larger historic
perfect-matching base certificates. They do not assert sharp values of
the new eventual thresholds.

### Linear entropy on both parity-minimal subsequences

In the taxicab two-block involution, the baseline has one fixed point
from a block if and only if that block's cube sum is **even**.
Each disjoint four-vertex dimer switch changes only transpositions,
so it never creates or removes fixed points.

Restricting the cube-scaling parameter `u` to **odd** positive
integers, the two explicit taxicab identities give

```
even n = 54406*u**3:
  J_0(n) >= 2**((4913*u**3-1)//2),   zero fixed points.

odd n = 4118149*u**3:
  J_1(n) >= 2**((970299*u**3-1)//2), exactly one fixed point.
```

Here `J_0` counts fixed-point-free legal involutions at even lengths
and `J_1` counts involutions with exactly one fixed point at odd
lengths. Both are *parity-minimal*, and both admit positive linear
entropy along their explicit infinite subsequences:

```
limsup_even log J_0(n)/n >= 4913*log(2)/108812
limsup_odd  log J_1(n)/n >= 970299*log(2)/8236298.
```

These are **pure algebraic counts**, not matching search results.
They complement the earlier *all-length* parity-minimal theorem,
whose uniform proven growth remains `exp(Omega(n**(1/3)))`.
The statement that `J_min(n)>=exp(c*n)` for *every* sufficiently
large n remains **unproved**.

## 1. Exact graph and independent-set formulations

Let G_n have vertices [n], an undirected edge ij for i != j when
i+j is a cube, and a loop at i if 2i is a cube. Define N(S) as all
vertices adjacent to at least one vertex in S, including loops.

**Perfect-2-matching/cycle cover.** Every valid permutation breaks
uniquely into fixed points (loops), transpositions (dimers) and
oriented cycles of length >= 3. In particular, existence is equivalent
to a spanning configuration of such undirected components. If F is an
unoriented configuration and c(F) counts its length>=3 cycles,

    P(n) = sum_F 2**c(F).

**Independent-set Hall criterion.** The bipartite double cover of G_n
has a perfect matching if and only if every *independent* I in G_n,
with loops also disallowed, satisfies |N(I)| >= |I|.

An elementary proof of sufficiency avoids referring to the general
perfect-2-matching theorem: suppose any S fails Hall's inequality.
Put I=S\N(S). Then I is independent, N(I) is disjoint from S and

    |N(I)| <= |N(S)\S| < |S\N(S)|=|I|.

Consequently *every* failed Hall inequality has an independent
counterpart. All 124 already archived negative witnesses for n<173
satisfy this stronger independence property.

## 2. Global near-perfect matching and boundary localization

These results hold at every length n>=7, regardless of whether
P(n) is zero.

**Near-perfect theorem.** Put k=floor(cuberoot(n+1)).
Choose the closer of k**3 and (k+1)**3 to n+1 and call it c.
Then

    J=[max(1,c-n), min(n,c-1)]

is a contiguous interval of exactly n-|c-(n+1)| positions. Reflection
i -> c-i permutes J and every index-image sum equals c. Since

    |c-(n+1)| <= ((k+1)**3-k**3)//2
              = (3*k*k+3*k+1)//2,

the maximal partial matching covers at least

    n - (3*k*k+3*k+1)//2

positions (the exact number covered by this reflection is
n-|c-(n+1)|). Thus the unmatched proportion is O(n**(-1/3)).
There is no finite base certificate in this argument.

**Boundary-localization theorem.** Put
K=floor(cuberoot(2*n)) and G=(K+1)**3-K**3.
For any S subset [n], if its diameter is at most n-G,
the integer interval

    [max(S)+1, min(S)+n]

contains a cube c. The map i -> c-i is therefore an injection
S -> N(S), proving |N(S)| >= |S|.

Indeed the candidate interval has >=G consecutive integers, and no
G consecutive integers in [2,2n] can be noncubes. Therefore every
Hall-deficient independent set I must satisfy

    max(I)-min(I) > n-G,
    min(I) < G,
    max(I) > n-G+1.

Only independent sets simultaneously reaching the *two boundary
layers of thickness O(n**(2/3))* can possibly obstruct existence.
This is a new precise target for an entirely non-computational
eventual-existence proof; it is not itself that proof.

## 3. Threshold-free affine renormalization

The length-171 involution is specified by four reflection blocks:

    [1,7]    : p(i)=8-i
    [8,19]   : p(i)=27-i
    [20,44]  : p(i)=64-i
    [45,171] : p(i)=216-i

All four sums are cubes and each interval maps bijectively to itself.

**General perfect-power identity.** For any integer d>=2, odd t,
L=t**d and A=(L-1)//2, set T_t(n)=L*n+A. Let P_d(n)
count dth-power-sum permutations. Take one valid prefix permutation
of size A and choose L independent legal permutations p_r of [n].
For each position x=A+(i-1)*L+r, define

    Q(x)=A+(p_r(i)-1)*L+(L+1-r).

Then x+Q(x)=L*(i+p_r(i)), which is a dth power, and all different
choices give different output permutations. Hence

    P_d(T_t(n)) >= P_d(A) * P_d(n)**L.
    2*T_t(n)+1 = L*(2*n+1).
    T_s(T_t(n)) = T_(s*t)(n).

With d=3 and t=7, the explicit prefix size A=171 suffices:

    T(n)=343*n+171,
    P(T(n)) >= P(n)**343,
    T**r(n)=343**r*(n+1/2)-1/2,
    P(T**r(n)) >= P(n)**(343**r).

For any n with P(n)>0, set h(n)=log(P(n))/(n+1/2).
Then h(T(n))>=h(n), and consequently

    limsup_N log(P(N))/N
       >= sup_{n>=1:P(n)>0} log(P(n))/(n+1/2).

This is a multiplicative semigroup action on the odd coordinate
2n+1, with no dependence on a sharp eventual-existence threshold.

## 4. Global parity and factorization

Let H_n be the symmetric n-by-n matrix with entries
H[i,j]=1 if and only if i+j is a cube.

    P(n) = permanent(H_n).
    P(n) mod 2 = determinant(H_n) over GF(2).
               = (number of legal involutions) mod 2.

In particular, if H_n is nonsingular over GF(2), at least one legal
involution exists. All fixed points of a legal permutation occur
at indices i=4*r**3 (because 2i=(2r)**3).

**Factorization from a single valid permutation.**
Given one legal p, form the directed graph with arcs i->j when
i!=j and i+p(j) is a cube. For each strongly connected component C,
let B_C[i,j] record the same allowed relation, *including*
the diagonal i=j. Then

    P(n) = product_{C is an SCC} permanent(B_C).

Any alternative q yields f=p^{-1}o q. The directed cycles of f
must be entirely inside SCCs, so the choices multiply exactly.
This makes multiplicity and uniqueness transparent: P(n)=1 iff
all SCCs are singleton, and a nontrivial SCC supplies a second
solution. At n=236 the nine five-cycle components yield P(236)=2**9.

Independent exact regressions:
- python papers/A006063/renormalization.py
- python papers/A006063/global_graph_audit.py
- python papers/A006063/verify_extended.py

## 5. Distinct global research questions

1. **Complete existence without a finite certificate:** prove that a
   sufficiently large cube-sum graph has no independent Hall-deficient
   set simultaneously spanning both boundary layers. The localization
   theorem reduces the question but does *not* eliminate it.
2. **Uniform exponential counts:** show P(n)>=exp(c*n) for all
   sufficiently large n, rather than only explicit infinite
   subsequences. Such a claim has **not** been proved.
3. **Entropy limit:** decide whether log(P(n))/n converges, diverges,
   or oscillates. The current limsup lower bound and affine entropy
   monotonicity along sparse orbits do not answer this.
4. **Parity/Hankel structure:** characterize when the binary Hankel
   matrix H_n=(1_{i+j is cube}) is nonsingular. This is a distinct
   arithmetic problem about the GF(2) indicator sequence of cubes.
5. **Other perfect powers:** for exponents d>=2, determine the
   existence threshold (if any), nontrivial finite seeds and their
   affine renormalization semigroup.

These questions explicitly separate what is currently a proved
global theorem from what remains a conjectural extension.
