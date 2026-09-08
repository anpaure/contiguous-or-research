#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>

static bool good_cut(const std::vector<int>& order,
                     const std::vector<int>& inverse, int position) {
  const int k = static_cast<int>(order.size());
  int height = 0;
  int minimum = k;
  int maximum = -k;
  for (int distance = 1; distance < k; ++distance) {
    int value = order[position] + distance;
    if (value >= k) value -= k;
    int position_distance = inverse[value] - position;
    if (position_distance <= 0) position_distance += k;
    height += ((position_distance - distance) & 1) ? -1 : 1;
    minimum = std::min(minimum, height);
    maximum = std::max(maximum, height);
  }
  return minimum >= 0 && maximum <= height;
}

int main(int argc, char** argv) {
  const int k = argc > 1 ? std::stoi(argv[1]) : 11;
  std::vector<int> tail(k - 1);
  std::iota(tail.begin(), tail.end(), 1);
  std::map<int, std::uint64_t> histogram;
  std::map<int, int> maximum_gap_changes;
  std::map<int, std::vector<int>> example;
  do {
    std::vector<int> order(k);
    order[0] = 0;
    std::copy(tail.begin(), tail.end(), order.begin() + 1);
    std::vector<int> inverse(k);
    for (int i = 0; i < k; ++i) inverse[order[i]] = i;
    int bad = 0;
    for (int i = 0; i < k; ++i) bad += !good_cut(order, inverse, i);
    ++histogram[bad];
    std::vector<int> gaps(k);
    for (int value = 0; value < k; ++value) {
      gaps[value] = inverse[(value + 1) % k] - inverse[value];
      if (gaps[value] <= 0) gaps[value] += k;
    }
    int changes = 0;
    for (int value = 0; value < k; ++value)
      changes += gaps[value] != gaps[(value + k - 1) % k];
    if (!maximum_gap_changes.count(bad) || changes > maximum_gap_changes[bad]) {
      maximum_gap_changes[bad] = changes;
      example[bad] = order;
    }
  } while (std::next_permutation(tail.begin(), tail.end()));

  std::cout << "K=" << k << "\n";
  for (const auto& [bad, count] : histogram) {
    std::cout << "bad=" << bad << " count=" << count
              << " max_gap_changes=" << maximum_gap_changes[bad] << " example=";
    for (int value : example[bad]) std::cout << value << ',';
    std::cout << '\n';
  }
}
