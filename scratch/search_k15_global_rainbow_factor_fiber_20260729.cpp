#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <queue>
#include <random>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// Exact k=15 search in the global first-rainbow 2-factor fiber.
//
// A rank-seven colour orbit L has eight extension incidences L -> L+a.
// Selecting two incidences at every L and two at every rank-eight vertex
// orbit is exactly the quotient form of
//   (i) one Johnson edge per rank-seven intersection colour, and
//  (ii) degree two at every rank-eight middle vertex.
// Thus the state space is the 2-factor fiber of an 8-regular bipartite
// incidence multigraph.  Every move made below is the symmetric difference
// with alternating cycles.  The large move generator fixes one of the two
// alternating perfect matchings and finds a new disjoint perfect matching;
// its difference from the old matching decomposes into exact alternating
// cycles.  No repair or projection is ever used.

namespace {

constexpr int K = 15;
constexpr int R = 8;
constexpr int M = 7;
constexpr int D = 3;
constexpr int N = 429;
constexpr int W = 6435;
constexpr int FULL = (1 << K) - 1;

int rotate_mask(int value, int shift) {
    shift %= K;
    if (shift < 0) shift += K;
    if (shift == 0) return value;
    return ((value << shift) | (value >> (K - shift))) & FULL;
}

std::pair<int, int> canonical_shift(int value) {
    int representative = value;
    for (int s = 1; s < K; ++s) representative = std::min(representative, rotate_mask(value, s));
    for (int s = 0; s < K; ++s) {
        if (rotate_mask(representative, s) == value) return {representative, s};
    }
    throw std::runtime_error("canonical shift failure");
}

int canonical(int value) { return canonical_shift(value).first; }

struct Arc {
    int l = -1;
    int v = -1;
    int added = -1;       // Coordinate in the lower representative frame.
    int phase = -1;       // midPhysical = rotate(midRepresentative, phase).
    int lower_at_v = 0;   // The rank-seven mask in the canonical V frame.
};

struct Catalogue {
    std::vector<int> lower;
    std::vector<int> middle;
    std::array<int, 1 << K> middle_index{};
    std::vector<Arc> arcs;
    std::array<std::array<int, K - M>, N> by_l{};
    std::array<std::vector<int>, N> by_v;

