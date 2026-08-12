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
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <queue>
#include <random>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <vector>
#include <unistd.h>

using namespace std;

namespace q369 {

using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int FULL = LIMIT - 1;
constexpr int M = 462;
constexpr int N = 465;
constexpr int SIGMA = 369;
constexpr int LOWER_TARGETS = 1023;
constexpr int SHORT_INTERVALS = 3 * N - 3;

struct Interval { int left, right; };

static array<Interval, M> make_central() {
    array<Interval, M> result{};
    for (int i = 0; i < M; ++i) result[i] = {i, i + (i < SIGMA ? 2 : 3)};
    return result;
}

static const array<Interval, M> CENTRAL = make_central();

static int pc(Mask value) {
    return popcount(static_cast<unsigned>(value));
}

static bool johnson_adjacent(Mask a, Mask b) {
    return pc(static_cast<Mask>(a ^ b)) == 2;
}

// The q369 short-band saturation theorem forces at least 323 of the 330
// rank-four masks to occur as consecutive triple intersections in the two
// bulk ranges.  The two seam-crossing triples p=367,368 (zero based) are not
// forced hosts and are deliberately omitted.
static int bulk_d3_distinct(const vector<Mask>& row) {
    array<uint8_t, LIMIT> seen{};
    int distinct = 0;
    auto add_range = [&](int begin, int end) {
        for (int p = begin; p < end; ++p) {
            const Mask value = static_cast<Mask>(row[p] & row[p + 1] & row[p + 2]);
            if (pc(value) == 4 && !seen[value]++) ++distinct;
        }
    };
    add_range(0, 367);       // p=0,...,366
    add_range(369, 460);     // p=369,...,459
    return distinct;
}

static vector<Mask> read_row(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<unsigned> raw;
    for (unsigned value; input >> value;) raw.push_back(value);
    if (!input.eof()) throw runtime_error("invalid token in " + path);
    if (raw.size() == M + 1 && raw.front() == M) raw.erase(raw.begin());
    if (raw.size() != M) throw runtime_error(path + " must contain 462 masks");
    vector<Mask> row;
    array<uint8_t, LIMIT> count{};
    for (unsigned value : raw) {
        if (value >= LIMIT || pc(static_cast<Mask>(value)) != 6 || ++count[value] != 1)
            throw runtime_error(path + " is not a rank-six permutation");
        row.push_back(static_cast<Mask>(value));
    }
    return row;
}

static void write_row(const string& path, const vector<Mask>& row) {
    ofstream output(path);
    if (!output) throw runtime_error("cannot write " + path);
    for (int i = 0; i < M; ++i)
        output << static_cast<int>(row[i]) << (i + 1 == M ? '\n' : ' ');
}

static bool rainbow_johnson_path(const vector<Mask>& row, bool two_component = false) {
    if (row.size() != M) return false;
    array<uint8_t, LIMIT> vertex{}, color{};
    for (Mask value : row)
        if (pc(value) != 6 || ++vertex[value] != 1) return false;
    for (int i = 0; i + 1 < M; ++i) {
        if (two_component && i == SIGMA - 1) continue;
        if (!johnson_adjacent(row[i], row[i + 1])) return false;
        const Mask intersection = static_cast<Mask>(row[i] & row[i + 1]);
        if (pc(intersection) != 5 || ++color[intersection] != 1) return false;
    }
    if (two_component) {
        vector<Mask> missing;
        for (int mask = 1; mask < LIMIT; ++mask)
            if (pc(static_cast<Mask>(mask)) == 5 && !color[mask])
                missing.push_back(static_cast<Mask>(mask));
        if (missing.size() != 2) return false;
        const array<Mask, 3> endpoint_masks{row.front(), row[SIGMA], row.back()};
        for (int first = 0; first < 3; ++first) {
            if (missing[0] & static_cast<Mask>(~endpoint_masks[first])) continue;
            for (int second = 0; second < 3; ++second) {
                if (first == second) continue;
                if (!(missing[1] & static_cast<Mask>(~endpoint_masks[second])))
                    return bulk_d3_distinct(row) >= 323;
            }
        }
        return false;
    }
    for (int mask = 1; mask < LIMIT; ++mask) {
        if (pc(static_cast<Mask>(mask)) != 5 || color[mask]) continue;
        if ((mask & ~row.front()) && (mask & ~row.back())) return false;
    }
    return true;
}

static const vector<Mask>& lower_masks() {
    static const vector<Mask> result = [] {
        vector<Mask> values;
        for (int mask = 1; mask < LIMIT; ++mask)
            if (pc(static_cast<Mask>(mask)) <= 5)
                values.push_back(static_cast<Mask>(mask));
        return values;
    }();
    return result;
}

static const vector<Interval>& short_intervals() {
    static const vector<Interval> result = [] {
        vector<Interval> values;
        for (int length = 1; length <= 3; ++length)
            for (int left = 0; left + length <= N; ++left)
                values.push_back({left, left + length - 1});
        return values;
    }();
    return result;
}

struct Evaluation {
    struct PinFailure {
        char kind;
        int owner;
        int bit;
        Interval interval;
    };
    int pin_deficit = 0;
    int empty_envelopes = 0;
    int missing_central_pins = 0;
    int hall_matching = 0;
    int hall_deficit = LOWER_TARGETS;
    int matching_pin_conflicts = 0;
    // A failed pin obligation has positive forbidden multiplicity at every
    // one of its possible pin positions.  The pressure is the sum, over all
    // failed obligations, of the minimum such multiplicity.  Hence pressure
    // is zero exactly when matching_pin_conflicts is zero, but it gives the
    // matching search a gradient while the binary conflict count is flat.
    int matching_pin_pressure = 0;
    // Total number of currently surviving pin choices over all position,
    // central, and matched-target obligations.  This is only a tie breaker:
    // more choices make a matching less fragile under a subsequent path move.
    int matching_pin_slack = 0;
    int matching_empty_positions = 0;
    int matching_central_failures = 0;
    int matching_target_failures = 0;
    int empty_targets = 0;
    int upper_missing = 0;
    int selectors = 0;
    int seam_union_rank = 0;
    int d3_distinct = 0;
    int d3_cut_deficit = 0;
    int projection_failures = 0;
    bool projection_checked = false;
    array<int, K + 1> upper_missing_by_rank{};
    vector<int> hot_positions;
    vector<PinFailure> pin_failures;
};

static bool better(const Evaluation& a, const Evaluation& b) {
    return tuple{a.pin_deficit, a.d3_cut_deficit, a.hall_deficit,
                 a.projection_failures, a.matching_pin_conflicts,
                 a.matching_pin_pressure, -a.matching_pin_slack,
                 -a.d3_distinct, a.upper_missing,
                 a.empty_targets, abs(a.seam_union_rank - 8), -a.selectors} <
           tuple{b.pin_deficit, b.d3_cut_deficit, b.hall_deficit,
                 b.projection_failures, b.matching_pin_conflicts,
                 b.matching_pin_pressure, -b.matching_pin_slack,
                 -b.d3_distinct, b.upper_missing,
                 b.empty_targets, abs(b.seam_union_rank - 8), -b.selectors};
}

// Comparator used before the optional exact projection oracle is invoked.
// It deliberately omits projection_failures, which is not populated by the
// hot inner evaluator.
static bool better_cheap(const Evaluation& a, const Evaluation& b) {
    return tuple{a.pin_deficit, a.d3_cut_deficit, a.hall_deficit,
                 a.matching_pin_conflicts, a.matching_pin_pressure,
                 -a.matching_pin_slack, -a.d3_distinct, a.upper_missing,
                 a.empty_targets, abs(a.seam_union_rank - 8), -a.selectors} <
           tuple{b.pin_deficit, b.d3_cut_deficit, b.hall_deficit,
                 b.matching_pin_conflicts, b.matching_pin_pressure,
                 -b.matching_pin_slack, -b.d3_distinct, b.upper_missing,
                 b.empty_targets, abs(b.seam_union_rank - 8), -b.selectors};
}

static long long anneal_cost(const Evaluation& value) {
    return static_cast<long long>(value.pin_deficit) * 10000000000LL
         + static_cast<long long>(value.d3_cut_deficit) * 1000000000LL
         + static_cast<long long>(value.hall_deficit) * 10000000LL
         + static_cast<long long>(value.matching_pin_conflicts) * 100000LL
         + static_cast<long long>(value.matching_pin_pressure) * 1000LL
         + static_cast<long long>(value.upper_missing) * 10000LL
         - static_cast<long long>(value.d3_distinct) * 100LL
         + static_cast<long long>(value.empty_targets) * 100LL
         - min(value.matching_pin_slack, 50000) * 10LL
         - value.selectors;
}

static Evaluation evaluate(const vector<Mask>& row, int matching_trials = 256) {
    Evaluation result;
    result.seam_union_rank = pc(static_cast<Mask>(row[SIGMA - 1] | row[SIGMA]));
    result.d3_distinct = bulk_d3_distinct(row);
    result.d3_cut_deficit = max(0, 323 - result.d3_distinct);
    array<Mask, N> envelope;
    envelope.fill(static_cast<Mask>(FULL));
    for (int i = 0; i < M; ++i)
        for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p)
            envelope[p] &= row[i];

