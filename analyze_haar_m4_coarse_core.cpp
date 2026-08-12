#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>

using namespace std;
static constexpr int M=4, N=9, VARS=8;
using Order=array<int,N>;
struct Edge { int u,v,su,sv,mask; };

static Order ordinary(const Order&q){Order c{};for(int i=0;i<N;++i)c[i]=q[2*i%N];return c;}
static int imask(const Order&c,int s){int z=0;for(int j=0;j<M;++j)z|=1<<(c[(s+j)%N]-1);return z;}
static int kap(int z){z=(z%N+N)%N;if(z<=2)return 0;if(z==3)return 1;if(z==4)return 2;if(z<=7)return 3;return 4;}

static bool propagate(array<uint16_t,VARS>&d,const vector<Edge>&es){
  bool changed=true;
  while(changed){changed=false;
    for(auto&e:es){
      uint16_t nu=0,nv=0;
      for(int a=0;a<N;++a)if(d[e.u]>>a&1)for(int b=0;b<N;++b)if(d[e.v]>>b&1)
        if(kap(a-e.su)==kap(b-e.sv)){nu|=1u<<a;nv|=1u<<b;}
      uint16_t xu=d[e.u]&nu,xv=d[e.v]&nv;
      if(!xu||!xv)return false;
      if(xu!=d[e.u]||xv!=d[e.v]){d[e.u]=xu;d[e.v]=xv;changed=true;}
    }
  }return true;
}
static bool sat_rec(array<uint16_t,VARS>d,const vector<Edge>&es){
  if(!propagate(d,es))return false;
  int v=-1,best=99;
  for(int i=0;i<VARS;++i){int c=__builtin_popcount(d[i]);if(c>1&&c<best)best=c,v=i;}
  if(v<0)return true;
  uint16_t x=d[v];
  for(int a=0;a<N;++a)if(x>>a&1){auto e=d;e[v]=1u<<a;if(sat_rec(e,es))return true;}
  return false;
}
static bool sat(const vector<Edge>&es){array<uint16_t,VARS>d{};d.fill((1u<<N)-1);return sat_rec(d,es);}

int main(){
 const array<Order,4> nq{{
 {1,8,6,7,4,5,3,9,2},{1,9,8,6,7,4,5,2,3},
 {1,5,3,9,8,6,7,2,4},{1,7,3,9,4,5,8,2,6}}};
 const array<Order,4> pq{{
 {1,9,3,5,4,7,6,8,2},{1,5,4,7,6,8,9,2,3},
 {1,7,6,8,9,3,5,2,4},{1,8,5,4,9,3,7,2,6}}};
 array<Order,4>A{},B{};for(int i=0;i<4;++i)A[i]=ordinary(nq[i]),B[i]=ordinary(pq[i]);
 map<int,pair<int,int>> ownA,ownB;
 for(int z=0;z<4;++z)for(int s=0;s<N;++s)ownA[imask(A[z],s)]={z,s},ownB[imask(B[z],s)]={z,s};
 vector<Edge> all;
 for(auto&[mask,us]:ownA){auto it=ownB.find(mask);if(it==ownB.end()){cerr<<"missing\n";return 2;}
   all.push_back({us.first,4+it->second.first,us.second,it->second.second,mask});}
 cerr<<"edges="<<all.size()<<" full_sat="<<sat(all)<<"\n";
 vector<Edge> core=all;
 bool changed=true;
 while(changed){changed=false;for(size_t i=0;i<core.size();++i){auto t=core;t.erase(t.begin()+i);if(!sat(t)){core=move(t);changed=true;break;}}}
 cout<<"irreducible_core="<<core.size()<<"\n";
 for(auto&e:core)cout<<"mask="<<e.mask<<" N"<<e.u<<"@"<<e.su<<" P"<<(e.v-4)<<"@"<<e.sv<<"\n";
 // Exhaustively find a smallest unsatisfiable subset inside the irreducible core's size bound.
 int E=all.size(), upper=core.size();
 for(int want=2;want<upper;++want){
   vector<int> pick(want);iota(pick.begin(),pick.end(),0);
   while(true){vector<Edge> t;for(int i:pick)t.push_back(all[i]);if(!sat(t)){
       cout<<"smaller_core="<<want<<"\n";for(auto&e:t)cout<<"mask="<<e.mask<<" N"<<e.u<<"@"<<e.su<<" P"<<(e.v-4)<<"@"<<e.sv<<"\n";
       if(want==3){
         cout<<"x : D1 | D2 | D3\n";
         for(int x=0;x<N;++x){cout<<x<<" :";
           for(int d=0;d<N;++d)if(kap(x)==kap(x+d+2))cout<<d;cout<<" | ";
           for(int d=0;d<N;++d)if(kap(x+1)==kap(x+d+1))cout<<d;cout<<" | ";
           for(int d=0;d<N;++d)if(kap(x+7)==kap(x+d+4))cout<<d;cout<<"\n";}
       }
       return 0;}
     int j=want-1;while(j>=0&&pick[j]==E-want+j)--j;if(j<0)break;++pick[j];for(int k=j+1;k<want;++k)pick[k]=pick[k-1]+1;}
 }
}
