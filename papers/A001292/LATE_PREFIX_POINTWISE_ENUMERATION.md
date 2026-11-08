# Effective pointwise square enumeration from the full prefix

This note gives a constructive characterization, not a new density estimate. For every cut, it enumerates at most eight explicit square-root candidates over a substantial endpoint interval, possibly crossing a decimal-width boundary. Every candidate is either rejected by its decimal length or determines exactly one endpoint for an exact equality test. A completed run can therefore certify absence for all endpoints in that interval without testing those endpoints individually.

The theorem does **not** prove that the resulting candidates always fail. The finite audit below is not promoted to infinite nonexistence. No literature-priority claim is made.

## 1. Setup and the inherited local fact

Let W_k be the concatenation 123...k and D(k) its decimal digit count. For k<m, move the complete prefix W_k to the end and denote the resulting integer by R_(m,k). Put

    U=W_k, s=D(k), E=D(m).

The exact identity is

    R_(m,k)=10^s W_m-(10^E-1)U,
    R_(m,k)=U (mod 10^s).                              (1)

The rotation begins with k+1, which has no leading zero. Consequently

    decimal_length(R_(m,k))=D(m).                       (2)

Fix k>=10. The full-prefix valuation lemma in `UNIFIED_FULL_PREFIX_FIXED_EXPONENT.md` proves, with w the decimal width of k, b=10^w and J=k(b-1)+b,

    v_p(U)=v_p(J)<s for p=2,5,
    U_(2,5):=2^v_2(U) 5^v_5(U) <= J < b^2.            (3)

No restriction that k or m be far from a width boundary is needed.

If either valuation is odd, (1) already excludes every square for this cut, at every endpoint m>k. Otherwise write

    v_2(U)=2a, v_5(U)=2c,
    z=2^a 5^c, H=10^s/z.                              (4)

The congruence y^2=U modulo 10^s is equivalent to y belonging to a set A_k of at most eight residue classes modulo H. Take their representatives in [0,H).

To construct A_k, solve the unit congruences

    u_2^2=U/2^(2a) (mod 2^(s-2a)),
    u_5^2=U/5^(2c) (mod 5^(s-2c)).                    (5)

A 2-adic unit congruence has at most four roots and a 5-adic one has at most two. The corresponding y classes are 2^a u_2 modulo 2^(s-a) and 5^c u_5 modulo 5^(s-c). Chinese remaindering these two coprime moduli gives A_k. Empty A_k excludes every endpoint, not merely a finite interval.

Conversely, every y in these compressed classes really satisfies (1)'s square congruence. In particular the compression is exact, not a necessary-condition approximation. The strict inequalities in (3) guarantee that the unit moduli in (5) have positive exponents.

## 2. Pointwise enumeration theorem

**Theorem.** Fix k>=10 that has no local obstruction. All square rotations with

    m>k, R_(m,k)<H^2                                  (6)

are obtained by this algorithm:

1. Construct A_k, of size at most eight.
2. For each r in A_k, form the integer r^2 and its decimal length e.
3. If e is not D(m) for an integer m>k, discard r.
4. Otherwise there is exactly one such m. Test the exact equality

       r^2=10^s W_m-(10^D(m)-1)U.                     (7)

Return precisely the successful pairs (m,k).

**Proof.** A square in (6) has positive root y<H. The full-prefix congruence forces y to equal one of the least representatives r, not a representative plus a positive multiple of H. Its square's digit length equals D(m) by (2). The function D is strictly increasing, so the endpoint is unique. Conversely, every equality (7) with m>k is exactly a square rotation, and r<H ensures (6). This proves necessity, sufficiency, and completeness.

Thus the work after root construction consists of at most eight digit-length checks and at most eight exact comparisons. It does not require a scan through endpoints, numerical square roots, floating-point logarithms, or binary search through the rotation values. The no-leading-zero observation is essential to direct endpoint recovery.

A certificate of absence consists of the complete modular root classes and, for each class, one of:

- its squared representative has a digit length outside the image of D;
- its uniquely determined endpoint is at most k;
- the exact unequal comparison in (7).

The roots can be reconstructed rather than stored as enormous decimal strings. The supplied verifier reconstructs them, verifies every square congruence, and records every branch disposition.

## 3. Exact endpoint inversion

For an endpoint of width d, write L=10^(d-1). Then

    t=D(L-1)=((9d-10)L+1)/9,
    D(m)=t+d(m-L+1),        L<=m<=10L-1.              (8)

Given a positive digit length e, find the unique width d for which

    t<e<=t+9dL.

Then e occurs as a concatenation length if and only if e-t is divisible by d. When it does,

    m=L+(e-t)/d-1.                                    (9)

Everything in (8)-(9) is integer arithmetic. The missing digit lengths at d>=2 provide a genuine filter before computing the candidate rotation.

## 4. A uniform, explicit endpoint region

Since z^2=U_(2,5)<10^(2w),

    H^2=10^(2s)/z^2 > 10^(2s-2w).                    (10)

Therefore every pair with

    k>=10, k<m, D(m)<=2D(k)-2w                       (11)

