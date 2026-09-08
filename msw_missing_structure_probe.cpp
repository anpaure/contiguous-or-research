#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>

using U32=std::uint32_t;

static bool dyck(U32 x,int m){int h=0;for(int i=0;i<2*m;++i){h+=((x>>i)&1U)?1:-1;if(h<0)return false;}return h==0;}
static std::pair<U32,int> g(U32 x,int m){
    std::vector<int> h(2*m);int z=0,d0=0;
    for(int i=0;i<2*m;++i){h[i]=z;if(!((x>>i)&1U)&&z==0)++d0;z+=((x>>i)&1U)?1:-1;}
    int c=0;for(int i=0;i<2*m;++i)if(!((x>>i)&1U)&&(h[i]==0||h[i]==1)&&++c==d0+1)return{x|(U32{1}<<i),i};
    __builtin_unreachable();
}
static std::pair<U32,int> h(U32 y,int m){
    std::vector<int> ht(2*m);int z=0,u1=0;
    for(int i=0;i<2*m;++i){ht[i]=z;if(((y>>i)&1U)&&z==1)++u1;z+=((y>>i)&1U)?1:-1;}
    int c=0;for(int i=0;i<2*m;++i)if(((y>>i)&1U)&&(ht[i]==0||ht[i]==1)&&++c==u1)return{y&~(U32{1}<<i),i};
    __builtin_unreachable();
}
struct Stats {int mn=0,mx=0,runs=0,ret0=0,down0=0,upm1=0,first=0,last=0;};
static Stats stats(U32 x,int n){
    Stats s;int z=0;s.first=x&1U;s.last=(x>>(n-1))&1U;s.runs=1;
    for(int i=0;i<n;++i){int b=(x>>i)&1U;if(i&&b!=int((x>>(i-1))&1U))++s.runs;if(!b&&z==0)++s.down0;if(b&&z==-1)++s.upm1;z+=b?1:-1;s.mn=std::min(s.mn,z);s.mx=std::max(s.mx,z);s.ret0+=z==0;}
    return s;
}
int main(int argc,char**argv){
    int m=argc>1?std::stoi(argv[1]):9,n=2*m;U32 lim=U32{1}<<n;
    std::unordered_map<U32,int> mult;mult.reserve(lim/4);
    for(U32 root=0;root<lim;++root)if(std::popcount(root)==m&&dyck(root,m)){
        U32 x=root;
        for(int i=0;i<m;++i){auto [y,a]=g(x,m);auto [nx,b]=h(y,m);++mult[x&nx];x=nx;}
    }
    using Key=std::pair<int,int>;
    std::map<Key,std::pair<std::uint64_t,std::uint64_t>> by_minmax,by_runs_min,by_returns;
    std::uint64_t total=0,miss=0;
    for(U32 x=0;x<lim;++x)if(std::popcount(x)==m-1){
        Stats s=stats(x,n);bool z=!mult.contains(x);++total;miss+=z;
        auto add=[&](auto& mp,Key k){++mp[k].first;mp[k].second+=z;};
        add(by_minmax,{s.mn,s.mx});add(by_runs_min,{s.runs,s.mn});add(by_returns,{s.down0,s.upm1});
    }
    std::cout<<"m="<<m<<" missing="<<miss<<'/'<<total<<"\n";
    auto dump=[&](const char*name,const auto&mp){std::cout<<name<<"\n";for(auto [k,v]:mp)if(v.second)std::cout<<k.first<<','<<k.second<<' '<<v.second<<'/'<<v.first<<"\n";};
    dump("min,max missing/total",by_minmax);dump("runs,min missing/total",by_runs_min);dump("down0,up(-1) missing/total",by_returns);
}
