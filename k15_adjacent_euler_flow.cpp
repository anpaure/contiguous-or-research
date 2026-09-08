#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

using std::array;
using std::cerr;
using std::cout;
using std::pair;
using std::runtime_error;
using std::string;
using std::vector;

namespace {

long long choose_int(int n, int r) {
  if (r < 0 || r > n) return 0;
  r = std::min(r, n - r);
  long long ans = 1;
  for (int i = 1; i <= r; ++i) ans = ans * (n - r + i) / i;
  return ans;
}

uint64_t splitmix64(uint64_t x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}

vector<int> parse_integer_array(const string& filename, const string& key) {
  std::ifstream in(filename);
  if (!in) throw runtime_error("cannot open " + filename);
  string text((std::istreambuf_iterator<char>(in)),
              std::istreambuf_iterator<char>());
  const string needle = "\"" + key + "\"";
  size_t p = text.find(needle);
  if (p == string::npos) throw runtime_error("missing key " + key);
  p = text.find('[', p + needle.size());
  if (p == string::npos) throw runtime_error("missing array for " + key);
  vector<int> out;
  int depth = 0;
  for (; p < text.size(); ++p) {
    const char ch = text[p];
    if (ch == '[') {
      ++depth;
      continue;
    }
    if (ch == ']') {
      --depth;
      if (depth == 0) break;
      continue;
    }
    if (depth != 1) continue;
    if (ch == '-' || (ch >= '0' && ch <= '9')) {
      bool neg = false;
      if (text[p] == '-') {
        neg = true;
        ++p;
      }
      int v = 0;
      while (p < text.size() && text[p] >= '0' && text[p] <= '9') {
        v = 10 * v + (text[p] - '0');
        ++p;
      }
      --p;
      out.push_back(neg ? -v : v);
    }
  }
  return out;
}

vector<int> trace_counts(const vector<int>& path, int q, int k) {
  const int lim = 1 << k;
  vector<int> cnt(lim, 0);
  for (int i = 0; i + q < static_cast<int>(path.size()); ++i) {
    int mask = path[i];
    for (int j = 1; j <= q; ++j) mask &= path[i + j];
    ++cnt[mask];
  }
  return cnt;
}

vector<int> point_degree(const vector<int>& counts, int k) {
  vector<int> d(k, 0);
  for (int mask = 0; mask < static_cast<int>(counts.size()); ++mask) {
    if (!counts[mask]) continue;
    for (int x = 0; x < k; ++x)
      if ((mask >> x) & 1) d[x] += counts[mask];
  }
  return d;
}

vector<int> build_excess(int k, int s, int e, vector<int> degree,
                         uint64_t seed) {
  const int lim = 1 << k;
  vector<int> counts(lim, 0);
  if (static_cast<int>(std::accumulate(degree.begin(), degree.end(), 0LL)) !=
      s * e)
    throw runtime_error("bad excess checksum");
  for (int remaining = e; remaining >= 1; --remaining) {
    vector<int> chosen;
    vector<char> used(k, false);
    for (int x = 0; x < k; ++x) {
      if (degree[x] == remaining) {
        chosen.push_back(x);
        used[x] = true;
      }
    }
    if (static_cast<int>(chosen.size()) > s)
      throw runtime_error("too many forced coordinates");
    vector<int> candidates;
    for (int x = 0; x < k; ++x)
      if (!used[x] && degree[x] > 0) candidates.push_back(x);
    std::sort(candidates.begin(), candidates.end(), [&](int a, int b) {
      if (degree[a] != degree[b]) return degree[a] > degree[b];
      return splitmix64(seed ^ (uint64_t(remaining) << 20) ^ uint64_t(a)) <
             splitmix64(seed ^ (uint64_t(remaining) << 20) ^ uint64_t(b));
    });
    for (int x : candidates) {
      if (static_cast<int>(chosen.size()) == s) break;
      chosen.push_back(x);
    }
    if (static_cast<int>(chosen.size()) != s)
      throw runtime_error("not enough positive coordinates");
    int mask = 0;
    for (int x : chosen) {
      mask |= 1 << x;
      if (--degree[x] < 0) throw runtime_error("negative degree");
    }
    ++counts[mask];
  }
  if (std::any_of(degree.begin(), degree.end(), [](int x) { return x != 0; }))
    throw runtime_error("excess construction did not finish");
  return counts;
}

long long square_energy(const vector<int>& counts) {
  long long ans = 0;
  for (int x : counts) ans += 1LL * x * x;
  return ans;
}

bool rebalance_excess(int k, int s, vector<int>& counts, uint64_t seed,
                      long long max_iterations = 20000000) {
  vector<int> occurrences;
  int number_of_types = 0;
  for (int mask = 0; mask < static_cast<int>(counts.size()); ++mask) {
    if (std::popcount(static_cast<unsigned>(mask)) == s) ++number_of_types;
    for (int j = 0; j < counts[mask]; ++j) occurrences.push_back(mask);
  }
  const int e = occurrences.size();
  const int floor_load = e / number_of_types;
  const int remainder = e % number_of_types;
  const long long target_energy =
      1LL * (number_of_types - remainder) * floor_load * floor_load +
      1LL * remainder * (floor_load + 1) * (floor_load + 1);
  long long energy = square_energy(counts);
  uint64_t state = splitmix64(seed);
  for (long long iteration = 0;
       iteration < max_iterations && energy > target_energy; ++iteration) {
    state = splitmix64(state);
    int i = state % e;
    state = splitmix64(state);
    int j = state % e;
    if (i == j) continue;
    int A = occurrences[i], B = occurrences[j];
    int onlyA = A & ~B, onlyB = B & ~A;
    if (!onlyA || !onlyB) continue;
    state = splitmix64(state);
    int ai = state % std::popcount(static_cast<unsigned>(onlyA));
    state = splitmix64(state);
    int bi = state % std::popcount(static_cast<unsigned>(onlyB));
    int abit = 0, bbit = 0;
    for (int x = 0; x < k; ++x) if ((onlyA >> x) & 1) {
      if (ai-- == 0) { abit = 1 << x; break; }
    }
    for (int x = 0; x < k; ++x) if ((onlyB >> x) & 1) {
      if (bi-- == 0) { bbit = 1 << x; break; }
    }
    int C = (A ^ abit) | bbit;
    int D = (B ^ bbit) | abit;
    array<int,4> masks{A,B,C,D};
    std::sort(masks.begin(), masks.end());
    long long before = 0, after = 0;
    for (int z = 0; z < 4;) {
      int w = z + 1;
      while (w < 4 && masks[w] == masks[z]) ++w;
      int mask = masks[z];
      int delta = (mask == C) + (mask == D) - (mask == A) - (mask == B);
      before += 1LL * counts[mask] * counts[mask];
      after += 1LL * (counts[mask] + delta) * (counts[mask] + delta);
      z = w;
    }
    long long change = after - before;
    // Strict descent is primary; rare flat moves avoid contingency-table
    // plateaux without ever worsening the convex objective.
    bool accept = change < 0;
    if (change == 0) {
      state = splitmix64(state);
      accept = (state & 1023ULL) == 0;
    }
    if (!accept) continue;
    --counts[A]; --counts[B]; ++counts[C]; ++counts[D];
    occurrences[i] = C; occurrences[j] = D;
    energy += change;
  }
  return energy == target_energy;
}

vector<int> hole_free_design(int k, int s, int total,
                             const vector<int>& target_point_degree,
                             uint64_t seed) {
  const int lim = 1 << k;
  const int nsets = static_cast<int>(choose_int(k, s));
  const int e = total - nsets;
  if (e < 0) throw runtime_error("negative excess");
  vector<int> gamma(k);
  const int base_degree = static_cast<int>(choose_int(k - 1, s - 1));
  for (int x = 0; x < k; ++x) gamma[x] = target_point_degree[x] - base_degree;
  vector<int> counts(lim, 0);
  for (int mask = 0; mask < lim; ++mask)
    if (std::popcount(static_cast<unsigned>(mask)) == s) counts[mask] = 1;
  const vector<int> excess = build_excess(k, s, e, gamma, seed);
  vector<int> balanced_excess = excess;
  const bool balanced = rebalance_excess(k, s, balanced_excess,
                                         splitmix64(seed ^ 0xba1aULL));
  if (!balanced) cerr << "warning: excess did not reach floor/ceiling loads\n";
  for (int mask = 0; mask < lim; ++mask) counts[mask] += balanced_excess[mask];
  if (std::accumulate(counts.begin(), counts.end(), 0LL) != total)
    throw runtime_error("design size mismatch");
  if (point_degree(counts, k) != target_point_degree)
    throw runtime_error("design degree mismatch");
  return counts;
}

struct Dinic {
  struct Edge {
    int to, rev, cap, original;
  };
  int n;
  vector<vector<Edge>> g;
  vector<int> level, it;
  explicit Dinic(int n_) : n(n_), g(n_), level(n_), it(n_) {}
  int add_edge(int u, int v, int cap) {
    int idx = static_cast<int>(g[u].size());
    Edge a{v, static_cast<int>(g[v].size()), cap, cap};
    Edge b{u, idx, 0, 0};
    g[u].push_back(a);
    g[v].push_back(b);
    return idx;
  }
  bool bfs(int s, int t) {
    std::fill(level.begin(), level.end(), -1);
    std::queue<int> q;
    level[s] = 0;
    q.push(s);
    while (!q.empty()) {
      int u = q.front(); q.pop();
      for (const auto& e : g[u]) if (e.cap && level[e.to] < 0) {
        level[e.to] = level[u] + 1;
        q.push(e.to);
      }
    }
    return level[t] >= 0;
  }
  int dfs(int u, int t, int f) {
    if (u == t) return f;
    for (int& i = it[u]; i < static_cast<int>(g[u].size()); ++i) {
      Edge& e = g[u][i];
      if (!e.cap || level[e.to] != level[u] + 1) continue;
      int z = dfs(e.to, t, std::min(f, e.cap));
      if (!z) continue;
      e.cap -= z;
      g[e.to][e.rev].cap += z;
      return z;
    }
    return 0;
  }
  long long maxflow(int s, int t) {
    long long ans = 0;
    while (bfs(s, t)) {
      std::fill(it.begin(), it.end(), 0);
      while (int f = dfs(s, t, std::numeric_limits<int>::max())) ans += f;
    }
    return ans;
  }
  vector<char> reachable(int s) const {
    vector<char> seen(n, false);
    std::queue<int> q;
    seen[s] = true; q.push(s);
    while (!q.empty()) {
      int u = q.front(); q.pop();
      for (const auto& e : g[u]) if (e.cap && !seen[e.to]) {
        seen[e.to] = true; q.push(e.to);
      }
    }
    return seen;
  }
};

struct DSU {
  vector<int> p, sz;
  explicit DSU(int n) : p(n), sz(n, 1) { std::iota(p.begin(), p.end(), 0); }
  int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
  void unite(int a, int b) {
    a = find(a); b = find(b); if (a == b) return;
    if (sz[a] < sz[b]) std::swap(a, b);
    p[b] = a; sz[a] += sz[b];
  }
};

struct SelectedEdge { int a, b, color; };

int component_count(int na, const vector<int>& upper_masks,
                    const vector<int>& upper_counts,
                    const vector<SelectedEdge>& edges,
                    vector<int>* roots = nullptr) {
  DSU dsu(na);
  for (const auto& e : edges) dsu.unite(e.a, e.b);
  int comps = 0;
  for (int ai = 0; ai < na; ++ai)
    if (upper_counts[upper_masks[ai]] && dsu.find(ai) == ai) ++comps;
  if (roots) {
    roots->resize(na);
    for (int ai = 0; ai < na; ++ai) (*roots)[ai] = dsu.find(ai);
  }
  return comps;
}

int merge_same_colour_components(int na, const vector<int>& upper_masks,
                                 const vector<int>& upper_counts,
                                 vector<SelectedEdge>& edges,
                                 int number_of_colours) {
  while (true) {
    vector<int> roots;
    int before = component_count(na, upper_masks, upper_counts, edges, &roots);
    if (before <= 1) return before;
    vector<int> first(number_of_colours, -1);
    bool changed = false;
    for (int j = 0; j < static_cast<int>(edges.size()) && !changed; ++j) {
      const int color = edges[j].color;
      int i = first[color];
      if (i < 0) {
        first[color] = j;
        continue;
      }
      if (roots[edges[i].a] == roots[edges[j].a]) continue;
      const SelectedEdge old_i = edges[i], old_j = edges[j];
      // Cutting an edge in each of two Euler components and crossing the
      // four half-edges preserves degrees and colour and normally joins the
      // two components.  Test both cross pairings and keep a strict merge.
      edges[i] = {old_i.a, old_j.a, color};
      edges[j] = {old_i.b, old_j.b, color};
      int after = component_count(na, upper_masks, upper_counts, edges);
      if (after >= before) {
        edges[i] = {old_i.a, old_j.b, color};
        edges[j] = {old_i.b, old_j.a, color};
        after = component_count(na, upper_masks, upper_counts, edges);
      }
      if (after < before) {
        changed = true;
      } else {
        edges[i] = old_i;
        edges[j] = old_j;
      }
    }
    if (!changed) return before;
  }
}

struct FlowResult {
  bool flow_feasible = false;
  bool connected = false;
  int components = -1;
  uint64_t trail_hash = 0;
  long long value = 0, required = 0;
  vector<vector<pair<int,int>>> half; // per color: (upper index, load)
  vector<int> lower_masks, upper_masks;
  vector<int> trail_masks;
};

struct IncEntry { int r, a, cap, h; };

int half_support_components(int nr, int na, const vector<IncEntry>& entries,
                            vector<int>* roots = nullptr) {
  DSU dsu(nr + na);
  for (const auto& e : entries) if (e.h > 0) dsu.unite(e.r, nr + e.a);
  int comps = 0;
  for (int v = 0; v < nr + na; ++v) if (dsu.find(v) == v) ++comps;
  if (roots) {
    roots->resize(nr + na);
    for (int v = 0; v < nr + na; ++v) (*roots)[v] = dsu.find(v);
  }
  return comps;
}

bool connect_half_support(int nr, int na, vector<IncEntry>& entries,
                          uint64_t seed, int max_steps = 4096) {
  const int n = nr + na;
  for (int step = 0; step < max_steps; ++step) {
    vector<int> roots;
    int before = half_support_components(nr, na, entries, &roots);
    if (before == 1) return true;

    vector<vector<pair<int,int>>> g(n), rg(n);
    for (int id = 0; id < static_cast<int>(entries.size()); ++id) {
      const auto& e = entries[id];
      int u = e.r, v = nr + e.a;
      if (e.h < e.cap) { g[u].push_back({v,id}); rg[v].push_back({u,id}); }
      if (e.h > 0)     { g[v].push_back({u,id}); rg[u].push_back({v,id}); }
    }

    vector<char> seen(n,false);
    vector<int> order; order.reserve(n);
    for (int start = 0; start < n; ++start) if (!seen[start]) {
      vector<pair<int,int>> st{{start,0}}; seen[start] = true;
      while (!st.empty()) {
        int u = st.back().first;
        int& at = st.back().second;
        if (at < static_cast<int>(g[u].size())) {
          int v = g[u][at++].first;
          if (!seen[v]) { seen[v] = true; st.push_back({v,0}); }
        } else {
          order.push_back(u); st.pop_back();
        }
      }
    }
    vector<int> scc(n,-1);
    int scc_count = 0;
    for (int oi = n - 1; oi >= 0; --oi) {
      int start = order[oi];
      if (scc[start] >= 0) continue;
      vector<int> st{start}; scc[start] = scc_count;
      while (!st.empty()) {
        int u = st.back(); st.pop_back();
        for (auto [v,id] : rg[u]) {
          (void)id;
          if (scc[v] < 0) { scc[v] = scc_count; st.push_back(v); }
        }
      }
      ++scc_count;
    }

    vector<int> candidates;
    for (int id = 0; id < static_cast<int>(entries.size()); ++id) {
      const auto& e = entries[id];
      int u = e.r, v = nr + e.a;
      if (e.h < e.cap && roots[u] != roots[v] && scc[u] == scc[v])
        candidates.push_back(id);
    }
    std::sort(candidates.begin(), candidates.end(), [&](int a, int b) {
      return splitmix64(seed ^ (uint64_t(step) << 32) ^ uint64_t(a)) <
             splitmix64(seed ^ (uint64_t(step) << 32) ^ uint64_t(b));
    });
    bool improved = false;
    const int trials = std::min<int>(256, candidates.size());
    for (int ci = 0; ci < trials && !improved; ++ci) {
      int add_id = candidates[ci];
      int target = entries[add_id].r;
      int start = nr + entries[add_id].a;
      vector<int> parent_node(n,-1), parent_edge(n,-1);
      std::queue<int> q;
      parent_node[start] = start; q.push(start);
      while (!q.empty() && parent_node[target] < 0) {
        int u = q.front(); q.pop();
        for (auto [v,id] : g[u]) {
          if (parent_node[v] >= 0) continue;
          parent_node[v] = u; parent_edge[v] = id; q.push(v);
          if (v == target) break;
        }
      }
      if (parent_node[target] < 0) continue;
      vector<pair<int,int>> changes; // (entry, signed change)
      changes.push_back({add_id,+1});
      int cur = target;
      vector<pair<int,int>> reverse_path;
      while (cur != start) {
        int prev = parent_node[cur], id = parent_edge[cur];
        // BFS path direction is prev -> cur.
        int delta = (prev < nr) ? +1 : -1;
        reverse_path.push_back({id,delta});
        cur = prev;
      }
      changes.insert(changes.end(), reverse_path.begin(), reverse_path.end());
      for (auto [id,delta] : changes) entries[id].h += delta;
      int after = half_support_components(nr, na, entries);
      if (after < before) {
        improved = true;
      } else {
        for (auto [id,delta] : changes) entries[id].h -= delta;
      }
    }
    if (!improved) return false;
  }
  return half_support_components(nr, na, entries) == 1;
}

FlowResult adjacent_flow(int k, const vector<int>& upper_counts,
                         const vector<int>& lower_counts,
                         int endpoint_left, int endpoint_right,
                         uint64_t pairing_seed) {
  FlowResult out;
  const int lim = 1 << k;
  vector<int> upper_idx(lim, -1), lower_idx(lim, -1);
  for (int mask = 0; mask < lim; ++mask) {
    if (upper_counts[mask] > 0) {
      upper_idx[mask] = static_cast<int>(out.upper_masks.size());
      out.upper_masks.push_back(mask);
    }
    if (lower_counts[mask] > 0) {
      lower_idx[mask] = static_cast<int>(out.lower_masks.size());
      out.lower_masks.push_back(mask);
    }
  }
  const int nr = out.lower_masks.size(), na = out.upper_masks.size();
  const int source = 0, rbase = 1, abase = rbase + nr, sink = abase + na;
  Dinic din(sink + 1);
  struct Ref { int ri, ai, node, edge_index; };
  vector<Ref> refs;
  long long total_left = 0, total_right = 0;
  for (int ri = 0; ri < nr; ++ri) {
    int R = out.lower_masks[ri], c = lower_counts[R];
    din.add_edge(source, rbase + ri, 2 * c);
    total_left += 2 * c;
    int outside = ((1 << k) - 1) ^ R;
    for (int x = 0; x < k; ++x) if ((outside >> x) & 1) {
      int A = R | (1 << x);
      int ai = upper_idx[A];
      if (ai < 0) continue;
      int ei = din.add_edge(rbase + ri, abase + ai, c);
      refs.push_back({ri, ai, rbase + ri, ei});
    }
  }
  for (int ai = 0; ai < na; ++ai) {
    int A = out.upper_masks[ai];
    int ends = (A == endpoint_left) + (A == endpoint_right);
    int demand = 2 * upper_counts[A] - ends;
    if (demand < 0) throw runtime_error("negative upper demand");
    din.add_edge(abase + ai, sink, demand);
    total_right += demand;
  }
  if (total_left != total_right) throw runtime_error("flow totals disagree");
  out.required = total_left;
  out.value = din.maxflow(source, sink);
  if (out.value != out.required) {
    auto seen = din.reachable(source);
    int U = 0, V = 0;
    long long pU = 0, dV = 0, cross = 0;
    for (int ri = 0; ri < nr; ++ri) if (seen[rbase + ri]) {
      ++U; pU += 2LL * lower_counts[out.lower_masks[ri]];
    }
    for (int ai = 0; ai < na; ++ai) if (seen[abase + ai]) {
      ++V;
      int A = out.upper_masks[ai];
      dV += 2LL * upper_counts[A] - (A == endpoint_left) - (A == endpoint_right);
    }
    for (const Ref& ref : refs) {
      if (seen[rbase + ref.ri] && !seen[abase + ref.ai])
        cross += lower_counts[out.lower_masks[ref.ri]];
    }
    cout << "  mincut U=" << U << " V=" << V
         << " p(U)-d(V)=" << (pU-dV) << " crosscap=" << cross << "\n";
    return out;
  }
  out.flow_feasible = true;
  vector<IncEntry> incidence_entries;
  for (const Ref& ref : refs) {
    const auto& edge = din.g[ref.node][ref.edge_index];
    int flow = edge.original - edge.cap;
    incidence_entries.push_back({ref.ri, ref.ai, edge.original, flow});
  }
  const int initial_half_components =
      half_support_components(nr, na, incidence_entries);
  const bool half_connected = connect_half_support(
      nr, na, incidence_entries, pairing_seed ^ 0xc011ec7ULL);
  const int final_half_components =
      half_support_components(nr, na, incidence_entries);
  cout << "  half-support components " << initial_half_components
       << " -> " << final_half_components
       << (half_connected ? " (connected)\n" : " (stuck)\n");
  out.half.assign(nr, {});
  for (const auto& e : incidence_entries) {
    if (e.h) out.half[e.r].push_back({e.a, e.h});
  }

  // Try many legal within-colour pairings of the certified half-edge flow.
  int best_components = std::numeric_limits<int>::max();
  vector<SelectedEdge> best_edges;
  for (int attempt = 0; attempt < 256; ++attempt) {
    vector<SelectedEdge> edges;
    bool ok = true;
    uint64_t salt = splitmix64(pairing_seed + attempt);
    for (int ri = 0; ri < nr && ok; ++ri) {
      vector<int> stubs;
      for (auto [ai, h] : out.half[ri]) for (int j = 0; j < h; ++j) stubs.push_back(ai);
      bool paired = false;
      for (int trial = 0; trial < 128 && !paired; ++trial) {
        vector<int> z = stubs;
        uint64_t state = splitmix64(salt ^ (uint64_t(ri) << 32) ^ trial);
        for (int i = static_cast<int>(z.size()) - 1; i > 0; --i) {
          state = splitmix64(state);
          int j = state % (i + 1);
          std::swap(z[i], z[j]);
        }
        paired = true;
        for (int i = 0; i < static_cast<int>(z.size()); i += 2)
          if (z[i] == z[i+1]) { paired = false; break; }
        if (paired) {
          for (int i = 0; i < static_cast<int>(z.size()); i += 2)
            edges.push_back({z[i], z[i+1], ri});
        }
      }
      if (!paired) {
        // Deterministic degree-sequence construction from Lemma 2.1.
        using Item = pair<int,int>; // (remaining degree, upper index)
        std::priority_queue<Item> pq;
        for (auto [ai,h] : out.half[ri]) if (h) pq.push({h, ai});
        while (!pq.empty()) {
          auto [da,a] = pq.top(); pq.pop();
          if (pq.empty()) { ok = false; break; }
          auto [db,b] = pq.top(); pq.pop();
          edges.push_back({a,b,ri});
          if (--da) pq.push({da,a});
          if (--db) pq.push({db,b});
        }
      }
    }
    if (!ok) continue;
    int comps = component_count(na, out.upper_masks, upper_counts, edges);
    if (comps < best_components) {
      best_components = comps;
      best_edges = std::move(edges);
    }
    if (comps == 1) break;
  }
  if (!best_edges.empty()) {
    best_components = merge_same_colour_components(
        na, out.upper_masks, upper_counts, best_edges, nr);
  }
  out.components = best_components;
  if (best_components != 1) return out;
  out.connected = true;

  // Construct and independently verify the Euler trail.
  vector<vector<pair<int,int>>> adj(na);
  for (int id = 0; id < static_cast<int>(best_edges.size()); ++id) {
    auto e = best_edges[id];
    adj[e.a].push_back({id,e.b});
    adj[e.b].push_back({id,e.a});
  }
  int start = upper_idx[endpoint_left];
  vector<int> ptr(na,0), stack{start}, trail;
  vector<char> used(best_edges.size(), false);
  while (!stack.empty()) {
    int u = stack.back();
    while (ptr[u] < static_cast<int>(adj[u].size()) && used[adj[u][ptr[u]].first]) ++ptr[u];
    if (ptr[u] == static_cast<int>(adj[u].size())) {
      trail.push_back(u); stack.pop_back();
    } else {
      auto [id,v] = adj[u][ptr[u]++];
      if (used[id]) continue;
      used[id] = true; stack.push_back(v);
    }
  }
  std::reverse(trail.begin(), trail.end());
  const long long nocc = std::accumulate(upper_counts.begin(), upper_counts.end(), 0LL);
  if (static_cast<long long>(trail.size()) != nocc)
    throw runtime_error("bad Euler trail length");
  vector<int> got_upper(lim,0), got_lower(lim,0);
  uint64_t hash = 0xcbf29ce484222325ULL;
  for (int ai : trail) {
    int A = out.upper_masks[ai];
    out.trail_masks.push_back(A);
    ++got_upper[A];
    hash ^= uint64_t(A + 1); hash *= 0x100000001b3ULL;
  }
  for (int i = 0; i + 1 < static_cast<int>(trail.size()); ++i) {
    int R = out.upper_masks[trail[i]] & out.upper_masks[trail[i+1]];
    ++got_lower[R];
  }
  if (got_upper != upper_counts || got_lower != lower_counts)
    throw runtime_error("Euler witness verification failed");
  out.trail_hash = hash;
  return out;
}

void print_histogram(const vector<int>& counts, int rank) {
  std::unordered_map<int,int> hist;
  for (int mask = 0; mask < static_cast<int>(counts.size()); ++mask)
    if (std::popcount(static_cast<unsigned>(mask)) == rank) ++hist[counts[mask]];
  vector<pair<int,int>> v(hist.begin(),hist.end());
  std::sort(v.begin(),v.end());
  uint64_t hash = 0xcbf29ce484222325ULL;
  for (int mask = 0; mask < static_cast<int>(counts.size()); ++mask) {
    if (!counts[mask]) continue;
    hash ^= uint64_t(mask + 1); hash *= 0x100000001b3ULL;
    hash ^= uint64_t(counts[mask]); hash *= 0x100000001b3ULL;
  }
  cout << "  load histogram";
  for (auto [load,num] : v) cout << " " << load << "^" << num;
  cout << " hash=" << hash << "\n";
}

} // namespace

