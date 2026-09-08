#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <mutex>
#include <numeric>
#include <random>
#include <set>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

using namespace std;

namespace br11 {

using Mask = uint16_t;

constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int FULL = LIMIT - 1;
constexpr int M = 462;
constexpr int DELAY = 3;
constexpr int SIGMA = 369;
constexpr int N = M + DELAY;
constexpr int LOWER_COUNT = 1023;
constexpr int BULK_COUNT = 1011;
constexpr int RESERVOIR_COUNT = 12;

struct Interval {
    int left = 0;
    int right = -1;
};

struct Core {
    int first = 0;
    int last = 0;
    Interval physical;
};

struct Geometry {
    array<Interval, M> central{};
    vector<Core> cores;
    array<Interval, RESERVOIR_COUNT> reservoir{};
    array<int, N> omega_index{};
    uint16_t omega_mask = 0;
};

static int popcount(Mask value) {
    return std::popcount(static_cast<unsigned>(value));
}

static bool strict_subset(Mask a, Mask b) {
    return a != b && (a & static_cast<Mask>(~b)) == 0;
}

static bool contains(const Interval& outer, const Interval& inner) {
    return outer.left <= inner.left && inner.right <= outer.right;
}

static Geometry make_geometry() {
    Geometry g;
    g.omega_index.fill(-1);
    for (int i = 0; i < M; ++i) {
        const int right = i + (i < SIGMA ? 2 : 3);
        g.central[i] = {i, right};
        for (int q = i + 1; q <= min(M - 1, right); ++q)
            g.cores.push_back({i, q, {q, right}});
    }
    g.reservoir = {
        Interval{0, 0}, Interval{0, 1}, Interval{1, 1},
        Interval{369, 371}, Interval{370, 371}, Interval{371, 371},
        Interval{462, 462}, Interval{462, 463}, Interval{462, 464},
        Interval{463, 463}, Interval{463, 464}, Interval{464, 464},
    };
    const array<int, 8> omega{0, 1, 369, 370, 371, 462, 463, 464};
    for (int i = 0; i < static_cast<int>(omega.size()); ++i) {
        g.omega_index[omega[i]] = i;
        g.omega_mask |= static_cast<uint16_t>(1u << i);
    }
    if (g.cores.size() != BULK_COUNT)
        throw runtime_error("internal geometry error: wrong core count");
    return g;
}

static const Geometry GEOMETRY = make_geometry();

static vector<Mask> all_rank6() {
    vector<Mask> values;
    for (int x = 1; x < LIMIT; ++x)
        if (popcount(static_cast<Mask>(x)) == 6)
            values.push_back(static_cast<Mask>(x));
    if (values.size() != M) throw runtime_error("rank-six enumeration failed");
    return values;
}

static vector<long long> read_numbers(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<long long> values;
    for (long long x; input >> x;) values.push_back(x);
    if (!input.eof()) throw runtime_error("invalid token in " + path);
    return values;
}

static vector<Mask> read_row(const string& path) {
    vector<long long> raw = read_numbers(path);
    if (raw.size() == M + 1 && raw.front() == M) raw.erase(raw.begin());
    if (raw.size() != M)
        throw runtime_error("row must contain exactly 462 masks");
    vector<Mask> row;
    row.reserve(M);
    for (long long x : raw) {
        if (x <= 0 || x >= LIMIT) throw runtime_error("row mask out of range");
        row.push_back(static_cast<Mask>(x));
    }
    return row;
}

static void write_row(const string& path, const vector<Mask>& row) {
    ofstream output(path);
    if (!output) throw runtime_error("cannot write " + path);
    for (int i = 0; i < M; ++i)
        output << static_cast<int>(row[i]) << (i + 1 == M ? '\n' : ' ');
}

static bool valid_permutation(const vector<Mask>& row, string* reason = nullptr) {
    if (row.size() != M) {
        if (reason) *reason = "wrong row length";
        return false;
    }
    array<uint8_t, LIMIT> count{};
    for (Mask value : row) {
        if (value == 0 || value >= LIMIT || popcount(value) != 6) {
            if (reason) *reason = "row contains a non-rank-six mask";
            return false;
        }
        if (++count[value] != 1) {
            if (reason) *reason = "row contains a duplicate";
            return false;
        }
    }
    for (int value = 1; value < LIMIT; ++value) {
        if (popcount(static_cast<Mask>(value)) == 6 && count[value] != 1) {
            if (reason) *reason = "row omits a rank-six mask";
            return false;
        }
    }
    return true;
}

static int mixed_run_deficit(const vector<Mask>& row) {
    int deficit = 0;
    for (int bit = 0; bit < K; ++bit) {
        const Mask flag = static_cast<Mask>(1u << bit);
        int position = 0;
        while (position < M) {
            if (!(row[position] & flag)) {
                ++position;
                continue;
            }
            const int first = position;
            while (position < M && (row[position] & flag)) ++position;
            if (first == 0 || position == M) continue;
            const int required = first <= 369 ? 3 : 4;
            deficit += max(0, required - (position - first));
        }
    }
    return deficit;
}

static vector<Mask> compute_meets(const vector<Mask>& row) {
    vector<Mask> values;
    values.reserve(BULK_COUNT);
    for (const Core& core : GEOMETRY.cores) {
        Mask value = static_cast<Mask>(FULL);
        for (int i = core.first; i <= core.last; ++i) value &= row[i];
        values.push_back(value);
    }
    return values;
}

struct UpperCoverage {
    array<uint8_t, LIMIT> seen{};
    array<int, K + 1> covered_by_rank{};
    array<int, K + 1> missing_by_rank{};
    vector<Mask> missing;
};

static UpperCoverage compute_upper(const vector<Mask>& row) {
    UpperCoverage answer;
    vector<Mask> previous, current;
    previous.reserve(K + 1);
    current.reserve(K + 1);
    for (Mask x : row) {
        current.clear();
        current.push_back(x);
        for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (Mask value : current) answer.seen[value] = 1;
        previous.swap(current);
    }
    for (int value = 1; value < LIMIT; ++value) {
        const int rank = popcount(static_cast<Mask>(value));
        if (rank < 7) continue;
        if (answer.seen[value]) {
            ++answer.covered_by_rank[rank];
        } else {
            ++answer.missing_by_rank[rank];
            answer.missing.push_back(static_cast<Mask>(value));
        }
    }
    return answer;
}

struct Evaluation {
    bool permutation = false;
    int run_deficit = 0;
    int zero_meets = 0;
    int distinct_nonzero_meets = 0;
    int meet_loss = BULK_COUNT;
    array<int, K + 1> missing_upper{};
    vector<Mask> meets;
    vector<Mask> missing_lower;
    vector<Mask> missing_upper_masks;
};

static Evaluation evaluate(const vector<Mask>& row) {
    Evaluation e;
    e.permutation = valid_permutation(row);
    if (!e.permutation) return e;
    e.run_deficit = mixed_run_deficit(row);
    e.meets = compute_meets(row);
    array<uint8_t, LIMIT> seen_meet{};
    for (Mask value : e.meets) {
        if (value == 0) {
            ++e.zero_meets;
        } else if (!seen_meet[value]) {
            seen_meet[value] = 1;
            ++e.distinct_nonzero_meets;
        }
    }
    e.meet_loss = BULK_COUNT - e.distinct_nonzero_meets;
    for (int value = 1; value < LIMIT; ++value) {
        const Mask mask = static_cast<Mask>(value);
        if (popcount(mask) <= 5 && !seen_meet[mask]) e.missing_lower.push_back(mask);
    }
    UpperCoverage upper = compute_upper(row);
    e.missing_upper = upper.missing_by_rank;
    e.missing_upper_masks = std::move(upper.missing);
    return e;
}

static bool row_gates_pass(const Evaluation& e) {
    if (!e.permutation || e.run_deficit != 0 || e.zero_meets != 0 ||
        e.distinct_nonzero_meets != BULK_COUNT ||
        e.missing_lower.size() != RESERVOIR_COUNT)
        return false;
    for (int rank = 7; rank <= K; ++rank)
        if (e.missing_upper[rank]) return false;
    return true;
}

static array<Mask, N> central_envelopes(const vector<Mask>& row) {
    array<Mask, N> envelope;
    envelope.fill(static_cast<Mask>(FULL));
    for (int i = 0; i < M; ++i)
        for (int j = GEOMETRY.central[i].left; j <= GEOMETRY.central[i].right; ++j)
            envelope[j] &= row[i];
    return envelope;
}

static uint16_t local_positions(const Interval& interval) {
    uint16_t result = 0;
    for (int j = interval.left; j <= interval.right; ++j) {
        const int local = GEOMETRY.omega_index[j];
        if (local >= 0) result |= static_cast<uint16_t>(1u << local);
    }
    return result;
}

static uint16_t local_legal_for_bit(const array<Mask, N>& envelope, int bit) {
    const Mask flag = static_cast<Mask>(1u << bit);
    uint16_t result = 0;
    for (int j = 0; j < N; ++j) {
        const int local = GEOMETRY.omega_index[j];
        if (local >= 0 && (envelope[j] & flag))
            result |= static_cast<uint16_t>(1u << local);
    }
    return result;
}

struct LocalRequirement {
    int bit = 0;
    uint16_t positions = 0;
};

static vector<LocalRequirement> vulnerable_requirements(
    const vector<Mask>& row, const vector<Mask>& meets,
    const array<Mask, N>& envelope) {
    vector<LocalRequirement> requirements;
    auto add_interval = [&](const Interval& interval, Mask label) {
        for (int bit = 0; bit < K; ++bit) {
            const Mask flag = static_cast<Mask>(1u << bit);
            if (!(label & flag)) continue;
            bool outside = false;
            uint16_t local = 0;
            for (int j = interval.left; j <= interval.right; ++j) {
                if (!(envelope[j] & flag)) continue;
                const int oi = GEOMETRY.omega_index[j];
                if (oi < 0) outside = true;
                else local |= static_cast<uint16_t>(1u << oi);
            }
            if (!outside) requirements.push_back({bit, local});
        }
    };
    for (int i = 0; i < M; ++i) add_interval(GEOMETRY.central[i], row[i]);
    for (int e = 0; e < BULK_COUNT; ++e)
        add_interval(GEOMETRY.cores[e].physical, meets[e]);
    return requirements;
}

static int containment_matching_size(const vector<Mask>& missing,
                                     const array<Mask, N>& envelope) {
    if (missing.size() != RESERVOIR_COUNT) return 0;
    array<vector<int>, RESERVOIR_COUNT> edges;
    for (int a = 0; a < RESERVOIR_COUNT; ++a) {
        Mask capacity = 0;
        for (int j = GEOMETRY.reservoir[a].left;
             j <= GEOMETRY.reservoir[a].right; ++j)
            capacity |= envelope[j];
        for (int t = 0; t < RESERVOIR_COUNT; ++t)
            if ((missing[t] & static_cast<Mask>(~capacity)) == 0)
                edges[a].push_back(t);
    }
    array<int, RESERVOIR_COUNT> owner;
    owner.fill(-1);
    function<bool(int, array<uint8_t, RESERVOIR_COUNT>&)> augment =
        [&](int a, array<uint8_t, RESERVOIR_COUNT>& used) {
            for (int t : edges[a]) {
                if (used[t]) continue;
                used[t] = 1;
                if (owner[t] < 0 || augment(owner[t], used)) {
                    owner[t] = a;
                    return true;
                }
            }
            return false;
        };
    int matched = 0;
    for (int a = 0; a < RESERVOIR_COUNT; ++a) {
        array<uint8_t, RESERVOIR_COUNT> used{};
        matched += augment(a, used);
    }
    return matched;
}

struct ReservoirSolution {
    bool feasible = false;
    array<Mask, RESERVOIR_COUNT> labels{};
    uint64_t nodes = 0;
    int containment_matching = 0;
    int vulnerable_pins = 0;
};

class ReservoirSolver {
public:
    ReservoirSolver(const vector<Mask>& row, const Evaluation& evaluation)
        : row_(row), meets_(evaluation.meets), missing_(evaluation.missing_lower),
          envelope_(central_envelopes(row)) {
        requirements_ = vulnerable_requirements(row_, meets_, envelope_);
        for (int bit = 0; bit < K; ++bit)
            initial_legal_[bit] = local_legal_for_bit(envelope_, bit);
        for (int a = 0; a < RESERVOIR_COUNT; ++a) {
            reservoir_local_[a] = local_positions(GEOMETRY.reservoir[a]);
            for (int b = 0; b < RESERVOIR_COUNT; ++b)
                proper_subset_[a][b] =
                    a != b && contains(GEOMETRY.reservoir[b], GEOMETRY.reservoir[a]);
        }
        assigned_.fill(-1);
        labels_.fill(0);
        for (int a = 0; a < RESERVOIR_COUNT; ++a) {
            Mask capacity = 0;
            for (int j = GEOMETRY.reservoir[a].left;
                 j <= GEOMETRY.reservoir[a].right; ++j)
                capacity |= envelope_[j];
            for (int t = 0; t < static_cast<int>(missing_.size()); ++t)
                candidate_[a][t] =
                    (missing_[t] & static_cast<Mask>(~capacity)) == 0;
        }
    }

