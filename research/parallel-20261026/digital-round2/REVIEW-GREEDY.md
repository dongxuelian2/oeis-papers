# Independent greedy/formula round-two review, 2026-10-26

Read the full manuscripts and verifiers of A260056, A308620 and
A092635. Independently opened each official OEIS entry (plus A004524)
and reran all three verifiers successfully. No algebraic or
implementation blocker found.

## A260056

The trinomial expansion by the number i of nonconstant selections
gives x^i(1+x)^i. Extracting x^k and summing binomial(j,i) gives
the stated column formula, including rows where i>n. Its i=k term
has exact leading coefficient 1/(k+1)!, proving the degree and
minimal difference order. The bivariate substitution (z,-z) gives
1/((1-z)^2(1+z²)); A004524's official generating function has exactly
the required z³ factor, confirming the shift. The supplied four-case
expression agrees independently. Both recorded conjectures are
fully addressed, with all row/column indices included.

## A308620

Checked the original official Maple sums against the manuscript.
Re-derived each of the five component generating functions by setting
n equal to its minimum permitted value plus j. In particular the
floor(j/2) counts produce (1+x)/(1-x²)^(h+1), giving both barred
expressions exactly. The combined denominator D*E and numerator
identity agree with the verifier, and its degree-11 remainder proves
the recurrence starts at 12. The stated n=11 defect is genuine.

The direct word/reflection enumeration is independent of the
binomial sums and passed through length18. The proof appropriately
attributes the original game-state count to Burger, van der Merwe
and van Vuuren and treats the rational-GF conjecture as the completed
problem. An independent web fetch returned HTTP502, but the agent supplied
its earlier successful download at /tmp/oeis-gamespaths.pdf. Read
Theorem3/Eq4.2 directly and its full Q/R/S derivation in the extracted
text, and visually inspected the primary theorem page. All five
sums match the manuscript, including floors, limits, and one-half
factors. The source also confirms reflection classes and the
run-length steady-state characterization. Primary-source audit passes.

## A092635

The logarithmic Stirling cancellation gives the displayed odd
coefficients with the correct scaling x=1/(8t). The Bernoulli
expansion of 2/(1+exp(4z)) matches these coefficients multiplied
by their index, proving the proposed exponential formula and
recurrence. The Euler-polynomial sign convention is consistent.

Independently checked duplication:
F(t)=t*(Gamma(t+1/2)/Gamma(t+1))², hence
F(t)F(t-1/2)=(t-1/2)/t. Its asymptotic formal shift gives
G(x)G(x/(1-4x))=1-4x. Together with oddness of logG this proves
all three stated H identities, with formal compositions well-defined
and no use of negative-t analytic evaluation or convergence.
The second coefficient construction from the exact gamma shift
is independent of the Euler coefficients and all301official values
agree; all three identities were independently rerun through100.
