#pragma GCC optimize("O3,unroll-loops")
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

using Mask = std::uint16_t;
using OldOrder = std::array<int, 9>;

static const std::array<OldOrder, 4> negative = {{
    {1,8,6,7,4,5,3,9,2}, {1,9,8,6,7,4,5,2,3},
    {1,5,3,9,8,6,7,2,4}, {1,7,3,9,4,5,8,2,6},
}};
static const std::array<OldOrder, 4> positive = {{
    {1,9,3,5,4,7,6,8,2}, {1,5,4,7,6,8,9,2,3},
    {1,7,6,8,9,3,5,2,4}, {1,8,5,4,9,3,7,2,6},
}};

static std::vector<int> ordinary(const OldOrder& q) {
    std::vector<int> c(9);
    for (int i=0;i<9;++i) c[i]=q[(2*i)%9];
    return c;
}

static std::vector<int> extend(const std::vector<int>& c,int point,int d) {
    std::vector<int> out;
    for(int i=0;i<9;++i){
        out.push_back(c[i]);
        if(i==point) out.push_back(10);
        if(i==(point+d)%9) out.push_back(11);
    }
    return out;
}

static Mask interval(const std::vector<int>& c,int s,int r){
    Mask x=0;
    for(int j=0;j<r;++j)x|=Mask{1}<<(c[(s+j)%11]-1);
    return x;
}

struct Row { std::array<std::array<std::vector<Mask>,36>,4> a; };
static Row build(const std::array<OldOrder,4>& side){
    Row out;
    for(int z=0;z<4;++z){
        auto c=ordinary(side[z]);
        for(int ch=0;ch<36;++ch){
            int p=ch%9,d=3+ch/9;
            auto e=extend(c,p,d);
            for(int r:{5,4,3})for(int s=0;s<11;++s)
                out.a[z][ch].push_back(interval(e,s,r));
        }
    }
    return out;
}

struct Sig {
    std::array<Mask,88> x{};
    bool operator==(const Sig& o)const{return x==o.x;}
};
struct Hash { size_t operator()(const Sig& s)const{
    std::uint64_t h=1469598103934665603ULL;
    for(Mask x:s.x){h^=x;h*=1099511628211ULL;}
    return h;
}};

static bool signature(const Row& R,const std::array<int,4>& c,Sig& sig,
                      std::vector<Mask>* deep=nullptr){
    std::vector<Mask> mid,low,dep;
    for(int z=0;z<4;++z){
        auto const& v=R.a[z][c[z]];
        mid.insert(mid.end(),v.begin(),v.begin()+11);
        low.insert(low.end(),v.begin()+11,v.begin()+22);
        dep.insert(dep.end(),v.begin()+22,v.end());
    }
    std::sort(mid.begin(),mid.end());
    if(std::adjacent_find(mid.begin(),mid.end())!=mid.end())return false;
    std::sort(low.begin(),low.end());
    for(int i=0;i<44;++i)sig.x[i]=mid[i];
    for(int i=0;i<44;++i)sig.x[44+i]=low[i];
    if(deep){std::sort(dep.begin(),dep.end());*deep=std::move(dep);}
    return true;
}

static std::array<int,4> decode(std::uint32_t q){
    std::array<int,4>a{};for(int&i:a){i=q%36;q/=36;}return a;
}

int main(){
    Row N=build(negative),P=build(positive);
    constexpr std::uint32_t total=36u*36u*36u*36u;
    std::unordered_map<Sig,std::uint32_t,Hash> tab;
    tab.reserve(total/2);
    std::uint64_t np=0,pp=0;
    for(std::uint32_t q=0;q<total;++q){auto a=decode(q);Sig s;
        if(signature(N,a,s)){++np;tab.try_emplace(s,q);}}
    std::cerr<<"negative_packings="<<np<<" signatures="<<tab.size()<<'\n';
    for(std::uint32_t q=0;q<total;++q){auto b=decode(q);Sig s;std::vector<Mask> pd;
        if(!signature(P,b,s,&pd))continue;++pp;
        auto it=tab.find(s);if(it==tab.end())continue;
        auto a=decode(it->second);Sig z;std::vector<Mask> nd;signature(N,a,z,&nd);
        std::cout<<"FOUND deep_equal="<<(nd==pd)<<"\nN";
        for(int x:a)std::cout<<' '<<x;
        std::cout<<"\nP";for(int x:b)std::cout<<' '<<x;std::cout<<'\n';return 0;
    }
    std::cout<<"NONE negative_packings="<<np<<" positive_packings="<<pp<<'\n';
}
