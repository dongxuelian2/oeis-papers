# Supplement: whole-block prime obstructions and surviving local powers

This supplement gives proved infinite families of integer nonpowers and exact classifications of a particular local obstruction. **Kashihara's integer perfect-power conjecture remains open.** The final section constructs simultaneous local powers, not integer counterexamples.

Let $W_m=1\Vert2\Vert\cdots\Vert m$, let $d$ be the decimal digit length of $m$, and let $D(m)$ be the total digit length of $W_m$. For a whole-block cut $0\le k<m$,

$$R_{m,k}=10^{D(k)}W_m-(10^{D(m)}-1)W_k.$$

Write $V_j=W_{10^j-1}$ and $\Delta=10^{D(m)}-1$. All endpoint congruences below apply to actual $d$-digit integers. Finite computations are exact integer modular certificates; the periodicity proofs extend them to infinitely many endpoints.

## 1. A general covering criterion

Put $X_k=10^{-D(k)}W_k$ in $\mathbb Z_p$, for a prime $p\nmid10$. Suppose some fixed existing cuts $0\le k\le K$ cover every residue of $\mathbb F_p$ through $X_k$.

**Proposition.** Every rotation has $p$-adic valuation exactly one if and only if

$$p^2\mid\Delta,\qquad p\mid W_m,\qquad p^2\nmid W_m.$$

**Proof.** Normalize the rotation to $Y_k=W_m-\Delta X_k$. Sufficiency is immediate. Conversely, cut zero gives $v_p(W_m)=1$. Cut one, with $X_1=1/10$, forces $p\mid\Delta$. If $v_p(\Delta)=1$, choose an available $X_k\equiv(W_m/p)/(\Delta/p)\pmod p$. Then $p^2\mid Y_k$, a contradiction. This proves necessity.

An integer perfect power with exponent $e\ge2$ has every prime valuation divisible by $e$. Thus valuation one excludes every such exponent at once. The proposition classifies **uniform valuation one**, not all possible local or global nonpowers.

A related identity, valid for $m\ge2$, is

$$\gcd_{0\le k<m}R_{m,k}=\gcd(W_m,\Delta).$$

Indeed cuts zero and one are $W_m$ and $10W_m-\Delta$, and every rotation is an integer combination of $W_m$ and $\Delta$.

## 2. Exact finite-period certificates

To append consecutive integers, use the matrix

$$A_d=\begin{pmatrix}10^d&1&0\\0&1&1\\0&0&1\end{pmatrix}$$

on the state $(W,x,1)$, where $x$ is the next integer. The complete $d$-digit interval applies $A_d^{9\cdot10^{d-1}}$ to $(V_{d-1},10^{d-1},1)$. Call its affine action on $V_{d-1}$ the map $F_d$.

The following exact identities hold modulo $p^2$:

| $p$ | Append period $E$, with $A_d^E=I$ for every phase | Period $r$ of $F_d$ for $d\ge2$ | Composition $F_{r+1}\circ\cdots\circ F_2$ | Sufficient period of $V_d$, $d\ge1$ |
|---|---:|---:|---|---:|
| 7 | 294 | 42 | $V\mapsto V$ | 42 |
| 11 | 242 | 22 | $V\mapsto V+99$ | 242 |
| 13 | 1014 | 78 | $V\mapsto V+104$ | 1014 |
| 31 | 14415 | 465 | $V\mapsto V+868$ | 14415 |
| 41 | 8405 | 205 | $V\mapsto V+861$ | 8405 |

The append identities are checked for every width phase, not inferred from sampled prefixes. The periodicity of $F_d$ follows because its starting endpoint and block count repeat modulo the append period. The factor of $E$ supported on 2 and 5 divides 10 and has stabilized for positive powers; the remaining factor satisfies $10^r\equiv1$. In each nonidentity row the translation is divisible by $p$, so its $p$th iterate is the identity modulo $p^2$. Propagation from $V_1$ proves the displayed boundary periods.

The digit-count identity is

