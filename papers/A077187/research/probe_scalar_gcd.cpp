// A077187 exact repunit-ring SCALAR RANK probe (CONJECTURE ONLY).
//
// Tests whether gcd(N,U+V)==gcd(N,U,V) at each fixed order r.
// Neither this program nor any finite successful run proves the identity
// for all r. It uses GMP integers and the shortened stable period.
// g++ -O3 -std=c++17 probe_scalar_gcd.cpp -lgmpxx -lgmp -o scalar_probe
// ./scalar_probe 2 100
#include <gmpxx.h>
#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

static int order10(int v) {
    if (v == 1) return 1;
    assert(gcd(v, 10) == 1);
    int x = 10 % v, k = 1;
    while (x != 1) {
        x = (long long)x * 10 % v;
        ++k;
        assert(k <= v);
    }
    return k;
}

struct Sums {
    mpz_class power, sum, weighted;
};

static Sums geom(mpz_class q, unsigned n, const mpz_class& N) {
    mpz_class P = 1, S = 0, J = 0, bp = q, bs = 1, bj = 0;
    unsigned len = 0, blocklen = 1;
    while (n) {
        if (n & 1) {
            J = (J + P * (len * bs + bj)) % N;
            S = (S + P * bs) % N;
            P = (P * bp) % N;
            len += blocklen;
        }
        n >>= 1;
        if (n) {
            mpz_class nextJ = (bj + bp * (blocklen * bs + bj)) % N;
            mpz_class nextS = (bs + bp * bs) % N;
            bp = (bp * bp) % N;
            bs = nextS;
            bj = nextJ;
            blocklen *= 2;
        }
    }
    return {P, S, J};
}

static bool probe(int r) {
    assert(r >= 2);
    int v = r;
    for (int f : {2, 5}) while (v % f == 0) v /= f;
    int t = v / gcd(v, 9);
    long T = lcm((long)r, (long)order10(t));
    mpz_class N;
    mpz_ui_pow_ui(N.get_mpz_t(), 10, r);
    N -= 1;
    vector<mpz_class> pow10(r);
    pow10[0] = 1;
    for (int i = 1; i < r; ++i) pow10[i] = pow10[i - 1] * 10;
    mpz_class C = 0, Y = 0, ten = 10;
    for (long d = T + 1; d <= 2 * T; ++d) {
        int h = r / gcd((long)r, d);
        mpz_class hN = h * N, nmod;
        mpz_powm_ui(nmod.get_mpz_t(), ten.get_mpz_t(),
                    d - 1, hN.get_mpz_t());
        nmod = 9 * nmod % hN;
        mpz_class quotient = nmod / h;
        mpz_class remainder = nmod % h;
        unsigned b = remainder.get_ui();
        Sums full = geom(pow10[d % r], h, N);
        Sums extra = geom(pow10[d % r], b, N);
        assert(full.power == 1);
        mpz_class S = (quotient * full.sum + extra.sum) % N;
        // All divisions by 2 here are exact integer divisions,
        // performed before reduction modulo odd N.
        mpz_class choose2 = quotient * (quotient - 1) / 2;
        mpz_class J = (quotient * full.weighted
                      + h * full.sum * choose2
                      + quotient * h * extra.sum
                      + extra.weighted) % N;
        unsigned exp = ((d % r) * b) % r;
        const mpz_class& A = pow10[exp];
        const mpz_class& invA = pow10[(r - exp) % r];
        C = (A * C + (pow10[d % r] - 1) * S - J) % N;
        Y = (invA * (Y + pow10[(d - 1) % r] * S + J)) % N;
    }
    mpz_class scalar = (C + Y) % N, scalarGcd, vectorGcd;
    mpz_gcd(scalarGcd.get_mpz_t(), N.get_mpz_t(), scalar.get_mpz_t());
    mpz_gcd(vectorGcd.get_mpz_t(), N.get_mpz_t(), C.get_mpz_t());
    mpz_gcd(vectorGcd.get_mpz_t(), vectorGcd.get_mpz_t(), Y.get_mpz_t());
    if (scalarGcd != vectorGcd) {
        cout << "COUNTEREXAMPLE to scalar conjecture at r=" << r
             << " T=" << T << " scalar gcd=" << scalarGcd
             << " vector gcd=" << vectorGcd << "\n";
        return false;
    }
    return true;
}

int main(int argc, char** argv) {
    int lo = argc > 1 ? atoi(argv[1]) : 2;
    int hi = argc > 2 ? atoi(argv[2]) : 100;
    if (lo < 2 || hi < lo) return 3;
    for (int r = lo; r <= hi; ++r) {
        if (!probe(r)) return 2;
    }
    cout << "FINITE CHECK PASSED for " << lo << "<=r<=" << hi
         << "; GENERAL SCALAR GCD CONJECTURE OPEN.\n";
}
