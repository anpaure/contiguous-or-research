// Exact lower certificate for the saving over the four-block coefficient.
// Integer arithmetic selects and verifies every contributing cell, its feasible
// thresholds, its polynomial, and its integral. Square roots are rounded up and
// checked with integer comparisons; decimals are diagnostics only.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using I = __int128_t;
using U = __uint128_t;
using Aff = std::array<long long, 4>;
using Order = std::array<int, 4>;
constexpr int D = 2160;

struct Poly {
    std::array<I, 64> c{};
    static int id(int a, int b, int c) { return 16*a + 4*b + c; }
};

Poly affine(const Aff& a) {
    Poly p;
    p.c[0] = a[0]; p.c[16] = a[1]; p.c[4] = a[2]; p.c[1] = a[3];
    return p;
}

Poly add(Poly a, const Poly& b, I scale = 1) {
    for (int j = 0; j < 64; ++j) a.c[j] += scale*b.c[j];
    return a;
}

Poly scale(Poly a, I s) {
    for (auto& v : a.c) v *= s;
    return a;
}

Poly mul(const Poly& a, const Poly& b) {
    Poly out;
    for (int i = 0; i < 64; ++i) if (a.c[i]) {
        int x = i/16, y = (i/4)%4, z = i%4;
        for (int j = 0; j < 64; ++j) if (b.c[j]) {
            int xx = x+j/16, yy = y+(j/4)%4, zz = z+j%4;
            assert(xx+yy+zz <= 3);
            out.c[Poly::id(xx, yy, zz)] += a.c[i]*b.c[j];
        }
    }
    return out;
}

U checked_mul(U a, U b) {
    assert(!b || a <= ~U(0)/b);
    return a*b;
}

std::string decimal(U x) {
    if (!x) return "0";
    std::string out;
    while (x) { out.push_back(char('0'+x%10)); x /= 10; }
    std::reverse(out.begin(), out.end());
    return out;
}

struct Candidate {
    Order order{};
    // t = sum_i coeff[i]*length[i]/K, with global sorted length indices.
    Aff coeff{};
    bool positive_delta = true;
    bool exists = false;
};

I integer_cost(const std::array<long long, 4>& x, const std::array<long long, 4>& u, int K) {
    I v[4], w[4];
    for (int i = 0; i < 4; ++i) {
        int j = (i+1)%4;
        v[i] = I(K)*K*x[i]*x[j] - I(u[i])*(K*x[j]-u[j]);
        w[i] = std::max(std::min(K*x[i],u[j]), std::min(K*x[i]-u[i],K*x[j]));
    }
    return v[0]*w[2]+v[2]*w[0]+v[1]*w[3]+v[3]*w[1];
}

bool feasible(const Candidate& z, int i, int j, int l, int N, int K) {
    for (int corner = 0; corner < 8; ++corner) {
        std::array<long long,4> g{i+(corner&1), j+((corner>>1)&1),
                                  l+((corner>>2)&1), N};
        long long t = 0;
        for (int h = 0; h < 4; ++h) t += z.coeff[h]*g[h];
        long long a=g[z.order[0]], b=g[z.order[1]],
                  c=g[z.order[2]], d=g[z.order[3]];
        long long delta=d-c+b-a;
        if ((z.positive_delta && delta<0) || (!z.positive_delta && delta>0)) return false;
        std::array<long long,4> u{t, K*a-t, K*(b-a)+t, K*(c-b+a)-t};
        std::array<long long,4> x{a,b,c,d};
        for (int h=0; h<4; ++h) if (u[h]<0 || u[h]>K*x[h]) return false;
        long long eta = z.positive_delta ? delta : 0;
        long long cap = z.positive_delta ? a : d;
        if (t+K*eta > K*cap) return false;
    }
    return true;
}

