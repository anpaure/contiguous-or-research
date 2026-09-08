#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <mutex>
#include <random>
#include <sstream>
#include <string>
#include <thread>
#include <utility>
#include <vector>

struct SelfOption { int group; std::array<int,4> rows; };
struct PairOption { std::array<int,10> rows; };

static int squared_cost(int load) { const int d=load-1; return d*d; }

static std::vector<int> parse_array(const std::string& text,
                                    const std::string& key) {
  const size_t key_position=text.find(key);
  if (key_position==std::string::npos) return {};
  const size_t left=text.find('[',key_position);
  const size_t right=text.find(']',left);
  if (left==std::string::npos || right==std::string::npos) return {};
  std::vector<int> result;
  int value=0; bool reading=false;
  for (size_t i=left+1;i<right;i++) {
    if (text[i]>='0' && text[i]<='9') {
      value=10*value+(text[i]-'0'); reading=true;
    } else if (reading) {
      result.push_back(value); value=0; reading=false;
    }
  }
  if (reading) result.push_back(value);
  return result;
}

struct Delta { int weighted=0; int unweighted=0; };

template <size_t OLD, size_t NEW>
static Delta swap_delta(const std::array<int,680>& loads,
                        const std::array<int,680>& weights,
                        const std::array<int,OLD>& old_rows,
                        const std::array<int,NEW>& new_rows) {
  std::array<int,OLD+NEW> touched{};
  std::array<int,OLD+NEW> changes{};
  int count=0;
  auto add_change=[&](int row,int change) {
    for (int i=0;i<count;i++) if (touched[i]==row) {
      changes[i]+=change; return;
    }
    touched[count]=row; changes[count]=change; count++;
  };
  for (int row:old_rows) add_change(row,-1);
  for (int row:new_rows) add_change(row,+1);
  Delta result;
  for (int i=0;i<count;i++) {
    const int row=touched[i], before=squared_cost(loads[row]);
    const int after=squared_cost(loads[row]+changes[i]);
    result.unweighted += after-before;
    result.weighted += weights[row]*(after-before);
  }
  return result;
}

template <size_t OLD, size_t NEW>
static void apply_swap(std::array<int,680>& loads,
                       const std::array<int,OLD>& old_rows,
                       const std::array<int,NEW>& new_rows) {
  for (int row:old_rows) loads[row]--;
  for (int row:new_rows) loads[row]++;
}

struct BestState {
  std::atomic<int> energy{std::numeric_limits<int>::max()};
  std::mutex mutex;
  std::vector<int> self_indices;
  std::vector<int> pair_indices;
};

