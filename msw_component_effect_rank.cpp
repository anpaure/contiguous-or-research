#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <utility>
#include <vector>

using U32 = std::uint32_t;
static constexpr int MOD = 1000000007;

struct DSU {
    std::vector<int> p, sz;
    explicit DSU(int n) : p(n), sz(n, 1) { std::iota(p.begin(), p.end(), 0); }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    void unite(int a, int b) {
        a = find(a); b = find(b); if (a == b) return;
        if (sz[a] < sz[b]) std::swap(a, b);
        p[b] = a; sz[a] += sz[b];
    }
};

static std::pair<U32,int> apply_g(U32 x, int m) {
    std::vector<int> before(2*m); int h=0,d0=0;
    for (int i=0;i<2*m;++i) { before[i]=h; if (!((x>>i)&1U) && h==0) ++d0; h += ((x>>i)&1U)?1:-1; }
    int ord=0; for (int i=0;i<2*m;++i) if (!((x>>i)&1U) && (before[i]==0||before[i]==1))
        if (++ord==d0+1) return {x|(U32{1}<<i),i};
    assert(false); return {};
}
static std::pair<U32,int> apply_h(U32 y, int m) {
    std::vector<int> before(2*m); int h=0,u1=0;
    for (int i=0;i<2*m;++i) { before[i]=h; if (((y>>i)&1U)&&h==1) ++u1; h += ((y>>i)&1U)?1:-1; }
    int ord=0; for (int i=0;i<2*m;++i) if (((y>>i)&1U) && (before[i]==0||before[i]==1))
        if (++ord==u1) return {y&~(U32{1}<<i),i};
    assert(false); return {};
}
static long long binom(int n,int k) { long long z=1; if(k<0||k>n)return 0; for(int i=1;i<=k;++i)z=z*(n-k+i)/i; return z; }
static U32 swap_bits(U32 s,int u,int v) { if (((s>>u)^(s>>v))&1U) s^=(U32{1}<<u)|(U32{1}<<v); return s; }

struct Factor {
    int m,n,blocks=0; std::vector<int> owner; std::vector<U32> middle;
    std::vector<std::vector<int>> q; std::vector<U32> dyck;
    explicit Factor(int mm):m(mm),n(2*mm+1),owner(U32{1}<<n,-1){ gen(0,0,0,0); assert(blocks==binom(2*m,m)/(m+1)); }
    void add(U32 x0) {
        dyck.push_back(x0);
        U32 x=x0; std::vector<int> w; w.reserve(n);
        for(int e=0;e<m;++e){auto g=apply_g(x,m);auto h=apply_h(g.first,m);w.push_back(g.second);w.push_back(h.second);x=h.first;} w.push_back(2*m); q.push_back(w);
        for(int i=0;i<n;++i){U32 s=0;for(int t=0;t<m;++t)s|=U32{1}<<w[(i+1+2*t)%n];assert(owner[s]<0);owner[s]=blocks;middle.push_back(s);} ++blocks;
    }
    void gen(int pos,int up,int down,U32 mask){if(pos==2*m){add(mask);return;}if(up<m)gen(pos+1,up+1,down,mask|(U32{1}<<pos));if(down<up)gen(pos+1,up,down+1,mask);}
};

using Sparse = std::map<U32,int>;
static void add_intervals(Sparse& d,const std::vector<int>&q,int n,int r,int sign,int u,int v,bool tr){
    for(int i=0;i<n;++i){U32 s=0;for(int t=0;t<r;++t){int x=q[(i+2*t)%n];if(tr){if(x==u)x=v;else if(x==v)x=u;}s|=U32{1}<<x;}int &z=d[s];z+=sign;if(z==0)d.erase(s);}
}
static Sparse effect(const Factor&f,const std::vector<int>&ids,int u,int v,int r){Sparse d;for(int id:ids){add_intervals(d,f.q[id],f.n,r,-1,u,v,false);add_intervals(d,f.q[id],f.n,r,+1,u,v,true);}return d;}
static int invmod(long long a){long long b=MOD-2,r=1;while(b){if(b&1)r=r*a%MOD;a=a*a%MOD;b>>=1;}return int(r);}
static void axpy(Sparse& a,const Sparse& b,int c){
    for(auto [x,y]:b){long long z=(a.count(x)?a[x]:0)+(long long)c*y;z%=MOD;if(z<0)z+=MOD;if(z)a[x]=int(z);else a.erase(x);}
}

