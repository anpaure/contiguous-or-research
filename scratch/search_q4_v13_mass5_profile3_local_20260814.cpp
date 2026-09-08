// H100-only stochastic search for a cyclic realization of q4 mass5 Profile 3.
// The exact support is the independently verified V13 certificate.  A score
// of zero is a literal five-by-five named-owner atom with simple shores.

#include <algorithm>
#include <array>
#include <atomic>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <thread>
#include <unordered_set>
#include <vector>

struct Rail {
  std::string name;
  int sign;
  int center;
  std::vector<int> support;
};

static std::vector<int> complement(int center, std::initializer_list<int> holes) {
  std::array<bool, 13> omit{};
  omit[center] = true;
  for (int x : holes) omit[x] = true;
  std::vector<int> out;
  for (int x = 0; x < 13; ++x) if (!omit[x]) out.push_back(x);
  return out;
}

static std::vector<Rail> make_rails(int profile) {
  if (profile == 2) return {
    {"p10c4", +1, 4, complement(4, {0,12})},
    {"p11c0_1", +1, 0, complement(0, {4})},
    {"p11c0_2", +1, 0, complement(0, {4})},
    {"p11c0_3", +1, 0, complement(0, {4})},
    {"p11c4", +1, 4, complement(4, {0})},
    {"n10c0_1", -1, 0, complement(0, {1,3})},
    {"n10c0_2", -1, 0, complement(0, {1,12})},
    {"n11c1", -1, 1, complement(1, {2})},
    {"n11c2", -1, 2, complement(2, {3})},
    {"n11c3", -1, 3, complement(3, {2})},
  };
  if (profile == 3) return {
    {"p10c5_1", +1, 5, complement(5, {7,9})},
    {"p10c5_2", +1, 5, complement(5, {1,10})},
    {"p11c0", +1, 0, complement(0, {5})},
    {"p11c1", +1, 1, complement(1, {5})},
    {"p11c2", +1, 2, complement(2, {5})},
    {"n10c0", -1, 0, complement(0, {1,7})},
    {"n10c1", -1, 1, complement(1, {3,9})},
    {"n10c2", -1, 2, complement(2, {4,10})},
    {"n11c3", -1, 3, complement(3, {4})},
    {"n11c4", -1, 4, complement(4, {3})},
  };
  if (profile == 4) return {
    {"p10c4_1", +1, 4, complement(4, {0,1})},
    {"p10c4_2", +1, 4, complement(4, {0,5})},
    {"p11c0", +1, 0, complement(0, {3})},
    {"p11c1", +1, 1, complement(1, {4})},
    {"p11c2", +1, 2, complement(2, {3})},
    {"n10c0", -1, 0, complement(0, {3,5})},
    {"n10c1", -1, 1, complement(1, {0,3})},
    {"n10c2", -1, 2, complement(2, {1,3})},
    {"n11c3", -1, 3, complement(3, {0})},
    {"n11c4", -1, 4, complement(4, {3})},
  };
  if (profile == 44) return {
    {"p10c4_1", +1, 4, complement(4, {0,1})},
    {"p10c4_2", +1, 4, complement(4, {0,5})},
    {"p11c0", +1, 0, complement(0, {3})},
    {"p11c1", +1, 1, complement(1, {4})},
    {"p11c2", +1, 2, complement(2, {3})},
    {"p10x", +1, 5, complement(5, {6,7})},
    {"n10c0", -1, 0, complement(0, {3,5})},
    {"n10c1", -1, 1, complement(1, {0,3})},
    {"n10c2", -1, 2, complement(2, {1,3})},
    {"n11c3", -1, 3, complement(3, {0})},
    {"n11c4", -1, 4, complement(4, {3})},
    {"n10x", -1, 5, complement(5, {6,7})},
  };
  if (profile == 5) return {
    {"p10c4", +1, 4, complement(4, {5,11})},
    {"p11c0", +1, 0, complement(0, {4})},
    {"p11c4", +1, 4, complement(4, {5})},
    {"p11c5_1", +1, 5, complement(5, {4})},
    {"p11c5_2", +1, 5, complement(5, {4})},
    {"n10c0", -1, 0, complement(0, {1,11})},
    {"n10c5", -1, 5, complement(5, {1,2})},
    {"n11c1", -1, 1, complement(1, {3})},
    {"n11c2", -1, 2, complement(2, {3})},
    {"n11c3", -1, 3, complement(3, {2})},
  };
  throw std::runtime_error("profile must be 2,3,4,5,44");
}

static std::vector<int> deck(const Rail& rail, const std::vector<int>& cycle) {
  std::vector<int> out;
  const int n = static_cast<int>(cycle.size());
  out.reserve(n);
  for (int i = 0; i < n; ++i) {
    int mask = 1 << rail.center;
    for (int j = 0; j < 4; ++j) mask |= 1 << cycle[(i+j) % n];
    out.push_back(mask);
  }
  return out;
}