    ReservoirSolution solve() {
        ReservoirSolution result;
        result.vulnerable_pins = static_cast<int>(requirements_.size());
        result.containment_matching = containment_matching_size(missing_, envelope_);
        if (missing_.size() != RESERVOIR_COUNT ||
            result.containment_matching != RESERVOIR_COUNT)
            return result;
        array<uint16_t, K> legal = initial_legal_;
        if (dfs(0, legal)) {
            result.feasible = true;
            result.labels = labels_;
        }
        result.nodes = nodes_;
        return result;
    }

private:
    const vector<Mask>& row_;
    const vector<Mask>& meets_;
    vector<Mask> missing_;
    array<Mask, N> envelope_{};
    vector<LocalRequirement> requirements_;
    array<uint16_t, K> initial_legal_{};
    array<uint16_t, RESERVOIR_COUNT> reservoir_local_{};
    array<array<uint8_t, RESERVOIR_COUNT>, RESERVOIR_COUNT> proper_subset_{};
    array<array<uint8_t, RESERVOIR_COUNT>, RESERVOIR_COUNT> candidate_{};
    array<int, RESERVOIR_COUNT> assigned_{};
    array<Mask, RESERVOIR_COUNT> labels_{};
    uint16_t used_targets_ = 0;
    uint64_t nodes_ = 0;

