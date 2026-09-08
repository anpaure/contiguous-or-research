#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

struct Profile {
  int bad_count;
  int bad_value;
  int reflection_mismatches;
  std::vector<int> gaps;
};

static Profile profile(const std::vector<int>& order) {
  const int k = static_cast<int>(order.size());
  std::vector<int> inverse(k);
  for (int i = 0; i < k; ++i) inverse[order[i]] = i;
  std::vector<int> gaps(k);
  for (int value = 0; value < k; ++value) {
    gaps[value] = inverse[(value + 1) % k] - inverse[value];
    if (gaps[value] <= 0) gaps[value] += k;
  }
  int bad_count = 0;
  int bad_value = -1;
  for (int value = 0; value < k; ++value) {
    int height = 0, minimum = k, maximum = -k;
    for (int length = 1; length < k; ++length) {
      int distance = inverse[(value + length) % k] - inverse[value];
      if (distance <= 0) distance += k;
      height += ((distance - length) & 1) ? -1 : 1;
      minimum = std::min(minimum, height);
      maximum = std::max(maximum, height);
    }
    if (minimum < 0 || maximum > height) {
      ++bad_count;
      bad_value = value;
    }
  }
  int mismatches = 0;
  if (bad_count == 1) {
    const int half = (k - 1) / 2;
    const int free_gap = (bad_value + half) % k;
    for (int step = 1; step <= half; ++step)
      mismatches += gaps[(free_gap + step) % k] !=
                    gaps[(free_gap - step + k) % k];
  }
  return {bad_count, bad_value, mismatches, gaps};
}

int main(int argc, char** argv) {
  const int k = argc > 1 ? std::stoi(argv[1]) : 17;
  const int restarts = argc > 2 ? std::stoi(argv[2]) : 2000;
  std::mt19937_64 rng(20260822 + k);
  std::vector<int> order(k);
  std::iota(order.begin(), order.end(), 0);
  int one_bad_hits = 0;
  for (int restart = 0; restart < restarts; ++restart) {
    std::shuffle(order.begin(), order.end(), rng);
    Profile current = profile(order);
    double temperature = 3.0;
    for (int iteration = 0; iteration < 20000; ++iteration) {
      int x = rng() % k, y = rng() % k;
      if (x == y) continue;
      std::swap(order[x], order[y]);
      Profile candidate = profile(order);
      const double old_energy = 20.0 * std::abs(current.bad_count - 1) -
                                current.reflection_mismatches;
      const double new_energy = 20.0 * std::abs(candidate.bad_count - 1) -
                                candidate.reflection_mismatches;
      const bool accept = new_energy <= old_energy ||
          std::generate_canonical<double, 53>(rng) <
              std::exp((old_energy - new_energy) / temperature);
      if (accept) {
        current = std::move(candidate);
      } else {
        std::swap(order[x], order[y]);
      }
      temperature *= 0.9997;
      if (temperature < 0.03) temperature = 0.03;
      if (current.bad_count == 1) {
        ++one_bad_hits;
        if (current.reflection_mismatches) {
          std::cout << "COUNTEREXAMPLE K=" << k
                    << " bad=" << current.bad_value
                    << " mismatches=" << current.reflection_mismatches
                    << " order=";
          for (int value : order) std::cout << value << ',';
          std::cout << " gaps=";
          for (int gap : current.gaps) std::cout << gap << ',';
          std::cout << '\n';
          return 1;
        }
      }
    }
  }
  std::cout << "NO_COUNTEREXAMPLE K=" << k
            << " one_bad_hits=" << one_bad_hits << '\n';
}
