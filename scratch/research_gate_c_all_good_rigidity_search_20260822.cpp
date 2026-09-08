#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <vector>

static int good_count(const std::vector<int>& order) {
  const int k = static_cast<int>(order.size());
  std::vector<int> inverse(k);
  for (int i = 0; i < k; ++i) inverse[order[i]] = i;
  int answer = 0;
  for (int value = 0; value < k; ++value) {
    int height = 0, minimum = k, maximum = -k;
    for (int length = 1; length < k; ++length) {
      int distance = inverse[(value + length) % k] - inverse[value];
      if (distance <= 0) distance += k;
      height += ((distance - length) & 1) ? -1 : 1;
      minimum = std::min(minimum, height);
      maximum = std::max(maximum, height);
    }
    answer += minimum >= 0 && maximum <= height;
  }
  return answer;
}

static std::vector<int> gaps(const std::vector<int>& order) {
  const int k = static_cast<int>(order.size());
  std::vector<int> inverse(k), answer(k);
  for (int i = 0; i < k; ++i) inverse[order[i]] = i;
  for (int a = 0; a < k; ++a) {
    answer[a] = inverse[(a + 1) % k] - inverse[a];
    if (answer[a] <= 0) answer[a] += k;
  }
  return answer;
}

int main(int argc, char** argv) {
  const int k = argc > 1 ? std::stoi(argv[1]) : 13;
  const int restarts = argc > 2 ? std::stoi(argv[2]) : 2000;
  std::mt19937_64 rng(0xA11C00DULL + k);
  std::vector<int> order(k);
  std::iota(order.begin(), order.end(), 0);
  std::set<std::vector<int>> normalized_gap_hits;
  int best = 0;
  for (int restart = 0; restart < restarts; ++restart) {
    std::shuffle(order.begin(), order.end(), rng);
    int current = good_count(order);
    double temperature = 2.0;
    for (int iteration = 0; iteration < 30000; ++iteration) {
      int x = rng() % k, y = rng() % k;
      if (x == y) continue;
      std::swap(order[x], order[y]);
      int candidate = good_count(order);
      const bool accept = candidate >= current ||
          std::generate_canonical<double, 53>(rng) <
              std::exp((candidate - current) / temperature);
      if (accept) current = candidate;
      else std::swap(order[x], order[y]);
      temperature *= 0.9996;
      if (temperature < 0.02) temperature = 0.02;
      best = std::max(best, current);
      if (current == k) {
        auto d = gaps(order);
        const int shift = std::min_element(d.begin(), d.end()) - d.begin();
        std::rotate(d.begin(), d.begin() + shift, d.end());
        normalized_gap_hits.insert(d);
        break;
      }
    }
  }
  std::cout << "K=" << k << " best=" << best
            << " all_good_gap_types=" << normalized_gap_hits.size() << '\n';
  for (const auto& d : normalized_gap_hits) {
    bool constant = std::all_of(d.begin(), d.end(), [&](int x) {
      return x == d.front();
    });
    std::cout << (constant ? "CONSTANT " : "NONCONSTANT ");
    for (int x : d) std::cout << x << ',';
    std::cout << '\n';
  }
}
