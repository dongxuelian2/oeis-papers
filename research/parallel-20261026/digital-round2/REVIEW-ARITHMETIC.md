# Independent arithmetic round-two review, 2026-10-26

Read all three complete manuscripts and verifiers and independently
reopened A308090, A357127, A081257, and A334958 on official OEIS.
Reran every verifier successfully. No mathematical blocker found.

## A308090

The composite-factorial lemma correctly treats every composite m>4
and isolates the exceptional m=4. Wilson/Fermat give the prime branch
for m>=5, and the composite gcd reduces to gcd(2^n,3^n,m)=1.
The three small m values are indeed one. The counterexample to the
entry's separate single-sum assertion is valid and does not weaken
the proved joint-gcd classification. The finite modular audit checks
the original definition, rather than substituting the prime formula.

## A357127

Confirmed A081257 is the largest prime factor of n^3-1. Passing to
n²+n+1 for factors exceeding n is valid. A nonunit p>n cannot be
3 and makes n an element of order three modulo p. Its second root
m=p-n-1 lies in [2,p-1] and is distinct. Since f(m)<p², the known
factor p is necessarily the largest prime factor, proving the
involution. The converse and exactly-two multiplicity use the two
nontrivial cube roots in a finite field; no root is lost at endpoints.

Both the unit counterexample and the stronger nonunit pair 35,61
are correct. The replacement gcd formula follows exactly by
subtracting f(m)-f(n)=p(m-n). Thus the paper proves conjecture 1,
refutes conjecture 2 as stated even in its natural nonunit reading,
and provides a complete valid correction. It explicitly leaves the
separate new-record observation about A256148 open.

## A334958

The recurrence A_(n+1)=(n+1)A_n+(-1)^(n+2)n! gives the gcd reduction
by one Euclidean step. If H'_n=u/v is reduced, integrality yields
v|n!, and gcd((n!/v)u,(n!/v)v)=n!/v. The valuation product is
exactly this reduced-denominator identity, not an empirical pattern.
The B identities and the lcm divisibility follow as written.

Scope is essential: this completes the explicit all-index
valuation-product conjecture and the stated divisibility observation.
The independent infinitude assertions in the entry remain open,
as the manuscript clearly says. Count this as one completed problem,
not as complete resolution of every question attached to A334958.
