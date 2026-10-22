// Exact, exhaustive minimum-value certificate for A087354(26)..A087354(30) and A087354(36).
// This is a research verifier, separate from the manuscript.
// g++ -std=c++17 -O3 verify_minima_extended.cpp -o verify_ext && ./verify_ext
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using U = unsigned __int128;
using u64 = std::uint64_t;

static std::array<U, 39> powers{};
U parse(const std::string& s) {
    U x = 0;
    for (char c : s) { assert(c >= '0' && c <= '9'); x = 10*x + (c-'0'); }
    return x;
}
std::string decimal(U x) {
    if (!x) return "0";
    std::string s;
    while (x) { s.push_back(char('0' + x%10)); x /= 10; }
    std::reverse(s.begin(), s.end());
    return s;
}
// Floating point is only a starting estimate: ALL decisions use exact
// adjusted integer square roots. Products here are below 10^37.
U isqrt_exact(U x) {
    if (!x) return 0;
    U r = static_cast<std::uint64_t>(std::sqrt(static_cast<long double>(x)));
    while ((r+1)*(r+1) <= x) ++r;
    while (r*r > x) --r;
    return r;
}
bool square(U x) { U r = isqrt_exact(x); return r*r == x; }

bool has_partition(U number, int n) {
    const std::string s = decimal(number);
    const int L = int(s.size());
    std::vector<std::vector<bool>> dp(L+1, std::vector<bool>(n+1, false));
    dp[0][0] = true;
    for (int i=0; i<L; ++i) {
        if (s[i] == '0') continue; // no leading zero in a block
        for (int k=0; k<n; ++k) {
            if (!dp[i][k]) continue;
            U x = 0;
            // Each verified upper-bound witness has L <= n+2.
            // Hence a feasible block in any n-block partition has <=3 digits.
            for (int j=i; j<L && j<i+3; ++j) {
                x = 10*x + (s[j]-'0');
                if (square(x)) dp[j+1][k+1] = true;
            }
        }
    }
    return dp[L][n];
}

constexpr int one[] = {1,4,9};
constexpr int two[] = {16,25,36,49,64,81};
constexpr int three[] = {
    100,121,144,169,196,225,256,289,324,361,400,
    441,484,529,576,625,676,729,784,841,900,961
};

struct Search {
    int n, length;
    U cap, best = 0;
    u64 nodes = 0, square_gap_prunes = 0, square_leaves = 0;

    void dfs(U prefix, int digits, int blocks) {
        ++nodes;
        U lo = prefix * powers[length-digits];
        U hi = (prefix+1) * powers[length-digits] - 1;
        U upper = best && best<cap ? best : cap;
        if (hi>upper) hi=upper;
        if (lo>hi) { ++square_gap_prunes; return; }

        // The interval of ALL decimal completions of this prefix has
        // no square iff ceil(sqrt(lo)) > floor(sqrt(hi)).
        U first_root = lo ? isqrt_exact(lo-1)+1 : 0;
        if (first_root > isqrt_exact(hi)) {
            ++square_gap_prunes;
            return;
        }

        if (blocks==n) {
            if (digits==length && square(prefix)) {
                ++square_leaves;
                if (!best || prefix < best) best = prefix;
            }
            return;
        }
        int extra = length-digits-(n-blocks);
        if (extra<0) return;
        for (int b : one) dfs(prefix*10+b, digits+1, blocks+1);
        if (extra>=1)
            for (int b : two) dfs(prefix*100+b, digits+2, blocks+1);
        if (extra>=2)
            for (int b : three) dfs(prefix*1000+b, digits+3, blocks+1);
    }
};

int main() {
    powers[0] = 1;
    for (int i=1; i<int(powers.size()); ++i) powers[i]=10*powers[i-1];

    struct Entry { int n; const char* expected; };
    const std::vector<Entry> entries = {
        {26, "114491941251191919194194944"},
        {27, "1494991191499944141414491136"},
        {28, "14919999448111491414944114944"},
        {29, "1111191491149991691191911414161"},
        {30, "1111194441113699414944949914441"},
        {36, "419994999149149944149149944191494441"}
    };
    for (const auto& entry : entries) {
        U claim = parse(entry.expected);
        int Lmax = int(std::string(entry.expected).size());
        assert(Lmax <= entry.n+2 && square(claim));
        assert(has_partition(claim, entry.n));
        bool located=false;
        for (int L=entry.n; L<=Lmax; ++L) {
            Search search{entry.n,L,claim};
            search.dfs(0,0,0);
            std::cout << "n=" << entry.n << " L=" << L
                << " nodes=" << search.nodes
                << " square-gap-prunes=" << search.square_gap_prunes
                << " square-leaves=" << search.square_leaves
                << " least=" << decimal(search.best) << "\n";
            if (L<Lmax) assert(search.best == 0);
            else { assert(search.best == claim); located=true; }
        }
        assert(located);
        std::cout << "CERTIFIED a(" << entry.n << ")="
                  << entry.expected << "\n";
    }
    std::cout << "ALL EXACT TESTS PASSED\n";
}
