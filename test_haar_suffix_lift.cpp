#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

using Mask=std::uint32_t;
using Order=std::vector<int>;

static const std::array<std::array<int,9>,4> negative={{
 {1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},
 {1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}}};
static const std::array<std::array<int,9>,4> positive={{
 {1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},
 {1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}}};

static Mask interval(const Order&q,int start,int rank){
 Mask s=0;int n=q.size();
 for(int j=0;j<rank;++j)s|=Mask{1}<<(q[(start+2*j)%n]-1);
 return s;
}

static Order substitute(const std::array<int,9>&q,const Order&tail){
 Order out;
 for(int x:q)if(x==9)out.insert(out.end(),tail.begin(),tail.end());else out.push_back(x);
 return out;
}

template<class Side>
static std::map<Mask,int> effect(const Side&p,const Side&n,const Order&tail,int rank){
 std::map<Mask,int>d;
 for(const auto&q:p){auto e=substitute(q,tail);for(int i=0;i<(int)e.size();++i)++d[interval(e,i,rank)];}
 for(const auto&q:n){auto e=substitute(q,tail);for(int i=0;i<(int)e.size();++i)--d[interval(e,i,rank)];}
 for(auto it=d.begin();it!=d.end();)if(!it->second)it=d.erase(it);else ++it;
 return d;
}

int main(){
 std::vector<Order> tails={{10,9,11},{12,10,11,9,13},{14,12,10,11,9,13,15}};
 for(const auto&t:tails){
  int r=(t.size()-1)/2,m=4+r;
  std::cout<<"tail=";for(int x:t)std::cout<<x<<',';
  for(int rank=m;rank>=m-3;--rank){auto d=effect(positive,negative,t,rank);std::cout<<" B"<<rank<<'='<<d.size();}
  std::cout<<'\n';
 }
}
