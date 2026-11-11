// g++ -O3 -std=c++17 -fopenmp pointwise_rotation.cpp -lgmpxx -lgmp -o pointwise_rotation
// --candidate m k prefix_digits suffix_digits: exact window/root certificate.
// --odd-candidate m k exponent prefix_digits suffix_digits: odd exponent coprime to 5.
// --late max_cut threads: complete R_(m,k)<H_k^2 square audit, 10<=k<=max_cut.
#include <gmpxx.h>
#include <omp.h>
#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using Z=mpz_class;
using U=unsigned long;
Z power(U b,U e){ Z z;mpz_ui_pow_ui(z.get_mpz_t(),b,e);return z; }
Z mod(const Z&a,const Z&m){Z z;mpz_mod(z.get_mpz_t(),a.get_mpz_t(),m.get_mpz_t());return z;}
Z inv(const Z&a,const Z&m){Z z;if(!mpz_invert(z.get_mpz_t(),a.get_mpz_t(),m.get_mpz_t()))throw std::runtime_error("inverse");return z;}
Z floorroot(const Z&a,U e=2){Z z;mpz_root(z.get_mpz_t(),a.get_mpz_t(),e);return z;}
Z raised(const Z&a,U e){Z z;mpz_pow_ui(z.get_mpz_t(),a.get_mpz_t(),e);return z;}
U width(U n){U d=1;while(n>=10){n/=10;++d;}return d;}
U digits(const Z&n){U d=mpz_sizeinbase(n.get_mpz_t(),10);return n<power(10,d-1)?d-1:d;}
U D(U m){if(m<10)return m;U d=width(m),L=1;for(U i=1;i<d;++i)L*=10;return ((9*d-10)*L+1)/9+d*(m-L+1);}
U endpoint(U E){U d=1,L=1,t=0;while(E>t+9*d*L){t+=9*d*L;++d;L*=10;}
 U q=(E-t)/d;return (E-t)%d==0 && q>0?L+q-1:0;}
Z prefix(U m){Z W=0;U L=1,B=10;while(L<=m){U j=std::min(m,B-1),C=B-1;
 Z numerator=(Z(C)*C*W+Z(L)*C+1)*power(B,j-L+1)-(Z(j)*C+B);
 Z divisor=Z(C)*C;if(numerator%divisor!=0)throw std::runtime_error("prefix division");
 W=numerator/divisor;L=B;B*=10;}return W;}
