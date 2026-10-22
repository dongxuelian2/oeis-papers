# A077187 continuation: finite-defect transfer across arbitrary multiplicative orders

**2026-10-17 · status: PROVED intermediate lemmas, NOT an all-primes solution.**

This note continues the user-supplied `HANDOFF.md`, which reports a previously established `u | 20` subfamily. The main new contribution here is an explicit **finite-defect conjugation** computing the state after `pT` digit layers for every prime `p >= 7`, without iterating through `pT` layers. It is a constructive new reduction, not a proof that the unrestricted sequence is positive.

## 1. States and exact full-layer maps

Let `C_k` concatenate `1,2,...,k`, let `R_k` concatenate `k,k-1,...,1`, let `D(k)` be the total number of digits in `1,...,k`, and put `Y_k = 10^{-D(k)} R_k (mod p)` (for `p \nmid 10`). For a new `d`-digit integer `j`,

```
C_j = 10^d C_{j-1} + j,
Y_j = 10^{-d}(Y_{j-1} + j)  (mod p).
```

For the full `d`-digit layer let `L=10^{d-1}`, `B=10^d-1`, `N=9L`, `q=10^d`, and `A=q^N`. Put `S=sum_{h=0}^{N-1}q^h` and `J=sum_{h=0}^{N-1}h q^h` in `F_p`. With `s_d=(C_{10^d-1},Y_{10^d-1})`:

```
s_d = F_d(s_{d-1}),
F_d(C,Y) = (A*C+B*S-J,  A^{-1}*(Y+L*S+J)).
```

All coefficients can be computed in logarithmic time with geometric-sum formulas; `q=1` is handled separately.

## 2. Eventual periodic translation

Write `r=ord_p(10)=u*v` with `u=2^a 5^c`, `gcd(v,10)=1`. Define

```
E = 1+max(a,c),
T = lcm(r, ord_v(10)),  ord_1(10)=1.
```

For all `d>=E`, `u | 9*d*10^(d-1)`. Moreover, both `q` and the map exponent modulo `v` repeat after `T`; hence `F_{d+T}=F_d` for `d>=E`.

**Monodromy translation lemma.** The product of the diagonal multipliers across any full `T`-layer stable block is 1. Indeed, it is `10^H`, with

`H=9*sum_{d=e}^{e+T-1}d 10^(d-1)`.

The smooth part `u` divides each summand. For `v`, let `G_T=(10^T-1)/9`. Because `T` is a multiple of `v` and `10^T=1 (mod v)`, `v|G_T`: for any prime factor other than 3 this follows by inverting 9, and for 3 it follows from `v_3(G_T)=v_3(T)` (LTE). The identity

```
9*sum_{d=e}^{e+T-1}d*10^(d-1)
 = (e+T-1)*10^(e+T-1) - e*10^(e-1)
   - sum_{j=e}^{e+T-2}10^j
```

then shows `v|H`, because modulo `v` its right side is `(T-1)*10^(e-1)+10^(e-1)=T*10^(e-1)=0`. Thus `r|H`. Every `T`-layer stable composite is a translation in the two-dimensional state, repeated every `T` layers. `p` repetitions are the identity in characteristic `p`:

`(C_{pT+E-1},Y_{pT+E-1})=(C_{E-1},Y_{E-1})`.

## 3. New finite-defect transfer theorem

Define `Fhat_d=F_{T+d}` for `1<=d<E`. These are **stable continuations** of the finitely many initial exceptional digit layers. The exact end state at the enormous exponent `pT` is

```
STATE(pT) = Fhat_1^{-1} o Fhat_2^{-1} o ... o Fhat_(E-1)^{-1}
            o F_(E-1) o ... o F_2 o F_1 (0,0).
```

This follows by first reaching the initial state after `E-1` layers, applying `p` complete stable periods, and reversing the last `E-1` stable layers. Since `F_{pT+d}=F_{T+d}` in the stable range, the right side requires only `O(E)` affine-map operations after `r,T` are known. In particular, **the number of transient layers, not the enormous exponent `pT`, controls the state calculation**.