Candidate choose(int i, int j, int l, int N, int K) {
    std::array<long long,4> global{2*i+1,2*j+1,2*l+1,2*N};
    constexpr Order cycles[] = {{0,1,2,3},{0,1,3,2},{0,2,1,3}};
    Candidate best;
    I best_cost = 0;
    for (const auto& cycle : cycles) for (int rotation=0; rotation<4; ++rotation) {
        Order order;
        for (int h=0; h<4; ++h) order[h]=cycle[(h+rotation)%4];
        long long a=global[order[0]], b=global[order[1]],
               c=global[order[2]], d=global[order[3]];
        long long p=b-a, q=c-b+a, delta=d-q, eta=std::max(delta,0LL);
        long long lo=std::max({0LL,a-b,-delta});
        long long hi=std::min({a,q,(delta>=0?a:d)-eta});
        if (lo>hi) continue;
        long long B=(b-d)*(c-a)+(p-a)*delta-2*a*q+(a+q)*eta;
        long long twice_A=2*std::min(a+c,b+d);
        long long t_num=std::clamp(-B,twice_A*lo,twice_A*hi);
        long long t_den=twice_A*a;
        int nearest=int((K*t_num+t_den/2)/t_den);
        std::vector<Aff> local;
        for (int e=-1; e<=1; ++e) local.push_back({std::clamp(nearest+e,0,K),0,0,0});
        local.push_back({0,0,0,0});              // 0
        local.push_back({K,0,0,0});              // a
        local.push_back({K,-K,0,0});             // a-b
        local.push_back({K,-K,K,0});             // c-b+a
        local.push_back({K,-K,K,-K});            // -delta
        local.push_back(delta>=0 ? Aff{2*K,-K,K,-K} : Aff{0,0,0,K});
        for (const auto& f : local) {
            Candidate z; z.exists=true; z.order=order; z.positive_delta=(delta>=0);
            for (int h=0; h<4; ++h) z.coeff[order[h]]=f[h];
            if (!feasible(z,i,j,l,N,K)) continue;
            long long tt=0;
            for (int h=0; h<4; ++h) tt += z.coeff[h]*global[h];
            I value=integer_cost({a,b,c,d},{tt,K*a-tt,K*p+tt,K*q-tt},K);
            if (!best.exists || value<best_cost) { best_cost=value; best=z; }
        }
    }
    return best;
}

U cell(int i, int j, int l, int N, int K, long long& feasible_count, long long& positive_count,
       bool trace=false) {
    Candidate z=choose(i,j,l,N,K);
    if (!z.exists) return 0;
    assert(feasible(z,i,j,l,N,K));
    ++feasible_count;
    std::array<Poly,4> g{affine({i,1,0,0}),affine({j,0,1,0}),
                          affine({l,0,0,1}),affine({N,0,0,0})};
    std::array<Poly,4> x;
    for (int h=0; h<4; ++h) x[h]=g[z.order[h]];
    Poly t;
    for (int h=0; h<4; ++h) t=add(t,g[h],z.coeff[h]);
    Poly delta=add(add(x[3],x[2],-1),add(x[1],x[0],-1));
    Poly eta=z.positive_delta ? delta : Poly{};
    std::array<Poly,4> u{t,add(scale(x[0],K),t,-1),
                         add(scale(add(x[1],x[0],-1),K),t),
                         add(scale(add(add(x[2],x[1],-1),x[0]),K),t,-1)};
    std::array<Poly,4> w{u[1],u[2],u[3],add(t,eta,K)}, v;
    for (int h=0; h<4; ++h) {
        int next=(h+1)%4;
        v[h]=add(scale(mul(x[h],x[next]),I(K)*K),mul(u[h],add(scale(x[next],K),u[next],-1)),-1);
    }
    Poly Q=add(add(mul(v[0],w[2]),mul(v[2],w[0])),
               add(mul(v[1],w[3]),mul(v[3],w[1])));
    I K3=I(K)*K*K;
    Poly P=scale(mul(mul(g[0],g[1]),add(g[2],g[3])),4*K3);
    // If a+b-c can be positive, subtract its full square. This is a lower
    // bound even in a cell that straddles the positive-part breakpoint.
    if (i+j+2-l > 0) {
        Poly r=add(add(g[0],g[1]),g[2],-1);
        P=add(P,mul(g[3],mul(r,r)),-K3);
    }
    Poly saving=add(P,Q,-4);
    I lower=saving.c[0];
    for (int h=1; h<64; ++h) lower += std::min(I(0),saving.c[h]);
    if (lower<0) return 0;
    ++positive_count;
    I moment=0;
    for (int h=0; h<64; ++h) if (saving.c[h]) {
        int a=h/16,b=(h/4)%4,c=h%4;
        assert(a+b+c<=3);
        int den=(a+1)*(a+2)*(b+1)*(b+2)*(c+1)*(c+2);
        assert(D%den==0);
        I num=I(i*(a+2)+a+1)*(j*(b+2)+b+1)*(l*(c+2)+c+1)*(D/den);
        moment += saving.c[h]*num;
    }
    assert(moment>=0);
    unsigned long long S=1ULL*N*N+1ULL*(i+1)*(i+1)+1ULL*(j+1)*(j+1)+1ULL*(l+1)*(l+1);
    unsigned long long root=static_cast<unsigned long long>(std::sqrt(static_cast<long double>(S)));
    while (root*root<S) ++root;
    while (root && (root-1)*(root-1)>=S) --root;
    assert(root*root>=S && (!root || (root-1)*(root-1)<S));
    U numerator=checked_mul(checked_mul(U(moment),U(N)*N),45360ULL*7);
    U denominator=checked_mul(checked_mul(checked_mul(U(4)*K*K*K,D),22),root);
    for (int h=0; h<5; ++h) denominator=checked_mul(denominator,S);
    assert(denominator <= ~U(0)/2);
    assert(numerator<denominator);
    U quotient=0, remainder=numerator;
    for (int h=0; h<64; ++h) {
        remainder *= 2;
        quotient *= 2;
        if (remainder>=denominator) { remainder-=denominator; ++quotient; }
    }
    if (trace) {
        std::cout << "{\"cell\":["<<i<<","<<j<<","<<l<<"],\"N\":"<<N<<",\"K\":"<<K
                  <<",\"positive_delta\":"<<(z.positive_delta?"true":"false")<<",\"order\":[";
        for (int h=0; h<4; ++h) std::cout<<(h?",":"")<<z.order[h];
        std::cout << "],\"coeff\":[";
        for (int h=0; h<4; ++h) std::cout<<(h?",":"")<<z.coeff[h];
        std::cout << "],\"poly\":[";
        for (int h=0; h<64; ++h) {
            I value=saving.c[h];
            std::cout<<(h?",":"")<<(value<0?"-":"")<<decimal(U(value<0?-value:value));
        }
        std::cout << "],\"moment\":"<<decimal(U(moment))<<",\"numerator\":"<<decimal(numerator)
                  <<",\"denominator\":"<<decimal(denominator)<<",\"quotient\":"<<decimal(quotient)<<"}\n";
    }
    return quotient;
}

