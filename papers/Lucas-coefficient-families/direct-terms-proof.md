# Direct terms for A191980–A191983

Let \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\). Index all four sequences from \(n=1\). The notation is \(S(i,j)=L_i-5L_j\), \(T(i,j)=5L_i-L_j\), and \(P(i,j)=5L_i+L_j\), with positive indices. Each of A191981, A191982, A191983 starts with zero.

The interval decompositions below give the exact ordered representations in every sufficiently large shell. Their lengths are linear functions of the shell index; their cumulative counts are quadratic. The resulting formulas use square-root index selectors and fixed-case Lucas expressions. 

## A191981

## Complete elementary proof

### 1. Admissible index pairs, independent of source's uniqueness proof

For i>=5,

    L_i - 5L_(i-4) = 3L_(i-5) > 0,
    L_i - 5L_(i-3) = 2(L_(i-4)-L_(i-3)) < 0.

Lucas numbers increase strictly from index 1 onward. Therefore admissible j are
exactly 1<=j<=i-4 for i>=5. The only earlier pair is (i,j)=(4,1), value2.
Within any fixed i, increasing values correspond to decreasing j, without repetitions.

### 2. Exact shell content

Let m>=11. All values of S in [L_(m-1),L_m) come from exactly these pairs:

    (m+2,m-2),
    (m,m-6), (m,m-7),
    (m+1,m-4),
    (m,m-8), (m,m-9), ..., (m,1).

This is also their strict increasing order. In particular the shell length is m-4.

To prove both assertions, put x=L_(m-8), y=L_(m-7). Thus x>0, y>x, and

    L_(m-1) = 8x+13y,
    L_m     =13x+21y,
    L_(m+1) =21x+34y,
    L_(m+2) =34x+55y.

The first five displayed values are

    A= 9x+15y = L_(m+2)-5L_(m-2) =3L_(m-3),
    B= 8x+16y = L_m-5L_(m-6),
    C=13x+16y = L_m-5L_(m-7),
    D=11x+19y = L_(m+1)-5L_(m-4),
    E= 8x+21y = L_m-5L_(m-8).

All strict increasing comparisons follow from

    A-L_(m-1)=x+2y>0,
    B-A=y-x>0,
    C-B=5x>0,
    D-C=3y-2x>0,
    E-D=2y-3x>0.

For the last inequality define z_t=2L_(t+1)-3L_t. It obeys the Lucas recurrence
in t, and z_3=2,z_4=1, so z_t>0 for all t>=3. Here t=m-8>=3.
The remaining values L_m-5L_j are increasing as j descends and always below L_m.

To exclude omitted pairs:

* i<=m-1: every value <L_(m-1).
* i=m: j<=m-6 gives the displayed B,C,E,...; j>=m-5 is below the shell, because
  L_m-5L_(m-5)=8x+11y < L_(m-1).
* i=m+1: its lowest point j=m-3 is 6x+9y < L_(m-1); j=m-4 is D;
  j<=m-5 is above the shell, because the smallest such value is
  16x+24y > L_m.
* i=m+2: j=m-2 is A; all j<=m-3 are above the shell, since the smallest
  such value is 19x+30y > L_m.
* i>=m+3: every positive value is at least 3L_(i-5)>=3L_(m-2)>L_m.
  The final strict inequality is
  3L_(m-2)-L_m=L_(m-2)-L_(m-3)>0.

This proves completeness and strict order. It also proves absence of all repeated
representations in these shells 

### 3. Initial count and inversion

The admissible region from step1 and the bound
3L_8=141>L_10=123 show that the values below L_10 are exhaustively obtained
from i<=12. Exact evaluation gives the 26-entry prefix above, including zero.
No value from later rows can enter it. Direct computation also verifies this finite
prefix has no duplicate positive values.

Thus the number of sequence entries below L_(m-1), for m>=11, is

    26 + sum_(h=11)^(m-1) (h-4)
      = 5 + (m-5)(m-4)/2.

For k=m-4, shell position r corresponds exactly to

    n = 5 + k(k-1)/2 + r,   1<=r<=k.

The inequalities T_(k-1)<n-5<=T_k invert to the radical formula for k.
Substituting m=k+4 into the shell list proves every branch of the formula.

Boundary check: the pre-shell count constant is 5. The n=27 case and the independent indexing checks verify this value.

## Four mod-5 subsequences: separately explicit

For i>=1, Lucas residues mod5 are 1,3,4,2, periodically. Therefore the four
positive residue subsequences of S correspond exactly to first indices i modulo4.
Their within-residue row blocks do not overlap: the minimum in row i+4 is
3L_(i-1)>L_i, whereas the maximum in row i is L_i-5. The exceptional row i=4
has value2 and precedes the first ordinary residue-2 row i=8, whose minimum is12.

