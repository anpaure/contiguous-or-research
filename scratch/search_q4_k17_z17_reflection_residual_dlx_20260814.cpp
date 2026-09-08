#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <mutex>
#include <numeric>
#include <random>
#include <string>
#include <thread>
#include <vector>

struct Candidate {
  int original;
  std::array<int,10> rows;
  std::array<uint64_t,11> mask{};
};

static inline bool disjoint(const std::array<uint64_t,11>& a,
                            const std::array<uint64_t,11>& b) {
  for (int i=0;i<11;i++) if (a[i]&b[i]) return false;
  return true;
}

int main(int argc,char**argv) {
  if (argc!=6) {
    std::cerr << "usage INSTANCE SOLUTION SECONDS THREADS SEED\n"; return 2;
  }
  const std::string input=argv[1], output=argv[2];
  const double seconds=std::stod(argv[3]);
  const int thread_count=std::stoi(argv[4]);
  const uint64_t seed=std::stoull(argv[5]);
  std::ifstream in(input);
  int nrows,nused,ncand; in>>nrows>>nused>>ncand;
  if(!in||nrows!=680) return 3;
  std::array<uint64_t,11> initial{};
  for(int i=0,r;i<nused;i++){in>>r;initial[r/64]|=1ULL<<(r%64);}
  std::vector<Candidate> candidates(ncand);
  std::vector<std::vector<int>> incidence(nrows);
  for(int i=0;i<ncand;i++){
    in>>candidates[i].original;
    for(int& r:candidates[i].rows){
      in>>r; candidates[i].mask[r/64]|=1ULL<<(r%64); incidence[r].push_back(i);
    }
  }
  if(!in) return 4;
  std::atomic<bool> stop{false};
  std::atomic<long long> total_nodes{0};
  std::atomic<int> best_depth{0};
  std::mutex answer_mutex;
  std::vector<int> answer;
  auto deadline=std::chrono::steady_clock::now()
      +std::chrono::milliseconds((long long)(seconds*1000));

  auto worker=[&](int tid){
    std::mt19937_64 rng(seed+0x9e3779b97f4a7c15ULL*tid);
    std::vector<int> selected(54,-1);
    long long local_nodes=0;
    std::function<bool(int,std::array<uint64_t,11>)> dfs;
    dfs=[&](int depth,std::array<uint64_t,11> covered)->bool{
      if(stop.load(std::memory_order_relaxed)) return false;
      if((++local_nodes&1023)==0 && std::chrono::steady_clock::now()>=deadline)
        return false;
      int previous=best_depth.load();
      while(depth>previous&&!best_depth.compare_exchange_weak(previous,depth)){}
      if(depth==54){
        std::lock_guard<std::mutex> lock(answer_mutex);
        if(!stop.exchange(true)) answer.assign(selected.begin(),selected.end());
        return true;
      }
      int chosen_row=-1,min_count=1<<30,ties=0;
      for(int row=0;row<nrows;row++){
        if((covered[row/64]>>(row%64))&1ULL) continue;
        int count=0;
        for(int ci:incidence[row]) if(disjoint(covered,candidates[ci].mask)) count++;
        if(count==0) return false;
        if(count<min_count){min_count=count;chosen_row=row;ties=1;}
        else if(count==min_count && (rng()%++ties)==0) chosen_row=row;
      }
      if(chosen_row<0) return false;
      auto options=incidence[chosen_row];
      std::shuffle(options.begin(),options.end(),rng);
      std::stable_sort(options.begin(),options.end(),[&](int x,int y){
        int sx=0,sy=0;
        for(int r:candidates[x].rows) sx+=(int)incidence[r].size();
        for(int r:candidates[y].rows) sy+=(int)incidence[r].size();
        return sx<sy;
      });
      for(int ci:options){
        if(!disjoint(covered,candidates[ci].mask)) continue;
        auto next=covered;
        for(int w=0;w<11;w++) next[w]|=candidates[ci].mask[w];
        selected[depth]=ci;
        if(dfs(depth+1,next)) return true;
        if(std::chrono::steady_clock::now()>=deadline) return false;
      }
      return false;
    };
    while(!stop.load()&&std::chrono::steady_clock::now()<deadline) dfs(0,initial);
    total_nodes.fetch_add(local_nodes);
  };

  std::vector<std::thread> threads;
  for(int t=0;t<thread_count;t++)threads.emplace_back(worker,t);
  for(auto&thread:threads)thread.join();
  std::ofstream out(output);
  out<<"{\n  \"status\": \""<<(answer.empty()?"UNKNOWN":"PASS")<<"\",\n";
  out<<"  \"nodes\": "<<total_nodes.load()<<",\n";
  out<<"  \"best_depth\": "<<best_depth.load()<<",\n";
  out<<"  \"pair_indices\": [";
  for(size_t i=0;i<answer.size();i++){
    if(i)out<<",";out<<candidates[answer[i]].original;
  }
  out<<"]\n}\n";
  std::cout<<(answer.empty()?"UNKNOWN":"PASS")<<" nodes "<<total_nodes.load()
           <<" depth "<<best_depth.load()<<"\n";
  return answer.empty()?1:0;
}
