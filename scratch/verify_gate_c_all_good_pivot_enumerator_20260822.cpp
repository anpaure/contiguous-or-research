#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>

struct Enumerator {
  int k, e;
  std::vector<int> color, used, order, inverse;
  std::uint64_t pivot_leaves = 0, all_good = 0;
  std::set<int> constant_gaps;
  bool counterexample = false;

  explicit Enumerator(int size)
      : k(size), e((size - 1) / 2), color(k), used(k), order(k), inverse(k) {}

  std::vector<int> candidates(int position) {
    std::vector<int> increment(k), cumulative(k + 1), prefix_min(k + 1),
        prefix_max(k + 1), suffix_min(k + 1), suffix_max(k + 1);
    for (int value = 0; value < k; ++value)
      increment[value] = color[value] * (used[value] ? -1 : 1);
    for (int value = 0; value < k; ++value)
      cumulative[value + 1] = cumulative[value] + increment[value];
    prefix_min[0] = prefix_max[0] = cumulative[0];
    for (int index = 1; index <= k; ++index) {
      prefix_min[index] = std::min(prefix_min[index - 1], cumulative[index]);
      prefix_max[index] = std::max(prefix_max[index - 1], cumulative[index]);
    }
    suffix_min[k] = suffix_max[k] = cumulative[k];
    for (int index = k - 1; index >= 0; --index) {
      suffix_min[index] = std::min(suffix_min[index + 1], cumulative[index]);
      suffix_max[index] = std::max(suffix_max[index + 1], cumulative[index]);
    }
    std::vector<int> answer;
    for (int value = 0; value < k; ++value) {
      if (used[value] || color[value] != (((value + position) & 1) ? -1 : 1))
        continue;
      bool pivot = false;
      if (increment[value] == 1)
        pivot = cumulative[value] == prefix_min[value] &&
                cumulative[value + 1] == suffix_min[value + 1];
      else
        pivot = cumulative[value] == prefix_max[value] &&
                cumulative[value + 1] == suffix_max[value + 1];
      if (pivot) answer.push_back(value);
    }
    if (answer.size() > 2) {
      std::cerr << "internal pivot-count failure\n";
      std::exit(2);
    }
    return answer;
  }

  bool good_cut(int root) const {
    int height = 0, minimum = k, maximum = -k;
    for (int offset = 1; offset < k; ++offset) {
      int distance = inverse[(root + offset) % k] - inverse[root];
      if (distance <= 0) distance += k;
      height += ((distance - offset) & 1) ? -1 : 1;
      minimum = std::min(minimum, height);
      maximum = std::max(maximum, height);
    }
    return minimum >= 0 && maximum <= height;
  }

  void inspect_leaf() {
    ++pivot_leaves;
    for (int position = 0; position < k; ++position) inverse[order[position]] = position;
    for (int root = 0; root < k; ++root)
      if (!good_cut(root)) return;
    ++all_good;
    std::vector<int> gaps(k);
    for (int root = 0; root < k; ++root) {
      gaps[root] = inverse[(root + 1) % k] - inverse[root];
      if (gaps[root] <= 0) gaps[root] += k;
    }
    if (!std::all_of(gaps.begin(), gaps.end(), [&](int gap) { return gap == gaps[0]; })) {
      counterexample = true;
      std::cout << "NONAFFINE K=" << k << " order=";
      for (int value : order) std::cout << value << ',';
      std::cout << " gaps=";
      for (int gap : gaps) std::cout << gap << ',';
      std::cout << '\n';
      return;
    }
    constant_gaps.insert(gaps[0]);
  }

  void dfs(int position) {
    if (counterexample) return;
    if (position == k) {
      inspect_leaf();
      return;
    }
    for (int value : candidates(position)) {
      if (position == 0 && value != 0) continue;
      used[value] = 1;
      order[position] = value;
      dfs(position + 1);
      used[value] = 0;
    }
  }

  void run() {
    // Normalization tau(0)=0 forces value 0 into the even-position class.
    const std::uint64_t limit = 1ULL << (k - 1);
    for (std::uint64_t mask = 0; mask < limit && !counterexample; ++mask) {
      if (__builtin_popcountll(mask) != e) continue;
      std::fill(used.begin(), used.end(), 0);
      for (int value = 0; value < k; ++value) {
        const bool allowed_even = value == 0 || (mask & (1ULL << (value - 1)));
        color[value] = allowed_even ? ((value & 1) ? -1 : 1)
                                    : ((value & 1) ? 1 : -1);
      }
      dfs(0);
    }
  }
};

int main(int argc, char** argv) {
  int k = argc > 1 ? std::stoi(argv[1]) : 13;
  if (k < 3 || !(k & 1) || k >= 63) return 2;
  Enumerator enumerator(k);
  enumerator.run();
  std::cout << "K=" << k << " pivot_leaves=" << enumerator.pivot_leaves
            << " all_good=" << enumerator.all_good << " constant_gaps=";
  for (int gap : enumerator.constant_gaps) std::cout << gap << ',';
  std::cout << '\n';
  return enumerator.counterexample ? 1 : 0;
}
