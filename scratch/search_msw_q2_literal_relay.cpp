#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using U32 = std::uint32_t;
using U64 = std::uint64_t;

struct Hex {
  U32 core{};
  std::array<int, 3> a{};
  std::array<std::pair<U32, int>, 6> incidences{};
};

static int pc(U32 x) { return std::popcount(x); }

static bool dyck(U32 x, int m) {
  int h = 0;
  for (int i = 0; i < 2 * m; ++i) {
    h += ((x >> i) & 1U) ? 1 : -1;
    if (h < 0) return false;
  }
  return h == 0;
}

static std::pair<U32, int> g(U32 x, int m) {
  std::vector<int> before(2 * m);
  int h = 0, d0 = 0;
  for (int i = 0; i < 2 * m; ++i) {
    before[i] = h;
    if (!((x >> i) & 1U) && h == 0) ++d0;
    h += ((x >> i) & 1U) ? 1 : -1;
  }
  int ord = 0;
  for (int i = 0; i < 2 * m; ++i) {
    if (!((x >> i) & 1U) && (before[i] == 0 || before[i] == 1) &&
        ++ord == d0 + 1)
      return {x | (U32{1} << i), i};
  }
  std::abort();
}

static std::pair<U32, int> hmap(U32 y, int m) {
  std::vector<int> before(2 * m);
  int h = 0, u1 = 0;
  for (int i = 0; i < 2 * m; ++i) {
    before[i] = h;
    if (((y >> i) & 1U) && h == 1) ++u1;
    h += ((y >> i) & 1U) ? 1 : -1;
  }
  int ord = 0;
  for (int i = 0; i < 2 * m; ++i) {
    if (((y >> i) & 1U) && (before[i] == 0 || before[i] == 1) &&
        ++ord == u1)
      return {y & ~(U32{1} << i), i};
  }
  std::abort();
}

static U64 edge_key(U32 owner, int added) {
  return (U64(owner) << 6) | U64(added);
}

static std::string word(U32 x, int n) {
  std::string s;
  for (int i = 0; i < n; ++i) s += ((x >> i) & 1U) ? '1' : '0';
  return s;
}

static U32 parse_word(const std::string &s) {
  U32 x = 0;
  for (int i = 0; i < int(s.size()); ++i)
    if (s[i] == '1') x |= U32{1} << i;
  return x;
}

struct Factor {
  int m{}, n{};
  std::unordered_set<U64> selected;
  std::unordered_map<U32, int> q2;
  std::vector<U32> cores;

  explicit Factor(int mm) : m(mm), n(2 * mm) {
    const U32 lim = U32{1} << n;
    selected.reserve(4 * (1U << (n - 2)));
    q2.reserve(1U << (n - 2));
    for (U32 root = 0; root < lim; ++root) {
      if (pc(root) != m || !dyck(root, m)) continue;
      U32 x = root;
      std::vector<U32> colors;
      std::vector<U32> owners{x};
      for (int i = 0; i < m; ++i) {
        auto [y, a] = g(x, m);
        auto [nx, b] = hmap(y, m);
        (void)a;
        (void)b;
        colors.push_back(y);
        owners.push_back(nx);
        selected.insert(edge_key(x, std::countr_zero(y ^ x)));
        selected.insert(edge_key(nx, std::countr_zero(y ^ nx)));
        x = nx;
      }
      for (int j = 1; j < m; ++j) ++q2[colors[j - 1] | colors[j]];
    }
    for (U32 k = 0; k < lim; ++k)
      if (pc(k) == m - 1) cores.push_back(k);
  }
};

struct State {
  const Factor *f{};
  std::unordered_set<U64> flipped;
  std::unordered_map<U32, int> qdelta;

  bool status(U32 owner, int added) const {
    U64 k = edge_key(owner, added);
    return f->selected.contains(k) ^ flipped.contains(k);
  }

  int qcount(U32 t) const {
    int z = 0;
    if (auto it = f->q2.find(t); it != f->q2.end()) z += it->second;
    if (auto it = qdelta.find(t); it != qdelta.end()) z += it->second;
    return z;
  }
};

static Hex make_hex(U32 k, int a, int b, int c) {
  Hex h;
  h.core = k;
  h.a = {a, b, c};
  U32 oa = k | (U32{1} << a);
  U32 ob = k | (U32{1} << b);
  U32 oc = k | (U32{1} << c);
  // Oa-Qab-Ob-Qbc-Oc-Qca-Oa.
  h.incidences = {{{oa, b}, {ob, a}, {ob, c},
                   {oc, b}, {oc, a}, {oa, c}}};
  return h;
}

static bool alternating(const State &s, const Hex &h) {
  bool first = s.status(h.incidences[0].first, h.incidences[0].second);
  for (int i = 1; i < 6; ++i)
    if (s.status(h.incidences[i].first, h.incidences[i].second) !=
        (first ^ bool(i & 1)))
      return false;
  return true;
}

