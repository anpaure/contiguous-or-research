#include <algorithm>
#include <bit>
#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

// Target-local enumeration of canonical MSW alternating incidence cycles.
// It uses the exact touching-step rule and therefore does not materialize
// the Catalan factor.  Heavy runs belong on h100 only.

using U = std::uint64_t;

static int pc(U x) { return std::popcount(x); }

static std::string word(U x, int n) {
  std::string s;
  for (int i = 0; i < n; ++i) s += ((x >> i) & 1U) ? '1' : '0';
  return s;
}

static U parse_word(const std::string &s) {
  U x = 0;
  for (int i = 0; i < int(s.size()); ++i)
    if (s[i] == '1') x |= U{1} << i;
  return x;
}

static std::vector<U> selected_colours(U owner, int n) {
  std::vector<int> before(n);
  int h = 0, d0 = 0;
  for (int i = 0; i < n; ++i) {
    before[i] = h;
    if (!((owner >> i) & 1U) && h == 0) ++d0;
    h += ((owner >> i) & 1U) ? 1 : -1;
  }
  std::vector<U> out;
  int ord = 0;
  for (int i = 0; i < n; ++i) {
    if (!((owner >> i) & 1U) && (before[i] == 0 || before[i] == 1)) {
      ++ord;
      if ((d0 > 0 && ord == d0) || ord == d0 + 1)
        out.push_back(owner | (U{1} << i));
    }
  }
  return out;
}

static bool selected(U owner, U colour, int n) {
  auto cs = selected_colours(owner, n);
  return std::find(cs.begin(), cs.end(), colour) != cs.end();
}

static std::vector<U> selected_owners(U colour, int n) {
  std::vector<U> out;
  U bits = colour;
  while (bits) {
    int y = std::countr_zero(bits);
    bits &= bits - 1;
    U owner = colour & ~(U{1} << y);
    if (selected(owner, colour, n)) out.push_back(owner);
  }
  return out;
}

static int q2_load(U target, int n) {
  std::vector<int> before(n);
  int h = 0;
  for (int i = 0; i < n; ++i) {
    before[i] = h;
    h += ((target >> i) & 1U) ? 1 : -1;
  }
  int ans = 0;
  for (int p = 0; p < n; ++p) {
    if (!((target >> p) & 1U) || (before[p] != 0 && before[p] != 1))
      continue;
    int left = 0;
    for (int i = 0; i < p; ++i)
      if (((target >> i) & 1U) && before[i] == 0) ++left;
    for (int q = p + 1; q < n; ++q) {
      if (!((target >> q) & 1U) || (before[q] != 2 && before[q] != 3))
        continue;
      bool barrier = false;
      for (int i = p + 1; i < q; ++i)
        if (!((target >> i) & 1U) && (before[i] == 2 || before[i] == 3))
          barrier = true;
      if (barrier) continue;
      int right = 0;
      for (int i = q + 1; i < n; ++i)
        if (((target >> i) & 1U) && before[i] == 3) ++right;
      if (left != right) continue;
      U pred = target & ~(U{1} << p) & ~(U{1} << q);
      int z = 0, mn = 0, mx = 0;
      for (int i = 0; i < n; ++i) {
        z += ((pred >> i) & 1U) ? 1 : -1;
        mn = std::min(mn, z);
        mx = std::max(mx, z);
      }
      if (mn >= 0 || mx <= 0) continue;
      ++ans;
    }
  }
  return ans;
}

struct Cycle {
  std::vector<U> owners;
  std::vector<U> outgoing;
  std::vector<std::pair<U, int>> delta;
  bool safe{};
};

