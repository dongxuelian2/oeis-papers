# Independent cross-review, 2026-10-26

Read the complete proofs and source implementations; these notes are
additional review rather than a claim to have rerun the owning agents'
full audits.

- **A084043:** The pair automaton has the correct orientation:
  `(p,q) -> (delta(p,x),q')` whenever `delta(q',x)=q`.
  Reverse Dijkstra implements exactly the reverse relation. Lexical
  reconstruction takes the minimum over every inverse predecessor,
  avoiding an invalid arbitrary choice among nondeterministic branches.
  The matcher skips the leading digit, then requires a following digit
  after a complete occurrence. Unique accept `(0,d+1)` therefore enforces
  both exterior digits. Deleting a repeated pair from a shortest path
  proves the bound `2Q^2-1`. The elementary repeated-block existence
  proof handles the 2/5 part and coprime part separately and correctly.
- **A085124:** The zero-free suffix lift has unit coefficient
  `5^(j-1)` modulo 2 or `2^(j-1)` modulo 5. The extra start state handles
  the empty-word issue at n=1 and makes the digit bound N correct.
  The residue/product-valuation states accept precisely the intended
  words; increasing-digit BFS supplies exact numeric minimization.
- **A048702:** Checked the carry algebra, nonprime-base valuation,
  changes of digit length, and the exact valuation counts in the second
  Maple formula. All statements are valid including n=1.
- **A393833:** The evaluator's minimum exponent-sum bound follows by
  splitting multiplicative tau factors into primes. All later bases
  are at least the current base, making its root cap valid. The residue
  condition `K/minprime == 1 mod n` follows from comparing the first
  and last proper-divisor residues. Published values are used only as
  fully verified upper witnesses, not presumed minimum values. The
  final manuscript was subsequently reviewed as well: every prime
  divisor p of Phi_n(2n) avoids 2n, and squarefreeness of X^n-1 mod p
  proves that the residue of 2n has exact order n. Hence p=1 mod n,
  with no prime-distribution assumption. The ordered divisors of
  2*p^n alternate powers and twice powers because p>2, giving the
  asserted palindrome. All finite candidate indices are correct.
- **A152009 (root proof outline):** The survivor-index map is
  `F_A(j)=1+b_j`, where b is the complement of the deletion-index set.
  Iteration gives the L-sieve output `F_A^(r-1)(1)`. A triangular prefix
  of length k is preserved, with next term at least the next triangular
  number. One further transform makes that term exact. Nonempty A
  makes `F_A(j)>=j+2` eventually; output therefore has infinite
  complement and stays in the admissible domain.

For very large inputs, the Python programs have ordinary implementation
resource limits: e.g. palindrome reconstruction uses recursion, dense
pair distances require quadratic memory, and Python may cap decimal
integer conversions. These do not invalidate the finite-state mathematical
formulas or their termination in an unbounded resource model.
