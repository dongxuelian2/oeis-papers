# A085124: all-index zero classification and exact minima

Official source: <https://oeis.org/A085124>, inspected 2026-10-26. Its stated conjecture is that a(n)>0 whenever n is 7-smooth and 10 does not divide n. No proof or solved-status comment appears in the inspected entry.

**Result.** The conjecture holds for every positive integer n. The program computes every nonzero minimum by a finite automaton. This is an exact finite-state formula, not an elementary expression without minimization.

## Elementary existence proof

Write n=2^a 3^b 5^c 7^d. If n has a prime factor larger than 7, a positive decimal digit product cannot be divisible by n. If 10 divides n, every multiple of n ends in zero and has zero digit product. These are necessary obstructions.

Suppose n is 7-smooth and 10 does not divide n. At most one of a,c is positive. Put C=2^a5^c and m=n/C, so gcd(m,10)=1.

For p in {2,5} and e>=1 there is a zero-free decimal word of length e whose value is divisible by p^e. Inductively suppose the j-1 rightmost digits have value s divisible by p^(j-1). Choose the new leftmost digit t in {1,...,p} so that s+t*10^(j-1) is divisible by p^j. After division by p^(j-1), the coefficient 10^(j-1)/p^(j-1) is invertible modulo p, so exactly one of these digits works. All digits are nonzero. Let T be this suffix for the nontrivial factor C, or T="1" if C=1. Its length is at least the exponent of 2 or 5 in C.

Let W consist of a copies of "2", b copies of "3", c copies of "5", and d copies of "7". The nonempty word B=WT has nonzero digits, its digit product is divisible by n, and its integer value is divisible by C: the suffix T supplies divisibility and 10^|T| is divisible by C.

Put L=|B|. If m>1, set h=ord_m(10^L); if m=1, set h=1. Repeat B exactly R=mh times. The resulting integer is

    B * (1 + 10^L + ... + 10^((R-1)L)).

It is divisible by C. Modulo m, group the geometric sum into m groups of length h; every group has the same residue, hence their sum is zero. Thus it is divisible by n. Its digit product remains a positive multiple of n. This proves sufficiency, without a conjecture about primes or restricted-digit multiples.

## All-index exact minimum formula

For admissible n with target exponents e=(a,b,c,d), use states (r,f), where 0<=r<n and 0<=f_p<=e_p. Reading digit t in {1,...,9} maps

    (r,f) -> ((10r+t) mod n, (min(e_p,f_p+v_p(t)))_p).

Start at an extra initial vertex and accept at (0,e). The extra initial vertex enforces a nonempty decimal expansion, including n=1. Among accepted words take first shortest length, then lexicographically smallest digits. This is exactly numeric minimization because the alphabet excludes zero. Breadth-first search with ascending outgoing digits computes it.

There are N=n*product(e_p+1) ordinary states. A shortest accepted path cannot revisit an ordinary state, since deleting the intervening cycle preserves acceptance and shortens a nonempty word. Consequently a(n) has at most N digits. Equivalently, a(n) is the minimum of the accepted words of lengths 1 through N. Existence above proves that this finite set is nonempty for every admissible n; all other indices have value zero.

## Validation

Run `python papers/A085124/verify.py` from the repository root. The verifier compares 50 displayed official terms, checks 51 independent minima obtained by direct scanning of integers through 200000 for n<=200, and checks all 73 admissible constructive witnesses through n=500. The infinite result follows from the proof, not from these finite controls.

## Artifacts

- `main.tex`, `main.pdf`: two-page paper, compiled twice with no LaTeX warnings; both pages rendered and visually checked.
- `b085124.txt`: exact values for n=1..100, rechecked by the verifier.
- `oeis.txt`: proposed entry update, not submitted.

## Resource limits

The proved finite bound is not a practical running-time bound for large input. Breadth-first search can visit n*product(e_p+1) states, and each state stores a residue, a capped-valuation tuple, and predecessor data. Large admissible indices can exhaust memory, and conversion of very long winning words to Python integers may reach the interpreter's digit limit. The constructive witness can be extremely long. No polynomial-time guarantee in the bit length of n is claimed; the supplied evaluator targets moderate indices and exact reproducibility.
