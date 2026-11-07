# A general limitation of fixed finite-prime tests

**The integer perfect-power conjecture remains open.** This note proves a limitation of necessary local square conditions for an arbitrary fixed finite set of primes. It does not construct integer squares or assert that every possible local or global proof method must fail.

Let $W_m=1\Vert2\Vert\cdots\Vert m$ be the unrotated decimal concatenation. Densities in this note concern the **endpoint index $m$**, not the enumeration of all rotations in A001292.

## 1. Statement for every finite prime set

Let $S$ be any finite set of primes and put $P=S\setminus\{2,3,5\}$. For $p\in P$, define $r_p=\operatorname{ord}_p(10)$. Set

$$L=\operatorname{lcm}_{p\in P}r_p,\qquad Q=\operatorname{lcm}\bigl(120,\{p(p-1):p\in P\}\bigr),$$

$$\sigma=\frac1{120}\prod_{p\in P}\frac{p-1}{2p}.$$

An empty least common multiple is 1 and an empty product is 1.

**Theorem.** The set of endpoints $m$ for which the same integer $W_m$ is a square in every $\mathbb Q_p$, $p\in S$, has lower natural density at least

$$\frac{9\sigma}{10^L-1}>0.$$

More precisely, for every digit length $d\ge3$ satisfying

$$r_p\nmid d\quad\text{for every }p\in P,$$

there is a union of exactly $\sigma Q$ endpoint residue classes modulo $Q$, all congruent to 1 modulo 120, whose $d$-digit representatives have this simultaneous local-square property. The classes can depend on $d$, but their count does not. In any subinterval of that digit interval, their count is $\sigma$ times its length plus an error of absolute value at most $Q$.

The progression $d\equiv1\pmod L$ always qualifies. Indeed $r_p>1$ for $p>5$, because a prime with $10\equiv1\pmod p$ would divide 9.

## 2. The concatenation is affine-exponential within a digit interval

Fix $d$, and write

$$B=10^d,\qquad b=10^{d-1},\qquad c=B-1,\qquad A=c^2W_{b-1}+bc+1.$$

The recurrence $W_m=BW_{m-1}+m$ gives the exact identity

$$c^2W_m=A B^{m-b+1}-((m+1)c+1)\qquad(b-1\le m<B).$$

It holds at $m=b-1$ by the definition of $A$, and induction using the recurrence proves it at the next endpoint.

If $p\nmid10c$, reduce this identity modulo $p$ to obtain

$$W_m\equiv F_{p,d}(m)=\alpha_p B^m+\beta_p m+\gamma_p\pmod p,$$

where

$$\alpha_p=AB^{1-b}/c^2,\qquad\beta_p=-1/c,\qquad\gamma_p=-B/c^2.$$

In particular $\beta_p\ne0$. The hypothesis $r_p\nmid d$ is exactly what ensures $p\nmid c$.

For counting purposes $F_{p,d}(n)$ has a periodic extension to all integers $n$, with period dividing $p(p-1)$. It is identified with the actual concatenation only inside the fixed digit interval. No global periodicity of the entire sequence $W_m$ across digit boundaries is being assumed.

## 3. Exact simultaneous counting, including overlapping periods

**Lemma.** For any finite set $P$ of primes greater than 5, suppose

$$F_p(n)=\alpha_p B_p^n+\beta_p n+\gamma_p\pmod p,\qquad p\nmid B_p\beta_p.$$

Among the residue classes modulo $Q=\operatorname{lcm}(120,\{p(p-1):p\in P\})$, the conditions

$$n\equiv1\pmod{120},\qquad F_p(n)\text{ is a nonzero square modulo }p\quad(p\in P)$$

hold in exactly the fraction $\sigma$ defined above, regardless of the coefficients.

**Proof.** Start with the single class 1 modulo 120, of density $1/120$. Add primes in increasing order. Suppose all earlier conditions have a period $T$, and let $q$ be the next prime. Put

$$H=\operatorname{lcm}(T,q-1).$$

Every prime factor of $T$ is less than $q$: initially they are 2, 3 and 5, and an earlier prime $p$ contributes only factors of $p(p-1)$. Also every prime factor of $q-1$ is less than $q$. Hence $q\nmid H$.

In each fixed class $a\pmod H$, all earlier conditions are fixed and the exponential term $B_q^n$ is fixed modulo $q$. Its $q$ lifts $n=a+Ht$ for $0\le t<q$ give

$$F_q(a+Ht)\equiv C+\beta_q Ht\pmod q.$$

The slope is nonzero, so these values run through the entire residue field. Exactly $(q-1)/2$ are nonzero squares. Thus the proportion is multiplied by $(q-1)/(2q)$ in every surviving class. The new common period is $qH=\operatorname{lcm}(T,q(q-1))$. Induction proves the formula.

This argument does not assume that the periods $p(p-1)$ are pairwise coprime. For example, one tested prime may divide another tested prime minus one.