This statement holds for *any* prime `p>=7`, including orders with prime factors other than 2,3,5.

## 4. A universal quadratic first-window criterion

Write `(C,Y)=STATE(pT)` and `X=81C+10`, `Z=81Y+1` modulo `p`. Since `10^(pT)=1 (mod p)`, for `k=10^(pT)+j`, `0<=j<r`, and `z=10^j`, direct solution of the two within-window recurrences gives

```
M(k)/10^D(k-1) = [10*X*z^2-20*z+Z]/(81*z)  (mod p).
```

Thus **if** the quadratic `10X z^2-20z+Z` has a root in the cyclic subgroup `<10>`, an exact witness is obtained without iterating any digit layer. This is a sufficient criterion, **not** asserted to hold for every prime. Its discriminant is `40*(10-XZ)`. In particular, if `XZ=10` and `X^-1 in <10>`, the root `z=X^-1` is a double root.

## 5. Self-contained review of the earlier u|20 theorem

If `u|20`, every digit layer `d>=2` belongs to the stable regime. Take `E=2`. For the actual first layer, `A=10^9`. For its stable continuation, `Ahat=10^[9(1+T)10^T]` modulo `p`. Both have `q=10,L=1`, and therefore

```
F_A(C,Y)=(A*C+(10*A-91)/81,
          A^-1*Y+(80*A+1)/(81*A)).
```

Set `rho=Ahat/A`, which is a nonzero power of 10 modulo `p`. The transfer theorem gives

```
C=10*(rho^-1-1)/81,   Y=(rho-1)/81,
X=10/rho,             Z=rho.
```

Consequently the window polynomial is the perfect square

```
M(10^(pT)+j)/10^D = (10*10^j-rho)^2/(81*rho*10^j).
```

Taking `j=(9*10^T-10) mod r` in `[0,r-1]` gives `10^j=rho/10`, hence `p|M(10^(pT)+j)`. This is a complete elementary proof for `p>=7` with `u|20`; `p=3` has direct witness `M(3)=12321`. The primes 2 and 5 cannot divide any `M(k)`.

## 6. New exact witnesses beyond the proven subfamilies

The **first prime not covered** by either the reported `u|20` theorem or the reported smooth `v|9` theorem is `p=113`, because `ord_113(10)=112=16*7`. The new transfer formula gives `T=336`, `E=5`, `(C,Y)=(86,0)`, `(X,Z)=(83,1)`. The quadratic vanishes for `z=10^32` and `z=10^55`. Therefore

`113 | M(10^37968+32)`.

Independent direct digit-layer iteration through all 37,968 layers confirms this exact congruence, though OEIS already lists a much smaller least witness `k=156`.

Similarly, `p=233`, `r=232=8*29`, `T=1624`, `E=4`, `(X,Z)=(119,174)`, and `z=10^33` is a root, so

`233 | M(10^378392+33)`.

Again, independent direct iteration through all 378,392 digit layers confirms the congruence. This is NOT a new unconditional infinite family; they are individual examples.

**Important negative control:** for `p=313` the same `pT`-window quadratic has no root in `<10>`. This does not imply no witness for 313; it proves that the particular first-window criterion alone does not solve A077187.

## 7. Remaining gap

The all-primes theorem remains open. Combining the handoff's two proven classes shows that any still-uncovered prime must have BOTH `u∤20` and `v∤9`. This is a necessary condition for escaping existing *proofs*, not a necessary condition for having no divisible mountain.

The finite-defect state and window quadratic provide a new reduction with small complexity, but the crucial missing universal step is either to show nonzero stable drift, or to show that some window (not necessarily the first at `pT`) contains a subgroup root when the drift vanishes. More b-layer finite norm computations are not a substitute for that step.

## 8. Reproduction

From this directory, with Python and SymPy:

```
python defect_transfer.py
python independent_digit_layers.py
python verify.py
```

The tests deliberately use two methods: (i) fast inverse affine-map transfer, (ii) direct forward simulation through the actual digit layers to exponent `pT` and within the target window. The first method does not call the second method internally.