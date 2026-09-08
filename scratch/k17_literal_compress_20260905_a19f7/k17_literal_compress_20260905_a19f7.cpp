#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using Mask = uint32_t;
using Count = int64_t;
using Word = std::vector<Mask>;
using Clock = std::chrono::steady_clock;

static void require(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

static Word read_word(const std::string& path, int k) {
    std::ifstream in(path);
    require(bool(in), "cannot read " + path);
    Word word;
    for (std::string token; in >> token;) {
        size_t used = 0;
        auto value = std::stoll(token, &used);
        require(used == token.size() && value > 0 && value < (1 << k),
                "invalid nonempty mask: " + token);
        word.push_back(Mask(value));
    }
    require(!word.empty(), "empty input word");
    return word;
}

static void write_word(const std::string& path, const Word& word) {
    std::ofstream out(path);
    require(bool(out), "cannot write " + path);
    for (size_t i = 0; i < word.size(); ++i) out << (i ? " " : "") << word[i];
    out << '\n';
    require(bool(out), "failed writing " + path);
}

struct Run {
    Mask mask;
    Count count;
};
using Profile = std::vector<Run>;

static void append(Profile& runs, Mask mask, Count count) {
    if (!runs.empty() && runs.back().mask == mask) runs.back().count += count;
    else runs.push_back({mask, count});
}

static std::vector<Count> suffix_counts(const Word& word, int k) {
    std::vector<Count> counts(1 << k);
    Profile previous, next;
    previous.reserve(k + 1);
    next.reserve(k + 1);
    for (Mask value : word) {
        if (!value) continue;  // Internal tombstones are not serialized letters.
        next.clear();
        append(next, value, 1);
        for (auto run : previous) append(next, run.mask | value, run.count);
        for (auto run : next) counts[run.mask] += run.count;
        previous.swap(next);
    }
    return counts;
}

// Each tree node aggregates both OR and the number of surviving positions.
// A profile traversal skips a whole node once its OR adds no new bit.
struct OrTree {
    int n, size = 1;
    std::vector<Mask> masks;
    std::vector<int> sizes;

    explicit OrTree(const Word& word) : n(int(word.size())) {
        while (size < n) size *= 2;
        masks.resize(2 * size);
        sizes.resize(2 * size);
        for (int i = 0; i < n; ++i) {
            masks[size + i] = word[i];
            sizes[size + i] = bool(word[i]);
        }
        for (int i = size - 1; i; --i) pull(i);
    }

    void pull(int p) {
        masks[p] = masks[2 * p] | masks[2 * p + 1];
        sizes[p] = sizes[2 * p] + sizes[2 * p + 1];
    }

    void set(int p, Mask value) {
        p += size;
        masks[p] = value;
        sizes[p] = bool(value);
        while ((p /= 2)) pull(p);
    }

    void visit(int p, int lo, int hi, int qlo, int qhi, bool reverse,
               Profile& result) const {
        if (!sizes[p] || hi <= qlo || qhi <= lo) return;
        if (qlo <= lo && hi <= qhi &&
            (result.back().mask | masks[p]) == result.back().mask) {
            result.back().count += sizes[p];
            return;
        }
        if (hi - lo == 1) {
            append(result, result.back().mask | masks[p], 1);
            return;
        }
        int mid = (lo + hi) / 2;
        if (reverse) {
            visit(2 * p + 1, mid, hi, qlo, qhi, reverse, result);
            visit(2 * p, lo, mid, qlo, qhi, reverse, result);
        } else {
            visit(2 * p, lo, mid, qlo, qhi, reverse, result);
            visit(2 * p + 1, mid, hi, qlo, qhi, reverse, result);
        }
    }

    Profile profile(int lo, int hi, bool reverse) const {
        Profile result;
        result.reserve(18);
        result.push_back({0, 1});  // The one empty prefix/suffix.
        visit(1, 0, size, lo, hi, reverse, result);
        return result;
    }

    int select(int order) const {
        if (order < 0 || order >= sizes[1]) return -1;
        int p = 1;
        while (p < size) {
            p *= 2;
            if (order >= sizes[p]) {
                order -= sizes[p];
                ++p;
            }
        }
        return p - size;
    }

    int before(int p) const {
        int total = 0;
        for (int lo = size, hi = size + p; lo < hi; lo /= 2, hi /= 2) {
            if (lo & 1) total += sizes[lo++];
            if (hi & 1) total += sizes[--hi];
        }
        return total;
    }

    int next(int p) const { return select(before(p + 1)); }
    int previous(int p) const { return select(before(p) - 1); }
};

struct State {
    int k;
    Word word;
    OrTree tree;
    std::vector<Count> counts, delta;
    std::vector<int> touched, missing, missing_index;
    std::vector<uint64_t> stamps;
    uint64_t stamp = 0;
    int new_missing = 0;
    double rarity_delta = 0;

    State(Word input, int bits)
        : k(bits), word(std::move(input)), tree(word), counts(suffix_counts(word, k)),
          delta(1 << k), missing_index(1 << k, -1), stamps(1 << k) {
        touched.reserve(1024);
        for (int mask = 1; mask < (1 << k); ++mask) {
            if (!counts[mask]) {
                missing_index[mask] = int(missing.size());
                missing.push_back(mask);
            }
        }
    }

    Word compact() const {
        Word result;
        result.reserve(tree.sizes[1]);
        for (auto value : word) if (value) result.push_back(value);
        return result;
    }

    void add(Mask mask, Count amount) {
        if (!amount) return;
        require(mask != 0, "empty interval in delta");
        if (stamps[mask] != stamp) {
            stamps[mask] = stamp;
            delta[mask] = 0;
            touched.push_back(int(mask));
        }
        delta[mask] += amount;
    }

    // This partitions affected intervals into internal, left-prefix,
    // suffix-right, and left-to-right classes. All untouched intervals cancel.
    void boundary_delta(const Word& block, const Profile& left,
                        const Profile& right, int sign) {
        for (size_t i = 0; i < block.size(); ++i) {
            Mask value = 0;
            for (size_t j = i; j < block.size(); ++j) {
                value |= block[j];
                add(value, sign);
            }
        }
        Mask value = 0;
        for (auto letter : block) {
            value |= letter;
            for (size_t i = 1; i < left.size(); ++i)
                add(left[i].mask | value, sign * left[i].count);
        }
        value = 0;
        for (auto i = block.rbegin(); i != block.rend(); ++i) {
            value |= *i;
            for (size_t j = 1; j < right.size(); ++j)
                add(right[j].mask | value, sign * right[j].count);
        }
    }

    int trial(int lo, int hi, const Word& replacement) {
        ++stamp;
        touched.clear();
        Word old;
        for (int p = lo; p >= 0 && p <= hi; p = tree.next(p)) old.push_back(word[p]);
        require(!old.empty() && word[lo] && word[hi] && replacement.size() <= old.size(),
                "invalid replacement positions");
        for (auto value : replacement)
            require(value && value < (1u << k), "invalid replacement letter");
        auto left = tree.profile(0, lo, true);
        auto right = tree.profile(hi + 1, int(word.size()), false);
        boundary_delta(old, left, right, -1);
        boundary_delta(replacement, left, right, 1);
        Mask old_or = 0, new_or = 0;
        for (auto value : old) old_or |= value;
        for (auto value : replacement) new_or |= value;
        if (old_or != new_or) {
            for (size_t i = 1; i < left.size(); ++i) {
                for (size_t j = 1; j < right.size(); ++j) {
                    Mask outside = left[i].mask | right[j].mask;
                    if ((outside | old_or) == (outside | new_or)) continue;
                    Count ways = left[i].count * right[j].count;
                    add(outside | old_or, -ways);
                    add(outside | new_or, ways);
                }
            }
        }
        new_missing = int(missing.size());
        rarity_delta = 0;
        for (int mask : touched) {
            auto after = counts[mask] + delta[mask];
            require(after >= 0, "negative exact multiplicity");
            new_missing += int(after == 0) - int(counts[mask] == 0);
            // Soft tie-break only; exact zero multiplicities define feasibility.
            rarity_delta += (after ? 1.0 / after : 2.0) -
                            (counts[mask] ? 1.0 / counts[mask] : 2.0);
        }
        return new_missing;
    }

    void commit(int lo, int hi, const Word& replacement) {
        for (int mask : touched) {
            Count after = counts[mask] + delta[mask];
            if (counts[mask] && !after) {
                missing_index[mask] = int(missing.size());
                missing.push_back(mask);
            } else if (!counts[mask] && after) {
                int index = missing_index[mask];
                missing[index] = missing.back();
                missing_index[missing[index]] = index;
                missing.pop_back();
                missing_index[mask] = -1;
            }
            counts[mask] = after;
        }
        size_t i = 0;
        for (int p = lo; p >= 0 && p <= hi;) {
            int next = tree.next(p);
            word[p] = i < replacement.size() ? replacement[i++] : 0;
            tree.set(p, word[p]);
            p = next;
        }
        require(int(missing.size()) == new_missing, "missing-list mismatch");
    }

    void audit() const {
        require(counts == suffix_counts(word, k), "incremental/full counts disagree");
        Count total = std::accumulate(counts.begin(), counts.end(), Count(0));
        Count n = tree.sizes[1];
        require(total == n * (n + 1) / 2, "interval count total mismatch");
    }
};

static std::vector<Count> brute_counts(const Word& word, int k) {
    std::vector<Count> result(1 << k);
    for (size_t i = 0; i < word.size(); ++i) {
        Mask value = 0;
        for (size_t j = i; j < word.size(); ++j) ++result[value |= word[j]];
    }
    return result;
}

static void self_test() {
    std::mt19937_64 rng(20260905);
    uint64_t tested = 0;
    for (int sample = 0; sample < 3000; ++sample) {
        int k = 1 + int(rng() % 7), n = 1 + int(rng() % 25);
        Word word(n);
        for (auto& value : word) value = 1 + Mask(rng() % ((1 << k) - 1));
        State state(word, k);
        require(state.counts == brute_counts(word, k), "initial count test failed");
        for (int step = 0; step < 24 && state.tree.sizes[1]; ++step) {
            int lo = state.tree.select(int(rng() % state.tree.sizes[1]));
            int hi = lo;
            if ((rng() & 1) && state.tree.next(lo) >= 0) hi = state.tree.next(lo);
            Word replacement;
            switch (rng() % 5) {
                case 0: break;
                case 1: replacement = {state.word[lo] | state.word[hi]}; break;
                case 2: replacement = {1 + Mask(rng() % ((1 << k) - 1))}; break;
                default:
                    replacement = {state.word[hi]};
                    if (hi != lo) replacement.push_back(state.word[lo]);
            }
            Word expected;
            for (int p = 0; p < int(state.word.size()); ++p) {
                if (p == lo) expected.insert(expected.end(), replacement.begin(), replacement.end());
                if ((p < lo || p > hi) && state.word[p]) expected.push_back(state.word[p]);
            }
            auto counts = brute_counts(expected, k);
            state.trial(lo, hi, replacement);
            auto predicted = state.counts;
            for (int mask : state.touched) predicted[mask] += state.delta[mask];
            require(predicted == counts, "local delta/brute-force mismatch");
            ++tested;
            if (rng() % 3 == 0) {
                state.commit(lo, hi, replacement);
                require(state.compact() == expected, "committed word mismatch");
                state.audit();
            }
        }
    }
    Word repeated(100000, 1);
    auto large = suffix_counts(repeated, 1);
    require(large[1] == 5000050000LL, "64-bit multiplicity test failed");
    std::cout << "SELF_TEST_PASS delta_cases=" << tested
              << " repeated_intervals=" << large[1] << '\n';
}

struct Move {
    int lo, hi, damage;
    Word replacement;
};

static std::vector<Move> census(State& state, const std::string& prefix) {
    require(state.missing.empty(), "census requires a universal word");
    std::ofstream out(prefix + ".census.tsv");
    out << "operation\tposition\tright_position\tletter\tmissing\tlost_targets\n";
    std::array<std::map<int, int>, 2> histogram;
    std::array<std::array<uint64_t, 18>, 2> lost_by_rank{};
    std::vector<Move> moves;
    for (int p = state.tree.select(0); p >= 0; p = state.tree.next(p)) {
        for (int kind = 0; kind < 2; ++kind) {
            int q = kind ? state.tree.next(p) : p;
            if (q < 0) continue;
            Word replacement = kind ? Word{state.word[p] | state.word[q]} : Word{};
            int damage = state.trial(p, q, replacement);
            ++histogram[kind][damage];
            out << (kind ? "merge" : "delete") << '\t' << p << '\t' << q << '\t'
                << state.word[p] << '\t' << damage << '\t';
            bool first = true;
            for (int mask : state.touched) {
                if (state.counts[mask] && state.counts[mask] + state.delta[mask] == 0) {
                    ++lost_by_rank[kind][__builtin_popcount(unsigned(mask))];
                    out << (first ? "" : ",") << mask;
                    first = false;
                }
            }
            out << '\n';
            if (damage <= 8) moves.push_back({p, q, damage, std::move(replacement)});
        }
    }
    for (int kind = 0; kind < 2; ++kind) {
        std::cout << "CENSUS operation=" << (kind ? "merge" : "delete") << " histogram=";
        for (auto [damage, number] : histogram[kind]) std::cout << damage << ':' << number << ',';
        std::cout << " lost_by_rank=";
        for (int rank = 1; rank <= state.k; ++rank)
            if (lost_by_rank[kind][rank]) std::cout << rank << ':' << lost_by_rank[kind][rank] << ',';
        std::cout << '\n';
    }
    std::cout << "MULTIPLICITY unique_witness_by_rank=";
    std::array<int, 18> unique{};
    for (int mask = 1; mask < (1 << state.k); ++mask)
        if (state.counts[mask] == 1) ++unique[__builtin_popcount(unsigned(mask))];
    for (int rank = 1; rank <= state.k; ++rank) std::cout << rank << ':' << unique[rank] << ',';
    std::cout << '\n';
    std::sort(moves.begin(), moves.end(), [](const Move& a, const Move& b) {
        return a.damage < b.damage;
    });
    return moves;
}

// Keep a few actual initial witness endpoints per target to focus repair.
static std::vector<std::vector<int>> witness_positions(const Word& word, int k) {
    std::vector<std::vector<int>> witnesses(1 << k);
    std::vector<std::pair<Mask, int>> previous, next;
    for (int p = 0; p < int(word.size()); ++p) {
        next = {{word[p], p}};
        for (auto [mask, start] : previous) {
            mask |= word[p];
            if (mask != next.back().first) next.push_back({mask, start});
        }
        for (auto [mask, start] : next) {
            if (witnesses[mask].size() < 8) {
                witnesses[mask].push_back(start);
                witnesses[mask].push_back(p);
            }
        }
        previous.swap(next);
    }
    return witnesses;
}

static void search(const Word& initial, int k, double seconds, uint64_t seed,
                   const std::string& prefix) {
    const auto start = Clock::now();
    auto elapsed = [&] { return std::chrono::duration<double>(Clock::now() - start).count(); };
    std::mt19937_64 rng(seed);
    State state(initial, k);
    require(state.missing.empty(), "input is not literal OR-universal");
    auto moves = census(state, prefix);
    state.audit();
    if (seconds <= 0) return;
    Word best = initial;
    auto witnesses = witness_positions(initial, k);
    uint64_t trials = 0, accepted = 0, episodes = 0, improvements = 0;
    int episode_best = 1 << k, global_best_missing = 1 << k;
    double next_log = 20;
    std::ofstream trajectory(prefix + ".trajectory.tsv");
    trajectory << "seconds\tepisode\tlength\tmissing\ttrials\taccepted\n";
    std::vector<int> hot;
    auto record_best = [&] {
        if (state.missing.empty() && state.tree.sizes[1] < int(best.size())) {
            state.audit();
            best = state.compact();
            auto checked = suffix_counts(best, k);
            require(std::none_of(checked.begin() + 1, checked.end(),
                                 [](Count count) { return count == 0; }),
                    "candidate failed full suffix-OR verification");
            write_word(prefix + ".best.word", best);
            ++improvements;
            std::cout << "IMPROVEMENT length=" << best.size() << " covered=" << ((1 << k) - 1)
                      << " seconds=" << elapsed() << std::endl;
        }
    };
    auto record_near = [&] {
        int holes = int(state.missing.size());
        if (holes < global_best_missing) {
            global_best_missing = holes;
            if (holes) {
                state.audit();
                write_word(prefix + ".near.word", state.compact());
            }
        }
    };

    // Every episode starts at a universal incumbent, deletes/merges one cell,
    // then repairs the exact missing masks with local nonempty-mask rewrites.
    while (elapsed() < seconds) {
        ++episodes;
        state = State(best, k);
        hot.clear();
        Move selected{};
        bool selected_move = false;
        int smallest = 1 << k;
        for (int probe = 0; probe < 64; ++probe) {
            int p, q;
            Word replacement;
            if (best.size() == initial.size() && !moves.empty() && probe < 48) {
                size_t pool = std::min(moves.size(), size_t(128 + (episodes % 16) * 512));
                const auto& move = moves[rng() % pool];
                p = move.lo;
                q = move.hi;
                replacement = move.replacement;
            } else {
                p = int(rng() % best.size());
                q = p;
                if ((rng() & 1) && p + 1 < int(best.size())) {
                    q = p + 1;
                    replacement = {best[p] | best[q]};
                }
            }
            // The unmarked copy is already a k=16 optimum. In this bounded
            // lift attempt, start on the marked side and keep the bare new bit.
            Mask lift_bit = 1u << (k - 1);
            if (!(state.word[p] & lift_bit) || state.word[p] == lift_bit) continue;
            int damage = state.trial(p, q, replacement);
            ++trials;
            if (damage < smallest || (damage == smallest && rng() % 4 == 0)) {
                selected = {p, q, damage, replacement};
                selected_move = true;
                smallest = damage;
            }
            if (smallest == 0) break;
        }
        if (!selected_move) break;
        state.trial(selected.lo, selected.hi, selected.replacement);
        state.commit(selected.lo, selected.hi, selected.replacement);
        for (int p = std::max(0, selected.lo - 12);
             p <= std::min(int(best.size()) - 1, selected.hi + 12); ++p) hot.push_back(p);
        episode_best = int(state.missing.size());
        record_near();
        if (state.missing.empty()) {
            record_best();
            witnesses = witness_positions(best, k);
            continue;
        }
        const int step_limit = 1000 + int(episodes % 4) * 1000;
        for (int step = 0; step < step_limit && elapsed() < seconds; ++step) {
            Mask target = Mask(state.missing[rng() % state.missing.size()]);
            int p;
            const auto& positions = witnesses[target];
            if (!positions.empty() && rng() % 5 != 0) {
                p = positions[rng() % positions.size()] + int(rng() % 13) - 6;
            } else {
                p = hot[rng() % hot.size()];
            }
            p = std::clamp(p, 0, int(state.word.size()) - 1);
            if (!state.word[p]) p = state.tree.next(p);
            if (p < 0) continue;
            int q = p;
            Word replacement;
            unsigned mode = unsigned(rng() % 10);
            if (mode < 5) {
                auto left = state.tree.profile(0, p, true);
                auto right = state.tree.profile(p + 1, int(state.word.size()), false);
                Mask context = 0;
                for (size_t j = 1; j < left.size() && !(left[j].mask & ~target); ++j)
                    context |= left[j].mask;
                for (size_t j = 1; j < right.size() && !(right[j].mask & ~target); ++j)
                    context |= right[j].mask;
                Mask value = (state.word[p] & target) | (target & ~context);
                if (mode == 0) value = target & ~context;
                if (!value) value = target & -target;
                replacement = {value};
            } else if (mode < 8 && state.tree.next(p) >= 0) {
                q = state.tree.next(p);
                Mask a = state.word[p], b = state.word[q];
                if (mode == 5) replacement = {b, a};
                else {
                    Mask bit = 1u << (rng() % k);
                    if (mode == 6) replacement = {a ^ (b & bit), b ^ (a & bit)};
                    else replacement = {a | (b & bit), b & ~bit};
                    if (!replacement[0] || !replacement[1]) continue;
                }
            } else {
                Mask value = state.word[p] ^ (1u << (rng() % k));
                if (!value) continue;
                replacement = {value};
            }
            if (q == p && replacement[0] == state.word[p]) continue;
            int old_missing = int(state.missing.size());
            int new_missing = state.trial(p, q, replacement);
            ++trials;
            double temperature = (0.06 + 0.14 * (seed % 4)) *
                                 (1.0 - 0.8 * double(step) / step_limit);
            double cost = new_missing - old_missing + 0.015 * state.rarity_delta;
            double uniform = std::generate_canonical<double, 53>(rng);
            bool take = new_missing <= std::min(12, episode_best + 5) &&
                        (new_missing == 0 || cost <= 0 || uniform < std::exp(-cost / temperature));
            if (take) {
                state.commit(p, q, replacement);
                ++accepted;
                hot.push_back(p);
                if (hot.size() > 512) hot.erase(hot.begin(), hot.begin() + 128);
                episode_best = std::min(episode_best, new_missing);
                record_near();
                if (!new_missing) {
                    record_best();
                    witnesses = witness_positions(best, k);
                    break;
                }
            }
            if ((trials & 65535) == 0) state.audit();
        }
        if (episodes <= 32 || elapsed() >= next_log) {
            trajectory << elapsed() << '\t' << episodes << '\t' << state.tree.sizes[1] << '\t'
                       << episode_best << '\t' << trials << '\t' << accepted << '\n';
            trajectory.flush();
        }
        if (elapsed() >= next_log) {
            state.audit();
            std::cout << "PROGRESS seconds=" << elapsed() << " episodes=" << episodes
                      << " trials=" << trials << " accepted=" << accepted
                      << " best_length=" << best.size() << " best_missing_at_shorter="
                      << global_best_missing << std::endl;
            next_log += 20;
        }
    }
    state.audit();
    std::cout << "FINAL seed=" << seed << " seconds=" << elapsed() << " episodes=" << episodes
              << " trials=" << trials << " accepted=" << accepted << " improvements=" << improvements
              << " initial_length=" << initial.size() << " best_length=" << best.size()
              << " best_missing_at_shorter=" << global_best_missing << std::endl;
}

int main(int argc, char** argv) {
    try {
        std::cout << std::setprecision(9);
        if (argc == 2 && std::string(argv[1]) == "--self-test") {
            self_test();
            return 0;
        }
        require(argc == 7, "usage: compressor K INPUT OUTPUT_PREFIX SECONDS SEED search|census");
        int k = std::stoi(argv[1]);
        require(k >= 1 && k <= 17, "supported k is 1..17");
        auto word = read_word(argv[2], k);
        std::string mode = argv[6];
        require(mode == "search" || mode == "census", "invalid mode");
        search(word, k, mode == "census" ? 0 : std::stod(argv[4]), std::stoull(argv[5]), argv[3]);
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "ERROR " << error.what() << '\n';
        return 1;
    }
}
