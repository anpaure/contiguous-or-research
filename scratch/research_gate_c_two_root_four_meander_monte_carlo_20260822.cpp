#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

static bool forward(const std::vector<int>& x) {
  int h = 0;
  for (int s : x) if ((h += s) < 0) return false;
  return true;
}

static bool backward(std::vector<int> x) {
  std::reverse(x.begin(), x.end());
  return forward(x);
}

static bool good(const std::vector<int>& sigma, int a) {
  const int k = sigma.size();
  int h = 0, lo = k, hi = -k;
  for (int u = 1; u < k; ++u) {
    const int r = (sigma[(a + u) % k] - sigma[a] + k) % k;
    h += ((r - u) & 1) ? -1 : 1;
    lo = std::min(lo, h);
    hi = std::max(hi, h);
  }
  return lo >= 0 && hi <= h;
}

int main(int argc, char** argv) {
  int k = argc > 1 ? std::stoi(argv[1]) : 101;
  int u = argc > 2 ? std::stoi(argv[2]) : k / 2;
  int d = argc > 3 ? std::stoi(argv[3]) : k / 2;
  int samples = argc > 4 ? std::stoi(argv[4]) : 1000000;
  std::mt19937_64 rng(20260822ULL + k * 10000 + u * 100 + d);
  std::vector<int> values, positions;
  for (int x = 1; x < k; ++x) {
    if (x != u) values.push_back(x);
    if (x != d) positions.push_back(x);
  }
  long long exact = 0, four = 0, root0 = 0;
  std::vector<int> sigma(k), si, ti, sj, tj;
  sigma[0] = 0;
  sigma[u] = d;
  for (int iteration = 0; iteration < samples; ++iteration) {
    std::shuffle(positions.begin(), positions.end(), rng);
    for (int i = 0; i < (int)values.size(); ++i)
      sigma[values[i]] = positions[i];
    const bool g0 = good(sigma, 0);
    const bool gu = good(sigma, u);
    root0 += g0;
    exact += g0 && gu;
    si.clear(); ti.clear(); sj.clear(); tj.clear();
    for (int v = 1; v < u; ++v) {
      int s = ((v + sigma[v]) & 1) ? -1 : 1;
      int t = ((((v-u+k)%k) + ((sigma[v]-d+k)%k)) & 1) ? -1 : 1;
      si.push_back(s); ti.push_back(t);
    }
    for (int v = u + 1; v < k; ++v) {
      int s = ((v + sigma[v]) & 1) ? -1 : 1;
      int t = ((((v-u+k)%k) + ((sigma[v]-d+k)%k)) & 1) ? -1 : 1;
      sj.push_back(s); tj.push_back(t);
    }
    four += forward(si) && backward(ti) && forward(tj) && backward(sj);
  }
  const double scale = std::sqrt(1.0*u*(k-u)*d*(k-d));
  std::cout << "K=" << k << " u=" << u << " d=" << d
            << " root0=" << (double)root0/samples
            << " exact=" << (double)exact/samples
            << " exact_scaled=" << (double)exact/samples*scale
            << " four=" << (double)four/samples
            << " four_scaled=" << (double)four/samples*scale << '\n';
}