    for (int p = 0; p < N; ++p)
        if (!envelope[p]) ++result.empty_envelopes;
    for (int i = 0; i < M; ++i) {
        Mask required = row[i];
        while (required) {
            const int bit = countr_zero(static_cast<unsigned>(required));
            bool pinned = false;
            for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p)
                pinned |= (envelope[p] & (1u << bit)) != 0;
            if (!pinned) ++result.missing_central_pins;
            required &= static_cast<Mask>(required - 1);
        }
    }
    result.pin_deficit = result.empty_envelopes + result.missing_central_pins;

    const vector<Mask>& targets = lower_masks();
    const vector<Interval>& intervals = short_intervals();
    vector<vector<int>> edges(LOWER_TARGETS);
    for (int target_index = 0; target_index < LOWER_TARGETS; ++target_index) {
        const Mask target = targets[target_index];
        for (int interval_index = 0; interval_index < SHORT_INTERVALS;
             ++interval_index) {
            const Interval interval = intervals[interval_index];
            Mask union_envelope = 0;
            bool compatible = true;
            for (int p = interval.left; p <= interval.right; ++p) {
                union_envelope |= envelope[p];
                if (!(target & envelope[p])) compatible = false;
            }
            if (!compatible || (target & static_cast<Mask>(~union_envelope))) continue;

            const int first_central = max(0, interval.left - 3);
            const int last_central = min(M - 1, interval.right);
            for (int i = first_central; compatible && i <= last_central; ++i) {
                if (interval.left <= CENTRAL[i].left &&
                    CENTRAL[i].right <= interval.right &&
                    (row[i] & static_cast<Mask>(~target))) {
                    compatible = false;
                    break;
                }
                Mask omitted = row[i] & static_cast<Mask>(~target);
                while (omitted && compatible) {
                    const int bit = countr_zero(static_cast<unsigned>(omitted));
                    bool pin = false, outside = false;
                    for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p) {
                        if (!(envelope[p] & (1u << bit))) continue;
                        pin = true;
                        outside |= p < interval.left || p > interval.right;
                    }
                    if (pin && !outside) compatible = false;
                    omitted &= static_cast<Mask>(omitted - 1);
                }
            }
            if (compatible) edges[target_index].push_back(interval_index);
        }
        result.selectors += static_cast<int>(edges[target_index].size());
        result.empty_targets += edges[target_index].empty();
    }

    vector<int> left_match(LOWER_TARGETS, -1), right_match(SHORT_INTERVALS, -1);
    vector<int> distance(LOWER_TARGETS);
    auto bfs = [&]() {
        queue<int> todo;
        bool augmenting = false;
        for (int left = 0; left < LOWER_TARGETS; ++left) {
            if (left_match[left] < 0) distance[left] = 0, todo.push(left);
            else distance[left] = -1;
        }
        while (!todo.empty()) {
            const int left = todo.front();
            todo.pop();
            for (int right : edges[left]) {
                const int next = right_match[right];
                if (next < 0) augmenting = true;
                else if (distance[next] < 0)
                    distance[next] = distance[left] + 1, todo.push(next);
            }
        }
        return augmenting;
    };
    auto dfs = [&](auto&& self, int left) -> bool {
        for (int right : edges[left]) {
            const int next = right_match[right];
            if (next < 0 || (distance[next] == distance[left] + 1 && self(self, next))) {
                left_match[left] = right;
                right_match[right] = left;
                return true;
            }
        }
        distance[left] = -1;
        return false;
    };
    while (bfs())
        for (int left = 0; left < LOWER_TARGETS; ++left)
            if (left_match[left] < 0 && dfs(dfs, left)) ++result.hall_matching;
    result.hall_deficit = LOWER_TARGETS - result.hall_matching;
    array<uint8_t, N> failure_hot{};

    if (!result.hall_deficit) {
        struct MatchingScore {
            int failures = 0;
            int pressure = 0;
            int slack = 0;
            int position_failures = 0;
            int central_failures = 0;
            int target_failures = 0;
        };
        struct MatchingMeasurement {
            MatchingScore score;
            // Repetitions are deliberate: a target participating in several
            // currently blocked pin obligations is sampled more often.
            vector<int> hot_left;
        };
        auto score_key = [](const MatchingScore& score) {
            return tuple{score.failures, score.pressure,
                         score.position_failures, score.central_failures,
                         score.target_failures, -score.slack};
        };
        auto score_better = [&](const MatchingScore& a, const MatchingScore& b) {
            return score_key(a) < score_key(b);
        };
        auto score_equal = [&](const MatchingScore& a, const MatchingScore& b) {
            return score_key(a) == score_key(b);
        };
        auto measure = [&](const vector<int>& matching, bool collect_hot = false) {
            array<array<uint16_t, K>, N> forbidden{};
            for (int left = 0; left < LOWER_TARGETS; ++left) {
                const Interval interval = intervals[matching[left]];
                const Mask omitted = static_cast<Mask>(FULL & ~targets[left]);
                for (int p = interval.left; p <= interval.right; ++p) {
                    Mask bits = static_cast<Mask>(envelope[p] & omitted);
                    while (bits) {
                        const int bit = countr_zero(static_cast<unsigned>(bits));
                        ++forbidden[p][bit];
                        bits &= static_cast<Mask>(bits - 1);
                    }
                }
            }
            MatchingMeasurement measurement;
            MatchingScore& score = measurement.score;
            array<array<uint16_t, K>, N> failed_weight{};
            vector<int> blame(collect_hot ? LOWER_TARGETS : 0);
            auto account = [&](int minimum, int surviving) {
                score.slack += surviving;
                if (minimum > 0) {
                    ++score.failures;
                    score.pressure += minimum;
                }
            };
            for (int p = 0; p < N; ++p) {
                int minimum = LOWER_TARGETS + 1, surviving = 0;
                for (int bit = 0; bit < K; ++bit) {
                    if (!(envelope[p] & (1u << bit))) continue;
                    minimum = min<int>(minimum, forbidden[p][bit]);
                    surviving += forbidden[p][bit] == 0;
                }
                account(minimum, surviving);
                if (minimum > 0) {
                    ++score.position_failures;
                    if (collect_hot)
                        for (int bit = 0; bit < K; ++bit)
                            if (envelope[p] & (1u << bit))
                                ++failed_weight[p][bit];
                }
            }
            for (int i = 0; i < M; ++i) {
                Mask bits = row[i];
                while (bits) {
                    const int bit = countr_zero(static_cast<unsigned>(bits));
                    int minimum = LOWER_TARGETS + 1, surviving = 0;
                    for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p) {
                        if (!(envelope[p] & (1u << bit))) continue;
                        minimum = min<int>(minimum, forbidden[p][bit]);
                        surviving += forbidden[p][bit] == 0;
                    }
                    account(minimum, surviving);
                    if (minimum > 0) {
                        ++score.central_failures;
                        if (collect_hot)
                            for (int p = CENTRAL[i].left;
                                 p <= CENTRAL[i].right; ++p)
                                if (envelope[p] & (1u << bit))
                                    ++failed_weight[p][bit];
                    }
                    bits &= static_cast<Mask>(bits - 1);
                }
            }
            for (int left = 0; left < LOWER_TARGETS; ++left) {
                const Interval interval = intervals[matching[left]];
                Mask bits = targets[left];
                while (bits) {
                    const int bit = countr_zero(static_cast<unsigned>(bits));
                    int minimum = LOWER_TARGETS + 1, surviving = 0;
                    for (int p = interval.left; p <= interval.right; ++p) {
                        if (!(envelope[p] & (1u << bit))) continue;
                        minimum = min<int>(minimum, forbidden[p][bit]);
                        surviving += forbidden[p][bit] == 0;
                    }
                    account(minimum, surviving);
                    if (minimum > 0) {
                        ++score.target_failures;
                        if (collect_hot) {
                            // Moving the failed target can change both its
                            // pin domain and the blockers it contributes.
                            ++blame[left];
                            for (int p = interval.left; p <= interval.right; ++p)
                                if (envelope[p] & (1u << bit))
                                    ++failed_weight[p][bit];
                        }
                    }
                    bits &= static_cast<Mask>(bits - 1);
                }
            }
            if (collect_hot) {
                // This is the incidence score in the pin-conflict
                // hypergraph: a chosen matching edge receives blame whenever
                // one of its omitted bits blocks a candidate pin of a failed
                // obligation.
                for (int left = 0; left < LOWER_TARGETS; ++left) {
                    const Interval interval = intervals[matching[left]];
                    const Mask omitted = static_cast<Mask>(FULL & ~targets[left]);
                    for (int p = interval.left; p <= interval.right; ++p) {
                        Mask bits = static_cast<Mask>(envelope[p] & omitted);
                        while (bits) {
                            const int bit = countr_zero(static_cast<unsigned>(bits));
                            blame[left] += failed_weight[p][bit];
                            bits &= static_cast<Mask>(bits - 1);
                        }
                    }
                }
                for (int left = 0; left < LOWER_TARGETS; ++left)
                    for (int repeat = 0; repeat < min(blame[left], 8); ++repeat)
                        measurement.hot_left.push_back(left);
            }
            return measurement;
        };

        MatchingMeasurement current_measurement = measure(left_match, true);
        MatchingScore current_score = current_measurement.score;
        MatchingScore best_score = current_score;
        vector<int> best_match = left_match;
        uint64_t hash = 0xcbf29ce484222325ULL;
        for (Mask value : row) hash = (hash ^ value) * 0x100000001b3ULL;
        mt19937_64 matching_random(hash);
        const int restarts = min(256, matching_trials / 256);
        for (int restart = 0; restart < restarts; ++restart) {
            vector<vector<int>> shuffled = edges;
            for (auto& list : shuffled) shuffle(list.begin(), list.end(), matching_random);
            vector<int> order(LOWER_TARGETS), trial_left(LOWER_TARGETS, -1);
            vector<int> trial_right(SHORT_INTERVALS, -1), seen(SHORT_INTERVALS);
            for (int left = 0; left < LOWER_TARGETS; ++left) order[left] = left;
            shuffle(order.begin(), order.end(), matching_random);
            int stamp = 0, matched = 0;
            auto augment = [&](auto&& self, int left) -> bool {
                for (int right : shuffled[left]) {
                    if (seen[right] == stamp) continue;
                    seen[right] = stamp;
                    if (trial_right[right] < 0 || self(self, trial_right[right])) {
                        trial_left[left] = right;
                        trial_right[right] = left;
                        return true;
                    }
                }
                return false;
            };
            for (int left : order) {
                ++stamp;
                matched += augment(augment, left);
            }
            if (matched != LOWER_TARGETS) continue;
            const MatchingScore score = measure(trial_left).score;
            if (score_better(score, best_score))
                best_score = score, best_match = std::move(trial_left);
        }
        left_match = best_match;
        fill(right_match.begin(), right_match.end(), -1);
        for (int left = 0; left < LOWER_TARGETS; ++left)
            right_match[left_match[left]] = left;
        current_measurement = measure(left_match, true);
        current_score = current_measurement.score;
        vector<uint8_t> used_left(LOWER_TARGETS), used_right(SHORT_INTERVALS);
        vector<int> chain_left, chain_right, old_right;
        for (int trial = 0; trial < matching_trials; ++trial) {
            if (!best_score.failures) break;
            chain_left.clear();
            chain_right.clear();
            fill(used_left.begin(), used_left.end(), 0);
            fill(used_right.begin(), used_right.end(), 0);
            const bool targeted = !current_measurement.hot_left.empty() &&
                matching_random() % 100 < 85;
            int left = targeted
                ? current_measurement.hot_left[
                    matching_random() % current_measurement.hot_left.size()]
                : matching_random() % LOWER_TARGETS;
            const int first_left = left;
            bool complete = false;
            for (int depth = 0; depth < 32; ++depth) {
                if (used_left[left] || edges[left].size() < 2) break;
                used_left[left] = 1;
                int right = -1;
                const int start = matching_random() % edges[left].size();
                for (int offset = 0; offset < static_cast<int>(edges[left].size()); ++offset) {
                    const int candidate = edges[left][(start + offset) % edges[left].size()];
                    if (candidate != left_match[left] && !used_right[candidate]) {
                        right = candidate;
                        break;
                    }
                }
                if (right < 0) break;
                used_right[right] = 1;
                chain_left.push_back(left);
                chain_right.push_back(right);
                const int next = right_match[right];
                if (next < 0) {
                    complete = true;
                    break;
                }
                // An alternating cycle is just as valid as an ejection path:
                // every left vertex remains matched and no right is repeated.
                if (next == first_left) {
                    complete = true;
                    break;
                }
                left = next;
            }
            if (!complete) continue;

            old_right.clear();
            for (int changed_left : chain_left) {
                old_right.push_back(left_match[changed_left]);
                right_match[left_match[changed_left]] = -1;
            }
            for (int i = 0; i < static_cast<int>(chain_left.size()); ++i) {
                left_match[chain_left[i]] = chain_right[i];
                right_match[chain_right[i]] = chain_left[i];
            }
            MatchingMeasurement next_measurement = measure(left_match, true);
            const MatchingScore& next_score = next_measurement.score;
            const bool nonworse = score_better(next_score, current_score) ||
                score_equal(next_score, current_score);
            const bool pressure_step =
                next_score.failures == current_score.failures &&
                next_score.pressure <= current_score.pressure + 1 &&
                matching_random() % 100 < 5;
            const bool conflict_step =
                next_score.failures == current_score.failures + 1 &&
                matching_random() % 100 < 1;
            const bool accept = nonworse || pressure_step || conflict_step;
            if (accept) {
                const bool improves_best = score_better(next_score, best_score);
                current_score = next_score;
                current_measurement = std::move(next_measurement);
                if (improves_best)
                    best_score = current_score, best_match = left_match;
            } else {
                for (int right : chain_right) right_match[right] = -1;
                for (int i = 0; i < static_cast<int>(chain_left.size()); ++i) {
                    left_match[chain_left[i]] = old_right[i];
                    right_match[old_right[i]] = chain_left[i];
                }
            }
        }
        left_match = std::move(best_match);
        fill(right_match.begin(), right_match.end(), -1);
        for (int left = 0; left < LOWER_TARGETS; ++left) {
            const int right = left_match[left];
            if (right < 0 || right >= SHORT_INTERVALS || right_match[right] >= 0 ||
                find(edges[left].begin(), edges[left].end(), right) == edges[left].end())
                throw logic_error("matching optimizer broke perfect-matching invariant");
            right_match[left_match[left]] = left;
        }
        result.matching_pin_conflicts = best_score.failures;
        result.matching_pin_pressure = best_score.pressure;
        result.matching_pin_slack = best_score.slack;
        result.matching_empty_positions = best_score.position_failures;
        result.matching_central_failures = best_score.central_failures;
        result.matching_target_failures = best_score.target_failures;

        array<array<uint16_t, K>, N> forbidden{};
        for (int left = 0; left < LOWER_TARGETS; ++left) {
            const Interval interval = intervals[left_match[left]];
            const Mask omitted = static_cast<Mask>(FULL & ~targets[left]);
            for (int p = interval.left; p <= interval.right; ++p) {
                Mask here = static_cast<Mask>(envelope[p] & omitted);
                while (here) {
                    const int bit = countr_zero(static_cast<unsigned>(here));
                    ++forbidden[p][bit];
                    here &= static_cast<Mask>(here - 1);
                }
            }
        }
        auto legal = [&](int position, int bit) {
            return (envelope[position] & (1u << bit)) && !forbidden[position][bit];
        };
        for (int p = 0; p < N; ++p) {
            bool nonzero = false;
            for (int bit = 0; bit < K; ++bit) nonzero |= legal(p, bit);
            if (!nonzero) failure_hot[p] = 1;
            if (!nonzero) result.pin_failures.push_back({'P', p, -1, {p, p}});
        }
        for (int i = 0; i < M; ++i) {
            Mask bits = row[i];
            while (bits) {
                const int bit = countr_zero(static_cast<unsigned>(bits));
                bool hit = false;
                for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p)
                    hit |= legal(p, bit);
                if (!hit)
                    for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p)
                        failure_hot[p] = 1;
                if (!hit) result.pin_failures.push_back({'C', i, bit, CENTRAL[i]});
                bits &= static_cast<Mask>(bits - 1);
            }
        }
        for (int left = 0; left < LOWER_TARGETS; ++left) {
            const Interval interval = intervals[left_match[left]];
            Mask bits = targets[left];
            while (bits) {
                const int bit = countr_zero(static_cast<unsigned>(bits));
                bool hit = false;
                for (int p = interval.left; p <= interval.right; ++p)
                    hit |= legal(p, bit);
                if (!hit)
                    for (int p = interval.left; p <= interval.right; ++p)
                        failure_hot[p] = 1;
                if (!hit)
                    result.pin_failures.push_back(
                        {'T', static_cast<int>(targets[left]), bit, interval});
                bits &= static_cast<Mask>(bits - 1);
            }
        }
    }

    vector<uint8_t> seen_left(LOWER_TARGETS), seen_right(SHORT_INTERVALS);
    queue<int> todo;
    for (int left = 0; left < LOWER_TARGETS; ++left)
        if (left_match[left] < 0) seen_left[left] = 1, todo.push(left);
    while (!todo.empty()) {
        const int left = todo.front();
        todo.pop();
        for (int right : edges[left]) {
            if (left_match[left] == right || seen_right[right]) continue;
            seen_right[right] = 1;
            const int next = right_match[right];
            if (next >= 0 && !seen_left[next]) seen_left[next] = 1, todo.push(next);
        }
    }
    array<uint8_t, N> hot = failure_hot;
    for (int right = 0; right < SHORT_INTERVALS; ++right) {
        if (!seen_right[right]) continue;
        for (int p = intervals[right].left; p <= intervals[right].right; ++p) hot[p] = 1;
    }
    for (int p = 0; p < N; ++p) if (hot[p]) result.hot_positions.push_back(p);

    array<uint8_t, LIMIT> upper_seen{};
    vector<Mask> previous, current;
    for (Mask x : row) {
        current.clear();
        current.push_back(x);
        for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (Mask value : current) upper_seen[value] = 1;
        previous.swap(current);
    }
    for (int mask = 1; mask < LIMIT; ++mask) {
        const int rank = pc(static_cast<Mask>(mask));
        if (rank >= 7 && !upper_seen[mask]) {
            ++result.upper_missing;
            ++result.upper_missing_by_rank[rank];
        }
    }
    return result;
}

