# Norm restrictions on stationary Lucas collisions

Let (L_0=2,L_1=1), (F_0=0,F_1=1), and (L_{n+2}=L_{n+1}+L_n).
Write (alpha=(1+sqrt5)/2), (eta=(1-sqrt5)/2), so
(alphaeta=-1). The results below refine the finite stationary-pattern
criterion in `main.tex`.

## 1. A necessary square-norm equation

**Proposition.** Suppose (qge2), (i<k), (j<ell), and

[
qL_{n+k}-L_{n+ell}=qL_{n+i}-L_{n+j}
]

holds for all (nge0). Put (h=k-i), (e=ell-j), and

[
C(d)=L_d-1-(-1)^d quad(dge1).
]

Then

[
oxed{e>h,qquad jequiv ipmod 2,qquad q^2 C(h)=C(e).}
]

*Proof.* Rearrangement gives
(q(L_{n+k}-L_{n+i})=L_{n+ell}-L_{n+j}).
Independence of the (alpha^n) and (eta^n) terms yields
[
qalpha^i(alpha^h-1)=alpha^j(alpha^e-1),qquad
qeta^i(eta^h-1)=eta^j(eta^e-1).
]
The algebraic norm of (alpha^d-1) is
[
(alpha^d-1)(eta^d-1)
=1+(-1)^d-L_d=-C(d).
]
Multiplying the two equations gives
(q^2(-1)^i C(h)=(-1)^j C(e)).
Both (C(h)) and (C(e)) are positive, hence (j-i) is even
and (q^2C(h)=C(e)). Since (qge2) and (C) is nondecreasing
and strictly increasing from (d=2) onward, (e>h). (square)

This is a necessary condition, not by itself a sufficiency claim.
Every accepted pattern must still satisfy the two consecutive-shift
equalities and positivity from the manuscript.

## 2. Classification when both gaps are even

The double-angle identity yields
[
C(2r)=L_{2r}-2=
egin{cases}
L_r^2,&r	ext{ odd},\
5F_r^2,&r	ext{ even}.
end{cases}
]

**Proposition.** For prescribed even gaps (h=2r) and (e=2m),
with (m>rge1), a positive stationary (T_q) collision with
integer (qge2) exists **if and only if** (r,m) have the
same parity and
[
q=egin{cases}
L_m/L_rinmathbb Z,&r,m	ext{ odd},\
F_m/F_rinmathbb Z,&r,m	ext{ even}.
end{cases}
]

*Proof.* The square-norm equation gives
(q^2C(2r)=C(2m)). With opposite parities,
this would equate the square of a nonzero rational
to (5) times the square of a nonzero rational, which
is impossible. With the same parity, taking the positive
square root gives the displayed quotient. Conversely,
the elementary identities
[
L_{n+2r}-L_n=
egin{cases}
L_rL_{n+r},&r	ext{ odd},\
5F_rF_{n+r},&r	ext{ even}
end{cases}
]
show, for either integral quotient, that
[
qL_{n+m-r}-L_n
=qL_{n+m+r}-L_{n+2m}>0
]
for all (nge1). The two index gaps are exactly (2r)
and (2m); shifting (n) produces infinitely many
distinct repeated positive values. (square)

Thus the Lucas/Fibonacci quotient conditions already present in
the manuscript **exhaust all stationary collisions whose two
first/second-index gaps are even**.

## 3. Odd-gap restrictions

For odd (d), (C(d)=L_d). For every (rge1),
(C(4r)=5F_{2r}^2). No Lucas number is divisible by (5),
as (L_nmod5) has period (4) and nonzero residues
(1,3,4,2) for (nge1).
Consequently a stationary pattern can **never** have one
odd gap and one gap divisible by (4): the equation
(q^2C(h)=C(e)) would have incompatible parity of
its (5)-adic valuation.

If the gaps have opposite parity, their even member
must therefore be (2mod4). The norm identity then
implies that the odd-index Lucas number involved is a
perfect square (the square of a rational number which is
an integer is an integer square). This gives a further
strong restriction without presuming that every norm
solution is a stationary identity.

The cases with both gaps odd reduce to
[
L_e=q^2L_h,qquad h,e	ext{ odd}, e>h,
]
plus the required shift identity. A simple closed
arithmetic classification for these remaining cases is
not established here.

## 4. Exact norm-pruned decision algorithm

The existing stationary theorem sets
(t=min{nge1:L_n>200(q+1)^4}), (K=12t+1).
Its complete search ranges imply
[
1le h=K-i<3t,qquad 1le e=ell-jle7t.
]
For (qge2), (q^2C(h)ge4); the values (C(e)) are
strictly increasing for (ege3). Therefore **each (h)
determines at most one candidate (e)**, by the norm equation.

For any such pair, the function
[
jlongmapsto L_{j+e}-L_j
]
is strictly increasing for (jge1) and (ege3).
The first of the two consecutive-shift equations
[
q(L_K-L_{K-h})=L_{j+e}-L_j
]
therefore determines at most one (j); binary search
within the proved bounds finds it. Check the second
equation, parity, and positive value to decide whether
the candidate gives a stationary collision.

`norm_stationary.py` implements this without floating point.
Once the Lucas values and the (C(e)) lookup table are
formed, the index search takes (O(tlog t)) integer
comparisons; bit complexity also depends on the sizes
of the Lucas integers. This is an independent,
necessary-and-sufficient implementation of the **already
proved** finite stationary criterion, not a new assumption
about the sufficiency of the norm equation.

`verify_norm_stationary.py` independently compares the
full returned pattern lists with the original exhaustive
two-shift search for all (q=2,ldots,200). The comparison
finds **26 norm-compatible gap pairs** across these 199
coefficients, and agrees on all **19** coefficients with
infinite (T_q/P_q) collisions. It also checks five further
shifts of every returned identity.

The current two manuscript PDFs remain unchanged; this
note and its verifier are additional research material.
