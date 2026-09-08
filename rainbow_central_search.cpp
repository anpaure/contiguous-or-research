#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <atomic>
#include <bit>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <random>
#include <thread>
#include <vector>
using namespace std;

struct Eval {
    int deficit = 0;
    int covered = 0;
    int lower = 0;
    int upper = 0;
    int rank_below_possible = 0;
    int focus = 0;
    int potential = 0;
    vector<int> ranks;
};

struct Search {
    int k, rank, d, threads, full, minimum_colors;
    bool cyclic_required;
    string mode;
    double seconds;
    string output_path;
    vector<int> global_path;
    vector<uint8_t> focus_mask;
    Eval global_eval;
    atomic<long long> global_key{0};
    mutex global_mutex;
    chrono::steady_clock::time_point deadline;

    bool valid(const vector<int>& path) const {
        vector<uint8_t> color(1 << k);
        int distinct = 0;
        const int edge_count = cyclic_required ? path.size() : path.size() - 1;
        for (int i = 0; i < edge_count; ++i) {
            const int next = (i + 1) % path.size();
            if (popcount(static_cast<unsigned>(path[i] ^ path[next])) != 2)
                return false;
            const int intersection = path[i] & path[next];
            if (popcount(static_cast<unsigned>(intersection)) != rank - 1)
                return false;
            if (!color[intersection]) {
                color[intersection] = 1;
                ++distinct;
            }
        }
        return distinct >= minimum_colors;
    }

