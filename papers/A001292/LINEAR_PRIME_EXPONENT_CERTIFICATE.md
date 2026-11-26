# A linear certificate for prime exponents beyond squares and cubes

This supplement gives a finite-field progression lemma that does not require the digit width to be divisible by the witness order. Its explicit fifth-power instance produces integer nonpower blocks that are fifth powers in Q_3 but neither squares nor cubes there. The earlier Q_3-square and Q_3-cube families are therefore disjoint from this instance.

## 1. A progression lemma

Let p be a prime not dividing30, and suppose10 has order q modulo p, where q is an odd prime different from3. Let e>=5 be a prime dividing (p-1)/q. These are hypotheses to verify for a chosen pair, not a claim that suitable primes exist for every e.

Fix a digit width d with q not dividing d. Set

    R_d=(10^d-1)/9,
    a_d=R_d*d^(-1)-1 modulo q.

For endpoints m=a_d modulo q, the length D(m)=d(m+1)-R_d is divisible by q. Hence p divides the cyclic modulus. Since10 has order q dividing (p-1)/e, it is an e-th power modulo p and multiplication by10^D(k) preserves e-th-power cosets at every cut.

Put B=10^d modulo p. Its order is q and B!=1. Appending q consecutive integers gives

    W_(m+q)=W_m+q/(1-B) modulo p.

The coefficient of the previous prefix is B^q=1; the coefficient of m is the geometric sum, which is0; the weighted constant is q/(1-B). Consequently, on the specified endpoint progression inside the digit interval,

    W_m=m/(1-B)+c_d modulo p

for a constant c_d. The slope is nonzero. The constant may depend on the width and progression; its actual value is unnecessary for counting.

There are exactly (p-1)(e-1)/e nonzero residues that are not e-th powers in F_p. CRT between q and p therefore gives exactly that many successful classes modulo pq, with density

    eta=(p-1)(e-1)/(e*p*q)

among all endpoint residues. Each successful class rules out integer e-th powers for every rotation. This statement alone does not rule out other integer exponents.

## 2. Combining with power-of-e3-adic valuations

Let h=v_3(d), and choose b=e^r with r>=1 and b<=h+1. Take any of the four classes

    m=3^b, 2*3^b, 3^b-1, 2*3^b-1 modulo3^(b+1).

These are exactly the classes for which v_3(T_m)=b. The inherited cubic reduction gives

    10^(-D(k))*R_(m,k)=T_m modulo3^(h+2).

Its precision exceeds b. Therefore every rotation has exact3-adic valuation b. Since e>=5, raising to the e-th power is an automorphism of the3-adic unit group; a nonzero3-adic number is an e-th power exactly when its valuation is divisible by e. Thus every rotation is an e-th power in Q_3. The valuation b is odd and not divisible by3, so no rotation is a Q_3 square or cube.

Any possible prime exponent of an integer power must divide b=e^r, hence must be e. The finite-field obstruction in Section1 rules out this last exponent. Combining these conditions yields an entire integer-nonpower block.

The modulus3^(b+1) is coprime to p and q, so these conditions combine by exact CRT without losing classes. Endpoint parity is unrestricted. Widths can be even or odd, subject only to the stated hypotheses.

## 3. Infinite valuation union and interval error

Let B_e be the largest power of e not exceeding h+1, assuming h+1>=e. Define

    K_e=sum_{r>=1}4/3^(e^r+1),
    K_(e,h)=sum_{e<=b<=B_e, b a power of e}4/3^(b+1).

Classes at different b are disjoint by their triangular-number valuations. The exact certified density in a full endpoint period is eta*K_(e,h), with a common period

    T=p*q*3^(B_e+1)<=p*q*3^(h+2).

The omitted tail is bounded by summing over every integer b>=e*B_e:

    0<=K_e-K_(e,h)<=2*3^(-e*B_e)<=2*3^(-(h+2)).

For H=9*10^(d-1), d>=3^h, one has

    T/H<=10*p*q*3^h/10^(3^h).

Discarding an incomplete period gives the explicit certified endpoint lower count

    H*[eta*K_e-2*3^(-(h+2))-10*p*q*3^h/10^(3^h)].

In particular the certified proportion is at least eta*K_e-O(3^(-h)), uniformly in d/3^h subject to q not dividing d. A negative numerical lower bound at small h is simply vacuous; the exact residue criterion remains valid.

These are digit-interval endpoint counts, not a natural density across all sequence entries or widths. The proof does not assume an infinite supply of witness primes.

## 4. An explicit fifth-power instance

Take

    e=5, p=1031, q=103.

Both p and q are prime; exact arithmetic gives10^103=1 modulo1031 and10!=1, hence the order is103. Also(p-1)/q=10 is divisible by5. All conditions of the progression lemma hold, and

    eta=824/106193.

For every width with103 not dividing d and h=v_3(d)>=4, the construction is available. The asymptotic assertion applies as h tends to infinity. It includes both parities of widths and imposes no parity restriction on endpoints. It does not assert that every odd endpoint or every even width is certified.

The limiting lower proportion is

    (824/106193)*sum_{r>=1}4/3^(5^r+1).

The family is outside the previous Q_3-square and Q_3-cube block families. It is not outside every other possible local obstruction, and it is not a counterexample or a solution to the global integer-power conjecture.

## 5. Novelty and verification scope

The matrix/concatenation recurrence, inherited3-adic reduction, and general finite-field power test are existing ingredients. The new combination uses a nontrivial witness-order endpoint progression rather than requiring q|d, and proves an infinite valuation-union family for an exponent beyond2 and3. This is not a claim of literature priority or a theorem supplying witnesses for every prime exponent.

The verifier checks the explicit prime/order/power data, exact non-fifth-power counts, scalar q-step identities in all102 nontrivial B phases, finite tail bounds, selected actual prefixes and rotation cuts, and the stated3-adic valuation residues. It does not enumerate whole large endpoint intervals or all valuations. Unbounded assertions follow from the proof. The main manuscript/PDF remain unchanged.

Run `python papers/A001292/verify_linear_prime_exponent.py`; it imports the published sibling matrix-prefix routine from `verify_antiperiodic_thirteen.py`. Separated copies need that module directory on PYTHONPATH.

The included independent verifier checks408 complete affine counts,29520 triangular valuation residues, all12 supplied prefixes, and120 cuts including digit boundaries, midpoints and late cuts. Its certificate path is adapted to the published sibling-file layout.
