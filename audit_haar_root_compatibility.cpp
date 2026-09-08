#pragma GCC optimize("O3")
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>

using Order=std::array<int,9>;
using Mask=std::uint16_t;
static const std::array<Order,4>N={{
 {1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},
 {1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}}};
static const std::array<Order,4>P={{
 {1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},
 {1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}}};

static Mask vertex(const Order&q,int i){
 Mask x=0;for(int j=0;j<4;++j)x|=Mask{1}<<(q[(i+1+2*j)%9]-1);return x;
}
static std::pair<Mask,Mask> rootpair(const Order&q,int z){
 int i=std::find(q.begin(),q.end(),z)-q.begin();
 Mask a=vertex(q,i),b=vertex(q,(i+1)%9);if(a>b)std::swap(a,b);return {a,b};
}
template<class A>static std::multiset<std::pair<Mask,Mask>> pairs(const A&a,int z){
 std::multiset<std::pair<Mask,Mask>>s;for(auto&q:a)s.insert(rootpair(q,z));return s;
}
int main(){for(int z=1;z<=9;++z){auto a=pairs(N,z),b=pairs(P,z);
 std::vector<std::pair<Mask,Mask>>onlya,onlyb;
 std::set_difference(a.begin(),a.end(),b.begin(),b.end(),std::back_inserter(onlya));
 std::set_difference(b.begin(),b.end(),a.begin(),a.end(),std::back_inserter(onlyb));
 std::cout<<"z="<<z<<" differing_pairs="<<onlya.size()<<" equal="<<(a==b)<<'\n';}}