Parameter c=1,2,3,4 corresponds respectively to residues 1,3,4,2.
The ordinary rows are i=4+c+4t, t>=0, and row t has length c+4t.
Let h be the positive rank in this ordinary-row subsequence. Define

    t = floor((sqrt((c-2)^2 + 8(h-1)) - (c-2))/4),
    q = h - (2t^2+(c-2)t),
    i = 4+c+4t,
    j = c+4t-q+1.

Then its h-th value is L_i-5L_j. This follows because the prefix length before
row t is Q(t)=2t^2+(c-2)t, and Q(t)<h<=Q(t+1).
For c=4, the full residue-2 subsequence starts with2; at its rank n>=2 use h=n-1.
For c=1,2,3 use h=n. This supplies the originally requested four-subsequence
structure, 

## A191982 and A191980

## 1. A191982: exact shell theorem

For every m>=4, the representations whose value lies in

    5L_(m-1) < x <= 5L_m

are precisely the following pairs, already in strictly increasing value order:

    (m+3,m+6), (m,m+1), (m+1,m+3),
    (m,m), (m,m-1), ..., (m,1).

Here a pair (i,j) means 5L_i-L_j. There are m+3 entries. Thus shell ordering itself proves uniqueness for all values above20.

### Exhaustiveness

For i=1 the positive j are1,2,3. For i>=2, positivity is equivalent to 1<=j<=i+3 and the minimum is

    5L_i-L_(i+3)=2L_(i-2).

This follows from checking 5L_i>L_(i+3) and 5L_i<L_(i+4) at i=2,3 and propagating by recurrence. For i<=m-1 the upper bound5L_i-1 is below the shell. For i>=m+4 the lower bound2L_(i-2)>=2L_(m+2)>5L_m is above it. Thus only rows i=m,m+1,m+2,m+3 matter. Strict monotonicity in j reduces their membership to a finite set of endpoint inequalities:

- i=m contributes j<=m+1; j=m+2 is already below the shell.
- i=m+1 contributes j=m+3; j=m+4 is below and j=m+2 above.
- i=m+2 contributes no j: j=m+5 is below and j=m+4 above.
- i=m+3 contributes j=m+6; j=m+5 is above.

All inequalities, and the strict order of the first three terms before the descending-j row tail, are the11 homogeneous fixed-shift Lucas expressions in `t_certificate(m)` in the companion script. Their values at m=4,5 are respectively

    (1,3), (3,9), (12,21), (2,6), (6,13), (8,14),
    (34,57), (2,1), (2,1), (2,6), (2,1).

Each expression satisfies h_(m+2)=h_(m+1)+h_m, so positivity at two consecutive bases proves it for **every** m>=4, not just tested m.

### Finite prefix and count

Values at most20 have i<=6, since i>=7 has minimum2L_5=22. Direct enumeration of i1..6 and j1..i+3 therefore proves the complete prefix, including the OEIS zero:

    0,1,2,4,6,8,9,11,12,13,14,16,17,19.

There are13 positive entries at most20. The cumulative positive count through shell m is

    C_T(m) = 13 + sum_(k=4)^m (k+3) = (m^2+7m-4)/2.

### Fully explicit nth term

For n1..14 use the literal prefix above. For n>=15 define

    m = ceil((sqrt(8n+57)-7)/2)
      = floor((sqrt(8n+49)-5)/2),
    r = n - (m^2+5m-8)/2.

Then1<=r<=m+3 and

| condition | a982(n) |
|---|---|
| r=1 | 2L_(m+1) |
| r=2 | 5L_m-L_(m+1) |
| r=3 | 5L_(m+1)-L_(m+3) |
| 4<=r<=m+3 | 5L_m-L_(m+4-r) |

Derivation: the shell's last OEIS index is1+C_T(m)=(m^2+7m-2)/2; solving that quadratic gives m. Its first local index is r=n-(1+C_T(m-1)). All inequality endpoints are included correctly: an equality at the quadratic bound gives the last entry of the shell, not the next shell.

## 2. A191980: exact shell theorem

For every m>=12, the representations in

    L_m <= x < L_(m+1)

are precisely:

- (i,m), 1<=i<=m-5;
- (m-3,j), 1<=j<=m-2;
- (m-5,m-1), (m-4,m-2), (m-4,m-1).

