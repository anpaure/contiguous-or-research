// Isolated partial compiler. Reuse the audited exact edit/count engine only;
// the old baseline search entry point is never called.
#define main k17_partial_unused_compressor_main
#include "k17_literal_compress_20260905_a19f7.cpp"
#undef main

#include <functional>
#include <queue>
#include <set>
#include <unistd.h>

static constexpr int K = 17, FULL = (1 << K) - 1, W = 24310;
using Hist = std::array<int, K + 1>;
using Cycles = std::vector<Word>;

static int rank_of(Mask x) { return __builtin_popcount(x); }

template<class T> static void json_array(std::ostream& out, const T& values) {
    out << '[';
    bool first = true;
    for (auto value : values) {
        out << (first ? "" : ",") << value;
        first = false;
    }
    out << ']';
}

static Hist missing_hist(const std::vector<Count>& counts) {
    Hist result{};
    for (int x = 1; x <= FULL; ++x) if (!counts[x]) ++result[rank_of(x)];
    return result;
}

static int holes(const std::vector<Count>& counts) {
    return int(std::count(counts.begin() + 1, counts.end(), Count(0)));
}

static Mask rotate_mask(Mask x, int shift) {
    return shift ? ((x << shift) | (x >> (K - shift))) & FULL : x;
}

static Cycles read_factor(const std::string& path) {
    std::ifstream in(path);
    std::string magic;
    int k, n, w, d;
    require(bool(in >> magic >> k >> n >> w >> d), "factor header missing");
    require(magic == "K17QF1" && k == K && n == 1430 && w == W && d == 3,
            "wrong factor instance");
    std::vector<Word> adjacency(FULL + 1);
    std::vector<int> facets(FULL + 1);
    for (int row = 0; row < n; ++row) {
        Mask low;
        int a, b;
        require(bool(in >> low >> a >> b), "factor row missing");
        require(low <= FULL && rank_of(low) == 8 && a >= 0 && a < K &&
                b >= 0 && b < K && a != b && !(low & ((1u << a) | (1u << b))),
                "bad factor row");
        for (int shift = 0; shift < K; ++shift) {
            Mask u = rotate_mask(low | (1u << a), shift);
            Mask v = rotate_mask(low | (1u << b), shift);
            adjacency[u].push_back(v);
            adjacency[v].push_back(u);
            ++facets[u & v];
        }
    }
    std::string extra;
    require(!(in >> extra), "extra factor tokens");
    for (int x = 1; x <= FULL; ++x) {
        if (rank_of(x) == 8) require(facets[x] == 1, "rank-eight facet not rainbow");
        if (rank_of(x) == 9) {
            require(adjacency[x].size() == 2 && adjacency[x][0] != adjacency[x][1],
                    "rank-nine owner not degree two");
            std::sort(adjacency[x].begin(), adjacency[x].end());
        } else require(adjacency[x].empty(), "wrong owner rank");
    }
    std::vector<bool> seen(FULL + 1);
    Cycles result;
    for (int start = 1; start <= FULL; ++start) {
        if (adjacency[start].empty() || seen[start]) continue;
        Word cycle;
        Mask previous = 0, current = start;
        while (!seen[current]) {
            seen[current] = true;
            cycle.push_back(current);
            Mask next = adjacency[current][0];
            if (next == previous) next = adjacency[current][1];
            previous = current;
            current = next;
        }
        require(current == Mask(start) && cycle.size() >= 3, "cycle does not close");
        result.push_back(std::move(cycle));
    }
    std::sort(result.begin(), result.end(), [](const Word& a, const Word& b) {
        return a.size() != b.size() ? a.size() > b.size() : a[0] < b[0];
    });
    return result;
}

static Word derivative(const Word& row) {
    Word result(row.size());
    for (size_t i = 0; i < row.size(); ++i) result[i] = row[i] | row[(i + 1) % row.size()];
    return result;
}

static Word erosion(const Word& cycle) {
    Word p(cycle.size(), FULL);
    for (size_t i = 0; i < p.size(); ++i)
        for (int age = 0; age <= 3; ++age) p[i] &= cycle[(i + p.size() - age) % p.size()];
    auto row = p;
    for (int depth = 0; depth <= 3; ++depth) {
        for (Mask x : row) require(rank_of(x) == 6 + depth, "erosion row rank failure");
        if (depth < 3) row = derivative(row);
    }
    require(row == cycle, "D^3 P differs from literal carrier");
    return p;
}