Z rotation(U m,U k){return power(10,D(k))*prefix(m)-(power(10,D(m))-1)*prefix(k);}
std::vector<Z> unique(std::vector<Z> v){std::sort(v.begin(),v.end());v.erase(std::unique(v.begin(),v.end()),v.end());return v;}
std::vector<Z> unitroots(Z u,U p,U n){
 Z M=power(p,n);u=mod(u,M);std::vector<Z> out;
 if(p==2 && n<=3){for(U r=1;r<M.get_ui();r+=2)if(Z(r)*r%M==u)out.push_back(Z(r));return out;}
 Z r;U e;
 if(p==2){if(u%8!=1)return {};r=1;e=3;}
 else {if(u%5==1)r=1;else if(u%5==4)r=2;else return {};e=1;}
 while(e<n){U t=std::min(n,p==2?2*e-2:2*e);Z q=power(p,t);
  if(p==2)r=mod(r+((u-r*r)/2)*inv(r,q),q);
  else r=mod(r+(u-r*r)*inv(2*r,q),q);
  e=t;
 }
 out={r,mod(-r,M)};if(p==2){out.push_back(mod(r+M/2,M));out.push_back(mod(-r+M/2,M));}
 return unique(out);
}
struct Roots{Z H;std::vector<Z> roots;bool odd=false;};
std::vector<Z> unitpowerroots(const Z&u,U p,U n,U e){
 if(e==2)return unitroots(u,p,n);
 if(p==2&&n==1)return {Z(1)};
 Z M=power(p,n),phi=(p-1)*power(p,n-1),exponent=inv(Z(e),phi),r;
 mpz_powm(r.get_mpz_t(),u.get_mpz_t(),exponent.get_mpz_t(),M.get_mpz_t());
 return {r};
}
Roots compressed(const Z&u,U s,U e=2){
 if(u<=0)throw std::runtime_error("positive suffix required");
 U v2=mpz_scan1(u.get_mpz_t(),0);Z odd5;const Z five=5;
 U v5=mpz_remove(odd5.get_mpz_t(),u.get_mpz_t(),five.get_mpz_t());
 if(v2>=s||v5>=s)throw std::runtime_error("increase suffix precision");
 if(v2%e||v5%e)return {0,{},true};
 U a=v2/e,b=v5/e;Z m2=power(2,s-(e-1)*a),m5=power(5,s-(e-1)*b),H=m2*m5;
 auto r2=unitpowerroots(u/power(2,v2),2,s-v2,e);if(r2.empty())return {H,{},false};
 auto r5=unitpowerroots(odd5,5,s-v5,e);if(r5.empty())return {H,{},false};
 Z inverse=inv(m2,m5),z2=power(2,a),z5=power(5,b);std::vector<Z> roots;
 for(const auto&x:r2)for(const auto&y:r5){Z v=x*z2;roots.push_back(mod(v+m2*mod((y*z5-v)*inverse,m5),H));}
 return {H,unique(roots),false};
}
void candidate(U m,U k,U h,U q,U e=2){
 if(m<2||m>10000000||k>=m||h<1||h>D(m)||q<3||q>D(m))throw std::runtime_error("candidate range");
 if(e<2||e>1000000||(e!=2&&(e%2==0||e%5==0)))throw std::runtime_error("exponent must be 2 or odd and coprime to 5");
 Z R=rotation(m,k);U E=D(m);Z scale=power(10,E-h),P=R/scale;
 Z low=floorroot(P*scale-1,e)+1,high=floorroot((P+1)*scale-1,e);
 Z suffix=mod(R,power(10,q));auto rs=compressed(suffix,q,e);
 std::cout<<"R="<<R<<"\nE="<<E<<" suffix="<<suffix<<"\nroot_interval=["<<low<<","<<high<<"]\n";
 std::cout<<"H="<<rs.H<<"\n";U count=0;
 for(const auto&r:rs.roots){std::cout<<"ROOT_CLASS "<<r<<"\n";
  if(mod(raised(r,e)-suffix,power(10,q))!=0)throw std::runtime_error("root congruence");
  Z a,b;Z u=low-r,v=high-r;mpz_cdiv_q(a.get_mpz_t(),u.get_mpz_t(),rs.H.get_mpz_t());
  mpz_fdiv_q(b.get_mpz_t(),v.get_mpz_t(),rs.H.get_mpz_t());if(a<0)a=0;
  if(b-a>1000)throw std::runtime_error("increase suffix precision: too many candidates");
  for(Z j=a;j<=b;++j){Z y=r+j*rs.H;std::cout<<"CANDIDATE "<<y<<(e==2?" SQUARE ":" POWER ")<<raised(y,e)<<"\n";++count;}
 }
 std::cout<<"WINDOW_CANDIDATES="<<count<<"\n";
}
void late(U limit,int threads){
 if(limit<10||limit>10000000||threads<1)throw std::runtime_error("late audit range");
 omp_set_num_threads(threads);const U chunk=128;
 unsigned long long branches=0,gaps=0,earlier=0,comparisons=0,heads=0,squares=0,odd=0,unit=0,local=0;
 auto start=std::chrono::steady_clock::now();
 #pragma omp parallel for schedule(dynamic) reduction(+:branches,gaps,earlier,comparisons,heads,squares,odd,unit,local)
 for(U begin=10;begin<=limit;begin+=chunk){
  Z W=prefix(begin-1);U s=D(begin-1);
  for(U k=begin;k<=limit&&k<begin+chunk;++k){U w=width(k);W=W*power(10,w)+k;s+=w;
   auto rs=compressed(W,s);if(rs.odd){++odd;continue;}if(rs.roots.empty()){++unit;continue;}++local;
   Z M=power(10,s);
   for(const auto&r:rs.roots){++branches;Z square=r*r;
    if(mod(square,M)!=W)throw std::runtime_error("full-prefix congruence");
    U E=digits(square),m=endpoint(E);if(!m){++gaps;continue;}if(m<=k){++earlier;continue;}++comparisons;
    Z head=square/power(10,E-width(k+1));
    if(head!=k+1)continue;
    ++heads;bool equal=square==rotation(m,k);squares+=equal;
    #pragma omp critical
    std::cout<<"HEAD_MATCH k="<<k<<" m="<<m<<" square="<<equal<<"\n";
   }
  }
 }
 double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 std::cout<<"max_cut="<<limit<<" threads="<<threads<<" odd="<<odd<<" unit="<<unit<<" local="<<local
 <<" branches="<<branches<<" digit_gaps="<<gaps<<" earlier="<<earlier<<" comparisons="<<comparisons
 <<" head_matches="<<heads<<" squares="<<squares<<" seconds="<<elapsed<<"\n";
}
int main(int argc,char**argv){try{
 if(argc==6&&std::string(argv[1])=="--candidate")candidate(std::stoul(argv[2]),std::stoul(argv[3]),std::stoul(argv[4]),std::stoul(argv[5]));
 else if(argc==7&&std::string(argv[1])=="--odd-candidate")candidate(std::stoul(argv[2]),std::stoul(argv[3]),std::stoul(argv[5]),std::stoul(argv[6]),std::stoul(argv[4]));
 else if(argc==4&&std::string(argv[1])=="--late")late(std::stoul(argv[2]),std::stoi(argv[3]));
 else throw std::runtime_error("usage: --candidate m k prefix_digits suffix_digits | --odd-candidate m k exponent prefix_digits suffix_digits | --late max_cut threads");
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
