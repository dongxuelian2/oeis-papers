// Exact-integer, independent branch-and-bound verifier for A087354(20..25).
// g++ -std=c++17 -O3 verify_minima.cpp -o verify_minima && ./verify_minima
#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <cassert>
using U = unsigned __int128;
using ull = unsigned long long;

U parse(const char *p) { U v=0; while(*p) { v=10*v+(*p++-'0'); } return v; }
std::string str(U x) { if(!x)return "0"; std::string s; while(x){s.push_back(char('0'+x%10));x/=10;} return std::string(s.rbegin(),s.rend()); }
U isqrt_exact(U n) {
    if(!n)return 0;
    // sqrt gives a provisional estimate ONLY; exact integer corrections follow.
    U r=static_cast<ull>(std::sqrt(static_cast<long double>(n)));
    while((r+1)*(r+1)<=n)++r;
    while(r*r>n)--r;
    return r;
}
const std::array<U,27> pow10=[] {std::array<U,27> x{};x[0]=1;for(int i=1;i<27;i++)x[i]=x[i-1]*10;return x;}();

struct Search {
    int n,L;
    U cap,best;
    ull nodes=0,pruned=0,leaves=0;
    void dfs(U p,int d,int k){
        ++nodes;
        U upper=best?best:cap;
        U lo=p*pow10[L-d];
        if(lo>upper) {++pruned;return;}
        U hi=(p+1)*pow10[L-d]-1;
        if(hi>upper)hi=upper;
        U lowroot=lo?isqrt_exact(lo-1)+1:0;
        if(lowroot>isqrt_exact(hi)){++pruned;return;}
        if(k==n){if(d==L && isqrt_exact(p)*isqrt_exact(p)==p){++leaves;if(!best||p<best)best=p;} return;}
        int excess=L-d-(n-k);
        if(excess<0)return;
        constexpr int one[]={1,4,9},two[]={16,25,36,49,64,81};
        for(int b:one)dfs(p*10+b,d+1,k+1);
        if(excess>=1)for(int b:two)dfs(p*100+b,d+2,k+1);
    }
};
int main(){
    const std::vector<std::pair<int,const char*>> data={
        {20,"111125911149919941444"},
        {21,"444411911999914911441"},
        {22,"11199444494448114419449"},
        {23,"144949449149149194448144"},
        {24,"1111425414199449191191449"},
        {25,"41914991191911941194149136"}
    };
    for(auto [n,num]:data){
        U bound=parse(num);
        assert(isqrt_exact(bound)*isqrt_exact(bound)==bound);
        bool hit=false;
        int maxL=int(std::string(num).size());
        for(int L=n;L<=maxL;L++){
            Search s{n,L,bound,0};s.dfs(0,0,0);
            std::cout<<"n="<<n<<", L="<<L<<": nodes="<<s.nodes
                <<", pruned="<<s.pruned<<", square-leaves="<<s.leaves
                <<", minimum="<<str(s.best)<<'\n';
            if(s.best){assert(s.best==bound);hit=true;}
        }
        assert(hit);
        std::cout<<"CERTIFIED a("<<n<<")="<<num<<'\n';
    }
}
