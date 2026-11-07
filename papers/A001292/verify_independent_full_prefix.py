#!/usr/bin/env python3
"""Independent finite corroboration, never a replacement for the written proof."""
from fractions import Fraction as F
from pathlib import Path
import json


def valuation(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


W = [0]
digits = [""]
lengths = [0]
for k in range(1, 10001):
    width = len(str(k))
    W.append(W[-1] * 10**width + k)
    lengths.append(lengths[-1] + width)
    if k <= 300:
        digits.append(digits[-1] + str(k))
    if k >= 10:
        b = 10**width
        j = k*(b-1)+b
        for p in (2,5):
            assert valuation(W[k],p) == valuation(j,p)
            assert valuation(W[k],p) < lengths[k]
        assert 2**valuation(W[k],2) * 5**valuation(W[k],5) < b*b

pairs = negative = previous = same = 0
for m in range(10,301):
    d = len(str(m))
    B = 10**d
    L = B//10
    C = B-1
    t = lengths[L-1]
    G = 10**t
    A = C*C*W[L-1]+L*C+1
    N = m-L+1
    M = m*C+B
    assert C*C*W[m] == A*B**N-M
    for k in range(1,m):
        s = lengths[k]
        U = W[k]
        V = 10**s
        coefficient = V*A-G*C*C*U
        correction = V*M-C*C*U
        rotation = int(digits[m][s:]+digits[m][:s])
        assert C*C*rotation == coefficient*B**N-correction
        assert rotation % V == U
        assert coefficient >= C*C*10**(t-1)
        assert abs(correction) < B*B*V
        if k < L:
            previous += 1
            assert coefficient//V >= L*C+1
        else:
            same += 1
            assert coefficient == G*(k*C+B)
        negative += correction < 0
        pairs += 1

curvature_cases = 0
for e in (2,3,5,7,11,101):
    for q in (F(1,10),F(1),F(2),F(5)):
        for a in (F(1,3),F(2),F(10)):
            aqe = a*q**e
            for b_ratio in (F(1,10),F(1,2),F(99,100)):
                b = b_ratio*e*aqe
                for z_ratio in (F(-100),F(-1),F(0),F(1,10),F(99,100)):
                    z = z_ratio*aqe
                    g = aqe-z
                    gp = e*a*q**(e-1)-b/q
                    gpp = e*(e-1)*a*q**(e-2)+b/q**2
                    assert g > 0 and gp > 0
                    numerator = e*g*gpp-(e-1)*gp*gp
                    rhs = (e*a*q**(e-2)*((2*e-1)*b-e*(e-1)*z)
                           -(e*b*z+(e-1)*b*b)/q**2)
                    assert numerator == rhs
                    h_derivative = (-e*(e-1)*b+e*b*z/aqe+(e-2)*b*b/aqe)
                    assert h_derivative < 0
                    curvature_cases += 1

for d in range(3,1001):
    L = 10**(d-1)
    t = ((9*d-10)*L+1)//9
    assert F(t,d)-7 >= F(L,2)
    assert F(t,d) < L

certificate = {
    "status": "PASS",
    "valuation_prefixes": {"first":10,"last":10000,"exact_J_equality":True},
    "rotation_identity_pairs":pairs,
    "same_width_pairs":same,
    "earlier_width_pairs":previous,
    "negative_correction_pairs":negative,
    "exact_rational_curvature_cases":curvature_cases,
    "h_range_widths":[3,1000],
    "scope":"Finite corroboration only. General proof and every exponent quantifier were reviewed separately."
}
text = json.dumps(certificate,indent=2,sort_keys=True)
Path(__file__).with_name("independent-full-prefix-certificate.json").write_text(text+"\n")
print(text)
