# All 57 residual cases as algebraic determinant families

**Scope and verification status.** This eliminates the need for **57
separate endpoint-multiset identities** as a *construction format*:
all 57 are instances of one symbolic integer-matrix formula.
The remaining finite information consists of **57 cubic-root words
and 57 output-block orders**, plus the exact positivity condition
for the resulting integer lengths. These are **not** eliminated
case distinctions and should not be advertised as a case-free
existence theorem.

The full compact parameter file is
[certificates/finite_57_cubic_order_shapes.txt](certificates/finite_57_cubic_order_shapes.txt).
It contains **no breakpoints** and no previously calculated image
intervals. Each shape also defines infinitely many further cube-sum
permutations by a universal dilation formula below.

## 1. Universal block-rearrangement matrix

Take any permutation `pi=(pi_1,...,pi_t)` of `1,...,t`.
Let `pos(i)` be the position of block `i` within `pi`.
Define the explicit integer matrix

```
M(pi)[j,i] = [i<j] + [pos(i)<pos(j)] + [i=j],
```

with `[statement]` equal to 1 if true and 0 otherwise.
Let `k_1,...,k_t` be positive integers and set

```
b(k) = (k_1^3-1, ..., k_t^3-1)^T.
```

If `det M(pi)=1`, define the *algebraic block lengths*

```
ell_j(k) = det M_j(pi,k),                          (1)
```

where `M_j(pi,k)` is obtained by **replacing column j** of
`M(pi)` with `b(k)`. By Cramer's rule, these are integers and

```
M(pi) ell(k) = b(k).                              (2)
```

Whenever `ell_j(k)>0` for all `j`, define
`N(k)=sum ell_j(k)`. Divide `[1,N(k)]` into input blocks
of lengths `ell_1(k),...,ell_t(k)`, and divide its output
copy into blocks of the same lengths arranged in order `pi`.

**Universal algebraic theorem.** On input block `j`, define
`p(i)=k_j^3-i`. Then `p` is a permutation of `[1,N(k)]`
and every `i+p(i)` is a cube, for every integer root vector
satisfying `ell_j(k)>0`.

**Proof.** Let `A_j=sum_(i<j) ell_i` and
`B_j=sum_(pos(i)<pos(j)) ell_i`. Equation (2) is precisely
`A_j+B_j+ell_j=k_j^3-1`. Therefore

```
k_j^3 = 1 + A_j + B_j + ell_j.
```

Reflection of the input interval
`[A_j+1,A_j+ell_j]` sends it bijectively onto
`[B_j+1,B_j+ell_j]`. By definition of `pi`, these
output intervals partition `[1,N(k)]`. Hence the
construction is bijective, with the requested cube sums.
There is *no* appeal to an endpoint-multiset cancellation
test for the individual instances. QED.

The determinant formula is a polynomial, not a numerical
inversion prescription: for fixed `pi`, every `ell_j` is
an **integer-linear expression in `k_1^3,...,k_t^3,1`**.

## 2. Why every nonsingular block-order matrix is unimodular

**Unimodularity theorem.** For *every* output order `pi`,
the matrix `M(pi)` above satisfies

```
det M(pi) in {0,1}.
```

In particular, any nonsingular such matrix has determinant +1,
so formula (1) uses integral coefficients.

**Proof.** Let `u=(1,...,1)^T`. Observe that

```
M = u*u^T + K,
K[j,i] = -K[i,j],
```

where, for `i<j`, `K[i,j]=-1` if
`pos(i)<pos(j)`, and `0` otherwise.
Thus `K` is the oriented crossing matrix of the following
chord diagram: put the first ends of chords in order
`1,...,t` around one arc of a circle, and their second
ends in order `pi_1,...,pi_t` around the complementary
arc. Two oriented chords cross precisely when their
labels have the same relative order in both lists.

We use a standard elementary topological fact about such
integer crossing matrices: **every even-order chord-diagram
crossing matrix has Pfaffian `0`, `1`, or `-1`.**
Indeed, thicken the oriented chord diagram to a compact,
connected, oriented ribbon surface with boundary. Its core
loops give an integral basis of first homology, and `K`
is their intersection pairing. In a suitable integral
homology basis, this pairing is a direct sum of integral
unimodular symplectic blocks
`[[0,1],[-1,0]]` and zero blocks (the boundary radical).
The determinant of the integral basis change is `+1`
or `-1`; hence the full Pfaffian is either `0` or
`+/-1`.

If `t` is even, `adj(K)` is skew-symmetric. Therefore,
by the rank-one determinant formula,

```
det M = det K + u^T adj(K) u
      = det K = Pf(K)^2 in {0,1}.
```

If `t` is odd, `det K=0`. Form the skew matrix

```
H = [[0, u^T], [-u, K]].
```

It is itself a signed chord-crossing matrix: add one new
chord with its ends between the first and second batches
and after the second batch, so it crosses all earlier
chords with identical sign. Expanding its bordered
determinant gives

```
det M = u^T adj(K) u = det H = Pf(H)^2 in {0,1}.
```

