# Official OEIS screening: greedy, recurrences, binary structure

Accessed 2026-10-26. Every URL below is the official complete entry;
later remarks and formulas were read before treating a conjecture as open.
This ledger records screening decisions, not claims of comprehensive
literature searches or OEIS acceptance.

| Entry and official source | Exact question screened (paraphrased) | Current entry status and decision |
|---|---|---|
| [A195608](https://oeis.org/A195608) | For indices n with sum of first n evil numbers equal to E(n)E(n+1)/4: prove gaps belong to {1,4,6}, maximal blocks have size 1 or 3, and block starts m have E(m+1)-E(m-1)=5. | Entry still labels all three conjectures, attributed to Vladimir Shevelev, Sep 21 2011. **Solved in this batch**, with necessary m>1 boundary qualification for the third assertion. Complete binary membership theorem in papers/A195608. |
| [A019445](https://oeis.org/A019445) | Greedy integer-average permutation partial sums are divisible by their indices (Somos's observation). | Entry explicitly says proved in Shapovalov (1996) and Venkatachala (2009), reiterated Shallit Jul 18 2023. **Exclude: already proved.** |
| [A195507](https://oeis.org/A195507) | For least m>n agreeing with n modulo every k<n, prove the displayed denominator recurrence. | Adams-Watters remark, Sep 20 2011, already derives it from a(n)=n+lcm(1,...,n-1). **Exclude: already proved.** |
| [A006165](https://oeis.org/A006165) | Bala's seven iterated-map identities, especially plateaus of n-a iterated k times. | Complete entry includes a 2026 Byungwoong Yoo technical note proving conjecture (vii). **Exclude (vii) as already proved; other identities not pursued.** |
| [A163873](https://oeis.org/A163873) | For a(n)=n-a(a(n-k)), does the stated recursive two-construct tree description hold for every k? | General structural conjecture remains stated. Definitions involve diagrams and crossing conventions; no short complete proof identified. **Deferred; no result claimed.** |
| [A374284](https://oeis.org/A374284) | Is the least-unused sequence with transition rule [omega(y)>omega(x) or rad(y) divides x] a permutation? | Entry still explicitly conjectures the full permutation property. **Deferred.** Least-missing-value argument only restricts eventual omega and support; it does not prove every missing integer eventually appears. |
| [A329453](https://oeis.org/A329453) | Is the lexicographically first distinct nonnegative sequence with exactly two prime pairwise sums in every five-term window a permutation? | Conjectured in entry; extension discussion exposes coupled prime/composite constraints. **Deferred: no unconditional prime-pattern existence proof identified.** |
| [A157182](https://oeis.org/A157182) | Is the greedy antidiagonal square array with prime sums between horizontal/vertical neighbors a permutation? | Entry asks this as a conjecture. **Deferred: simultaneous prime-sum constraints.** |
| [A087666](https://oeis.org/A087666) | Does approximate squaring x -> x*floor(x), starting at n/3>=2, always reach an integer; and is summed stopping time 2n+O(sqrt(n))? | Entry retains conjectures and cites Lagarias-Sloane approximate-squaring paper. **Deferred: known hard dynamical question.** |
| [A085061](https://oeis.org/A085061) | For prime-difference/composite-sum greedy sequence, is a(n+5)>a(n), and are all values distinct? | Both conjectures remain in comments; displayed data itself repeats 594. **Negative result audited in this batch:** growth fails at n=24, since a(24)=594 and a(29)=485; repeated value 594 occurs at n=24 and n=28. See counterexample audit rather than treating conjectures as a fresh proof target. |
| [A085265](https://oeis.org/A085265) | Are 1 and 13 the only positive integers not expressible as positive squarefree plus positive square? | Entry only cites Estermann's finiteness theorem and retains exact exception conjecture. **Deferred: exact effective threshold needs substantial sieve estimates.** |
| [A085267](https://oeis.org/A085267) | Does the increasing list of integers having at least two such representations eventually equal n+11 after index 50? | Conjecture remains; no explicit effective threshold available in entry. **Deferred: same analytic obstacle.** |
| [A079495](https://oeis.org/A079495) | For squared digit sums modulo every base b, does every residue have density 1/b and positional slope b? | Complete entry retains conjecture (Carlos Alves, Jan 20 2003); **solved in this batch for all b>=2**, including composite bases. See papers/A079495. |
| [A079498](https://oeis.org/A079498) | Analogous density/slope conjecture for ordinary digit sums modulo b. | Complete entry explicitly includes Michel Dekking's Apr 18 2019 proof. **Exclude: already proved**, and distinguish it from squared digits. |
| [A339607](https://oeis.org/A339607) | Is the greedy binary-pattern-containing sequence a permutation? | Complete entry explicitly includes Branicky's Dec 16 2020 proof. **Exclude: already proved.** |
| [A340138](https://oeis.org/A340138) | Is the decimal digital-root/digit-containing greedy sequence a permutation? | Complete entry retains conjecture (Michael De Vlieger, Jan 21 2021). **Solved in this batch for its published program/data sequence**, and generalized to every base. Prose has an index typo relative to program/displayed data; the proof explicitly specifies the intended immediate-predecessor rule. See papers/A340138. |

## Failed proof attempts and scope checks

- A374284: If k is the least omitted integer, sufficiently late predecessors
  must have omega at least omega(k) and radical not containing rad(k).
  This observation alone does not force a contradiction: increasing-omega
  transitions can introduce fresh supports. No claim of permutation follows.
- A195608: The third conjecture as literally written includes the initial
  singleton {1}, where E(0) is undefined because A001969 has offset 1.
  We explicitly state and prove the meaningful version for every later
  block. This is a boundary correction, not an invented extension at 0.
- A006165: A search-result snippet still calls (vii) conjectural, while
  the complete live entry links a 2026 proof. Excluded after the full read.

## Source data

`b195608-published.txt` is downloaded directly from
https://oeis.org/A195608/b195608.txt on 2026-10-26, preserving all 10,000
published pairs as an external check. It is OEIS source data, not a new
b-file or a claim of novelty for those terms.

`b340138-published.txt` is downloaded directly from
https://oeis.org/A340138/b340138.txt on 2026-10-26. Its 10,000 terms
are compared in full with the explicitly stated immediate-predecessor
rule. This validates the indexing interpretation independently of
the entry's inconsistent prose.

For the squared-digit density proof, also read the complete related
pages A006287 (raw ternary squared-digit sums; no density theorem),
A075311 (a distinct binary-weight sieve; no relevant density theorem),
A079496 and A079497 (unrelated adjacent Diophantine-approximation
sequences). The directly related A079498 explicitly proves ordinary
digit-sum density, which is acknowledged and excluded from novelty.
