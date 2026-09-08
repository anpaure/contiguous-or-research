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
using NO=std::array<int,11>;
static NO cap(O q,int z,int ch){
 if(ch&1)std::reverse(q.begin(),q.end());
 int iz=std::find(q.begin(),q.end(),z)-q.begin();NO a{};int t=0;
 for(int j=1;j<9;++j)a[t++]=q[(iz+j)%9];
 a[t++]=(ch&2)?11:10;a[t++]=(ch&2)?10:11;a[t++]=z;return a;
}
static Mask I(const NO&q,int s,int r){Mask x=0;for(int j=0;j<r;++j)x|=Mask{1}<<(q[(s+2*j)%11]-1);return x;}
struct S{std::array<Mask,88>x{};bool operator<(S const&o)const{return x<o.x;}};
struct M{std::array<Mask,44>x{};bool operator<(M const&o)const{return x<o.x;}};
static bool sig(const std::array<O,4>&A,int z,int code,S&s,std::vector<Mask>*d=nullptr){std::vector<Mask>a,b,c;
 for(int i=0;i<4;++i){int ch=code&3;code>>=2;auto q=cap(A[i],z,ch);for(int p=0;p<11;++p){a.push_back(I(q,p,5));b.push_back(I(q,p,4));c.push_back(I(q,p,3));}}
 std::sort(a.begin(),a.end());if(std::adjacent_find(a.begin(),a.end())!=a.end())return false;std::sort(b.begin(),b.end());for(int i=0;i<44;++i)s.x[i]=a[i],s.x[44+i]=b[i];if(d){std::sort(c.begin(),c.end());*d=c;}return true;}
static M middle(S const&s){M m;std::copy_n(s.x.begin(),44,m.x.begin());return m;}
int main(){for(int z=1;z<=9;++z){std::map<S,int>tab;std::map<M,int>mtab;int np=0,pp=0,midmatch=0,top=0;
 for(int c=0;c<256;++c){S s;if(sig(N,z,c,s)){++np;tab.emplace(s,c);mtab.emplace(middle(s),c);}}
 for(int c=0;c<256;++c){S s;std::vector<Mask>pd;if(!sig(P,z,c,s,&pd))continue;++pp;midmatch+=mtab.count(middle(s));auto it=tab.find(s);if(it==tab.end())continue;++top;std::vector<Mask>nd;S q;sig(N,z,it->second,q,&nd);std::cout<<"FOUND z="<<z<<" N="<<it->second<<" P="<<c<<" deep_equal="<<(nd==pd)<<'\n';return 0;}
 std::cout<<"z="<<z<<" np="<<np<<" pp="<<pp<<" middle_matches="<<midmatch<<" top="<<top<<'\n';}}