static void print_evaluation(const string& prefix, const Evaluation& value) {
    cerr << prefix << " pin=" << value.pin_deficit
         << " d3=" << value.d3_distinct << "/323"
         << " projection=";
    if (value.projection_checked) cerr << value.projection_failures;
    else cerr << "NA";
    cerr
         << " empty_envelopes=" << value.empty_envelopes
         << " missing_pins=" << value.missing_central_pins
         << " hall=" << value.hall_deficit
         << " matching=" << value.hall_matching << "/1023"
         << " conflict=" << value.matching_pin_conflicts
         << " pressure=" << value.matching_pin_pressure
         << " slack=" << value.matching_pin_slack
         << "(position=" << value.matching_empty_positions
         << ",central=" << value.matching_central_failures
         << ",target=" << value.matching_target_failures << ')'
         << " empty_targets=" << value.empty_targets
         << " upper=" << value.upper_missing
         << " selectors=" << value.selectors << " upper_ranks";
    for (int rank = 7; rank <= K; ++rank)
        if (value.upper_missing_by_rank[rank])
            cerr << ' ' << rank << ':' << value.upper_missing_by_rank[rank];
    cerr << " seam_rank=" << value.seam_union_rank << '\n';
}

static void print_pin_failures(const Evaluation& value) {
    for (const auto& failure : value.pin_failures) {
        cerr << "failure kind=" << failure.kind << " owner=" << failure.owner;
        if (failure.bit >= 0) cerr << " bit=" << failure.bit;
        cerr << " interval=[" << failure.interval.left + 1 << ','
             << failure.interval.right + 1 << "]\n";
    }
}

