#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

using U32 = std::uint32_t;

struct DSU {
    std::vector<int> p, sz;
    explicit DSU(int n) : p(n), sz(n, 1) {
        std::iota(p.begin(), p.end(), 0);
    }
    int find(int x) {
        while (p[x] != x) x = p[x] = p[p[x]];
        return x;
    }
    void unite(int x, int y) {
        x = find(x); y = find(y);
        if (x == y) return;
        if (sz[x] < sz[y]) std::swap(x, y);
        p[y] = x; sz[x] += sz[y];
    }
};

static std::pair<U32, int> apply_g(U32 x, int m) {
    std::vector<int> before(2 * m);
    int h = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (((x >> i) & 1U) == 0 && h == 0) ++d0;
        h += ((x >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((x >> i) & 1U) == 0 && (before[i] == 0 || before[i] == 1)) {
            if (++ordinal == d0 + 1) return {x | (U32{1} << i), i};
        }
    }
    assert(false);
    return {};
}

static std::pair<U32, int> apply_h(U32 y, int m) {
    std::vector<int> before(2 * m);
    int h = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (((y >> i) & 1U) && h == 1) ++u1;
        h += ((y >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((y >> i) & 1U) && (before[i] == 0 || before[i] == 1)) {
            if (++ordinal == u1) return {y & ~(U32{1} << i), i};
        }
    }
    assert(false);
    return {};
}

static long long binom(int n, int k) {
    if (k < 0 || k > n) return 0;
    long long z = 1;
    for (int i = 1; i <= k; ++i) z = z * (n - k + i) / i;
    return z;
}

static U32 swap_bits(U32 s, int u, int v) {
    const U32 bu = (s >> u) & 1U;
    const U32 bv = (s >> v) & 1U;
    if (bu != bv) s ^= (U32{1} << u) | (U32{1} << v);
    return s;
}

static U32 block_mask(const std::vector<int>& q, int n, int m, int cut) {
    U32 s = 0;
    for (int t = 0; t < m; ++t)
        s |= U32{1} << q[(cut + 1 + 2 * t) % n];
    return s;
}

static std::string dyck_string(U32 x, int m) {
    std::string s;
    s.reserve(2 * m);
    for (int p = 0; p < 2 * m; ++p)
        s.push_back(((x >> p) & 1U) ? '1' : '0');
    return s;
}

static int dyck_area(U32 x, int m) {
    int h = 0, area = 0;
    for (int p = 0; p < 2 * m; ++p) {
        area += h;
        h += ((x >> p) & 1U) ? 1 : -1;
    }
    return area;
}

static int nontrivial_primitive_count(U32 x, int m) {
    int h = 0, start = 0, count = 0;
    for (int p = 0; p < 2 * m; ++p) {
        h += ((x >> p) & 1U) ? 1 : -1;
        if (h == 0) {
            if (p + 1 - start > 2) ++count;
            start = p + 1;
        }
    }
    return count;
}

struct Factor {
    int m, n;
    std::vector<int> owner;
    std::vector<U32> middle_sets;
    std::vector<U32> base_dyck;
    std::vector<std::vector<int>> omitted_words;
    int blocks = 0;

    explicit Factor(int m_) : m(m_), n(2 * m + 1), owner(U32{1} << n, -1) {
        assert(n < 32);
        generate_dyck(0, 0, 0, 0);
        assert(blocks == binom(2 * m, m) / (m + 1));
        assert(static_cast<long long>(middle_sets.size()) == binom(n, m));
    }

    void add_block(U32 x0) {
        base_dyck.push_back(x0);
        U32 x = x0;
        std::vector<int> omitted;
        omitted.reserve(n);
        for (int e = 0; e < m; ++e) {
            auto [y, a] = apply_g(x, m);
            auto [next, b] = apply_h(y, m);
            omitted.push_back(a);
            omitted.push_back(b);
            x = next;
        }
        const U32 old_full = (U32{1} << (2 * m)) - 1;
        assert(x == (old_full ^ x0));
        omitted.push_back(2 * m);
        omitted_words.push_back(omitted);

        for (int i = 0; i < n; ++i) {
            U32 s = 0;
            for (int t = 0; t < m; ++t)
                s |= U32{1} << omitted[(i + 1 + 2 * t) % n];
            assert(owner[s] == -1);
            owner[s] = blocks;
            middle_sets.push_back(s);
        }
        ++blocks;
    }