This proves the assertion. The theorem is general; it is
**not** merely the observation that 57 numerical
determinants happen to equal 1. QED.

## 3. Every one of the 57 cases is now a determinant formula

The file `finite_57_cubic_order_shapes.txt` records exactly

```
target n | cube roots k_1,...,k_t | output order pi_1,...,pi_t
```

for **all 57 previously exceptional lengths**.

For each, the integer matrix of Section 1 is nonsingular
and hence automatically unimodular by Section 2. The
determinant formula yields strictly positive lengths,
and their sum agrees with the indicated `n`. Across the
57 shapes, the minimum block length is **1**, the largest
number of blocks in a shape is **43**, and the total number
of generated input blocks is **795**.

The separate [57-row positivity digest](certificates/finite_57_determinant_positivity_summary.txt)
records the exact minimum and maximum reconstructed block lengths,
together with the minimum/maximum coordinates of `M^{-1}u`,
for each shape. There are **28 even-block and 29 odd-block** shapes;
thus their cubic dilations have exactly the two parity-dependent
length formulas proved below. The digest is a redundant audit,
not an additional endpoint certificate.

Thus **all 57 residual finite witnesses have an algebraic
*definition* through one general theorem**. None needs its
own endpoint-cancellation identity. The set of 57 choices
of `pi` and `k` and the verification of positivity are
still explicitly finite; it would be misleading to say
the discrete classification is solved without casework.

A worked small instance is `n=82`:

```
k  = (4,2,3,4,5,4,5)
pi = (6,2,3,4,7,1,5)
det M(pi) = 1
ell(k) = (2,3,16,21,19,2,19)
N(k) = 82
```

For any choice of positive cube roots `k'_j` making the
seven determinant polynomials positive, the *same* output
order gives a valid permutation at the automatically
determined length `N(k')`.

## 4. Every algebraic shape gives an explicit infinite family

Let `ell=ell(k)` be any positive block length vector
with `det M=1`. Put

```
v=M^{-1}u.
```

The same skew-Pfaffian argument (using one deleted chord
in an augmented diagram) gives, for every coordinate,

```
v_j in {-1,0,1}.
```

More explicitly, the relevant Cramer minors are up to
sign Pfaffians of chord diagrams with one marked chord,
divided by a nonzero Pfaffian of absolute value 1.
Also, `sum(v_j)=epsilon`, where
`epsilon=0` for even `t` and `epsilon=1` for odd
`t`. To see this, multiply `Mv=u` by `v^T`:
`(sum v_j)^2=sum v_j`. For even `t`, `K` is
invertible and so `sum v_j=0`; for odd `t`,
invertibility of `M` forces `sum v_j=1`.

For any positive integer `h`, replace **every** cube root
`k_j` by `h*k_j`. The new lengths are *exactly*

```
ell_j(h) = ell_j + (h^3-1)*(ell_j+v_j).           (3)
```

Indeed,
`M*ell(h)=h^3*(k^3-u)+ (h^3-1)*u
          = (h*k)^3-u`.
Since `ell_j>=1` and `v_j>=-1`, the coefficient
`ell_j+v_j` is nonnegative and every length
in (3) remains positive for all `h>=1`.

The resulting lengths obey the uniform scaling law

```
N(h) = (N+epsilon)*h^3 - epsilon.
```

That is,

```
t even: N(h) = N*h^3,
t odd:  N(h) = (N+1)*h^3 - 1.
```

This construction is **symbolic for all positive h**.
It proves that the former 57 exceptional witnesses are
not isolated numerical accidents: each belongs to an
explicit infinite cubic-parameter construction, derived
without recomputing a matching or an endpoint atlas.

## 5. How the existence proof uses this new certificate

The *entire* 57-row endpoint atlas can be replaced by the
57-line cubic-order shape file, the universal determinant
construction, and the positivity statements above.
The six previously established block template families
provide 25 further seed lengths. Together there are still
82 independent positive seed lengths: 22 below 173 and 60
from 173 through 364. The strictly growing cubic suffix
rule establishes the additional 26 lower and 132 middle
lengths, covering every n in [173,364]. The symbolic
cubic-gap induction proves the tail for n>=365.

The standalone exact
[verify_unimodular_factory.py](verify_unimodular_factory.py)
reads only the 57 cubic-order shapes (not the old
endpoint atlas), recovers all integer block lengths
via **fraction-free integer elimination**, checks their
positivity and the predicted n, and audits the cubic
dilation identities at h=2 and h=3 as a redundancy check.
For the other 25 seed lengths it calls the already
separate six algebraic family generators, and rechecks
the finite reflection closure. The general matrix
identities and dilation for **arbitrary h** are proved
symbolically above, not inferred from finitely many tests.

**Logical boundary:** This achieves a genuine universal
*algebraic parameterization of all 57 remaining rows*,
not a case-free proof of existence for every middle n.
There remain 57 specified output orders and 57 root
words, and proving those parameter vectors lie in the
positive determinant domain is a finite arithmetic
obligation. Removing those 57 choices altogether is
a separate, harder question.