int main(int argc, char** argv) {
  try {
    const string file = argc > 1 ? argv[1] : "scratch/k15_doubletrans_05_213_hall29.json";
    const int max_seeds = argc > 2 ? std::stoi(argv[2]) : 8;
    constexpr int k = 15;
    vector<int> path = parse_integer_array(file, "middle_path");
    if (static_cast<long long>(path.size()) != choose_int(k, 8))
      throw runtime_error("unexpected path length");
    vector<int> actual1 = trace_counts(path, 1, k);
    vector<int> actual2 = trace_counts(path, 2, k);
    vector<int> actual3 = trace_counts(path, 3, k);
    vector<int> deg2 = point_degree(actual2, k), deg3 = point_degree(actual3, k);
    int left1 = path[0] & path[1], right1 = path[path.size()-2] & path.back();
    int left2 = path[0] & path[1] & path[2];
    int right2 = path[path.size()-3] & path[path.size()-2] & path.back();

    bool found = false;
    for (uint64_t seed = 0; seed < static_cast<uint64_t>(max_seeds) && !found; ++seed) {
      vector<int> design2 = hole_free_design(k, 6, path.size()-2, deg2,
                                             0x22000000ULL + seed);
      vector<int> design3 = hole_free_design(k, 5, path.size()-3, deg3,
                                             0x33000000ULL + 17*seed);
      if (seed == 0) {
        cout << "depth 2 design:\n"; print_histogram(design2, 6);
        cout << "depth 3 design:\n"; print_histogram(design3, 5);
      }
      cout << "seed " << seed << " q1->q2\n";
      FlowResult f12 = adjacent_flow(k, actual1, design2, left1, right1,
                                     0x12000000ULL + seed);
      cout << "  flow " << f12.value << "/" << f12.required
           << " components=" << f12.components;
      if (f12.connected) cout << " trail_hash=" << f12.trail_hash;
      cout << "\n";
      if (f12.connected) {
        vector<int> expected_internal(1 << k, 0);
        for (int mask = 0; mask < (1 << k); ++mask)
          if (std::popcount(static_cast<unsigned>(mask)) == 8)
            expected_internal[mask] = 1;
        --expected_internal[path.front()]; --expected_internal[path.back()];
        vector<int> got_union(1 << k, 0);
        for (int i = 0; i + 1 < static_cast<int>(f12.trail_masks.size()); ++i)
          ++got_union[f12.trail_masks[i] | f12.trail_masks[i+1]];
        long long deficit = 0, excess = 0;
        int hole_types = 0, excess_types = 0;
        for (int mask = 0; mask < (1 << k); ++mask) {
          if (got_union[mask] < expected_internal[mask]) {
            deficit += expected_internal[mask] - got_union[mask]; ++hole_types;
          }
          if (got_union[mask] > expected_internal[mask]) {
            excess += got_union[mask] - expected_internal[mask]; ++excess_types;
          }
        }
        cout << "  top-owner union deficit=" << deficit
             << " in " << hole_types << " types, excess=" << excess
             << " in " << excess_types << " types\n";
      }
      cout << "seed " << seed << " q2->q3\n";
      FlowResult f23 = adjacent_flow(k, design2, design3, left2, right2,
                                     0x23000000ULL + seed);
      cout << "  flow " << f23.value << "/" << f23.required
           << " components=" << f23.components;
      if (f23.connected) cout << " trail_hash=" << f23.trail_hash;
      cout << "\n";
      if (f23.connected) {
        vector<int> expected_internal = actual1;
        --expected_internal[left1]; --expected_internal[right1];
        vector<int> got_union(1 << k, 0);
        for (int i = 0; i + 1 < static_cast<int>(f23.trail_masks.size()); ++i)
          ++got_union[f23.trail_masks[i] | f23.trail_masks[i+1]];
        long long deficit = 0, excess = 0;
        int hole_types = 0, excess_types = 0;
        for (int mask = 0; mask < (1 << k); ++mask) {
          if (got_union[mask] < expected_internal[mask]) {
            deficit += expected_internal[mask] - got_union[mask]; ++hole_types;
          }
          if (got_union[mask] > expected_internal[mask]) {
            excess += got_union[mask] - expected_internal[mask]; ++excess_types;
          }
        }
        cout << "  common-order upper deficit=" << deficit
             << " in " << hole_types << " types, excess=" << excess
             << " in " << excess_types << " types\n";
      }
      found = f12.connected && f23.connected;
      if (found) cout << "PAIRWISE_ADJACENT_EULER_PASS seed=" << seed << "\n";
    }
    if (!found) {
      cout << "NO_CONNECTED_PAIRWISE_WITNESS_IN_SEEDS\n";
      return 2;
    }
    return 0;
  } catch (const std::exception& e) {
    cerr << "error: " << e.what() << "\n";
    return 1;
  }
}
