# A quantitative height barrier for the same-width exponential representation

This is a method limitation, not a proof of Kashihara's conjecture or a limitation of every global method. It quantifies the previously noted fixed-coefficient issue. Even the unrotated prefix has a moving leading coefficient whose height is not negligible relative to the exponential variable, uniformly throughout the digit interval. Thus neither fixed-coefficient results alone nor a theorem requiring negligible moving coefficient height can supply the missing global exclusion through this representation.

## 1. Exact representation

Let d>=2, B=10^d, L=B/10, C=B-1, and t=D(L-1). For L<=m<=B-1 put N=m-L+1. With W_j the decimal concatenation 1 through j, define

    A=C^2*W_(L-1)+L*C+1.

The already proved same-width identity is

    C^2*W_m=A*B^N-(m*C+B).

Here A is fixed only while d is fixed. The number of allowed exponents in that width is finite: 1<=N<=9B/10. Increasing m without bound necessarily changes A and B.

## 2. Exact scale of the coefficient

The digit-count formula gives

    t=(d-1)*L-(L-1)/9.

Since 10^(t-1)<=W_(L-1)<10^t and (9/10)B<=C<B, we have the elementary bounds

    (81/1000)*10^(t+2d)<=A<2*10^(t+2d).

For the upper bound use L*C+1<=B^2 and t>=1. Consequently

    log_10 A=t+2d+O(1),

with an absolute bounded error. Since A is independent of m and N is largest at m=B-1,

    min_(L<=m<=B-1) log(A)/(N*log B)
      = log(A)/((9B/10)*d*log10)
      -> 1/9 as d -> infinity.

Indeed t/((9B/10)d)=(d-10/9)/(9d)+1/(81dL), and the remaining O(d) numerator is negligible. This is a positive lower height ratio, not an o(1) ratio. Near the beginning of a width the ratio is even larger.

For the rational leading coefficient alpha=A/C^2 in W_m=alpha*B^N-(m*C+B)/C^2, the absolute logarithmic rational height is exactly log A. To see this, A=1 modulo C, hence gcd(A,C^2)=1, and A>C^2. The displayed ratio therefore describes its actual rational height, not just an unreduced numerator bound.

## 3. Removing powers of ten does not fix the scale

The final two integer blocks of W_(L-1) end with L-2 and L-1. Their final d digits are 9L-1; this also holds at d=2, where the last two blocks are 8 and 9. Therefore

    W_(L-1)=9L-1 modulo B,
    A=8L modulo B.

Thus v_5(A)=d-1 and v_2(A)>=d-1. In particular the largest common integral power of 10 dividing A is exactly 10^(d-1). Removing it replaces log A by log A-(d-1)log10, which has the same limiting ratio 1/9 above. A cannot contain even one full factor B.

## 4. Consequences and limits

A theorem with fixed recurrence coefficients has constants or exceptional thresholds depending on those coefficients. Finiteness for each artificial extension in N says nothing uniform about the actual diagonal family, whose allowed range stops at N=9B/10 while its coefficients change with d.

A moving-coefficient theorem that requires h(alpha)=o(h(B^N)) also has an unverified hypothesis here: Section 2 proves the opposite in this representation. Replacing square roots by fixed e-th roots does not remove the issue by a formal height rescaling; both coefficient-root height and exponential-root height would be divided by e.

The alternative representation in IRRATIONAL_TARGET_ASSESSMENT.md does escape this height barrier and proves a fixed-squareclass finiteness theorem; its remaining limitations are stated separately.

This does not rule out a theorem allowing a positive coefficient-height ratio, a specially structured argument using A, another exact representation, or a genuinely global approach. It does not show that the corresponding integers are powers. Existing density-zero bounds and local survivor constructions remain compatible, and the original integer-power conjecture remains open.

## 5. Finite verification

The verifier constructs W_(L-1) at widths d=2,3,4,5, checks the exact identity at the first eight endpoints of each tested width, both coefficient bounds, coprimality, the residue 8L and v_5(A)=d-1. It additionally checks the digit-count formula arithmetically for d through 2000. These tests do not establish the asymptotic by sampling: the exact formulas and bounds above prove it. No search or claimed exclusion of new integer-power candidates is performed. The main manuscript and PDF are unchanged.
