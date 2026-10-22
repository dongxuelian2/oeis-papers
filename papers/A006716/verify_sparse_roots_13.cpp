// Independent exact-integer certificate for the A006716 support-13 class.
// Build: g++ -std=c++17 -O3 verify_sparse_roots_13.cpp -o sparse13
// Run: ./sparse13       (also independently verifies support 12)
// Requires only Boost.Multiprecision header files. No floating point.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using namespace std;

static vector<cpp_int> pow10;
static uint64_t leaves,interior_nodes,pruned;
static vector<string> solutions;
static int target;

static bool all_allowed(const cpp_int& sq) {
    string word=sq.convert_to<string>();
    return all_of(word.begin(),word.end(),[](char c){
        return c=='1'||c=='4'||c=='9';
    });
}

// If x is fixed below decimal exponent e, then every later root increment
// divisible by 10^e leaves x^2 unchanged modulo 10^e.
// Thus the first e digits of x^2 must already be from {1,4,9}.
static int permitted_low_width(const cpp_int& sq) {
    string word=sq.convert_to<string>();
    int width=0;
    for(auto it=word.rbegin();it!=word.rend();++it){
        if(*it!='1' && *it!='4' && *it!='9')break;
        ++width;
    }
    // If e exceeds the number of square digits, an implicit zero appears,
    // so this is also the exact upper bound for the next exponent.
    return width;
}

static void dfs(const cpp_int& root, int last, int support) {
    if(support==target) {
        ++leaves;
        if(all_allowed(root*root))solutions.push_back(root.convert_to<string>());
        return;
    }
    ++interior_nodes;
    const cpp_int sq=root*root;
    // Low-gap lemma e_(j+1)<=2e_j+2; high-gap lemma applies at the
    // FINAL root digit only: e_r<=e_(r-1)+3.
    int upper=min(2*last+2,permitted_low_width(sq));
    if(support==target-1)upper=min(upper,last+3);
    if(upper<=last) { ++pruned; return; }
    for(int e=last+1;e<=upper;++e) {
        for(int digit=1;digit<=9;++digit)
            dfs(root+cpp_int(digit)*pow10[e],e,support+1);
    }
}

static void check(int r,uint64_t expected_leaves,const vector<string>& expected){
    target=r;leaves=interior_nodes=pruned=0;solutions.clear();
    auto t0=chrono::steady_clock::now();
    for(int units=1;units<=9;++units) dfs(cpp_int(units),0,1);
    sort(solutions.begin(),solutions.end());
    assert(leaves==expected_leaves);
    assert(solutions==expected);
    cout<<"PASS support="<<r<<" leaves="<<leaves
        <<" interior="<<interior_nodes<<" pruned="<<pruned
        <<" roots="<<solutions.size()
        <<" seconds="<<chrono::duration<double>(
            chrono::steady_clock::now()-t0).count()<<"\n";
}

int main(){
    constexpr int MAX_EXP=(1<<13)-2;
    pow10.resize(MAX_EXP+1);
    pow10[0]=1;
    for(int e=1;e<=MAX_EXP;++e)pow10[e]=pow10[e-1]*10;
    check(12,23707917,{});
    check(13,91475739,{});
    cout<<"CERTIFIED: no A006716 roots with exactly 13 nonzero digits\n";
}
