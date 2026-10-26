# A308090: Exact joint factorial gcd classification

Official source: <https://oeis.org/A308090>, opened 2026-10-26. The relevant conjecture remains explicitly labelled in the inspected entry; no resolving later comment was found. This is not an exhaustive literature-priority claim.

**Completed result.** For every n>=1, a(n)=n+1 if n+1 is prime at least 5, and a(n)=1 otherwise. This proves the official converse conjecture and the prime-indicator identity.

**Scope and corrections.** The single-sum observation is false without qualifications: n=7 gives 8 dividing 2^7+7!, although 8 is composite.

The full elementary proof is in `main.tex` and `main.pdf`. `verify.py` uses only the Python standard library and independently compares the original definition with the proved formulas. `b308090.txt` contains 100 exact consecutive values. `oeis.txt` is a proposed update; it has not been submitted.

Run `python papers/A308090/verify.py` from the repository root. Large integer sizes and trial-division factorization can require substantial resources; no polynomial runtime in the bit length of the index is asserted. The proof establishes global scope independently of finite verification.

Final PDF: 1 page(s), compiled twice without warnings; every page rendered and visually checked.
