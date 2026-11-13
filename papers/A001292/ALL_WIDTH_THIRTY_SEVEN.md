# An effective37 certificate at every digit width

The new component here is the linear37-prefix formula when3 does not divide the digit width. The published quadratic formula for widths divisible by3 and the general mod27 identity are inherited. Their combination supplies one explicit sufficient endpoint certificate at every width, including even widths and odd endpoints. It does not classify all endpoints or solve the integer conjecture.

## Theorem

Let d>=2 and let m be a d-digit endpoint with m=18 modulo27. Define F_d(m) modulo37 as follows:

    d=1+3a: F_d(m)=4m+33a;
    d=2+3a: F_d(m)=34m+26+33a;
    d=0 modulo3: F_d(m)=m(m+1)/2+11d.

If F_d(m) is a quadratic nonresidue modulo37, every rotation in the endpoint block is an integer nonpower. All those rotations are squares in Q_3 and nonsquare units in Q_37. No endpoint parity restriction is imposed.

If3 does not divide d, there are exactly18 allowed classes modulo999, giving a certified count

    (2/111)*H + error of absolute value at most18,
    H=9*10^(d-1).

If3 divides d, write Delta=1-88d modulo37. The number n_d of allowed classes modulo999 is

    17 if Delta is a nonzero square;
    18 if Delta is a nonsquare;
    36 if Delta=0.

The count is n_d*H/999 with absolute error at most n_d. In particular, at every width d>=2 there are at least17 sufficient classes modulo999 and at least17*H/999-36 certified endpoints. This lower bound can be vacuous for small widths; the exact residue test is still valid there. At width2 it certifies endpoints45 and72, including an odd endpoint.

The d=0 modulo3 branch uses an old prefix identity and is not claimed as a new local formula. The new width phases are d=1,2 modulo3; they include every even width coprime to3, all of which have v_3(d)=0. The result is effective from the stated small widths, rather than restricted to a giant common width multiple.

## 1. A linear prefix along multiples of3

Let V_j=W_(10^j-1), B=10^d modulo37, and assume3 does not divide d. Then B has order3. Appending three consecutive integers shows

    W_(m+3)=W_m+3/(1-B) modulo37.

The coefficient of the old prefix is B^3=1, the coefficient of m is1+B+B^2=0, and the weighted constant sum is3/(1-B). Thus along m=0 modulo3 the prefix is affine with slope (1-B)^(-1). The slopes are4 for d=1 modulo3 and34 for d=2 modulo3.

The already established complete-block translations at widths j=2,3,4 are26,8,36 modulo37; their sum is33 modulo37. They repeat with period3 for j>=2, yielding

    V_(j+3)=V_j+33 modulo37 for j>=1.

For completeness, the append matrix A_j on (W,u,1) satisfies A_j^111=I modulo37 in each of its three phases. The start10^(j-1) and count9*10^(j-1) repeat modulo111 on increasing j by3, since the order of10 modulo111 is3. The full-block multiplier is1. These exact finite phase calculations prove the recurrence; the previous supplements already recorded these translations.

For d>=2 the first multiple-of3 endpoint in the width is L+2, with L=10^(d-1)=1 modulo3. Appending those three integers multiplies V_(d-1) by B^3=1. The remaining residues repeat as d increases by3. Hence the affine constant increases by33 modulo37. Base constants at widths2 and4 are26 and33 respectively, proving the two linear formulas displayed in the theorem. The phase1 formula also holds at width1, but the theorem does not need that width.

At widths divisible by3, the published formula W_m=T_m+11d modulo37 supplies the third phase directly. All three formulas are only used at m=0 modulo3, which contains the specified endpoint class.

## 2. Rotation invariance and all integer exponents

The published general prefix identity is

    W_m=T_m+9d*floor((m+1)/3) modulo27.

For m=18 modulo27 it gives W_m=9 modulo27 at every width. The exact length formula gives D(m)=dm modulo3, so3 divides D(m). Therefore the cyclic modulus is divisible by27 and by37, since10 has order3 modulo37.

The rotation identity now gives R_(m,k)=9 modulo27 and

    R_(m,k)=10^D(k)*W_m modulo37.

Thus every rotation has exact3-adic valuation2 and normalized unit1 modulo3, and is a Q_3 square. Since10 is a square modulo37, the negative character of W_m at37 persists at every cut, ruling out integer squares. Any integer prime exponent must divide the3-adic valuation2, so no other exponent is possible. Every rotation is consequently an integer nonpower.

This argument needs neither even m nor odd d, unlike the13 construction. It is disjoint from the37 uniform-valuation-one certificate because here W_m is a nonzero37-adic unit; it may of course overlap other already known exclusions.

## 3. Class counts and an explicit union with13

For the two linear phases, the affine map modulo37 is bijective, so precisely18 residues have negative character. CRT with m=18 modulo27 gives18 classes modulo999.

In the quadratic phase, the character sum for nonzero discriminant is -(2/37)=1, with two or zero roots according as Delta is a square or nonsquare. The negative count is respectively17 or18. At zero discriminant the polynomial is one half times a square, and (2/37)=-1, giving36 negative values. This proves all counts and the error estimates by counting each class individually.

For odd widths, combine this certificate with ALL_ODD_WIDTH_THIRTEEN.md, retaining the same endpoint class m=18 modulo27. On even m the13 test succeeds on six of13 residues; on odd m only the37 test is used. Since2,13,27,37 are pairwise coprime, the union has exactly

    20*n_d+222 classes modulo25974=2*27*13*37,

where n_d=18 for the linear37 phases and is17,18,36 for the quadratic phase. The union count has width period222 when restricted to odd widths; the actual combined endpoint-class set can require the larger width period lcm(111,78)=2886. Equivalently its endpoint density is

    (10*n_d+111)/12987,

with absolute interval count error at most20*n_d+222. In particular at odd widths not divisible by3 this gives582 classes, density97/4329. This is an exact finite CRT union, not a heuristic independence assumption. The constants in both formulas may depend on d; that does not affect counting at distinct moduli.

At odd widths divisible by3, the additional old class m=8 modulo27 can be used separately. It is not included in the union count just stated, so it is not double-counted as new.

## 4. Scope and verification

The new contribution is the two linear37 phases and their effective all-width certificate, plus the exact union with the13 criterion. The older general mod27 identity,37 quadratic phase and three-width boundary translation are explicitly reused. This does not claim that the small endpoints were previously unknown or that every endpoint has been excluded. No compatibility with all local square tests is asserted. The global conjecture remains open and the main manuscript/PDF are unchanged.

The verifier checks all matrix phases, all width phases modulo111 for the37 criterion and all111 odd-width count phases modulo222 for the union (not every combined endpoint-class phase modulo2886), direct prefix residues through99999, selected larger prefixes, and all cuts at selected certified endpoints. Finite checks support the proof; they are not substituted for its uniform scope.

Run `python papers/A001292/verify_all_width_thirty_seven.py`. The standard-library verifier imports `prefix` from the sibling `verify_antiperiodic_thirteen.py`.

An additional independent scalar verifier, `verify_all_width_thirty_seven_independent.py`, checks1596 prefixes through width400, all1443 odd-width class phases, the exact count/class periods, and3357 literal integer rotations. It imports none of the primary verifier or its arithmetic helpers. Its file-location setting was adapted for the published sibling-file layout.