static void scan_two_component_reversals(const vector<Mask>& seed,
                                         const string& output_path) {
    if (!rainbow_johnson_path(seed, true))
        throw runtime_error("two-opt seed fails two-component invariant");
    vector<Mask> best_row = seed;
    Evaluation best = evaluate(seed, 4096);
    print_evaluation("two_opt_seed", best);
    long long pairs = 0, joined = 0, valid = 0, evaluated = 0;
    const array<pair<int, int>, 2> components{{{0, SIGMA}, {SIGMA, M}}};
    for (const auto [begin, end] : components) {
        for (int left = begin; left < end; ++left) {
            for (int right = left + 2; right < end; ++right) {
                ++pairs;
                if (left > begin && !johnson_adjacent(seed[left - 1], seed[right]))
                    continue;
                if (right + 1 < end &&
                    !johnson_adjacent(seed[left], seed[right + 1]))
                    continue;
                ++joined;
                vector<Mask> candidate = seed;
                reverse(candidate.begin() + left, candidate.begin() + right + 1);
                if (!rainbow_johnson_path(candidate, true)) continue;
                ++valid;
                Evaluation value = evaluate(candidate, 256);
                ++evaluated;
                if (value.pin_deficit > best.pin_deficit ||
                    value.hall_deficit > best.hall_deficit ||
                    value.matching_pin_conflicts > best.matching_pin_conflicts + 8)
                    continue;
                value = evaluate(candidate, 4096);
                if (!better(value, best)) continue;
                best = std::move(value);
                best_row = std::move(candidate);
                write_row(output_path, best_row);
                print_evaluation("two_opt_best", best);
            }
        }
    }
    write_row(output_path, best_row);
    print_evaluation("two_opt_final", best);
    cerr << "two_opt_pairs=" << pairs << " joins=" << joined
         << " valid=" << valid << " evaluated=" << evaluated << '\n';
}