## 4. Local roots and the lower-density conclusion

Apply the lemma to the affine-exponential expressions in an eligible digit interval. For every $p\in P$, a nonzero square residue lifts to a square in $\mathbb Q_p$ by Hensel's lemma.

The imposed endpoint condition $m\equiv1\pmod{120}$ handles the other primes uniformly:

- The final integer block gives $W_m\equiv1\pmod5$.
- Since $d\ge3$, the final integer block gives $W_m\equiv1\pmod8$, the criterion for an odd 2-adic unit to be a square.
- Digit sums give $W_m\equiv m(m+1)/2\equiv1\pmod3$.

Thus the same unrotated member is a square at every prime in $S$. It is also positive, so the real place supplies no obstruction.

For the density assertion, restrict to widths $d\equiv1\pmod L$, omitting finitely many small widths. Let $N_L(X)$ count positive integers up to $X$ in those width intervals. Counting complete and partial periods within each digit interval gives a subset $C$ of the simultaneous local squares with

$$\#(C\cap[1,X])=\sigma N_L(X)+O_S(Q\log X).$$

The coefficients and the precise surviving classes may change with the width, but their fraction remains exactly $\sigma$, so this estimate is uniform over the intervals.

A geometric-series calculation gives

$$\liminf_{X\to\infty}\frac{N_L(X)}X=\frac9{10^L-1}.$$

For completeness, just before a selected width $d$, the earlier selected blocks have total length

$$9\sum_{j\ge1}10^{d-jL-1}$$

up to a finite initial correction. Dividing by $10^{d-1}$ tends to $9/(10^L-1)$. During a selected block the fraction increases, and during the intervening unselected blocks it decreases, so these are the limiting minima. The $L=1$ case is all sufficiently large integers and gives 1. The counting error divided by $X$ tends to zero. This proves the theorem.

## 5. Quantitative consequence for the eight primes already studied

For $S=\{2,3,5,7,11,13,31,41\}$, the orders at the primes greater than 5 are $6,2,6,15,5$. A digit length qualifies exactly when it is odd and not divisible by 5.

Here

$$Q=152672520,\qquad \sigma=\frac{225}{1272271}=\frac{27000}{152672520}.$$

Thus **every eligible digit length has exactly 27000 simultaneous local-square endpoint classes modulo $Q$**. This is stronger than exhibiting a single fixed endpoint class along a large width progression: the classes are allowed to adapt to the width, while the count is uniform.

The general theorem already yields a positive lower density by using $d\equiv1\pmod{30}$. Using all qualifying widths, which are $1,3,7,9\pmod{10}$, improves the lower-density bound to

$$\frac{227272725}{1413634444303081}\approx1.6077192085684\times10^{-7}.$$

To check this last number, the limiting fraction of integers in the qualifying width blocks at the end of width phase $r$ is

$$\frac9{10^{10}-1}\sum_{j=0}^{9}\mathbf1_{\{1,3,7,9\}}(r-j\bmod10)10^{9-j}.$$

Its minimum, at phase 6, is $1010101/1111111111$. Multiply by $\sigma$ and use the same interval-counting argument as above.

## 6. What this does and does not rule out

For every fixed finite prime set, infinitely many candidates survive **all p-adic precisions at once**, with a common exponent 2 and a common cut zero. By CRT they are squares modulo every positive integer whose prime factors lie in that set. Consequently a proof that merely tries to reject every candidate by necessary local square conditions at a fixed finite collection of primes cannot finish the conjecture.

This is not a proof that integer squares occur. It does not obstruct additional primes that grow with the endpoint, global inequalities, digit-structure arguments, or other Diophantine input. Nor does it claim every rotation of a surviving block is locally square. A single surviving member is enough to prevent exclusion of that entire block by this finite collection of necessary conditions.

The positive density is in the endpoint index $m$. It is not a positive density of integer perfect powers and does not conflict with the manuscript's density-zero theorem for actual powerful values.

## 7. New verification and provenance

This is a newly proved generalization, not a restored old file. It reuses the fixed-digit affine-exponential identity from the main manuscript and supplies the full simultaneous-square counting and density argument above.

Run `python verify_finite_prime_limit.py` beside the existing `verify_a001292.py`. The audit checks the joint-count lemma by exhaustive periods for prime sets with overlapping dependencies, then checks actual concatenation coefficients against a separate arithmetic-geometric formula. At width 9 it checks all 27000 surviving classes; at widths 11 and 31 it checks 1000 classes each, for a total of 145000 independent prime-residue comparisons. It also verifies the exact product density and geometric density formulas.

The arbitrary-finite-set theorem follows from the proof, not from extrapolating those numerical examples. See [fresh output](finite-prime-limit-verification.txt), [exact certificate](finite-prime-limit-certificate.json), and [provenance](finite-prime-limit-provenance.json).