    bool compatible(int cell, int target) const {
        if (!candidate_[cell][target] || (used_targets_ & (1u << target))) return false;
        const Mask value = missing_[target];
        for (int other = 0; other < RESERVOIR_COUNT; ++other) {
            if (assigned_[other] < 0) continue;
            const Mask placed = labels_[other];
            if (proper_subset_[cell][other] && !strict_subset(value, placed)) return false;
            if (proper_subset_[other][cell] && !strict_subset(placed, value)) return false;
        }
        return true;
    }

    bool pins_survive(const array<uint16_t, K>& legal) const {
        for (const LocalRequirement& req : requirements_)
            if ((legal[req.bit] & req.positions) == 0) return false;
        for (int cell = 0; cell < RESERVOIR_COUNT; ++cell) {
            if (assigned_[cell] < 0) continue;
            const Mask label = labels_[cell];
            for (int bit = 0; bit < K; ++bit)
                if ((label & (1u << bit)) &&
                    (legal[bit] & reservoir_local_[cell]) == 0)
                    return false;
        }
        return true;
    }

    bool future_poset_support() const {
        for (int cell = 0; cell < RESERVOIR_COUNT; ++cell) {
            if (assigned_[cell] >= 0) continue;
            bool any = false;
            for (int target = 0; target < RESERVOIR_COUNT; ++target)
                if (compatible(cell, target)) {
                    any = true;
                    break;
                }
            if (!any) return false;
        }
        return true;
    }

