#include <gmpxx.h>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int main(int argc,char**argv){
 int lo=argc>=2?stoi(argv[1]):1,hi=argc>=3?stoi(argv[2]):728;
 for(int g=lo;g<=hi;g++){
  if(g%3==0)continue;
  ifstream in("norm_gamma_"+to_string(g)+".txt");
  string ns;in>>ns;
  if(ns.empty()){cerr<<"missing norm "<<g<<endl;return 2;}
  mpz_class N(ns,10),B=(N-1)/6561,S,E,x,G,y;
  unsigned long A=mpz_sizeinbase(B.get_mpz_t(),2)-1;
  mpz_class pp=1;unsigned long C=0;
  while(pp*5<=B){pp*=5;C++;}
  mpz_ui_pow_ui(S.get_mpz_t(),2,A);S*=pp;
  E=2187*S;
  mpz_class ten(10);
  mpz_powm(x.get_mpz_t(),ten.get_mpz_t(),E.get_mpz_t(),N.get_mpz_t());
  y=(x*x+x+1)%N;
  mpz_gcd(G.get_mpz_t(),N.get_mpz_t(),y.get_mpz_t());
  cout<<g<<" "<<A<<" "<<C<<" "<<G.get_str()<<"\n";
 }
}
