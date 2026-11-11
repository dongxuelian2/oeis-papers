# Weighted Lucas sums and differences

[Manuscript (PDF)](main.pdf) · [LaTeX source](main.tex)

The paper studies positive representations of Lucas-number expressions
\(L_i-qL_j\), \(qL_i-L_j\), and \(qL_i+L_j\), where \(i,j\ge1\)
and \(q\) is an integer. We use \(L_0=2\), \(L_1=1\), and
\(L_{n+2}=L_{n+1}+L_n\).

## Results

### General coefficients

For each \(q\ge2\), the positive collisions of \(L_i-qL_j\) have
an explicit finite index bound. The coefficients that produce infinitely
many repeated positive values in the reverse differences and weighted sums
are precisely three arithmetic families: integral quotients of odd-indexed
Lucas numbers, integral quotients of even-indexed Fibonacci numbers, and
the half-Lucas coefficients \(L_{6r+3}/2\).

Signed ratios of Lucas-number gaps classify the coefficients producing
finite collisions. For \(q=5F_{2r}\), every positive value of
\(L_i-qL_j\) has a unique representation.

### Four OEIS sequences at coefficient five

| Sequence | Definition (in increasing order) | Result |
| --- | --- | --- |
| [A191980](https://oeis.org/A191980) | \(5L_i+L_j\) | Direct term formula; five repeated values |
| [A191981](https://oeis.org/A191981) | \(L_i-5L_j>0\), preceded by zero | Direct term formula; unique positive representations |
| [A191982](https://oeis.org/A191982) | \(5L_i-L_j>0\), preceded by zero | Direct term formula; five repeated values |
| [A191983](https://oeis.org/A191983) | Positive values of the two difference forms, preceded by zero | Direct term formula; complete intersection classification |

Every term has an exact piecewise expression with a square-root index selector
and a fixed number of Lucas values. The formulas follow from complete,
strictly ordered Lucas-scale intervals:

| Sequence | Fixed initial terms | Terms per large interval | Growth of \(\log_\varphi a(n)\) |
| --- | ---: | ---: | --- |
| A191981 | 26 | \(m-4\) | \(\sqrt{2n}+O(1)\) |
| A191982 | 14 | \(m+3\) | \(\sqrt{2n}+O(1)\) |
| A191980 | 80 | \(2m-4\) | \(\sqrt n+O(1)\) |
| A191983 | 56 | \(2m-5\) | \(\sqrt n+O(1)\) |

Here \(\varphi=(1+\sqrt5)/2\). The repeated positive values of A191982
are \(2,4,8,14,17\); those of A191980 are \(16,23,38,62,91\).
The manuscript also determines the complete intersections
\(S_5\cap T_5\) and \(P_5\cap T_5\), with their finite exceptions
and infinite Lucas families.

## Files and verification

The [manuscript](main.tex) contains the classification theorems,
direct expressions, exact counts and proofs. The
[Lucas-shell proof details](direct-terms-proof.md) give the interval
partitions, base inequalities and quadratic index inversions.

The [direct evaluator](direct_terms.py) computes each term with exact
integer arithmetic. The [comparison script](check_direct_terms.py)
checks its output against the original double-index definitions:

    cd papers/Lucas-coefficient-families
    python check_direct_terms.py 80

The [q=5 verification programs](../A191980-A191983/) cover
counting, intersections and multiplicities. The remaining
verification programs in this directory check the general-coefficient
theorems and finite collision bounds.

The exact Lucas-shell inequalities are implemented in
[the proof checks](proof_checks/): A191981 shell comparisons,
A191980/A191982 interval certificates, and the A191983
union ordering.
