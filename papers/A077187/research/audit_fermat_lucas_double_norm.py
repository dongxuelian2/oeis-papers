#!/usr/bin/env python3
"""Independent finite-field audit of Fermat-Lucas double norms.

No third-party libraries. Test generic coefficients and all three
drift types; this is a consistency audit, not the proof of identity.
"""
def order10(p):
    z, n = 10 % p, 1
    while z != 1:
        z = 10 * z % p
        n += 1
    return n


def lucas(p, r, A, H, B):
    def multiply(X, Y):
        return ((X[0]*Y[0]+X[1]*Y[2]) % p,
                (X[0]*Y[1]+X[1]*Y[3]) % p,
                (X[2]*Y[0]+X[3]*Y[2]) % p,
                (X[2]*Y[1]+X[3]*Y[3]) % p)
    mat, base = (1,0,0,1), (-H % p, -A*B % p,1,0)
    n = r
    while n:
        if n & 1:
            mat = multiply(mat, base)
        base = multiply(base, base)
        n >>= 1
    return (pow(A,r,p)+pow(B,r,p)-mat[0]-mat[3]) % p


def audit_one(p, A, B, H, U, V):
    r = order10(p)
    assert r >= 3
    outer = 1
    for j in range(p):
        R = lucas(p,r,(A+10*j*U)%p,H,(B+j*V)%p)
        outer = outer*R%p
    want = (lucas(p,r,A,H,B)
            * (1-pow(U,p-1,p)) * (1-pow(V,p-1,p))) % p
    assert outer == want,(p,U,V,outer,want)
    if p<=43:
        for j in (0,1,2):
            aj,bj=(A+10*j*U)%p,(B+j*V)%p
            direct=1
            for n in range(r):
                z=pow(10,n,p)
                direct=direct*(aj*z*z+H*z+bj)%p
            assert direct==lucas(p,r,aj,H,bj)
    return outer


def main():
    count=0
    for p in (7,13,17,23,29,37,43,73,101,137,211):
        H=-20*pow(81,-1,p)%p
        for U,V in ((0,0),(1,p-1),(3,4)):
            audit_one(p,19%p,29%p,H,U,V)
            count+=1
    assert count==33
    print("PASS 33 Fermat-Lucas exact double-norm identities")
    print("PASS independent direct cyclic-product comparisons")
    print("Nonzero drift gives zero double norm; zero drift remains open.")


if __name__=="__main__":
    main()