    bool dfs(int depth, const array<uint16_t, K>& legal) {
        ++nodes_;
        if (!pins_survive(legal) || !future_poset_support()) return false;
        if (depth == RESERVOIR_COUNT) return true;

        int cell = -1;
        vector<int> choices;
        for (int a = 0; a < RESERVOIR_COUNT; ++a) {
            if (assigned_[a] >= 0) continue;
            vector<int> current;
            for (int t = 0; t < RESERVOIR_COUNT; ++t)
                if (compatible(a, t)) current.push_back(t);
            if (cell < 0 || current.size() < choices.size()) {
                cell = a;
                choices.swap(current);
            }
        }
        sort(choices.begin(), choices.end(), [&](int lhs, int rhs) {
            return popcount(missing_[lhs]) < popcount(missing_[rhs]);
        });
        for (int target : choices) {
            const Mask label = missing_[target];
            assigned_[cell] = target;
            labels_[cell] = label;
            used_targets_ |= static_cast<uint16_t>(1u << target);
            array<uint16_t, K> next = legal;
            const uint16_t positions = reservoir_local_[cell];
            for (int bit = 0; bit < K; ++bit)
                if (!(label & (1u << bit)))
                    next[bit] &= static_cast<uint16_t>(~positions);
            if (dfs(depth + 1, next)) return true;
            used_targets_ &= static_cast<uint16_t>(~(1u << target));
            assigned_[cell] = -1;
            labels_[cell] = 0;
        }
        return false;
    }
};

static vector<Mask> construct_array(
    const vector<Mask>& row, const array<Mask, RESERVOIR_COUNT>& labels) {
    array<Mask, N> values = central_envelopes(row);
    for (int a = 0; a < RESERVOIR_COUNT; ++a)
        for (int j = GEOMETRY.reservoir[a].left;
             j <= GEOMETRY.reservoir[a].right; ++j)
            values[j] &= labels[a];
    return vector<Mask>(values.begin(), values.end());
}

static Mask interval_or(const vector<Mask>& values, Interval interval) {
    Mask result = 0;
    for (int i = interval.left; i <= interval.right; ++i) result |= values[i];
    return result;
}

static bool verify_constructed(const vector<Mask>& row,
                               const vector<Mask>& meets,
                               const array<Mask, RESERVOIR_COUNT>& labels,
                               const vector<Mask>& values,
                               string* reason = nullptr) {
    if (values.size() != N) {
        if (reason) *reason = "wrong constructed length";
        return false;
    }
    for (Mask value : values) {
        if (value == 0 || value >= LIMIT) {
            if (reason) *reason = "constructed array contains zero/out-of-range entry";
            return false;
        }
    }
    for (int i = 0; i < M; ++i) {
        if (interval_or(values, GEOMETRY.central[i]) != row[i]) {
            if (reason) *reason = "central witness mismatch";
            return false;
        }
    }
    for (int e = 0; e < BULK_COUNT; ++e) {
        if (interval_or(values, GEOMETRY.cores[e].physical) != meets[e]) {
            if (reason) *reason = "bulk meet witness mismatch";
            return false;
        }
    }
    for (int a = 0; a < RESERVOIR_COUNT; ++a) {
        if (interval_or(values, GEOMETRY.reservoir[a]) != labels[a]) {
            if (reason) *reason = "reservoir witness mismatch";
            return false;
        }
    }

    array<uint8_t, LIMIT> exhaustive{}, suffix{};
    for (int left = 0; left < N; ++left) {
        Mask value = 0;
        for (int right = left; right < N; ++right) {
            value |= values[right];
            exhaustive[value] = 1;
        }
    }
    vector<Mask> previous, current;
    for (Mask x : values) {
        current.clear();
        current.push_back(x);
        for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (Mask value : current) suffix[value] = 1;
        previous.swap(current);
    }
    for (int value = 1; value < LIMIT; ++value) {
        if (!exhaustive[value] || !suffix[value] || exhaustive[value] != suffix[value]) {
            if (reason) *reason = "coverage verifier failed at mask " + to_string(value);
            return false;
        }
    }
    return true;
}

static void write_vector(ofstream& output, const vector<Mask>& values) {
    output << values.size() << '\n';
    for (size_t i = 0; i < values.size(); ++i)
        output << static_cast<int>(values[i]) << (i + 1 == values.size() ? '\n' : ' ');
}

static void write_certificate(const string& path, const vector<Mask>& row,
                              const array<Mask, RESERVOIR_COUNT>& labels,
                              const vector<Mask>& values) {
    ofstream output(path);
    if (!output) throw runtime_error("cannot write " + path);
    write_vector(output, row);
    vector<Mask> label_vector(labels.begin(), labels.end());
    write_vector(output, label_vector);
    write_vector(output, values);
}

static void print_evaluation(const Evaluation& e) {
    cout << "permutation=" << (e.permutation ? "yes" : "no")
         << " run_deficit=" << e.run_deficit
         << " zero_meets=" << e.zero_meets
         << " distinct_meets=" << e.distinct_nonzero_meets << '/' << BULK_COUNT
         << " missing_lower=" << e.missing_lower.size();
    for (int rank = 7; rank <= K; ++rank)
        cout << " missing_r" << rank << '=' << e.missing_upper[rank];
    cout << '\n';
}

static bool exact_solve_row(const vector<Mask>& row, const string& certificate,
                            bool verbose = true) {
    Evaluation e = evaluate(row);
    if (verbose) print_evaluation(e);
    if (!row_gates_pass(e)) return false;
    ReservoirSolver solver(row, e);
    ReservoirSolution solution = solver.solve();
    if (verbose) {
        cout << "containment_matching=" << solution.containment_matching
             << "/12 vulnerable_pins=" << solution.vulnerable_pins
             << " reservoir_nodes=" << solution.nodes
             << " reservoir=" << (solution.feasible ? "SAT" : "UNSAT") << '\n';
    }
    if (!solution.feasible) return false;
    vector<Mask> values = construct_array(row, solution.labels);
    string reason;
    if (!verify_constructed(row, e.meets, solution.labels, values, &reason))
        throw runtime_error("internal final verification failed: " + reason);
    if (!certificate.empty()) write_certificate(certificate, row, solution.labels, values);
    if (verbose) cout << "PASS optimal nonzero k=11 length=465\n";
    return true;
}

struct Score {
    int run = 0;
    int meet = 0;
    int r7 = 0;
    int r8 = 0;
    int r9 = 0;
    int r10 = 0;
    int matching = RESERVOIR_COUNT;
};

static Score make_score(const vector<Mask>& row, const Evaluation& e) {
    Score s;
    s.run = e.run_deficit;
    s.meet = e.meet_loss;
    s.r7 = e.missing_upper[7];
    s.r8 = e.missing_upper[8];
    s.r9 = e.missing_upper[9];
    s.r10 = e.missing_upper[10];
    if (e.missing_lower.size() == RESERVOIR_COUNT) {
        const auto envelope = central_envelopes(row);
        s.matching = RESERVOIR_COUNT - containment_matching_size(e.missing_lower, envelope);
    }
    return s;
}

static tuple<int, int, int, int, int, int, int> key(const Score& s,
                                                     const string& mode) {
    if (mode == "upper")
        return {s.run, s.r7, s.r8, s.r9, s.r10, s.meet, s.matching};
    if (mode == "lower")
        return {s.run, s.meet, s.matching, s.r7, s.r8, s.r9, s.r10};
    return {s.run, s.meet, s.r7, s.r8, s.r9, s.r10, s.matching};
}

static double energy(const Score& s, const string& mode) {
    if (mode == "upper")
        return 5000.0 * s.run + 200.0 * s.r7 + 40.0 * s.r8 +
               10.0 * s.r9 + 3.0 * s.r10 + 20.0 * s.meet + 5.0 * s.matching;
    if (mode == "lower")
        return 5000.0 * s.run + 200.0 * s.meet + 30.0 * s.matching +
               20.0 * s.r7 + 5.0 * s.r8 + 2.0 * s.r9 + s.r10;
    return 5000.0 * s.run + 100.0 * s.meet + 60.0 * s.r7 +
           15.0 * s.r8 + 4.0 * s.r9 + s.r10 + 10.0 * s.matching;
}

static void mutate(vector<Mask>& row, mt19937_64& rng) {
    uniform_int_distribution<int> position(0, M - 1);
    const int kind = static_cast<int>(rng() % 100);
    if (kind < 45) {
        int a = position(rng), b = position(rng);
        if (a != b) swap(row[a], row[b]);
    } else if (kind < 75) {
        int a = position(rng), b = position(rng);
        if (a > b) swap(a, b);
        if (a != b) reverse(row.begin() + a, row.begin() + b + 1);
    } else {
        int left = position(rng);
        int length = 1 + static_cast<int>(rng() % 20);
        int right = min(M - 1, left + length - 1);
        vector<Mask> block(row.begin() + left, row.begin() + right + 1);
        row.erase(row.begin() + left, row.begin() + right + 1);
        int gap = static_cast<int>(rng() % (row.size() + 1));
        if (rng() & 1) reverse(block.begin(), block.end());
        row.insert(row.begin() + gap, block.begin(), block.end());
    }
}

static string score_string(const Score& s) {
    return "run=" + to_string(s.run) + " meet=" + to_string(s.meet) +
           " r7=" + to_string(s.r7) + " r8=" + to_string(s.r8) +
           " r9=" + to_string(s.r9) + " r10=" + to_string(s.r10) +
           " matching=" + to_string(s.matching);
}

[[maybe_unused]] static int search(const vector<Mask>& seed,
                                   const string& output_path,
                                   uint64_t iterations, uint64_t random_seed,
                                   const string& mode) {
    string reason;
    if (!valid_permutation(seed, &reason)) throw runtime_error(reason);

    vector<Mask> global_best = seed;
    Evaluation initial_eval = evaluate(seed);
    Score global_score = make_score(seed, initial_eval);
    write_row(output_path, global_best);
    mutex best_mutex;
    atomic<bool> solved{false};
    cerr << "initial " << score_string(global_score) << '\n';

#ifdef _OPENMP
#pragma omp parallel
#endif
    {
        int tid = 0;
#ifdef _OPENMP
        tid = omp_get_thread_num();
#endif
        mt19937_64 rng(random_seed + 0x9e3779b97f4a7c15ULL * (tid + 1));
        vector<Mask> current = seed;
        if (tid) {
            for (int j = 0; j < tid % 17; ++j) {
                int a = static_cast<int>(rng() % M);
                int b = static_cast<int>(rng() % M);
                swap(current[a], current[b]);
            }
        }
        Evaluation current_eval = evaluate(current);
        Score current_score = make_score(current, current_eval);
        double current_energy = energy(current_score, mode);
        const uint64_t local_iterations = iterations;
        const uint64_t cycle = 200000;

        for (uint64_t it = 0; it < local_iterations && !solved.load(); ++it) {
            vector<Mask> candidate = current;
            mutate(candidate, rng);
            Evaluation candidate_eval = evaluate(candidate);
            Score candidate_score = make_score(candidate, candidate_eval);

            // Once a thread reaches an exact earlier gate, preserve it while
            // optimizing the later gates.
            if (current_score.run == 0 && candidate_score.run != 0) continue;
            if (current_score.run == 0 && current_score.meet == 0 &&
                candidate_score.meet != 0) continue;

            const double candidate_energy = energy(candidate_score, mode);
            const double phase = static_cast<double>(it % cycle) / cycle;
            const double temperature = max(0.25, 100.0 * (1.0 - phase));
            bool accept = key(candidate_score, mode) < key(current_score, mode);
            if (!accept) {
                const double delta = candidate_energy - current_energy;
                const double probability = exp(-max(0.0, delta) / temperature);
                accept = generate_canonical<double, 53>(rng) < probability;
            }
            if (accept) {
                current.swap(candidate);
                current_eval = std::move(candidate_eval);
                current_score = candidate_score;
                current_energy = candidate_energy;
            }

            bool new_best = false;
            {
                lock_guard<mutex> lock(best_mutex);
                if (key(current_score, mode) < key(global_score, mode)) {
                    global_best = current;
                    global_score = current_score;
                    write_row(output_path, global_best);
                    cerr << "best tid=" << tid << " it=" << it << ' '
                         << score_string(global_score) << '\n';
                    new_best = true;
                }
            }
            if (new_best && current_score.run == 0 && current_score.meet == 0 &&
                current_score.r7 == 0 && current_score.r8 == 0 &&
                current_score.r9 == 0 && current_score.r10 == 0) {
                if (exact_solve_row(current, output_path + ".cert", false)) {
                    solved.store(true);
                    lock_guard<mutex> lock(best_mutex);
                    global_best = current;
                    write_row(output_path, global_best);
                    cerr << "SOLVED certificate=" << output_path << ".cert\n";
                }
            }
            if ((it + 1) % cycle == 0) {
                lock_guard<mutex> lock(best_mutex);
                current = global_best;
                current_eval = evaluate(current);
                current_score = make_score(current, current_eval);
                current_energy = energy(current_score, mode);
            }
        }
    }
    return solved.load() ? 0 : 1;
}

static vector<Mask> suffix_values(const vector<Mask>& values) {
    vector<Mask> result;
    vector<Mask> previous, current;
    for (Mask x : values) {
        current.clear();
        current.push_back(x);
        for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        result.insert(result.end(), current.begin(), current.end());
        previous.swap(current);
    }
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result;
}

static void self_test() {
    if (GEOMETRY.cores.size() != BULK_COUNT) throw runtime_error("core-count test");
    constexpr int omitted_lower = LOWER_COUNT - BULK_COUNT;
    constexpr int rank5_masks = 462;
    constexpr int pair_cores = 461;
    constexpr int triple_cores = 460;
    constexpr int rank4_masks = 330;
    constexpr int forced_rank5_pairs = rank5_masks - omitted_lower;
    constexpr int low_pairs = pair_cores - forced_rank5_pairs;
    constexpr int forced_rank4_triples = triple_cores - 2 * low_pairs;
    static_assert(omitted_lower == 12 && forced_rank5_pairs == 450 &&
                  low_pairs == 11 && forced_rank4_triples == 438 &&
                  forced_rank4_triples > rank4_masks);
    set<pair<int, int>> cells;
    auto insert_unique = [&](Interval interval) {
        if (!cells.insert({interval.left, interval.right}).second)
            throw runtime_error("short-cell partition overlap");
    };
    for (int i = 0; i < SIGMA; ++i) insert_unique(GEOMETRY.central[i]);
    for (const Core& core : GEOMETRY.cores) insert_unique(core.physical);
    for (Interval interval : GEOMETRY.reservoir) insert_unique(interval);
    if (cells.size() != 1392) throw runtime_error("short-cell partition count");
    for (int left = 0; left < N; ++left)
        for (int length = 1; length <= DELAY && left + length <= N; ++length)
            if (!cells.count({left, left + length - 1}))
                throw runtime_error("short-cell partition omission");
    int affected_central = 0, affected_cores = 0;
    for (Interval interval : GEOMETRY.central)
        affected_central += local_positions(interval) != 0;
    for (const Core& core : GEOMETRY.cores)
        affected_cores += local_positions(core.physical) != 0;
    if (affected_central != 10 || affected_cores != 11)
        throw runtime_error("localized-pin support count");

    mt19937_64 rng(0x42524f554e444152ULL);
    for (int trial = 0; trial < 128; ++trial) {
        vector<Mask> incidence(M);
        for (Mask& x : incidence) x = (rng() & 1) ? 1 : 0;
        array<uint8_t, N> legal;
        legal.fill(1);
        for (int i = 0; i < M; ++i)
            if (!incidence[i])
                for (int j = GEOMETRY.central[i].left;
                     j <= GEOMETRY.central[i].right; ++j)
                    legal[j] = 0;
        bool direct = true;
        for (int i = 0; i < M; ++i) {
            if (!incidence[i]) continue;
            bool pin = false;
            for (int j = GEOMETRY.central[i].left;
                 j <= GEOMETRY.central[i].right; ++j)
                pin |= legal[j];
            direct &= pin;
        }
        vector<Mask> fake(M);
        for (int i = 0; i < M; ++i) fake[i] = incidence[i] ? 1 : 0;
        const bool run_rule = mixed_run_deficit(fake) == 0;
        if (direct != run_rule) throw runtime_error("mixed-run equivalence test");
    }

    for (int trial = 0; trial < 128; ++trial) {
        vector<Mask> incidence(M);
        for (Mask& x : incidence) x = (rng() & 1) ? 1 : 0;
        array<uint8_t, RESERVOIR_COUNT> label_bit{};
        for (uint8_t& x : label_bit) x = static_cast<uint8_t>(rng() & 1);
        const auto envelope = central_envelopes(incidence);
        array<uint8_t, N> generic{};
        for (int j = 0; j < N; ++j) generic[j] = envelope[j] & 1;
        for (int a = 0; a < RESERVOIR_COUNT; ++a)
            if (!label_bit[a])
                for (int j = GEOMETRY.reservoir[a].left;
                     j <= GEOMETRY.reservoir[a].right; ++j)
                    generic[j] = 0;
        const array<int, 8> position{0, 1, 369, 370, 371, 462, 463, 464};
        const array<uint8_t, 8> formula{
            static_cast<uint8_t>(incidence[0] && label_bit[0] && label_bit[1]),
            static_cast<uint8_t>(incidence[0] && incidence[1] &&
                                 label_bit[1] && label_bit[2]),
            static_cast<uint8_t>(incidence[367] && incidence[368] &&
                                 incidence[369] && label_bit[3]),
            static_cast<uint8_t>(incidence[368] && incidence[369] &&
                                 incidence[370] && label_bit[3] && label_bit[4]),
            static_cast<uint8_t>(incidence[369] && incidence[370] &&
                                 incidence[371] && label_bit[3] && label_bit[4] &&
                                 label_bit[5]),
            static_cast<uint8_t>(incidence[459] && incidence[460] &&
                                 incidence[461] && label_bit[6] && label_bit[7] &&
                                 label_bit[8]),
            static_cast<uint8_t>(incidence[460] && incidence[461] &&
                                 label_bit[7] && label_bit[8] && label_bit[9] &&
                                 label_bit[10]),
            static_cast<uint8_t>(incidence[461] && label_bit[8] &&
                                 label_bit[10] && label_bit[11]),
        };
        for (int i = 0; i < 8; ++i)
            if (generic[position[i]] != formula[i])
                throw runtime_error("local reservoir formula test");
    }

    for (int trial = 0; trial < 128; ++trial) {
        vector<Mask> values(30);
        for (Mask& x : values) x = static_cast<Mask>(1 + rng() % FULL);
        array<uint8_t, LIMIT> exhaustive{};
        for (int left = 0; left < static_cast<int>(values.size()); ++left) {
            Mask value = 0;
            for (int right = left; right < static_cast<int>(values.size()); ++right) {
                value |= values[right];
                exhaustive[value] = 1;
            }
        }
        array<uint8_t, LIMIT> recurrence{};
        for (Mask value : suffix_values(values)) recurrence[value] = 1;
        if (exhaustive != recurrence) throw runtime_error("suffix recurrence test");
    }

    vector<Mask> sorted = all_rank6();
    string reason;
    if (!valid_permutation(sorted, &reason)) throw runtime_error("permutation test");
    Evaluation check = evaluate(sorted);
    if (check.meets.size() != BULK_COUNT) throw runtime_error("evaluation test");
    cout << "PASS geometry=1392 core=1011 reservoir=12"
            " no-go=438>330 run-rule local-pins suffix-OR\n";
}

}  // namespace br11

