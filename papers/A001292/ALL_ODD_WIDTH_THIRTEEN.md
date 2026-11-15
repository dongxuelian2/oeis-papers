# A13 certificate at every odd digit width, including v_3(d)=0

This extends ANTIPERIODIC_THIRTEEN.md beyond widths divisible by3. The new contribution combines three explicit linear phases modulo13 with the already published mod27 prefix identity valid at every width (main.tex and RESIDUE_EXCLUSIONS.md). That identity and existing six-width translations are reused and reproved or reverified, not claimed as new.

## Theorem

Let d>=3 be any odd decimal digit width. Write d=s+6a, with s in {1,3,5}. Define coefficients modulo13 by

    s=1: alpha=10, c=5a;
    s=3: alpha=7,  c=5a+5;
    s=5: alpha=4,  c=5a+11.

Let N={2,5,6,7,8,11}, the quadratic nonresidues modulo13. Every d-digit endpoint satisfying

    m=18 modulo27,
    m even,
    alpha*m+c modulo13 in N

has an entire block of integer nonpowers. All its rotations are squares over Q_3 and nonsquare units over Q_13.

There are exactly six allowed residue classes modulo702 at every such width. If H=9*10^(d-1), the certified endpoint count differs from H/117 by at most6. This is a sufficient criterion, not a classification of all endpoints. It starts in small widths and requires no large width threshold.

For d=3 modulo6 the previous extra class m=8 modulo27 remains available and gives the earlier total12 classes modulo702; this is not recounted as new. The genuinely added width phases are d=1 or5 modulo6, which have v_3(d)=0. No even-width assertion is made, and the global integer conjecture remains open.

## 1. A mod27 identity without a hypothesis on v_3(d)

For every positive endpoint m of width d,

    W_m=T_m+9d*floor((m+1)/3) modulo27.

Here T_m=m(m+1)/2. A direct induction proves the formula. Within a width,10^d=1+9d modulo27 and the proposed formula at m-1 gives

    W_m=T_m+9d*[floor(m/3)+T_(m-1)] modulo27.

Modulo3, T_(m-1) is1 exactly when m=2 modulo3 and otherwise0. This equals floor((m+1)/3)-floor(m/3), proving the step.

At a width transition m=10^(d-1), the old expression used d-1 instead of d. The resulting correction is9*floor(m/3). Since10^(d-1)=1 modulo9, floor(m/3)=(m-1)/3 is divisible by3, so the correction vanishes modulo27. The base m=1 is immediate. This proves the formula at all widths.

For m=18 modulo27, T_m=9 modulo27 and floor((m+1)/3)=6 modulo9. Thus W_m=9 modulo27 for every d, including d coprime to3.

The digit count is

    D(m)=d(m+1)-(10^d-1)/9.

Its residue modulo3 is dm, since (10^d-1)/9 is the sum of d powers of10 and equals d modulo3. Therefore3 divides D(m) for the stated endpoint class. For odd d its parity is m, because the repunit term is odd. With m even this gives6|D(m).

In particular the cyclic modulus10^D(m)-1 is divisible by27. The rotation identity yields

    R_(m,k)=10^D(k)*W_m=9 modulo27.

So every rotation has exact3-adic valuation2 and normalized unit1 modulo3, hence is a Q_3 square. Any integer prime-power exponent must be2.

## 2. Linear phases modulo13

Let B=10^d modulo13. At odd widths B is respectively10,-1,4 as d is1,3,5 modulo6. In particular B!=1 and B^6=1. Appending six integers gives, for same-width endpoints,

    W_(m+6)=W_m+6/(1-B) modulo13.

Indeed the coefficient of W_m is B^6=1, the coefficient of m is the geometric sum1+B+...+B^5=0, and the remaining weighted sum is6/(1-B). Thus along m=0 modulo6, W_m is affine with slope alpha=(1-B)^(-1), giving10,7,4 in the three phases.

For d>=3 let L=10^(d-1). Its residue modulo6 is4, so the first endpoint divisible by6 is L+2. Appending those first three integers multiplies V_(d-1) by B^3=-1. On increasing d by6, the previously proved exact boundary recurrence gives

    V_(d+5)=V_(d-1)+8 modulo13.

All other initial residues, including L modulo78, repeat. Consequently the affine constant satisfies c_(d+6)=c_d-8=c_d+5 modulo13.

The base constants at widths3,5,7 are5,11,5 respectively, obtained by exact matrix concatenation (or direct geometric sums). These establish the displayed formulas for every d>=3. The phase1 formula also agrees with the single width1 endpoint divisible by6 (m=6), but no new width1 certificate is asserted here.

Our endpoints are divisible by3 and are even, hence are0 modulo6. Therefore W_m=alpha*m+c modulo13 applies. Because6 divides D(m),13 divides the cyclic modulus. The number10 is a square modulo13, so every rotation has the same Legendre symbol at13 as W_m. The required negative sign excludes squares, and the valuation2 conclusion above excludes every other integer prime exponent. This proves the theorem.

## 3. Exact finite classes and scope

The combined constraints m=18 modulo27 and m even form one residue class modulo54. Since gcd(54,13)=1 and alpha is a unit modulo13, precisely six residues modulo13 give the required nonresidue value. CRT gives exactly six classes modulo702. Counting each class in the endpoint interval incurs error at most1, proving the error bound6.

The digit-width coefficients repeat modulo78. No new claim of an unbounded supply of witness primes is involved:13 is the only additional prime. Unlike the previous high-v_3(d) and fixed-v_3(d)=1 constructions, this includes odd widths with no3 factor. It is a new combined certificate, not a claim that the underlying local conditions themselves are new or that small endpoints escaped prior computational verification. The old13-adic common-valuation-one family remains disjoint, because the present endpoints are nonzero units modulo13.

Nothing here proves that the omitted endpoint classes or even widths contain integer powers. No compatibility with the Q_37 square test is claimed. The main manuscript and PDF remain unchanged.

## 4. Finite audit

The script checks all39 odd width phases modulo78, the general mod27 identity at every endpoint through99999, every even endpoint divisible by3 in the relevant odd widths1,3,5, and selected prefixes at larger widths. It then checks every available cut for all three-digit endpoints selected by this criterion and three selected five-digit endpoints, using exact modular rotation arithmetic. These checks do not substitute for the unbounded proof or claim that every rotation at every width was enumerated.

Run `python papers/A001292/verify_all_odd_width_thirteen.py`. The standard-library script imports the sibling `verify_antiperiodic_thirteen.py` matrix-prefix routine; separated copies need that directory on PYTHONPATH.