int main(int argc, char **argv) {
  if (argc < 2) {
    std::cerr << "usage: search_msw_target_local_cycles target_word [max_C]\n";
    return 2;
  }
  std::string sw = argv[1];
  int n = sw.size(), r = n / 2;
  int max_c = argc > 2 ? std::stoi(argv[2]) : 20;
  std::string prefix_filter = argc > 3 ? argv[3] : "";
  if (n % 2 || n >= 63) return 2;
  U target = parse_word(sw);
  std::unordered_map<U, int> load_cache;
  auto load = [&](U t) {
    auto it = load_cache.find(t);
    if (it != load_cache.end()) return it->second;
    int z = q2_load(t, n);
    load_cache.emplace(t, z);
    return z;
  };
  std::cout << "r=" << r << " target=" << sw << " load=" << load(target)
            << '\n';

  std::vector<U> tbits;
  for (U z = target; z; z &= z - 1)
    tbits.push_back(U{1} << std::countr_zero(z));

  for (int maxowners = 3; 2 * maxowners <= max_c; ++maxowners) {
    std::vector<Cycle> found;
    std::uint64_t partials = 0;
    for (int ii = 0; ii < int(tbits.size()) && found.size() < 20; ++ii)
      for (int jj = ii + 1; jj < int(tbits.size()) && found.size() < 20;
           ++jj) {
        U o0 = target & ~tbits[ii] & ~tbits[jj];
        auto cs0 = selected_colours(o0, n);
        if (cs0.size() != 2) continue;
        for (int ez = 0; ez < 2 && found.size() < 20; ++ez) {
          U mate = cs0[ez], qminus = cs0[1 - ez];
          if ((mate & target) != mate) continue;
          U qplus = o0 | (target & ~mate);
          if (pc(qplus) != r + 1 || selected(o0, qplus, n)) continue;
          for (U o1 : selected_owners(qplus, n)) {
            if (o1 == o0) continue;
            std::vector<U> os{o0, o1}, qs{qplus};
            std::function<void()> dfs = [&]() {
              ++partials;
              U u = os.back();
              for (int x = 0; x < n && found.size() < 20; ++x) {
                if ((u >> x) & 1U) continue;
                U q = u | (U{1} << x);
                if (selected(u, q, n)) continue;
                auto dest = selected_owners(q, n);
                for (U v : dest) {
                  if (v == o0) {
                    if (q != qminus || os.size() != size_t(maxowners))
                      continue;
                    qs.push_back(q);
                    std::unordered_map<U, int> dm;
                    for (int k = 0; k < int(os.size()); ++k) {
                      U oo = os[k], qin = k ? qs[k - 1] : qminus,
                        qout = qs[k];
                      auto cs = selected_colours(oo, n);
                      if (cs.size() != 2) continue;
                      U other = cs[0] == qin ? cs[1]
                                             : (cs[1] == qin ? cs[0] : 0);
                      if (!other) std::abort();
                      --dm[other | qin];
                      ++dm[other | qout];
                    }
                    std::vector<std::pair<U, int>> dv;
                    bool creates = dm[target] > 0, safe = true;
                    for (auto [t, d] : dm)
                      if (d) {
                        dv.push_back({t, d});
                        if (load(t) + d < 1) safe = false;
                      }
                    std::sort(dv.begin(), dv.end());
                    bool prefix_ok = prefix_filter.empty();
                    if (!prefix_ok) {
                      prefix_ok = true;
                      for (U oo : os)
                        prefix_ok &= word(oo, n).starts_with(prefix_filter);
                      for (U qq : qs)
                        prefix_ok &= word(qq, n).starts_with(prefix_filter);
                    }
                    if (creates && prefix_ok) found.push_back({os, qs, dv, safe});
                    qs.pop_back();
                    continue;
                  }
                  if (os.size() >= size_t(maxowners) ||
                      std::find(os.begin(), os.end(), v) != os.end() ||
                      std::find(qs.begin(), qs.end(), q) != qs.end())
                    continue;
                  os.push_back(v);
                  qs.push_back(q);
                  dfs();
                  qs.pop_back();
                  os.pop_back();
                }
              }
            };
            dfs();
          }
        }
      }
    std::cout << "C" << 2 * maxowners << " creators_sample=" << found.size()
              << " partial_states=" << partials << '\n';
    for (int z = 0; z < std::min<int>(3, found.size()); ++z) {
      auto &c = found[z];
      std::cout << "  safe=" << c.safe << " owners=";
      for (U o : c.owners) std::cout << word(o, n) << ',';
      std::cout << " colours=";
      for (U q : c.outgoing) std::cout << word(q, n) << ',';
      std::cout << " delta=";
      for (auto [t, d] : c.delta)
        std::cout << (d > 0 ? "+" : "") << d << ':' << word(t, n)
                  << "(load=" << load(t) << "),";
      std::cout << '\n';
    }
    if (!found.empty()) break;
  }
}
