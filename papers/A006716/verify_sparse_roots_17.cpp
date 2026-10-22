// Full, exact A006716 root-support-17 exploration/certificate, sharded by unit digit.
// Compile: g++ -std=c++17 -O3 verify_sparse_roots_17.cpp -o /tmp/a006716_r17
// Run: /tmp/a006716_r17 1  (units 1,2,3,7,8,9 are exhaustive).
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

using Wide = unsigned __int128;
static uint16_t triple_mask[4][5][10][10]={};
static bool viable_second[5][10][10]={};

// Exact construction: every possible first 8 significant digits of x*x
// must be a word in {1,4,9}^8. Intersect rational intervals by integer math.
static void initialize_leading_masks(){
    Wide ten[17]; ten[0]=1;
    for(int i=1;i<17;++i)ten[i]=10*ten[i-1];
    struct Interval {Wide lo,hi;};
    vector<Interval> intervals;
    for(int j=1;j<=2;++j)for(int number=0;number<6561;++number){
        int v=number; Wide p=0;
        for(int i=0;i<8;++i){int c=v%3;v/=3;p=10*p+(c==0?1:c==1?4:9);}
        intervals.push_back({p*ten[j],(p+1)*ten[j]});
    }
    sort(intervals.begin(),intervals.end(),[](const Interval& a,const Interval& b){
        return a.lo<b.lo;
    });
    for(int g=1;g<=3;++g)for(int h=1;h<=4;++h){
        Wide den=ten[2*(g+h)];
        for(int a=1;a<=9;++a)for(int b=1;b<=9;++b)for(int c=1;c<=9;++c){
            Wide z=a*ten[g+h]+b*ten[h]+c;
            Wide L=z*z*ten[8],R=(z+1)*(z+1)*ten[8];
            size_t low=0,high=intervals.size();
            while(low<high){
                size_t mid=(low+high)/2;
                if(intervals[mid].hi*den<=L)low=mid+1;
                else high=mid;
            }
            if(low<intervals.size() && intervals[low].lo*den<R)
                triple_mask[g][h][a][b]|=(uint16_t(1)<<c);
        }
    }
    const int expected[4][5]={
        {},{0,49,25,13,0},{0,49,12,5,5},{0,4,0,0,0}
    };
    for(int g=1;g<=3;++g)for(int h=1;h<=4;++h){
        int count=0;
        for(int a=1;a<=9;++a)for(int b=1;b<=9;++b){
            count+=__builtin_popcount((unsigned)triple_mask[g][h][a][b]);
            for(int c=1;c<=9;++c)if(triple_mask[g][h][a][b]&(1<<c))
                viable_second[h][b][c]=true;
        }
        assert(count==expected[g][h]);
    }
}
constexpr int SUPPORT=17;

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

void enumerate(const cpp_int& x,int last,int previous,int used) {
    if(used==SUPPORT) {
        ++leaves;
        if(allowed_full_square(x*x)) solutions.push_back(x.convert_to<string>());
        return;
    }
    ++interior;
    int max_next=min(2*last+2,allowed_tail_width(x*x));
    if(used==SUPPORT-1)max_next=min(max_next,last+3);
    // Digit-sum bound: every eligible support-r square has <=81*r*r digits.
    // Thus its root's highest decimal exponent <=floor((81*r*r-1)/2).
    constexpr int EXP_CAP=(81*SUPPORT*SUPPORT-1)/2;
    if(max_next>EXP_CAP)max_next=EXP_CAP;
    if(max_next<=last){++prunes;return;}

    if(used==SUPPORT-1){
        int h=last-previous;
        if(h>4){++prunes;return;}
        int b=(x/pow10[last]).convert_to<int>();
        int c=((x/pow10[previous])%10).convert_to<int>();
        for(int next=last+1;next<=max_next;++next){
            int g=next-last;if(g>3)continue;
            for(int a=1;a<=9;++a){
                if(!(triple_mask[g][h][a][b]&(1<<c)))continue;
                enumerate(x+cpp_int(a)*pow10[next],next,last,used+1);
            }
        }
    } else if(used==SUPPORT-2) {
        int c=(x/pow10[last]).convert_to<int>();
        for(int next=last+1;next<=max_next;++next){
            int h=next-last;if(h>4)continue;
            for(int b=1;b<=9;++b){
                if(!viable_second[h][b][c])continue;
                enumerate(x+cpp_int(b)*pow10[next],next,last,used+1);
            }
        }
    } else {
        for(int next=last+1;next<=max_next;++next)
            for(int digit=1;digit<=9;++digit)
                enumerate(x+cpp_int(digit)*pow10[next],next,last,used+1);
    }
}
int main(int argc,char** argv) {
    if(argc!=2){cerr<<"Usage: "<<argv[0]<<" <units digit 1,2,3,7,8,9>\n";return 2;}
    int units=stoi(argv[1]);
    const vector<int> allowed_units={1,2,3,7,8,9};
    if(find(allowed_units.begin(),allowed_units.end(),units)==allowed_units.end())
        return 2;
    constexpr int MAX_EXP=(81*SUPPORT*SUPPORT-1)/2;
    initialize_leading_masks();
    pow10.resize(MAX_EXP+1);pow10[0]=1;
    for(int e=1;e<=MAX_EXP;++e)pow10[e]=10*pow10[e-1];
    enumerate(cpp_int(units),0,-1,1);
    sort(solutions.begin(),solutions.end());
    // Pinned from a complete six-class GitHub Actions audit.
    const uint64_t expected_leaves[10]={
      0,171650208,107967008,92701557,0,0,0,380875967,177741697,104052733
    };
    if(leaves!=expected_leaves[units] || !solutions.empty()){
      cerr<<"FAIL support 17, units="<<units<<" leaves="<<leaves<<" matches=";
      for(const auto& x:solutions)cerr<<x<<",";
      cerr<<"\\n";return 1;
    }
    cout<<"EXHAUSTED support=17 units="<<units<<" leaves="<<leaves
        <<" interior="<<interior<<" pruned="<<prunes<<" roots=";
    for(const auto& s:solutions)cout<<s<<",";
    cout<<"\n";
}
