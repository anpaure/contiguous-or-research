#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <random>
#include <string>
#include <thread>
#include <vector>

struct SelfOption { int group; std::array<int,4> rows; };
struct PairOption { std::array<int,10> rows; };

static inline int cost(int load) { int d=load-1; return d*d; }

template <size_t N>
static int apply_rows(std::array<int,680>& loads,
                      const std::array<int,N>& rows, int delta) {
  int change=0;
  for (int row: rows) {
    change -= cost(loads[row]);
    loads[row] += delta;
    change += cost(loads[row]);
  }
  return change;
}

struct BestState {
  std::atomic<int> energy{1<<30};
  std::mutex mutex;
  std::vector<int> self_indices;
  std::vector<int> pair_indices;
};

int main(int argc, char** argv) {
  if (argc != 6) {
    std::cerr << "usage: INSTANCE SOLUTION SECONDS THREADS SEED\n";
    return 2;
  }
  const std::string instance_path=argv[1], solution_path=argv[2];
  const double seconds=std::stod(argv[3]);
  const int thread_count=std::stoi(argv[4]);
  const uint64_t base_seed=std::stoull(argv[5]);
  std::ifstream in(instance_path);
  int row_count, group_count, self_count, pair_count;
  in >> row_count >> group_count >> self_count >> pair_count;
  if (!in || row_count!=680 || group_count!=35) return 3;
  std::vector<SelfOption> self_options(self_count);
  std::vector<std::vector<int>> group_options(group_count);
  std::vector<std::vector<int>> self_incidence(row_count);
  for (int i=0;i<self_count;i++) {
    auto& option=self_options[i];
    in >> option.group;
    for (int& row: option.rows) in >> row;
    group_options[option.group].push_back(i);
    for (int row: option.rows) self_incidence[row].push_back(i);
  }
  std::vector<PairOption> pair_options(pair_count);
  std::vector<std::vector<int>> pair_incidence(row_count);
  for (int i=0;i<pair_count;i++) {
    for (int& row: pair_options[i].rows) in >> row;
    for (int row: pair_options[i].rows) pair_incidence[row].push_back(i);
  }
  if (!in) return 4;

  BestState best;
  std::atomic<bool> stop{false};
  const auto deadline=std::chrono::steady_clock::now()
      +std::chrono::milliseconds((long long)(1000*seconds));

  auto worker = [&](int thread_id) {
    std::mt19937_64 rng(base_seed + 0x9e3779b97f4a7c15ULL*thread_id);
    std::uniform_real_distribution<double> unit(0.0,1.0);
    auto random_index=[&](int n){ return (int)(rng() % (uint64_t)n); };
    while (!stop.load(std::memory_order_relaxed)
           && std::chrono::steady_clock::now() < deadline) {
      std::array<int,680> loads{};
      std::vector<int> selected_self(group_count);
      for (int g=0;g<group_count;g++) {
        const auto& options=group_options[g];
        int choice=options[random_index((int)options.size())];
        selected_self[g]=choice;
        apply_rows(loads,self_options[choice].rows,+1);
      }
      std::vector<int> selected_pairs;
      std::vector<int> pair_position(pair_count,-1);
      selected_pairs.reserve(54);
      while ((int)selected_pairs.size()<54) {
        int choice=random_index(pair_count);
        if (pair_position[choice]>=0) continue;
        pair_position[choice]=(int)selected_pairs.size();
        selected_pairs.push_back(choice);
        apply_rows(loads,pair_options[choice].rows,+1);
      }
      int energy=0;
      for (int load: loads) energy += cost(load);
      int local_best=energy;
      long long stagnant=0;

      auto record = [&]() {
        int previous=best.energy.load(std::memory_order_relaxed);
        while (energy<previous && !best.energy.compare_exchange_weak(previous,energy)) {}
        if (energy <= best.energy.load(std::memory_order_relaxed)) {
          std::lock_guard<std::mutex> lock(best.mutex);
          if (energy <= best.energy.load(std::memory_order_relaxed)) {
            best.energy.store(energy,std::memory_order_relaxed);
            best.self_indices=selected_self;
            best.pair_indices=selected_pairs;
            std::cerr << "best " << energy << " thread " << thread_id << "\n";
          }
        }
        if (energy==0) stop.store(true,std::memory_order_relaxed);
      };
      record();

      const long long restart_limit=3000000;
      for (long long iteration=0;
           iteration<restart_limit && !stop.load(std::memory_order_relaxed)
           && std::chrono::steady_clock::now()<deadline; iteration++) {
        const double phase=(double)(iteration%300000)/300000.0;
        const double temperature=0.15 + 5.85*(1.0-phase);
        int hole=-1;
        for (int tries=0;tries<24;tries++) {
          int row=random_index(680);
          if (loads[row]==0) { hole=row; break; }
        }
        bool self_move = (rng()&1);
        if (hole>=0) {
          if (self_incidence[hole].empty()) self_move=false;
          if (pair_incidence[hole].empty()) self_move=true;
        }

        int delta_energy=0;
        if (self_move) {
          int candidate;
          if (hole>=0) {
            const auto& incident=self_incidence[hole];
            candidate=incident[random_index((int)incident.size())];
          } else {
            int g=random_index(group_count);
            const auto& options=group_options[g];
            candidate=options[random_index((int)options.size())];
          }
          int group=self_options[candidate].group;
          int old=selected_self[group];
          if (candidate==old) continue;
          delta_energy += apply_rows(loads,self_options[old].rows,-1);
          delta_energy += apply_rows(loads,self_options[candidate].rows,+1);
          bool accept=delta_energy<=0 || unit(rng)<std::exp(-delta_energy/temperature);
          if (accept) {
            selected_self[group]=candidate;
            energy += delta_energy;
          } else {
            apply_rows(loads,self_options[candidate].rows,-1);
            apply_rows(loads,self_options[old].rows,+1);
          }
        } else {
          int candidate=-1;
          for (int tries=0;tries<30;tries++) {
            if (hole>=0) {
              const auto& incident=pair_incidence[hole];
              candidate=incident[random_index((int)incident.size())];
            } else candidate=random_index(pair_count);
            if (pair_position[candidate]<0) break;
            candidate=-1;
          }
          if (candidate<0) continue;
          int position=random_index(54);
          int old=selected_pairs[position];
          delta_energy += apply_rows(loads,pair_options[old].rows,-1);
          delta_energy += apply_rows(loads,pair_options[candidate].rows,+1);
          bool accept=delta_energy<=0 || unit(rng)<std::exp(-delta_energy/temperature);
          if (accept) {
            pair_position[old]=-1;
            pair_position[candidate]=position;
            selected_pairs[position]=candidate;
            energy += delta_energy;
          } else {
            apply_rows(loads,pair_options[candidate].rows,-1);
            apply_rows(loads,pair_options[old].rows,+1);
          }
        }
        if (energy<local_best) { local_best=energy; stagnant=0; record(); }
        else stagnant++;
        if (stagnant>800000) break;
      }
    }
  };

  std::vector<std::thread> threads;
  for (int t=0;t<thread_count;t++) threads.emplace_back(worker,t);
  for (auto& thread: threads) thread.join();

  std::ofstream out(solution_path);
  const int final_energy=best.energy.load();
  out << "{\n  \"status\": \"" << (final_energy==0?"PASS":"BEST") << "\",\n";
  out << "  \"energy\": " << final_energy << ",\n";
  out << "  \"self_indices\": [";
  for (size_t i=0;i<best.self_indices.size();i++) {
    if (i) out << ","; out << best.self_indices[i];
  }
  out << "],\n  \"pair_indices\": [";
  for (size_t i=0;i<best.pair_indices.size();i++) {
    if (i) out << ","; out << best.pair_indices[i];
  }
  out << "]\n}\n";
  std::cout << "energy " << final_energy << "\n";
  return final_energy==0 ? 0 : 1;
}
