# A084043: all-index existence and exact palindromic minima

Official source: <https://oeis.org/A084043>, inspected 2026-10-26. The entry conjectures that a(n)=0 exactly when 10 divides n. The inspected entry supplies 38 terms and no proof or solved-status comment.

**Result.** The conjecture holds for every positive integer n. A finite pair-automaton algorithm computes the exact minimum at every remaining index. The formula is finite-state minimization, not a claimed elementary expression without minimization.

## Elementary existence proof

Every positive multiple of 10 ends in zero. A decimal palindrome ending in zero would start in zero, which is forbidden, so multiples of 10 are exactly the necessary candidates for zero.

For 10 not dividing n, write n=Cm, where C is the full 2-power or 5-power dividing n (or 1), and gcd(m,10)=1. If C=p^a>1, let S be the decimal representation of C padded on the left with zeros to length a. This is possible because p^a<10^a. If C=1, take S="1". The last digit of S is nonzero.

Let D be the decimal expansion of n and form the word

    B = reverse(S) D reverse(D) S.

This is a palindrome with nonzero leading digit. It contains D strictly inside its two end digits. The suffix S has value C and its decimal place length is at least a; hence B is divisible by C. Put L=|B|, h=ord_m(10^L) when m>1, and h=1 when m=1. Repeat B exactly R=mh times. Repetition of a palindrome is a palindrome. Every copy still contains D internally. The repeated integer equals

    B * sum(j=0..R-1, 10^(Lj)).

It remains divisible by C. Modulo m, the powers in each block of h terms have the same sum, and there are m such blocks, so the sum is divisible by m. Thus the integer is a palindromic multiple of n with the required interior string. This proves the full zero classification.

## Exact minimum by a finite automaton

Let d=|D|. Use a deterministic automaton whose ordinary states are (r,k), with r the residue modulo n and k in {0,...,d+1}. Before a complete occurrence is found, k<d records the longest prefix of D that is a suffix of all digits read after the first digit. State k=d means an occurrence just ended; reading any following digit changes it to k=d+1, which is absorbing for the string condition. This extra step ensures an occurrence has at least one digit to its right. Matching starts only after the first digit, ensuring a digit to its left. Add a start state and a dead state for a leading zero. The only accepting state is (0,d+1). There are Q=n(d+2)+2 states. Every accepted word is precisely a positive multiple of n containing D as an interior substring.

For any deterministic digit automaton delta with start s and accepting state f, construct a directed graph on Q^2 pairs (p,q). There is a digit-labelled edge

    (p,q) --x--> (delta(p,x),q')  whenever delta(q',x)=q.

A pair can terminate with an empty center at cost 0 when p=q, or with a one-digit center x at cost 1 when delta(p,x)=q. Every pair edge has cost 2. By induction on length, the paths from (s,f) to these centers correspond exactly to accepted palindromes: wrap the center in the same digit on its left and right at each edge. Thus the shortest weighted path gives the minimum length; selecting the lexicographically smallest word among all shortest paths gives exactly a(n). Leading zero is already rejected by the original automaton.

A shortest path cannot repeat a pair: deleting the cycle reduces its length and preserves acceptance. Thus a shortest palindrome has at most 2Q^2-1 digits. Existence above guarantees a reachable center. This proves a finite all-index minimum formula independent of unbounded scanning. The implementation computes reverse distances from all centers by Dijkstra and reconstructs the smallest shortest word.

## Validation

Run `python papers/A084043/verify.py` from the repository root. The verifier compares all 38 official terms and independently enumerates ordinary decimal palindrome halves through seven digits to verify minima for n<=100. It separately checks the constructive witnesses for every n<=500 that is not divisible by 10. Infinite scope follows from the construction and finite graph argument.

## Artifacts

- `main.tex`, `main.pdf`: two-page paper, compiled twice with no LaTeX warnings; both pages rendered and visually checked.
- `b084043.txt`: exact values for n=1..100, rechecked by the verifier.
- `oeis.txt`: proposed entry update, not submitted.

## Resource limits

Termination is proved mathematically; practical scalability is limited. The implementation materializes Q^2 distances for Q=n*(digits(n)+2)+2, plus a reverse-edge heap and memoized reconstruction strings. Large n can require prohibitive memory and time, and reconstruction can exceed Python's recursion or integer-conversion limits. The universal witness may have an enormous number of digits. No polynomial-time guarantee in the bit length of n is claimed; the implementation is intended for moderate indices and reproducible exact controls.
