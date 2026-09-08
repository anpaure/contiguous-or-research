#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

// Standalone fresh-seed search. Text checkpoints preserve the two matching
// colours; JSON choices are uncoloured, stable explicit (lower, added, added).
// No physical expansion occurs in the proposal loop.
namespace {
constexpr int K = 17, R = 9, M = 8, D = 3, N = 1430, W = 24310;
constexpr int FULL = (1 << K) - 1, A = 9 * N;
constexpr std::array<int, 4> TARGETS{1144, 1144, 728, 728};
constexpr std::array<int, 4> RANKS{10, 7, 11, 6};
using Matching = std::array<int, N>;
using Clock = std::chrono::steady_clock;

void require(bool ok, const char *message) {
    if (!ok) throw std::runtime_error(message);
}
int mod(int x) { x %= K; return x < 0 ? x + K : x; }
int rot(int x, int s) {
    s = mod(s);
    unsigned value = static_cast<unsigned>(x);
    return s ? static_cast<int>(((value << s) | (value >> (K - s))) & FULL) : x;
}
int pc(int x) { return std::popcount(static_cast<unsigned>(x)); }

struct Arc { int l, v, added, phase; };
struct Catalogue {
    std::vector<int> canon, phase, label;
    std::array<std::vector<int>, K + 1> reps;
    std::vector<Arc> arcs;
    std::array<std::array<int, 9>, N> by_l{};
    std::array<std::vector<int>, N> by_v;
    Catalogue() : canon(FULL + 1, -1), phase(FULL + 1), label(FULL + 1) {
        for (int x = 0; x <= FULL; ++x) {
            if (canon[x] >= 0) continue;
            int rank = pc(x), id = static_cast<int>(reps[rank].size());
            reps[rank].push_back(x);
            for (int s = 0; s < K; ++s) {
                int y = rot(x, s);
                if (canon[y] < 0) { canon[y] = x; phase[y] = s; label[y] = id; }
            }
        }
        require(reps[M].size() == N && reps[R].size() == N, "central orbit counts");
        for (int t = 0; t < 4; ++t)
            require(reps[RANKS[t]].size() == static_cast<size_t>(TARGETS[t]), "shadow orbit counts");
        for (int l = 0; l < N; ++l) {
            int slot = 0;
            for (int a = 0; a < K; ++a) {
                if (reps[M][l] & (1 << a)) continue;
                int middle = reps[M][l] | (1 << a), v = label[middle];
                int e = static_cast<int>(arcs.size());
                arcs.push_back({l, v, a, phase[middle]});
                by_l[l][slot++] = e;
                by_v[v].push_back(e);
                require(middle == rot(reps[R][v], phase[middle]), "incidence phase");
            }
            require(slot == 9, "left regularity");
        }
        require(arcs.size() == A, "incidence count");
        for (const auto &row : by_v) require(row.size() == 9, "right regularity");
    }
};

struct Factor { Matching base{}, p{}; };
struct Topology {
    int quotient = 0, components = 0, minimum = W, maximum = 0, zero_voltage = 0;
    int constant_bad3 = 0;
    std::vector<int> lengths;
    bool operator==(const Topology &) const = default;
};
struct Feature {
    std::array<int, 4> label{};
    int bad2 = 0, bad3 = 0;
    bool operator==(const Feature &) const = default;
};
struct Score {
    std::array<int, 4> missing = TARGETS, pairs{}, invalid{};
    int bad2 = 0, bad3 = 0;
    bool operator==(const Score &) const = default;
};
struct Desc {
    int next = -1, shift = 0, ins = -1, del = -1;
    int u1 = -1, l2 = -1, umask = 0, lmask = 0;
};

struct Engine {
    const Catalogue &cat;
    Factor f;
    Matching base_inv{}, p_inv{}, pred{};
    std::array<Desc, A> desc{};
    std::array<int, N> middle{};
    std::array<Feature, N> feature{};
    std::array<std::vector<int>, 4> loads;
    std::array<std::vector<int>, N> allowed;
    Score score;
    Topology top;

