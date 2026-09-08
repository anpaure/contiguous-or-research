#pragma GCC optimize("O3,unroll-loops")
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using Mask=std::uint16_t;using O=std::array<int,9>;
static const std::array<O,4>N={{{1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},{1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}}};
static const std::array<O,4>P={{{1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},{1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}}};
static const std::array<std::array<int,4>,2>Q={{{13,11,12,10},{11,10,13,12}}};
using NO=std::array<int,13>;
static NO cap(O q,int z,int rev){if(rev)std::reverse(q.begin(),q.end());int iz=std::find(q.begin(),q.end(),z)-q.begin();NO a{};int t=0;for(int j=1;j<9;++j)a[t++]=q[(iz+j)%9];for(auto&r:Q[0])a[t++]=r;a[t++]=z;return a;}
static NO capq(O q,int z,int rev,int qi){if(rev)std::reverse(q.begin(),q.end());int iz=std::find(q.begin(),q.end(),z)-q.begin();NO a{};int t=0;for(int j=1;j<9;++j)a[t++]=q[(iz+j)%9];for(auto&r:Q[qi])a[t++]=r;a[t++]=z;return a;}
static Mask I(const NO&q,int s,int r){Mask x=0;for(int j=0;j<r;++j)x|=Mask{1}<<(q[(s+2*j)%13]-1);return x;}
struct S{std::array<Mask,208>x{};bool operator<(S const&o)const{return x<o.x;}};
struct M{std::array<Mask,104>x{};bool operator<(M const&o)const{return x<o.x;}};
static bool sig(const std::array<O,4>&A,int z,int code,S&s){std::vector<Mask>a,b;for(int i=0;i<4;++i){int rv=(code>>i)&1;for(int qi=0;qi<2;++qi){auto q=capq(A[i],z,rv,qi);for(int p=0;p<13;++p){a.push_back(I(q,p,6));b.push_back(I(q,p,5));}}}std::sort(a.begin(),a.end());if(std::adjacent_find(a.begin(),a.end())!=a.end())return false;std::sort(b.begin(),b.end());for(int i=0;i<104;++i)s.x[i]=a[i],s.x[104+i]=b[i];return true;}
static M mid(S const&s){M m;std::copy_n(s.x.begin(),104,m.x.begin());return m;}
int main(){for(int z=1;z<=9;++z){std::map<S,int>T;std::map<M,int>U;int np=0,pp=0,mm=0,tt=0;for(int c=0;c<16;++c){S s;if(sig(N,z,c,s)){++np;T.emplace(s,c);U.emplace(mid(s),c);}}for(int c=0;c<16;++c){S s;if(!sig(P,z,c,s))continue;++pp;mm+=U.count(mid(s));auto it=T.find(s);if(it!=T.end()){++tt;std::cout<<"FOUND z="<<z<<" N="<<it->second<<" P="<<c<<'\n';return 0;}}std::cout<<"z="<<z<<" np="<<np<<" pp="<<pp<<" middle="<<mm<<" top="<<tt<<'\n';}}
