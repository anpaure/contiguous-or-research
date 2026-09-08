#pragma GCC optimize("O3")
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <tuple>
#include <vector>
using Mask=std::uint16_t;using O=std::array<int,9>;
static const std::array<O,4>N={{{1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},{1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}}};
static const std::array<O,4>P={{{1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},{1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}}};
static Mask A(const O&q,int i){Mask x=0;for(int j=0;j<4;++j)x|=Mask{1}<<(q[(i+1+2*j)%9]-1);return x;}
struct F{std::vector<Mask>end,L,U,E0,E1;};
static void add(F&f,O q,int z,bool rev){if(rev)std::reverse(q.begin(),q.end());int iz=std::find(q.begin(),q.end(),z)-q.begin();Mask X=((Mask{1}<<9)-1)^(Mask{1}<<(z-1));std::array<Mask,5>x{};std::array<Mask,4>y{};for(int t=0;t<9;++t){Mask a=A(q,(iz+1+t)%9);if(t%2==0)x[t/2]=a;else y[t/2]=X^(a&X);}f.end.push_back(x[4]);for(int i=0;i<4;++i)f.L.push_back(x[i]&x[i+1]);for(int i=1;i<4;++i)f.U.push_back(X^(y[i-1]|y[i]));f.E0.push_back(X^y[0]);f.E1.push_back(X^y[3]);}
template<class T>static F flags(const T&S,int z,int code){F f;for(int i=0;i<4;++i)add(f,S[i],z,(code>>i)&1);for(auto*v:{&f.end,&f.L,&f.U,&f.E0,&f.E1})std::sort(v->begin(),v->end());return f;}
static int diff(const std::vector<Mask>&a,const std::vector<Mask>&b){std::vector<Mask>x,y;std::set_difference(a.begin(),a.end(),b.begin(),b.end(),std::back_inserter(x));std::set_difference(b.begin(),b.end(),a.begin(),a.end(),std::back_inserter(y));return x.size()+y.size();}
static Mask firstdiff(const std::vector<Mask>&a,const std::vector<Mask>&b){std::vector<Mask>x;std::set_difference(a.begin(),a.end(),b.begin(),b.end(),std::back_inserter(x));return x.empty()?0:x[0];}
int main(){for(int z=1;z<=9;++z){int pairs=0,best=999,bn=0,bp=0;std::array<int,4>bd{};Mask witness=0;for(int a=0;a<16;++a){auto f=flags(N,z,a);for(int b=0;b<16;++b){auto g=flags(P,z,b);if(f.end!=g.end)continue;++pairs;std::array<int,4>d={diff(f.L,g.L),diff(f.U,g.U),diff(f.E0,g.E0),diff(f.E1,g.E1)};int s=d[0]+d[1]+d[2]+d[3];if(s<best){best=s;bn=a;bp=b;bd=d;witness=firstdiff(f.L,g.L);if(!witness)witness=firstdiff(f.U,g.U);if(!witness)witness=firstdiff(f.E0,g.E0);if(!witness)witness=firstdiff(f.E1,g.E1);}}}std::cout<<"z="<<z<<" endpoint_pairs="<<pairs<<" best="<<(pairs?best:-1)<<" codes="<<bn<<','<<bp<<" flag_diffs="<<bd[0]<<','<<bd[1]<<','<<bd[2]<<','<<bd[3]<<" witness="<<witness<<'\n';}}
