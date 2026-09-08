#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

// Research prototype: one integral cyclic set-word, scored at every rank.
// No independent-rank selection, truncated interval inventory, or matching oracle.
using Mask = uint32_t;
using Word = std::vector<Mask>;
using Profile = std::vector<Mask>;

static void require(bool ok, const char* message) {
    if (!ok) throw std::runtime_error(message);
}

static uint64_t binomial(int n, int r) {
    uint64_t value = 1;
    for (int i = 1; i <= r; ++i) value = value * (n - r + i) / i;
    return value;
}

struct OrbitTable {
    int k;
    Mask full;
    std::vector<Mask> canonical, representatives;
    std::vector<int> sizes;

    explicit OrbitTable(int bits)
        : k(bits), full(bits >= 2 && bits <= 24 ? (Mask(1) << bits) - 1 : 0),
          canonical(full + 1), sizes(full + 1) {
        require(k >= 2 && k <= 24, "supported dimensions are 2 through 24");
        for (Mask x = 1; x <= full; ++x) {
            if (canonical[x]) continue;
            representatives.push_back(x);
            Mask y = x;
            int size = 0;
            do {
                canonical[y] = x;
                y = rotate(y, 1);
                ++size;
            } while (y != x);
            sizes[x] = size;
        }
    }

    Mask rotate(Mask x, int amount) const {
        amount %= k;
        if (amount < 0) amount += k;
        return amount ? ((x << amount) & full) | (x >> (k - amount)) : x;
    }
};

static Profile next_profile(const Profile& before, Mask letter) {
    Profile after;
    after.reserve(before.size() + 1);
    after.push_back(letter);
    for (Mask x : before) {
        x |= letter;
        if (x != after.back()) after.push_back(x);
    }
    return after;
}

struct CyclicState {
    const OrbitTable& table;
    Word seed;
    std::vector<Profile> profiles;
    std::vector<int> counts, delta, index_stamp, target_stamp;
    std::vector<int> changed_indices;
    std::vector<Profile> old_profiles;
    std::vector<Mask> touched;
    int stamp = 0, ignored_pairs;
    uint64_t holes = 0, controlled_holes = 0;
    int64_t hole_delta = 0, controlled_delta = 0;
    double cost = 0, cost_delta = 0;

    CyclicState(const OrbitTable& orbits, Word word, int ignored = 0)
        : table(orbits), seed(std::move(word)), profiles(seed.size()),
          counts(table.full + 1), delta(table.full + 1), index_stamp(seed.size()),
          target_stamp(table.full + 1), ignored_pairs(ignored) {
        require(!seed.empty(), "empty seed");
        for (Mask x : seed) require(x && !(x & ~table.full), "invalid letter");
        rebuild();
    }

    Word developed() const {
        Word word;
        word.reserve(table.k * seed.size());
        for (int shift = 0; shift < table.k; ++shift)
            for (Mask x : seed) word.push_back(table.rotate(x, shift));
        return word;
    }

    bool controlled(Mask x) const {
        int rank = __builtin_popcount(x);
        return rank < table.k / 2 - ignored_pairs + 1 ||
               rank > table.k / 2 + ignored_pairs;
    }

    void rebuild() {
        std::fill(counts.begin(), counts.end(), 0);
        Profile current;
        // A complete developed period supplies all possible cyclic suffix unions.
        for (int round = 0; round <= table.k; ++round) {
            if (round) for (Mask& x : current) x = table.rotate(x, -1);
            for (size_t i = 0; i < seed.size(); ++i) {
                current = next_profile(current, seed[i]);
                if (round == table.k) profiles[i] = current;
            }
        }
        for (const auto& profile : profiles)
            for (Mask x : profile) ++counts[table.canonical[x]];
        holes = controlled_holes = 0;
        cost = 0;
        for (Mask x : table.representatives) {
            if (!counts[x]) holes += table.sizes[x];
            if (controlled(x)) {
                if (!counts[x]) controlled_holes += table.sizes[x];
                cost += double(table.sizes[x]) / table.k * penalty(counts[x]);
            }
        }
    }

    static double penalty(int count) {
        return count ? 0.06 / count : 1.0;
    }

    void add(Mask x, int amount) {
        x = table.canonical[x];
        if (target_stamp[x] != stamp) {
            target_stamp[x] = stamp;
            delta[x] = 0;
            touched.push_back(x);
        }
        delta[x] += amount;
    }

