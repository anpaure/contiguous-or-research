#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>

using u64 = std::uint64_t;

int main(int argc, char** argv) {
  const int r = 3;
  const int b = 7;
  const double p = argc > 1 ? std::stod(argv[1]) : 0.75;

  std::vector<u64> middle;
  std::vector<u64> lower;
  for (u64 mask = 0; mask < (1ULL << b); ++mask) {
    if (__builtin_popcountll(mask) == r) middle.push_back(mask);
    if (__builtin_popcountll(mask) == r - 1) lower.push_back(mask);
  }
  std::map<std::pair<char, u64>, int> target_id;
  for (u64 mask : middle) target_id[{'M', mask}] = target_id.size();
  for (u64 mask : lower) target_id[{'L', mask}] = target_id.size();

  std::array<int, b> word{};
  std::iota(word.begin(), word.end(), 0);
  std::set<u64> row_set;
  std::map<u64, std::array<int, b>> row_word;
  do {
    u64 row = 0;
    for (int start = 1; start < b; ++start) {
      u64 mm = 0, lm = 0;
      for (int j = 0; j < r; ++j) mm |= 1ULL << word[(start + j) % b];
      for (int j = 0; j < r - 1; ++j) lm |= 1ULL << word[(start + j) % b];
      row |= 1ULL << target_id[{'M', mm}];
      row |= 1ULL << target_id[{'L', lm}];
    }
    row_set.insert(row);
    row_word[row] = word;
  } while (std::next_permutation(word.begin(), word.end()));

  std::vector<u64> rows(row_set.begin(), row_set.end());
  if (rows.size() != 5040 || target_id.size() != 56) return 2;
  std::map<u64, int> row_index;
  for (int i = 0; i < static_cast<int>(rows.size()); ++i) row_index[rows[i]] = i;

  std::array<int, b> identity{};
  std::iota(identity.begin(), identity.end(), 0);
  u64 base = 0;
  std::array<int, 6> roots{};
  for (int start = 1; start < b; ++start) {
    u64 mm = 0, lm = 0;
    for (int j = 0; j < r; ++j) mm |= 1ULL << identity[(start + j) % b];
    for (int j = 0; j < r - 1; ++j) lm |= 1ULL << identity[(start + j) % b];
    roots[start - 1] = target_id[{'M', mm}];
    base |= 1ULL << roots[start - 1];
    base |= 1ULL << target_id[{'L', lm}];
  }
  if (!row_index.count(base)) return 3;

  std::vector<double> pinv_pow(13, 1.0);
  for (int i = 1; i <= 12; ++i) pinv_pow[i] = pinv_pow[i - 1] / p;
  const double q0 = std::pow(p, 12);
  const double z = 864.0 * q0 / p;

  std::cout << std::setprecision(12);
  std::cout << "p " << p << " q0 " << q0 << " z " << z << "\n";
  double min_profile = 1e300, max_profile = -1e300;
  for (int pos = 0; pos < 6; ++pos) {
    const u64 root_bit = 1ULL << roots[pos];
    std::vector<u64> star;
    for (u64 row : rows) if (row & root_bit) star.push_back(row);
    if (star.size() != 864) return 4;

    long double denom = 0.0L;
    long double numer = 0.0L;
    for (u64 h : star) {
      if (h == base) continue;
      const int union_size = __builtin_popcountll(base | h);
      const long double qfh = std::pow(p, union_size);
      denom += qfh;
      long double kval = 0.0L;
      for (u64 g : rows) {
        const u64 left = (g & base) & ~root_bit;
        const u64 right = (g & h) & ~root_bit;
        if (!left || !right) continue;
        const int lu = __builtin_popcountll(left | right);
        const int la = __builtin_popcountll(left);
        const int lb = __builtin_popcountll(right);
        if (g & root_bit) {
          kval += (pinv_pow[lu] - pinv_pow[la] - pinv_pow[lb] + 1.0) / p;
        } else {
          kval += pinv_pow[lu] - pinv_pow[la] - pinv_pow[lb];
        }
      }
      numer += qfh * kval;
    }
    const double profile = static_cast<double>(numer / denom);
    min_profile = std::min(min_profile, profile);
    max_profile = std::max(max_profile, profile);
    std::cout << "position " << pos + 1 << " a " << profile
              << " q0a/z " << q0 * profile / z << "\n";
  }
  std::cout << "osc " << max_profile - min_profile
            << " q0osc/z " << q0 * (max_profile - min_profile) / z << "\n";
}