// Minimum vertex covers of each positive run, with its endpoints forced.
// This is the path DP from graded_quotient_pipeline, independently per trace.
static std::vector<int> cover_pattern(int length, std::mt19937_64& rng, bool randomize) {
    require(length > 0, "empty positive run");
    if (length == 1) return {1};
    std::vector<std::array<int, 2>> dp(length + 1, {length + 1, length + 1});
    dp[length] = {0, 0};
    for (int i = length - 1; i >= 1; --i)
        for (int previous = 0; previous <= 1; ++previous)
            for (int bit = 0; bit <= 1; ++bit)
                if ((previous || bit) && (i != length - 1 || bit))
                    dp[i][previous] = std::min(dp[i][previous], bit + dp[i + 1][bit]);
    std::vector<int> answer{1};
    for (int i = 1; i < length; ++i) {
        std::vector<int> choices;
        for (int bit = 0; bit <= 1; ++bit)
            if ((answer.back() || bit) && (i != length - 1 || bit) &&
                bit + dp[i + 1][bit] == dp[i][answer.back()]) choices.push_back(bit);
        answer.push_back(choices[randomize ? rng() % choices.size() : choices.size() - 1]);
    }
    return answer;
}

static Word make_core(const Word& p, std::mt19937_64& rng, bool randomize) {
    int n = int(p.size());
    Word core(n);
    for (int bit = 0; bit < K; ++bit) {
        int zero = 0;
        while (zero < n && (p[zero] & (1u << bit))) ++zero;
        // The resident factors have no constant coordinates. Handle a constant
        // trace as a cyclic cover rather than incorrectly forcing path ends.
        if (zero == n) {
            int phase = randomize ? int(rng() % n) : 0;
            for (int i = 0; i < n; i += 2) core[(phase + i) % n] |= 1u << bit;
            continue;
        }
        std::vector<int> run;
        for (int step = 1; step <= n; ++step) {
            int pos = (zero + step) % n;
            if (p[pos] & (1u << bit)) run.push_back(pos);
            else if (!run.empty()) {
                auto pattern = cover_pattern(int(run.size()), rng, randomize);
                for (size_t j = 0; j < run.size(); ++j) if (pattern[j]) core[run[j]] |= 1u << bit;
                run.clear();
            }
        }
    }
    require(derivative(core) == derivative(p), "core does not preserve DP");
    for (size_t i = 0; i < p.size(); ++i) require(!(core[i] & ~p[i]), "core escapes P");
    return core;
}

struct Matching {
    std::vector<int> left, right, distance;
    int cardinality = 0, cover_size = 0;

    Matching(const std::vector<std::vector<int>>& adjacency, int positions)
        : left(adjacency.size(), -1), right(positions, -1), distance(adjacency.size()) {
        std::function<bool(int)> dfs = [&](int u) {
            for (int v : adjacency[u]) {
                int mate = right[v];
                if (mate < 0 || (distance[mate] == distance[u] + 1 && dfs(mate))) {
                    left[u] = v;
                    right[v] = u;
                    return true;
                }
            }
            distance[u] = -1;
            return false;
        };
        for (;;) {
            std::queue<int> queue;
            std::fill(distance.begin(), distance.end(), -1);
            for (int u = 0; u < int(left.size()); ++u) if (left[u] < 0) {
                distance[u] = 0;
                queue.push(u);
            }
            bool augment = false;
            while (!queue.empty()) {
                int u = queue.front();
                queue.pop();
                for (int v : adjacency[u]) {
                    int mate = right[v];
                    if (mate < 0) augment = true;
                    else if (distance[mate] < 0) {
                        distance[mate] = distance[u] + 1;
                        queue.push(mate);
                    }
                }
            }
            if (!augment) break;
            for (int u = 0; u < int(left.size()); ++u)
                if (left[u] < 0 && dfs(u)) ++cardinality;
        }
        // An equal-size vertex cover certifies maximum, not merely maximal.
        std::vector<bool> reachable_right(positions);
        for (int u = 0; u < int(left.size()); ++u)
            if (distance[u] >= 0) for (int v : adjacency[u]) reachable_right[v] = true;
        for (int u = 0; u < int(left.size()); ++u) cover_size += distance[u] < 0;
        for (int v = 0; v < positions; ++v) {
            cover_size += reachable_right[v];
            require(!reachable_right[v] || right[v] >= 0, "augmenting path remains");
        }
        require(cover_size == cardinality, "matching/vertex-cover cardinalities differ");
        for (int u = 0; u < int(left.size()); ++u)
            for (int v : adjacency[u])
                require(distance[u] < 0 || reachable_right[v], "uncovered Hall edge");
    }
};

