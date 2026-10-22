// A077187 unrestricted-order finite drift scan (2026-10-18).
// Exact F_p layer arithmetic, with no floating point and no giant mountain integers.
// WARNING: finite scan only; does not prove universal nonzero drift.
// g++ -O3 -std=c++17 drift_scan_general.cpp -o drift_scan_general
// ./drift_scan_general 5000
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <vector>
using namespace std;

static int modpow(int a, long long n, int p) {
    int z = 1;
    while (n) {
        if (n & 1) z = (long long)z * a % p;
        a = (long long)a * a % p; n >>= 1;
    }
    return z;
}
static bool isprime(int n) {
    if (n < 2) return false;
    for (int j = 2; j*j <= n; ++j) if (n%j == 0) return false;
    return true;
}
static int order(int a, int n) {
    if (n == 1) return 1;
    if (gcd(a, n) != 1) return -1;
    int x = a % n, t = 1;
    while (x != 1) { x = (long long)x * (a % n) % n; ++t; }
    return t;
}
static int nonnegative(long long x, int p) {
    int y = x % p;
    return y < 0 ? y + p : y;
}
int main(int argc, char **argv) {
    int limit = argc >= 2 ? atoi(argv[1]) : 5000;
    if (limit < 12 || limit > 50000) {
        fprintf(stderr, "choose 12 <= limit <= 50000 (larger limits may be slow)\n");
        return 2;
    }
    long long sumT = 0;
    int checked = 0, zero = 0, witnesses = 0, maxT = 0, identity = 0;
    for (int p = 7; p < limit; ++p) {
        if (!isprime(p) || p == 11) continue; // 11 | M(2)=121
        const int r = order(10, p);
        int v = r;
        while (v%2 == 0) v /= 2;
        while (v%5 == 0) v /= 5;
        const int T = lcm(r, order(10, v));
        sumT += T;
        maxT = max(maxT, T);

        vector<int> pow10(r), invden(p);
        pow10[0] = 1;
        for (int i = 1; i < r; ++i)
            pow10[i] = (long long)pow10[i-1]*10%p;
        for (int q = 2; q < p; ++q)
            invden[q] = modpow(q-1, p-2, p);

        int C = 0, Y = 0, L = 1, q = 10%p, Lr = 1;
        int C1 = 0, Y1 = 0;
        for (int d = 1; d <= 2*T; ++d) {
            int N = (long long)9*L%p;
            int exp = (long long)(9LL*d%r)*Lr%r;
            int A = pow10[exp], invA = pow10[(r-exp)%r];
            int S, J;
            if (q == 1) {
                S = N;
                J = (long long)N * nonnegative(N-1, p) % p
                    * ((p+1)/2) % p;
            } else {
                const int inv = invden[q];
                S = (long long)nonnegative(A-1, p)*inv%p;
                const int numerator = nonnegative(
                    (long long)q-(long long)N*A
                    + (long long)(N-1)*A*q, p);
                J = (long long)numerator*inv%p*inv%p;
            }
            int c = nonnegative((long long)(q-1)*S-J, p);
            C = ((long long)A*C+c)%p;
            Y = (long long)invA*(Y+(long long)L*S+J)%p;
            if (d == T) { C1 = C; Y1 = Y; }
            L = q;
            q = (long long)q*10%p;
            Lr = (long long)Lr*10%r;
        }
        int U = nonnegative(C-C1, p), V = nonnegative(Y-Y1, p);
        if (v == 1 || v == 3 || v == 9) {
            const int target = 9LL*modpow(100%p, p-2, p)%p;
            if ((U+V)%p != target) {
                printf("FAIL 9/100 identity p=%d r=%d v=%d U=%d V=%d\n",
                       p, r, v, U, V);
                return 1;
            }
            ++identity;
        }
        ++checked;
        if (U == 0 && V == 0) {
            ++zero;
            printf("ZERO_DRIFT p=%d r=%d T=%d\n", p, r, T);
            continue;
        }
        int slope0 = (10LL*U+V)%p;
        int slope1 = (1000LL*U+V)%p;
        if (slope0 == 0 && slope1 == 0) {
            printf("ERROR both slopes zero p=%d\n", p); return 1;
        }
        int slope = slope0 ? slope0 : slope1;
        int offset = slope0 ? 0 : 1;
        int constant = slope0
            ? (10LL*C1+Y1+1)%p : (1000LL*C1+Y1+121)%p;
        int j = 1+(long long)nonnegative(-constant, p)
                       *modpow(slope, p-2, p)%p;
        if (j < 1 || j > p ||
            (constant + (long long)(j-1)*slope)%p != 0) {
            printf("ERROR witness verification p=%d\n", p); return 1;
        }
        ++witnesses;
        (void)offset; // offset is 0 or 1, as proved in the research note
    }
    printf("PASS primes=%d witnesses=%d zero=%d identity_checks=%d "
           "sumT=%lld maxT=%d\n", checked, witnesses, zero,
           identity, sumT, maxT);
    return 0;
}