int main(int argc,char** argv) {
    if (argc==5 && std::string(argv[1])=="--sample") {
        int N=std::atoi(argv[2]), K=std::atoi(argv[3]), tries=std::atoi(argv[4]);
        assert(N>=4 && N<=192 && K>=2 && K<=32 && tries>0 && tries<=10000);
        uint64_t state=906621;
        long long f=0,p=0;
        for (int h=0; h<tries; ++h) {
            std::array<int,3> index;
            for (auto& x:index) { state=state*6364136223846793005ULL+1; x=int((state>>32)%N); }
            std::sort(index.begin(),index.end());
            if (index[0]==index[1] || index[1]==index[2]) continue;
            cell(index[0],index[1],index[2],N,K,f,p,true);
        }
        return 0;
    }
    int N=argc>1?std::atoi(argv[1]):64;
    int K=argc>2?std::atoi(argv[2]):32;
    assert(N>=4 && N<=192 && K>=2 && K<=32);
    U sum=0;
    long long count=0, feasible_count=0, positive_count=0;
    // These disjoint boxes lie inside 0<a<b<c<1. The omitted diagonal slabs
    // and all noncontributing boxes have nonnegative true saving.
    for (int l=2; l<N; ++l) for (int j=1; j<l; ++j) for (int i=0; i<j; ++i) {
        sum += cell(i,j,l,N,K,feasible_count,positive_count);
        ++count;
    }
    std::cout << "N="<<N<<" K="<<K<<" cells="<<count
              <<" feasible="<<feasible_count<<" nonnegative="<<positive_count<<"\n";
    std::cout << "CERTIFIED saving >= "<<decimal(sum)<<" / 18446744073709551616\n";
    std::cout.precision(12);
    std::cout << "Diagnostic decimal: "<<static_cast<long double>(sum)/std::ldexp(1.0L,64)<<"\n";
    std::cout << "saving > 1/50: "<<(checked_mul(sum,50)>(U(1)<<64))<<"\n";
    std::cout << "saving > 49/2000: "<<(checked_mul(sum,2000)>checked_mul(U(1)<<64,49))<<"\n";
    if (N==192 && K==16) assert(checked_mul(sum,2000)>checked_mul(U(1)<<64,49));
}