struct Compiled {
    Cycles p, core, word, assigned;
    int matched = 0, cover_size = 0, zero_degree = 0;
    Hist unmatched{}, zero_by_rank{};
};

static Compiled compile(const Cycles& cycles, std::mt19937_64& rng, bool randomize) {
    Compiled result;
    Word targets;
    std::vector<int> index(FULL + 1, -1);
    for (int x = 1; x <= FULL; ++x) if (rank_of(x) <= 6) targets.push_back(x);
    if (randomize) std::shuffle(targets.begin(), targets.end(), rng);
    require(targets.size() == 21777, "lower target mass");
    for (int i = 0; i < int(targets.size()); ++i) index[targets[i]] = i;
    std::vector<std::vector<int>> adjacency(targets.size());
    int pos = 0;
    for (const auto& cycle : cycles) {
        result.p.push_back(erosion(cycle));
        result.core.push_back(make_core(result.p.back(), rng, randomize));
        Word word, assigned(cycle.size());
        for (size_t i = 0; i < cycle.size(); ++i, ++pos) {
            Mask low = result.core.back()[i], high = result.p.back()[i], free = high & ~low;
            for (Mask s = free;; s = (s - 1) & free) {
                Mask x = low | s;
                if (x) adjacency[index[x]].push_back(pos);
                if (!s) break;
            }
            word.push_back(low ? low : high & -high);
        }
        result.word.push_back(std::move(word));
        result.assigned.push_back(std::move(assigned));
    }
    require(pos == W, "wrong physical size");
    for (size_t u = 0; u < targets.size(); ++u) {
        if (adjacency[u].empty()) {
            ++result.zero_degree;
            ++result.zero_by_rank[rank_of(targets[u])];
        }
        if (randomize) std::shuffle(adjacency[u].begin(), adjacency[u].end(), rng);
    }
    Matching matching(adjacency, W);
    result.matched = matching.cardinality;
    result.cover_size = matching.cover_size;
    for (size_t u = 0; u < targets.size(); ++u)
        if (matching.left[u] < 0) ++result.unmatched[rank_of(targets[u])];
    pos = 0;
    for (size_t c = 0; c < cycles.size(); ++c) {
        for (size_t i = 0; i < cycles[c].size(); ++i, ++pos) {
            int u = matching.right[pos];
            if (u >= 0) result.word[c][i] = result.assigned[c][i] = targets[u];
        }
        require(derivative(result.word[c]) == derivative(result.p[c]), "DA != DP");
    }
    return result;
}

static std::vector<Count> cyclic_counts(const Cycles& cycles) {
    std::vector<Count> got(FULL + 1);
    for (auto cycle : cycles) {
        auto copy = cycle;
        cycle.insert(cycle.end(), copy.begin(), copy.end());
        auto counts = suffix_counts(cycle, K);
        // Intervals longer than one turn add no masks: their OR is the
        // component's total OR, already witnessed by exactly one turn.
        for (int x = 1; x <= FULL; ++x) got[x] += counts[x];
    }
    return got;
}

struct Opened {
    Word word;
    std::vector<int> order, cuts, reverse;
    std::vector<Count> counts;
};