    void generate_dyck(int pos, int up, int down, U32 mask) {
        if (pos == 2 * m) {
            assert(up == m && down == m);
            add_block(mask);
            return;
        }
        if (up < m) generate_dyck(pos + 1, up + 1, down,
                                  mask | (U32{1} << pos));
        if (down < up) generate_dyck(pos + 1, up, down + 1, mask);
    }
};

struct Stats {
    int u, v, components, largest, smallest, singletons;
    std::map<int, int> hist;
};

static Stats analyze(const Factor& f, int u, int v) {
    DSU dsu(f.blocks);
    for (U32 s : f.middle_sets) {
        U32 t = swap_bits(s, u, v);
        dsu.unite(f.owner[s], f.owner[t]);
    }
    std::map<int, int> sizes;
    for (int b = 0; b < f.blocks; ++b) ++sizes[dsu.find(b)];
    Stats out{u, v, static_cast<int>(sizes.size()), 0, f.blocks, 0, {}};
    for (auto [root, size] : sizes) {
        out.largest = std::max(out.largest, size);
        out.smallest = std::min(out.smallest, size);
        out.singletons += size == 1;
        ++out.hist[size];
    }
    return out;
}

static void dump_components(const Factor& f, int u, int v) {
    DSU dsu(f.blocks);
    for (U32 s : f.middle_sets)
        dsu.unite(f.owner[s], f.owner[swap_bits(s, u, v)]);
    std::map<int, std::vector<int>> members;
    for (int b = 0; b < f.blocks; ++b) members[dsu.find(b)].push_back(b);
    for (const auto& [root, ids] : members) {
        std::cout << "COMPONENT size=" << ids.size() << " dyck=";
        for (int id : ids) {
            for (int p = 0; p < 2 * f.m; ++p)
                std::cout << (((f.base_dyck[id] >> p) & 1U) ? '1' : '0');
            std::cout << "[";
            for (int x : f.omitted_words[id]) std::cout << x + 1 << '.';
            std::cout << "],";
        }
        std::cout << '\n';
    }
}

static void dump_owner_edges(const Factor& f, int u, int v) {
    for (int id = 0; id < f.blocks; ++id) {
        struct Witness { int other, cut, other_cut; U32 mask; };
        std::map<int, Witness> neighbors;
        for (int cut = 0; cut < f.n; ++cut) {
            U32 s = block_mask(f.omitted_words[id], f.n, f.m, cut);
            U32 t = swap_bits(s, u, v);
            int other = f.owner[t];
            if (other == id) continue;
            int other_cut = -1;
            for (int j = 0; j < f.n; ++j)
                if (block_mask(f.omitted_words[other], f.n, f.m, j) == t) {
                    other_cut = j;
                    break;
                }
            assert(other_cut >= 0);
            neighbors.try_emplace(other, Witness{other, cut, other_cut, s});
        }
        const std::string x = dyck_string(f.base_dyck[id], f.m);
        std::cout << "ROOT " << x
                  << " area=" << dyck_area(f.base_dyck[id], f.m)
                  << " nontriv="
                  << nontrivial_primitive_count(f.base_dyck[id], f.m)
                  << " starts10=" << (x.rfind("10", 0) == 0)
                  << '\n';
        for (const auto& [other, w] : neighbors) {
            const std::string y = dyck_string(f.base_dyck[other], f.m);
            std::cout << " EDGE to=" << y
                      << " area=" << dyck_area(f.base_dyck[other], f.m)
                      << " nontriv="
                      << nontrivial_primitive_count(f.base_dyck[other], f.m)
                      << " starts10=" << (y.rfind("10", 0) == 0)
                      << " cut=" << w.cut
                      << " other_cut=" << w.other_cut
                      << " mask=" << w.mask << '\n';
        }
    }
}

static void add_rank_intervals(std::unordered_map<U32, int>& delta,
                               const std::vector<int>& q, int n, int r,
                               int sign, int u, int v, bool transpose) {
    for (int i = 0; i < n; ++i) {
        U32 s = 0;
        for (int t = 0; t < r; ++t) {
            int x = q[(i + 2 * t) % n];
            if (transpose) {
                if (x == u) x = v;
                else if (x == v) x = u;
            }
            s |= U32{1} << x;
        }
        delta[s] += sign;
    }
}

