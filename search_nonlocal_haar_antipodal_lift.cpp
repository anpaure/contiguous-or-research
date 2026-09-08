#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using Mask=std::uint32_t;using Q=std::vector<int>;
static const int neg0[4][9]={{1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},{1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}};
static const int pos0[4][9]={{1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},{1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}};
static Mask in(const Q&q,int i,int r){Mask x=0;for(int t=0;t<r;++t)x|=Mask{1}<<(q[(i+2*t)%q.size()]-1);return x;}
static std::string canon(Q p){int n=p.size(),at=std::find(p.begin(),p.end(),1)-p.begin();std::rotate(p.begin(),p.begin()+at,p.end());Q r(n);r[0]=1;for(int i=1;i<n;++i)r[i]=p[n-i];Q z=std::min(p,r);return std::string(z.begin(),z.end());}
static std::vector<Q> options(const int*a){Q q(a,a+9),p(9);for(int i=0;i<9;++i)p[i]=q[(2*i)%9];std::unordered_set<std::string>seen;std::vector<Q>out;for(int gx=0;gx<9;++gx)for(int gy=0;gy<9;++gy)for(int sameorder=0;sameorder<(gx==gy?2:1);++sameorder){Q z;for(int i=0;i<9;++i){z.push_back(p[i]);if(i==gx&&i==gy){z.push_back(sameorder?11:10);z.push_back(sameorder?10:11);}else{if(i==gx)z.push_back(10);if(i==gy)z.push_back(11);}}int x=std::find(z.begin(),z.end(),10)-z.begin(),y=std::find(z.begin(),z.end(),11)-z.begin(),d=std::abs(x-y);d=std::min(d,11-d);if(d!=5)continue;auto key=canon(z);if(!seen.insert(key).second)continue;Q pc(key.begin(),key.end()),qq(11);for(int i=0;i<11;++i)qq[(2*i)%11]=pc[i];out.push_back(qq);}return out;}
struct Sig{std::array<std::uint64_t,2>h{};bool operator==(const Sig&o)const{return h==o.h;}};struct Hash{size_t operator()(Sig const&s)const{return s.h[0]^(s.h[1]*0x9e3779b97f4a7c15ULL);}};
static Sig signature(const std::array<Q,4>&q){Sig s{{1469598103934665603ULL,1099511628211ULL}};std::vector<unsigned char>c(1<<11);for(auto&z:q)for(int r:{4,5})for(int i=0;i<11;++i)++c[in(z,i,r)];for(auto z:c){s.h[0]^=z;s.h[0]*=1099511628211ULL;s.h[1]^=z+0x9d;s.h[1]*=14029467366897019727ULL;}return s;}
static bool exactsame(const std::array<Q,4>&a,const std::array<Q,4>&b){for(int r:{4,5}){std::vector<int>x(1<<11);for(auto&q:a)for(int i=0;i<11;++i)++x[in(q,i,r)];for(auto&q:b)for(int i=0;i<11;++i)--x[in(q,i,r)];if(std::any_of(x.begin(),x.end(),[](int z){return z;}))return false;}return true;}
static bool partial(const std::array<Q,4>&q){std::vector<char>u(1<<11);for(auto&z:q)for(int i=0;i<11;++i){auto x=in(z,i,5);if(u[x])return false;u[x]=1;}return true;}
static bool lowerdiff(const std::array<Q,4>&a,const std::array<Q,4>&b){std::vector<int>x(1<<11);for(auto&q:a)for(int i=0;i<11;++i)++x[in(q,i,3)];for(auto&q:b)for(int i=0;i<11;++i)--x[in(q,i,3)];return std::any_of(x.begin(),x.end(),[](int z){return z;});}
static std::array<Q,4> dec(const std::array<std::vector<Q>,4>&o,int c){std::array<Q,4>a;for(int i=0;i<4;++i){int z=o[i].size();a[i]=o[i][c%z];c/=z;}return a;}
int main(){std::array<std::vector<Q>,4>p,n;int tp=1,tn=1;for(int i=0;i<4;++i){p[i]=options(pos0[i]);n[i]=options(neg0[i]);std::cerr<<"opts "<<i<<' '<<p[i].size()<<' '<<n[i].size()<<'\n';tp*=p[i].size();tn*=n[i].size();}std::unordered_multimap<Sig,int,Hash>tab;for(int c=0;c<tp;++c){auto q=dec(p,c);if(partial(q))tab.emplace(signature(q),c);}std::cerr<<"positive="<<tab.size()<<" negative_space="<<tn<<'\n';for(int c=0;c<tn;++c){auto q=dec(n,c);if(!partial(q))continue;auto range=tab.equal_range(signature(q));for(auto it=range.first;it!=range.second;++it){auto a=dec(p,it->second);if(exactsame(a,q)&&lowerdiff(a,q)){std::cout<<"FOUND "<<it->second<<' '<<c<<'\n';for(int side=0;side<2;++side){std::cout<<(side?"NEG\n":"POS\n");auto &v=side?q:a;for(auto&z:v){for(int x:z)std::cout<<x<<'.';std::cout<<'\n';}}return 0;}}}std::cout<<"NONE\n";}