A pair now means5L_i+L_j. Their strict order is

    (i,m), i=1,...,m-9;
    (m-5,m-1);
    (m-8,m);
    (m-4,m-2);
    (m-7,m);
    (m-3,j), j=1,...,m-5;
    (m-6,m);
    (m-3,m-4);
    (m-4,m-1);
    (m-3,m-3);
    (m-5,m);
    (m-3,m-2).

There are(m-9)+4+(m-5)+6=2m-4 entries. In particular all these large sums are unique, independently of the source's collision theorem.

### Exhaustiveness

A value in the shell must have j<=m, because L_j>=L_(m+1) otherwise. It must have i<=m-3 since5L_(m-2)>L_(m+1). Now partition this rectangle:

1. If j=m, the upper-shell condition is5L_i<L_(m-1). The inequalities5L_(m-5)<L_(m-1)<5L_(m-4) give i<=m-5.
2. If i=m-3, its value is already>L_m. The inequalities
   5L_(m-3)+L_(m-2)<L_(m+1)<5L_(m-3)+L_(m-1)
   give j<=m-2.
3. In the remaining rectangle i<=m-4,j<=m-1, any i<=m-6 is excluded by5L_(m-6)+L_(m-1)<L_m. If i=m-5, only j=m-1 lies above L_m. If i=m-4, precisely j=m-2,m-1 lie above L_m. The three surviving sums are all below L_(m+1).

The13 homogeneous expressions proving these claims are explicitly listed in `p_certificate(m)`. Their pairs of base values at m=12,13 are

    (94,152), (54,87), (36,58), (58,94), (18,29),
    (58,94), (33,54), (54,87), (22,36), (177,286),
    (11,18), (36,58), (87,141).

For strict sorting, both growing runs are ordered by monotonicity. Their bridges and the single terms are verified by11 further expressions in the same script. At m=12,13 the pairs are

    (2,1), (13,19), (1,3), (19,32), (3,4), (3,4),
    (15,25), (7,11), (22,36), (11,18), (36,58).

One bridge compares5L_(m-7)+L_m with5L_(m-3)+L_1. The listed expression omits the positive L_1 and is already positive, so the required strict comparison follows. Every listed expression is homogeneous in shifted Lucas numbers and therefore obeys the ordinary recurrence; its two positive base cases prove all subsequent cases.

### Prefix and count

Below L_12=322, every pair has i<=8 and j<=11. The finite rectangle therefore gives a complete prefix,  Its80 distinct terms are

    6,8,9,12,16,18,19,21,22,23,24,26,27,31,33,34,36,38,39,42,
    44,46,49,52,53,56,58,59,62,64,66,67,73,81,82,84,91,93,94,96,
    97,101,102,108,111,119,128,131,137,138,143,146,148,149,152,156,
    158,163,166,174,178,192,204,213,214,219,221,234,236,238,239,
    242,246,253,254,264,268,282,289,311.

The cumulative count through shell m is

    C_P(m)=80+sum_(k=12)^m (2k-4)=m^2-3m-8.

### Fully explicit nth term

For n1..80 use the fixed prefix. For n>=81 define

    m = ceil((3+sqrt(4n+41))/2)
      = floor((5+sqrt(4n+37))/2),
    r = n-m^2+5m+4.

Then1<=r<=2m-4. The term is5L_i+L_j with(i,j) from this fixed table:

| condition on r | i | j |
|---|---:|---:|
| 1<=r<=m-9 | r | m |
| r=m-8 | m-5 | m-1 |
| r=m-7 | m-8 | m |
| r=m-6 | m-4 | m-2 |
| r=m-5 | m-7 | m |
| m-4<=r<=2m-10 | m-3 | r-m+5 |
| r=2m-9 | m-6 | m |
| r=2m-8 | m-3 | m-4 |
| r=2m-7 | m-4 | m-1 |
| r=2m-6 | m-3 | m-3 |
| r=2m-5 | m-5 | m |
| r=2m-4 | m-3 | m-2 |

The two intervals are nonempty at m=12 and all larger m; no case overlaps. Solving n<=C_P(m) yields m, and r=n-C_P(m-1) gives the local index.

## A191983

## Explicit nth term

For n<=56 use the fixed prefix in `proof_checks/verify_union.py` (also displayed below).
For n>=57 set

    m = 3 + floor(sqrt(n-8)),
    r = n - ((m-3)^2+7).

Then 1<=r<=2m-5 and m>=10. The term is the following fixed-case expression:

| r | term |
|---|---|
| 1<=r<=m-4 | 5L_(m-3)-L_(m-3-r) |
| m-3 | 2L_(m-1) |
| m-2 | 5L_(m-2)-L_(m-1) |
| m-1 | L_(m+1)-5L_(m-6) |
| m | L_(m+2)-5L_(m-3) |
| m+1 | L_(m+1)-5L_(m-7) |
| m+2 | 5L_(m-1)-L_(m+1) |
| m+3 | L_(m+1)-5L_(m-8) |
| m+4 | 4L_(m-2) |
| m+5<=r<=2m-5 | L_(m+1)-5L_(2m-4-r) |

Replacing L_j by phi^j+(-phi)^(-j), phi=(1+sqrt(5))/2, makes it an elementary
radical/power/floor expression with a fixed finite number of cases.

Prefix n=1..56:

    0,1,2,3,4,6,8,9,11,12,13,14,16,17,19,21,22,24,26,27,
    28,31,32,33,34,36,37,41,42,43,44,48,51,52,54,56,58,61,
    68,69,71,72,79,83,86,87,88,89,94,98,103,108,109,112,116,118.

## Proof structure, independent of the general coefficient theorem

### Admissible representations

S-positive pairs are (4,1), or i>=5 and 1<=j<=i-4. This follows from
L_i-5L_(i-4)=3L_(i-5)>0 and 5L_(i-3)-L_i=2L_(i-5)>0,
with the few small indices checked directly. For T, i=1 permits j=1,2,3;
for i>=2 precisely 1<=j<=i+3 is permitted, since
5L_i-L_(i+3)=2L_(i-2)>0 and L_(i+4)-5L_i=3L_(i-1)>0.
These are two-initial-value recurrence identities.

### Complete T shell

For m>=10 consider [L_m,L_(m+1)). The least positive T in row i>=2 is
2L_(i-2); the largest is 5L_i-1. Thus i<=m-4 and i>=m+2 are impossible:
5L_(m-4)<L_m and 2L_m>L_(m+1). Check the five remaining rows:

| i | admitted j in this shell |
|---|---|
| m-3 | 1,...,m-4 |
| m-2 | m-2,m-1 |
| m-1 | m+1 |
| m | none |
| m+1 | m+4 |

The function T(i,j) decreases strictly in j. Therefore to prove a row of
this table it suffices to compare its two proposed endpoints and immediate
neighbors with the two shell endpoints. Every such comparison is a
fixed-shift linear combination of Lucas numbers. `cert(m)` in
`proof_checks/verify_union.py` gives all 19 needed inequalities. Each is strictly
positive at m=10 and m=11, so the Lucas recurrence proves it for every
m>=10. The actual two initial values are in `verification-results.txt`.
This proves *exhaustiveness*, 

### Complete S shell and merging

The independent S notes prove that [L_m,L_(m+1)), m>=10, consists exactly of

    S(m+3,m-1), S(m+1,m-5), S(m+1,m-6), S(m+2,m-3),
    S(m+1,j) for j=m-7,m-8,...,1,

in this order. 
The first two values already occur in the long T row, by the exact identities

    S(m+3,m-1) = T(m-3,m-7),
    S(m+1,m-5) = T(m-3,m-9).

For m>=10 both displayed T indices are positive. The remaining values
merge in precisely the order of the nth-term table: a T run of length
m-4, eight fixed entries, and an S run of length m-9. Within each run,
strict ordering follows from Lucas monotonicity. For the eight fixed
entries, all seven neighbor differences are Lucas-linear functions of m,
positive at 10 and11. The T-run-to-fixed boundary follows from
2L_(m-1)>5L_(m-3); the fixed-to-S-run boundary is also Lucas-linear,
positive at 10 and11. The first and last values lie within the shell by
the endpoint comparisons. Thus the resulting list is strictly increasing;
there can be no further coincidences or omissions. This independently
proves that exactly two S/T overlaps occur in each of these shells.

### Counts and inversion

The shell length is (m-4)+8+(m-9)=2m-5. Direct finite enumeration gives
56 entries including zero below L_10=123. This finite check is complete:
for S below123 the first index cannot exceed12, and for T it cannot
exceed10, by the least-positive-row bounds above. Consequently the number
of entries including zero below L_m is

    56 + sum_(h=10)^(m-1) (2h-5) = (m-3)^2+7.

The inequalities (m-3)^2+7<n<=(m-2)^2+7 yield exactly
m=3+floor(sqrt(n-8)); r subtracts the count below the shell. The sum is
used only in the proof, not in the nth-term formula.

## Exact inequality checks

The companion programs [A191981](proof_checks/check_s_formula.py), [A191980/A191982](proof_checks/check_t_p.py), and [A191983](proof_checks/verify_union.py) evaluate the fixed-shift Lucas inequalities and verify complete ordered intervals. Every stated inequality is propagated from two consecutive positive initial values by the Lucas recurrence.
