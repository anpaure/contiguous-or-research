#include <algorithm>
#include <array>
#include <atomic>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <numeric>
#include <random>
#include <thread>
#include <unordered_map>
#include <vector>

using std::array;
using std::vector;

constexpr int K = 17;
constexpr int U = 1430;
constexpr uint32_t FULL = (1u << K) - 1;

uint32_t rotate_mask(uint32_t mask, int shift) {
  if (!shift) return mask;
  return ((mask << shift) | (mask >> (K - shift))) & FULL;
}

uint32_t canonical(uint32_t mask) {
  uint32_t best = mask;
  for (int s = 1; s < K; ++s) best = std::min(best, rotate_mask(mask, s));
  return best;
}

struct Candidate {
  array<int, 5> core{};
  array<int, 10> order{};
  array<int, 10> edge{};
};

struct Universe {
  vector<uint32_t> reps;
  std::unordered_map<uint32_t, int> index;
  Universe() {
    for (uint32_t mask = 0; mask <= FULL; ++mask)
      if (__builtin_popcount(mask) == 9) reps.push_back(canonical(mask));
    std::sort(reps.begin(), reps.end());
    reps.erase(std::unique(reps.begin(), reps.end()), reps.end());
    if ((int)reps.size() != U) std::abort();
    for (int i = 0; i < U; ++i) index.emplace(reps[i], i);
  }
};

bool build_edge(Candidate &c, Universe const &universe) {
  uint32_t core_mask = 0;
  for (int x : c.core) core_mask |= 1u << x;
  for (int i = 0; i < 10; ++i) {
    uint32_t owner = core_mask;
    for (int j = 0; j < 4; ++j) owner |= 1u << c.order[(i + j) % 10];
    auto it = universe.index.find(canonical(owner));
    if (it == universe.index.end()) std::abort();
    c.edge[i] = it->second;
  }
  std::sort(c.edge.begin(), c.edge.end());
  return std::adjacent_find(c.edge.begin(), c.edge.end()) == c.edge.end();
}

template<class RNG>
Candidate random_candidate(RNG &rng, Universe const &universe) {
  array<int, K> labels{};
  std::iota(labels.begin(), labels.end(), 0);
  for (;;) {
    std::shuffle(labels.begin(), labels.end(), rng);
    Candidate c;
    std::copy_n(labels.begin(), 5, c.core.begin());
    std::copy_n(labels.begin() + 5, 10, c.order.begin());
    if (build_edge(c, universe)) return c;
  }
}

template<class RNG>
Candidate conditioned_candidate(int vertex, RNG &rng, Universe const &universe) {
  array<int, 9> inside{};
  array<int, 8> outside{};
  int ni = 0, no = 0;
  uint32_t owner = universe.reps[vertex];
  for (int x = 0; x < K; ++x)
    ((owner >> x) & 1 ? inside[ni++] : outside[no++]) = x;
  for (;;) {
    std::shuffle(inside.begin(), inside.end(), rng);
    std::shuffle(outside.begin(), outside.end(), rng);
    Candidate c;
    std::copy_n(inside.begin(), 5, c.core.begin());
    array<int, 4> window{};
    std::copy_n(inside.begin() + 5, 4, window.begin());
    std::shuffle(window.begin(), window.end(), rng);
    array<int, 6> singles{};
    std::copy_n(outside.begin(), 6, singles.begin());
    std::shuffle(singles.begin(), singles.end(), rng);
    int block_position = std::uniform_int_distribution<int>(0, 6)(rng);
    int out = 0;
    for (int unit = 0; unit < 7; ++unit) {
      if (unit == block_position)
        for (int x : window) c.order[out++] = x;
      else
        c.order[out++] = singles[unit - (unit > block_position)];
    }
    if (out != 10) std::abort();
    if (build_edge(c, universe) &&
        std::binary_search(c.edge.begin(), c.edge.end(), vertex)) return c;
  }
}

template<class RNG>
Candidate mutate_candidate(Candidate const &old, RNG &rng,
                           Universe const &universe) {
  for (;;) {
    Candidate c = old;
    int kind = std::uniform_int_distribution<int>(0, 3)(rng);
    if (kind == 0) {
      int a = std::uniform_int_distribution<int>(0, 9)(rng);
      int b = std::uniform_int_distribution<int>(0, 9)(rng);
      if (a == b) continue;
      std::swap(c.order[a], c.order[b]);
    } else if (kind == 1) {
      int a = std::uniform_int_distribution<int>(0, 4)(rng);
      int b = std::uniform_int_distribution<int>(0, 9)(rng);
      std::swap(c.core[a], c.order[b]);
    } else {
      bool used[K] = {};
      for (int x : c.core) used[x] = true;
      for (int x : c.order) used[x] = true;
      array<int, 2> holes{};
      int h = 0;
      for (int x = 0; x < K; ++x) if (!used[x]) holes[h++] = x;
      int which = std::uniform_int_distribution<int>(0, 1)(rng);
      if (kind == 2) {
        int a = std::uniform_int_distribution<int>(0, 4)(rng);
        std::swap(c.core[a], holes[which]);
      } else {
        int a = std::uniform_int_distribution<int>(0, 9)(rng);
        std::swap(c.order[a], holes[which]);
      }
    }
    if (build_edge(c, universe)) return c;
  }
}

