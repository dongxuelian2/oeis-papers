# Exact valuation-three Q_3-cube blocks at small width periods

This supplement classifies one specific local block type: every rotation has3-adic valuation exactly3 and is a cube in Q_3. It then supplies integer nonpower certificates inside that type using37. The classification is not a classification of all local cubes, all valuations, or integer powers.

## 1. A three-cut equivalence

Let m>=3, W=W_m, D=D(m), Delta=10^D-1. Every whole-block rotation has valuation exactly3 and is a Q_3 cube if and only if

    W=27 or216 modulo243,
    Delta=0 modulo243.

Equivalently the second condition is27|D. This follows from v_3(10^D-1)=2+v_3(D).

For sufficiency, write the normalized rotation as

    10^(-D(k))*R_(m,k)=W-Delta*X_k,
    X_k=10^(-D(k))*W_k in Z_3.

Division by27 preserves the unit±1 modulo9, while10^D(k)=1 modulo9. Every valuation is3 and every normalized unit is±1 modulo9, exactly the Q_3 cube condition.

For necessity, cut0 gives W/27=u with u=±1 modulo9. If v_3(Delta)<3, cut1 has valuation less than3, a contradiction. Otherwise set a=Delta/27. If v_3(Delta)=3, a is a unit; cut2 has X_2=12*10^(-2)=3 modulo9, so its normalized unit is u-3a, which is neither1 nor-1 modulo9. If v_3(Delta)=4, use X_1=10^(-1)=1 modulo9 instead: u-a again differs from u by3 or6 and cannot be±1. Thus v_3(Delta)>=5 is necessary. Only cuts0,1,2 are needed for the reverse implication.

The same proof gives a general common-valuation criterion: for any positive b divisible by3, every rotation has exact valuation b and is a Q_3 cube if and only if W/3^b is a unit congruent to±1 modulo9 and v_3(Delta)>=b+2. Replace27 by3^b in the normalized-cut argument. This is an equivalence at any specified common valuation, but the explicit width/endpoint table below is only for b=3. For b not a power of3, additional prime exponents may divide b, so a37 noncube condition alone need not exclude every integer power.

## 2. Complete finite-period classification

For d-digit endpoints with d>=2, the equivalence gives the following complete table of allowed residues m modulo243. The row depends only on d modulo27:

    d mod27              allowed m mod243
    0                    53,54,188,189
    1,10,19              27,216
    3,12,21              108,216
    4,13,22              54,108
    6,15,24              27,135
    7,16,25              135,189
    9,18                 54,189
    2,5,8,11,14,17,20,23,26    none

The classes are to be intersected with the actual d-digit interval. Thus d=2 has no block of this particular local type; this says nothing about other valuations or individual local cubes. The rows with d=1 modulo3 include v_3(d)=0, and the rows at d=3 or6 modulo9 include v_3(d)=1.

Here is the exact finite proof of the table's unbounded periodicity. Work modulo243 and use the append matrix

    A_d=[[10^d,1,0],[0,1,1],[0,0,1]].

For all27 phases d modulo27, exact multiplication gives A_d^243=I. The phase count is complete because10 has order27 modulo243. The initial endpoint10^(d-1), complete-block length9*10^(d-1), and A_d all repeat modulo243 with width period27. Thus the full-block maps F_d repeat every27 widths.

Exact composition gives F_27 composed with ... composed with F_1 equal to the identity as a map of the initial prefix modulo243: its multiplier is1 and its translation is0. Consequently V_(d+27)=V_d modulo243, where V_d=W_(10^d-1), including V_0=0. Combining these facts, the prefix residue at any endpoint depends only on d modulo27 and m modulo243. Computing it by A_d raised to (m-10^(d-1)+1) modulo243 is valid because of the matrix period.

The digit-count residue is also periodic in those coordinates:

    D(m)=d(m+1)-(10^d-1)/9 modulo27.

The repunit term is obtained by taking10^d modulo243, subtracting1, and dividing by9; the chosen residue is1 modulo9, so this division gives the correct residue modulo27. Checking all27*243 pairs against the two conditions in Section1 gives exactly the displayed table. The accompanying standard-library verifier performs every finite phase and pair check. No finite endpoint experiment is used to infer the period.

## 3. Integer exclusion by the cubic character at37

At every endpoint in the table,27 divides D, so37 divides the cyclic modulus. The number10 is a cube modulo37. Thus the cubic residue class of W_m modulo37 persists at every rotation. If W_m is a nonzero noncube modulo37, every rotation is an integer nonpower: its valuation3 permits only the prime exponent3, which the37 character excludes. All these rotations remain Q_3 cubes and are not Q_3 squares.

The previously proved all-width37 prefix formulas apply. For d=1+3a the listed endpoints are multiples of3 and

    W_m=4m+33a modulo37.

For3|d, the inherited formula is W_m=T_m+11d modulo37. The missing d=2 modulo3 row needs no37 test.

Let H=9*10^(d-1). At d=1 modulo3 there are two endpoint classes modulo243. The affine37 map has24 nonzero noncube residues, so CRT gives exactly48 sufficient classes modulo8991=243*37. The number of endpoints certified by these conditions differs from

    (16/2997)*H

by at most48. This is effective from the small widths, including d=4, without a growing v_3(d) hypothesis or enormous width period.

For3|d, let n_(d mod37) be the exact noncube count in CUBIC_LOCAL_SURVIVORS.md, with20<=n<=28. If27 does not divide d there are two local classes, giving2n classes modulo8991. If27 divides d there are four, giving4n classes. The corresponding interval count differs from its residue density times H by at most the number of classes.

These are sufficient global certificates inside an exactly classified local type. A failed37 condition does not establish an integer power or exhaust all other possible obstructions.

## 4. Novelty and scope

The cube criterion at3, append matrices and37 character invariance are standard or already used in preceding supplements. The new contribution relative to those materials is the necessity argument using three cuts, the complete small-period table for exact valuation3 Q_3-cube blocks, and its effective integer exclusions at v_3(d)=0,1,2 as well as larger valuations. The row d=0 modulo27 overlaps the earlier b=3 family and is not counted as a separate discovery.

There is no claim of literature priority or a full solution to the integer conjecture. No statement that all Q_3-cube blocks have valuation3 is made. The main manuscript/PDF are unchanged.

## 5. Verification

The verifier checks all27 matrix phases, the full boundary-cycle map, all6561 table cells, and direct prefix/length conditions at every endpoint through99999. It checks selected integer-nonpower endpoints at widths3,4,6 by all available cuts modulo243 and37. The local equivalence and periodicity extend the finite table to all widths.

Run `python papers/A001292/verify_fixed_valuation_cubic.py`; the verifier imports the published sibling matrix helpers from `verify_antiperiodic_thirteen.py`. Separated audit copies need that directory on PYTHONPATH.

The additional independent scalar verifier `verify_fixed_valuation_cubic_independent.py` checks90 state-period cases, all6561 local cells, the full boundary cycle, normalized three-cut congruences, all999 combined width count phases and49284 modulo37 prefix phase values. Its certificate path was adapted to the published sibling-file layout.