static Opened open_cycles(const Cycles& cycles, std::mt19937_64& rng, int trials) {
    Opened best;
    for (int trial = 0; trial < trials; ++trial) {
        Opened next;
        next.order.resize(cycles.size());
        std::iota(next.order.begin(), next.order.end(), 0);
        if (trial) std::shuffle(next.order.begin(), next.order.end(), rng);
        for (int c : next.order) {
            int n = int(cycles[c].size()), cut = trial ? int(rng() % n) : 0;
            bool reverse = trial && (rng() & 1);
            next.cuts.push_back(cut);
            next.reverse.push_back(reverse);
            for (int i = 0; i < n + 3; ++i)
                next.word.push_back(cycles[c][(cut + (reverse ? n - i % n : i)) % n]);
        }
        next.counts = suffix_counts(next.word, K);
        if (best.word.empty() || holes(next.counts) < holes(best.counts)) best = std::move(next);
    }
    return best;
}

static Word next_suffix(const Word& previous, Mask letter) {
    Word result{letter};
    for (Mask x : previous) if ((x | letter) != result.back()) result.push_back(x | letter);
    return result;
}

struct Repair {
    Word word;
    int greedy_letters = 0, pruned_letters = 0, fallback_letters = 0;
    std::array<int, 18> gains{};
};

static Repair repair(const Opened& base, std::mt19937_64& rng, int mode,
                     Clock::time_point deadline) {
    Repair result;
    result.word = base.word;
    Word suffix;
    for (Mask x : base.word) suffix = next_suffix(suffix, x);
    std::vector<uint8_t> need(FULL + 1);
    Word missing;
    for (int x = 1; x <= FULL; ++x) if (!base.counts[x]) {
        missing.push_back(x);
        need[x] = 1;
    }
    const double low_weight = mode % 3 == 0 ? 1.0 : mode % 3 == 1 ? 1.6 : 2.4;
    auto weight = [&](Mask x) {
        int rank = rank_of(x);
        if (rank > 7) return 1.0;
        return low_weight + (rank <= 6 ? 0.15 * ((mode / 3) % 3) : 0.0);
    };
    std::vector<uint32_t> stamps(FULL + 1);
    uint32_t stamp = 0;
    Word candidates;
    int remaining = int(missing.size());
    auto append_letter = [&](Mask x, bool fallback) {
        require(x > 0 && x <= FULL, "empty repair letter");
        result.word.push_back(x);
        suffix = next_suffix(suffix, x);
        int gain = 0;
        for (Mask s : suffix) if (need[s]) {
            need[s] = 0;
            --remaining;
            ++gain;
        }
        require(gain > 0, "repair step covers no missing target");
        ++result.gains[gain];
        ++result.greedy_letters;
        result.fallback_letters += fallback;
    };
    while (remaining && Clock::now() < deadline) {
        ++stamp;
        candidates.clear();
        auto add = [&](Mask x) {
            if (x && stamps[x] != stamp) {
                stamps[x] = stamp;
                candidates.push_back(x);
            }
        };
        for (Mask target : missing) if (need[target]) {
            add(target);
            if (mode >= 3) for (Mask s : suffix) {
                if (!(s & ~target)) add(target & ~s);
            }
        }
        Mask best = 0;
        double best_score = -1;
        std::vector<std::pair<double, Mask>> beam;
        auto immediate = [&](const Word& context, Mask x) {
            double score = need[x] ? weight(x) : 0.0;
            Mask last = x;
            for (Mask s : context) {
                Mask u = s | x;
                if (u != last && need[u]) score += weight(u);
                last = u;
            }
            return score;
        };
        // A literal-only mode is the colored-union trail baseline. Residual
        // modes also admit helper letters completing any current suffix.
        for (Mask x : candidates) {
            double score = immediate(suffix, x);
            // Sparse residuals retain more possible interval starts for the
            // next step. Jitter explores tied trails, never overrides a hole.
            score += 0.001 * (K - rank_of(x)) + 0.0005 * std::generate_canonical<double, 20>(rng);
            if (score > best_score) {
                best_score = score;
                best = x;
            }
            if (mode >= 9) beam.emplace_back(score, x);
        }
        if (mode >= 9) {
            size_t width = std::min<size_t>(16, beam.size());
            std::partial_sort(beam.begin(), beam.begin() + width, beam.end(), std::greater<>());
            double best_two_step = -1;
            for (size_t i = 0; i < width; ++i) {
                if (Clock::now() >= deadline) break;
                auto [score, x] = beam[i];
                auto context = next_suffix(suffix, x);
                Word newly_covered;
                for (Mask s : context) if (need[s]) {
                    newly_covered.push_back(s);
                    need[s] = 0;
                }
                double next_gain = 0;
                int ties = 0;
                for (Mask target : missing) if (need[target]) {
                    Mask next = (x & ~target) ? target : target & ~x;
                    if (!next) continue;
                    double gain = immediate(context, next);
                    if (gain > next_gain + 1e-8) {
                        next_gain = gain;
                        ties = 1;
                    } else if (gain >= next_gain - 1e-8) ++ties;
                }
                for (Mask s : newly_covered) need[s] = 1;
                double two_step = score + 0.8 * next_gain + 0.00001 * std::min(ties, 100);
                if (two_step > best_two_step) {
                    best_two_step = two_step;
                    best = x;
                }
            }
        }
        require(best != 0, "repair candidate set empty");
        append_letter(best, false);
    }
    // A hard deadline cannot turn a partial construction into a claimed word.
    for (Mask x : missing) if (need[x]) append_letter(x, true);
    require(remaining == 0 && holes(suffix_counts(result.word, K)) == 0,
            "full literal repair audit failed");
    return result;
}

