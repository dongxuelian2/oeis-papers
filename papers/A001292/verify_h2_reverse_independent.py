from fractions import Fraction
from itertools import product
# Every unit residue coset at valuation 6 has a square, cube or valuation-7 witness.
def accepts6(r): return r%3==1 or r in (8,3,6)
for c,z in product((1,2,4,5,7,8),range(9)):
 assert any(accepts6((z-c*t)%9) for t in (0,3,6))
 assert any(accepts6((z-c*t)%9) for t in (8,2,5))
for k,r in ((4,8),(19,2),(22,5)):
 s=''.join(map(str,range(1,k+1)))
 q=(Fraction(int(s),10**len(s))-Fraction(1,10))/9
 assert q.denominator%3 and q.numerator*pow(q.denominator,-1,9)%9==r
# Negative branch at valuation 3: classify existence of cubes using cuts0,1.
for u in (1,2):
 bad=[]
 for z in (1,2,4,5,7,8):
  rr={(-z*pow(2,-1,9)+3*u*t)%9 for t in (0,1)}
  if not rr.intersection({1,8}):bad.append((27*z-1)%243)
 assert sorted(bad)==({1:[26,134],2:[107,215]}[u])
# Remaining negative branch: v>=4. k0,2,3 either square or valuation5;
# only coset2 remains, and k1 either square, valuation5 or reaches v>=6.
for u,a in product((1,2,4,5,7,8),range(9)):
 rs={(a+u*t)%9 for t in (0,3,6)}
 if any(r%3==1 or r in (3,6) for r in rs):continue
 b=(a+u)%9
 assert b%3==1 or b in (0,3,6)
print('PASS: independent exact constants, 108 coset tests, negative-branch class and lifting checks')
