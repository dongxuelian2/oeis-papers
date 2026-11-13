# Nearly complete Jacobi coverage in a surviving congruence class

This supplement combines the growing cyclotomic certificates, proves the required independence by CRT, and extends the admissible digit widths beyond powers of three. The conclusions are uniform in the remaining factor of the digit width. They do not resolve all endpoint classes or the full integer conjecture.

## Theorem

Let d be a decimal digit width, h=v_3(d), and q=3^h. Assume h>=2 and that d is a nonzero square modulo37. For every integer j>=2 define

    Q_j=(10^(2*3^(j-1))+10^(3^(j-1))+1)/3.

For each sufficiently large h, consider the indices

    max(2,ceil(h/2)) <= j <= h.

Among the d-digit endpoints m=666 modulo999, all but a proportion O(2^(-h/2)) have a negative Jacobi symbol (W_m/Q_j) for at least one of these j. The implicit constant is absolute; the estimate is uniform in d with the stated hypotheses.

Every such endpoint has an entire rotation block containing no nontrivial integer powers. All those rotations are nevertheless squares in Q_3 and Q_37. Every prime factor of every tested modulus is greater than 2 sqrt(q).

Equivalently, if H=9*10^(d-1), the number certified is

    H/999 * (1-O(2^(-h/2))).

The quantity on the right is an asymptotic lower bound as h tends to infinity, not a literal nonnegative bound with a specified constant for small h. Since the total number of endpoints in the congruence class is H/999+O(1), the conditional coverage tends to one.

The theorem includes d=3^h and the even digit widths d=4*3^h. More generally it applies whenever v_3(d) tends to infinity and d is a nonzero quadratic residue modulo37. It is not a natural-density assertion about all digit widths or all A001292 entries.

## 1. Moduli, eligibility and the two surviving local fields

The preceding CYCLOTOMIC_JACOBI_FAMILY.md proves the following facts for every j>=2: Q_j is coprime to30, is 3 modulo8, and every prime divisor of Q_j has multiplicative order exactly 3^j for10. Consequently all such primes exceed 2*3^j, and different Q_j have disjoint prime supports. In particular the Q_j are pairwise coprime, and each is coprime to999. Also (10/Q_j)=1.

For a d-digit endpoint,

    D(m)=d(m+1)-(10^d-1)/9.

LTE gives v_3((10^d-1)/9)=v_3(d)=h, so q divides D(m). As 3^j divides d and D(m) for j<=h, every Q_j in the theorem divides both 10^d-1 and 10^(D(m))-1.

For m=666 modulo999, the same prefix identities as in the preceding supplement give

    W_m=9 modulo27,       W_m=11d modulo37.

The first uses m=18 modulo27 and 3|d. Since 11 is a square modulo37 (14^2=11 modulo37), the hypothesis on d makes the second residue a nonzero square. The earlier equivalent identity 11=33/3 modulo37 also verifies this. Every rotation has 3-adic valuation exactly2 and normalized unit1 modulo3; it is thus a Q_3 square. Because 3 divides D(m), 37 divides the cyclic modulus, and 10 is a square modulo37, every rotation is a Q_37 square as well.

Any negative Jacobi symbol (W_m/Q_j) rules out squares for the entire block by the invariant (10/Q_j)=1. The exact 3-adic valuation2 then rules out all other prime exponents, exactly as in the preceding proof.

For j>=ceil(h/2), all prime divisors exceed 2*3^j>=2 sqrt(q). Thus these witnesses eventually lie outside every prescribed fixed finite prime set, even though d need not equal q.

## 2. A uniform negative-sign proportion

On a fixed width d, put L=10^(d-1). Since 10^d=1 modulo Q_j,

    W_m=f_j(m) modulo Q_j,
    f_j(T)=T(T+1)/2+c_j,
    c_j=W_(L-1)-L(L-1)/2 modulo Q_j.

The constants can depend on the entire digit width d. The character lemma in the preceding supplement is uniform in that constant, including degenerate discriminants.

Specifically, with P_j=2*3^j+1 and S_j=sum_{p|Q_j}1/p, it gives a negative proportion at least

    1/2-3/(2P_j)-2S_j.

All prime factors exceed 2*3^j and log Q_j <= (2/3)*3^j log10. Therefore

    S_j <= log10/(3j log3).

It follows, for j>=2, that

    3/(2P_j)+2S_j <= 2/j.

For an elementary numerical bound, use log10/log3<9/4 and 3/(4*3^j)<=1/(2j). Thus the fraction s_j of residues with symbol 0 or +1 is at most

    s_j <= 1/2+2/j.

We use this estimate only for sufficiently large j, when it is less than1. Zero symbols are explicitly included among the unexcluded residues.

## 3. Exact CRT independence, not a randomness assumption

Fix a digit width d. Although the constants c_j arise from the same prefix, each sign condition depends only on m modulo Q_j. Since the Q_j are pairwise coprime, the proportion failing all the selected negative-sign tests in a complete joint residue system is exactly

    product_{j=max(2,ceil(h/2))}^h s_j.

There is no probabilistic assumption about the coefficients or their correlation. This is an exact count of a Cartesian product under CRT. The additional condition m=666 modulo999 is also independent, because 999 is coprime to every Q_j.

Let J=ceil(h/2), for h large enough that J>=5. Then

    product_{j=J}^h s_j
       <= 2^(-(h-J+1)) product_{j=J}^h (1+4/j)
       = O(2^(-h/2)).

The product on the right is bounded absolutely: its logarithm is at most 4 sum_{j=J}^h 1/j=O(1). This proves the stated residual fraction in a full period.

## 4. A common period that fits inside the endpoint interval

A crude product bound would obscure the interval error. Instead the cyclotomic factors telescope:

    product_{j=2}^h Q_j
       =(10^q-1)/(999*3^(h-1)).

Hence all selected conditions, including the fixed endpoint congruence, have a common period dividing

    T=999 product_{j=2}^h Q_j
      =3(10^q-1)/q.

The number of unexcluded endpoints in an arbitrary d-digit interval is at most

    H/999 * O(2^(-h/2)) + T.

Since d>=q, we have T/H <= 10/(3q). Dividing the interval error by the congruence-class size H/999 gives O(3^(-h)), which is absorbed by O(2^(-h/2)). This proves the uniform theorem, even when d/q grows with h.

## 5. Scope and comparison

The earlier single-modulus theorem certified asymptotically at least half of the fixed endpoint class at widths d=3^h. The present union covers a proportion tending to one of that class, uses only moduli with prime factors tending to infinity, and applies also to suitable non-prime-power and even widths.

This is not a disguised reuse of a fixed37 nonsquare condition: all certified blocks are square blocks over Q_37. Nor does it claim that every endpoint in the class is eventually certified; an asymptotically small exceptional set may remain at every width.

Other endpoint classes, digit widths with bounded v_3(d), and widths failing the stated37 condition are not covered by this theorem. The global integer conjecture remains open.

## 6. Finite audit

The accompanying script checks exact Cartesian-product sign counts on independent small coprime moduli. At actual widths 9,27,36,81,108 it verifies the telescoping period and sign invariants, tests a fixed finite sample of congruence-class endpoints, and directly checks selected prefixes. These samples illustrate the union and the added even widths; they are not an estimate of its asymptotic success rate. The unbounded uniform claim is proved in Sections1–4. The main manuscript and PDF are unchanged.
