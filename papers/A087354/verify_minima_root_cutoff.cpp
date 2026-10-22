// Exact square-root-interval certificate for OEIS A087354(31..34).
// g++ -O3 -std=c++17 verify_minima_root_cutoff.cpp -o /tmp/check && /tmp/check
// No floating-point comparison is used to accept or exclude a square.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using U=unsigned __int128;
using u64=unsigned long long;
static U pow10[39];

U parse(const std::string& s) {
    U v=0; for(char c:s){assert(c>='0'&&c<='9');v=10*v+(c-'0');}return v;
}
std::string dec(U v) {
    if(!v)return "0";
    std::string s;while(v){s.push_back(char('0'+v%10));v/=10;}
    std::reverse(s.begin(),s.end());return s;
}
U root(U v) {
    if(!v)return 0;
    U r=static_cast<u64>(sqrtl(static_cast<long double>(v)));
    while((r+1)*(r+1)<=v)++r;
    while(r*r>v)--r;
    return r;
}
bool square(U v){U r=root(v);return r*r==v;}
constexpr int Q1[]={1,4,9}, Q2[]={16,25,36,49,64,81};
constexpr int Q3[]={100,121,144,169,196,225,256,289,324,361,400,441,
                    484,529,576,625,676,729,784,841,900,961};

// Exact parsing: e=L-n extra digits implies only square blocks of length
// at most e+1. dp[pos][used extra digits] avoids any floating point.
bool full_parse(U v,int L,int e) {
    int digits[39];
    for(int i=L-1;i>=0;--i){digits[i]=int(v%10);v/=10;}
    if(v)return false;
    if(digits[0]==0)return false;
    bool dp[40][3]={};dp[0][0]=true;
    for(int i=0;i<L;++i)for(int q=0;q<=e;++q)if(dp[i][q]){
        for(int t:Q1)if(digits[i]==t)dp[i+1][q]=true;
        if(q+1<=e&&i+1<L){
            int x=10*digits[i]+digits[i+1];
            for(int t:Q2)if(x==t)dp[i+2][q+1]=true;
        }
        if(q+2<=e&&i+2<L){
            int x=100*digits[i]+10*digits[i+1]+digits[i+2];
            for(int t:Q3)if(x==t)dp[i+3][q+2]=true;
        }
    }
    return dp[L][e];
}
// Fast necessary-and-sufficient filter for e=0,1,2.
// The general e=2 case uses the exact DP above.
bool feasible(U v,int L,int e) {
    if(e==2)return full_parse(v,L,e);
    int d[39],bad[2],count=0;
    for(int i=L-1;i>=0;--i){
        int z=int(v%10);v/=10;d[i]=z;
        if(z!=1&&z!=4&&z!=9){
            if(count<2)bad[count]=i;
            if(++count>2*e)return false;
        }
    }
    if(v||d[0]==0)return false;
    if(e==0)return count==0;
    for(int j=0;j<L-1;++j){
        if(count==1&&(bad[0]<j||bad[0]>j+1))continue;
        if(count==2&&(!((bad[0]==j||bad[0]==j+1)&&
                        (bad[1]==j||bad[1]==j+1))))continue;
        int z=10*d[j]+d[j+1];
        for(int t:Q2)if(z==t)return true;
    }
    return false;
}
struct Search {
    int n,L;
    U cap,best=0;
    u64 nodes=0,prunes=0,root_candidates=0,hits=0;
    void visit(U p,int d,int k){
        ++nodes;
        U upper=best?best:cap;
        U lo=p*pow10[L-d];
        if(lo>upper){++prunes;return;}
        U hi=(p+1)*pow10[L-d]-1;
        if(hi>upper)hi=upper;
        U first=lo?root(lo-1)+1:0, last=root(hi);
        if(first>last){++prunes;return;}
        // Every square in this prefix interval is now tested directly.
        // Integer roots cannot be skipped: [first,last] is exact.
        if(last-first<=1 || d>=L/2+2){
            for(U r=first;r<=last;++r){
                U x=r*r;++root_candidates;
                if(feasible(x,L,L-n)){
                    ++hits;
                    if(!best||x<best)best=x;
                }
            }
            return;
        }
        if(k>=n)return;
        int remaining_extra=L-d-(n-k);
        if(remaining_extra<0)return;
        for(int z:Q1)visit(10*p+z,d+1,k+1);
        if(remaining_extra>=1)
            for(int z:Q2)visit(100*p+z,d+2,k+1);
        if(remaining_extra>=2)
            for(int z:Q3)visit(1000*p+z,d+3,k+1);
    }
};
int main(){
    pow10[0]=1;for(int j=1;j<39;++j)pow10[j]=10*pow10[j-1];
    struct Test{int n;const char* minimum;};
    const std::vector<Test> tests={
        {31,"49914994111911949994369194414144"},
        {32,"1111114494199449941144494641164944"},
        {33,"1144999199499994444141914194949136"},
        {34,"19144941911414919911419125114194449"}
    };
    for(const auto& t:tests){
        U target=parse(t.minimum);
        int maxL=std::string(t.minimum).size();
        assert(square(target)&&full_parse(target,maxL,maxL-t.n));
        bool obtained=false;
        for(int L=t.n;L<=maxL;++L){
            Search s{t.n,L,target};
            s.visit(0,0,0);
            std::cout<<"n="<<t.n<<" L="<<L
                     <<" nodes="<<s.nodes
                     <<" pruned="<<s.prunes
                     <<" roots="<<s.root_candidates
                     <<" hits="<<s.hits
                     <<" least="<<dec(s.best)<<"\n";
            if(L<maxL)assert(s.best==0);
            else{assert(s.best==target);obtained=true;}
        }
        assert(obtained);
        std::cout<<"CERTIFIED a("<<t.n<<")="<<t.minimum<<"\n";
    }
}