static void analyze_size_two_effects(const Factor& f, int u, int v,
                                     int dump_rank = -1) {
    DSU dsu(f.blocks);
    for (U32 s : f.middle_sets)
        dsu.unite(f.owner[s], f.owner[swap_bits(s, u, v)]);
    std::map<int, std::vector<int>> members;
    for (int b = 0; b < f.blocks; ++b) members[dsu.find(b)].push_back(b);
    std::vector<std::vector<int>> pairs;
    for (auto& [root, ids] : members) if (ids.size() == 2) pairs.push_back(ids);
    std::cout << "EFFECTS swap=" << u + 1 << ',' << v + 1
              << " size_two_components=" << pairs.size() << '\n';
    for (int r = 1; r <= f.m; ++r) {
        long long sum_support = 0, sum_l1 = 0;
        int max_support = 0, max_abs = 0;
        std::unordered_map<U32, int> target_degree;
        for (const auto& ids : pairs) {
            std::unordered_map<U32, int> delta;
            for (int id : ids) {
                add_rank_intervals(delta, f.omitted_words[id], f.n, r,
                                   -1, u, v, false);
                add_rank_intervals(delta, f.omitted_words[id], f.n, r,
                                   +1, u, v, true);
            }
            int support = 0, l1 = 0;
            for (auto [s, z] : delta) if (z) {
                ++support; l1 += std::abs(z);
                max_abs = std::max(max_abs, std::abs(z));
                ++target_degree[s];
            }
            if (dump_rank == r) {
                std::cout << "  TRADE dyck=";
                for (int id : ids) {
                    for (int p = 0; p < 2 * f.m; ++p)
                        std::cout << (((f.base_dyck[id] >> p) & 1U) ? '1' : '0');
                    std::cout << ',';
                }
                std::cout << " delta=";
                std::vector<std::pair<U32,int>> nz;
                for (auto [s,z] : delta) if (z) nz.push_back({s,z});
                std::sort(nz.begin(), nz.end());
                for (auto [s,z] : nz) {
                    std::cout << (z > 0 ? '+' : '-') << '{';
                    for (int b = 0; b < f.n; ++b)
                        if ((s >> b) & 1U) std::cout << b + 1 << '.';
                    std::cout << "},";
                }
                std::cout << '\n';
            }
            sum_support += support;
            sum_l1 += l1;
            max_support = std::max(max_support, support);
        }
        int max_degree = 0;
        for (auto [s, d] : target_degree) max_degree = std::max(max_degree, d);
        std::cout << " rank=" << r
                  << " union_targets=" << target_degree.size()
                  << " avg_support=" << (pairs.empty() ? 0.0 :
                         double(sum_support) / pairs.size())
                  << " max_support=" << max_support
                  << " avg_l1=" << (pairs.empty() ? 0.0 :
                         double(sum_l1) / pairs.size())
                  << " max_abs=" << max_abs
                  << " max_target_degree=" << max_degree << '\n';
    }
}

static std::unordered_map<U32,int> component_rank_effect(
        const Factor& f, const std::vector<int>& ids, int u, int v, int r) {
    std::unordered_map<U32,int> delta;
    for (int id : ids) {
        add_rank_intervals(delta, f.omitted_words[id], f.n, r,
                           -1, u, v, false);
        add_rank_intervals(delta, f.omitted_words[id], f.n, r,
                           +1, u, v, true);
    }
    return delta;
}

