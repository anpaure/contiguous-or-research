#include <algorithm>
#include <array>
#include <bit>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <set>
#include <vector>

using u64 = std::uint64_t;

long double falling(int d, int k) {
  if (d < k) return 0.0L;
  long double value = 1.0L;
  for (int j = 0; j < k; ++j) value *= d - j;
  return value;
}

int main(int argc, char** argv) {
  constexpr int r = 3;
  constexpr int b = 7;
  const double p = argc > 1 ? std::stod(argv[1]) : 0.9;
  const int samples = argc > 2 ? std::stoi(argv[2]) : 100000;
  const std::uint64_t seed = argc > 3 ? std::stoull(argv[3]) : 20260822ULL;

  std::vector<u64> middle;
  std::vector<u64> lower;
  for (u64 mask = 0; mask < (1ULL << b); ++mask) {
    if (std::popcount(mask) == r) middle.push_back(mask);
    if (std::popcount(mask) == r - 1) lower.push_back(mask);
  }
  std::map<std::pair<char, u64>, int> target_id;
  for (u64 mask : middle) target_id[{'M', mask}] = target_id.size();
  for (u64 mask : lower) target_id[{'L', mask}] = target_id.size();
  if (target_id.size() != 56) return 2;

  std::array<int, b> word{};
  std::iota(word.begin(), word.end(), 0);
  std::set<u64> row_set;
  do {
    u64 row = 0;
    for (int start = 1; start < b; ++start) {
      u64 mm = 0;
      u64 lm = 0;
      for (int j = 0; j < r; ++j) mm |= 1ULL << word[(start + j) % b];
      for (int j = 0; j < r - 1; ++j) lm |= 1ULL << word[(start + j) % b];
      row |= 1ULL << target_id[{'M', mm}];
      row |= 1ULL << target_id[{'L', lm}];
    }
    row_set.insert(row);
  } while (std::next_permutation(word.begin(), word.end()));
  if (row_set.size() != 5040) return 3;
  std::vector<u64> rows(row_set.begin(), row_set.end());

  const int root = target_id[{'M', middle.front()}];
  const u64 root_bit = 1ULL << root;
  std::vector<u64> star;
  for (u64 row : rows) {
    if (row & root_bit) star.push_back(row);
  }
  const int D = star.size();
  if (D != 864) return 4;

  const int chunks = (D + 63) / 64;
  std::vector<std::vector<u64>> overlap(D, std::vector<u64>(chunks));
  for (int i = 0; i < D; ++i) {
    for (int j = i + 1; j < D; ++j) {
      if (((star[i] & star[j]) & ~root_bit) != 0) {
        overlap[i][j / 64] |= 1ULL << (j % 64);
        overlap[j][i / 64] |= 1ULL << (i % 64);
      }
    }
  }

  const long double z = D * std::pow(p, 4 * r - 1);
  std::vector<int> cutoffs;
  for (double multiplier : {1.0, 1.05, 1.1, 1.2, 1.4, 1.6, 2.0}) {
    cutoffs.push_back(static_cast<int>(std::ceil(multiplier * z)));
  }
  std::sort(cutoffs.begin(), cutoffs.end());
  cutoffs.erase(std::unique(cutoffs.begin(), cutoffs.end()), cutoffs.end());

  struct Accumulator {
    long double mass = 0.0L;
    long double overlap = 0.0L;
    long double degree = 0.0L;
    int nonzero = 0;
  };
  Accumulator factorial;
  std::vector<Accumulator> tail(cutoffs.size());
  std::vector<long double> degree_overlap_sum(D + 1, 0.0L);
  std::vector<int> degree_sample_count(D + 1, 0);

  std::mt19937_64 rng(seed);
  std::bernoulli_distribution retain(p);
  std::vector<u64> live_bits(chunks);
  std::vector<int> live;
  for (int sample = 0; sample < samples; ++sample) {
    u64 state = root_bit;
    for (int target = 0; target < 56; ++target) {
      if (target != root && retain(rng)) state |= 1ULL << target;
    }
    std::fill(live_bits.begin(), live_bits.end(), 0);
    live.clear();
    for (int i = 0; i < D; ++i) {
      if ((star[i] & ~state) == 0) {
        live.push_back(i);
        live_bits[i / 64] |= 1ULL << (i % 64);
      }
    }
    const int d = live.size();
    if (d < 2) continue;
    std::uint64_t overlap_ordered = 0;
    for (int i : live) {
      for (int chunk = 0; chunk < chunks; ++chunk) {
        overlap_ordered += std::popcount(overlap[i][chunk] & live_bits[chunk]);
      }
    }
    const long double overlap_fraction =
        static_cast<long double>(overlap_ordered) /
        (static_cast<long double>(d) * (d - 1));
    degree_overlap_sum[d] += overlap_fraction;
    ++degree_sample_count[d];

    const long double wf = falling(d, 12);
    factorial.mass += wf;
    factorial.overlap += wf * overlap_fraction;
    factorial.degree += wf * d;
    if (wf > 0) ++factorial.nonzero;

    for (std::size_t index = 0; index < cutoffs.size(); ++index) {
      const int excess = std::max(d - cutoffs[index], 0);
      const long double wt = std::pow(static_cast<long double>(excess), 12);
      tail[index].mass += wt;
      tail[index].overlap += wt * overlap_fraction;
      tail[index].degree += wt * d;
      if (wt > 0) ++tail[index].nonzero;
    }
  }

  std::cout << std::setprecision(10);
  std::cout << "r 3 p " << p << " samples " << samples << " z " << z << "\n";
  std::cout << "factorial overlap " << factorial.overlap / factorial.mass
            << " tilted_degree " << factorial.degree / factorial.mass
            << " nonzero_samples " << factorial.nonzero << "\n";
  for (std::size_t index = 0; index < cutoffs.size(); ++index) {
    std::cout << "cutoff " << cutoffs[index]
              << " ratio " << static_cast<long double>(cutoffs[index]) / z
              << " overlap " << tail[index].overlap / tail[index].mass
              << " tilted_degree " << tail[index].degree / tail[index].mass
              << " nonzero_samples " << tail[index].nonzero << "\n";
  }
  int adjacent_increases = 0;
  int previous_degree = -1;
  long double previous_mean = 0.0L;
  for (int d = 2; d <= D; ++d) {
    if (degree_sample_count[d] < 50) continue;
    const long double mean = degree_overlap_sum[d] / degree_sample_count[d];
    if (previous_degree >= 0 && mean > previous_mean) ++adjacent_increases;
    previous_degree = d;
    previous_mean = mean;
  }
  std::cout << "degree-profile supported-adjacent increases "
            << adjacent_increases << "\n";
  for (int d = 2; d <= D; ++d) {
    if (degree_sample_count[d] >= 1000 && d % 20 == 0) {
      std::cout << "degree-bin " << d << " overlap "
                << degree_overlap_sum[d] / degree_sample_count[d]
                << " samples " << degree_sample_count[d] << "\n";
    }
  }
}
