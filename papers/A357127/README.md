# A357127: Prime-pair involution and corrected gcd conjecture

Official source: <https://oeis.org/A357127>, opened 2026-10-26. The relevant conjecture remains explicitly labelled in the inspected entry; no resolving later comment was found. This is not an exhaustive literature-priority claim.

**Completed result.** Every nonunit value is a prime p congruent to 1 modulo 3 and occurs exactly twice, at n and p-n-1. This proves Conjecture 1 at every index.

**Scope and corrections.** Conjecture 2 is false: a(35)=a(61)=97, but gcd(35^2+35+1,61^2+61+1)=1261. The exact replacement is p*gcd((n^2+n+1)/p,m-n) for the paired indices. The separate record-prime observation is not proved.

The full elementary proof is in `main.tex` and `main.pdf`. `verify.py` uses only the Python standard library and independently compares the original definition with the proved formulas. `b357127.txt` contains 100 exact consecutive values. `oeis.txt` is a proposed update; it has not been submitted.

Run `python papers/A357127/verify.py` from the repository root. Large integer sizes and trial-division factorization can require substantial resources; no polynomial runtime in the bit length of the index is asserted. The proof establishes global scope independently of finite verification.

Final PDF: 2 page(s), compiled twice without warnings; every page rendered and visually checked.
