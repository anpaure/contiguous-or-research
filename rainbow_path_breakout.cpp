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

// Breakout local search for a rainbow Johnson path.  The hard constraints are
// the complete lower intersection shadow, endpoint feasibility of the omitted
// rank-(r-1) colour, the factorization run condition, and distinct adjacent
// intersections.  Missing upper masks receive increasing Lagrange weights at
// the end of every epoch.  This prevents the search from repeatedly repairing
// the same easy masks while merely exchanging one difficult hole for another.

struct Eval {
    int deficit = 0;
    int lower = 0;
    int possible = 0;
    int upper = 0;
    int weighted = 0;
    int redundancy = 0;
    vector<uint8_t> covered;
};

struct Search {
    int k, rank, d, threads, full, required_lower, required_possible;
    double seconds, epoch_seconds;
    string output_path;
    vector<int> weights;
    vector<int> incumbent;
    Eval incumbent_eval;
    vector<int> raw_best;
    Eval raw_best_eval;
    atomic<int> raw_upper{0};
    mutex lock;
    chrono::steady_clock::time_point final_deadline;

    bool adjacent(int a, int b) const {
        return popcount(static_cast<unsigned>(a ^ b)) == 2;
    }

    bool rainbow(const vector<int>& path) const {
        vector<uint8_t> seen(1 << k);
        for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
            if (!adjacent(path[i], path[i + 1])) return false;
            const int colour = path[i] & path[i + 1];
            if (seen[colour]) return false;
            seen[colour] = 1;
        }
        return true;
    }

    Eval evaluate(const vector<int>& path) const {
        Eval result;
        result.covered.assign(1 << k, 0);
        for (int bit = 0; bit < k; ++bit) {
            int i = 0;
            while (i < static_cast<int>(path.size())) {
                if (!(path[i] & (1 << bit))) {
                    ++i;
                    continue;
                }
                const int first = i;
                while (i < static_cast<int>(path.size()) &&
                       (path[i] & (1 << bit))) ++i;
                if (first && i < static_cast<int>(path.size()))
                    result.deficit += max(0, d + 1 - (i - first));
            }
        }
        vector<uint8_t> count(1 << k);
        auto record = [&](int value, int wanted) {
            if (popcount(static_cast<unsigned>(value)) != wanted) return;
            if (!count[value]) result.covered[value] = 1;
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
            if (!count[mask]) continue;
            if (r < rank) ++result.lower;
            if (r > rank) {
                ++result.upper;
                result.weighted += weights[mask];
                // Reward spare witnesses, but cap the reward so the search
                // cannot prefer redundancy to a genuinely uncovered target.
                result.redundancy += min<int>(count[mask] - 1, 3);
            }
        }
        for (int mask = 1; mask <= full; ++mask) {
            if (popcount(static_cast<unsigned>(mask)) != rank - 1) continue;
            if (result.covered[mask] || !(mask & ~path.front()) ||
                !(mask & ~path.back())) ++result.possible;
        }
        return result;
    }

    bool admissible(const Eval& value) const {
        return value.deficit == 0 && value.lower >= required_lower &&
               value.possible >= required_possible;
    }

    long long score(const Eval& value) const {
        return static_cast<long long>(value.weighted) * 1000000LL +
               static_cast<long long>(value.upper) * 10000LL +
               value.redundancy;
    }

    static bool raw_better(const Eval& a, const Eval& b) {
        if (a.upper != b.upper) return a.upper > b.upper;
        return a.redundancy > b.redundancy;
    }

    void save(const vector<int>& path) const {
        ofstream output(output_path);
        for (int value : path) output << value << ' ';
        output << '\n';
    }

    void report(const char* tag, const Eval& value, int epoch) const {
        vector<int> missing_by_rank(k + 1);
        for (int mask = 1; mask <= full; ++mask)
            if (popcount(static_cast<unsigned>(mask)) > rank &&
                !value.covered[mask])
                ++missing_by_rank[popcount(static_cast<unsigned>(mask))];
        cerr << tag << " epoch=" << epoch << " upper=" << value.upper
             << " weighted=" << value.weighted
             << " lower=" << value.lower << " possible=" << value.possible
             << " redundancy=" << value.redundancy << " missing";
        for (int r = rank + 1; r <= k; ++r)
            if (missing_by_rank[r]) cerr << ' ' << r << ':' << missing_by_rank[r];
        cerr << '\n';
    }

    bool reverse_random(vector<int>& path, mt19937_64& random) const {
        const int n = path.size();
        for (int attempt = 0; attempt < 160; ++attempt) {
            int left = random() % n, right = random() % n;
            if (left > right) swap(left, right);
            if (right - left < 2) continue;
            if (left && !adjacent(path[left - 1], path[right])) continue;
            if (right + 1 < n && !adjacent(path[left], path[right + 1])) continue;
            reverse(path.begin() + left, path.begin() + right + 1);
            if (rainbow(path)) return true;
            reverse(path.begin() + left, path.begin() + right + 1);
        }
        return false;
    }

    bool reverse_target(vector<int>& path, const Eval& value,
                        mt19937_64& random) const {
        vector<int> missing;
        for (int mask = 1; mask <= full; ++mask)
            if (popcount(static_cast<unsigned>(mask)) == rank + 1 &&
                !value.covered[mask])
                missing.push_back(mask);
        if (missing.empty()) return false;
        const int target = missing[random() % missing.size()];
        vector<int> vertices;
        for (int bit = 0; bit < k; ++bit)
            if (target & (1 << bit)) vertices.push_back(target ^ (1 << bit));
        vector<int> position(1 << k, -1);
        for (int i = 0; i < static_cast<int>(path.size()); ++i)
            position[path[i]] = i;
        shuffle(vertices.begin(), vertices.end(), random);
        for (int first : vertices) for (int second : vertices) {
            if (first == second) continue;
            int i = position[first], j = position[second];
            if (i > j) swap(i, j);
            // Reverse [i+1,j], thereby introducing path[i]--path[j].
            if (j > i + 1 &&
                (j + 1 == static_cast<int>(path.size()) ||
                 adjacent(path[i + 1], path[j + 1]))) {
                reverse(path.begin() + i + 1, path.begin() + j + 1);
                if (rainbow(path)) return true;
                reverse(path.begin() + i + 1, path.begin() + j + 1);
            }
            // Reverse [i,j-1], which introduces the same desired edge at the
            // other cut and is often valid when the first orientation is not.
            if (j > i + 1 &&
                (i == 0 || adjacent(path[i - 1], path[j - 1]))) {
                reverse(path.begin() + i, path.begin() + j);
                if (rainbow(path)) return true;
                reverse(path.begin() + i, path.begin() + j);
            }
        }
        return false;
    }

    bool relocate(vector<int>& path, mt19937_64& random) const {
        const int n = path.size();
        for (int attempt = 0; attempt < 80; ++attempt) {
            const int length = 1 + random() % 8;
            const int left = random() % (n - length + 1);
            const int right = left + length;
            // Removing an internal block creates this bridge.  Reject the cut
            // before spending time on possible insertion sites.
            if (left && right < n && !adjacent(path[left - 1], path[right]))
                continue;
            vector<int> reduced;
            reduced.reserve(n - length);
            reduced.insert(reduced.end(), path.begin(), path.begin() + left);
            reduced.insert(reduced.end(), path.begin() + right, path.end());
            for (int orientation = 0; orientation < 2; ++orientation) {
                vector<int> block(path.begin() + left, path.begin() + right);
                if (orientation) reverse(block.begin(), block.end());
                vector<int> gaps;
                for (int gap = 0; gap <= static_cast<int>(reduced.size()); ++gap) {
                    if (gap == left) continue;
                    if (gap && !adjacent(reduced[gap - 1], block.front())) continue;
                    if (gap < static_cast<int>(reduced.size()) &&
                        !adjacent(block.back(), reduced[gap])) continue;
                    gaps.push_back(gap);
                }
                shuffle(gaps.begin(), gaps.end(), random);
                for (int gap : gaps) {
                    vector<int> candidate = reduced;
                    candidate.insert(candidate.begin() + gap,
                                     block.begin(), block.end());
                    if (!rainbow(candidate)) continue;
                    path.swap(candidate);
                    return true;
                }
            }
        }
        return false;
    }

    void worker(int id, int epoch,
                chrono::steady_clock::time_point epoch_deadline,
                vector<int> start) {
        mt19937_64 random(0x9e3779b97f4a7c15ULL * (id + 1) ^
            0xbf58476d1ce4e5b9ULL * (epoch + 1) ^
            chrono::high_resolution_clock::now().time_since_epoch().count());
        uniform_real_distribution<double> uniform(0.0, 1.0);
        vector<int> path = move(start);
        Eval current = evaluate(path);
        long long current_score = score(current);
        vector<int> local_best = path;
        Eval local_eval = current;
        long long iteration = 0;
        while (chrono::steady_clock::now() < epoch_deadline) {
            ++iteration;
            vector<int> candidate = path;
            bool moved = false;
            const int choice = random() % 100;
            if (choice < 30) moved = reverse_target(candidate, current, random);
            else if (choice < 82) moved = reverse_random(candidate, random);
            else moved = relocate(candidate, random);
            if (!moved) continue;
            Eval next = evaluate(candidate);
            if (!admissible(next)) continue;
            const long long next_score = score(next);
            // Reheat every 20,000 proposals.  Temperatures are expressed in
            // one mask-weight unit (1e6 in score()).
            const double phase = (iteration % 20000) / 20000.0;
            const double temperature = 8.0e6 * pow(1.0e-3, phase) + 1.0;
            if (next_score >= current_score ||
                uniform(random) < exp((next_score - current_score) / temperature)) {
                path.swap(candidate);
                current = move(next);
                current_score = next_score;
            }
            if (score(current) > score(local_eval)) {
                local_best = path;
                local_eval = current;
            }
            if (current.upper >= raw_upper.load(memory_order_relaxed)) {
                lock_guard<mutex> guard(lock);
                if (raw_better(current, raw_best_eval)) {
                    raw_best = path;
                    raw_best_eval = current;
                    raw_upper.store(current.upper, memory_order_relaxed);
                    report("raw-best", raw_best_eval, epoch);
                    save(raw_best);
                }
            }
        }
        lock_guard<mutex> guard(lock);
        if (score(local_eval) > score(incumbent_eval)) {
            incumbent = move(local_best);
            incumbent_eval = move(local_eval);
        }
    }

    void run() {
        final_deadline = chrono::steady_clock::now() +
            chrono::milliseconds(static_cast<long long>(seconds * 1000));
        int epoch = 0;
        report("initial", incumbent_eval, epoch);
        while (chrono::steady_clock::now() < final_deadline &&
               raw_upper.load(memory_order_relaxed) < upper_total()) {
            const auto epoch_deadline = min(final_deadline,
                chrono::steady_clock::now() + chrono::milliseconds(
                    static_cast<long long>(epoch_seconds * 1000)));
            // Under the new weights, recompute the incumbent's score before
            // launching the independent annealing replicas.
            incumbent_eval = evaluate(incumbent);
            vector<thread> pool;
            for (int id = 0; id < threads; ++id)
                pool.emplace_back(&Search::worker, this, id, epoch,
                                  epoch_deadline, incumbent);
            for (thread& worker_thread : pool) worker_thread.join();
            incumbent_eval = evaluate(incumbent);
            report("epoch-best", incumbent_eval, epoch);
            // Breakout step: every still-missing mask becomes more expensive.
            // Rank-7 holes receive a little more pressure because they are
            // controlled by individual path edges and enable higher windows.
            for (int mask = 1; mask <= full; ++mask) {
                const int r = popcount(static_cast<unsigned>(mask));
                if (r <= rank || incumbent_eval.covered[mask]) continue;
                weights[mask] += r == rank + 1 ? 3 : 2;
            }
            // Keep the best raw-coverage path as a periodic restart, while
            // retaining a weighted incumbent when it has genuinely absorbed
            // the accumulated hard masks.
            if (epoch % 4 == 3 && raw_best_eval.upper >= incumbent_eval.upper - 4)
                incumbent = raw_best;
            ++epoch;
        }
        save(raw_best);
    }

    int upper_total() const {
        int result = 0;
        for (int mask = 1; mask <= full; ++mask)
            if (popcount(static_cast<unsigned>(mask)) > rank) ++result;
        return result;
    }

    Search(int bits, int central_rank, int slack, int thread_count,
           double duration, double epoch_duration, string output,
           vector<int> seed)
        : k(bits), rank(central_rank), d(slack), threads(thread_count),
          full((1 << bits) - 1), seconds(duration),
          epoch_seconds(epoch_duration), output_path(move(output)),
          weights(1 << bits, 1), incumbent(move(seed)) {
        if (!rainbow(incumbent))
            throw runtime_error("seed is not a rainbow Johnson path");
        incumbent_eval = evaluate(incumbent);
        required_lower = incumbent_eval.lower;
        required_possible = incumbent_eval.possible;
        raw_best = incumbent;
        raw_best_eval = incumbent_eval;
        raw_upper.store(raw_best_eval.upper, memory_order_relaxed);
    }
};

int main(int argc, char** argv) {
    if (argc != 9) {
        cerr << "usage: program k rank d threads seconds epoch_seconds input output\n";
        return 2;
    }
    vector<int> seed;
    ifstream input(argv[7]);
    for (int value; input >> value;) seed.push_back(value);
    Search search(stoi(argv[1]), stoi(argv[2]), stoi(argv[3]), stoi(argv[4]),
                  stod(argv[5]), stod(argv[6]), argv[8], move(seed));
    search.run();
    return 0;
}