$$D(m)=d(m+1)-\frac{10^d-1}{9}.$$

The required periods for the repunit modulo $\operatorname{ord}_{p^2}(10)$ are verified by reducing $10^r$ modulo the factor of $9\operatorname{ord}_{p^2}(10)$ coprime to 10; its remaining factor is already supplied by $10^d$. These facts reduce the following classifications to complete finite residue tables.

Normalized prefixes cover all residues modulo $p$ at cuts $0,\ldots,K$ with

$$(p,K)=(7,12),(11,103),(13,27),(31,88),(41,133).$$

For the first three classifications, endpoints below the covering thresholds are directly checked and give no exceptions. In the selected 31 and 41 width families, all covering cuts automatically exist.

## 3. Complete classifications at 7, 11 and 13

### Prime 7

Every rotation has valuation one at 7 exactly in one of these three families:

1. $d\equiv1\pmod{42}$, $m\equiv0\pmod{42}$, $m\not\equiv0\pmod{294}$.
2. $d\equiv5\pmod{42}$, $m\equiv12\pmod{42}$, $m\not\equiv264\pmod{294}$.
3. $d\equiv9\pmod{42}$, $m\equiv2\pmod{14}$, $m\not\equiv30\pmod{98}$.

The complete 42-by-294 table has no other nonempty rows. For illustration, in the third row $V_{d-1}\equiv2\pmod{49}$, the starting endpoint is 16 modulo 294, and the recurrence is $W_m\equiv13W_{m-1}+m\pmod{49}$. Its endpoint period is 98. At $m=2+14t$,

$$W_m\equiv7(t+5)\pmod{49},\qquad D(m)\equiv9m-18\pmod{42}.$$

This gives precisely the third family. The verifier exhausts every row using the proved periods; the covering proposition proves completeness.

### Prime 11

Every rotation has valuation one at 11 exactly in either family, with $a\ge0$:

1. $d=1+22a$, $m=22t$, $t\not\equiv-2a\pmod{11}$.
2. $d=17+22a$, $m=12+22t$, $t\not\equiv2-2a\pmod{11}$.

Each eligible width gives ten classes modulo 242. These formulas are checked against the complete 242-by-242 table.

### Prime 13

Every rotation has valuation one at 13 exactly when

$$d=s+78a,\quad m=b+Lt,\quad t\not\equiv\alpha+\beta a\pmod{13},\quad a\ge0,$$

for a row of this table:

| $s$ | $L$ | $b$ | $\alpha$ | $\beta$ |
|---:|---:|---:|---:|---:|
| 1 | 78 | 0 | 0 | 1 |
| 15 | 26 | 22 | 10 | 8 |
| 17 | 78 | 24 | 2 | 9 |
| 25 | 78 | 24 | 0 | 1 |
| 29 | 78 | 54 | 11 | 9 |
| 45 | 26 | 24 | 0 | 8 |

The two $L=26$ rows give 36 classes modulo 1014; each other row gives 12. The verifier checks every lifted width phase and every endpoint residue against this compact description. The matrix periods and covering proposition make this a proof for arbitrary endpoints, not an extrapolation from the first few lifts.

## 4. Odd-order primes reach the parity gap

If $\operatorname{ord}_p(10)$ is even and every rotation is divisible by $p$, the gcd identity forces $D(m)$ even. But $D(m)$ is odd for every even digit length, and has parity $m$ for odd digit length. Uniform common-valuation tests at such primes cannot handle these odd-$D(m)$ blocks.

The orders of 10 modulo 31 and 41 are respectively 15 and 5, so they avoid that obstruction. Both orders are divisible by 5, so they also fall outside the earlier averaging theorem's hypothesis $10^P\equiv1\pmod{9\operatorname{ord}_p(10)}$. The finite-period method still applies.

**Theorem.** Each family below excludes every integer perfect-power rotation:

- $d=168+465a$, $m=91+155t$, $t\not\equiv2+4a\pmod{31}$.
- $d=38+205a$, $m=126+205t$, $t\not\equiv15+15a\pmod{41}$.

