#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

using Target = std::uint64_t;

struct Model {
  int r;
  int b;
  double p;
  std::mt19937_64 rng;
  std::vector<int> labels;
  std::vector<Target> base;

  Model(int rr, double pp, std::uint64_t seed)
      : r(rr), b(2 * rr + 1), p(pp), rng(seed), labels(b) {
    std::iota(labels.begin(), labels.end(), 0);
    base = make_row(labels);
  }

  Target target(int shore, std::uint32_t mask) const {
    return (static_cast<Target>(shore) << 32) | mask;
  }

  std::vector<Target> make_row(const std::vector<int>& word) const {
    std::vector<Target> row;
    row.reserve(4 * r);
    for (int start = 1; start < b; ++start) {
      std::uint32_t middle = 0, lower = 0;
      for (int j = 0; j < r; ++j) middle |= 1U << word[(start + j) % b];
      for (int j = 0; j < r - 1; ++j) lower |= 1U << word[(start + j) % b];
      row.push_back(target(1, middle));
      row.push_back(target(0, lower));
    }
    std::sort(row.begin(), row.end());
    return row;
  }

  Target middle_root(int position) const {
    std::uint32_t mask = 0;
    for (int j = 0; j < r; ++j) mask |= 1U << ((position + j) % b);
    return target(1, mask);
  }

  std::vector<Target> uniform_row() {
    auto word = labels;
    std::shuffle(word.begin(), word.end(), rng);
    return make_row(word);
  }

  std::vector<Target> uniform_root_row(Target root) {
    const std::uint32_t root_mask = static_cast<std::uint32_t>(root);
    std::vector<int> inside, outside;
    for (int x : labels) ((root_mask >> x) & 1U ? inside : outside).push_back(x);
    std::shuffle(inside.begin(), inside.end(), rng);
    std::shuffle(outside.begin(), outside.end(), rng);
    std::uniform_int_distribution<int> start_dist(1, b - 1);
    const int start = start_dist(rng);
    std::vector<int> word(b, -1);
    for (int j = 0; j < r; ++j) word[(start + j) % b] = inside[j];
    int out = 0;
    for (int i = 0; i < b; ++i) if (word[i] < 0) word[i] = outside[out++];
    return make_row(word);
  }

  static bool contains(const std::vector<Target>& row, Target x) {
    return std::binary_search(row.begin(), row.end(), x);
  }

  static int intersection_size(const std::vector<Target>& a,
                               const std::vector<Target>& b) {
    int count = 0;
    auto i = a.begin(), j = b.begin();
    while (i != a.end() && j != b.end()) {
      if (*i < *j) ++i;
      else if (*j < *i) ++j;
      else { ++count; ++i; ++j; }
    }
    return count;
  }

  double k_sample(const std::vector<Target>& h,
                  const std::vector<Target>& g, Target root) const {
    int left = 0, right = 0, common = 0;
    for (Target t : g) {
      if (t == root) continue;
      const bool in_f = contains(base, t);
      const bool in_h = contains(h, t);
      left += in_f;
      right += in_h;
      common += in_f && in_h;
    }
    if (!left || !right) return 0.0;
    const int uni = left + right - common;
    const double wu = std::pow(p, -uni);
    const double wl = std::pow(p, -left);
    const double wr = std::pow(p, -right);
    return contains(g, root) ? (wu - wl - wr + 1.0) / p : (wu - wl - wr);
  }
};

long double factorial_ld(int n) {
  long double out = 1;
  for (int i = 2; i <= n; ++i) out *= i;
  return out;
}

int main(int argc, char** argv) {
  const int r = argc > 1 ? std::stoi(argv[1]) : 3;
  const double p = argc > 2 ? std::stod(argv[2]) : 0.9;
  const std::uint64_t samples = argc > 3 ? std::stoull(argv[3]) : 1000000;
  Model model(r, p, 0xC0FFEEULL + r);
  const long double catalogue = factorial_ld(2 * r + 1);
  const long double degree = 2.0L * r * factorial_ld(r) * factorial_ld(r + 1);
  const long double prefactor = p * catalogue / degree;

  std::cout << std::setprecision(10);
  std::cout << "r " << r << " p " << p << " samples-per-position " << samples << "\n";
  double low = 1e300, high = -1e300;
  for (int position = 1; position <= 2 * r; ++position) {
    const Target root = model.middle_root(position);
    long double denominator = 0.0L, numerator = 0.0L, numerator2 = 0.0L;
    std::uint64_t nonzero = 0;
    for (std::uint64_t sample = 0; sample < samples; ++sample) {
      const auto h = model.uniform_root_row(root);
      const auto g = model.uniform_row();
      const int overlap = Model::intersection_size(model.base, h);
      const long double weight = std::pow(p, -overlap);
      const long double value = model.k_sample(h, g, root);
      denominator += weight;
      numerator += weight * value;
      numerator2 += weight * value * value;
      nonzero += value != 0.0;
    }
    const double normalized = static_cast<double>(prefactor * numerator / denominator);
    low = std::min(low, normalized);
    high = std::max(high, normalized);
    const long double mean = numerator / samples;
    const long double variance = std::max(0.0L, numerator2 / samples - mean * mean);
    const long double standard_error = prefactor * std::sqrt(variance / samples)
                                      / (denominator / samples);
    std::cout << "position " << position << " q0a/z " << normalized
              << " naive-se " << static_cast<double>(standard_error)
              << " nonzero " << nonzero << "\n";
  }
  std::cout << "observed-osc " << high - low << "\n";
}