    // The changed letters must have distinct seed indices. Their copies are
    // changed simultaneously in all coordinate-rotated blocks.
    void trial(const std::vector<std::pair<int, Mask>>& changes) {
        require(!changes.empty(), "empty mutation");
        ++stamp;
        touched.clear();
        changed_indices.clear();
        old_profiles.clear();
        int first = int(seed.size()), last = -1;
        for (auto [i, x] : changes) {
            require(i >= 0 && i < int(seed.size()) && x && !(x & ~table.full),
                    "invalid mutation");
            seed[i] = x;
            first = std::min(first, i);
            last = std::max(last, i);
        }
        Profile current = profiles[(first + seed.size() - 1) % seed.size()];
        if (!first) for (Mask& x : current) x = table.rotate(x, -1);
        const int limit = int((table.k + 2) * seed.size());
        int i = first;
        bool past_last = false, settled = false;
        for (int step = 0; step < limit; ++step) {
            current = next_profile(current, seed[i]);
            if (i == last) past_last = true;
            if (current == profiles[i] && past_last) {
                settled = true;
                break;
            }
            if (current != profiles[i]) {
                if (index_stamp[i] != stamp) {
                    index_stamp[i] = stamp;
                    changed_indices.push_back(i);
                    old_profiles.push_back(profiles[i]);
                }
                for (Mask x : profiles[i]) add(x, -1);
                for (Mask x : current) add(x, 1);
                profiles[i] = current;
            }
            if (++i == int(seed.size())) {
                i = 0;
                for (Mask& x : current) x = table.rotate(x, -1);
            }
        }
        require(settled, "profile propagation failed to settle");
        hole_delta = controlled_delta = 0;
        cost_delta = 0;
        for (Mask x : touched) {
            int after = counts[x] + delta[x];
            require(after >= 0, "negative endpoint count");
            hole_delta += int64_t(table.sizes[x]) * ((after == 0) - (counts[x] == 0));
            if (controlled(x)) {
                controlled_delta += int64_t(table.sizes[x]) * ((after == 0) - (counts[x] == 0));
                cost_delta += double(table.sizes[x]) / table.k *
                              (penalty(after) - penalty(counts[x]));
            }
        }
    }

    void accept() {
        for (Mask x : touched) counts[x] += delta[x];
        holes = uint64_t(int64_t(holes) + hole_delta);
        controlled_holes = uint64_t(int64_t(controlled_holes) + controlled_delta);
        cost += cost_delta;
    }

    void reject(const std::vector<std::pair<int, Mask>>& old_letters) {
        for (auto [i, x] : old_letters) seed[i] = x;
        for (size_t j = 0; j < changed_indices.size(); ++j)
            profiles[changed_indices[j]] = std::move(old_profiles[j]);
    }

    void audit(bool brute = false) const {
        CyclicState other(table, seed, ignored_pairs);
        require(other.profiles == profiles, "incremental profile mismatch");
        require(other.counts == counts && other.holes == holes &&
                other.controlled_holes == controlled_holes, "incremental count mismatch");
        if (!brute) return;
        Word word = developed();
        std::vector<bool> seen(table.full + 1);
        for (size_t i = 0; i < word.size(); ++i) {
            Mask x = 0;
            for (size_t j = 0; j < word.size(); ++j) {
                x |= word[(i + j) % word.size()];
                seen[x] = true;
            }
        }
        for (Mask x = 1; x <= table.full; ++x)
            require(seen[x] == bool(counts[table.canonical[x]]), "literal cyclic inventory mismatch");
    }

    void report(const char* label, uint64_t step, bool emit) const {
        std::vector<uint64_t> by_rank(table.k + 1);
        for (Mask x : table.representatives)
            if (!counts[x]) by_rank[__builtin_popcount(x)] += table.sizes[x];
        std::cout << label << " k=" << table.k << " seed_length=" << seed.size()
                  << " period=" << table.k * seed.size()
                  << " width=" << binomial(table.k, table.k / 2)
                  << " holes=" << holes << " density=" << std::setprecision(12)
                  << double(holes) / (uint64_t(1) << table.k)
                  << " ignored_pairs=" << ignored_pairs << " controlled_holes=" << controlled_holes
                  << " step=" << step << " ranks=";
        for (int r = 1; r <= table.k; ++r) std::cout << (r > 1 ? "," : "") << by_rank[r];
        std::cout << '\n';
        if (emit) {
            std::cout << "SEED";
            for (Mask x : seed) std::cout << ' ' << x;
            std::cout << '\n';
        }
        std::cout.flush();
    }
};

static Word known_seed(int k) {
    if (k == 7) return {3, 5, 64, 20, 36};
    if (k == 9) return {1, 130, 136, 12, 36, 48, 80, 272, 18, 17, 9, 65, 96, 68};
    return {};
}