int score(vector<int> const &loads) {
  int out = 0;
  for (int value : loads) out += (value - 1) * (value - 1);
  return out;
}

int replacement_delta(Candidate const &old, Candidate const &fresh,
                      vector<int> const &loads) {
  std::unordered_map<int, int> change;
  for (int v : old.edge) --change[v];
  for (int v : fresh.edge) ++change[v];
  int delta = 0;
  for (auto [v, d] : change) {
    int before = loads[v] - 1;
    int after = loads[v] + d - 1;
    delta += after * after - before * before;
  }
  return delta;
}

std::atomic<bool> found(false);
std::atomic<int> global_best(1 << 30);
std::mutex output_mutex;

void worker(int tid, uint64_t iterations, Universe const &universe) {
  std::mt19937_64 rng(20260814ull + 1000003ull * tid);
  vector<Candidate> state(143);
  vector<int> loads(U, 0);
  for (auto &candidate : state) {
    candidate = random_candidate(rng, universe);
    for (int v : candidate.edge) ++loads[v];
  }
  int current = score(loads);
  int local_best = current;
  uint64_t stale = 0;
  for (uint64_t iteration = 1; iteration <= iterations && !found; ++iteration) {
    int remove = std::uniform_int_distribution<int>(0, 142)(rng);
    Candidate proposal;
    if (std::uniform_int_distribution<int>(0, 99)(rng) < 75) {
      vector<int> holes;
      for (int v = 0; v < U; ++v) if (!loads[v]) holes.push_back(v);
      if (!holes.empty()) {
        int target = holes[std::uniform_int_distribution<int>(0, holes.size()-1)(rng)];
        proposal = conditioned_candidate(target, rng, universe);
        int best_over = -1;
        for (int trial = 0; trial < 24; ++trial) {
          int candidate_index = std::uniform_int_distribution<int>(0, 142)(rng);
          int over = 0;
          for (int v : state[candidate_index].edge) over += std::max(0, loads[v]-1);
          if (over > best_over) { best_over = over; remove = candidate_index; }
        }
      } else proposal = mutate_candidate(state[remove], rng, universe);
    } else {
      proposal = mutate_candidate(state[remove], rng, universe);
    }
    int delta = replacement_delta(state[remove], proposal, loads);
    double phase = double(iteration % 1000000ull) / 1000000.0;
    double temperature = 0.03 + 2.0 * (1.0 - phase);
    bool accept = delta <= 0 ||
      std::uniform_real_distribution<double>(0.0, 1.0)(rng) < std::exp(-delta / temperature);
    if (!accept) continue;
    for (int v : state[remove].edge) --loads[v];
    for (int v : proposal.edge) ++loads[v];
    state[remove] = proposal;
    current += delta;
    if (current < local_best) {
      local_best = current;
      stale = 0;
      int prior = global_best.load();
      while (current < prior && !global_best.compare_exchange_weak(prior, current)) {}
      if (tid == 0 || current <= 20)
        std::cerr << "best=" << current << " thread=" << tid
                  << " iteration=" << iteration << "\n";
    } else ++stale;
    if (!current && !found.exchange(true)) {
      std::lock_guard<std::mutex> lock(output_mutex);
      std::cout << "{\n  \"status\": \"PASS\",\n  \"thread\": " << tid
                << ",\n  \"iteration\": " << iteration
                << ",\n  \"certificate\": [\n";
      for (int i = 0; i < 143; ++i) {
        std::cout << "    {\"core\":[";
        for (int j = 0; j < 5; ++j) std::cout << (j ? "," : "") << state[i].core[j];
        std::cout << "],\"order\":[";
        for (int j = 0; j < 10; ++j) std::cout << (j ? "," : "") << state[i].order[j];
        std::cout << "]}" << (i == 142 ? "\n" : ",\n");
      }
      std::cout << "  ]\n}\n";
    }
    if (stale > 3000000ull) {
      for (int &value : loads) value = 0;
      for (auto &candidate : state) {
        candidate = random_candidate(rng, universe);
        for (int v : candidate.edge) ++loads[v];
      }
      current = score(loads);
      local_best = current;
      stale = 0;
    }
  }
}

int main(int argc, char **argv) {
  int threads = argc > 1 ? std::stoi(argv[1]) : 32;
  uint64_t iterations = argc > 2 ? std::stoull(argv[2]) : 100000000ull;
  Universe universe;
  vector<std::thread> jobs;
  for (int t = 0; t < threads; ++t) jobs.emplace_back(worker, t, iterations, std::cref(universe));
  for (auto &job : jobs) job.join();
  if (!found) std::cout << "{\"status\":\"NO_WITNESS\",\"best\":"
                        << global_best.load() << "}\n";
}