Here $a\ge0$. At these respective digit lengths, the displayed conditions also completely characterize uniform valuation one at the named prime.

**Proof.** The exact prefix formulas are

$$W_m\equiv31(28+17t-6a)\pmod{961},$$

$$W_m\equiv41(5+27t+5a)\pmod{1681}.$$

The endpoint periods are respectively 4805 and 8405. The proven width periods reduce these identities to all 961 and 1681 parameter pairs $(a,t)$ modulo the respective prime, which the verifier checks exhaustively. Also

$$D(m)\equiv0\pmod{465}\iff m\equiv91\pmod{155}\quad(d\equiv168\pmod{465}),$$

$$D(m)\equiv0\pmod{205}\iff m\equiv126\pmod{205}\quad(d\equiv38\pmod{205}).$$

Thus $p^2\mid\Delta$, and the nonzero normalized prefix conditions are exactly the excluded lifts stated in the theorem. The covering proposition gives necessity as well as sufficiency at those widths.

Two particularly simple subfamilies are

$$d\equiv168\pmod{28830},\quad m\equiv91\pmod{28830},$$

$$d\equiv38\pmod{16810},\quad m\equiv331\pmod{50430}.$$

In both, $d$ is even, $m$ is odd, and $m\equiv1\pmod3$. Every rotation is therefore a square in $\mathbb Q_3$, yet the prime-valuation theorem excludes every integer perfect power. These are genuine examples outside both the 3-adic exclusion and the even-order common-divisibility method.

## 5. Exact intersections and coverage

These are **endpoint residue densities within eligible digit intervals**, not densities among digit lengths or sequence entries. Actual finite-interval counts have the ordinary incomplete-period endpoint error.

For $d\equiv346803\pmod{858858}$, selected 7, 11 and 13 families apply simultaneously. Their endpoint conditions are

$$m\equiv2\pmod{14},\ m\not\equiv30\pmod{98};$$
$$m\equiv12\pmod{22},\ m\not\equiv56\pmod{242};$$
$$m\equiv22\pmod{26},\ m\not\equiv282\pmod{338}.$$

They share even parity. Conditional on even $m$, their moduli 49, 121, 169 are coprime, with respectively 6, 10, 12 excluded classes. The union density is

$$u_E=\frac{1-(43/49)(111/121)(157/169)}2=\frac{126320}{1002001}.$$

For $d=9468+19065n$, both odd-order families apply. Their lifted exceptions are $20+9n$ modulo 31 and $8+n$ modulo 41. Both require $m\equiv1\pmod5$. Conditional on that residue, the moduli $31^2$ and $41^2$ are coprime, with 30 and 40 excluded classes. Their union density is

$$u_O=\frac{1-(931/961)(1641/1681)}5=\frac{17534}{1615441}.$$

The conditional factors $1/2$ and $1/5$ are essential. Treating events within either group as unconditionally independent would be wrong.

The groups are simultaneously available on

$$d\equiv4200162423\pmod{5458042590}.$$

Their endpoint moduli are coprime to one another, so the five-prime union density is

$$u=1-(1-u_E)(1-u_O)=\frac{219416697774}{1618673497441}.$$

It is also coprime to the 3-power modulus of the manuscript's complete local criterion. If $q(d)$ is that criterion's excluded fraction, the combined sufficient global exclusion fraction is $q(d)+(1-q(d))u$. For $h=v_3(d)=1,2,3,4$, this is approximately 60.1572%, 60.8687%, 61.9491%, 61.9622%.

This particular five-prime width progression is odd. The separate odd-order families provide the even-width exclusions. The manuscript already proves the existence of other width progressions with arbitrarily high coverage; the present explicit calculations are not a new claim of that general existence result.

## 6. Infinite simultaneous local powers that remain

Let $S=\{2,3,5,7,11,13,31,41\}$, $T=38168130$, and $M=152672520$.

**Theorem.**

