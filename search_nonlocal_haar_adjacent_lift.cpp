#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using Mask=std::uint32_t; using Q=std::vector<int>;
static const int neg0[4][9]={{1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},{1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}};
static const int pos0[4][9]={{1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},{1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}};
static Mask in(const Q&q,int i,int r){Mask x=0;for(int t=0;t<r;++t)x|=Mask{1}<<(q[(i+2*t)%q.size()]-1);return x;}
struct Sig{std::vector<unsigned char>x;bool operator==(const Sig&o)const{return x==o.x;}};
struct Hash{size_t operator()(Sig const&s)const{std::uint64_t h=1469598103934665603ULL;for(auto c:s.x){h^=c;h*=1099511628211ULL;}return h;}};
static std::vector<Q> options(const int *a){std::vector<Q>v;Q b(a,a+9);for(int gap=0;gap<9;++gap)for(int rev=0;rev<2;++rev){Q q=b;q.insert(q.begin()+gap,rev?11:10);q.insert(q.begin()+gap,rev?10:11);v.push_back(q);}return v;}
static Sig signature(const std::array<Q,4>&q){Sig s;s.x.assign(1<<12,0);for(auto &z:q)for(int r:{4,5})for(int i=0;i<11;++i)++s.x[in(z,i,r)];return s;}
static bool partial(const std::array<Q,4>&q){std::vector<char>u(1<<11);for(auto&z:q)for(int i=0;i<11;++i){auto x=in(z,i,5);if(u[x])return false;u[x]=1;}return true;}
static std::map<Mask,int> effect(const std::array<Q,4>&p,const std::array<Q,4>&n,int r){std::map<Mask,int>d;for(auto&q:p)for(int i=0;i<11;++i)++d[in(q,i,r)];for(auto&q:n)for(int i=0;i<11;++i)--d[in(q,i,r)];for(auto it=d.begin();it!=d.end();)if(!it->second)it=d.erase(it);else++it;return d;}
static std::array<Q,4> decode(const std::array<std::vector<Q>,4>&o,int code){std::array<Q,4>a;for(int i=0;i<4;++i){a[i]=o[i][code%18];code/=18;}return a;}
int main(){std::array<std::vector<Q>,4>po,no;for(int i=0;i<4;++i){po[i]=options(pos0[i]);no[i]=options(neg0[i]);}std::unordered_map<Sig,int,Hash>tab;int total=18*18*18*18;for(int c=0;c<total;++c){auto q=decode(po,c);if(partial(q))tab.emplace(signature(q),c);}std::cerr<<"positive signatures="<<tab.size()<<"\n";for(int c=0;c<total;++c){auto q=decode(no,c);if(!partial(q))continue;auto it=tab.find(signature(q));if(it==tab.end())continue;auto p=decode(po,it->second);auto d=effect(p,q,3);if(d.empty())continue;std::cout<<"FOUND poscode="<<it->second<<" negcode="<<c<<" lower="<<d.size()<<"\n";for(int side=0;side<2;++side){std::cout<<(side?"NEG\n":"POS\n");auto &a=side?q:p;for(auto&z:a){for(int x:z)std::cout<<x<<'.';std::cout<<'\n';}}return 0;}std::cout<<"NONE\n";}
