# An antiperiodic13 certificate at every odd multiple-of-three digit width

The earlier bounded-valuation construction used a very large common width period and primes with10^d=1. Here10^d=-1 modulo13 instead gives a linear prefix formula. The resulting family applies already at width3 and at every width3 modulo6; it is not another enormous-width CRT construction.

## Explicit theorem

Let d=3+6a with a>=0, and let m be a d-digit endpoint. Put

    N={2,5,6,7,8,11},

which is precisely the set of quadratic nonresidues modulo13. Suppose

    m=8 or18 modulo27,
    m is even,
    m/2+5(a+1) modulo13 belongs to N.

Then every whole-block rotation R_(m,k) is an integer nonpower. Every one of these rotations is a square in Q_3 but a nonsquare unit in Q_13.

At each such digit width the condition selects exactly12 residue classes modulo702=27*26, so the number of certified endpoints in the digit interval of length H=9*10^(d-1) is

    (2/117)*H + O(12),

with absolute error at most12. The explicit congruence criterion, rather than this rounded count, applies to every endpoint. It is periodic in the width modulo78, but the theorem covers every d=3 modulo6, not merely multiples of a large width period.

In particular it includes infinitely many widths with v_3(d)=1, such as d=3+18t and d=15+18t for t>=0. It also includes odd widths of larger3-adic valuation. It does not address even widths or claim that the unselected endpoints are powers.

## 1. Exact complete-block period

Let V_j=W_(10^j-1). To append integers starting at u in a width-j block, use the state (W,u,1) and matrix

    A_j=[[10^j,1,0],[0,1,1],[0,0,1]] modulo13.

The multiplicative order of10 modulo13 is6. For each of the six phases, A_j^78 is the identity modulo13; this is checked by exact3-by-3 matrix arithmetic in the accompanying verifier. Alternatively, the eigenvalue10^j has order dividing6, and raising to a multiple of13 kills the possible unipotent part in characteristic13.

For j>=2, the start10^(j-1) and block count9*10^(j-1), modulo78, repeat when j increases by6: modulo2 both starts are even, and modulo39 the order of10 is6. A_j itself repeats modulo13. The full-block affine map F_j on W therefore has period6 for j>=2.

Moreover9*10^(j-1)*j is divisible by6, so the coefficient multiplying the old W is1 modulo13. The exact translations for j=2,3,4,5,6,7 are respectively

    5,8,11,4,7,12 modulo13.

Their sum is8 modulo13. Propagating the six-periodic translations gives

    V_(j+6)=V_j+8 modulo13 for every j>=1.

These are complete finite phase checks establishing an unbounded recurrence, not extrapolation from selected prefixes. The six-width boundary translation by8 modulo13 already appears in PRIME_FAMILIES.md; it is reused and independently reverified here, not claimed as a new period mechanism.

## 2. Linear prefix formula at even endpoints

Fix d=3+6a and put L=10^(d-1), an even integer. Since10^d=-1 modulo13, appending two successive integers gives

    W_m=W_(m-2)+1 modulo13

whenever both endpoints are even and in the same width. At the first endpoint,

    W_L=-V_(d-1)+L modulo13.

Thus at every even m in the interval,

    W_m=m/2+c_d modulo13,
    c_d=-V_(d-1)+L/2 modulo13.

Here division by2 is well defined modulo13 and m/2 is also an actual integer. The residue of L repeats when d increases by6, whereas V_(d-1) increases by8. Consequently c_(d+6)=c_d-8=c_d+5 modulo13. Direct computation at d=3 gives c_3=5. Hence

    W_m=m/2+5(a+1) modulo13,

as asserted.

## 3. Every rotation, and every integer exponent

For d-digit m,

    D(m)=d(m+1)-(10^d-1)/9.

Because3 divides d, LTE implies that the second term is divisible by3, so3 divides D(m). The second term is odd; d is odd and m is even, so d(m+1) is odd too. Therefore D(m) is even, and6 divides D(m). It follows that13 divides the cyclic modulus10^D(m)-1.

The rotation identity now gives

    R_(m,k)=10^D(k)*W_m modulo13.

The number10 is a square modulo13 (6^2=10). The stated nonresidue condition on W_m therefore makes every rotation a nonsquare unit modulo13, excluding integer squares.

The published uniform cubic formula, since h=v_3(d)>=1, gives

    10^(-D(k))*R_(m,k)=T_m modulo27.

Both endpoint classes8 and18 give T_m=9 modulo27. Thus every rotation has exact3-adic valuation2 and normalized unit1 modulo3; all are Q_3 squares. Any integer prime exponent must divide2 and therefore must equal2. The nonsquare condition at13 rules this out, excluding every nontrivial integer power.

## 4. Count and comparison with existing results

The map from even residues m modulo26 to m/2 modulo13 is a bijection. There are six allowed values for the latter, regardless of a. Combining them with either endpoint class modulo27 yields12 distinct classes modulo702. Counting each residue in the endpoint interval differs from H/702 by at most1, proving the stated absolute error.

The old complete13-adic valuation-one classification already includes antiperiodic widths15 and45 modulo78; this is not the first use of that phase. That classification required W_m divisible by13. Here W_m is explicitly a nonzero nonresidue modulo13, so these certificate families are disjoint. This does not claim that every newly displayed endpoint was absent from all previous tests: small endpoints were already computationally checked, and other primes may give additional proofs. The new content is the exact linear formula, its uniform all-width certificate, and its finite period/count.

The quadratic reduction for10^d=1 used in earlier supplements does not cover this phase:10^d=-1 here. The integer conjecture remains open. No compatibility with the Q_37 square test is claimed. The main manuscript and PDF remain unchanged.

## 5. Verification scope

The standard-library verifier checks all six matrix phases and translations, and derives the modulus702 class counts for all13 width phases. It independently constructs prefix residues at all endpoints through width3, checking the450 even three-digit endpoints, then checks selected larger-width prefixes by matrix exponentiation. For the15 certified three-digit endpoints it directly checks every available whole-integer rotation modulo27 and13. These finite checks are separate from the proofs of the unbounded recurrence and whole-block theorem.

Run `python papers/A001292/verify_antiperiodic_thirteen.py` from the repository root. The script uses only the Python standard library.
