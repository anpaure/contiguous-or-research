#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <tuple>
#include <vector>

using Clock = std::chrono::steady_clock;

struct Solver {
  int n = 0, m = 0, k = 0, target_depth = 0;
  std::vector<std::vector<int>> edges;
  std::vector<std::vector<int>> incidence;
  std::vector<int> degree;
  std::vector<unsigned char> covered, active;
  std::vector<int> solution, best;
  std::mt19937_64 rng;
  Clock::time_point deadline;
  uint64_t nodes = 0;
  bool timed_out = false;

  explicit Solver(uint64_t seed) : rng(seed) {}

  bool load(const std::string &path) {
    std::ifstream input(path);
    if (!(input >> n >> m >> k)) return false;
    edges.assign(m, std::vector<int>(k));
    incidence.assign(n, {});
    for (int e = 0; e < m; ++e) {
      for (int j = 0; j < k; ++j) {
        input >> edges[e][j];
        if (edges[e][j] < 0 || edges[e][j] >= n) return false;
        incidence[edges[e][j]].push_back(e);
      }
    }
    if (n % k) return false;
    target_depth = n / k;
    return true;
  }

  void reset() {
    covered.assign(n, 0);
    active.assign(m, 1);
    degree.resize(n);
    for (int v = 0; v < n; ++v) degree[v] = incidence[v].size();
    solution.clear();
    best.clear();
    nodes = 0;
    timed_out = false;
  }

  int choose_vertex() {
    int chosen = -1;
    int best_degree = m + 1;
    std::vector<int> ties;
    for (int v = 0; v < n; ++v) {
      if (covered[v]) continue;
      if (degree[v] < best_degree) {
        best_degree = degree[v];
        ties.assign(1, v);
      } else if (degree[v] == best_degree) {
        ties.push_back(v);
      }
    }
    if (!ties.empty()) chosen = ties[rng() % ties.size()];
    return chosen;
  }

  bool select_edge(int e, std::vector<int> &disabled) {
    for (int v : edges[e]) if (covered[v]) return false;
    for (int v : edges[e]) covered[v] = 1;
    disabled.clear();
    for (int v : edges[e]) {
      for (int f : incidence[v]) {
        if (!active[f]) continue;
        active[f] = 0;
        disabled.push_back(f);
        for (int w : edges[f]) if (!covered[w]) --degree[w];
      }
    }
    solution.push_back(e);
    return true;
  }

  void undo_edge(int e, const std::vector<int> &disabled) {
    solution.pop_back();
    for (int v : edges[e]) covered[v] = 0;
    for (auto it = disabled.rbegin(); it != disabled.rend(); ++it) {
      int f = *it;
      active[f] = 1;
      for (int w : edges[f]) if (!covered[w]) ++degree[w];
    }
  }

  bool search() {
    ++nodes;
    if ((nodes & ((1u << 15) - 1)) == 0 && Clock::now() >= deadline) {
      timed_out = true;
      return false;
    }
    if (solution.size() > best.size()) {
      best = solution;
      if (best.size() % 10 == 0 || best.size() + 5 >= target_depth) {
        std::cerr << "best=" << best.size() << " nodes=" << nodes << "\n";
      }
    }
    if ((int)solution.size() == target_depth) return true;
    int v = choose_vertex();
    if (v < 0) return true;
    if (degree[v] == 0) return false;

    std::vector<std::tuple<int, uint64_t, int>> options;
    options.reserve(degree[v]);
    for (int e : incidence[v]) {
      if (!active[e]) continue;
      int score = 0;
      for (int w : edges[e]) score += degree[w];
      options.emplace_back(score, rng(), e);
    }
    std::sort(options.begin(), options.end());

    for (const auto &[score, noise, e] : options) {
      (void)score;
      (void)noise;
      std::vector<int> disabled;
      if (!select_edge(e, disabled)) continue;
      if (search()) return true;
      undo_edge(e, disabled);
      if (timed_out) return false;
    }
    return false;
  }

  bool run(double seconds) {
    reset();
    deadline = Clock::now() + std::chrono::milliseconds((long long)(seconds * 1000));
    bool result = search();
    std::cerr << "nodes=" << nodes << " best=" << best.size()
              << " timeout=" << timed_out << "\n";
    return result;
  }
};

int main(int argc, char **argv) {
  if (argc < 4) {
    std::cerr << "usage: solver EDGE_FILE SECONDS SEED\n";
    return 2;
  }
  Solver solver(std::stoull(argv[3]));
  if (!solver.load(argv[1])) {
    std::cerr << "failed to load edge file\n";
    return 2;
  }
  bool sat = solver.run(std::stod(argv[2]));
  if (!sat) {
    std::cout << "UNKNOWN nodes=" << solver.nodes
              << " best=" << solver.best.size() << "\n";
    return 0;
  }
  std::vector<int> load(solver.n, 0);
  for (int e : solver.solution) for (int v : solver.edges[e]) ++load[v];
  if (!std::all_of(load.begin(), load.end(), [](int x) { return x == 1; })) {
    std::cerr << "internal verification failed selected="
              << solver.solution.size() << "\n";
    int shown = 0;
    for (int v = 0; v < solver.n && shown < 30; ++v) {
      if (load[v] != 1) {
        std::cerr << " bad_vertex=" << v << " load=" << load[v] << "\n";
        ++shown;
      }
    }
    std::cout << "INVALID selected=" << solver.solution.size() << "\n";
    for (int e : solver.solution) std::cout << e << "\n";
    return 3;
  }
  std::cout << "SAT selected=" << solver.solution.size()
            << " nodes=" << solver.nodes << "\n";
  for (int e : solver.solution) std::cout << e << "\n";
  return 0;
}