static void analyze_all_component_effects(const Factor& f, int u, int v) {
    DSU dsu(f.blocks);
    for (U32 s : f.middle_sets)
        dsu.unite(f.owner[s], f.owner[swap_bits(s, u, v)]);
    std::map<int, std::vector<int>> members;
    for (int b = 0; b < f.blocks; ++b) members[dsu.find(b)].push_back(b);
    std::map<int, std::vector<std::vector<int>>> by_size;
    for (auto& [root, ids] : members) by_size[ids.size()].push_back(ids);
    std::cout << "ALL_EFFECTS swap=" << u + 1 << ',' << v + 1
              << " classes=" << by_size.size() << '\n';
    for (auto& [size, comps] : by_size) {
        std::cout << " class_size=" << size << " count=" << comps.size() << '\n';
        for (int r = 1; r <= f.m; ++r) {
            long long sum_support = 0, sum_l1 = 0;
            int nonzero_components = 0, max_support = 0, max_abs = 0;
            std::unordered_map<U32,int> degree;
            for (const auto& ids : comps) {
                auto delta = component_rank_effect(f, ids, u, v, r);
                int support = 0, l1 = 0;
                for (auto [s,z] : delta) if (z) {
                    ++support; l1 += std::abs(z); ++degree[s];
                    max_abs = std::max(max_abs, std::abs(z));
                }
                nonzero_components += support != 0;
                sum_support += support; sum_l1 += l1;
                max_support = std::max(max_support, support);
            }
            if (!nonzero_components) continue;
            int max_degree = 0;
            for (auto [s,d] : degree) max_degree = std::max(max_degree, d);
            std::cout << "  rank=" << r
                      << " nonzero=" << nonzero_components
                      << " avg_support=" << double(sum_support)/comps.size()
                      << " max_support=" << max_support
                      << " avg_l1=" << double(sum_l1)/comps.size()
                      << " max_abs=" << max_abs
                      << " union=" << degree.size()
                      << " max_degree=" << max_degree << '\n';
        }
    }

    std::cout << "HEAT_LEDGER\n";
    for (int r = 1; r <= f.m; ++r) {
        long long component_l2 = 0;
        std::unordered_map<U32,long long> total_delta;
        std::map<int, long long> class_component_l2;
        std::map<int, std::unordered_map<U32,long long>> class_delta;
        for (const auto& [size, comps] : by_size) {
            for (const auto& ids : comps) {
                auto delta = component_rank_effect(f, ids, u, v, r);
                for (auto [s,z] : delta) if (z) {
                    component_l2 += 1LL * z * z;
                    class_component_l2[size] += 1LL * z * z;
                    class_delta[size][s] += z;
                    total_delta[s] += z;
                }
            }
        }
        long long aggregate_l2 = 0;
        long long aggregate_l1 = 0;
        long long aggregate_max_abs = 0;
        for (auto [s,z] : total_delta) {
            (void)s;
            aggregate_l2 += z * z;
            aggregate_l1 += std::llabs(z);
            aggregate_max_abs = std::max(aggregate_max_abs, std::llabs(z));
        }
        std::cout << " rank=" << r
                  << " aggregate_l2=" << aggregate_l2
                  << " aggregate_l1=" << aggregate_l1
                  << " aggregate_max_abs=" << aggregate_max_abs
                  << " component_l2=" << component_l2
                  << " gap=" << (aggregate_l2-component_l2)
                  << '\n';
        for (const auto& [size, delta] : class_delta) {
            long long class_aggregate_l2 = 0;
            for (auto [s,z] : delta) {
                (void)s;
                class_aggregate_l2 += z * z;
            }
            std::cout << "  class_size=" << size
                      << " aggregate_l2=" << class_aggregate_l2
                      << " component_l2=" << class_component_l2[size]
                      << " gap="
                      << (class_aggregate_l2-class_component_l2[size])
                      << '\n';
        }
        if (r == f.m - 1) {
            std::cout << "  CLASS_GRAM" << '\n';
            for (auto it = class_delta.begin(); it != class_delta.end(); ++it) {
                auto jt = it;
                ++jt;
                for (; jt != class_delta.end(); ++jt) {
                    const auto* small = &it->second;
                    const auto* large = &jt->second;
                    if (small->size() > large->size()) std::swap(small, large);
                    long long dot = 0;
                    for (auto [s,z] : *small) {
                        auto found = large->find(s);
                        if (found != large->end()) dot += z * found->second;
                    }
                    if (dot != 0)
                        std::cout << "   " << it->first << ',' << jt->first
                                  << " dot=" << dot << '\n';
                }
            }
        }
    }
}

static void print_stats(const Stats& s, int infinity) {
    std::cout << "swap=" << s.u + 1 << ',' << s.v + 1;
    if (s.v == infinity) std::cout << "(infinity)";
    std::cout << " components=" << s.components
              << " smallest=" << s.smallest
              << " largest=" << s.largest
              << " singletons=" << s.singletons
              << " hist=";
    int printed = 0;
    for (auto [size, count] : s.hist) {
        if (printed++ == 12) { std::cout << "..."; break; }
        std::cout << size << ':' << count << ',';
    }
    std::cout << '\n';
}