    Catalogue() {
        middle_index.fill(-1);
        for (int mask = 0; mask <= FULL; ++mask) {
            int rank = std::popcount(static_cast<unsigned>(mask));
            if (rank == M && canonical(mask) == mask) lower.push_back(mask);
            if (rank == R && canonical(mask) == mask) middle.push_back(mask);
        }
        std::sort(lower.begin(), lower.end());
        std::sort(middle.begin(), middle.end());
        if (static_cast<int>(lower.size()) != N || static_cast<int>(middle.size()) != N)
            throw std::runtime_error("central quotient size mismatch");
        for (int v = 0; v < N; ++v) middle_index[middle[v]] = v;

        for (int l = 0; l < N; ++l) {
            int slot = 0;
            for (int a = 0; a < K; ++a) {
                if ((lower[l] >> a) & 1) continue;
                int physical_mid = lower[l] | (1 << a);
                auto [rep, phase] = canonical_shift(physical_mid);
                int v = middle_index[rep];
                if (v < 0) throw std::runtime_error("missing middle representative");
                Arc arc;
                arc.l = l;
                arc.v = v;
                arc.added = a;
                arc.phase = phase;
                arc.lower_at_v = rotate_mask(lower[l], -phase);
                int id = static_cast<int>(arcs.size());
                arcs.push_back(arc);
                by_l[l][slot++] = id;
                by_v[v].push_back(id);
            }
            if (slot != K - M) throw std::runtime_error("lower incidence degree mismatch");
        }
        if (static_cast<int>(arcs.size()) != 8 * N) throw std::runtime_error("arc count mismatch");
        for (const auto &row : by_v) {
            if (static_cast<int>(row.size()) != R) throw std::runtime_error("middle incidence degree mismatch");
        }
    }
};

struct State {
    std::vector<uint8_t> selected;
    explicit State(int arcs = 0) : selected(arcs, 0) {}
};

struct Metrics {
    bool invariant_ok = false;
    int components = 0;
    int min_component = 0;
    int max_component = 0;
    int residence_bad_runs = 0;
    int residence_shortfall = 0;
    int minimum_run = W + 1;
    int missing_upper_q1 = 0;
    int missing_lower_q2 = 0;
    int missing_upper_q2 = 0;
    int missing_upper_q1_orbits = 0;
    int missing_lower_q2_orbits = 0;
    int missing_upper_q2_orbits = 0;
    int quotient_loops = 0;
    int upper_q1_pair_collisions = 0;
    int lower_q2_pair_collisions = 0;
    int collision_floor_excess = 0;
    std::array<uint16_t, 1 << K> upper_q1_load{};
    std::array<uint16_t, 1 << K> lower_q2_load{};
    std::array<uint16_t, 1 << K> upper_q2_load{};
    std::array<uint16_t, 1 << K> upper_q1_quotient_load{};
    std::array<uint16_t, 1 << K> lower_q2_quotient_load{};
};

std::array<std::vector<int>, N> selected_by_l(const Catalogue &cat, const State &state) {
    std::array<std::vector<int>, N> result;
    for (int e = 0; e < static_cast<int>(cat.arcs.size()); ++e)
        if (state.selected[e]) result[cat.arcs[e].l].push_back(e);
    return result;
}

std::array<std::vector<int>, N> selected_by_v(const Catalogue &cat, const State &state) {
    std::array<std::vector<int>, N> result;
    for (int e = 0; e < static_cast<int>(cat.arcs.size()); ++e)
        if (state.selected[e]) result[cat.arcs[e].v].push_back(e);
    return result;
}

bool check_fiber(const Catalogue &cat, const State &state) {
    auto left = selected_by_l(cat, state);
    auto right = selected_by_v(cat, state);
    for (int i = 0; i < N; ++i) {
        if (left[i].size() != 2 || right[i].size() != 2) return false;
    }
    return std::count(state.selected.begin(), state.selected.end(), uint8_t{1}) == 2 * N;
}

std::vector<int> rank_masks(int rank) {
    std::vector<int> result;
    for (int mask = 0; mask <= FULL; ++mask)
        if (std::popcount(static_cast<unsigned>(mask)) == rank) result.push_back(mask);
    return result;
}

Metrics evaluate(const Catalogue &cat, const State &state) {
    Metrics out;
    out.invariant_ok = check_fiber(cat, state);
    if (!out.invariant_ok) return out;

    auto left = selected_by_l(cat, state);
    auto right = selected_by_v(cat, state);
    for (int l = 0; l < N; ++l) {
        const Arc &a = cat.arcs[left[l][0]];
        const Arc &b = cat.arcs[left[l][1]];
        int target = canonical(cat.lower[l] | (1 << a.added) | (1 << b.added));
        ++out.upper_q1_quotient_load[target];
    }
    for (int v = 0; v < N; ++v) {
        int target = cat.arcs[right[v][0]].lower_at_v & cat.arcs[right[v][1]].lower_at_v;
        if (std::popcount(static_cast<unsigned>(target)) == R - 2)
            ++out.lower_q2_quotient_load[canonical(target)];
    }
    for (int mask = 0; mask <= FULL; ++mask) {
        int upper_load = out.upper_q1_quotient_load[mask];
        int lower_load = out.lower_q2_quotient_load[mask];
        out.upper_q1_pair_collisions += upper_load * (upper_load - 1) / 2;
        out.lower_q2_pair_collisions += lower_load * (lower_load - 1) / 2;
    }
    out.collision_floor_excess =
        out.upper_q1_pair_collisions + out.lower_q2_pair_collisions - 188;
    std::array<std::array<int, 2>, 1 << K> adjacency{};
    std::array<uint8_t, 1 << K> degree{};
    for (int l = 0; l < N; ++l) {
        int e0 = left[l][0], e1 = left[l][1];
        const Arc &a0 = cat.arcs[e0];
        const Arc &a1 = cat.arcs[e1];
        if (a0.v == a1.v) ++out.quotient_loops;
        int base_u = cat.lower[l] | (1 << a0.added);
        int base_v = cat.lower[l] | (1 << a1.added);
        for (int sheet = 0; sheet < K; ++sheet) {
            int u = rotate_mask(base_u, sheet);
            int v = rotate_mask(base_v, sheet);
            if (u == v || degree[u] >= 2 || degree[v] >= 2) {
                out.invariant_ok = false;
                return out;
            }
            adjacency[u][degree[u]++] = v;
            adjacency[v][degree[v]++] = u;
            ++out.upper_q1_load[u | v];
        }
    }

    static const std::vector<int> middle_masks = rank_masks(R);
    for (int value : middle_masks) {
        if (degree[value] != 2) {
            out.invariant_ok = false;
            return out;
        }
        int lower = value & adjacency[value][0] & adjacency[value][1];
        int upper = value | adjacency[value][0] | adjacency[value][1];
        if (std::popcount(static_cast<unsigned>(lower)) == R - 2) ++out.lower_q2_load[lower];
        if (std::popcount(static_cast<unsigned>(upper)) == R + 2) ++out.upper_q2_load[upper];
    }

    auto count_missing = [&](int rank, const auto &load, int &physical, int &orbits) {
        std::array<uint8_t, 1 << K> orbit_missing{};
        for (int mask = 0; mask <= FULL; ++mask) {
            if (std::popcount(static_cast<unsigned>(mask)) != rank) continue;
            if (load[mask] == 0) {
                ++physical;
                orbit_missing[canonical(mask)] = 1;
            }
        }
        orbits = std::accumulate(orbit_missing.begin(), orbit_missing.end(), 0);
    };
    count_missing(R + 1, out.upper_q1_load, out.missing_upper_q1, out.missing_upper_q1_orbits);
    count_missing(R - 2, out.lower_q2_load, out.missing_lower_q2, out.missing_lower_q2_orbits);
    count_missing(R + 2, out.upper_q2_load, out.missing_upper_q2, out.missing_upper_q2_orbits);

    std::array<uint8_t, 1 << K> seen{};
    out.min_component = W + 1;
    for (int start : middle_masks) {
        if (seen[start]) continue;
        std::vector<int> cycle;
        int previous = -1;
        int current = start;
        while (true) {
            if (seen[current]) {
                if (current != start) out.invariant_ok = false;
                break;
            }
            seen[current] = 1;
            cycle.push_back(current);
            int x = adjacency[current][0], y = adjacency[current][1];
            int next = previous < 0 ? std::min(x, y) : (x == previous ? y : x);
            previous = current;
            current = next;
        }
        if (!out.invariant_ok) return out;
        ++out.components;
        out.min_component = std::min(out.min_component, static_cast<int>(cycle.size()));
        out.max_component = std::max(out.max_component, static_cast<int>(cycle.size()));

        const int length = static_cast<int>(cycle.size());
        for (int coordinate = 0; coordinate < K; ++coordinate) {
            int zero = -1;
            for (int i = 0; i < length; ++i) {
                if (((cycle[i] >> coordinate) & 1) == 0) {
                    zero = i;
                    break;
                }
            }
            if (zero < 0) {
                out.minimum_run = std::min(out.minimum_run, length);
                if (length < D + 1) {
                    ++out.residence_bad_runs;
                    out.residence_shortfall += D + 1 - length;
                }
                continue;
            }
            int run = 0;
            for (int step = 1; step <= length; ++step) {
                int index = (zero + step) % length;
                if ((cycle[index] >> coordinate) & 1) {
                    ++run;
                } else if (run) {
                    out.minimum_run = std::min(out.minimum_run, run);
                    if (run < D + 1) {
                        ++out.residence_bad_runs;
                        out.residence_shortfall += D + 1 - run;
                    }
                    run = 0;
                }
            }
        }
    }
    if (out.minimum_run == W + 1) out.minimum_run = 0;
    return out;
}

std::string metrics_string(const Metrics &m) {
    return "components=" + std::to_string(m.components) +
           " comp_range=" + std::to_string(m.min_component) + ":" + std::to_string(m.max_component) +
           " res_bad=" + std::to_string(m.residence_bad_runs) +
           " res_short=" + std::to_string(m.residence_shortfall) +
           " min_run=" + std::to_string(m.minimum_run) +
           " miss_u1=" + std::to_string(m.missing_upper_q1) +
           "(" + std::to_string(m.missing_upper_q1_orbits) + ")" +
           " miss_l2=" + std::to_string(m.missing_lower_q2) +
           "(" + std::to_string(m.missing_lower_q2_orbits) + ")" +
           " miss_u2=" + std::to_string(m.missing_upper_q2) +
           "(" + std::to_string(m.missing_upper_q2_orbits) + ")" +
           " pairs=" + std::to_string(m.upper_q1_pair_collisions) + ":" +
           std::to_string(m.lower_q2_pair_collisions) +
           " xi=" + std::to_string(m.collision_floor_excess) +
           " loops=" + std::to_string(m.quotient_loops);
}

State load_fixture(const Catalogue &cat, const std::string &path) {
    std::ifstream input(path);
    if (!input) throw std::runtime_error("cannot open fixture: " + path);
    std::string magic;
    int k, n, w, d;
    input >> magic >> k >> n >> w >> d;
    if (magic != "K15RF1" || k != K || n != N || w != W || d != D)
        throw std::runtime_error("fixture header mismatch");
    std::unordered_map<int, int> lower_index;
    for (int l = 0; l < N; ++l) lower_index[cat.lower[l]] = l;
    State state(static_cast<int>(cat.arcs.size()));
    for (int row = 0; row < N; ++row) {
        int lower, a, b;
        input >> lower >> a >> b;
        auto found = lower_index.find(lower);
        if (!input || found == lower_index.end()) throw std::runtime_error("bad fixture lower row");
        int l = found->second;
        bool got_a = false, got_b = false;
        for (int e : cat.by_l[l]) {
            if (cat.arcs[e].added == a) state.selected[e] = 1, got_a = true;
            if (cat.arcs[e].added == b) state.selected[e] = 1, got_b = true;
        }
        if (!got_a || !got_b || a == b) throw std::runtime_error("bad fixture extension pair");
    }
    if (!check_fiber(cat, state)) throw std::runtime_error("fixture is outside exact fiber");
    return state;
}

struct MatchingDecomposition {
    std::array<int, N> m0{};
    std::array<int, N> m1{};
    std::array<int, N> m0_at_v{};
    std::array<int, N> m1_at_v{};
};

MatchingDecomposition decompose_factor(
    const Catalogue &cat, const State &state, std::mt19937_64 &rng
) {
    auto left = selected_by_l(cat, state);
    auto right = selected_by_v(cat, state);
    std::vector<uint8_t> edge_seen(cat.arcs.size(), 0);
    std::vector<int8_t> colour(cat.arcs.size(), -1);
    for (int seed = 0; seed < static_cast<int>(cat.arcs.size()); ++seed) {
        if (!state.selected[seed] || edge_seen[seed]) continue;
        std::vector<int> component;
        int start_node = cat.arcs[seed].l;
        int node = start_node;
        int edge = seed;
        int parity = 0;
        while (true) {
            if (edge_seen[edge]) {
                if (edge != seed || node != start_node) throw std::runtime_error("factor decomposition collision");
                break;
            }
            edge_seen[edge] = 1;
            component.push_back(edge);
            colour[edge] = static_cast<int8_t>(parity);
            parity ^= 1;
            const Arc &arc = cat.arcs[edge];
            bool at_left = node < N;
            int next_node = at_left ? N + arc.v : arc.l;
            const auto &incidence = at_left ? right[arc.v] : left[arc.l];
            int next_edge = incidence[0] == edge ? incidence[1] : incidence[0];
            node = next_node;
            edge = next_edge;
        }
        if (component.size() % 2) throw std::runtime_error("odd factor component");
        if (rng() & 1) {
            for (int e : component) colour[e] ^= 1;
        }
    }

    MatchingDecomposition out;
    out.m0.fill(-1);
    out.m1.fill(-1);
    out.m0_at_v.fill(-1);
    out.m1_at_v.fill(-1);
    for (int e = 0; e < static_cast<int>(cat.arcs.size()); ++e) {
        if (!state.selected[e]) continue;
        const Arc &arc = cat.arcs[e];
        auto &by_l = colour[e] == 0 ? out.m0[arc.l] : out.m1[arc.l];
        auto &by_v = colour[e] == 0 ? out.m0_at_v[arc.v] : out.m1_at_v[arc.v];
        if (by_l >= 0 || by_v >= 0) throw std::runtime_error("matching decomposition is not one-regular");
        by_l = by_v = e;
    }
    for (int i = 0; i < N; ++i)
        if (out.m0[i] < 0 || out.m1[i] < 0 || out.m0_at_v[i] < 0 || out.m1_at_v[i] < 0)
            throw std::runtime_error("incomplete matching decomposition");
    return out;
}

struct SearchConfig {
    int iterations = 1000;
    int seconds = 0;
    uint64_t seed = 1;
    int missing_reward = 10000;
    int singleton_reward = 100;
    int keep_bonus = 2500;
    int noise = 4000;
    int residence_weight = 100000;
    int component_weight = 100;
    int collision_weight = 1000;
    double temperature = 0.0;
    bool allow_quotient_loops = false;
    bool hard_residence = false;
    bool arbitrary_fixture = false;
    bool best_component_first = false;
    bool collision_primary = false;
    bool exhaust_target_cycles = false;
    std::string target_fixture;
    std::string output = "scratch/k15_global_rainbow_factor_best_20260729.json";
};

long long energy(const Metrics &m, const SearchConfig &cfg) {
    if (!m.invariant_ok) return std::numeric_limits<long long>::max() / 4;
    long long terminal = m.missing_upper_q1 + m.missing_lower_q2 + m.missing_upper_q2;
    long long objective = cfg.collision_primary
        ? static_cast<long long>(cfg.collision_weight) * m.collision_floor_excess + terminal
        : terminal;
    return static_cast<long long>(cfg.residence_weight) * m.residence_shortfall +
           static_cast<long long>(cfg.component_weight) * std::max(0, m.components - 1) +
           objective;
}

std::array<int, N> preferred_perfect_matching(
    const Catalogue &cat,
    const MatchingDecomposition &dec,
    const Metrics &current,
    const SearchConfig &cfg,
    std::mt19937_64 &rng
) {
    std::array<std::vector<std::pair<long long, int>>, N> ordered;
    std::uniform_int_distribution<int> jitter(-cfg.noise, cfg.noise);
    for (int l = 0; l < N; ++l) {
        const Arc &base = cat.arcs[dec.m0[l]];
        for (int e : cat.by_l[l]) {
            if (e == dec.m0[l]) continue;
            const Arc &arc = cat.arcs[e];
            if (!cfg.allow_quotient_loops && arc.v == base.v) continue;
            long long score = jitter(rng);
            int upper = canonical(cat.lower[l] | (1 << base.added) | (1 << arc.added));
            int uload = current.upper_q1_quotient_load[upper];
            score += uload == 0 ? cfg.missing_reward : (uload == 1 ? cfg.singleton_reward : -uload);
            const Arc &base_at_v = cat.arcs[dec.m0_at_v[arc.v]];
            int lower = base_at_v.lower_at_v & arc.lower_at_v;
            if (std::popcount(static_cast<unsigned>(lower)) == R - 2) {
                lower = canonical(lower);
                int lload = current.lower_q2_quotient_load[lower];
                score += lload == 0 ? cfg.missing_reward : (lload == 1 ? cfg.singleton_reward : -lload);
            }
            if (e == dec.m1[l]) score += cfg.keep_bonus;
            ordered[l].push_back({score, e});
        }
        std::shuffle(ordered[l].begin(), ordered[l].end(), rng);
        std::stable_sort(ordered[l].begin(), ordered[l].end(), [](auto x, auto y) { return x.first > y.first; });
    }

    std::array<int, N> match_l, match_v;
    match_l.fill(-1);
    match_v.fill(-1);
    std::vector<int> order(N);
    std::iota(order.begin(), order.end(), 0);
    std::shuffle(order.begin(), order.end(), rng);
    std::array<int, N> stamp{};
    int epoch = 0;
    auto augment = [&](auto &&self, int l) -> bool {
        for (const auto &[weight, e] : ordered[l]) {
            (void)weight;
            int v = cat.arcs[e].v;
            if (stamp[v] == epoch) continue;
            stamp[v] = epoch;
            if (match_v[v] < 0 || self(self, cat.arcs[match_v[v]].l)) {
                match_l[l] = e;
                match_v[v] = e;
                return true;
            }
        }
        return false;
    };
    for (int l : order) {
        ++epoch;
        if (!augment(augment, l)) throw std::runtime_error("perfect matching proposal unexpectedly infeasible");
    }
    return match_l;
}

std::vector<std::vector<int>> matching_difference_cycles(
    const Catalogue &cat,
    const std::array<int, N> &old_matching,
    const std::array<int, N> &proposal
) {
    std::array<int, N> old_at_v;
    old_at_v.fill(-1);
    for (int l = 0; l < N; ++l) old_at_v[cat.arcs[old_matching[l]].v] = old_matching[l];
    std::array<uint8_t, N> seen_l{};
    std::vector<std::vector<int>> cycles;
    for (int start = 0; start < N; ++start) {
        if (seen_l[start] || old_matching[start] == proposal[start]) continue;
        std::vector<int> toggle;
        int l = start;
        while (!seen_l[l]) {
            seen_l[l] = 1;
            int add = proposal[l];
            int v = cat.arcs[add].v;
            int remove = old_at_v[v];
            if (remove < 0) throw std::runtime_error("matching difference lost old endpoint");
            toggle.push_back(add);
            toggle.push_back(remove);
            l = cat.arcs[remove].l;
        }
        if (l != start) throw std::runtime_error("matching difference is not a cycle");
        cycles.push_back(std::move(toggle));
    }
    return cycles;
}

std::vector<std::vector<int>> shared_matching_difference_cycles(
    const Catalogue &cat, const State &source, const State &target
) {
    if (!check_fiber(cat, source) || !check_fiber(cat, target))
        throw std::runtime_error("target-cycle endpoint is outside the exact fiber");
    auto source_l = selected_by_l(cat, source);
    auto target_l = selected_by_l(cat, target);
    std::array<std::vector<int>, N> common;
    for (int l = 0; l < N; ++l) {
        for (int edge : source_l[l])
            if (target.selected[edge]) common[l].push_back(edge);
        if (common[l].empty())
            throw std::runtime_error("source and target have no common incidence at a lower vertex");
    }
    std::array<int, N> base_l, base_v;
    base_l.fill(-1);
    base_v.fill(-1);
    std::array<int, N> stamp{};
    int epoch = 0;
    auto augment = [&](auto &&self, int l) -> bool {
        for (int edge : common[l]) {
            int v = cat.arcs[edge].v;
            if (stamp[v] == epoch) continue;
            stamp[v] = epoch;
            if (base_v[v] < 0 || self(self, cat.arcs[base_v[v]].l)) {
                base_l[l] = edge;
                base_v[v] = edge;
                return true;
            }
        }
        return false;
    };
    for (int l = 0; l < N; ++l) {
        ++epoch;
        if (!augment(augment, l))
            throw std::runtime_error("common source/target edges contain no perfect matching");
    }
    std::array<int, N> old_matching, new_matching;
    for (int l = 0; l < N; ++l) {
        old_matching[l] = source_l[l][0] == base_l[l] ? source_l[l][1] : source_l[l][0];
        new_matching[l] = target_l[l][0] == base_l[l] ? target_l[l][1] : target_l[l][0];
    }
    std::array<int, N> old_degree{}, new_degree{};
    for (int l = 0; l < N; ++l) {
        ++old_degree[cat.arcs[old_matching[l]].v];
        ++new_degree[cat.arcs[new_matching[l]].v];
    }
    if (std::any_of(old_degree.begin(), old_degree.end(), [](int x) { return x != 1; }) ||
        std::any_of(new_degree.begin(), new_degree.end(), [](int x) { return x != 1; }))
        throw std::runtime_error("common-base complements are not perfect matchings");
    return matching_difference_cycles(cat, old_matching, new_matching);
}

void toggle_cycle(State &state, const std::vector<int> &cycle) {
    for (int e : cycle) state.selected[e] ^= 1;
}

bool resident_better(const Metrics &candidate, const Metrics &best, const SearchConfig &cfg) {
    if (candidate.residence_shortfall != 0) return false;
    if (best.residence_shortfall != 0) return true;
    if (cfg.best_component_first && candidate.components != best.components)
        return candidate.components < best.components;
    if (cfg.collision_primary && candidate.collision_floor_excess != best.collision_floor_excess)
        return candidate.collision_floor_excess < best.collision_floor_excess;
    auto a = std::tuple(candidate.missing_upper_q1 + candidate.missing_lower_q2 + candidate.missing_upper_q2,
                        candidate.missing_lower_q2, candidate.missing_upper_q1,
                        candidate.missing_upper_q2, candidate.components);
    auto b = std::tuple(best.missing_upper_q1 + best.missing_lower_q2 + best.missing_upper_q2,
                        best.missing_lower_q2, best.missing_upper_q1,
                        best.missing_upper_q2, best.components);
    return a < b;
}

void write_candidate(
    const Catalogue &cat,
    const State &state,
    const Metrics &metrics,
    const std::string &path,
    uint64_t seed,
    int iteration
) {
    auto left = selected_by_l(cat, state);
    std::ofstream out(path);
    if (!out) throw std::runtime_error("cannot write candidate: " + path);
    out << "{\n  \"schema\": \"global-rainbow-factor-candidate-v1\",\n";
    out << "  \"k\": 15, \"r\": 8, \"d\": 3, \"W\": 6435, \"N\": 429,\n";
    out << "  \"seed\": " << seed << ", \"iteration\": " << iteration << ",\n";
    out << "  \"exact_audit\": {\n";
    out << "    \"fiber_invariant\": " << (metrics.invariant_ok ? "true" : "false") << ",\n";
    out << "    \"physical_cycle_count\": " << metrics.components << ",\n";
    out << "    \"residence_bad_runs\": " << metrics.residence_bad_runs << ",\n";
    out << "    \"residence_shortfall\": " << metrics.residence_shortfall << ",\n";
    out << "    \"minimum_run\": " << metrics.minimum_run << ",\n";
    out << "    \"missing_upper_q1_physical\": " << metrics.missing_upper_q1 << ",\n";
    out << "    \"missing_lower_q2_physical\": " << metrics.missing_lower_q2 << ",\n";
    out << "    \"missing_upper_q2_physical\": " << metrics.missing_upper_q2 << ",\n";
    out << "    \"missing_upper_q1_orbits\": " << metrics.missing_upper_q1_orbits << ",\n";
    out << "    \"missing_lower_q2_orbits\": " << metrics.missing_lower_q2_orbits << ",\n";
    out << "    \"missing_upper_q2_orbits\": " << metrics.missing_upper_q2_orbits << ",\n";
    out << "    \"upper_q1_pair_collisions\": " << metrics.upper_q1_pair_collisions << ",\n";
    out << "    \"lower_q2_pair_collisions\": " << metrics.lower_q2_pair_collisions << ",\n";
    out << "    \"collision_floor_excess\": " << metrics.collision_floor_excess << ",\n";
    out << "    \"quotient_loops\": " << metrics.quotient_loops << "\n  },\n";
    out << "  \"choices\": [\n";
    for (int l = 0; l < N; ++l) {
        if (left[l].size() != 2) throw std::runtime_error("candidate export outside fiber");
        int a = cat.arcs[left[l][0]].added;
        int b = cat.arcs[left[l][1]].added;
        if (a > b) std::swap(a, b);
        out << "    [" << cat.lower[l] << ", " << a << ", " << b << "]";
        out << (l + 1 == N ? "\n" : ",\n");
    }
    out << "  ]\n}\n";
}

SearchConfig parse_args(int argc, char **argv, std::string &fixture, bool &calibrate) {
    SearchConfig cfg;
    fixture = "scratch/k15_global_rainbow_factor_seed_20260729.txt";
    calibrate = false;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        auto value = [&]() -> std::string {
            if (++i >= argc) throw std::runtime_error("missing value after " + arg);
            return argv[i];
        };
        if (arg == "--fixture") fixture = value();
        else if (arg == "--iterations") cfg.iterations = std::stoi(value());
        else if (arg == "--seconds") cfg.seconds = std::stoi(value());
        else if (arg == "--seed") cfg.seed = std::stoull(value());
        else if (arg == "--output") cfg.output = value();
        else if (arg == "--missing-reward") cfg.missing_reward = std::stoi(value());
        else if (arg == "--singleton-reward") cfg.singleton_reward = std::stoi(value());
        else if (arg == "--keep-bonus") cfg.keep_bonus = std::stoi(value());
        else if (arg == "--noise") cfg.noise = std::stoi(value());
        else if (arg == "--residence-weight") cfg.residence_weight = std::stoi(value());
        else if (arg == "--component-weight") cfg.component_weight = std::stoi(value());
        else if (arg == "--collision-weight") cfg.collision_weight = std::stoi(value());
        else if (arg == "--temperature") cfg.temperature = std::stod(value());
        else if (arg == "--allow-quotient-loops") cfg.allow_quotient_loops = true;
        else if (arg == "--hard-residence") cfg.hard_residence = true;
        else if (arg == "--arbitrary-fixture") cfg.arbitrary_fixture = true;
        else if (arg == "--best-component-first") cfg.best_component_first = true;
        else if (arg == "--collision-primary") cfg.collision_primary = true;
        else if (arg == "--target-fixture") cfg.target_fixture = value();
        else if (arg == "--exhaust-target-cycles") cfg.exhaust_target_cycles = true;
        else if (arg == "--calibrate-only") calibrate = true;
        else throw std::runtime_error("unknown argument: " + arg);
    }
    return cfg;
}

} // namespace