class Search {
public:
    Search(double seconds, int threads, string output, vector<vector<Mask>> seeds,
           bool two_component)
        : seconds_(seconds), threads_(threads), output_(std::move(output)),
          seeds_(std::move(seeds)), two_component_(two_component) {
        if (const char* trials = getenv("Q369_MATCHING_TRIALS"))
            matching_trials_ = max(0, stoi(trials));
        if (const char* trials = getenv("Q369_MATCHING_REFINE_TRIALS"))
            matching_refine_trials_ = max(matching_trials_, stoi(trials));
        matching_refine_trials_ = max(matching_refine_trials_, matching_trials_);
        if (const char* margin = getenv("Q369_MATCHING_REFINE_MARGIN"))
            matching_refine_margin_ = max(0, stoi(margin));
        if (const char* hook = getenv("Q369_PROJECTION_HOOK")) projection_hook_ = hook;
        if (const char* period = getenv("Q369_PROJECTION_PERIOD"))
            projection_period_ = max(1, stoi(period));
        cerr << "matching_config inner=" << matching_trials_
             << " refine=" << matching_refine_trials_
             << " margin=" << matching_refine_margin_ << '\n';
        for (const auto& seed : seeds_)
            if (!rainbow_johnson_path(seed, two_component_))
                throw runtime_error("seed is not a feasible rainbow Johnson structure");
        best_row_ = seeds_.front();
        best_eval_ = evaluate(best_row_, matching_refine_trials_);
        if (!projection_hook_.empty()) {
            best_eval_.projection_failures = projection_score(best_row_);
            best_eval_.projection_checked = true;
        }
        for (int seed_index = 0; seed_index < static_cast<int>(seeds_.size());
             ++seed_index) {
            const auto& seed = seeds_[seed_index];
            Evaluation value = seed_index
                ? evaluate(seed, matching_refine_trials_) : best_eval_;
            if (seed_index && !projection_hook_.empty()) {
                value.projection_failures = projection_score(seed);
                value.projection_checked = true;
            }
            print_evaluation("seed", value);
            if (better(value, best_eval_)) best_row_ = seed, best_eval_ = value;
        }
        write_row(output_, best_row_);
    }

