// Arbitrary-order A077187 drift-gcd laboratory, not an all-orders proof.
// g++ -O3 -std=c++17 probe_universal_scalar_gcd.cpp -lgmpxx -lgmp -o probe
// ./probe 174 258 272 696 808 936 1014 2058 2662 4107 4624
//
// Computes full repunit-ring drift via ONE stable T-layer affine product,
// not by constructing giant mountain integers or factoring 10^r-1.
// Independent Python checks use the full 2T initial-state approach.
//
// Columns: r T gcd(N,U,V) gcd(N,U+V) gcd(N,10U+V) gcd(N,9T).
// Any mismatch is a real disproof of the proposed numerical GCD
// identity for that formal order, NOT automatically of OEIS A077187.
#include <gmpxx.h>
#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

static int coprime_tail(int x) {
    while (x % 2 == 0) x /= 2;
    while (x % 5 == 0) x /= 5;
    return x;
}
static int ord10_mod_v(int v) {
    if (v == 1) return 1;
    assert(gcd(v, 10) == 1);
    int x = 10 % v, k = 1;
    while (x != 1) {
        x = 10LL * x % v;
        ++k;
        assert(k <= v);
    }
    return k;
}
struct Geo {
    mpz_class P, S, J;
};
static Geo geometric(const mpz_class& q, int n, const mpz_class& mod) {
    mpz_class P = 1, S = 0, J = 0, bp = q, bs = 1, bj = 0;
    int len = 0, blen = 1;
    while (n) {
        if (n & 1) {
            J = (J + P * (len * bs + bj)) % mod;
            S = (S + P * bs) % mod;
            P = P * bp % mod;
            len += blen;
        }
        n >>= 1;
        if (n) {
            mpz_class nj = (bj + bp * (blen * bs + bj)) % mod;
            mpz_class ns = (bs + bp * bs) % mod;
            mpz_class np = bp * bp % mod;
            bj = nj; bs = ns; bp = np; blen *= 2;
        }
    }
    return {P, S, J};
}
static mpz_class exact_gcd(const mpz_class& a, const mpz_class& b) {
    mpz_class g;
    mpz_gcd(g.get_mpz_t(), a.get_mpz_t(), b.get_mpz_t());
    return g;
}
static bool check_order(int r) {
    assert(r >= 2 && r <= 20000);
    int v = coprime_tail(r);
    int T = lcm(r, ord10_mod_v(v));
    mpz_class mod;
    mpz_ui_pow_ui(mod.get_mpz_t(), 10, r);
    mod -= 1;
    mpz_class C = 0, Y = 0, ten = 10;
    vector<mpz_class> powers(r);
    powers[0] = 1;
    for (int k = 1; k < r; ++k) powers[k] = powers[k - 1] * 10;
    vector<Geo> cached(r);
    vector<char> computed(r, 0);

    // By the stable monodromy theorem, the displacement of this
    // affine product from zero is the actual S_(2T)-S_T drift mod N.
    for (int d = T + 1; d <= 2 * T; ++d) {
        int e = d % r, h = r / gcd(r, d);
        mpz_class hmod = mod * h, nmod;
        mpz_powm_ui(nmod.get_mpz_t(), ten.get_mpz_t(), d - 1,
                    hmod.get_mpz_t());
        nmod = 9 * nmod % hmod;
        mpz_class t = nmod / h, remain = nmod % h;
        int b = remain.get_si();

        const mpz_class& q = powers[e];
        const mpz_class& L = powers[(d - 1) % r];
        if (!computed[e]) {
            cached[e] = geometric(q, h, mod);
            computed[e] = 1;
        }
        const Geo& gh = cached[e];
        Geo gb = geometric(q, b, mod);
        assert(gh.P == 1);
        mpz_class sums = (t * gh.S + gb.S) % mod;
        mpz_class choose2 = t * (t - 1) / 2;
        mpz_class weighted = (t * gh.J + h * gh.S * choose2
                              + t * h * gb.S + gb.J) % mod;
        int exponent = (e * b) % r;
        const mpz_class& A = powers[exponent];
        const mpz_class& inverseA = powers[(r - exponent) % r];
        C = (A * C + (q - 1) * sums - weighted) % mod;
        Y = (inverseA * (Y + L * sums + weighted)) % mod;
    }
    mpz_class G = exact_gcd(exact_gcd(mod, C), Y);
    mpz_class H = exact_gcd(mod, C + Y);
    mpz_class K = exact_gcd(mod, 10 * C + Y);
    mpz_class expected = exact_gcd(mod, mpz_class(9 * T));
    bool ok = (G == expected && H == expected && K == expected);
    cout << r << "," << T << "," << G << "," << H << ","
         << K << "," << expected << (ok ? ",PASS" : ",FAIL") << "\n";
    return ok;
}
int main(int argc, char** argv) {
    bool ok = true;
    if (argc == 1) {
        for (int r : {174, 272, 696, 808, 936, 1014, 2058, 2662})
            ok = check_order(r) && ok;
    } else {
        for (int i = 1; i < argc; ++i)
            ok = check_order(atoi(argv[i])) && ok;
    }
    if (!ok)
        cerr << "FOUND A FINITE COUNTEREXAMPLE TO THE GCD PATTERN; "
             << "this alone does not disprove A077187.\n";
    else
        cerr << "Exact finite GCD tests passed. "
             << "Universal identity and A077187 remain OPEN.\n";
    return ok ? 0 : 1;
}
