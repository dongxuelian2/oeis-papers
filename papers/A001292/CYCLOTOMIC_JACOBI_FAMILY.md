# An infinite family of growing-modulus Jacobi block certificates

This supplement proves an infinite family by character counting, not by extrapolating the finite endpoint scan. Its certified blocks pass the square tests over both Q_3 and Q_37. The obstruction is supplied by a modulus whose every prime factor exceeds twice the endpoint digit width.

## Theorem

Let h>=2, d=3^h, x=10^(d/3), and

    Q_h=(x^2+x+1)/3.

Among the d-digit endpoint indices m, at least

    (1/1998-o(1)) * 9*10^(d-1)

satisfy both

    m=666 modulo999,       (W_m/Q_h)=-1,

as h tends to infinity. The parentheses denote the Jacobi symbol. Every rotation belonging to every such endpoint is an integer nonpower, while all those rotations are squares in Q_3 and in Q_37.

Every prime divisor of Q_h is greater than 2d. In fact it has multiplicative order d for 10. Consequently these moduli eventually avoid every prescribed finite set of primes. This does not assert that the candidates pass all tests at that finite set; the two specified local fields Q_3 and Q_37 are the ones proved to admit squares.

The lower bound is within each of the indicated digit-width blocks, not a natural-density statement over all endpoints or sequence entries. It guarantees infinitely many certified endpoint blocks. It is not an equivalent classification, and Kashihara's conjecture remains open.

## 1. The modulus and its prime factors

The identity x^3-1=(x-1)(x^2+x+1) and LTE give

    v_3(x^2+x+1)=1.

Thus Q_h is an integer coprime to3. It is also coprime to10. If p divides Q_h, then x^3=1 modulo p but x is not 1 modulo p: otherwise p would divide3. Since d is a power of3, it follows that

    ord_p(10)=d.

Hence d divides p-1, and the odd prime p satisfies p>=2d+1. This argument applies to every prime divisor, regardless of its multiplicity in Q_h.

Because d/3>=3, x is divisible by8. Therefore

    Q_h=3 modulo8,       Q_h=2 modulo5.

In particular Q_h is not a square. The supplementary laws and quadratic reciprocity yield

    (2/Q_h)=-1,       (10/Q_h)=(2/Q_h)(5/Q_h)=1.

The same conclusion for 10 follows from its odd order at every prime divisor.

## 2. The cyclic modulus and the local conditions

For a d-digit endpoint m, its total decimal length is

    D(m)=d(m+1)-(10^d-1)/9.

Since d=3^h and v_3((10^d-1)/9)=h, we have d|D(m). Thus Q_h divides 10^(D(m))-1, and v_3(10^(D(m))-1) is at least h+2>2. The modulus Q_h itself is coprime to3.

The elementary prefix congruence is

    W_m=m(m+1)/2+9d floor((m+1)/3) modulo27.

One proof expands each decimal multiplier as 10^j=1+9j modulo27. The linear correction is 9 times the sum of digit lengths at indices equal to2 modulo3; complete earlier width intervals contribute zero modulo3. This gives the displayed formula. As 3|d, it simplifies to W_m=m(m+1)/2 modulo27.

The condition m=666 modulo999 implies m=18 modulo27, so W_m=9 modulo27. Every rotation therefore has 3-adic valuation exactly2 and normalized unit 1 modulo3. All rotations are Q_3 squares, and any integer prime-power exponent would have to be2.

The existing 37-prefix identity, valid when 3 divides d, is

    W_m=m(m+1)/2+11d modulo37.

For clarity, it can be verified independently by summing complete digit-width blocks: their multipliers are1 modulo37; the three successive block contributions repeat as 36,26,8, with sum33. Thus the complete d-width boundary is 33(d/3), and removing its tail gives the stated identity.

Our endpoint condition also gives m=0 modulo37. Consequently

    W_m=33*3^(h-1) modulo37.

This is a nonzero square, since 33=12^2 and 3=15^2 modulo37. Also 10=11^2 modulo37 and 3|D(m), so every rotation is a nonzero square modulo37 and hence a square in Q_37. These blocks are not excluded by either of those two local square tests.