    void run() {
        deadline_ = chrono::steady_clock::now() +
            chrono::milliseconds(static_cast<long long>(1000 * seconds_));
        vector<thread> pool;
        for (int id = 0; id < threads_; ++id) pool.emplace_back(&Search::worker, this, id);
        for (thread& worker : pool) worker.join();
        lock_guard<mutex> lock(best_mutex_);
        print_evaluation("final", best_eval_);
        write_row(output_, best_row_);
        cerr << "attempted=" << attempted_ << " valid_moves=" << valid_moves_
             << " evaluated=" << evaluated_ << '\n';
    }

private:
    double seconds_;
    int threads_;
    string output_;
    vector<vector<Mask>> seeds_;
    bool two_component_ = false;
    int matching_trials_ = 1024;
    int matching_refine_trials_ = 4096;
    int matching_refine_margin_ = 12;
    string projection_hook_;
    int projection_period_ = 250;
    vector<Mask> best_row_;
    Evaluation best_eval_;
    mutex best_mutex_;
    chrono::steady_clock::time_point deadline_;
    atomic<long long> attempted_{0}, valid_moves_{0}, evaluated_{0};
    atomic<long long> projection_candidates_{0}, projection_calls_{0};

    static string shell_quote(const string& value) {
        string result = "'";
        for (char c : value) {
            if (c == '\'') result += "'\\''";
            else result += c;
        }
        return result + "'";
    }

    int projection_score(const vector<Mask>& row) {
        const long long id = projection_calls_++;
        const string path = "/tmp/q369-projection-" + to_string(getpid()) + "-" +
            to_string(id) + ".txt";
        write_row(path, row);
        const string command = projection_hook_ + " " + shell_quote(path);
        FILE* pipe = popen(command.c_str(), "r");
        if (!pipe) {
            remove(path.c_str());
            throw runtime_error("cannot start Q369_PROJECTION_HOOK");
        }
        int score = -1;
        const int scanned = fscanf(pipe, "%d", &score);
        const int status = pclose(pipe);
        remove(path.c_str());
        if (status != 0 || scanned != 1 || score < 0)
            throw runtime_error("Q369_PROJECTION_HOOK failed");
        return score;
    }

