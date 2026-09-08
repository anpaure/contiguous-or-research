#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>

struct Ribbon {
  uint16_t x, y;
  uint32_t sx, sy;
  bool operator==(const Ribbon& o) const {
    return x == o.x && y == o.y && sx == o.sx && sy == o.sy;
  }
};

template<int B, int H>
Ribbon ribbon_at(const std::array<int, B>& q, int start) {
  constexpr int r = (B - 1) / 2;
  auto flag = [&](int s) {
    uint16_t m = 0;
    for (int j = 0; j < r; ++j) m |= uint16_t(1u << q[(s + j) % B]);
    uint32_t suffix = 0;
    for (int j = r - H; j < r; ++j) suffix = (suffix << 4) | q[(s + j) % B];
    return std::pair<uint16_t, uint32_t>{m, suffix};
  };
  auto a = flag(start), b = flag((start + r) % B);
  if (b.first < a.first) std::swap(a, b);
  return {a.first, b.first, a.second, b.second};
}

template<int H>
void audit_h() {
  constexpr int B = 11;
  constexpr int r = 5;
  std::array<int, B> q{};
  for (int i = 0; i < B; ++i) q[i] = i;
  std::array<Ribbon, r> canonical{};
  for (int k = 1; k <= r; ++k) canonical[k - 1] = ribbon_at<B, H>(q, k);

  std::array<uint64_t, 1 << r> count{};
  uint64_t configurations = 0;
  do {
    unsigned hit = 0;
    for (int k = 1; k <= r; ++k) {
      Ribbon rib = ribbon_at<B, H>(q, k);
      for (int j = 0; j < r; ++j) {
        if (rib == canonical[j]) hit |= 1u << j;
      }
    }
    for (unsigned sub = hit; sub; sub = (sub - 1) & hit) {
      if (__builtin_popcount(sub) >= 2) ++count[sub];
    }
    ++configurations;
  } while (std::next_permutation(q.begin(), q.end()));
  assert(configurations == 39916800ULL);

  for (int t = 2; t <= r - H + 1; ++t) {
    uint64_t got = 0;
    for (unsigned sub = 0; sub < (1u << r); ++sub)
      if (__builtin_popcount(sub) == t) got = std::max(got, count[sub]);
    int free = r - H - t + 1;
    uint64_t fact = 1;
    for (int j = 2; j <= free; ++j) fact *= j;
    uint64_t expected = uint64_t(r - t + 1) * fact * fact;
    assert(got == expected);
    std::cout << "H=" << H << " t=" << t << " max=" << got << "\n";
  }
}

int main() {
  audit_h<1>();
  audit_h<2>();
  audit_h<3>();
  audit_h<4>();
  std::cout << "PASS audit_multidepth_ribbon_max_b11_20260821\n";
}
