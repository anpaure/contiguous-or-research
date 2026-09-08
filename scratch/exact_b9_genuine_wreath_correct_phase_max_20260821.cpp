#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <numeric>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using Deck = std::array<uint16_t, 9>;

static int top_parity(uint16_t x, uint16_t y) {
  int h = 0, mn = 0;
  for (int q = 0; q < 9; ++q) {
    h += (x >> q & 1) ? 1 : -1; mn = std::min(mn, h);
    h += (y >> q & 1) ? 1 : -1; mn = std::min(mn, h);
  }
  return (-mn) & 1;
}

static Deck windows(const std::array<int,9>& o, int size) {
  Deck d{};
  for (int e = 0; e < 9; ++e) {
    uint16_t m = 0;
    for (int q = 0; q < size; ++q) m |= uint16_t(1u << o[(e-q+9)%9]);
    d[e] = m;
  }
  return d;
}

int main() {
  std::vector<std::array<int,9>> orders;
  std::array<int,8> p{1,2,3,4,5,6,7,8};
  do {
    std::array<int,9> o{}; o[0]=0;
    for (int i=0;i<8;++i) o[i+1]=p[i];
    orders.push_back(o);
  } while (std::next_permutation(p.begin(),p.end()));
  const int n=orders.size();
  std::vector<Deck> A(n),B(n);
  for(int i=0;i<n;++i){A[i]=windows(orders[i],4);B[i]=windows(orders[i],5);}
  static uint8_t ori[512][512];
  for(int x=0;x<512;++x) if(__builtin_popcount((unsigned)x)==4)
    for(int y=0;y<512;++y) if(__builtin_popcount((unsigned)y)==5) ori[x][y]=top_parity(x,y);
  // The one-defect alternating word; all such words are rotations/complements.
  std::array<int,9> tau{};
  for(int x=0;x<9;++x) tau[x]=((4*x)%9<4)?1:0;
  std::atomic<int> best{-1};
  std::atomic<int> best_run{-1};
  std::mutex outmu;
  std::array<int,9> besta{},bestb{}; std::array<int,9> bestword{}; int bestshift=0;
  #pragma omp parallel for schedule(dynamic,1)
  for(int ai=0;ai<n;++ai){
    for(int bi=0;bi<n;++bi){
      std::array<int,9> w{}; w.fill(-1);
      for(int ph=0;ph<9;++ph){
        int v=ori[A[ai][0]][B[bi][ph]]; bool mono=true;
        for(int i=1;i<9;++i) if(ori[A[ai][i]][B[bi][(ph-i+9)%9]]!=v){mono=false;break;}
        if(mono)w[ph]=v;
      }
      int local=0,shift=0;
      for(int sh=0;sh<18;++sh){int rot=sh%9,flip=sh/9,z=0;for(int ph=0;ph<9;++ph)z+=(w[ph]>=0&&w[ph]==(tau[(ph+rot)%9]^flip));if(z>local){local=z;shift=sh;}}
      int run=0;
      for(int st=0;st<9;++st){int z=0;while(z<9&&w[(st+z)%9]>=0&&(z==0||w[(st+z)%9]!=w[(st+z-1)%9]))++z;run=std::max(run,z);}
      int old=best.load(std::memory_order_relaxed);
      if(local>old){
        std::lock_guard<std::mutex> lk(outmu);
        if(local>best.load()){best=local;besta=orders[ai];bestb=orders[bi];bestword=w;bestshift=shift;
          std::cerr<<"best "<<local<<" ai "<<ai<<" bi "<<bi<<"\n";}
      }
      int oldrun=best_run.load(std::memory_order_relaxed);
      if(run>oldrun){std::lock_guard<std::mutex> lk(outmu);if(run>best_run.load()){best_run=run;std::cerr<<"best_run "<<run<<" ai "<<ai<<" bi "<<bi<<"\n";}}
    }
    if(ai%1000==0){std::lock_guard<std::mutex> lk(outmu);std::cerr<<"progress "<<ai<<"/"<<n<<" best "<<best.load()<<"\n";}
  }
  std::cout<<"MAX "<<best.load()<<" MAXRUN "<<best_run.load()<<" shift "<<bestshift<<" alpha";
  for(int x:besta)std::cout<<" "<<x;std::cout<<" beta";for(int x:bestb)std::cout<<" "<<x;
  std::cout<<" word";for(int x:bestword)std::cout<<" "<<x;std::cout<<"\n";
}