    static bool reverse_move(vector<Mask>& row, const Evaluation& value,
                             mt19937_64& random, bool two_component) {
        const int n = row.size();
        for (int attempt = 0; attempt < 1200; ++attempt) {
            const bool targeted = !value.hot_positions.empty() && random() % 100 < 70;
            const int hot = targeted
                ? min(M - 1, value.hot_positions[random() % value.hot_positions.size()])
                : -1;
            int begin = 0, end = n;
            if (two_component) {
                const bool first_component = targeted ? hot < SIGMA : (random() & 1);
                if (first_component) end = SIGMA;
                else begin = SIGMA;
            }
            int left, right;
            if (targeted) {
                left = max(begin, min(end - 1,
                    hot + static_cast<int>(random() % 17) - 8));
                right = begin + random() % (end - begin);
            } else {
                left = begin + random() % (end - begin);
                right = begin + random() % (end - begin);
            }
            if (left > right) swap(left, right);
            if (right - left < 2 || (left == begin && right + 1 == end)) continue;
            if (left > begin && !johnson_adjacent(row[left - 1], row[right])) continue;
            if (right + 1 < end && !johnson_adjacent(row[left], row[right + 1])) continue;
            reverse(row.begin() + left, row.begin() + right + 1);
            if (rainbow_johnson_path(row, two_component)) return true;
            reverse(row.begin() + left, row.begin() + right + 1);
        }
        return false;
    }

    static bool relocate_move(vector<Mask>& row, const Evaluation& value,
                              mt19937_64& random, bool two_component) {
        const int n = row.size();
        for (int attempt = 0; attempt < 500; ++attempt) {
            const bool targeted = !value.hot_positions.empty() && random() % 100 < 70;
            const int hot = targeted
                ? min(M - 1, value.hot_positions[random() % value.hot_positions.size()])
                : -1;
            int begin = 0, end = n;
            if (two_component) {
                const bool first_component = targeted ? hot < SIGMA : (random() & 1);
                if (first_component) end = SIGMA;
                else begin = SIGMA;
            }
            const int component_size = end - begin;
            int length = 1 + random() % (random() % 10 ? 20 : 120);
            length = min(length, component_size - 2);
            int left;
            if (targeted) {
                left = max(begin, min(end - length,
                    hot - static_cast<int>(random() % length)));
            } else {
                left = begin + random() % (component_size - length + 1);
            }
            const int right = left + length;
            if (left > begin && right < end &&
                !johnson_adjacent(row[left - 1], row[right])) continue;

            vector<Mask> block(row.begin() + left, row.begin() + right);
            vector<Mask> reduced;
            reduced.reserve(component_size - length);
            reduced.insert(reduced.end(), row.begin() + begin, row.begin() + left);
            reduced.insert(reduced.end(), row.begin() + right, row.begin() + end);

            const int first_gap = random() % (reduced.size() + 1);
            for (int offset = 0; offset <= static_cast<int>(reduced.size()); ++offset) {
                const int gap = (first_gap + offset) % (reduced.size() + 1);
                for (int reversed = 0; reversed < 2; ++reversed) {
                    const Mask first = reversed ? block.back() : block.front();
                    const Mask last = reversed ? block.front() : block.back();
                    if (gap && !johnson_adjacent(reduced[gap - 1], first)) continue;
                    if (gap < static_cast<int>(reduced.size()) &&
                        !johnson_adjacent(last, reduced[gap])) continue;
                    vector<Mask> replacement = reduced;
                    if (!reversed)
                        replacement.insert(replacement.begin() + gap, block.begin(), block.end());
                    else
                        replacement.insert(replacement.begin() + gap, block.rbegin(), block.rend());
                    vector<Mask> candidate = row;
                    copy(replacement.begin(), replacement.end(), candidate.begin() + begin);
                    if (candidate == row ||
                        !rainbow_johnson_path(candidate, two_component)) continue;
                    row.swap(candidate);
                    return true;
                }
            }
        }
        return false;
    }

    static bool cross_swap_move(vector<Mask>& row, mt19937_64& random,
                                bool two_component) {
        if (!two_component) return false;
        for (int attempt = 0; attempt < 800; ++attempt) {
            const int length = 1 + random() % 16;
            const int left_p = random() % (SIGMA - length + 1);
            const int left_q = SIGMA + random() % (M - SIGMA - length + 1);
            vector<Mask> block_p(row.begin() + left_p, row.begin() + left_p + length);
            vector<Mask> block_q(row.begin() + left_q, row.begin() + left_q + length);
            for (int reverse_p = 0; reverse_p < 2; ++reverse_p)
                for (int reverse_q = 0; reverse_q < 2; ++reverse_q) {
                    vector<Mask> candidate = row;
                    for (int offset = 0; offset < length; ++offset) {
                        candidate[left_p + offset] = block_q[reverse_q ? length - 1 - offset : offset];
                        candidate[left_q + offset] = block_p[reverse_p ? length - 1 - offset : offset];
                    }
                    if (rainbow_johnson_path(candidate, true)) {
                        row.swap(candidate);
                        return true;
                    }
                }
        }
        return false;
    }