int main(int argc,char** argv) {
  if (argc!=7) {
    std::cerr << "usage: INSTANCE SEED_STATE SOLUTION SECONDS THREADS SEED\n";
    return 2;
  }
  const std::string instance_path=argv[1], seed_path=argv[2];
  const std::string solution_path=argv[3];
  const double seconds=std::stod(argv[4]);
  const int thread_count=std::stoi(argv[5]);
  const uint64_t base_seed=std::stoull(argv[6]);

  std::ifstream input(instance_path);
  int row_count,group_count,self_count,pair_count;
  input>>row_count>>group_count>>self_count>>pair_count;
  if (!input || row_count!=680 || group_count!=35) return 3;
  std::vector<SelfOption> self_options(self_count);
  std::vector<std::vector<int>> self_incidence(row_count);
  std::vector<std::vector<int>> group_options(group_count);
  for (int i=0;i<self_count;i++) {
    input>>self_options[i].group;
    for (int& row:self_options[i].rows) {
      input>>row; self_incidence[row].push_back(i);
    }
    group_options[self_options[i].group].push_back(i);
  }
  std::vector<PairOption> pair_options(pair_count);
  std::vector<std::vector<int>> pair_incidence(row_count);
  for (int i=0;i<pair_count;i++) for (int& row:pair_options[i].rows) {
    input>>row; pair_incidence[row].push_back(i);
  }
  if (!input) return 4;

  std::ifstream seed_stream(seed_path);
  std::stringstream seed_buffer; seed_buffer<<seed_stream.rdbuf();
  const std::string seed_text=seed_buffer.str();
  const std::vector<int> seed_self=parse_array(seed_text,"self_indices");
  const std::vector<int> seed_pairs=parse_array(seed_text,"pair_indices");
  if ((int)seed_self.size()!=35 || (int)seed_pairs.size()!=54) return 5;
  std::vector<int> seed_self_by_group(group_count,-1);
  for (int index:seed_self) {
    if (index<0 || index>=self_count) return 6;
    const int group=self_options[index].group;
    if (seed_self_by_group[group]>=0) return 7;
    seed_self_by_group[group]=index;
  }
  if (std::find(seed_self_by_group.begin(),seed_self_by_group.end(),-1)
      !=seed_self_by_group.end()) return 8;

  BestState best;
  std::atomic<bool> stop{false};
  const auto deadline=std::chrono::steady_clock::now()
      +std::chrono::milliseconds((long long)(1000*seconds));

  auto worker=[&](int thread_id) {
    std::mt19937_64 rng(base_seed
        +0x9e3779b97f4a7c15ULL*(uint64_t)(thread_id+1));
    std::vector<int> selected_self=seed_self_by_group;
    std::vector<int> selected_pairs=seed_pairs;
    std::vector<int> pair_position(pair_count,-1);
    for (int position=0;position<54;position++) {
      const int index=selected_pairs[position];
      if (index<0 || index>=pair_count || pair_position[index]>=0) return;
      pair_position[index]=position;
    }
    std::array<int,680> loads{};
    for (int index:selected_self)
      for (int row:self_options[index].rows) loads[row]++;
    for (int index:selected_pairs)
      for (int row:pair_options[index].rows) loads[row]++;
    std::array<int,680> weights{}; weights.fill(1);
    int energy=0;
    for (int load:loads) energy+=squared_cost(load);
    std::vector<long long> self_tabu(self_count,0),pair_tabu(pair_count,0);

    // Diversify all but the first trajectory while preserving both exact
    // configuration counts and one self lift per fixed matching edge.
    const int perturbations=3*thread_id;
    for (int step=0;step<perturbations;step++) {
      if (rng()&1) {
        const int group=(int)(rng()%35);
        const int old=selected_self[group];
        const auto& options=group_options[group];
        const int candidate=options[rng()%options.size()];
        if (candidate!=old) {
          const Delta delta=swap_delta(loads,weights,
              self_options[old].rows,self_options[candidate].rows);
          apply_swap(loads,self_options[old].rows,
                     self_options[candidate].rows);
          selected_self[group]=candidate; energy+=delta.unweighted;
        }
      } else {
        const int position=(int)(rng()%54),old=selected_pairs[position];
        int candidate;
        do candidate=(int)(rng()%pair_count);
        while (pair_position[candidate]>=0);
        const Delta delta=swap_delta(loads,weights,
            pair_options[old].rows,pair_options[candidate].rows);
        apply_swap(loads,pair_options[old].rows,pair_options[candidate].rows);
        pair_position[old]=-1; pair_position[candidate]=position;
        selected_pairs[position]=candidate; energy+=delta.unweighted;
      }
    }

    int weighted_energy=0;
    for (int row=0;row<680;row++)
      weighted_energy+=weights[row]*squared_cost(loads[row]);
    long long iteration=0,last_improvement=0;
    auto record=[&]() {
      int previous=best.energy.load(std::memory_order_relaxed);
      while (energy<previous &&
             !best.energy.compare_exchange_weak(previous,energy)) {}
      if (energy<=best.energy.load(std::memory_order_relaxed)) {
        std::lock_guard<std::mutex> lock(best.mutex);
        if (energy<=best.energy.load(std::memory_order_relaxed)) {
          best.energy.store(energy,std::memory_order_relaxed);
          best.self_indices=selected_self;
          best.pair_indices=selected_pairs;
          int holes=0,doubles=0;
          for (int load:loads) { holes+=(load==0); doubles+=(load==2); }
          std::cerr<<"best "<<energy<<" holes "<<holes
                   <<" doubles "<<doubles<<" thread "<<thread_id
                   <<" iteration "<<iteration<<"\n";
        }
      }
      if (energy==0) stop.store(true,std::memory_order_relaxed);
    };
    record();

    struct Move {
      bool is_self=false; int old_index=-1,new_index=-1,position=-1;
      Delta delta; long long tie=0;
    };
    while (!stop.load(std::memory_order_relaxed)
           && std::chrono::steady_clock::now()<deadline) {
      iteration++;
      std::vector<int> holes;
      for (int row=0;row<680;row++) if (loads[row]==0) holes.push_back(row);
      if (holes.empty()) { record(); break; }
      const int hole=holes[rng()%holes.size()];
      Move best_move; int best_score=std::numeric_limits<int>::max();

      // Target the chosen hole and, for each proposed incoming pair, test
      // every currently selected outgoing pair.  This is the exhaustive
      // one-pair ejection neighborhood around that hole.
      const auto& incoming_pairs=pair_incidence[hole];
      const int pair_trials=std::min<int>(160,incoming_pairs.size());
      const int pair_start=(int)(rng()%incoming_pairs.size());
      for (int trial=0;trial<pair_trials;trial++) {
        const int candidate=incoming_pairs[(pair_start+trial)%incoming_pairs.size()];
        if (pair_position[candidate]>=0) continue;
        for (int position=0;position<54;position++) {
          const int old=selected_pairs[position];
          const Delta delta=swap_delta(loads,weights,
              pair_options[old].rows,pair_options[candidate].rows);
          const bool tabu=pair_tabu[candidate]>iteration;
          if (tabu && energy+delta.unweighted>=best.energy.load()) continue;
          const int score=delta.weighted;
          const long long tie=(long long)(rng()&0xffff);
          if (score<best_score || (score==best_score && tie<best_move.tie)) {
            best_score=score;
            best_move={false,old,candidate,position,delta,tie};
          }
        }
      }

      // A self-lift move has its outgoing member forced by the lift group.
      for (int candidate:self_incidence[hole]) {
        const int group=self_options[candidate].group;
        const int old=selected_self[group];
        if (candidate==old) continue;
        const Delta delta=swap_delta(loads,weights,
            self_options[old].rows,self_options[candidate].rows);
        const bool tabu=self_tabu[candidate]>iteration;
        if (tabu && energy+delta.unweighted>=best.energy.load()) continue;
        const int score=delta.weighted;
        const long long tie=(long long)(rng()&0xffff);
        if (score<best_score || (score==best_score && tie<best_move.tie)) {
          best_score=score;
          best_move={true,old,candidate,group,delta,tie};
        }
      }
      if (best_move.new_index<0) continue;

      if (best_move.is_self) {
        apply_swap(loads,self_options[best_move.old_index].rows,
                   self_options[best_move.new_index].rows);
        selected_self[best_move.position]=best_move.new_index;
        self_tabu[best_move.old_index]=iteration+25+(rng()%90);
      } else {
        apply_swap(loads,pair_options[best_move.old_index].rows,
                   pair_options[best_move.new_index].rows);
        pair_position[best_move.old_index]=-1;
        pair_position[best_move.new_index]=best_move.position;
        selected_pairs[best_move.position]=best_move.new_index;
        pair_tabu[best_move.old_index]=iteration+35+(rng()%140);
      }
      energy+=best_move.delta.unweighted;
      weighted_energy+=best_move.delta.weighted;
      if (energy<best.energy.load(std::memory_order_relaxed)) {
        last_improvement=iteration; record();
      }

      // Breakout weighting turns a persistent local collision/deficit
      // boundary into a new objective without changing feasibility.
      if (iteration-last_improvement>12000 && iteration%2000==0) {
        for (int row=0;row<680;row++) if (loads[row]!=1)
          weights[row]=std::min(200,weights[row]+1);
        weighted_energy=0;
        for (int row=0;row<680;row++)
          weighted_energy+=weights[row]*squared_cost(loads[row]);
      }
      // Periodically flatten the breakout landscape while retaining tabu
      // memory, giving repeated long ejection chains from the best basin.
      if (iteration%250000==0) {
        for (int& weight:weights) weight=1+(weight/4);
        weighted_energy=0;
        for (int row=0;row<680;row++)
          weighted_energy+=weights[row]*squared_cost(loads[row]);
      }
    }
  };

  std::vector<std::thread> threads;
  for (int thread=0;thread<thread_count;thread++)
    threads.emplace_back(worker,thread);
  for (auto& thread:threads) thread.join();

  std::ofstream output(solution_path);
  const int final_energy=best.energy.load();
  output<<"{\n  \"status\": \""<<(final_energy==0?"PASS":"BEST")
        <<"\",\n  \"energy\": "<<final_energy<<",\n";
  output<<"  \"self_indices\": [";
  for (size_t i=0;i<best.self_indices.size();i++) {
    if (i) output<<","; output<<best.self_indices[i];
  }
  output<<"],\n  \"pair_indices\": [";
  for (size_t i=0;i<best.pair_indices.size();i++) {
    if (i) output<<","; output<<best.pair_indices[i];
  }
  output<<"]\n}\n";
  std::cout<<"energy "<<final_energy<<"\n";
  return final_energy==0?0:1;
}