int main(int argc,char**argv){
    int m=argc>1?std::stoi(argv[1]):7,u=argc>2?std::stoi(argv[2])-1:1,v=argc>3?std::stoi(argv[3])-1:2;
    Factor f(m); DSU d(f.blocks); for(U32 s:f.middle)d.unite(f.owner[s],f.owner[swap_bits(s,u,v)]);
    std::map<int,std::vector<int>> groups;for(int i=0;i<f.blocks;++i)groups[d.find(i)].push_back(i);
    std::vector<std::vector<int>> comps;for(auto &kv:groups)comps.push_back(kv.second);
    if(argc>4 && std::string(argv[4])=="dump"){
        for(size_t ci=0;ci<comps.size();++ci){
            Sparse a=effect(f,comps[ci],u,v,m-1);
            std::cout<<"COMP "<<ci<<" size="<<comps[ci].size()<<" words=";
            for(int id:comps[ci]){for(int p=0;p<2*m;++p)std::cout<<((f.dyck[id]>>p)&1U);std::cout<<",";}
            std::cout<<" effect=";
            for(auto [s,z]:a){int h=0,eta=2*m+1;for(int p=0;p<2*m;++p){h+=((s>>p)&1U)?1:-1;if(h<0){eta=p+1;break;}}std::cout<<(z>0?'+':'-')<<s<<"@"<<eta<<"z"<<((s>>(2*m))&1U)<<",";}
            std::cout<<"\n";
        }
        return 0;
    }
    std::map<U32,std::pair<Sparse,std::vector<int>>> piv;
    std::vector<std::vector<int>> kernel;
    std::vector<U32> pivot_for(comps.size(),0);
    for(int c=0;c<(int)comps.size();++c){
        Sparse a=effect(f,comps[c],u,v,m-1);for(auto &kv:a){kv.second%=MOD;if(kv.second<0)kv.second+=MOD;}std::vector<int> rel(c+1);rel[c]=1;
        while(!a.empty()){
            U32 p=a.begin()->first;auto it=piv.find(p);if(it==piv.end()){
                int z=invmod(a.begin()->second);for(auto &kv:a)kv.second=(long long)kv.second*z%MOD;for(int &x:rel)x=(long long)x*z%MOD;piv[p]={a,rel};pivot_for[c]=p;break;
            }
            int c0=(MOD-a.begin()->second)%MOD;axpy(a,it->second.first,c0);auto &rr=it->second.second;if(rel.size()<rr.size())rel.resize(rr.size());for(size_t j=0;j<rr.size();++j)rel[j]=(rel[j]+(long long)c0*rr[j])%MOD;
        }
        if(a.empty())kernel.push_back(rel);
    }
    std::cout<<"m="<<m<<" components="<<comps.size()<<" rank="<<piv.size()<<" nullity="<<kernel.size()<<" pivots=";
    for(const auto &kv:piv)std::cout<<kv.first<<",";
    std::cout<<" by_component=";for(size_t i=0;i<pivot_for.size();++i){std::cout<<i<<":"<<pivot_for[i]<<"{";for(int b=0;b<2*m+1;++b)if((pivot_for[i]>>b)&1U)std::cout<<b+1<<".";std::cout<<"},";}std::cout<<"\n";
    for(size_t z=0;z<kernel.size()&&z<8;++z){Sparse low;for(size_t c=0;c<kernel[z].size();++c)if(kernel[z][c]){Sparse e=effect(f,comps[c],u,v,m-2);for(auto &kv:e){kv.second%=MOD;if(kv.second<0)kv.second+=MOD;}axpy(low,e,kernel[z][c]);}std::cout<<" kernel="<<z<<" lower_support="<<low.size()<<" coeffs=";for(size_t c=0;c<kernel[z].size();++c)if(kernel[z][c])std::cout<<c<<":"<<kernel[z][c]<<",";std::cout<<"\n";}
}