static void self_test() {
    uint64_t cases = 0, trials = 0;
    std::mt19937_64 rng(9064471);
    for (int k = 2; k <= 4; ++k) {
        OrbitTable table(k);
        for (int length = 1; length <= 4; ++length) {
            uint64_t total = 1;
            for (int i = 0; i < length; ++i) total *= table.full;
            if (k == 4) total = std::min<uint64_t>(total, 200);
            for (uint64_t code = 0; code < total; ++code) {
                Word seed(length);
                uint64_t number = code;
                for (Mask& x : seed) {
                    x = k == 4 ? 1 + rng() % table.full : 1 + number % table.full;
                    number /= table.full;
                }
                CyclicState state(table, seed, int(code % (k / 2)));
                state.audit(true);
                ++cases;
                for (int repeat = 0; repeat < 8; ++repeat) {
                    int a = rng() % length, b = rng() % length;
                    std::vector<std::pair<int, Mask>> old{{a, state.seed[a]}};
                    std::vector<std::pair<int, Mask>> next{{a, Mask(1 + rng() % table.full)}};
                    if (a != b) {
                        old.push_back({b, state.seed[b]});
                        next.push_back({b, Mask(1 + rng() % table.full)});
                    }
                    if (repeat >= 4) {
                        old.clear();
                        next.clear();
                        for (int j = 0; j < length; ++j) {
                            old.push_back({j, state.seed[j]});
                            next.push_back({j, Mask(1 + rng() % table.full)});
                        }
                    }
                    uint64_t before = state.holes;
                    uint64_t controlled_before = state.controlled_holes;
                    state.trial(next);
                    CyclicState rebuilt(table, state.seed, state.ignored_pairs);
                    require(int64_t(before) + state.hole_delta == int64_t(rebuilt.holes),
                            "trial hole delta mismatch");
                    require(int64_t(controlled_before) + state.controlled_delta ==
                            int64_t(rebuilt.controlled_holes), "trial controlled delta mismatch");
                    if (repeat & 1) state.accept();
                    else state.reject(old);
                    state.audit(true);
                    ++trials;
                }
            }
        }
    }
    for (int k : {7, 9}) {
        OrbitTable table(k);
        CyclicState state(table, known_seed(k));
        state.audit(true);
        require(state.holes == uint64_t(k == 7 ? 0 : 12), "known seed mismatch");
    }
    std::cout << "SELF_TEST_PASS cases=" << cases << " mutations=" << trials << '\n';
}