static int contribution(int mask, const std::array<int,8192>& pos,
                        const std::array<int,8192>& neg) {
  constexpr int target = (1<<5)-1;
  const int want = mask == target ? 1 : 0;
  return std::abs(pos[mask] - neg[mask] - want)
       + 4 * (std::max(0, pos[mask]-1) + std::max(0, neg[mask]-1));
}

struct Witness {
  int score = 1'000'000;
  std::vector<std::vector<int>> cycles;
};

int main(int argc, char** argv) {
  const uint64_t iterations = argc > 1 ? std::stoull(argv[1]) : 20'000'000ULL;
  const int threads = argc > 2 ? std::stoi(argv[2]) : 64;
  const uint64_t seed0 = argc > 3 ? std::stoull(argv[3]) : 20260814ULL;
  const int profile = argc > 4 ? std::stoi(argv[4]) : 3;
  const auto rails = make_rails(profile);
  const std::vector<std::vector<int>> profile44_seed = {
    {7,10,11,3,0,5,8,9,1,2},
    {2,12,5,11,6,10,8,1,9,0},
    {12,11,1,10,6,5,8,9,3,4,2},
    {8,5,11,12,6,10,2,0,4,3,9},
    {6,0,8,9,1,12,3,7,10,11,5},
    {0,1,2,3,4,8,9,10,11,12},
    {5,8,9,4,2,12,11,1,10,6},
    {12,6,10,2,0,4,9,8,5,11},
    {4,1,9,8,0,6,5,11,10,7},
    {1,9,8,5,0,4,11,10,7,2,12},
    {2,0,3,9,1,8,10,6,11,5,12},
    {0,1,2,3,4,8,9,10,11,12},
  };
  std::atomic<bool> found(false);
  std::mutex best_mutex;
  Witness global_best;

  auto worker = [&](int tid) {
    std::mt19937_64 rng(seed0 + 0x9e3779b97f4a7c15ULL * (tid+1));
    std::array<int,8192> pos{}, neg{};
    std::vector<std::vector<int>> cycles, decks;
    cycles.reserve(rails.size()); decks.reserve(rails.size());
    for (size_t initial_r=0; initial_r<rails.size(); ++initial_r) {
      const auto& rail=rails[initial_r];
      auto c = profile==44 ? profile44_seed[initial_r] : rail.support;
      if(profile!=44) std::shuffle(c.begin(), c.end(), rng);
      cycles.push_back(c);
      decks.push_back(deck(rail, c));
    }
    for (size_t r=0; r<rails.size(); ++r)
      for (int mask : decks[r]) (rails[r].sign>0 ? pos[mask] : neg[mask])++;
    int score=0;
    for (int mask=0; mask<8192; ++mask) score += contribution(mask,pos,neg);
    int local_best=score;
    uint64_t stale=0;
    const int shore = static_cast<int>(rails.size()/2);

    for (uint64_t it=0; it<iterations && !found.load(); ++it) {
      std::vector<int> changed;
      std::vector<std::vector<int>> old_cycles, old_decks, new_decks;
      if (rng()%5 != 0) {
        const int r = rng() % rails.size();
        const int n = cycles[r].size();
        int a = rng()%n, b=rng()%n;
        if (a==b) continue;
        changed.push_back(r);
        old_cycles.push_back(cycles[r]); old_decks.push_back(decks[r]);
        if (a>b) std::swap(a,b);
        if (rng()%3==0) {
          std::reverse(cycles[r].begin()+a,cycles[r].begin()+b+1);
        } else if (rng()%3==0 && b-a>=2) {
          std::rotate(cycles[r].begin()+a,cycles[r].begin()+a+1,
                      cycles[r].begin()+b+1);
        } else {
          std::swap(cycles[r][a], cycles[r][b]);
        }
      } else if (rng()%2 == 0) {
        // Same-sign 2x2 hole switch.  Positive (or negative) column counts
        // are preserved, hence so is every signed support equation.
        const int base = (rng()%2)*shore;
        int r1=base+rng()%shore, r2=base+rng()%shore;
        if(r1==r2) continue;
        int x=-1,y=-1;
        for(int tries=0;tries<40 && (x<0||y<0);++tries) {
          int z=rng()%13;
          const bool s1=std::find(cycles[r1].begin(),cycles[r1].end(),z)!=cycles[r1].end();
          const bool s2=std::find(cycles[r2].begin(),cycles[r2].end(),z)!=cycles[r2].end();
          if(!s1 && z!=rails[r1].center && s2 && z!=rails[r2].center) x=z;
          if(s1 && z!=rails[r1].center && !s2 && z!=rails[r2].center) y=z;
        }
        if(x<0||y<0) continue;
        changed={r1,r2}; old_cycles={cycles[r1],cycles[r2]};
        old_decks={decks[r1],decks[r2]};
        *std::find(cycles[r1].begin(),cycles[r1].end(),y)=x;
        *std::find(cycles[r2].begin(),cycles[r2].end(),x)=y;
      } else {
        // Move one common positive/negative hole x to a common supported
        // label y.  Both hole columns change together, preserving P_z-N_z.
        int rp=rng()%shore, rn=shore+rng()%shore;
        int x=-1,y=-1;
        for(int tries=0;tries<60 && (x<0||y<0);++tries) {
          int z=rng()%13;
          const bool sp=std::find(cycles[rp].begin(),cycles[rp].end(),z)!=cycles[rp].end();
          const bool sn=std::find(cycles[rn].begin(),cycles[rn].end(),z)!=cycles[rn].end();
          if(!sp && !sn && z!=rails[rp].center && z!=rails[rn].center) x=z;
          if(sp && sn && z!=rails[rp].center && z!=rails[rn].center) y=z;
        }
        if(x<0||y<0) continue;
        changed={rp,rn}; old_cycles={cycles[rp],cycles[rn]};
        old_decks={decks[rp],decks[rn]};
        *std::find(cycles[rp].begin(),cycles[rp].end(),y)=x;
        *std::find(cycles[rn].begin(),cycles[rn].end(),y)=x;
      }
      for(int r:changed) new_decks.push_back(deck(rails[r],cycles[r]));
      std::array<bool,8192> touched{};
      std::vector<int> touched_list;
      for(const auto& d:old_decks) for (int mask:d)
        if (!touched[mask]) {touched[mask]=true;touched_list.push_back(mask);}
      for(const auto& d:new_decks) for (int mask:d)
        if (!touched[mask]) {touched[mask]=true;touched_list.push_back(mask);}
      int before=0, after=0;
      for (int mask:touched_list) before += contribution(mask,pos,neg);
      for(size_t j=0;j<changed.size();++j)
        for(int mask:old_decks[j]) (rails[changed[j]].sign>0 ? pos[mask] : neg[mask])--;
      for(size_t j=0;j<changed.size();++j)
        for(int mask:new_decks[j]) (rails[changed[j]].sign>0 ? pos[mask] : neg[mask])++;
      for (int mask:touched_list) after += contribution(mask,pos,neg);
      const int candidate = score + after-before;
      const double phase = double(it % 250000ULL) / 250000.0;
      const double temperature = 4.0*(1.0-phase)+0.08;
      const bool accept = candidate <= score ||
        std::uniform_real_distribution<double>(0.0,1.0)(rng) <
          std::exp(double(score-candidate)/temperature);
      if (accept) {
        score=candidate;
        for(size_t j=0;j<changed.size();++j) decks[changed[j]]=std::move(new_decks[j]);
      } else {
        for(size_t j=0;j<changed.size();++j)
          for(int mask:new_decks[j]) (rails[changed[j]].sign>0 ? pos[mask] : neg[mask])--;
        for(size_t j=0;j<changed.size();++j)
          for(int mask:old_decks[j]) (rails[changed[j]].sign>0 ? pos[mask] : neg[mask])++;
        for(size_t j=0;j<changed.size();++j) cycles[changed[j]]=std::move(old_cycles[j]);
      }
      if (score < local_best) {
        local_best=score; stale=0;
        std::lock_guard<std::mutex> lock(best_mutex);
        if (score < global_best.score) {
          global_best.score=score; global_best.cycles=cycles;
          std::cerr << "best=" << score << " thread=" << tid << " iter=" << it << "\n";
        }
      } else ++stale;
      if (score==0) { found.store(true); break; }
      if (stale > 500000) {
        pos.fill(0); neg.fill(0); cycles.clear(); decks.clear();
        for (const auto& rail:rails) {
          auto c=rail.support; std::shuffle(c.begin(),c.end(),rng);
          cycles.push_back(c); decks.push_back(deck(rail,c));
        }
        for (size_t rr=0; rr<rails.size(); ++rr)
          for (int mask:decks[rr]) (rails[rr].sign>0 ? pos[mask] : neg[mask])++;
        score=0; for(int mask=0;mask<8192;++mask) score+=contribution(mask,pos,neg);
        local_best=score; stale=0;
      }
    }
  };

  std::vector<std::thread> pool;
  for(int t=0;t<threads;++t) pool.emplace_back(worker,t);
  for(auto& th:pool) th.join();
  std::cout << "status=" << (global_best.score==0 ? "SAT" : "NO_WITNESS")
            << " best=" << global_best.score << " threads=" << threads
            << " iterations_per_thread=" << iterations << " profile=" << profile << "\n";
  if (!global_best.cycles.empty()) {
    std::array<int,8192> pos{},neg{};
    for(size_t r=0;r<rails.size();++r) {
      std::cout << rails[r].name << " center=" << rails[r].center << " order=";
      for(size_t i=0;i<global_best.cycles[r].size();++i)
        std::cout << (i?",":"") << global_best.cycles[r][i];
      std::cout << "\n";
      for(int mask:deck(rails[r],global_best.cycles[r]))
        (rails[r].sign>0 ? pos[mask] : neg[mask])++;
    }
    for(int mask=0;mask<8192;++mask) {
      const int want=mask==((1<<5)-1);
      if(pos[mask]-neg[mask]!=want || pos[mask]>1 || neg[mask]>1)
        std::cout << "defect mask=" << mask << " pos=" << pos[mask]
                  << " neg=" << neg[mask] << " want=" << want << "\n";
    }
  }
  return global_best.score==0 ? 0 : 2;
}
