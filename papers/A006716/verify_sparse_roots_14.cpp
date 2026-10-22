// Full, exact A006716 root-support-14 certificate, sharded by unit digit.
// Compile: g++ -std=c++17 -O3 verify_sparse_roots_14.cpp -o /tmp/a006716_r14
// Run: /tmp/a006716_r14 1  (units 1,2,3,7,8,9 are exhaustive).
// No floating-point decision and no numerical bound on the root is assumed.
// The six-leading-digit mask has an independent exact rational proof and
// generator in verify_leading_pairs.py.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using namespace std;

static vector<cpp_int> pow10;
static uint64_t leaves=0, interior=0, prunes=0;
static vector<string> solutions;
constexpr int SUPPORT=14;

int allowed_tail_width(const cpp_int& squared) {
    string s=squared.convert_to<string>();
    int width=0;
    for(auto it=s.rbegin();it!=s.rend();++it) {
        if(*it!='1' && *it!='4' && *it!='9')break;
        ++width;
    }
    return width;
}
bool allowed_full_square(const cpp_int& squared) {
    string s=squared.convert_to<string>();
    return all_of(s.begin(),s.end(),[](char c) {
        return c=='1'||c=='4'||c=='9';
    });
}
bool high_pair_possible(int gap,int top,int below) {
    // Exact rational interval containment against all {1,4,9}
    // six-digit prefixes, verified by verify_leading_pairs.py.
    static const unsigned short mask[4][10]={
      {},
      {0, (1<<1)|(1<<2)|(1<<3)|(1<<4),
       (1<<1)|(1<<2),
       (1<<1)|(1<<3)|(1<<4)|(1<<7)|(1<<8),
       (1<<3)|(1<<4), 0, (1<<4)|(1<<6)|(1<<7),
       0, 0, (1<<5)|(1<<7)|(1<<9)},
      {0, (1<<5)|(1<<6)|(1<<7)|(1<<9),
       (1<<2)|(1<<3)|(1<<4),
       (1<<1)|(1<<2)|(1<<3)|(1<<6)|(1<<7)|(1<<8),
       0,0,0, (1<<1)|(1<<2)|(1<<3)|(1<<6)|(1<<7),
       0,0},
      {0,0,0,0,0,0,0,(1<<7)|(1<<8),0,0}
    };
    return gap>=1 && gap<=3 && top>=1 && top<=9
        && below>=1 && below<=9 && (mask[gap][top]&(1<<below));
}

void enumerate(const cpp_int& x,int last,int used) {
    if(used==SUPPORT) {
        ++leaves;
        if(allowed_full_square(x*x))solutions.push_back(x.convert_to<string>());
        return;
    }
    ++interior;
    const cpp_int sq=x*x;
    int max_next=min(2*last+2, allowed_tail_width(sq));
    if(used==SUPPORT-1)max_next=min(max_next,last+3);
    if(max_next<=last){++prunes;return;}
    int preceding_top=0;
    if(used==SUPPORT-1)preceding_top=(x/pow10[last]).convert_to<int>();
    for(int e=last+1;e<=max_next;++e)for(int digit=1;digit<=9;++digit) {
        if(used==SUPPORT-1&&!high_pair_possible(e-last,digit,preceding_top))
            continue;
        enumerate(x+cpp_int(digit)*pow10[e],e,used+1);
    }
}

int main(int argc,char** argv) {
    if(argc!=2){cerr<<"Usage: "<<argv[0]<<" <units digit 1,2,3,7,8,9>\n";return 2;}
    int units=stoi(argv[1]);
    const vector<int> allowed_units={1,2,3,7,8,9};
    if(find(allowed_units.begin(),allowed_units.end(),units)==allowed_units.end())
        return 2;
    constexpr int MAX_EXP=(1<<SUPPORT)-2;
    pow10.resize(MAX_EXP+1);pow10[0]=1;
    for(int e=1;e<=MAX_EXP;++e)pow10[e]=10*pow10[e-1];
    enumerate(cpp_int(units),0,1);
    sort(solutions.begin(),solutions.end());
    const uint64_t counts[10]={
      0,12777251,8035316,6905447,0,0,0,28348050,13228782,7748312
    };
    const vector<string> expected = units==1
       ? vector<string>{"648070211589107021"} : vector<string>{};
    if(leaves!=counts[units] || solutions!=expected){
        cerr<<"FAIL units="<<units<<" leaves="<<leaves<<" solutions=";
        for(const auto& s:solutions)cerr<<s<<",";
        cerr<<"\n";return 1;
    }
    cout<<"PASS units="<<units<<" leaves="<<leaves
        <<" interior="<<interior<<" pruned="<<prunes<<" roots=";
    for(const auto& s:solutions)cout<<s<<",";
    cout<<"\n";
}
