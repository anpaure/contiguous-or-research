#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using Deck=std::array<uint16_t,9>;
static int parity(uint16_t x,uint16_t y){int h=0,m=0;for(int q=0;q<9;++q){h+=(x>>q&1)?1:-1;m=std::min(m,h);h+=(y>>q&1)?1:-1;m=std::min(m,h);}return(-m)&1;}
static Deck wins(const std::array<int,9>&o,int s){Deck d{};for(int e=0;e<9;++e){uint16_t m=0;for(int q=0;q<s;++q)m|=uint16_t(1u<<o[(e-q+9)%9]);d[e]=m;}return d;}
int main(){
 std::vector<std::array<int,9>>O;std::array<int,8>p{1,2,3,4,5,6,7,8};do{std::array<int,9>o{};for(int i=0;i<8;++i)o[i+1]=p[i];O.push_back(o);}while(std::next_permutation(p.begin(),p.end()));
 int n=O.size();std::vector<Deck>A(n),B(n);for(int i=0;i<n;++i){A[i]=wins(O[i],4);B[i]=wins(O[i],5);}static uint8_t c[512][512];for(int x=0;x<512;++x)if(__builtin_popcount((unsigned)x)==4)for(int y=0;y<512;++y)if(__builtin_popcount((unsigned)y)==5)c[x][y]=parity(x,y);
 std::atomic<int>best{-1},bestdiag{-1};std::mutex mu;std::array<int,9>ba{},bb{};
 #pragma omp parallel for schedule(dynamic,1)
 for(int ai=0;ai<n;++ai){for(int bi=0;bi<n;++bi){uint8_t M[9][9];for(int i=0;i<9;++i)for(int j=0;j<9;++j)M[i][j]=c[A[ai][i]][B[bi][j]];int q=0,qd[9]={};for(int i=0;i<9;++i)for(int j=0;j<9;++j){int z=M[i][j];int yes=(M[(i+1)%9][(j+1)%9]==z&&M[(i+1)%9][j]!=z&&M[i][(j+1)%9]!=z);q+=yes;qd[(i+j)%9]+=yes;}int md=*std::max_element(qd,qd+9);if(md>bestdiag.load(std::memory_order_relaxed)){std::lock_guard<std::mutex>lk(mu);if(md>bestdiag.load()){bestdiag=md;std::cerr<<"bestdiag "<<md<<" ai "<<ai<<" bi "<<bi<<"\n";}}if(q>best.load(std::memory_order_relaxed)){std::lock_guard<std::mutex>lk(mu);if(q>best.load()){best=q;ba=O[ai];bb=O[bi];std::cerr<<"best "<<q<<" ai "<<ai<<" bi "<<bi<<"\n";}}}if(ai%1000==0){std::lock_guard<std::mutex>lk(mu);std::cerr<<"progress "<<ai<<" best "<<best.load()<<"\n";}}
 std::cout<<"MAXQ "<<best.load()<<" MAXDIAG "<<bestdiag.load()<<" alpha";for(int z:ba)std::cout<<" "<<z;std::cout<<" beta";for(int z:bb)std::cout<<" "<<z;std::cout<<"\n";
}
