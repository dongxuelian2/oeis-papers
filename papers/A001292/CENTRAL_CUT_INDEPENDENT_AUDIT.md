# Independent mathematical audit

## Result

The proof in `CENTRAL_CUT_DETERMINANT_SPARSITY.md` supports the stated bound

    count < 32 B (1 + floor(log_2(18d)))

for exactly the domain `d>=2`, `B=10^d`, `L=B/10`, `2L<=m<B`, and `L+7<=k<m`. No substantive flaw was found. The conclusion counts square-producing pairs, not distinct rotated values, and does not imply nonexistence or cover omitted endpoints/cuts.

The initially reported prime-power notation issue has been corrected: the current proof uses `a_p=v_p(J)/2` consistently. The current proof and completed companion verifier have both been reviewed; no unresolved blocker remains.

## Independently checked steps

1. **Compressed modulus.** For `v_p(J)=2a_p<n`, every root has `v_p(x)=a_p`. Unit roots of `u^2=-J/p^(2a_p)` modulo `p^(n-2a_p)` determine `x=p^a_p u` modulo `p^(n-a_p)`. At most four choices for 2 and two for 5 give at most eight classes modulo `r=B^K/z`, with `z=sqrt(J_(2,5))<B`.

2. **Continuous domain.** The interval `max(L+1,K+1)<=N<=9L` contains all candidates at fixed cut. The inherited elementary estimates extend to real `N` on it. They give `0<T_N/(GJB^N)<20 B^(K-N)<=1/5`, so the square-root curve is positive and twice differentiable throughout, including between candidates.

3. **Strict concavity.** For `F(Q)=sqrt(alpha^2 Q^2-lambda log Q-mu)` and `T=lambda log Q+mu`, direct differentiation gives

       4 F^3 F'' = alpha^2(6lambda-4T)-lambda(2T+lambda)/Q^2.

   The draft proves `T/a_0>B/20>=5` while `(3lambda/2)/a_0=3/log B<1`. Both terms are strictly negative. Three distinct candidates in a fixed parity group are therefore never collinear.

4. **Determinant lower bound.** In one compressed-root branch, subtracting its common integer residue times the constant column makes the first column divisible by `r`. The second column is divisible by `Q_1` because the denominators are nested integral powers of ten. The nonzero determinant is consequently at least `rQ_1` in absolute value, without any coprimality assumption on `r` and `Q_1`.

5. **Determinant upper bound and gap.** The positive errors `delta_i=alpha Q_i-x_i` satisfy `delta_i<20Q_1 B^(K-N_1+1)`. Expanding the error-column determinant yields a strict bound `40Q_1Q_3 B^(K-N_1+1)`. Combining bounds and `z<B` gives

       N_3 > 2N_1-t/d-4-(2log_10(40)-e)/d
           > 2N_1-t/d-6.

   The final strict inequality is valid for every `d>=2`.

6. **Centered counting.** With `h=N-t/d-6`, the lower bound `h>=L/(2d)` for `d>=3` is precisely `11L>=90d+2`; it holds at 3 and then by elementary induction. Also `h<9L`. Odd and even subsequences each double strictly, so each has at most `1+floor(log_2(18d))` terms. Eight branches, two parities, and fewer than `B` cuts give the displayed theorem, with strictness supplied by the cut count.

7. **Small width and alternative uniform bound.** At `d=2` the entire permitted domain has exactly `sum_(m=20)^99(m-17)=3400` pairs, less than the theorem's 19200. The optional all-width lower bound `h>=L/(10d)` is equivalent to `91L>=450d+10`, with equality at `d=2`. It gives the alternative strict bound `32B ceil(log_2(90d))`.

8. **Cumulative estimate.** For `D=digits(floor X)>=2`, summing width bounds and using `sum_(d=2)^D 10^d<10^(D+1)/9` and `10^D<=10X` gives `(3200/9)X(1+floor(log_2(18D)))`. Thus the claimed restricted-domain `O(X log log X)` follows, with no extension to excluded regions.

## Independent finite checks

A separate inline Python/SymPy calculation, independent of the author's verifier, completed successfully. It was run as a shell command, not saved as a companion script file:

- Exact symbolic simplification of the second-derivative identity to zero.
- 1,789 complete prime-power target checks: all nonzero `J` modulo `2^n` for `1<=n<=9`, and modulo `5^n` for `1<=n<=4`, with all residues enumerated as potential roots. Odd valuations had no roots; compressed root counts obeyed four/two, and full root counts equaled compressed counts times the expected `p^a_p` multiplicity.
- Exact integer checks of both centered lower-bound inequalities through width 1000.
- Direct count of the 3400 width-2 admissible pairs.

These finite checks supplement, rather than replace, the mathematical proof. No claim of literature priority has been assessed, and no external publication or upload was performed.


## Review and rerun of the completed companion verifier

The current `verify_central_cut_determinant.py` was read in full and rerun successfully. It regenerated `central-cut-determinant-certificate.json` and reported PASS. The certificate accurately distinguishes finite checks from the infinite theorem and synthetic determinant inputs from actual rotation-square solutions.

The exact finite scope is:

- **3,442 exact rotation checks:** every one of the 3,400 admissible width-2 pairs, including 410 central-band pairs, and 42 explicitly listed width-3 samples. There were zero square pairs in the exhaustive width-2 domain. The certificate does not claim an exhaustive width-3 search.
- **3,154 prime-power compressed-branch checks:** primes 2 and 5, exponent ranges `1<=n<=10` and `1<=n<=6` respectively, and every target `1<=J<=min(p^n-1,500)` in those ranges. All candidate roots are enumerated modulo each prime power. This is not exhaustive over all targets when `p^n>501`.
- **979 decimal/CRT compressed-branch checks:** `10^n` for `1<=n<=4`, targets `1<=J<=min(10^n-1,500)`, restricted to `v_2(J)<n` and `v_5(J)<n`. Together with the prime-power checks this is 4,133 branch checks. The script additionally performs 2,993 individual root-valuation checks.
- **One exact symbolic polynomial identity:** the script expands `2 f f''-(f')^2` with explicitly supplied correct derivatives of the radicand, using integer coefficients and Laurent monomials. It is an algebraic identity check, not numerical differentiation and not a stand-alone proof of all sign hypotheses.
- **504 synthetic integer determinant checks:** divisibility by `rQ_1` and the nonzero lower bound, plus 12 separate rational synthetic examples for the error-column upper bound. These are not asserted to be rotation-square solutions.
- **999 exact width-constant checks:** every integer width from 2 through 1000 inclusive, checking centered lower bounds, the relaxed gap constant, and logarithmic counting factors.

The script uses exact integer and rational arithmetic for its assertions. The written proof supplies the general concavity, branch-count, growth, and counting arguments outside this finite scope. No substantive correction to the current script or certificate is required.