static std::map<U32, int> hex_qdelta(const State &s, const Hex &h) {
  std::map<U32, int> d;
  std::array<U32, 3> owners{
      h.core | (U32{1} << h.a[0]), h.core | (U32{1} << h.a[1]),
      h.core | (U32{1} << h.a[2])};
  for (U32 o : owners) {
    std::vector<int> oldbits, newbits;
    for (int b = 0; b < s.f->n; ++b) {
      if ((o >> b) & 1U) continue;
      bool z = s.status(o, b);
      bool toggled_here = false;
      for (auto [ho, hb] : h.incidences)
        if (ho == o && hb == b) toggled_here = true;
      if (z) oldbits.push_back(b);
      if (z ^ toggled_here) newbits.push_back(b);
    }
    if (oldbits.size() != newbits.size() || oldbits.size() > 2) {
      std::cerr << "degree failure owner=" << word(o, s.f->n) << '\n';
      std::abort();
    }
    if (oldbits.size() == 2) {
      U32 oldt = o | (U32{1} << oldbits[0]) | (U32{1} << oldbits[1]);
      U32 newt = o | (U32{1} << newbits[0]) | (U32{1} << newbits[1]);
      --d[oldt];
      ++d[newt];
    }
  }
  for (auto it = d.begin(); it != d.end();)
    if (it->second == 0)
      it = d.erase(it);
    else
      ++it;
  return d;
}

static void apply(State &s, const Hex &h, const std::map<U32, int> &d) {
  for (auto [o, b] : h.incidences) {
    U64 k = edge_key(o, b);
    if (!s.flipped.erase(k)) s.flipped.insert(k);
  }
  for (auto [t, z] : d) {
    s.qdelta[t] += z;
    if (!s.qdelta[t]) s.qdelta.erase(t);
  }
}

static bool final_safe(const State &s) {
  for (auto [t, d] : s.qdelta) {
    int base = 0;
    if (auto it = s.f->q2.find(t); it != s.f->q2.end()) base = it->second;
    if (base > 0 && base + d <= 0) return false;
  }
  return true;
}

static std::vector<Hex> enumerate_alternating(const State &s) {
  std::vector<Hex> out;
  for (U32 k : s.f->cores) {
    std::vector<int> outside;
    for (int a = 0; a < s.f->n; ++a)
      if (!((k >> a) & 1U)) outside.push_back(a);
    for (int i = 0; i < int(outside.size()); ++i)
      for (int j = i + 1; j < int(outside.size()); ++j)
        for (int l = j + 1; l < int(outside.size()); ++l) {
          Hex h = make_hex(k, outside[i], outside[j], outside[l]);
          if (alternating(s, h)) out.push_back(h);
        }
  }
  return out;
}

static void print_delta(const State &s, const std::map<U32, int> &d) {
  std::cout << " delta";
  for (auto [t, z] : d)
    std::cout << ' ' << (z > 0 ? "+" : "") << z << ':'
              << word(t, s.f->n) << "(base="
              << (s.f->q2.contains(t) ? s.f->q2.at(t) : 0) << ')';
  std::cout << '\n';
}

static void print_hex(const State &s, const Hex &h, int label) {
  std::cout << "H" << label << " core=" << word(h.core, s.f->n)
            << " active=" << h.a[0] + 1 << ',' << h.a[1] + 1 << ','
            << h.a[2] + 1 << '\n';
  print_delta(s, hex_qdelta(s, h));
}

int main(int argc, char **argv) {
  if (argc < 3) {
    std::cerr << "usage: search_msw_q2_literal_relay m target_word [max_h1]\n";
    return 2;
  }
  int m = std::stoi(argv[1]);
  std::string target_word = argv[2];
  int max_h1 = argc > 3 ? std::stoi(argv[3]) : 1000000;
  if (int(target_word.size()) != 2 * m) return 2;
  U32 target = parse_word(target_word);
  Factor f(m);
  State initial{&f};
  std::cout << "m=" << m << " target=" << target_word
            << " target_base=" << initial.qcount(target)
            << " selected_incidences=" << f.selected.size()
            << " q2_distinct=" << f.q2.size() << '\n';
  auto hs = enumerate_alternating(initial);
  std::cout << "initial_alternating_hexes=" << hs.size() << '\n';
  int creators = 0, safe_single = 0, attempted = 0;
  for (const Hex &h1 : hs) {
    auto d1 = hex_qdelta(initial, h1);
    auto it_target = d1.find(target);
    if (it_target == d1.end() || it_target->second <= 0) continue;
    ++creators;
    State s1 = initial;
    apply(s1, h1, d1);
    if (s1.qcount(target) > 0 && final_safe(s1)) {
      ++safe_single;
      std::cout << "SOLUTION length=1\n";
      print_hex(initial, h1, 1);
      if (safe_single >= 10) break;
    }
    if (++attempted > max_h1) break;
    auto h2s = enumerate_alternating(s1);
    for (const Hex &h2 : h2s) {
      auto d2 = hex_qdelta(s1, h2);
      State s2 = s1;
      apply(s2, h2, d2);
      if (s2.qcount(target) > 0 && final_safe(s2)) {
        std::cout << "SOLUTION length=2 h2_count=" << h2s.size() << '\n';
        print_hex(initial, h1, 1);
        print_hex(s1, h2, 2);
        std::cout << " final_delta";
        for (auto [t, z] : s2.qdelta)
          std::cout << ' ' << (z > 0 ? "+" : "") << z << ':'
                    << word(t, f.n) << "(base="
                    << (f.q2.contains(t) ? f.q2.at(t) : 0) << ')';
        std::cout << '\n';
        return 0;
      }
    }
  }
  std::cout << "creators=" << creators << " safe_single=" << safe_single
            << " attempted=" << attempted << " no_length2_solution\n";
  return 1;
}