int main(int argc, char **argv) {
    try {
        std::string fixture;
        bool calibrate = false;
        SearchConfig cfg = parse_args(argc, argv, fixture, calibrate);
        Catalogue cat;
        State current = load_fixture(cat, fixture);
        Metrics current_metrics = evaluate(cat, current);
        if (!current_metrics.invariant_ok) throw std::runtime_error("seed physical expansion failed");
        std::cerr << "SEED " << metrics_string(current_metrics) << "\n";
        if (!cfg.arbitrary_fixture && (current_metrics.components != 1 || current_metrics.residence_bad_runs != 0 ||
            current_metrics.minimum_run != 4 || current_metrics.missing_upper_q1 != 995 ||
            current_metrics.missing_lower_q2 != 685 || current_metrics.missing_upper_q2 != 405 ||
            current_metrics.missing_upper_q1_orbits != 67 ||
            current_metrics.missing_lower_q2_orbits != 47 ||
            current_metrics.missing_upper_q2_orbits != 27 ||
            current_metrics.upper_q1_pair_collisions != 206 ||
            current_metrics.lower_q2_pair_collisions != 159 ||
            current_metrics.collision_floor_excess != 177)) {
            throw std::runtime_error("authoritative seed calibration changed");
        }
        if (calibrate) {
            std::cout << "CALIBRATION PASS\n";
            return 0;
        }

        std::mt19937_64 rng(cfg.seed);
        State best = current;
        Metrics best_metrics = current_metrics;
        write_candidate(cat, best, best_metrics, cfg.output, cfg.seed, 0);
        if (!cfg.target_fixture.empty()) {
            State target = load_fixture(cat, cfg.target_fixture);
            Metrics target_metrics = evaluate(cat, target);
            if (!target_metrics.invariant_ok) throw std::runtime_error("target physical expansion failed");
            auto target_cycles = shared_matching_difference_cycles(cat, current, target);
            std::cerr << "TARGET " << metrics_string(target_metrics)
                      << " alternating_cycles=" << target_cycles.size() << " supports=";
            for (const auto &cycle : target_cycles) std::cerr << (cycle.size() / 2) << ",";
            std::cerr << "\n";
            if (cfg.exhaust_target_cycles) {
                if (target_cycles.size() > 24)
                    throw std::runtime_error("refuse exhaustive target cube above 24 cycles");
                uint64_t total = uint64_t{1} << target_cycles.size();
                uint64_t resident = 0, connected_resident = 0, exact_decks = 0;
                for (uint64_t subset = 0; subset < total; ++subset) {
                    State candidate = current;
                    for (size_t bit = 0; bit < target_cycles.size(); ++bit)
                        if ((subset >> bit) & 1) toggle_cycle(candidate, target_cycles[bit]);
                    Metrics cm = evaluate(cat, candidate);
                    if (!cm.invariant_ok) throw std::runtime_error("target cube left exact fiber");
                    if (cm.residence_shortfall == 0) {
                        ++resident;
                        if (cm.components == 1) ++connected_resident;
                    }
                    if (cm.missing_upper_q1_orbits == 0 && cm.missing_lower_q2_orbits == 0)
                        ++exact_decks;
                    if (resident_better(cm, best_metrics, cfg)) {
                        best = std::move(candidate);
                        best_metrics = std::move(cm);
                        write_candidate(cat, best, best_metrics, cfg.output, cfg.seed, static_cast<int>(subset));
                        std::cerr << "CUBE_BEST subset=" << subset << " " << metrics_string(best_metrics) << "\n";
                    }
                }
                std::cout << "TARGET_CUBE_DONE subsets=" << total
                          << " resident=" << resident
                          << " connected_resident=" << connected_resident
                          << " exact_decks=" << exact_decks
                          << " best=" << metrics_string(best_metrics)
                          << " output=" << cfg.output << "\n";
                return 0;
            }
        }
        long long current_energy = energy(current_metrics, cfg);
        auto started = std::chrono::steady_clock::now();
        long long exact_cycles = 0;
        long long accepted = 0;
        std::uniform_real_distribution<double> unit(0.0, 1.0);
        auto accept_energy = [&](long long proposed, const Metrics &pm) {
            if (cfg.hard_residence && pm.residence_shortfall != 0) return false;
            if (proposed <= current_energy) return true;
            if (cfg.temperature <= 0.0) return false;
            return unit(rng) < std::exp(static_cast<double>(current_energy - proposed) / cfg.temperature);
        };

        for (int iteration = 1; iteration <= cfg.iterations; ++iteration) {
            if (cfg.seconds > 0 && std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count() >= cfg.seconds)
                break;
            MatchingDecomposition dec = decompose_factor(cat, current, rng);
            auto proposal_matching = preferred_perfect_matching(cat, dec, current_metrics, cfg, rng);
            auto cycles = matching_difference_cycles(cat, dec.m1, proposal_matching);
            std::shuffle(cycles.begin(), cycles.end(), rng);

            // First test the genuinely global union.  It is itself an exact
            // kernel move, even when none of its alternating components is
            // individually useful.
            if (cycles.size() > 1) {
                State proposal = current;
                for (const auto &cycle : cycles) toggle_cycle(proposal, cycle);
                Metrics pm = evaluate(cat, proposal);
                if (!pm.invariant_ok) throw std::runtime_error("global matching move left fiber");
                long long pe = energy(pm, cfg);
                if (accept_energy(pe, pm)) {
                    current = std::move(proposal);
                    current_metrics = std::move(pm);
                    current_energy = pe;
                    ++accepted;
                    if (resident_better(current_metrics, best_metrics, cfg)) {
                        best = current;
                        best_metrics = current_metrics;
                        write_candidate(cat, best, best_metrics, cfg.output, cfg.seed, iteration);
                        std::cerr << "BEST iter=" << iteration << " " << metrics_string(best_metrics) << "\n";
                    }
                    continue;
                }
            }

            // Then scan the exact alternating components independently.  The
            // cycles are vertex-disjoint within this matching difference, so
            // accepted toggles do not invalidate the remaining toggles.
            for (const auto &cycle : cycles) {
                ++exact_cycles;
                toggle_cycle(current, cycle);
                Metrics candidate = evaluate(cat, current);
                if (!candidate.invariant_ok) throw std::runtime_error("alternating cycle left fiber");
                long long ce = energy(candidate, cfg);
                bool take = accept_energy(ce, candidate);
                if (take) {
                    current_metrics = std::move(candidate);
                    current_energy = ce;
                    ++accepted;
                    if (resident_better(current_metrics, best_metrics, cfg)) {
                        best = current;
                        best_metrics = current_metrics;
                        write_candidate(cat, best, best_metrics, cfg.output, cfg.seed, iteration);
                        std::cerr << "BEST iter=" << iteration << " " << metrics_string(best_metrics) << "\n";
                    }
                } else {
                    toggle_cycle(current, cycle);
                }
            }
            if (iteration % 100 == 0) {
                double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count();
                std::cerr << "PROGRESS iter=" << iteration << " cycles=" << exact_cycles
                          << " accepted=" << accepted << " seconds=" << elapsed
                          << " current=" << metrics_string(current_metrics) << "\n";
            }
        }
        double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count();
        std::cout << "DONE seconds=" << elapsed << " exact_cycles=" << exact_cycles
                  << " accepted=" << accepted << " best=" << metrics_string(best_metrics)
                  << " output=" << cfg.output << "\n";
        return 0;
    } catch (const std::exception &error) {
        std::cerr << "ERROR " << error.what() << "\n";
        return 2;
    }
}