static int prune_repair(Word& word, int base_length, std::mt19937_64& rng,
                        Clock::time_point deadline) {
    State state(word, K);
    require(state.missing.empty(), "pruning nonuniversal input");
    int removed = 0;
    for (int pass = 0; pass < 3 && Clock::now() < deadline; ++pass) {
        std::vector<int> positions;
        for (int i = base_length; i < int(state.word.size()); ++i)
            if (state.word[i]) positions.push_back(i);
        std::shuffle(positions.begin(), positions.end(), rng);
        int before = removed;
        for (int p : positions) {
            if (Clock::now() >= deadline) break;
            if (!state.word[p]) continue;
            if (state.trial(p, p, {}) == 0) {
                state.commit(p, p, {});
                ++removed;
                continue;
            }
            int q = state.tree.next(p);
            if (q < 0) continue;
            Word merged{state.word[p] | state.word[q]};
            if (state.trial(p, q, merged) == 0) {
                state.commit(p, q, merged);
                ++removed;
            }
        }
        if (removed == before) break;
    }
    state.audit();
    word = state.compact();
    require(holes(suffix_counts(word, K)) == 0, "pruned output not universal");
    return removed;
}

static void save(const std::string& prefix, const Cycles& carrier, const Compiled& compiled,
                 const Opened& opened, const Repair& repaired, uint64_t seed,
                 int trial, int mode, double elapsed) {
    write_word(prefix + ".best.word", repaired.word);
    write_word(prefix + ".best.partial.word", opened.word);
    write_word(prefix + ".best.repair.word", Word(repaired.word.begin() + opened.word.size(), repaired.word.end()));
    Word missing;
    for (int x = 1; x <= FULL; ++x) if (!opened.counts[x]) missing.push_back(x);
    write_word(prefix + ".best.missing.txt", missing);
    std::ofstream state(prefix + ".best.state.tsv");
    state << "cycle\tposition\tT\tP\tC\tS\tassigned\n";
    for (size_t c = 0; c < carrier.size(); ++c)
        for (size_t i = 0; i < carrier[c].size(); ++i)
            state << c << '\t' << i << '\t' << carrier[c][i] << '\t' << compiled.p[c][i]
                  << '\t' << compiled.core[c][i] << '\t' << compiled.word[c][i]
                  << '\t' << compiled.assigned[c][i] << '\n';
    require(bool(state), "state write failed");
    std::ofstream out(prefix + ".best.json");
    out << "{\n\"schema\":\"k17-partial-compile-c83a1-v1\",\n\"seed\":" << seed
        << ",\n\"trial\":" << trial << ",\n\"repair_mode\":" << mode
        << ",\n\"elapsed_seconds\":" << elapsed
        << ",\n\"length\":" << repaired.word.size()
        << ",\n\"base_length\":" << opened.word.size()
        << ",\n\"repair_length\":" << repaired.word.size() - opened.word.size()
        << ",\n\"universal\":true,\n\"improves_25745\":" << (repaired.word.size() < 25745 ? "true" : "false")
        << ",\n\"matched\":" << compiled.matched << ",\n\"matching_cover_size\":" << compiled.cover_size
        << ",\n\"matching_demand\":21777,\n\"zero_degree\":" << compiled.zero_degree
        << ",\n\"unmatched_by_rank\":";
    json_array(out, compiled.unmatched);
    out << ",\n\"zero_degree_by_rank\":";
    json_array(out, compiled.zero_by_rank);
    out << ",\n\"base_missing_by_rank\":";
    json_array(out, missing_hist(opened.counts));
    out << ",\n\"cyclic_missing_by_rank\":";
    json_array(out, missing_hist(cyclic_counts(compiled.word)));
    out << ",\n\"final_missing_by_rank\":";
    json_array(out, missing_hist(suffix_counts(repaired.word, K)));
    out << ",\n\"cycle_lengths\":";
    std::vector<int> sizes;
    for (const auto& c : carrier) sizes.push_back(int(c.size()));
    json_array(out, sizes);
    out << ",\n\"cycle_order\":";
    json_array(out, opened.order);
    out << ",\n\"cuts\":";
    json_array(out, opened.cuts);
    out << ",\n\"reverse\":";
    json_array(out, opened.reverse);
    out << ",\n\"closure_per_cycle\":3,\n\"greedy_letters\":" << repaired.greedy_letters
        << ",\n\"pruned_letters\":" << repaired.pruned_letters
        << ",\n\"fallback_letters\":" << repaired.fallback_letters
        << ",\n\"repair_step_gain_histogram\":";
    json_array(out, repaired.gains);
    out << "\n}\n";
    require(bool(out), "report write failed");
}

