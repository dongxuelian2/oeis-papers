// Certified A077187 bounded-order extension, 745 <= r <= 1000.
// Requires C++17, GMP/GMPXX; no factorization of 10^r-1.
// g++ -O3 -std=c++17 single_period_order_1000.cpp -lgmpxx -lgmp -o order1000
// ./order1000
// Every (r,T,G) below is asserted; each prime divisor q of G is proved
// to have ord_q(10) != r. Hence all exact-order-r primes have nonzero drift.
// The unrestricted all-primes conjecture remains open.
#include <gmpxx.h>
#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;

static long ord10(int v) {
    if (v == 1) return 1;
    assert(gcd(v,10) == 1);
    int x=10%v; long a=1;
    while (x!=1) { x=(long long)x*10%v; ++a; assert(a<=v); }
    return a;
}
static int tail(int r) {
    while(r%2==0) r/=2;
    while(r%5==0) r/=5;
    return r;
}
static bool elementary(int r) {
    int v=tail(r),u=r/v;
    return 20%u==0 || v==1 || v==3 || v==9;
}
struct Geom { mpz_class P,S,J; };
static Geom geom(const mpz_class& q, unsigned n, const mpz_class& N) {
    mpz_class P=1,S=0,J=0,bp=q,bs=1,bj=0;
    unsigned long length=0,bl=1;
    while(n) {
        if(n&1) {
            J=(J+P*(length*bs+bj))%N;
            S=(S+P*bs)%N; P=P*bp%N; length+=bl;
        }
        n>>=1;
        if(n) {
            mpz_class j=(bj+bp*(bl*bs+bj))%N;
            mpz_class s=(bs+bp*bs)%N;
            mpz_class p=bp*bp%N;
            bj=j;bs=s;bp=p;bl*=2;
        }
    }
    return {P,S,J};
}
struct Result { long T; mpz_class G,U,V; };
static Result certificate(int r) {
    int v=tail(r);
    long T=lcm((long)r,ord10(v));
    mpz_class N; mpz_ui_pow_ui(N.get_mpz_t(),10,r); N-=1;
    mpz_class ten=10,C=0,Y=0;
    vector<mpz_class> powers(r);
    powers[0]=1;
    for(int i=1;i<r;++i) powers[i]=powers[i-1]*10;
    vector<Geom> cached(r);
    vector<bool> seen(r,false);
    // Starting from zero is correct: the stable T-layer monodromy
    // has diagonal part identity mod N. Its translation is the drift.
    for(long d=T+1;d<=2*T;++d) {
        int e=d%r,h=r/gcd((long)r,d);
        mpz_class hN=N*h,nmod;
        mpz_powm_ui(nmod.get_mpz_t(),ten.get_mpz_t(),d-1,hN.get_mpz_t());
        nmod=9*nmod%hN;
        mpz_class t=nmod/h, remainder=nmod%h;
        unsigned long b=remainder.get_ui();
        const mpz_class& q=powers[e];
        const mpz_class& L=powers[(d-1)%r];
        if(!seen[e]) { cached[e]=geom(q,h,N);seen[e]=true; }
        const Geom& gh=cached[e];
        Geom gb=geom(q,b,N);
        assert(gh.P==1);
        mpz_class S=(t*gh.S+gb.S)%N;
        mpz_class bino=t*(t-1)/2;
        mpz_class J=(t*gh.J+h*gh.S*bino+t*h*gb.S+gb.J)%N;
        unsigned long exp=((d%r)*b)%r;
        const mpz_class& A=powers[exp];
        const mpz_class& invA=powers[(r-exp)%r];
        C=(A*C+(q-1)*S-J)%N;
        if(C<0)C+=N;
        Y=(invA*(Y+L*S+J))%N;
        if(Y<0)Y+=N;
    }
    mpz_class G;
    mpz_gcd(G.get_mpz_t(),N.get_mpz_t(),C.get_mpz_t());
    mpz_gcd(G.get_mpz_t(),G.get_mpz_t(),Y.get_mpz_t());
    return {T,G,C,Y};
}
static bool isprime(unsigned long n) {
    if(n<2) return false;
    for(unsigned long i=2;i<=n/i;++i) if(n%i==0) return false;
    return true;
}
static int residue_order(unsigned long prime) {
    assert(isprime(prime) && prime!=2 && prime!=5);
    unsigned long x=10%prime;
    int d=1;
    while(x!=1) {x=x*10%prime; ++d;assert(d<=prime);}
    return d;
}
struct Row {int r;long T;unsigned long G;};
static const vector<Row> EXPECTED = {
    {752,17296,9},{760,6840,9},{775,2325,9},{776,9312,9},
    {784,2352,9},{792,792,891},{808,808,909},{816,816,459},
    {824,14008,9},{825,1650,27},{832,2496,9},{840,840,189},
    {848,11024,9},{850,6800,9},{856,45368,9},{864,864,243},
    {872,23544,9},{875,5250,9},{880,880,99},{888,888,999},
    {896,2688,9},{904,12656,9},{912,2736,27},{920,10120,99},
    {925,2775,9},{928,6496,9},{936,936,1053},{944,27376,9},
    {950,8550,9},{952,5712,9},{968,968,1089},{975,1950,27},
    {976,14640,9},{984,4920,27},{992,14880,9}
};
int main() {
    size_t row=0;
    for(int r=745;r<=1000;++r) {
        if(elementary(r))continue;
        assert(row<EXPECTED.size() && EXPECTED[row].r==r);
        Result z=certificate(r);
        assert(z.T==EXPECTED[row].T);
        assert(mpz_fits_ulong_p(z.G.get_mpz_t()));
        unsigned long g=z.G.get_ui();
        assert(g==EXPECTED[row].G && g>0);
        // Complete trial division of the entire (small) GCD.
        unsigned long t=g;
        for(unsigned long q=2;q<=t/q;++q) if(t%q==0) {
            assert(isprime(q) && q!=2 && q!=5);
            assert(residue_order(q)!=r);
            while(t%q==0)t/=q;
        }
        if(t>1) {
            assert(isprime(t) && t!=2 && t!=5);
            assert(residue_order(t)!=r);
        }
        // Independently derived prime-field residues are also pinned.
        if(r==856) {
            assert((z.U%857)==789 && (z.V%857)==388);
        }
        if(r==936) {
            assert((z.U%937)==61 && (z.V%937)==281);
        }
        cout<<r<<","<<z.T<<","<<g<<"\n";
        ++row;
    }
    assert(row==35);
    cerr<<"PASS: 35 exact-order classes, 745..1000; no true-order zero drift\n";
    cerr<<"PASS: independently cross-checked finite-field residues r=856,936\n";
    cerr<<"FULL OEIS CONJECTURE OPEN (only bounded-order theorem).\n";
}