int main(int argc, char** argv) {
    using namespace br11;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc == 2 && string(argv[1]) == "--self-test") {
            self_test();
            return 0;
        }
        if (argc == 3 && string(argv[1]) == "--check") {
            vector<Mask> row = read_row(argv[2]);
            Evaluation e = evaluate(row);
            print_evaluation(e);
            if (e.missing_lower.size() == RESERVOIR_COUNT) {
                ReservoirSolver solver(row, e);
                ReservoirSolution solution = solver.solve();
                cout << "containment_matching=" << solution.containment_matching
                     << "/12 vulnerable_pins=" << solution.vulnerable_pins
                     << " reservoir_nodes=" << solution.nodes
                     << " reservoir=" << (solution.feasible ? "SAT" : "UNSAT") << '\n';
            }
            return row_gates_pass(e) ? 0 : 1;
        }
        if (argc == 4 && string(argv[1]) == "--solve") {
            vector<Mask> row = read_row(argv[2]);
            return exact_solve_row(row, argv[3]) ? 0 : 1;
        }
        if ((argc == 7 || argc == 8) && string(argv[1]) == "--search") {
            cerr << "REFUSED: the q369 rainbow 1011-core branch is proved UNSAT"
                    " (it would force 438 distinct rank-4 triple cores, but only"
                    " 330 exist). No search was launched.\n";
            return 3;
        }
        cerr << "usage:\n"
             << "  k11_boundary_reservoir_search --self-test\n"
             << "  k11_boundary_reservoir_search --check ROW\n"
             << "  k11_boundary_reservoir_search --solve ROW CERTIFICATE\n"
             << "  k11_boundary_reservoir_search --search ROW OUT ITERATIONS SEED"
                " {balanced|lower|upper} [THREADS]\n";
        return 2;
    } catch (const exception& e) {
        cerr << "error: " << e.what() << '\n';
        return 2;
    }
}
