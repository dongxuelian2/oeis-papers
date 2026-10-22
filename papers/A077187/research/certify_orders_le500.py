#!/usr/bin/env python3
"""A077187: exact universal-order certificates for every r <= 500.

For each order not already in the u|20 / 3-smooth classes, compute
G_r = gcd(10^r-1, U_r, V_r) with *integer arithmetic only*.
Prove that no prime with ord_p(10)=r can divide G_r, without factoring
10^r-1 and without enumerating its prime factors.

No SymPy, NumPy, GMP, floating point, primality test, or heuristic step.
Run: python research/certify_orders_le500.py
The run is finite and rigorous subject to inspection of the formulas/code.
The ALL-PRIMES A077187 conjecture remains OPEN for arbitrary r.
"""
from hashlib import sha256
from math import gcd, lcm

LIMIT = 500
EXPECTED_SHA256 = "6b4457a29bdf807ea748a96b8501c6af53c923629eeb323800389b40ae91af57"
# (r, T, G) for the 42 new order classes.
EXPECTED = [
    (56,168,9), (88,88,99), (104,312,9), (112,336,9),
    (136,272,9), (152,1368,9), (168,168,189), (175,1050,9),
    (176,176,99), (184,2024,99), (208,624,9), (224,672,9),
    (232,1624,9), (248,3720,9), (264,264,297), (272,272,153),
    (275,550,9), (280,840,9), (296,888,9), (304,2736,9),
    (312,312,351), (325,1950,9), (328,1640,9), (336,336,189),
    (344,7224,9), (350,1050,9), (352,352,99), (368,4048,99),
    (376,8648,9), (392,1176,9), (408,816,27), (416,1248,9),
    (424,5512,9), (425,6800,9), (440,440,99), (448,1344,9),
    (456,1368,27), (464,3248,9), (472,13688,9), (475,8550,9),
    (488,7320,9), (496,7440,9),
]

def split_order(r):
    """r=u*v, u=2^a 5^c, gcd(v,10)=1."""
    u, v = 1, r
    for factor in (2, 5):
        while v % factor == 0:
            v //= factor
            u *= factor
    return u, v

def already_covered(r):
    """Earlier results: u|20, or v is a 3-power with exponent <=8."""
    u, v = split_order(r)
    if 20 % u == 0:
        return True
    b = 0
    while v % 3 == 0:
        v //= 3
        b += 1
    return v == 1 and b <= 8

def multiplicative_order_10_mod_v(v):
    if v == 1:
        return 1
    assert gcd(10,v) == 1
    residue = 10 % v
    k = 1
    while residue != 1:
        residue = residue * (10 % v) % v
        k += 1
        assert k <= v
    return k

def geom(q, count, modulus):
    """Return (q^n, sum q^i, sum i*q^i) mod m, in O(log n).

    Concatenation identity: (P,S,J)_ab =
    (P_a P_b, S_a + P_a S_b, J_a + P_a (a S_b + J_b)).
    Lengths are tracked modulo m for weighted sums.
    """
    P,S,J,length = 1,0,0,0
    bp,bs,bj,bl = q,1,0,1
    while count:
        if count & 1:
            J = (J + P * (length * bs + bj)) % modulus
            S = (S + P * bs) % modulus
            P = P * bp % modulus
            length = (length + bl) % modulus
        count >>= 1
        if count:
            bj_new = (bj + bp * (bl * bs + bj)) % modulus
            bs_new = (bs + bp * bs) % modulus
            bp_new = bp * bp % modulus
            bl_new = 2 * bl % modulus
            bp,bs,bj,bl = bp_new,bs_new,bj_new,bl_new
    return P,S,J

def order_class_drift(r):
    """Returns (T, N_r, gcd(N_r,U_r,V_r), U_r, V_r).

    Uses 10^r == 1 mod N_r, where N_r=10^r-1.
    For layer d, q=10^d has exact order h=r/gcd(r,d) mod N_r.
    Write the enormous layer size n=9*10^(d-1) as n=t*h+b.
    Only t mod N_r is required; compute n mod (h*N_r) first.
    """
    assert r >= 2
    u,v = split_order(r)
    T = lcm(r, multiplicative_order_10_mod_v(v))
    N = 10**r - 1
    inv2 = (N+1)//2  # N odd
    C=Y=0
    L,q=1,10%N
    middle=None
    for d in range(1,2*T+1):
        h = r//gcd(r,d)
        nmod = 9*pow(10,d-1,h*N) % (h*N)
        t,b=divmod(nmod,h)
        ph,Sh,Jh=geom(q,h,N)
        pb,Sb,Jb=geom(q,b,N)
        assert ph == 1
        S=(t*Sh+Sb)%N
        J=(t*Jh + (h*Sh%N)*(t*(t-1)*inv2%N)
           + (t*h%N)*Sb + Jb)%N
        A=pb
        invA=pow(A,-1,N) # 10 and A are units mod 10^r-1
        C=(A*C+(q-1)*S-J)%N
        Y=invA*(Y+L*S+J)%N
        if d==T:middle=(C,Y)
        L,q=q,q*10%N
    U=(C-middle[0])%N
    V=(Y-middle[1])%N
    return T,N,gcd(N,U,V),U,V

def remove_allowed_factors(n, allowed):
    """Return 1 iff every prime factor of n is a factor of 'allowed'.

    No factoring either integer is needed: repeated gcd removal.
    """
    while n > 1:
        g=gcd(n,allowed)
        if g==1:break
        n//=g
    return n

def main():
    rows=[]
    for r in range(2,LIMIT+1):
        if already_covered(r):
            continue
        T,N,G,U,V=order_class_drift(r)
        # ord_p(10)=r implies r|(p-1), hence p>r.
        # Also p cannot be any of 2,3,5,11 in this range.
        # Thus p cannot divide 990*r.  G has only these factors.
        assert remove_allowed_factors(G,990*r)==1,(r,T,G)
        rows.append((r,T,G))
    assert rows == EXPECTED, (len(rows), rows)
    payload="".join(f"{r},{T},{G}\n" for r,T,G in rows).encode()
    assert sha256(payload).hexdigest()==EXPECTED_SHA256
    # Independent p-reductions of integer-ring vectors; exact residues
    # previously checked by direct forward prime-field layer recurrences.
    for r,p,u_expected,v_expected in [
        (56,7841,7833,1704), (88,617,405,356),
        (112,113,112,56), (152,457,284,321),
        (184,2393,1886,1984), (312,313,198,283),
    ]:
        T,N,G,U,V=order_class_drift(r)
        assert N%p==0 and pow(10,r,p)==1
        assert all(pow(10,r//q,p)!=1 for q in range(2,r+1)
                   if r%q==0 and all(q%d for d in range(2,int(q**0.5)+1)))
        assert (U%p,V%p)==(u_expected,v_expected),(r,p)
    print("PASS",len(rows),"new exact order classes, r<=500")
    print("PASS gcd certificate: every G_r is supported on primes dividing 990*r")
    print("PASS 6 prime-field cross-check vectors")
    print("SHA256",EXPECTED_SHA256)

if __name__=="__main__":
    main()