int main(int argc, char** argv) {
    const int m = argc > 1 ? std::stoi(argv[1]) : 8;
    bool all = false;
    int dump_u = -1, dump_v = -1, effects_u = -1, effects_v = -1;
    int effect_dump_rank = -1;
    int all_effects_u = -1, all_effects_v = -1;
    int owner_edges_u = -1, owner_edges_v = -1;
    bool cap_diamond = false;
    for (int i = 2; i < argc; ++i) all |= std::string(argv[i]) == "--all";
    for (int i = 2; i < argc; ++i)
        cap_diamond |= std::string(argv[i]) == "--capdiamond";
    for (int i = 2; i + 2 < argc; ++i) {
        if (std::string(argv[i]) == "--dump") {
            dump_u = std::stoi(argv[i + 1]) - 1;
            dump_v = std::stoi(argv[i + 2]) - 1;
        }
        if (std::string(argv[i]) == "--effects") {
            effects_u = std::stoi(argv[i + 1]) - 1;
            effects_v = std::stoi(argv[i + 2]) - 1;
        }
        if (std::string(argv[i]) == "--effectdump") {
            effects_u = std::stoi(argv[i + 1]) - 1;
            effects_v = std::stoi(argv[i + 2]) - 1;
            effect_dump_rank = std::stoi(argv[i + 3]);
        }
        if (std::string(argv[i]) == "--alleffects") {
            all_effects_u = std::stoi(argv[i + 1]) - 1;
            all_effects_v = std::stoi(argv[i + 2]) - 1;
        }
        if (std::string(argv[i]) == "--owneredges") {
            owner_edges_u = std::stoi(argv[i + 1]) - 1;
            owner_edges_v = std::stoi(argv[i + 2]) - 1;
        }
    }
    if (m < 2 || 2 * m + 1 >= 32) {
        std::cerr << "require 2 <= m <= 15\n";
        return 2;
    }

    Factor f(m);
    std::cout << "m=" << m << " n=" << f.n << " blocks=" << f.blocks
              << " middle=" << f.middle_sets.size() << '\n';

    if (cap_diamond) {
        Factor lifted(m + 1);
        long long hypotheses = 0, failures = 0;
        for (U32 z : f.middle_sets) {
            const U32 sz = swap_bits(z, 0, 1);
            if (f.owner[z] == f.owner[sz]) continue;
            ++hypotheses;
            const U32 cap_z = (z << 2) | U32{1};
            const U32 cap_sz = (sz << 2) | U32{1};
            if (lifted.owner[cap_z] != lifted.owner[cap_sz]) {
                if (failures < 20) {
                    std::cout << " CAP_FAIL z=" << z
                              << " sz=" << sz
                              << " old=" << f.owner[z] << ',' << f.owner[sz]
                              << " lifted=" << lifted.owner[cap_z] << ','
                              << lifted.owner[cap_sz] << '\n';
                }
                ++failures;
            }
        }
        std::cout << "CAP_DIAMOND m=" << m
                  << " hypotheses=" << hypotheses
                  << " failures=" << failures << '\n';
        return failures == 0 ? 0 : 1;
    }

    if (dump_u >= 0) {
        dump_components(f, dump_u, dump_v);
        return 0;
    }
    if (effects_u >= 0) {
        analyze_size_two_effects(f, effects_u, effects_v, effect_dump_rank);
        return 0;
    }
    if (all_effects_u >= 0) {
        analyze_all_component_effects(f, all_effects_u, all_effects_v);
        return 0;
    }
    if (owner_edges_u >= 0) {
        dump_owner_edges(f, owner_edges_u, owner_edges_v);
        return 0;
    }

    std::vector<std::pair<int, int>> swaps;
    if (all) {
        for (int u = 0; u < f.n; ++u)
            for (int v = u + 1; v < f.n; ++v) swaps.push_back({u, v});
    } else {
        // All old-coordinate separations from position 1, plus every swap
        // involving the distinguished coordinate infinity.
        for (int v = 1; v < 2 * m; ++v) swaps.push_back({0, v});
        for (int u = 0; u < 2 * m; ++u) swaps.push_back({u, 2 * m});
        std::sort(swaps.begin(), swaps.end());
        swaps.erase(std::unique(swaps.begin(), swaps.end()), swaps.end());
    }

    int min_components = f.blocks, max_components = 0;
    std::tuple<int, int, int> min_case, max_case;
    std::map<int, int> component_hist;
    for (auto [u, v] : swaps) {
        Stats s = analyze(f, u, v);
        print_stats(s, 2 * m);
        ++component_hist[s.components];
        if (s.components < min_components) {
            min_components = s.components;
            min_case = {u, v, s.largest};
        }
        if (s.components > max_components) {
            max_components = s.components;
            max_case = {u, v, s.largest};
        }
    }
    auto [min_u, min_v, min_largest] = min_case;
    auto [max_u, max_v, max_largest] = max_case;
    std::cout << "SUMMARY swaps=" << swaps.size()
              << " min_components=" << min_components
              << " at=" << min_u + 1 << ',' << min_v + 1
              << " largest=" << min_largest
              << " max_components=" << max_components
              << " at=" << max_u + 1 << ',' << max_v + 1
              << " largest=" << max_largest
              << " component_count_hist=";
    for (auto [count, frequency] : component_hist)
        std::cout << count << ':' << frequency << ',';
    std::cout << '\n';
}