    explicit Engine(const Catalogue &c, const Factor &state) : cat(c), f(state) { rebuild(); }
    void check_factor() const {
        std::array<int, N> b{}, p{};
        for (int l = 0; l < N; ++l) {
            int x = f.base[l], y = f.p[l];
            require(x >= 0 && x < A && y >= 0 && y < A && x != y, "distinct incidence ids");
            require(cat.arcs[x].l == l && cat.arcs[y].l == l, "incidence row");
            require(cat.arcs[x].v != cat.arcs[y].v, "quotient loops are excluded");
            ++b[cat.arcs[x].v]; ++p[cat.arcs[y].v];
        }
        for (int v = 0; v < N; ++v) require(b[v] == 1 && p[v] == 1, "two disjoint perfect matchings");
    }
    Feature at(int l) const {
        const Desc &a = desc[f.p[l]];
        const Desc &b = desc[f.p[a.next]];
        const Desc &c = desc[f.p[b.next]];
        Feature out;
        int u = a.umask | rot(b.umask, a.shift);
        int low = a.lmask & rot(b.lmask, a.shift);
        out.label = {a.u1, a.l2, pc(u) == 11 ? cat.label[u] : -1,
                     pc(low) == 6 ? cat.label[low] : -1};
        out.bad2 = a.ins == mod(b.del + a.shift);
        out.bad3 = a.ins == mod(c.del + a.shift + b.shift);
        return out;
    }
    void adjust_label(int t, int label, int sign) {
        if (label < 0) { score.invalid[t] += sign; return; }
        int &load = loads[t][label];
        if (sign > 0) {
            score.missing[t] -= load == 0;
            score.pairs[t] += load;
            ++load;
        } else {
            require(load > 0, "negative coverage load");
            --load;
            score.pairs[t] -= load;
            score.missing[t] += load == 0;
        }
    }
    void replace(int l, const Feature &next) {
        const Feature old = feature[l];
        for (int t = 0; t < 4; ++t) if (old.label[t] != next.label[t]) {
            adjust_label(t, old.label[t], -1);
            adjust_label(t, next.label[t], 1);
        }
        score.bad2 += next.bad2 - old.bad2;
        score.bad3 += next.bad3 - old.bad3;
        feature[l] = next;
    }
    Topology topology() const {
        Topology out;
        std::array<bool, N> seen{};
        for (int start = 0; start < N; ++start) {
            if (seen[start]) continue;
            int l = start, z = 0, count = 0, common = FULL;
            do {
                require(!seen[l], "successor is not a permutation");
                seen[l] = true;
                common &= rot(middle[l], z);
                ++count;
                const Desc &e = desc[f.p[l]];
                z = mod(z + e.shift); l = e.next;
            } while (l != start);
            int copies = std::gcd(K, z), length = count * K / copies;
            require(length >= 3, "physical cycle shorter than three");
            ++out.quotient;
            out.zero_voltage += z == 0;
            out.components += copies;
            out.minimum = std::min(out.minimum, length);
            out.maximum = std::max(out.maximum, length);
            for (int j = 0; j < copies; ++j) out.lengths.push_back(length);
            // Entry/deletion equalities count all nonconstant positive runs.
            // A voltage-zero triangle also has constant length-three traces.
            if (length == 3) out.constant_bad3 += pc(common);
        }
        std::sort(out.lengths.begin(), out.lengths.end(), std::greater<int>());
        return out;
    }
    void rebuild() {
        check_factor();
        for (int l = 0; l < N; ++l) {
            base_inv[cat.arcs[f.base[l]].v] = l;
            p_inv[cat.arcs[f.p[l]].v] = l;
            middle[l] = cat.reps[M][l] | (1 << cat.arcs[f.base[l]].added);
        }
        for (int l = 0; l < N; ++l) {
            allowed[l].clear();
            for (int e : cat.by_l[l]) {
                if (e == f.base[l]) continue;
                const Arc &arc = cat.arcs[e];
                int j = base_inv[arc.v], s = mod(arc.phase - cat.arcs[f.base[j]].phase);
                int next = rot(cat.reps[M][j], s), low = cat.reps[M][l];
                int ins = next & ~low, del = low & ~next;
                require(pc(ins) == 1 && pc(del) == 1, "lower Johnson step");
                int u = middle[l] | (1 << arc.added), v = low & next;
                require(pc(u) == 10 && pc(v) == 7, "pair shadow ranks");
                desc[e] = {j, s, std::countr_zero(static_cast<unsigned>(ins)),
                           std::countr_zero(static_cast<unsigned>(del)),
                           cat.label[u], cat.label[v], u, v};
                if (arc.v != cat.arcs[f.base[l]].v) allowed[l].push_back(e);
            }
            pred[desc[f.p[l]].next] = l;
        }
        score = Score{};
        for (int t = 0; t < 4; ++t) loads[t].assign(TARGETS[t], 0);
        for (int l = 0; l < N; ++l) {
            feature[l] = at(l);
            for (int t = 0; t < 4; ++t) adjust_label(t, feature[l].label[t], 1);
            score.bad2 += feature[l].bad2; score.bad3 += feature[l].bad3;
        }
        top = topology();
    }
    void rebase(std::mt19937_64 &rng) {
        std::array<bool, N> seen{};
        for (int start = 0; start < N; ++start) {
            if (seen[start]) continue;
            bool flip = rng() & 1;
            int l = start;
            do {
                seen[l] = true;
                int next = desc[f.p[l]].next;
                if (flip) std::swap(f.base[l], f.p[l]);
                l = next;
            } while (l != start);
        }
        rebuild();
    }
};

using Orders = std::array<std::vector<int>, N>;
bool matching(const Catalogue &cat, const Orders &order, Matching &out,
              const Matching *fixed = nullptr) {
    Matching owner, stamp{};
    std::array<bool, N> locked{};
    owner.fill(-1); out.fill(-1);
    if (fixed) for (int l = 0; l < N; ++l) if ((*fixed)[l] >= 0) {
        int e = (*fixed)[l], v = cat.arcs[e].v;
        require(owner[v] < 0, "forced matching conflict");
        owner[v] = l; out[l] = e; locked[l] = true;
    }
    int epoch = 0;
    auto augment = [&](auto &&self, int l) -> bool {
        for (int e : order[l]) {
            int v = cat.arcs[e].v;
            if (stamp[v] == epoch) continue;
            stamp[v] = epoch;
            if (owner[v] < 0 || (!locked[owner[v]] && self(self, owner[v]))) {
                owner[v] = l; out[l] = e; return true;
            }
        }
        return false;
    };
    // Edge orders, not just row order, are randomized by callers.
    for (int l = 0; l < N; ++l) if (!locked[l]) {
        ++epoch;
        if (!augment(augment, l)) return false;
    }
    return true;
}

Factor fresh(const Catalogue &cat, std::mt19937_64 &rng, bool triangle = false) {
    Matching fixed0, fixed1;
    fixed0.fill(-1); fixed1.fill(-1);
    if (triangle) {
        // Force a genuine physical triangle, then complete its two colours.
        for (;;) {
            int common = cat.reps[7][rng() % cat.reps[7].size()];
            std::vector<int> extra;
            for (int a = 0; a < K; ++a) if (!(common & (1 << a))) extra.push_back(a);
            std::shuffle(extra.begin(), extra.end(), rng);
            std::array<int, 3> low{}, mid{};
            for (int i = 0; i < 3; ++i) {
                low[i] = common | (1 << extra[i]);
                mid[i] = low[i] | (1 << extra[(i + 1) % 3]);
            }
            if (cat.label[low[0]] == cat.label[low[1]] || cat.label[low[0]] == cat.label[low[2]] ||
                cat.label[low[1]] == cat.label[low[2]] || cat.label[mid[0]] == cat.label[mid[1]] ||
                cat.label[mid[0]] == cat.label[mid[2]] || cat.label[mid[1]] == cat.label[mid[2]]) continue;
            for (int i = 0; i < 3; ++i) {
                int l = cat.label[low[i]], s = cat.phase[low[i]];
                int a = mod(extra[(i + 2) % 3] - s), b = mod(extra[(i + 1) % 3] - s);
                for (int e : cat.by_l[l]) {
                    if (cat.arcs[e].added == a) fixed0[l] = e;
                    if (cat.arcs[e].added == b) fixed1[l] = e;
                }
                require(fixed0[l] >= 0 && fixed1[l] >= 0, "forced triangle normalization");
            }
            break;
        }
    }
    for (int attempt = 0; attempt < 100; ++attempt) {
        Factor f;
        Orders order;
        for (int l = 0; l < N; ++l) {
            order[l].assign(cat.by_l[l].begin(), cat.by_l[l].end());
            std::shuffle(order[l].begin(), order[l].end(), rng);
        }
        if (!matching(cat, order, f.base, &fixed0)) continue;
        for (int l = 0; l < N; ++l) {
            order[l].clear();
            for (int e : cat.by_l[l])
                if (cat.arcs[e].v != cat.arcs[f.base[l]].v) order[l].push_back(e);
            std::shuffle(order[l].begin(), order[l].end(), rng);
        }
        if (matching(cat, order, f.p, &fixed1)) return f;
    }
    throw std::runtime_error("failed fresh matching completion");
}

struct Move {
    std::vector<int> rows, edges, old_edges, affected;
    std::vector<Feature> old_feature;
    Matching marks{};
    int epoch = 0;
    Move() {
        rows.reserve(N); edges.reserve(N); old_edges.reserve(N);
        affected.reserve(N); old_feature.reserve(N);
    }
    void apply(Engine &e) {
        affected.clear(); old_edges.clear(); old_feature.clear();
        if (++epoch == 1000000000) { marks.fill(0); epoch = 1; }
        auto touch = [&](int l) {
            if (marks[l] != epoch) { marks[l] = epoch; affected.push_back(l); }
        };
        auto predecessors = [&]() {
            for (int l : rows) { touch(l); touch(e.pred[l]); touch(e.pred[e.pred[l]]); }
        };
        predecessors();
        for (size_t i = 0; i < rows.size(); ++i) {
            int l = rows[i], edge = edges[i];
            old_edges.push_back(e.f.p[l]);
            e.f.p[l] = edge;
            e.p_inv[e.cat.arcs[edge].v] = l;
            e.pred[e.desc[edge].next] = l;
        }
        predecessors();
        for (int l : affected) { old_feature.push_back(e.feature[l]); e.replace(l, e.at(l)); }
    }
    void undo(Engine &e) {
        for (size_t i = 0; i < affected.size(); ++i) e.replace(affected[i], old_feature[i]);
        for (size_t i = 0; i < rows.size(); ++i) {
            int l = rows[i], edge = old_edges[i];
            e.f.p[l] = edge;
            e.p_inv[e.cat.arcs[edge].v] = l;
            e.pred[e.desc[edge].next] = l;
        }
    }
};

struct Proposer {
    Matching mark{}, position{};
    int epoch = 0;
    std::array<int, N> walk{}, edge_walk{};
    bool random_cycle(Engine &e, std::mt19937_64 &rng, Move &move) {
        if (++epoch == 1000000000) { mark.fill(0); epoch = 1; }
        int l = rng() % N;
        if ((rng() & 3) != 0) for (int tries = 0; tries < 6; ++tries) {
            const auto &f = e.feature[l];
            if (f.bad2 || f.bad3 || e.loads[0][f.label[0]] > 1) break;
            l = rng() % N;
        }
        int cap = (rng() & 7) == 0 ? 80 : 28;
        for (int step = 0; step < cap; ++step) {
            mark[l] = epoch; position[l] = step; walk[step] = l;
            const auto &options = e.allowed[l];
            int edge = -1, offset = rng() % options.size();
            // Prefer a short closure, but keep all directed walk proposals.
            size_t slot = offset;
            for (size_t j = 0; j < options.size(); ++j) {
                int candidate = options[slot];
                if (++slot == options.size()) slot = 0;
                if (candidate == e.f.p[l]) continue;
                if (edge < 0) edge = candidate;
                int target = e.p_inv[e.cat.arcs[candidate].v];
                if (mark[target] == epoch && step - position[target] < 10) { edge = candidate; break; }
            }
            if (edge < 0) return false;
            edge_walk[step] = edge;
            int next = e.p_inv[e.cat.arcs[edge].v];
            if (mark[next] == epoch) {
                int begin = position[next];
                move.rows.assign(walk.begin() + begin, walk.begin() + step + 1);
                move.edges.assign(edge_walk.begin() + begin, edge_walk.begin() + step + 1);
                return true;
            }
            l = next;
        }
        return false;
    }
    std::vector<std::pair<std::vector<int>, std::vector<int>>> preferred(
        Engine &e, std::mt19937_64 &rng, double res_weight, double u1_weight,
        double l2_weight, double noise) {
        Orders order;
        for (int l = 0; l < N; ++l) {
            std::vector<std::pair<double, int>> ranked;
            for (int edge : e.allowed[l]) {
                const Desc &a = e.desc[edge], &b = e.desc[e.f.p[a.next]];
                const Desc &c = e.desc[e.f.p[b.next]];
                double value = noise * (static_cast<double>(rng() >> 11) / 9007199254740992.0 - 0.5);
                value += u1_weight * (e.loads[0][a.u1] == 0 ? 2.0 : -0.12 * e.loads[0][a.u1]);
                value += l2_weight * (e.loads[1][a.l2] == 0 ? 2.0 : -0.12 * e.loads[1][a.l2]);
                value -= res_weight * (2 * (a.ins == mod(b.del + a.shift)) +
                                        (a.ins == mod(c.del + a.shift + b.shift)));
                if (edge == e.f.p[l]) value += 2.0;
                ranked.emplace_back(value, edge);
            }
            std::sort(ranked.begin(), ranked.end(), std::greater<std::pair<double, int>>());
            for (auto [weight, edge] : ranked) { (void)weight; order[l].push_back(edge); }
        }
        Matching next;
        require(matching(e.cat, order, next), "preferred perfect matching");
        std::array<bool, N> seen{};
        std::vector<std::pair<std::vector<int>, std::vector<int>>> cycles;
        for (int start = 0; start < N; ++start) {
            if (seen[start] || next[start] == e.f.p[start]) continue;
            cycles.emplace_back();
            auto &[rows, edges] = cycles.back();
            int l = start;
            do {
                require(!seen[l], "matching difference cycle"); seen[l] = true;
                rows.push_back(l); edges.push_back(next[l]);
                l = e.p_inv[e.cat.arcs[next[l]].v];
            } while (l != start);
        }
        std::shuffle(cycles.begin(), cycles.end(), rng);
        return cycles;
    }
};

struct Physical {
    std::array<std::vector<int>, 4> loads;
    std::array<int, K + 1> upper_missing{};
    std::array<int, 4> short_runs{};
    std::vector<int> lengths;
    int minimum_run = W, shortfall = 0, zero_gaps_short = 0;
};

Physical physical(const Catalogue &cat, const Factor &f) {
    Physical out;
    for (int t = 0; t < 4; ++t) out.loads[t].assign(TARGETS[t], 0);
    std::vector<std::array<int, 2>> adjacency(FULL + 1);
    std::vector<int> degree(FULL + 1), facets(FULL + 1);
    std::vector<bool> seen(FULL + 1), upper(FULL + 1);
    for (int l = 0; l < N; ++l) {
        int low = cat.reps[M][l];
        int a = low | (1 << cat.arcs[f.base[l]].added);
        int b = low | (1 << cat.arcs[f.p[l]].added);
        for (int s = 0; s < K; ++s) {
            int u = rot(a, s), v = rot(b, s);
            require(u != v && degree[u] < 2 && degree[v] < 2, "physical degree overflow");
            adjacency[u][degree[u]++] = v; adjacency[v][degree[v]++] = u;
            ++facets[u & v];
        }
    }
    int owners = 0, lower_count = 0;
    for (int x = 0; x <= FULL; ++x) {
        if (pc(x) == R) { require(degree[x] == 2, "missing physical owner"); ++owners; }
        else require(degree[x] == 0, "wrong-rank owner");
        if (pc(x) == M) { require(facets[x] == 1, "physical lower-q1 not once"); ++lower_count; }
        else require(facets[x] == 0, "wrong-rank facet");
    }
    require(owners == W && lower_count == W, "physical masses");
    for (int start = 0; start <= FULL; ++start) {
        if (!degree[start] || seen[start]) continue;
        std::vector<int> cycle;
        int current = start, previous = -1, total_union = 0;
        do {
            require(!seen[current], "physical cycle failed to close");
            seen[current] = true; cycle.push_back(current); total_union |= current;
            const auto &a = adjacency[current];
            int next = previous < 0 ? std::min(a[0], a[1]) : (a[0] == previous ? a[1] : a[0]);
            previous = current; current = next;
        } while (current != start);
        int n = static_cast<int>(cycle.size());
        require(n >= 3, "physical simple cycle"); out.lengths.push_back(n);
        for (int i = 0; i < n; ++i) {
            int a = cycle[i], b = cycle[(i + 1) % n], c = cycle[(i + 2) % n], d = cycle[(i + 3) % n];
            std::array<int, 4> masks{a | b, a & b & c, a | b | c, a & b & c & d};
            for (int t = 0; t < 4; ++t)
                if (pc(masks[t]) == RANKS[t]) ++out.loads[t][cat.label[masks[t]]];
            int u = a;
            for (int age = 1; age < n; ++age) {
                u |= cycle[(i + age) % n];
                if (pc(u) > R) upper[cat.canon[u]] = true;
                if (u == total_union) break;
            }
        }
        for (int bit = 0; bit < K; ++bit) for (int positive = 0; positive < 2; ++positive) {
            int zero = -1;
            for (int i = 0; i < n; ++i) if (((cycle[i] >> bit) & 1) != positive) { zero = i; break; }
            auto record = [&](int run) {
                if (!run) return;
                if (positive) {
                    out.minimum_run = std::min(out.minimum_run, run);
                    if (run <= D) { ++out.short_runs[run]; out.shortfall += D + 1 - run; }
                } else if (run <= D) ++out.zero_gaps_short;
            };
            if (zero < 0) { record(n); continue; }
            int run = 0;
            for (int step = 1; step <= n; ++step) {
                if (((cycle[(zero + step) % n] >> bit) & 1) == positive) ++run;
                else { record(run); run = 0; }
            }
        }
    }
    std::sort(out.lengths.begin(), out.lengths.end(), std::greater<int>());
    for (int rank = R + 1; rank <= K; ++rank)
        for (int rep : cat.reps[rank]) out.upper_missing[rank] += !upper[rep];
    return out;
}

void compare_physical(const Engine &e, const Physical &p) {
    require(p.lengths == e.top.lengths, "quotient voltage vs physical topology");
    require(p.short_runs[1] == 0, "middle positive run one cannot occur");
    require(p.short_runs[2] == K * e.score.bad2, "residence length-two equality");
    require(p.short_runs[3] == K * (e.score.bad3 + e.top.constant_bad3), "residence length-three equality");
    require(p.shortfall == K * (2 * e.score.bad2 + e.score.bad3 + e.top.constant_bad3), "residence shortfall");
    for (int t = 0; t < 4; ++t) for (int label = 0; label < TARGETS[t]; ++label)
        require(p.loads[t][label] == K * e.loads[t][label], "physical vs quotient shadow loads");
    require(p.upper_missing[10] == e.score.missing[0], "arbitrary-width U1 agreement");
    require(p.upper_missing[11] == e.score.missing[2], "arbitrary-width U2 agreement");
}

Factor read_factor(const Catalogue &cat, const std::string &path) {
    std::ifstream input(path);
    std::string magic; int k = 0, n = 0, w = 0, d = 0;
    input >> magic >> k >> n >> w >> d;
    require(magic == "K17QF1" && k == K && n == N && w == W && d == D, "resume header");
    Factor f; f.base.fill(-1); f.p.fill(-1);
    for (int row = 0; row < N; ++row) {
        int low = -1, a = -1, b = -1;
        input >> low >> a >> b;
        require(bool(input) && low >= 0 && low <= FULL && pc(low) == M && cat.canon[low] == low, "resume lower");
        int l = cat.label[low];
        require(f.base[l] < 0 && a != b, "duplicate resume lower or incidence");
        for (int edge : cat.by_l[l]) {
            if (cat.arcs[edge].added == a) f.base[l] = edge;
            if (cat.arcs[edge].added == b) f.p[l] = edge;
        }
        require(f.base[l] >= 0 && f.p[l] >= 0, "resume added coordinates");
    }
    std::string extra; require(!(input >> extra), "trailing resume data");
    return f;
}

void json_score(std::ostream &out, const Score &s, const Topology &t) {
    out << "{\"bad2_orbits\":" << s.bad2 << ",\"bad3_orbits\":" << s.bad3 + t.constant_bad3
        << ",\"constant_bad3_orbits\":" << t.constant_bad3
        << ",\"residence_shortfall_orbits\":" << 2 * s.bad2 + s.bad3 + t.constant_bad3
        << ",\"missing_orbits\":[";
    for (int i = 0; i < 4; ++i) out << (i ? "," : "") << s.missing[i];
    out << "],\"pair_collisions\":[";
    for (int i = 0; i < 4; ++i) out << (i ? "," : "") << s.pairs[i];
    out << "],\"invalid_rank_starts\":[";
    for (int i = 0; i < 4; ++i) out << (i ? "," : "") << s.invalid[i];
    out << "],\"quotient_cycles\":" << t.quotient << ",\"physical_cycles\":" << t.components
        << ",\"zero_voltage_cycles\":" << t.zero_voltage << ",\"min_component\":" << t.minimum
        << ",\"max_component\":" << t.maximum << ",\"quotient_loops\":0}";
}

void save(const Catalogue &cat, const Factor &f, const Score &s, const Topology &t,
          const std::string &prefix, uint64_t seed, uint64_t iteration, const Physical *audit = nullptr) {
    std::ofstream body(prefix + ".txt"); require(bool(body), "open checkpoint body");
    body << "K17QF1 17 1430 24310 3\n";
    for (int l = 0; l < N; ++l)
        body << cat.reps[M][l] << ' ' << cat.arcs[f.base[l]].added << ' ' << cat.arcs[f.p[l]].added << '\n';
    require(bool(body), "write checkpoint body");
    std::ofstream out(prefix + ".json"); require(bool(out), "open checkpoint JSON");
    out << "{\n\"schema\":\"k17-quotient-factor-f6c2e-v1\",\"k\":17,\"r\":9,\"d\":3,\"N\":1430,\"W\":24310,\n"
        << "\"seed\":" << seed << ",\"iteration\":" << iteration
        << ",\"deck_order\":[\"U1\",\"L2\",\"U2\",\"L3\"],\n\"quotient_score\":";
    json_score(out, s, t);
    if (audit) {
        out << ",\n\"physical_audit\":{\"degree2_owners\":24310,\"once_only_rank8_facets\":24310,"
            << "\"positive_bad_runs_by_length\":[" << audit->short_runs[1] << ',' << audit->short_runs[2]
            << ',' << audit->short_runs[3] << "],\"residence_shortfall\":" << audit->shortfall
            << ",\"minimum_positive_run\":" << audit->minimum_run
            << ",\"short_zero_gaps_not_forbidden\":" << audit->zero_gaps_short
            << ",\"all_width_upper_missing_orbits_by_rank_10_to_17\":[";
        for (int rank = 10; rank <= 17; ++rank) out << (rank == 10 ? "" : ",") << audit->upper_missing[rank];
        out << "],\"physical_cycle_lengths\":[";
        for (size_t i = 0; i < audit->lengths.size(); ++i) out << (i ? "," : "") << audit->lengths[i];
        out << "]}";
    }
    out << ",\n\"choices\":[\n";
    for (int l = 0; l < N; ++l) {
        int a = cat.arcs[f.base[l]].added, b = cat.arcs[f.p[l]].added;
        if (a > b) std::swap(a, b);
        out << '[' << cat.reps[M][l] << ',' << a << ',' << b << ']' << (l + 1 == N ? "\n" : ",\n");
    }
    out << "]\n}\n"; require(bool(out), "write checkpoint JSON");
}

struct Config {
    uint64_t seed = 1, max_moves = 0;
    double seconds = 240, res = 1.5, u1 = 3.0, l2 = 0.5, u2 = 0.2, l3 = 0.2;
    double collisions = 0.025, component = 0.015, hot = 2.0, cold = 0.12, epoch_seconds = 35;
    int self_test = 0;
    std::string output, resume;
    bool audit_only = false;
};
double local_energy(const Score &s, const Config &c) {
    return c.res * (2 * s.bad2 + s.bad3) + c.u1 * s.missing[0] + c.l2 * s.missing[1] +
           c.u2 * s.missing[2] + c.l3 * s.missing[3] +
           c.collisions * (s.pairs[0] + 0.4 * s.pairs[1]);
}
double topology_energy(const Topology &t, const Config &c) {
    return c.component * (t.components - 1) + c.res * t.constant_bad3;
}

struct Best {
    Factor f;
    Score s;
    Topology t;
    uint64_t iteration = 0;
};
int shortfall(const Best &b) { return 2 * b.s.bad2 + b.s.bad3 + b.t.constant_bad3; }
double energy(const Best &b, const Config &c) { return local_energy(b.s, c) + topology_energy(b.t, c); }

void self_test(const Catalogue &cat, const Config &cfg) {
    std::mt19937_64 rng(cfg.seed);
    uint64_t deltas = 0, physical_checks = 0, undos = 0, parallel_moves = 0, rebases = 0, global_moves = 0;
    Proposer proposer; Move move;
    for (int trial = 0; trial < cfg.self_test; ++trial) {
        Engine e(cat, fresh(cat, rng, trial == 0));
        if (trial == 0) require(e.top.constant_bad3 >= 7, "forced constant triangle test");
        compare_physical(e, physical(cat, e.f)); ++physical_checks;
        for (int i = 0; i < 400; ++i) {
            while (!proposer.random_cycle(e, rng, move)) {}
            parallel_moves += move.rows.size() == 1;
            Factor old = e.f; Score old_score = e.score; Topology old_top = e.top;
            move.apply(e);
            Engine full(cat, e.f);
            require(e.score == full.score && e.loads == full.loads && e.feature == full.feature &&
                    e.pred == full.pred && e.p_inv == full.p_inv, "delta vs full recomputation");
            e.top = e.topology(); require(e.top == full.top, "incremental successor topology"); ++deltas;
            if (i % 40 == 0) { compare_physical(e, physical(cat, e.f)); ++physical_checks; }
            if (rng() & 1) {
                move.undo(e); e.top = old_top; ++undos;
                require(e.f.base == old.base && e.f.p == old.p && e.score == old_score, "rollback score/body");
                Engine restored(cat, e.f);
                require(e.loads == restored.loads && e.feature == restored.feature &&
                        e.pred == restored.pred && e.p_inv == restored.p_inv, "rollback full state");
            }
            if (i % 67 == 0) {
                auto missing = e.score.missing, pairs = e.score.pairs, invalid = e.score.invalid;
                int b2 = e.score.bad2, b3 = e.score.bad3 + e.top.constant_bad3;
                auto lengths = e.top.lengths;
                e.rebase(rng); ++rebases;
                require(e.score.missing == missing && e.score.pairs == pairs && e.score.invalid == invalid &&
                        e.score.bad2 == b2 && e.score.bad3 + e.top.constant_bad3 == b3 && e.top.lengths == lengths,
                        "recolouring preserves the factor metrics");
            }
        }
        auto cycles = proposer.preferred(e, rng, cfg.res, cfg.u1, cfg.l2, 5.0);
        for (auto &[rows, edges] : cycles) {
            move.rows = rows; move.edges = edges; move.apply(e);
            Engine full(cat, e.f);
            require(e.score == full.score && e.loads == full.loads, "preferred matching difference delta");
            e.top = full.top; ++deltas; ++global_moves;
        }
        compare_physical(e, physical(cat, e.f)); ++physical_checks;
    }
    require(parallel_moves > 0 && global_moves > 0 && undos > 0, "move family test coverage");
    std::cout << "SELF_TEST_PASS factors=" << cfg.self_test << " delta_checks=" << deltas
              << " physical_checks=" << physical_checks << " rollback_checks=" << undos
              << " support1_parallel=" << parallel_moves << " recolourings=" << rebases
              << " preferred_difference_cycles=" << global_moves << " forced_triangle=1\n";
}

void search(const Catalogue &cat, const Config &cfg) {
    require(!cfg.output.empty(), "--output prefix is required");
    std::mt19937_64 rng(cfg.seed);
    Engine e(cat, cfg.resume.empty() ? fresh(cat, rng) : read_factor(cat, cfg.resume));
    auto initial_audit = physical(cat, e.f); compare_physical(e, initial_audit);
    save(cat, e.f, e.score, e.top, cfg.output + ".initial", cfg.seed, 0, &initial_audit);
    if (cfg.audit_only) { std::cout << "AUDIT_PASS "; json_score(std::cout, e.score, e.top); std::cout << '\n'; return; }
    std::array<Best, 3> best;
    for (auto &b : best) b = {e.f, e.score, e.top, 0};
    const std::array<std::string, 3> names{"best", "residence", "u1"};
    auto checkpoint = [&](bool final) {
        for (int i = 0; i < 3; ++i) {
            const auto &b = best[i];
            if (final) {
                Engine exact(cat, b.f); auto p = physical(cat, b.f); compare_physical(exact, p);
                require(exact.score == b.s && exact.top == b.t, "saved best dirty state agrees");
                save(cat, b.f, b.s, b.t, cfg.output + "." + names[i], cfg.seed, b.iteration, &p);
            } else save(cat, b.f, b.s, b.t, cfg.output + "." + names[i], cfg.seed, b.iteration);
        }
    };
    checkpoint(false);
    std::cout << "INITIAL "; json_score(std::cout, e.score, e.top); std::cout << std::endl;
    auto started = Clock::now();
    uint64_t attempts = 0, proposals = 0, accepted = 0, support1 = 0, globals = 0, recolourings = 0, restarts = 0;
    double elapsed = 0, last_save = 0, last_log = 0;
    int last_epoch = 0;
    bool dirty = false;
    Proposer proposer; Move move;
    auto unit = [&]() { return (static_cast<double>(rng() >> 11) + 0.5) / 9007199254740992.0; };
    auto consider = [&](double temperature) {
        ++proposals; support1 += move.rows.size() == 1;
        double before = local_energy(e.score, cfg);
        move.apply(e);
        double delta = local_energy(e.score, cfg) - before;
        // Delayed acceptance: O(N) voltage topology is evaluated only after
        // the O(changed support) energy filter, with its own Metropolis test.
        if (delta > 0 && unit() >= std::exp(-delta / temperature)) { move.undo(e); return; }
        Topology next = e.topology();
        double dt = topology_energy(next, cfg) - topology_energy(e.top, cfg);
        if (dt > 0 && unit() >= std::exp(-dt / temperature)) { move.undo(e); return; }
        e.top = std::move(next); ++accepted;
        Best candidate{e.f, e.score, e.top, attempts};
        double value = energy(candidate, cfg);
        bool improve0 = value < energy(best[0], cfg) - 1e-9;
        bool improve1 = std::tuple(shortfall(candidate), candidate.s.missing[0], value) <
                        std::tuple(shortfall(best[1]), best[1].s.missing[0], energy(best[1], cfg));
        bool improve2 = std::tuple(candidate.s.missing[0], shortfall(candidate), value) <
                        std::tuple(best[2].s.missing[0], shortfall(best[2]), energy(best[2], cfg));
        if (improve0) best[0] = candidate;
        if (improve1) best[1] = candidate;
        if (improve2) best[2] = candidate;
        dirty |= improve0 || improve1 || improve2;
    };
    while (!cfg.max_moves || attempts < cfg.max_moves) {
        if ((attempts & 1023) == 0) {
            elapsed = std::chrono::duration<double>(Clock::now() - started).count();
            if (elapsed >= cfg.seconds) break;
            int epoch = static_cast<int>(elapsed / cfg.epoch_seconds);
            if (epoch != last_epoch) {
                last_epoch = epoch;
                // Reheat from saved dirty states, not only zero-residence states.
                e.f = best[epoch % 4 == 3 ? 1 : 0].f; e.rebuild(); e.rebase(rng); ++restarts;
            }
            if (dirty && elapsed - last_save >= 5) { checkpoint(false); last_save = elapsed; dirty = false; }
            if (elapsed - last_log >= 20) {
                std::cout << "PROGRESS seconds=" << elapsed << " attempts=" << attempts << " proposals=" << proposals
                          << " accepted=" << accepted << " best=";
                json_score(std::cout, best[0].s, best[0].t); std::cout << std::endl; last_log = elapsed;
            }
        }
        double progress = std::fmod(elapsed, cfg.epoch_seconds) / cfg.epoch_seconds;
        double temperature = cfg.hot * std::pow(cfg.cold / cfg.hot, progress);
        ++attempts;
        if (attempts % 32768 == 0) { e.rebase(rng); ++recolourings; }
        if (attempts % 65536 == 0) {
            auto cycles = proposer.preferred(e, rng, cfg.res, cfg.u1, cfg.l2, 3.0 + 4 * temperature);
            // Test the global union, then its disjoint difference components.
            move.rows.clear(); move.edges.clear();
            for (const auto &[rows, edges] : cycles) {
                move.rows.insert(move.rows.end(), rows.begin(), rows.end());
                move.edges.insert(move.edges.end(), edges.begin(), edges.end());
            }
            uint64_t old_accepted = accepted;
            if (!move.rows.empty()) { consider(temperature); ++globals; }
            if (accepted == old_accepted) for (auto &[rows, edges] : cycles) {
                move.rows = rows; move.edges = edges; consider(temperature); ++globals;
            }
        } else if (proposer.random_cycle(e, rng, move)) consider(temperature);
    }
    elapsed = std::chrono::duration<double>(Clock::now() - started).count();
    checkpoint(true);
    std::ofstream stats(cfg.output + ".stats.json"); require(bool(stats), "open run statistics");
    stats << "{\"seed\":" << cfg.seed << ",\"seconds\":" << elapsed << ",\"attempts\":" << attempts
          << ",\"proposals\":" << proposals << ",\"accepted\":" << accepted << ",\"support1_proposals\":" << support1
          << ",\"global_proposals\":" << globals << ",\"recolourings\":" << recolourings
          << ",\"restarts\":" << restarts << ",\"best\":";
    json_score(stats, best[0].s, best[0].t); stats << "}\n";
    std::cout << "DONE seconds=" << elapsed << " attempts=" << attempts << " proposals=" << proposals
              << " accepted=" << accepted << " support1=" << support1 << " global=" << globals
              << " recolourings=" << recolourings << " restarts=" << restarts << '\n';
    for (int i = 0; i < 3; ++i) {
        std::cout << names[i] << ' '; json_score(std::cout, best[i].s, best[i].t); std::cout << '\n';
    }
}

Config parse(int argc, char **argv) {
    Config c;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        auto value = [&]() { require(++i < argc, "missing argument value"); return std::string(argv[i]); };
        if (arg == "--seed") c.seed = std::stoull(value());
        else if (arg == "--seconds") c.seconds = std::stod(value());
        else if (arg == "--moves") c.max_moves = std::stoull(value());
        else if (arg == "--res") c.res = std::stod(value());
        else if (arg == "--u1") c.u1 = std::stod(value());
        else if (arg == "--l2") c.l2 = std::stod(value());
        else if (arg == "--u2") c.u2 = std::stod(value());
        else if (arg == "--l3") c.l3 = std::stod(value());
        else if (arg == "--hot") c.hot = std::stod(value());
        else if (arg == "--cold") c.cold = std::stod(value());
        else if (arg == "--epoch-seconds") c.epoch_seconds = std::stod(value());
        else if (arg == "--self-test") c.self_test = std::stoi(value());
        else if (arg == "--output") c.output = value();
        else if (arg == "--resume") c.resume = value();
        else if (arg == "--audit-only") c.audit_only = true;
        else throw std::runtime_error("unknown option: " + arg);
    }
    require(c.seconds >= 0 && c.seconds <= 3600 && c.hot > 0 && c.cold > 0 && c.epoch_seconds > 0, "invalid time or temperature");
    require(c.res >= 0 && c.u1 >= 0 && c.l2 >= 0 && c.u2 >= 0 && c.l3 >= 0 && c.self_test >= 0, "invalid weights or tests");
    return c;
}
} // namespace

int main(int argc, char **argv) {
    try {
        Config cfg = parse(argc, argv); Catalogue cat;
        if (cfg.self_test) self_test(cat, cfg); else search(cat, cfg);
        return 0;
    } catch (const std::exception &error) {
        std::cerr << "ERROR " << error.what() << '\n'; return 2;
    }
}