    void publish(const vector<Mask>& row, Evaluation value) {
        bool refine = false;
        {
            lock_guard<mutex> lock(best_mutex_);
            refine = value.pin_deficit <= best_eval_.pin_deficit &&
                value.hall_deficit <= best_eval_.hall_deficit &&
                value.matching_pin_conflicts <=
                    best_eval_.matching_pin_conflicts + matching_refine_margin_;
        }
        if (refine) {
            Evaluation refined = evaluate(row, matching_refine_trials_);
            // A longer randomized run need not retrace the cheap run.  Both
            // scores come from valid perfect matchings, so retaining the
            // better one is a sound matching portfolio and makes refinement
            // monotone rather than accidentally throwing information away.
            if (better_cheap(refined, value)) value = std::move(refined);
        }

        if (!projection_hook_.empty()) {
            bool should_test = false;
            {
                lock_guard<mutex> lock(best_mutex_);
                const long long candidate = projection_candidates_++;
                const bool exact_region = !value.pin_deficit && !value.d3_cut_deficit &&
                    !value.hall_deficit;
                const bool near = exact_region &&
                    value.matching_pin_conflicts <= best_eval_.matching_pin_conflicts +
                        matching_refine_margin_;
                should_test = better_cheap(value, best_eval_) ||
                    (near && candidate % projection_period_ == 0);
            }
            if (!should_test) return;
            try {
                value.projection_failures = projection_score(row);
                value.projection_checked = true;
            } catch (const exception& error) {
                lock_guard<mutex> lock(best_mutex_);
                cerr << "projection oracle error: " << error.what() << '\n';
                return;
            }
        }
        lock_guard<mutex> lock(best_mutex_);
        if (!better(value, best_eval_)) return;
        best_row_ = row;
        best_eval_ = value;
        write_row(output_, best_row_);
        print_evaluation("best", best_eval_);
    }

    void worker(int id) {
        mt19937_64 random(0x9e3779b97f4a7c15ULL * (id + 1) ^
            chrono::high_resolution_clock::now().time_since_epoch().count());
        uniform_real_distribution<double> uniform(0.0, 1.0);
        int epoch = 0;
        while (chrono::steady_clock::now() < deadline_) {
            vector<Mask> row;
            if (epoch++ % 4 == 0) {
                lock_guard<mutex> lock(best_mutex_);
                row = best_row_;
            } else {
                row = seeds_[random() % seeds_.size()];
            }
            Evaluation current = evaluate(row, matching_trials_);
            ++evaluated_;
            const int epoch_length = 2500;
            for (int iteration = 0; iteration < epoch_length &&
                 chrono::steady_clock::now() < deadline_; ++iteration) {
                vector<Mask> candidate = row;
                ++attempted_;
                const int move_type = random() % 100;
                bool moved = move_type < 60
                    ? reverse_move(candidate, current, random, two_component_)
                    : (move_type < 88
                        ? relocate_move(candidate, current, random, two_component_)
                        : cross_swap_move(candidate, random, two_component_));
                if (!moved) continue;
                ++valid_moves_;
                Evaluation next = evaluate(candidate, matching_trials_);
                ++evaluated_;
                publish(candidate, next);

                const long long old_cost = anneal_cost(current);
                const long long new_cost = anneal_cost(next);
                const double phase = static_cast<double>(iteration) / epoch_length;
                const double temperature = 15000000.0 * pow(1e-6, phase) + 100.0;
                if (new_cost <= old_cost ||
                    uniform(random) < exp(static_cast<double>(old_cost - new_cost) /
                                           temperature)) {
                    row.swap(candidate);
                    current = std::move(next);
                }
                if (!current.pin_deficit && !current.hall_deficit &&
                    !current.matching_pin_conflicts && current.upper_missing == 0) return;
            }
        }
    }
};

}  // namespace q369

int main(int argc, char** argv) {
    using namespace q369;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc == 3 && string(argv[1]) == "--evaluate") {
            const vector<Mask> row = read_row(argv[2]);
            cerr << "rainbow_johnson=" << rainbow_johnson_path(row) << '\n';
            print_evaluation("evaluation", evaluate(row));
            return 0;
        }
        if (argc == 3 && string(argv[1]) == "--evaluate-two") {
            const vector<Mask> row = read_row(argv[2]);
            cerr << "two_component=" << rainbow_johnson_path(row, true) << '\n';
            print_evaluation("evaluation", evaluate(row));
            return 0;
        }
        if (argc == 4 && string(argv[1]) == "--match-evaluate") {
            const vector<Mask> row = read_row(argv[2]);
            cerr << "rainbow_johnson=" << rainbow_johnson_path(row) << '\n';
            print_evaluation("evaluation", evaluate(row, stoi(argv[3])));
            return 0;
        }
        if (argc == 4 && string(argv[1]) == "--explain-two") {
            const vector<Mask> row = read_row(argv[2]);
            cerr << "two_component=" << rainbow_johnson_path(row, true) << '\n';
            const Evaluation value = evaluate(row, stoi(argv[3]));
            print_evaluation("evaluation", value);
            print_pin_failures(value);
            return 0;
        }
        if (argc == 4 && string(argv[1]) == "--scan-two-opt") {
            scan_two_component_reversals(read_row(argv[2]), argv[3]);
            return 0;
        }
        bool two_component = false;
        int first = 1;
        if (argc > 1 && string(argv[1]) == "--two-component") {
            two_component = true;
            first = 2;
        }
        if (argc < first + 4) {
            cerr << "usage: k11_q369_hall_search SECONDS THREADS OUTPUT SEED [SEED ...]\n"
                 << "       k11_q369_hall_search --two-component SECONDS THREADS OUTPUT SEED [SEED ...]\n"
                 << "       k11_q369_hall_search --evaluate ROW\n"
                 << "       k11_q369_hall_search --evaluate-two ROW\n"
                 << "       k11_q369_hall_search --match-evaluate ROW TRIALS\n"
                 << "       k11_q369_hall_search --explain-two ROW TRIALS\n"
                 << "       k11_q369_hall_search --scan-two-opt ROW OUTPUT\n";
            return 2;
        }
        const double seconds = stod(argv[first]);
        const int threads = stoi(argv[first + 1]);
        vector<vector<Mask>> seeds;
        for (int arg = first + 3; arg < argc; ++arg) seeds.push_back(read_row(argv[arg]));
        Search search(seconds, threads, argv[first + 2], std::move(seeds), two_component);
        search.run();
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
