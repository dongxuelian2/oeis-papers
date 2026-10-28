# OEIS A191980–A191983 verification

The proof of the four OEIS sequences and their complete intersections
is included in the single
[weighted Lucas sums and differences manuscript](../Lucas-coefficient-families/main.pdf)
([LaTeX source](../Lucas-coefficient-families/main.tex)).

This directory preserves the exact-integer reference implementations and
independent certification scripts for the \`q=5\` case:

- \`rank.py\`: A191981 counting, ranking, residue substreams, and membership.
- \`intersection.py\`: A191981–A191982 intersection.
- \`count_union.py\`: A191982 and A191983 counting and unranking.
- \`sums.py\`: A191980 counting, ranking, and witnesses.
- \`sum_difference_overlap.py\`: A191980–A191982 intersection.
- \`verify.py\`, \`verify_intersection.py\`, \`verify_duplicates.py\`,
  \`verify_sums.py\`, and \`verify_sum_difference_overlap.py\`:
  independent finite and recurrence-based checks.

The [OEIS verification workflow](../../.github/workflows/a191980-a191983.yml)
runs these checks. The unified manuscript is compiled by the
[Lucas coefficient workflow](../../.github/workflows/lucas-coefficients.yml).