belongs to (6). This is a fully explicit, unbounded family of **search domains**, not an unbounded family already proved to have no squares. It includes endpoints across a decimal-width boundary. Roughly, its endpoint range is m up to 2k, with the precise digit-count condition handling all boundaries.

For any fixed k, the algorithm is complete on the larger, exact region (6), not just the sufficient region (11). At odd valuations or empty root classes, all m>k are excluded locally and there is no need to impose either region.

The last endpoint in the exact region is also computable without a scan. Put e=decimal_length(H^2-1), and let M_0 be the largest integer with D(M_0)<=e, using (8) and integer division. If D(M_0)<e, all of R_(M_0,k)'s digits fit strictly below H^2. If D(M_0)=e, compare R_(M_0,k) with H^2: retain M_0 if it is smaller, and otherwise decrement once. The interval is empty if the resulting endpoint is at most k. This observation describes the exact region but is not needed for candidate enumeration. For its rotation comparison, the only relevant case is M_0>k; if M_0<=k the interval is already empty.

### All remaining endpoints in one width

Let d>=2, B=10^d, L=B/10, and t=D(L-1). If k has width d and

    k >= ceil((11dL-t)/(2d)),                         (12)

then (11) holds for every k<m<=B-1. Indeed, using (8),

    2D(k)-D(B-1)>=2d

is exactly 2dk>=11dL-t. Thus at most eight explicit root candidates suffice to settle **all** remaining endpoints in this width for each such cut. The first thresholds are

    d=2: k>=53; d=3: k>=519; d=4: k>=5139.

The threshold tends to a fraction one half of B as d increases. Formula (12) is not a theorem that every one of these candidates is false.

## 5. An exact global extension, with a clear complexity boundary

For an arbitrary finite endpoint bound M>k, all positive square roots must have the form

    y=r+qH, r in A_k, q>=0,
    y^2<=R_(M,k).                                    (13)

The rotations increase strictly in m: their leading part is the concatenation (k+1)...m, which increases when the next integer is appended, and the trailing U is fixed. Thus (13) is a valid common upper bound. Enumerate the allowed q values and apply the same digit-length inversion and exact equality test. This gives a complete endpoint-free enumeration for every finite domain, not just (6).

However, the number of q values can be enormous for early cuts. Nothing here makes that general enumeration efficient. The useful bounded-work theorem is the q=0 region (6), where all candidates can actually be written down with at most eight branches. The full-prefix determinant theorem bounds how many true solutions lie outside this region but by itself does not locate them. No uniform interval-gap argument excluding those solutions is supplied here.

## 6. Relation to the exact-main-term obstacle

This argument never asks the archimedean leading coefficient to be a rational square. It therefore does not repeat the redundant local exclusion identified in `EXACT_MAIN_TERM_OBSTACLE.md`. At locally surviving cuts it uses the full modular roots, the *actual magnitude* of a possible integer square root, and the discrete set of possible full concatenation lengths.

It is an effective characterization of the remaining integer-square candidates, rather than another fixed-prime density or squareclass finiteness statement. It does not exclude odd prime powers and does not settle the full conjecture.

## 7. Implementation and finite audit

Run from this directory:

    python verify_late_prefix_candidates.py --max-cut 10000 --output late-prefix-10000-certificate.json

The standard-library implementation builds each prefix exactly, lifts unit roots by doubling their p-adic precision, combines compressed classes by CRT, obtains candidate endpoints from decimal lengths, and compares the exact integers. It never enumerates an enormous residue ring. It tests its root solver against exhaustive residue enumeration in 871 small unit-congruence cases. A separate small-domain audit uses integer square roots on all 3,554 pairs in the guaranteed region for cuts 10 through 99.

The completed run for every cut 10<=k<=10000 found:

- 9,991 cuts in total: 4,442 with odd local valuation, 4,861 with a unit obstruction, and 688 surviving the 2/5 tests.
- 5,504 compressed root branches at the surviving cuts.
- 3,830 digit-length-gap rejections and 1,674 exact candidate comparisons.
- No square in the audited exact regions R_(m,k)<H_k^2.
- 42,672,235 pairs in the guaranteed region k<m and D(m)<=2D(k)-2digits(k). Of these, 2,932,566 have cuts surviving the 2/5 tests.
- 369 locally surviving cuts whose guaranteed region crosses a decimal-width boundary.

The run completed in about 670 seconds. The cutwise dispositions are in `late-prefix-10000-certificate.json`; the compact counts and artifact hashes are in `late-prefix-10000-summary.json`. The smaller cut-1000 certificate was also independently reproduced: 65 locally surviving cuts, 520 branches, 329 digit-gap rejections, 191 exact comparisons, and no square. Its guaranteed region contains 406,544 pairs, including 26,623 at locally surviving cuts.

These are finite results only. The total covered pairs are not asserted to be newly excluded relative to earlier local results, and 2/5-local survival does not imply survival of every other previously studied local test. The independent review in `LATE_PREFIX_INDEPENDENT_AUDIT.md` verifies the proof and complete cut-1000 dispositions, and independently checks the cut-10000 local classification and coverage; it is not a second full cut-10000 root-enumeration run.