## 3. Negative quadratic characters on a full residue system

Put B=10^d and L=10^(d-1). Since B=1 modulo Q_h, the usual recurrence gives, throughout this digit interval,

    W_m=f(m) modulo Q_h,
    f(T)=T(T+1)/2+c_d,
    c_d=W_(L-1)-L(L-1)/2 modulo Q_h.

We prove uniformly in this constant c_d that the proportion of residue classes t modulo Q_h with (f(t)/Q_h)=-1 is at least

    1/2-O(1/log d).

All prime divisors of Q_h are at least P=2d+1. If S is the sum of their reciprocals, then

    S <= log Q_h/(P log P) = O(1/log d).

Indeed their number is at most log Q_h/log P. The proportion of classes where f is nonzero at every prime divisor is at least product_p(1-2/p)>=1-2S.

Write the factorization of Q_h formally as product p^e_p, without assuming a factorization is computationally available. The Jacobi character depends on the Legendre characters for odd e_p, together with the requirement that f be nonzero at all prime divisors.

If some p with odd e_p does not divide the discriminant of f, the standard quadratic-character sum is

    sum_{t modulo p} (f(t)/p)=-(2/p).

Together with at most two roots, this implies at least (p-3)/2 classes with each sign. Fix any nonzero choices at all other prime divisors and choose the sign at this p to make the full product negative. CRT, including the unrestricted lifts to prime powers, gives a negative proportion at least

    (1/2-3/(2p)) product_{q!=p}(1-2/q)
       >= 1/2-3/(2P)-2S.

If instead every odd-exponent prime divides the discriminant, at each such prime f is one half times a square after translation. On the nonzero classes its full Jacobi symbol is therefore

    (1/2 / Q_h)=(2/Q_h)=-1.

Even-exponent primes contribute +1 on their nonzero classes. In this case the negative proportion is at least 1-2S, which is also at least 1/2-3/(2P)-2S. These two cases prove the uniform bound, without any assumption that the discriminant is nonzero at a particular unknown factor.

## 4. Passing to actual endpoints

No prime factor of Q_h is3, and none is37 since its order would then be3 rather than d>=9. Hence gcd(Q_h,999)=1. Combining m=666 modulo999 with each negative-character class gives density at least

    (1/999)(1/2-O(1/log d))

in a period 999Q_h. In the actual interval [10^(d-1),10^d-1], whose length is H=9*10^(d-1), the count is at least H times that density minus 999Q_h. But Q_h is asymptotic to 10^(2d/3)/3, so the period error is o(H). This proves the theorem's lower count.

For any counted m, divide the rotation identity by9. Since Q_h is coprime to3 and divides 10^(D(m))-1, we have

    R_(m,k)/9 = 10^(D(k)) W_m/9 modulo Q_h.

The Jacobi symbol of 9 is1, and that of10 is1. Thus every normalized rotation has Jacobi symbol -1 and cannot be an integer square. Its 3-adic valuation is exactly2, so it cannot be any nontrivial integer power. This proves the whole-block conclusion.

## 5. Relation to earlier families and limitations

The main manuscript already gives fixed-37-character exclusion families. They are not being renamed as new results here: every block in the present family is a Q_37 square block, whereas its negative-character witness comes from primes of order d, all exceeding2d. The moduli and their prime supports grow without bound.

The proof does not establish the sign for every endpoint m=666 modulo999; it proves that many such endpoints have the required sign. It also does not assert that all integers satisfying the Jacobi condition are powers locally at every small prime. These distinctions avoid turning a sufficient certificate or a finite numerical pattern into a full classification.

The accompanying finite audit checks 40 quadratic-character cases on small moduli. For h=2 it enumerates the 333667 modulus classes and all 900901 endpoints satisfying the fixed congruence in the nine-digit interval, obtaining 450764 certificates. It then checks exact prefix residues at ten selected certified endpoints for each of h=2,3,4, totaling 30 selected prefix checks; it does not enumerate all endpoints for h=3,4 or individually check every rotation. Its samples do not prove the infinite assertion, which follows from Sections 1–4. The main manuscript and PDF are unchanged.
