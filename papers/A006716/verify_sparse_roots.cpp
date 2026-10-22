// Exact exhaustive A006716 roots with <= 12 nonzero decimal digits.
// g++ -O3 -std=c++17 verify_sparse_roots.cpp -o /tmp/sparse && /tmp/sparse
// Uses Boost.Multiprecision integer arithmetic, never floating point.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using namespace std;
static constexpr int MAX_SUPPORT=12;
static constexpr int MAX_EXP=(1<<MAX_SUPPORT)-2;
static vector<cpp_int> ten;
static unsigned long long final_nodes=0;
static vector<cpp_int> found;
static int target=0;

bool allowed_suffix(cpp_int residue, int width) {
    for(int i=0;i<width;i++) {
        unsigned digit=(residue%10).convert_to<unsigned>();
        if(digit!=1 && digit!=4 && digit!=9)return false;
        residue/=10;
    }
    return true;
}
bool allowed_square(const cpp_int& x) {
    const string s=(x*x).convert_to<string>();
    for(char c:s)if(c!='1' && c!='4' && c!='9')return false;
    return true;
}
void search(const cpp_int& x,int last_exp,int support) {
    if(support==target) {
        ++final_nodes;
        if(allowed_square(x))found.push_back(x);
        return;
    }
    const cpp_int squared=x*x;
    // The top-gap lemma e_r<=e_(r-1)+3 is applicable at FINAL
    // digit insertion only. Intermediate partial roots can be completed.
    const int high=(target==12 && support==11)
        ? min(2*last_exp+2,last_exp+3)
        : 2*last_exp+2;
    for(int e=last_exp+1;e<=high;e++) {
        assert(e<=MAX_EXP);
        if(!allowed_suffix(squared%ten[e],e))continue;
        for(int d=1;d<=9;d++)search(x+cpp_int(d)*ten[e],e,support+1);
    }
}
int main(int argc,char** argv) {
    ten.resize(MAX_EXP+1);
    ten[0]=1;
    for(int i=1;i<=MAX_EXP;i++)ten[i]=10*ten[i-1];
    const vector<vector<string>> expected={
        {},
        {"1","2","3","7"},
        {"12","21","38","107"},
        {"212","70107"},
        {},
        {"31488"},
        {"387288"},
        {"95610729"},
        {},
        {"446653271","3148717107","21081079479"},
        {},
        {},
        {}
    };
    const array<unsigned long long,13> expected_nodes={
        0,9,63,171,558,2007,7677,28494,110511,
        423567,1638540,6319638,23707917
    };
    int begin=1, end=MAX_SUPPORT;
    if(argc>1){begin=stoi(argv[1]);end=begin;}
    assert(begin>=1&&end<=MAX_SUPPORT);
    int total_roots=0;
    for(target=begin;target<=end;target++){
        final_nodes=0;
        found.clear();
        for(int d=1;d<=9;d++)search(cpp_int(d),0,1);
        sort(found.begin(),found.end());
        vector<string> got;
        for(const auto& x:found)got.push_back(x.convert_to<string>());
        if(got!=expected[target]||final_nodes!=expected_nodes[target]){
            cerr<<"FAIL support "<<target<<" candidates "<<final_nodes<<" roots ";
            for(const auto& x:got)cerr<<x<<" ";
            cerr<<"\n";
            return 1;
        }
        total_roots+=int(got.size());
        cout<<"PASS support="<<target<<" candidates="<<final_nodes
            <<" roots="<<got.size()<<endl;
    }
    if(begin==1 && end==MAX_SUPPORT) {
        assert(total_roots==16);
        cout<<"CERTIFIED 16 roots with <=12 nonzero decimal digits"<<endl;
    }
}