static void partial_tests() {
    self_test();
    std::mt19937_64 rng(20260906);
    for (int n = 1; n <= 14; ++n) {
        int optimal = n;
        for (int bits = 0; bits < (1 << n); ++bits) {
            if (!(bits & 1) || !(bits & (1 << (n - 1)))) continue;
            bool valid = true;
            for (int i = 0; i + 1 < n; ++i) valid &= bool((bits >> i) & 3);
            if (valid) optimal = std::min(optimal, __builtin_popcount(unsigned(bits)));
        }
        for (int trial = 0; trial < 16; ++trial) {
            auto p = cover_pattern(n, rng, trial != 0);
            require(p.front() && p.back() && std::accumulate(p.begin(), p.end(), 0) == optimal,
                    "minimum path cover test");
            for (int i = 0; i + 1 < n; ++i) require(p[i] || p[i + 1], "path edge test");
        }
    }
    for (int sample = 0; sample < 250; ++sample) {
        int l = 1 + int(rng() % 7), r = 1 + int(rng() % 7);
        std::vector<std::vector<int>> adj(l);
        for (auto& row : adj) for (int v = 0; v < r; ++v) if (rng() & 1) row.push_back(v);
        std::set<int> possible{0};
        for (const auto& row : adj) {
            auto next = possible;
            for (int used : possible) for (int v : row)
                if (!(used & (1 << v))) next.insert(used | (1 << v));
            possible = std::move(next);
        }
        int exact = 0;
        for (int x : possible) exact = std::max(exact, __builtin_popcount(unsigned(x)));
        require(Matching(adj, r).cardinality == exact, "matching/brute test");
        Word word(3 + rng() % 20);
        for (auto& x : word) x = 1 + Mask(rng() % 31);
        auto core = make_core(word, rng, true);
        require(derivative(core) == derivative(word), "arbitrary cyclic core test");
        auto got = cyclic_counts({word});
        std::set<Mask> brute;
        for (size_t i = 0; i < word.size(); ++i) {
            Mask x = 0;
            for (size_t j = 0; j < word.size(); ++j) brute.insert(x |= word[(i + j) % word.size()]);
        }
        for (int x = 1; x <= FULL; ++x) require(bool(got[x]) == bool(brute.count(x)), "cyclic census test");
    }
    for (int mode = 0; mode < 18; ++mode) {
        Opened base;
        base.word = {1, 2, 4, 8, 16};
        base.counts.assign(FULL + 1, 1);
        auto small = suffix_counts(base.word, K);
        for (int x = 1; x < 32; ++x) base.counts[x] = small[x];
        // repair() performs a full-universe check, so give the other masks
        // literal witnesses in this synthetic, deliberately nonoptimal base.
        for (int x = 32; x <= FULL; ++x) base.word.push_back(x);
        base.counts = suffix_counts(base.word, K);
        auto fixed = repair(base, rng, mode, Clock::now() + std::chrono::seconds(1));
        require(holes(suffix_counts(fixed.word, K)) == 0, "repair self test");
    }
    Word long_gap{1};
    long_gap.insert(long_gap.end(), 300, 2);
    long_gap.push_back(4);
    require(suffix_counts(long_gap, K)[7] == 1, "unbounded witness-width regression");
    std::cout << "PARTIAL_SELF_TEST_PASS covers=224 matching=250 cyclic=250 repair=18 long_gap=302\n";
}