1. If $d\equiv31\pmod T$ and $m\equiv53392081\pmod M$, the same integer $W_m$ is a square in every $\mathbb Q_p$, $p\in S$.
2. If $d\equiv32\pmod T$ and $m\equiv95797681\pmod M$, the same integer $W_m$ is a seventeenth power in every $\mathbb Q_p$, $p\in S$. Here $d$ is even and $m$ is odd.

These statements concern a common cut and exponent at every listed prime. They are not integer counterexamples.

**Proof.** Modulo the primes themselves, the append and sufficient boundary periods are $E=pr$, with the following data:

| $p$ | $r=\operatorname{ord}_p(10)$ | $E$ | Affine translation in one $r$-width cycle |
|---:|---:|---:|---:|
| 7 | 6 | 42 | 0 |
| 11 | 2 | 22 | 9 |
| 13 | 6 | 78 | 8 |
| 31 | 15 | 465 | 28 |
| 41 | 5 | 205 | 21 |

The same matrix argument proves these periods: every $A_d^E=I$ and repeating the affine translation $p$ times gives the identity modulo $p$. Thus $W_m\pmod p$ depends on $d,m\pmod E$ for $d\ge2$. Here $T$ is the least common multiple of the five periods and $M=\operatorname{lcm}(T,120)$.

Direct exact prefix computations at widths 31 and 32 give residues at $(7,11,13,31,41)$ equal respectively to $(1,1,1,1,1)$ and $(1,8,1,1,1)$. All 34 append phases, the affine identities, and these residues are certified. Both endpoint progressions are 1 modulo 120. Digit sums give $W_m\equiv1\pmod3$, and the final integer block gives $W_m\equiv1\pmod5$ and $W_m\equiv1\pmod8$.

For the first family, the odd-prime square roots lift by Hensel's lemma; an odd 2-adic unit is a square precisely when it is 1 modulo 8. For the second, every residue is a unit and $\gcd(17,p(p-1))=1$ at each listed prime. The seventeenth-power map is bijective on the nonzero residue field and has unit derivative, so its roots lift in $\mathbb Z_p^\times$. This proves the theorem.

By CRT, the first family is a square modulo every modulus supported on $S$, and the second is a seventeenth power modulo every such modulus. Increasing the powers of these eight primes or combining their necessary local conditions cannot remove these candidates. This is a limitation of this particular finite-prime collection, not a claim that every possible local or global approach must fail. Other primes, growing moduli or global Diophantine arguments may still help.

## 7. Verification and provenance

Run from `papers/A001292`:

```sh
python verify_seven_complete.py
python verify_eleven_thirteen.py
python verify_odd_order_families.py
python verify_local_survivor_families.py
```

The first two use the already published `verify_a001292.py`; the 11/13 audit also uses `prime_period_certificates.py`. The later two are self-contained. Scripts emit exact JSON certificates beside themselves.

Fresh outputs are [7](prime7-verification.txt), [11/13](prime11-13-verification.txt), [31/41](prime31-41-verification.txt), and [simultaneous local powers](local-survivors-verification.txt). They include exhaustive period/classification checks, 1,498,500 direct rotation checks for the 7/11/13 classifications, independent arithmetic-geometric prefix calculations through 2043-digit endpoints, and exact conditional CRT enumerations.

This supplement is newly assembled from recovered proofs and freshly rerun certificates. The 31/41 and simultaneous-local-power verifiers are byte-identical to their recovered originals. The 7/11/13 scripts have portability changes to import and output paths; the period helper was renamed. The main 18-cut manuscript remains unchanged. [Provenance metadata](prime-supplement-provenance.json) records the hashes and these distinctions. None of the local equivalences, finite certificates or coverage estimates resolves the integer conjecture.

## Further generalization

The subsequent [finite-prime limitation theorem](FINITE_PRIME_LIMIT.md) extends the last obstruction from this particular eight-prime set to **every fixed finite prime set**. It proves positive lower density in the endpoint index for simultaneous local squares, with one common exponent and cut. It does not claim positive density of integer squares or rule out additional primes or global arguments.
