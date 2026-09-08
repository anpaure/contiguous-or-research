#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using Mask=std::uint32_t; using Q=std::vector<int>;
static const int neg[4][9]={{1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},{1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}};
static const int posi[4][9]={{1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},{1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}};
static Mask in(const Q&q,int i,int r){Mask x=0;for(int t=0;t<r;++t)x|=Mask{1}<<(q[(i+2*t)%q.size()]-1);return x;}
static std::map<Mask,int> eff(const std::vector<Q>&p,const std::vector<Q>&n,int r){std::map<Mask,int>d;for(auto&q:p)for(int i=0;i<(int)q.size();++i)++d[in(q,i,r)];for(auto&q:n)for(int i=0;i<(int)q.size();++i)--d[in(q,i,r)];for(auto it=d.begin();it!=d.end();)if(!it->second)it=d.erase(it);else++it;return d;}
static Q anchored(const int* a,bool reverse) {
    Q q(a,a+9); auto it=std::find(q.begin(),q.end(),9); int at=it-q.begin(); q.erase(it);
    const int x[3]={reverse?11:10,9,reverse?10:11}; q.insert(q.begin()+at,x,x+3); return q;
}
int main(){
    for(int pairs=1;pairs<=5;++pairs)for(int gap=0;gap<=9;++gap){
        std::vector<Q>p,n;for(int s=0;s<2;++s)for(int z=0;z<4;++z){Q q((s?posi:neg)[z],(s?posi:neg)[z]+9);for(int x=0;x<2*pairs;++x)q.insert(q.begin()+gap,10+x);(s?p:n).push_back(q);}int m=4+pairs;auto a=eff(p,n,m),b=eff(p,n,m-1),c=eff(p,n,m-2);if(a.empty()&&b.empty())std::cout<<"SUCCESS pairs="<<pairs<<" gap="<<gap<<" lower="<<c.size()<<"\n";
    }
    for(int cp=0;cp<16;++cp)for(int cn=0;cn<16;++cn){
        std::vector<Q>p,n;for(int z=0;z<4;++z){p.push_back(anchored(posi[z],(cp>>z)&1));n.push_back(anchored(neg[z],(cn>>z)&1));}
        auto a=eff(p,n,5),b=eff(p,n,4),c=eff(p,n,3);
        if(a.empty()&&b.empty()&&!c.empty())std::cout<<"ANCHOR_SUCCESS cp="<<cp<<" cn="<<cn<<" lower="<<c.size()<<"\n";
    }
}
