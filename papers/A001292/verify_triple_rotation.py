"""Exact three-block Jacobi identity and actual full-rotation certificates.

No factorization or primality assertion is used.
"""
from math import gcd


def jacobi(a, n):
    assert n > 0 and n % 2
    sign = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


for v in range(1, 200, 2):
    B = 6*v-2
    M = (B*B+B+1)//3
    assert M == 12*v*v-6*v+1 and gcd(6*v, M) == 1
    sign = (-1)**((v-1)//2)
    assert jacobi(v, M) == jacobi(2, M) == sign
    assert jacobi(3, M) == jacobi(B+2, M) == -1

words = ['']
for m in range(1, 121):
    words.append(words[-1]+str(m))
for d in (2, 3):
    B = 10**d
    L = B//10
    M = (B*B+B+1)//3
    for m in range(L, min(L+12, B)):
        t, r = divmod(m-L+1, 3)
        tail = (0, m, (m-1)*B+m)[r]
        expected = (B**r*(int(words[L-1])+t*(B+2))+tail) % M
        assert int(words[m]) % M == expected

M = 333667
assert len(words[105]) == 207
assert int(words[99]) % M == 242665
assert int(words[105]) % M == 244669
assert 100000**2 % M == 10
assert 307823**2 % M == 244669
assert pow(10, 207, M) == 1
W = int(words[105])
for k in range(105):
    length = len(words[k])
    U = int(words[k]) if k else 0
    literal = int(words[105][length:]+words[k])
    exact = 10**length*W-(10**207-1)*U
    assert exact == literal
    root = 307823*pow(100000, length, M) % M
    assert root*root % M == literal % M
print('PASS: Jacobi proof identities, full-prefix grouping and all105 actual rotation roots.')
print('No integer-square rotation or conjecture exclusion inferred.')