    Eval evaluate(const vector<int>& path) const {
        Eval result;
        result.ranks.assign(k + 1, 0);
        for (int bit = 0; bit < k; ++bit) {
            int i = 0;
            while (i < static_cast<int>(path.size())) {
                if (!(path[i] & (1 << bit))) { ++i; continue; }
                const int first = i;
                while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
                if (first && i < static_cast<int>(path.size()))
                    result.deficit += max(0, d + 1 - (i - first));
            }
        }
        vector<uint8_t> count(1 << k);
        auto record = [&] (int value, int wanted) {
            if (popcount(static_cast<unsigned>(value)) != wanted) return;
            if (!count[value]) {
                ++result.covered;
                ++result.ranks[wanted];
                if (wanted < rank) ++result.lower;
                if (wanted > rank) ++result.upper;
                if (wanted > rank && focus_mask[value]) ++result.focus;
            }
            if (count[value] != 255) ++count[value];
        };
        for (int value : path) record(value, rank);
        for (int length = 2; length <= d + 1; ++length)
            for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
                int value = full;
                for (int j = left; j < left + length; ++j) value &= path[j];
                record(value, rank - length + 1);
            }
        for (int length = 2; rank + length - 1 <= k; ++length)
            for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
                int value = 0;
                for (int j = left; j < left + length; ++j) value |= path[j];
                record(value, rank + length - 1);
            }
        for (int mask = 1; mask <= full; ++mask) {
            const int r = popcount(static_cast<unsigned>(mask));
            if (r < rank - d || !count[mask]) continue;
            int reward = 1024;
            for (int bonus = 256, occurrence = 1;
                 bonus && occurrence < count[mask]; bonus >>= 1, ++occurrence)
                reward += bonus;
            result.potential += reward;
        }
        for (int mask = 1; mask <= full; ++mask) {
            if (popcount(static_cast<unsigned>(mask)) != rank - 1) continue;
            if (count[mask] || !(mask & ~path.front()) || !(mask & ~path.back()))
                ++result.rank_below_possible;
        }
        return result;
    }

    bool better(const Eval& a, const Eval& b) const {
        if (a.deficit != b.deficit) return a.deficit < b.deficit;
        if (mode == "upper" && a.upper != b.upper) return a.upper > b.upper;
        if (mode == "edgeupper" && a.ranks[rank + 1] != b.ranks[rank + 1])
            return a.ranks[rank + 1] > b.ranks[rank + 1];
        if (mode == "edgeupper" && a.ranks[rank - 2] != b.ranks[rank - 2])
            return a.ranks[rank - 2] > b.ranks[rank - 2];
        if (mode == "edgeupper" && a.ranks[rank + 2] != b.ranks[rank + 2])
            return a.ranks[rank + 2] > b.ranks[rank + 2];
        if (mode == "pinnableupper" && a.ranks[rank - 2] != b.ranks[rank - 2])
            return a.ranks[rank - 2] > b.ranks[rank - 2];
        if (mode == "pinnableupper" && a.ranks[rank + 1] != b.ranks[rank + 1])
            return a.ranks[rank + 1] > b.ranks[rank + 1];
        if (mode == "pinnableupper" && a.ranks[rank + 2] != b.ranks[rank + 2])
            return a.ranks[rank + 2] > b.ranks[rank + 2];
        if (mode == "lower" && a.lower != b.lower) return a.lower > b.lower;
        if (mode == "label" && a.rank_below_possible != b.rank_below_possible)
            return a.rank_below_possible > b.rank_below_possible;
        if (mode == "label" && a.lower != b.lower) return a.lower > b.lower;
        if (mode == "bridge" && a.rank_below_possible != b.rank_below_possible)
            return a.rank_below_possible > b.rank_below_possible;
        if (mode == "bridge" && a.upper != b.upper) return a.upper > b.upper;
        if (mode == "bridge" && a.lower != b.lower) return a.lower > b.lower;
        if (mode == "complete" && a.lower != b.lower) return a.lower > b.lower;
        if (mode == "complete" &&
            a.rank_below_possible != b.rank_below_possible)
            return a.rank_below_possible > b.rank_below_possible;
        if (mode == "complete" && a.upper != b.upper) return a.upper > b.upper;
        if (mode == "complete" && a.focus != b.focus) return a.focus > b.focus;
        if (a.covered != b.covered) return a.covered > b.covered;
        return a.potential > b.potential;
    }

    long long key(const Eval& e) const {
        if (mode == "edgeupper") {
            // k=14 targeted hierarchy: factorability, complete rank-8 edge
            // unions, complete rank-5 triple intersections, then rank-9
            // triple unions.  The seed deficit is below 902, so these scales
            // stay inside signed 64-bit arithmetic while remaining strictly
            // lexicographic over every lower-priority field.
            return -static_cast<long long>(e.deficit) * 10000000000000000LL
                 + static_cast<long long>(e.ranks[rank + 1]) * 1000000000000LL
                 + static_cast<long long>(e.ranks[rank - 2]) * 100000000LL
                 + static_cast<long long>(e.ranks[rank + 2]) * 10000LL
                 + e.potential;
        }
        if (mode == "pinnableupper") {
            // Preserve the complete rank-(r-2) triple-intersection layer that
            // supplies the Hall-perfect lower labeling, then optimize the two
            // most constrained upper rows.  Hot annealing may cross a path
            // missing one lower shadow, but the global incumbent is strictly
            // lexicographic and therefore never saves such a regression.
            return -static_cast<long long>(e.deficit) * 10000000000000000LL
                 + static_cast<long long>(e.ranks[rank - 2]) * 1000000000000LL
                 + static_cast<long long>(e.ranks[rank + 1]) * 100000000LL
                 + static_cast<long long>(e.ranks[rank + 2]) * 10000LL
                 + e.potential;
        }
        if (mode == "complete") {
            // The global comparison is strictly lexicographic (see better),
            // but these smaller scales deliberately let annealing traverse a
            // state missing one lower shadow at the hot part of each epoch.
            // That is essential for escaping neutral lower=956 components.
            return -static_cast<long long>(e.deficit) * 1000000000000000LL
                 + static_cast<long long>(e.lower) * 1000000000000LL
                 + static_cast<long long>(e.rank_below_possible) * 1000000000LL
                 + static_cast<long long>(e.upper) * 1000000LL
                 + static_cast<long long>(e.focus) * 1000LL
                 + e.potential;
        }
        if (mode == "bridge") {
            // Lexicographic order: first preserve endpoint labelability of
            // every (rank-1)-set, then complete the upper union shadows, then
            // improve the internal lower intersection shadows.  The scales
            // dominate all following fields for k<20 without overflowing.
            return -static_cast<long long>(e.deficit) * 100000000000000000LL
                 + static_cast<long long>(e.rank_below_possible) * 100000000000000LL
                 + static_cast<long long>(e.upper) * 100000000000LL
                 + static_cast<long long>(e.lower) * 100000000LL
                 + static_cast<long long>(e.covered) * 10000LL
                 + e.potential;
        }
        const int priority = mode == "upper" ? e.upper
            : (mode == "lower" ? e.lower
               : (mode == "label" ? e.rank_below_possible * 2048 + e.lower
                                  : e.covered));
        return -static_cast<long long>(e.deficit) * 1000000000000000LL
             + static_cast<long long>(priority) * 1000000000000LL
             + static_cast<long long>(e.covered) * 100000000LL + e.potential;
    }

    long long anneal_key(const Eval& e) const {
        if (mode == "runbreak") {
            // Permit temporary one- or two-unit run-deficit increases at the
            // hot end of an epoch.  The global incumbent still uses key() and
            // better(), so only lexicographically certified improvements are
            // ever written as the best path.
            return -static_cast<long long>(e.deficit) * 10000000000LL
                 + static_cast<long long>(e.ranks[rank - 2]) * 1000000LL
                 + static_cast<long long>(e.ranks[rank + 1]) * 1000LL
                 + e.potential;
        }
        return key(e);
    }

    void save() {
        ofstream output(output_path);
        for (int value : global_path) output << value << ' ';
        output << '\n';
    }

    void report(const Eval& e) {
        cerr << "best deficit=" << e.deficit << " covered=" << e.covered
             << " lower=" << e.lower << " upper=" << e.upper
             << " possible5=" << e.rank_below_possible
             << " focus=" << e.focus
             << " potential=" << e.potential << " ranks";
        for (int r = 0; r <= k; ++r) if (e.ranks[r])
            cerr << ' ' << r << ':' << e.ranks[r];
        cerr << '\n';
    }

    bool reverse_move(vector<int>& path, mt19937_64& random) const {
        const int n = path.size();
        for (int attempt = 0; attempt < 300; ++attempt) {
            int left = random() % n, right = random() % n;
            if (left > right) swap(left, right);
            if (right - left < 2) continue;
            if (left && popcount(static_cast<unsigned>(path[left - 1] ^ path[right])) != 2)
                continue;
            if (right + 1 < n &&
                popcount(static_cast<unsigned>(path[left] ^ path[right + 1])) != 2)
                continue;
            reverse(path.begin() + left, path.begin() + right + 1);
            if (valid(path)) return true;
            reverse(path.begin() + left, path.begin() + right + 1);
        }
        return false;
    }

    bool relocate_move(vector<int>& path, mt19937_64& random) const {
        const int n = path.size();
        for (int attempt = 0; attempt < 200; ++attempt) {
            const int length = 1 + random() % 8;
            const int left = random() % (n - length + 1), right = left + length;
            vector<int> block(path.begin() + left, path.begin() + right);
            vector<int> reduced;
            reduced.insert(reduced.end(), path.begin(), path.begin() + left);
            reduced.insert(reduced.end(), path.begin() + right, path.end());
            if (random() & 1) reverse(block.begin(), block.end());
            for (int gap_try = 0; gap_try < 100; ++gap_try) {
                const int gap = random() % (reduced.size() + 1);
                if (gap == left) continue;
                vector<int> candidate = reduced;
                candidate.insert(candidate.begin() + gap, block.begin(), block.end());
                if (!valid(candidate)) continue;
                path.swap(candidate);
                return true;
            }
        }
        return false;
    }

    void worker(int id) {
        mt19937_64 random(0x9e3779b97f4a7c15ULL * (id + 1) ^
            chrono::high_resolution_clock::now().time_since_epoch().count());
        uniform_real_distribution<double> uniform(0.0, 1.0);
        while (chrono::steady_clock::now() < deadline) {
            vector<int> path;
            {
                lock_guard<mutex> lock(global_mutex);
                path = global_path;
            }
            Eval current = evaluate(path);
            long long current_score = anneal_key(current);
            for (int iteration = 0;
                 iteration < 200000 && chrono::steady_clock::now() < deadline;
                 ++iteration) {
                vector<int> candidate = path;
                const int choice = random() % 100;
                const int move_count = choice < 70 ? 1 : (choice < 90 ? 2 : 3 + random() % 2);
                bool moved = false;
                for (int move = 0; move < move_count; ++move) {
                    const int type = random() % 100;
                    if (type < 10) {
                        vector<int> before = candidate;
                        const int shift = 1 + random() % (candidate.size() - 1);
                        rotate(candidate.begin(), candidate.begin() + shift, candidate.end());
                        if (valid(candidate)) moved = true;
                        else candidate.swap(before);
                    } else {
                        moved |= type < 80
                            ? reverse_move(candidate, random)
                            : relocate_move(candidate, random);
                    }
                }
                if (!moved) continue;
                Eval next = evaluate(candidate);
                const long long next_score = anneal_key(next);
                const double phase = (iteration % 5000) / 5000.0;
                const double temperature = (mode == "runbreak" ? 2e10 : 2e11) *
                    pow(1e-6, phase) + 1.0;
                if (next_score >= current_score ||
                    uniform(random) < exp((next_score - current_score) / temperature)) {
                    path.swap(candidate);
                    current = move(next);
                    current_score = next_score;
                }
                long long old = global_key.load(memory_order_relaxed);
                const long long candidate_key = key(current);
                if (candidate_key > old && global_key.compare_exchange_strong(old, candidate_key)) {
                    lock_guard<mutex> lock(global_mutex);
                    if (better(current, global_eval)) {
                        global_eval = current;
                        global_path = path;
                        report(global_eval);
                        save();
                    }
                }
            }
        }
    }

    Search(int bits, int central_rank, int slack, int thread_count,
           double duration, string output, vector<int> seed, bool require_cycle,
           int required_colors, string search_mode)
        : k(bits), rank(central_rank), d(slack), threads(thread_count),
          full((1 << bits) - 1), minimum_colors(required_colors),
          cyclic_required(require_cycle), mode(move(search_mode)),
          seconds(duration), output_path(move(output)),
          global_path(move(seed)) {
        if (!valid(global_path)) throw runtime_error("seed is not a rainbow Johnson path");
        focus_mask.assign(1 << k, 0);
        for (int mask = 1; mask <= full; ++mask)
            if (popcount(static_cast<unsigned>(mask)) > rank) focus_mask[mask] = 1;
        for (int length = 2; rank + length - 1 <= k; ++length)
            for (int left = 0; left + length <= static_cast<int>(global_path.size()); ++left) {
                int value = 0;
                for (int j = left; j < left + length; ++j) value |= global_path[j];
                if (popcount(static_cast<unsigned>(value)) == rank + length - 1)
                    focus_mask[value] = 0;
            }
        global_eval = evaluate(global_path);
        global_key.store(key(global_eval));
    }

    void run() {
        report(global_eval);
        deadline = chrono::steady_clock::now() +
            chrono::milliseconds(static_cast<long long>(seconds * 1000));
        vector<thread> pool;
        for (int id = 0; id < threads; ++id) pool.emplace_back(&Search::worker, this, id);
        for (thread& value : pool) value.join();
        save();
    }
};

int main(int argc, char** argv) {
    if (argc < 7) return 2;
    const int k = stoi(argv[1]), rank = stoi(argv[2]), d = stoi(argv[3]);
    const int threads = stoi(argv[4]);
    const double seconds = stod(argv[5]);
    vector<int> seed;
    for (int value; cin >> value;) seed.push_back(value);
    const int required_colors = argc > 7 ? stoi(argv[7]) : seed.size() - 1;
    const string mode = argc > 8 ? argv[8] : "normal";
    const bool require_cycle = argc > 9 && string(argv[9]) == "cycle";
    Search search(k, rank, d, threads, seconds, argv[6], move(seed),
                  require_cycle, required_colors, mode);
    search.run();
}
