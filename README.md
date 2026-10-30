# OEIS papers

Mathematical papers and research notes, ordered by OEIS sequence number. Each entry retains the sequence's OEIS description and briefly states the mathematical result established by its accompanying manuscript. Sequences treated in the same paper are grouped together.

- **[A001040 / A001053](papers/A001040-A001053/)**
  - [A001040](https://oeis.org/A001040): a(n+1) = n*a(n) + a(n-1) with a(0)=0, a(1)=1.
  - [A001053](https://oeis.org/A001053): a(n+1) = n*a(n) + a(n-1) with a(0)=1, a(1)=0.
  - **Result:** We proved Kurkov's endpoint-refined rook-tour conjectures for every positive board size: the numbers of directed Hamilton tours with endpoints in opposite and equal columns are respectively `2*n!*A001040(n)` and `2*n!*A001053(n)`.

- **[A003630](papers/A003630/)**
  - [A003630](https://oeis.org/A003630): Inert rational primes in Q[sqrt(3)].
  - **Result:** We proved that the conjectured prime-ordered Euler product converges to `sqrt(3)/2`, with an exact finite-product identity and the exceptional factors at 2 and 3.

- **[A005046](papers/A005046/)**
  - [A005046](https://oeis.org/A005046): Number of partitions of a 2n-set into even blocks.
  - **Result:** We proved eventual periodicity modulo every positive integer and the Bessel-moment formula for all indices. Modulo 10, the block `(1,4,1,9,6,9)` repeats from index 1.

- **[A006063 / A096680 / A096904](papers/A006063/)**
  - [A006063](https://oeis.org/A006063): Values of n admitting a permutation of 1, ..., n such that i + p_i is a cube for every i.
  - [A096680](https://oeis.org/A096680): Values of n admitting more than one such cube-sum permutation.
  - [A096904](https://oeis.org/A096904): Number of such permutations for each n.
  - **Result:** We proved the exact existence classification of cube-sum permutations: `P(n)>0` for every `n>=173`, with precisely 48 admissible smaller sizes, and `P(n)>=3` for every `n>=175`. Consequently `A006063(j)=j+124` for `j>=49` and `A096680(j)=j+161` for `j>=14`; the finite base cases have explicit certificates. We also constructed eventual one-fixed-point and fixed-point-free cube-sum involutions.

- **[A006154](papers/A006154/)**
  - [A006154](https://oeis.org/A006154): Number of labeled ordered partitions of an n-set into odd parts.
  - **Result:** We proved eventual periodicity modulo every positive integer, with a period dividing `2*phi(m)` (or `phi(m)` for odd `m`). The least eventual period modulo 10 is 4.

- **[A048702](papers/A048702/)**
  - [A048702](https://oeis.org/A048702): Binary palindromes of even length divided by 3.
  - **Result:** We proved all four previously conjectured or unproved formulas, including exact digit-valuation sums, floor-sum identities and recurrences, uniformly in every base `b>=2`.

- **[A069862](papers/A069862/)**
  - [A069862](https://oeis.org/A069862): Smallest k such that n divides the concatenation of numbers from (n+1) to (n+k), where (n+1) is on the most significant side.
  - **Result:** We proved existence for every positive index and an exact finite arithmetic formula for the minimum at every index, using modular roots and the Chinese remainder theorem. We also obtained closed formulas for several infinite families.

- **[A075000 / A075001 / A075002](papers/A075000-A075002/)**
  - [A075000](https://oeis.org/A075000) (published): Smallest number such that n*a(n) is a concatenation of n consecutive integers; or 0 if no such number exists.
  - [A075001](https://oeis.org/A075001) (published): Smallest k such that concatenating n consecutive integers starting at k gives a multiple of n; 0 if none exists.
  - [A075002](https://oeis.org/A075002) (published): a(n) = smallest k such that A007908(k) is divisible by n.
  - **Result:** We proved that all three sequences have positive, well-defined terms at every positive index, by constructing divisible concatenations of consecutive integers and Champernowne prefixes.

- **[A075018](papers/A075018/)**
  - [A075018](https://oeis.org/A075018): Smallest k such that the concatenation k, k-1,k-2,k-3 is divisible by n; or 0 if no such number exists.
  - **Result:** We proved `A075018(n)>0` for every `n`, as a consequence of a universal even-base theorem for arbitrary permutations of consecutive blocks. We also proved `A075018(d*10^r)=d*10^r+3` for `r>=2` and every positive divisor `d` of 30.

- **[A077183 / A077185](papers/A077183-A077185/)**
  - [A077183](https://oeis.org/A077183) (published): Least k such that the reverse concatenation k, k-1, ..., 1 is divisible by prime(n); 0 if no such k exists.
  - [A077185](https://oeis.org/A077185): a(n) = A000422(A077183(n))/prime(n).
  - **Result:** We proved the exact zero classification: `A077183(n)>0` precisely when `n` is neither 1 nor 3, and the associated quotient terms are then positive. More generally, a prime `p` divides an appropriate descending concatenation in base `b` if and only if `p` does not divide `b`.

- **[A079495](papers/A079495/)**
  - [A079495](https://oeis.org/A079495): Numbers k such that the sum of the squares of the digits of k in base 3 is 0 (mod 3).
  - **Result:** We proved that squared-digit sums are equidistributed modulo `b` in every base `b>=2`. Each residue class has natural density `1/b`, and its sequence of positions has asymptotic slope `b`.

- **[A083468 / A083469](papers/A083468-A083469/)**
  - [A083468](https://oeis.org/A083468) (published): Smallest multiple of n which is the reverse concatenation of n consecutive numbers; or 0 if no such number exists.
  - [A083469](https://oeis.org/A083469) (published): Smallest k such that n*k is a reverse concatenation of n consecutive natural numbers.
  - **Result:** We proved that both sequences are positive at every index, even allowing an arbitrary permutation of the consecutive blocks. For `n=10^r`, we also determined the exact smallest descending concatenation and its quotient.

- **[A084043](papers/A084043/)**
  - [A084043](https://oeis.org/A084043): Smallest palindromic multiple of n in which the digit string of n appears as sandwiched between at least a pair of digits, or 0 if n = 10k or no such number exists.
  - **Result:** We proved `A084043(n)=0` exactly when `10` divides `n`, and gave an exact finite-state procedure for the least qualifying palindromic multiple at every other index.

- **[A085124](papers/A085124/)**
  - [A085124](https://oeis.org/A085124): Smallest multiple of n whose digital product is also a positive multiple of n, or 0 if no such number exists.
  - **Result:** We proved that a positive term exists exactly when `n` is 7-smooth and `10` does not divide `n`. A finite automaton determines every nonzero minimum exactly.

- **[A086558](papers/A086558/)**
  - [A086558](https://oeis.org/A086558): Smallest n-digit number beginning with n and having prime signature of n, or 0 if no such number exists.
  - **Result:** We proved existence for every positive index and an exact finite prime-factor formula for the minimum. At prime-power indices the formula reduces to an integer root followed by one `nextprime` operation.

- **[A087304](papers/A087304/)**
  - [A087304](https://oeis.org/A087304): Smallest nontrivial multiple of n preserving the product of its nonzero digits; 0 if none exists.
  - **Result:** We proved that every positive integer has infinitely many nontrivial multiples preserving the product of its nonzero digits, in every base. We also gave an exact finite-state recurrence for every decimal minimum.

- **[A087354 / A391022 / A391189](papers/A087354/)**
  - [A087354](https://oeis.org/A087354): Smallest square which is the concatenation of n nonzero squares.
  - [A391022](https://oeis.org/A391022): Minimal square obtained by concatenating n distinct nonzero squares in ascending order.
  - [A391189](https://oeis.org/A391189): a(n) = least integer m such that concatenating n distinct nonzero squares <= m^2 in ascending order yields a perfect square.
  - **Result:** We proved that for every `n>=1`, a strictly increasing list of `n` positive squares can be concatenated to form another square, establishing existence for all three sequences. The least values are not determined by this construction.

- **[A088862 / A090335](papers/A088862-A090335/)**
  - [A088862](https://oeis.org/A088862): Smallest number with exactly n prime factors (possibly with repetitions) such that in binary representation the divisors >1 form a prefix code.
  - [A090335](https://oeis.org/A090335): Smallest number with exactly n distinct prime factors such that in binary representation the divisors >1 form a prefix code.
  - **Result:** We proved both existence conjectures: every prescribed prime-factor signature has infinitely many representatives whose nontrivial divisors form a prefix-free code in any base, with an explicit witness bound.

- **[A092635](papers/A092635/)**
  - [A092635](https://oeis.org/A092635): Coefficients in asymptotic expansion of (Pi\*n/16^n)\*binomial(2n,n)^2 in powers of 1/(8n).
  - **Result:** We proved the Euler-polynomial coefficient formula and all three conjectured generating-function identities, including `H(x)*H(-x)=-x^2`.

- **[A115038 / A115039 / A115041](papers/A115038-A115041/)**
  - [A115038](https://oeis.org/A115038): a(n) is the smallest x such that x^2 + prime(n) is a perfect power.
  - [A115039](https://oeis.org/A115039): a(n) is the greatest k such that A115038(n)^2 + prime(n) is a k-th power.
  - [A115041](https://oeis.org/A115041): a(n) = y where A115038(x)^2 + prime(n) = y^A115039(n).
  - **Result:** We proved the shared perfect-power existence statement for every prime, and derived exact finite formulas for the least solution and both companion quantities. For odd primes, a solution follows from the difference-of-squares identity.

- **[A136050](papers/A136050/)**
  - [A136050](https://oeis.org/A136050): Sum of digits of product of twin primes A037074.
  - **Result:** We proved that every term arising from a twin-prime pair other than `(3,5)` is congruent to 8 modulo 9, settling the digit-sum congruence conjecture.

- **[A152009 / A214972](papers/A214972-A152009/)**
  - [A152009](https://oeis.org/A152009): (L)-sieve transform of {1,4,7,10,...,3n-2,...} (A016777).
  - [A214972](https://oeis.org/A214972): a(n) = a(floor(2\*(n-1)/3)) + 1, where a(0) = 0.
  - **Result:** We proved an exact recurrence for the L-sieve thresholds, identified all jump positions of A214972, and proved deterministic coordinatewise convergence of iterated L-sieves to the triangular numbers.

- **[A181373](papers/A181373/)**
  - [A181373](https://oeis.org/A181373) (published): Least m > 0 such that prime(n) divides 123...m and all cyclic digit permutations; 0 if none exists.
  - **Result:** We proved that every prime other than 2 and 5 divides infinitely many Champernowne prefixes together with all their cyclic digit rotations. We also supplied explicit upper bounds for the first witness.

- **[A191980 / A191981 / A191982 / A191983](papers/Lucas-coefficient-families/)**
  - [A191980](https://oeis.org/A191980): Ordered sums f+5g, where f and g are Lucas numbers (A000032 beginning at 1).
  - [A191981](https://oeis.org/A191981): Ordered sequence of nonnegative differences f-5g, where f and g are Lucas numbers (A000032 beginning at 1).
  - [A191982](https://oeis.org/A191982): Ordered sequence of nonnegative differences 5*f-g, where f and g are Lucas numbers (A000032 beginning at 1).
  - [A191983](https://oeis.org/A191983): Ordered sequence of nonnegative differences c*f-d*g, where f and g are Lucas numbers (A000032 beginning at 1) and {c,d}={1,5}.
  - **Result:** We proved direct piecewise formulas for every term of A191980–A191983, with exact counting and asymptotic growth laws. A191981 has unique positive representations; A191980 and A191982 each have exactly five repeated values; both pairwise intersections are completely classified. For general integer coefficients, we classified infinite-collision families of weighted Lucas sums and reverse differences and bounded all collisions of `L_i-qL_j` for `q>=2`.

- **[A195608](papers/A195608/)**
  - [A195608](https://oeis.org/A195608): Numbers n such that Sum\_{i=1..n} A(i) = A(n)\*A(n+1)/4, where A(n) = A001969(n).
  - **Result:** We proved an exact binary-parity membership criterion for every index, settling the conjectured gap set `{1,4,6}`, maximal block lengths and the block-start identity.

- **[A236383](papers/A236383/)**
  - [A236383](https://oeis.org/A236383): Smallest k such that k^2 is a concatenation of two numbers x and y where y = x + n^2 and x and y have the same number of digits.
  - **Result:** We proved existence at every index, including multiples of 11, by an explicit square-concatenation construction, and obtained an exact finite arithmetic formula for every minimum.

- **[A237930](papers/A237930/)**
  - [A237930](https://oeis.org/A237930): a(n) = 3^(n+1) + (3^n-1)/2.
  - **Result:** We proved that none of the six residue classes `11,13,23,61,71,73 (mod 84)` can contain a prime divisor of a sequence term, and gave an exact multiplicative-order test for other primes.

- **[A248520 / A248521](papers/A248520-A248521/)**
  - [A248520](https://oeis.org/A248520): Numbers k such that floor(cot(Pi/(2k+2))) = floor(cot(Pi/(2k))).
  - [A248521](https://oeis.org/A248521): Numbers k such that floor(cot(Pi/(2k+2))) = floor(cot(Pi/(2k))) + 1.
  - **Result:** We proved both conjectured asymptotic formulas with bounded additive errors, and derived exact counting and nth-term formulas for both cotangent-floor sequences.

- **[A260056](papers/A260056/)**
  - [A260056](https://oeis.org/A260056): Irregular triangle read by rows: coefficients T(n, k) of certain polynomials p(n, x) with exponents in increasing order, n >= 0 and 0 <= k <= 2\*n.
  - **Result:** We proved the column binomial-sum formula and the precise finite-difference order, and identified the alternating antidiagonal generating function.

- **[A308090](papers/A308090/)**
  - [A308090](https://oeis.org/A308090): a(n) = gcd(2^n + n!, 3^n + n!, n+1).
  - **Result:** We proved the complete formula `a(n)=n+1` when `n+1` is a prime at least 5, and `a(n)=1` otherwise.

- **[A308620](papers/A308620/)**
  - [A308620](https://oeis.org/A308620): Number of states in the evolutionary spatial prisoner's dilemma with n players.
  - **Result:** We derived the conjectured rational generating function and order-10 recurrence from the exact state-count formula. The recurrence applies from `n=12`, with an exceptional value at `n=11`.

- **[A334595](papers/A334595/)**
  - [A334595](https://oeis.org/A334595): Binary interpretation of the right diagonal of the XOR-triangle with first row generated from the binary expansion of n.
  - **Result:** We proved both XOR-triangle conjectures: the record positions are 1 and `2^m+1`, and the value 1 occurs exactly at powers of 2. We also characterized the finite binary transform.

- **[A334958](papers/A334958/)**
  - [A334958](https://oeis.org/A334958): GCD of consecutive terms of the factorial times the alternating harmonic series.
  - **Result:** We proved the valuation-product formula `a(n)=n!/denominator(H_n)` for the alternating harmonic sum `H_n`, together with its divisibility consequence.

- **[A340138](papers/A340138/)**
  - [A340138](https://oeis.org/A340138): a(1)=0, a(n+1) = the least m not already in the sequence such that the decimal digital root r of a(n-1) is found somewhere among the decimal digits of m.
  - **Result:** We proved that the published greedy digital-root sequence is a permutation of the nonnegative integers, and generalized the argument to every base `b>=2`.

- **[A346644](papers/A346644/)**
  - [A346644](https://oeis.org/A346644): Least k >= 1 such that sigma(k)/tau(k) has denominator n or zero if no k exists.
  - **Result:** We proved existence and an exact finite arithmetic minimum formula for every index, including composite denominators. In particular, `a(2^s)=2^(2^s-1)` and `a(q)=2^(q-1)` for every prime `q`.

- **[A357127](papers/A357127/)**
  - [A357127](https://oeis.org/A357127): a(n) = A081257(n) if A081257(n) > n, otherwise a(n) = 1.
  - **Result:** We proved that every nonunit value is a prime congruent to 1 modulo 3 and occurs exactly twice. We also disproved the second gcd conjecture by counterexample and established a corrected identity.

- **[A382357 / A382360](papers/A382357-A382360/)**
  - [A382357](https://oeis.org/A382357): Lexicographically earliest sequence of distinct positive integers such that the 2-adic valuations of adjacent terms differ exactly by one.
  - [A382360](https://oeis.org/A382360): a(n) is the unique k such that A382357(k) = 2^n.
  - **Result:** We proved that A382357 is a permutation of the positive integers and established the adjacent-pair formula `A382360(2m+1)=A382360(2m)+1`, along with a general theorem for valuation-jump greedy sequences.

- **[A393833](papers/A393833/)**
  - [A393833](https://oeis.org/A393833): Least integer k having exactly 2n+2 divisors such that the sequence of its 2n+1 proper divisors modulo n is a palindrome.
  - **Result:** We proved existence for every positive index using witnesses of the form `2*p^n` with `p=1 (mod n)`, and obtained an exact finite arithmetic minimization formula.
