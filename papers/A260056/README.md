# A260056: both conjectures proved globally

[Official entry](https://oeis.org/A260056), read in full 2026-10-26:
the column finite-difference recurrence and alternating-antidiagonal
identification remain explicitly conjectural.

We prove the exact column formula
`T(n,k)=sum(i=ceil(k/2)..k, binomial(i,k-i)*binomial(n+1,i+1))`.
Its degree is exactly k+1, proving the conjectured difference order
k+2 and its minimality. The alternating antidiagonal generating
function is `1/((1-z)^2*(1+z^2))`, exactly A004524 shifted by3.

[main.tex](main.tex) gives full proofs; [verify.py](verify.py) checks
independent trinomial rows, all10000 published entries, columns and
antidiagonals. Run `python3 verify.py`. No OEIS update has been submitted.