int main(int argc, char** argv) {
    try {
        int k = 9, rounds = 12, ignored_pairs = 0;
        uint64_t steps = 300000, random_seed = 9064471;
        double hot = 0.35;
        bool emit = false, random_start = false;
        for (int a = 1; a < argc; ++a) {
            std::string option = argv[a];
            if (option == "--test") { self_test(); return 0; }
            if (option == "--emit") { emit = true; continue; }
            if (option == "--random-start") { random_start = true; continue; }
            require(a + 1 < argc, "missing option value");
            std::string value = argv[++a];
            if (option == "--k") k = std::stoi(value);
            else if (option == "--rounds") rounds = std::stoi(value);
            else if (option == "--ignore-middle-pairs") ignored_pairs = std::stoi(value);
            else if (option == "--steps") steps = std::stoull(value);
            else if (option == "--seed") random_seed = std::stoull(value);
            else if (option == "--hot") hot = std::stod(value);
            else throw std::runtime_error("unknown option: " + option);
        }
        OrbitTable table(k);
        require(k % 2 == 1, "width-length developed search uses odd k");
        require(rounds > 0 && steps > 0 && hot > 0, "invalid search parameters");
        require(ignored_pairs >= 0 && ignored_pairs < k / 2, "invalid ignored rank range");
        std::mt19937_64 rng(random_seed);
        auto uniform = [&]() { return double(rng() >> 11) * 0x1.0p-53; };
        Word initial = random_start ? Word{} : known_seed(k);
        if (initial.empty()) {
            const int length = int(binomial(k, k / 2) / k);
            std::vector<int> recent;
            const int gap = std::min(k - 2, k / 2 + 1);
            for (int i = 0; i < length; ++i) {
                int x;
                do { x = rng() % k; }
                while (std::find(recent.begin(), recent.end(), x) != recent.end());
                initial.push_back(Mask(1) << x);
                recent.push_back(x);
                if (int(recent.size()) > gap) recent.erase(recent.begin());
            }
        }
        CyclicState state(table, initial, ignored_pairs);
        state.report("INITIAL", 0, false);
        uint64_t best_holes = state.holes, completed = 0;
        uint64_t best_controlled = state.controlled_holes;
        double best_cost = state.cost;
        Word best = state.seed;
        const int length = int(state.seed.size());
        for (int round = 0; round < rounds && best_controlled; ++round) {
            state.seed = best;
            state.rebuild();
            for (uint64_t step = 0; step < steps && best_controlled; ++step) {
                int i = rng() % length;
                Mask x = state.seed[i];
                std::vector<std::pair<int, Mask>> next;
                int kind = rng() % 14;
                if (kind < 4) {
                    x ^= Mask(1) << (rng() % k);
                    next.push_back({i, x});
                } else if (kind < 6) {
                    int a = rng() % k, b = rng() % k;
                    Mask aa = Mask(1) << a, bb = Mask(1) << b;
                    if (bool(x & aa) != bool(x & bb)) x ^= aa | bb;
                    next.push_back({i, x});
                } else if (kind < 8 && length > 1) {
                    int j = (i + 1 + rng() % std::min(k, length - 1)) % length;
                    next.push_back({i, state.seed[j]});
                    next.push_back({j, x});
                } else if (kind == 8 && length > 1) {
                    int j = (i + 1) % length;
                    Mask bit = Mask(1) << (rng() % k);
                    Mask y = state.seed[j];
                    if (bool(x & bit) != bool(y & bit)) { x ^= bit; y ^= bit; }
                    else if (x & bit) { if (rng() & 1) x ^= bit; else y ^= bit; }
                    else { if (rng() & 1) x |= bit; else y |= bit; }
                    next.push_back({i, x});
                    next.push_back({j, y});
                } else if (kind == 9) {
                    Mask target = table.representatives[rng() % table.representatives.size()];
                    if (state.counts[target] || !state.controlled(target)) continue;
                    target = table.rotate(target, rng() % k);
                    Mask outside = 0;
                    const auto& before = state.profiles[(i + length - 1) % length];
                    for (Mask y : before) {
                        if (!i) y = table.rotate(y, -1);
                        if (y & ~target) break;
                        outside = y;
                    }
                    for (int j = i + 1; j < i + std::min(k, length); ++j) {
                        Mask y = table.rotate(state.seed[j % length], j / length);
                        if (y & ~target) break;
                        outside |= y;
                    }
                    x = (x & target) | (target & ~outside);
                    next.push_back({i, x});
                } else {
                    const auto& profile = state.profiles[i];
                    Mask before = profile[rng() % profile.size()];
                    Mask target = before;
                    bool found = false;
                    for (int attempt = 0; attempt < 8; ++attempt) {
                        target = before;
                        target ^= Mask(1) << (rng() % k);
                        if (rng() & 1) target ^= Mask(1) << (rng() % k);
                        if (target && state.controlled(target) &&
                            !state.counts[table.canonical[target]]) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) continue;
                    Mask united = 0;
                    int width = 0;
                    while (width < std::min(k, length) && united != before) {
                        int position = i - width;
                        int index = (position + length) % length;
                        united |= table.rotate(state.seed[index], position < 0 ? -1 : 0);
                        ++width;
                    }
                    if (united != before) continue;
                    // Cap a whole literal witness and put back exactly the
                    // missing positive bits. This forces the chosen hole.
                    Mask needed = target & ~before;
                    int owner = rng() % width;
                    Mask fallback = needed ? needed : target & -target;
                    for (int a = 0; a < width; ++a) {
                        int position = i - a;
                        int index = (position + length) % length;
                        int shift = position < 0 ? -1 : 0;
                        Mask value = table.rotate(state.seed[index], shift) & target;
                        if (a == owner) value |= needed;
                        if (!value) value = fallback;
                        next.push_back({index, table.rotate(value, -shift)});
                    }
                }
                bool valid = true, changed = false;
                std::vector<std::pair<int, Mask>> old;
                for (auto [j, y] : next) {
                    valid = valid && y;
                    changed = changed || y != state.seed[j];
                    old.push_back({j, state.seed[j]});
                }
                if (!valid || !changed) continue;
                state.trial(next);
                double temperature = hot * std::pow(0.002 / hot, double(step) / steps);
                if (state.cost_delta <= 0 || uniform() < std::exp(-state.cost_delta / temperature)) {
                    state.accept();
                    if (state.controlled_holes < best_controlled ||
                        (state.controlled_holes == best_controlled &&
                         (state.holes < best_holes ||
                          (state.holes == best_holes && state.cost < best_cost - 1e-9)))) {
                        best_controlled = state.controlled_holes;
                        best_holes = state.holes;
                        best_cost = state.cost;
                        best = state.seed;
                    }
                } else state.reject(old);
                if (step % 50000 == 0) state.audit();
            }
            completed += steps;
            state.seed = best;
            state.rebuild();
            state.audit();
            state.report("ROUND", completed, false);
        }
        state.seed = best;
        state.rebuild();
        state.audit(k <= 13);
        state.report("FINAL", completed, emit || length <= 150);
    } catch (const std::exception& e) {
        std::cerr << "ERROR: " << e.what() << '\n';
        return 1;
    }
}