int main(int argc, char** argv) {
    try {
        std::cout << std::setprecision(9);
        if (argc == 2 && std::string(argv[1]) == "--self-test") {
            partial_tests();
            return 0;
        }
        require(argc == 6, "usage: partial FACTOR.txt OUTPUT_PREFIX SECONDS SEED MAX_TRIALS");
        char host[256]{};
        require(gethostname(host, sizeof(host) - 1) == 0, "hostname unavailable");
        std::string hostname(host);
        require(hostname == "arboghast" || hostname == "h100", "heavy runs require h100");
        double seconds = std::stod(argv[3]);
        uint64_t seed = std::stoull(argv[4]);
        int max_trials = std::stoi(argv[5]);
        require(seconds > 0 && seconds <= 330 && max_trials > 0, "invalid bounds");
        auto start = Clock::now();
        auto deadline = start + std::chrono::milliseconds(int(seconds * 1000));
        auto elapsed = [&] { return std::chrono::duration<double>(Clock::now() - start).count(); };
        auto carrier = read_factor(argv[1]);
        std::mt19937_64 rng(seed);
        int best_length = FULL, completed = 0;
        std::ofstream trials(std::string(argv[2]) + ".trials.jsonl");
        for (int trial = 0; trial < max_trials && Clock::now() < deadline; ++trial) {
            auto compiled = compile(carrier, rng, trial > 0 || seed % 4 != 0);
            auto opened = open_cycles(compiled.word, rng, 12);
            for (int variant = 0; variant < 3 && Clock::now() < deadline; ++variant) {
                int mode = (int(seed % 18) + trial * 3 + variant) % 18;
                auto repair_deadline = std::min(deadline, Clock::now() + std::chrono::seconds(mode >= 9 ? 20 : 8));
                auto repaired = repair(opened, rng, mode, repair_deadline);
                repaired.pruned_letters = prune_repair(repaired.word, int(opened.word.size()), rng,
                    std::min(deadline, Clock::now() + std::chrono::seconds(2)));
                ++completed;
                trials << "{\"trial\":" << trial << ",\"mode\":" << mode
                       << ",\"matched\":" << compiled.matched << ",\"zero_degree\":" << compiled.zero_degree
                       << ",\"base_holes\":" << holes(opened.counts)
                       << ",\"length\":" << repaired.word.size() << ",\"greedy_letters\":" << repaired.greedy_letters
                       << ",\"pruned\":" << repaired.pruned_letters << ",\"fallback\":" << repaired.fallback_letters
                       << ",\"seconds\":" << elapsed() << "}\n";
                trials.flush();
                if (int(repaired.word.size()) < best_length) {
                    best_length = int(repaired.word.size());
                    save(argv[2], carrier, compiled, opened, repaired, seed, trial, mode, elapsed());
                    std::cout << "RETAIN seed=" << seed << " trial=" << trial << " mode=" << mode
                              << " matched=" << compiled.matched << " base_holes=" << holes(opened.counts)
                              << " length=" << best_length << " missing=0 improved=" << (best_length < 25745)
                              << " seconds=" << elapsed() << std::endl;
                }
            }
        }
        std::cout << "FINAL seed=" << seed << " trials=" << completed << " length=" << best_length
                  << " seconds=" << elapsed() << std::endl;
        require(completed > 0, "deadline elapsed before a construction completed");
    } catch (const std::exception& error) {
        std::cerr << "ERROR " << error.what() << '\n';
        return 1;
    }
}
