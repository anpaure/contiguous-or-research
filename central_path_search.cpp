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
#include <climits>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <random>
#include <thread>
#include <vector>

using namespace std;

struct Evaluation {
    int run_deficit = 0;
    int covered = 0;
    int potential = 0;
    int weighted_covered = 0;
    int upper_covered = 0;
    int lower_covered = 0;
    int priority = 0;
    vector<int> missing;
    vector<int> by_rank;

    bool better_than(const Evaluation& other) const {
        if (run_deficit != other.run_deficit)
            return run_deficit < other.run_deficit;
        if (priority != other.priority) return priority > other.priority;
        if (covered != other.covered) return covered > other.covered;
        return potential > other.potential;
    }
};

struct Search {
    int k;
    int rank;
    int d;
    int thread_count;
    double seconds;
    int mask_count;
    vector<int> desired;
    vector<int> initial;
    string output_path;
    bool upper_priority;
    bool lower_priority;
    bool bridge_priority;
    mutex best_mutex;
    atomic<long long> best_key{LLONG_MIN};
    Evaluation global_evaluation;
    vector<int> global_path;
    chrono::steady_clock::time_point deadline;

    static bool adjacent(int x, int y) {
        return popcount(static_cast<unsigned>(x ^ y)) == 2;
    }

    vector<int> reflected_gray(int n, int choose) const {
        if (choose == 0) return {0};
        if (choose == n) return {(1 << n) - 1};
        vector<int> first = reflected_gray(n - 1, choose);
        vector<int> second = reflected_gray(n - 1, choose - 1);
        reverse(second.begin(), second.end());
        for (int& value : second) value |= 1 << (n - 1);
        first.insert(first.end(), second.begin(), second.end());
        return first;
    }

    Evaluation evaluate(const vector<int>& path,
                        const vector<int>* weights = nullptr,
                        bool collect_missing = false) const {
        Evaluation result;
        result.by_rank.assign(k + 1, 0);
        for (int bit = 0; bit < k; ++bit) {
            int position = 0;
            while (position < static_cast<int>(path.size())) {
                if (!(path[position] & (1 << bit))) {
                    ++position;
                    continue;
                }
                const int first = position;
                while (position < static_cast<int>(path.size()) &&
                       (path[position] & (1 << bit))) ++position;
                if (first > 0 && position < static_cast<int>(path.size()))
                    result.run_deficit += max(0, d + 1 - (position - first));
            }
        }

        vector<uint8_t> counts(mask_count);
        auto record = [&] (int value, int wanted_rank) {
            if (popcount(static_cast<unsigned>(value)) != wanted_rank) return;
            if (!counts[value]) {
                ++result.covered;
                ++result.by_rank[wanted_rank];
                if (wanted_rank > rank) ++result.upper_covered;
                if (wanted_rank < rank) ++result.lower_covered;
            }
            if (counts[value] != 255) ++counts[value];
        };
        for (int value : path) record(value, rank);

        // Lower shadows: intersections of 2,...,d+1 central sets.
        for (int length = 2; length <= d + 1; ++length) {
            const int wanted_rank = rank - length + 1;
            for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
                int value = mask_count - 1;
                for (int j = left; j < left + length; ++j) value &= path[j];
                record(value, wanted_rank);
            }
        }

        // Upper shadows: unions through the full ground set.
        for (int length = 2; rank + length - 1 <= k; ++length) {
            const int wanted_rank = rank + length - 1;
            for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
                int value = 0;
                for (int j = left; j < left + length; ++j) value |= path[j];
                record(value, wanted_rank);
            }
        }
        for (int mask : desired) {
            if (!counts[mask]) {
                if (collect_missing) result.missing.push_back(mask);
                continue;
            }
            result.weighted_covered += weights ? (*weights)[mask] : 1;
            int reward = 1024;
            int increment = 256;
            for (int occurrence = 1; occurrence < counts[mask] && increment;
                 ++occurrence, increment >>= 1)
                reward += increment;
            const int mask_rank = popcount(static_cast<unsigned>(mask));
            const int weight = abs(mask_rank - rank) == 1 ? 4 : 1;
            result.potential += weight * reward;
        }
        result.priority = upper_priority ? result.upper_covered
            : (lower_priority ? result.lower_covered
               : (bridge_priority ? result.covered + 2 * result.lower_covered
                                  : result.covered));
        return result;
    }

    long long scalar(const Evaluation& value) const {
        return static_cast<long long>(value.weighted_covered) * 10000000LL
             + value.potential
             - static_cast<long long>(value.run_deficit) * 1000000000LL;
    }

    static long long comparison_key(const Evaluation& value) {
        return -static_cast<long long>(value.run_deficit) * 1000000000000LL
             + static_cast<long long>(value.priority) * 1000000000LL
             + static_cast<long long>(value.covered) * 1000000LL
             + value.potential;
    }

    void print_best(const Evaluation& value) {
        cerr << "best deficit=" << value.run_deficit
             << " covered=" << value.covered << '/' << desired.size()
             << " upper=" << value.upper_covered
             << " lower=" << value.lower_covered
             << " potential=" << value.potential
             << " ranks";
        for (int r = 0; r <= k; ++r)
            if (value.by_rank[r]) cerr << ' ' << r << ':' << value.by_rank[r];
        cerr << '\n';
    }

    void save_best() {
        ofstream output(output_path);
        for (int value : global_path) output << value << ' ';
        output << '\n';
    }

    bool reverse_move(vector<int>& path, mt19937_64& random) const {
        const int n = path.size();
        for (int attempt = 0; attempt < 200; ++attempt) {
            int left = random() % n;
            int right = random() % n;
            if (left > right) swap(left, right);
            if (right - left < 2) continue;
            if (left > 0 && !adjacent(path[left - 1], path[right])) continue;
            if (right + 1 < n && !adjacent(path[left], path[right + 1])) continue;
            reverse(path.begin() + left, path.begin() + right + 1);
            return true;
        }
        return false;
    }

    bool relocate_move(vector<int>& path, mt19937_64& random) const {
        const int n = path.size();
        for (int attempt = 0; attempt < 100; ++attempt) {
            const int length = 1 + random() % 6;
            const int left = random() % (n - length + 1);
            const int right = left + length;
            if (left > 0 && right < n && !adjacent(path[left - 1], path[right]))
                continue;
            vector<int> block(path.begin() + left, path.begin() + right);
            vector<int> reduced;
            reduced.reserve(n - length);
            reduced.insert(reduced.end(), path.begin(), path.begin() + left);
            reduced.insert(reduced.end(), path.begin() + right, path.end());
            if (random() & 1) reverse(block.begin(), block.end());
            for (int gap_attempt = 0; gap_attempt < 100; ++gap_attempt) {
                const int gap = random() % (reduced.size() + 1);
                if (gap == left) continue;
                if (gap > 0 && !adjacent(reduced[gap - 1], block.front())) continue;
                if (gap < static_cast<int>(reduced.size()) &&
                    !adjacent(block.back(), reduced[gap])) continue;
                reduced.insert(reduced.begin() + gap, block.begin(), block.end());
                path.swap(reduced);
                return true;
            }
        }
        return false;
    }

    bool mutate(vector<int>& path, mt19937_64& random) const {
        const int type = random() % 100;
        if (type < 60) return reverse_move(path, random);
        if (type < 80) return relocate_move(path, random);
        const int moves = 2 + random() % 3;
        bool changed = false;
        for (int i = 0; i < moves; ++i)
            changed |= random() % 4 ? reverse_move(path, random)
                                    : relocate_move(path, random);
        return changed;
    }

    void worker(int id) {
        mt19937_64 random(0x9e3779b97f4a7c15ULL * (id + 1) ^
            chrono::high_resolution_clock::now().time_since_epoch().count());
        uniform_real_distribution<double> uniform(0.0, 1.0);
        while (chrono::steady_clock::now() < deadline) {
            vector<int> path;
            {
                lock_guard<mutex> lock(best_mutex);
                path = global_path;
            }
            for (int i = 0; i < id * 7; ++i) mutate(path, random);
            vector<int> weights(mask_count, 1);
            if (upper_priority)
                for (int mask : desired)
                    if (popcount(static_cast<unsigned>(mask)) > rank) weights[mask] = 8;
            if (lower_priority || bridge_priority)
                for (int mask : desired)
                    if (popcount(static_cast<unsigned>(mask)) < rank)
                        weights[mask] = bridge_priority ? 3 : 8;
            Evaluation current = evaluate(path, &weights);
            long long current_score = scalar(current);
            for (int iteration = 0;
                 iteration < 200000 && chrono::steady_clock::now() < deadline;
                 ++iteration) {
                if (iteration && iteration % 5000 == 0) {
                    Evaluation audit = evaluate(path, &weights, true);
                    for (int mask : audit.missing) weights[mask] += 5;
                    current = evaluate(path, &weights);
                    current_score = scalar(current);
                }
                vector<int> candidate = path;
                if (!mutate(candidate, random)) continue;
                Evaluation next = evaluate(candidate, &weights);
                const long long next_score = scalar(next);
                const double phase = (iteration % 5000) / 5000.0;
                const double temperature = 2.0e8 * pow(1.0e-5, phase) + 1.0;
                const bool accept = next_score >= current_score ||
                    uniform(random) < exp((next_score - current_score) / temperature);
                if (accept) {
                    path.swap(candidate);
                    current = move(next);
                    current_score = next_score;
                }
                const long long key = comparison_key(current);
                long long old_key = best_key.load(memory_order_relaxed);
                if (key > old_key && best_key.compare_exchange_strong(
                        old_key, key, memory_order_relaxed)) {
                    lock_guard<mutex> lock(best_mutex);
                    if (current.better_than(global_evaluation)) {
                        global_evaluation = current;
                        global_path = path;
                        print_best(global_evaluation);
                        save_best();
                    }
                }
            }
        }
    }

    Search(int bits, int central_rank, int slack, int threads, double duration,
           const string& input_path, string result_path,
           bool prioritize_upper, bool prioritize_lower, bool bridge)
        : k(bits), rank(central_rank), d(slack), thread_count(threads),
          seconds(duration), mask_count(1 << bits), initial(reflected_gray(bits, central_rank)),
          output_path(move(result_path)), upper_priority(prioritize_upper),
          lower_priority(prioritize_lower), bridge_priority(bridge) {
        if (!input_path.empty()) {
            ifstream input(input_path);
            vector<int> loaded;
            for (int value; input >> value;) loaded.push_back(value);
            if (loaded.size() == initial.size()) initial.swap(loaded);
        }
        desired.assign(mask_count, 0);
        int total = 0;
        for (int mask = 1; mask < mask_count; ++mask) {
            const int r = popcount(static_cast<unsigned>(mask));
            if ((r >= rank - d && r <= rank + (k - rank)) && r != 1) {
                desired[total++] = mask;
            }
        }
        desired.resize(total);
        global_path = initial;
        global_evaluation = evaluate(global_path);
        best_key.store(comparison_key(global_evaluation));
    }

    void run() {
        cerr << "k=" << k << " rank=" << rank << " d=" << d
             << " vertices=" << initial.size() << " threads=" << thread_count << '\n';
        print_best(global_evaluation);
        deadline = chrono::steady_clock::now() + chrono::milliseconds(
            static_cast<long long>(seconds * 1000));
        vector<thread> threads;
        for (int id = 0; id < thread_count; ++id)
            threads.emplace_back(&Search::worker, this, id);
        for (thread& worker : threads) worker.join();
        save_best();
    }
};

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const int rank = argc > 2 ? stoi(argv[2]) : 5;
    const int d = argc > 3 ? stoi(argv[3]) : 3;
    const int threads = argc > 4 ? stoi(argv[4]) : 8;
    const double seconds = argc > 5 ? stod(argv[5]) : 60.0;
    const string input_path = argc > 6 ? argv[6] : "";
    const string output_path = argc > 7 ? argv[7] : "central_path_best.txt";
    const string mode = argc > 8 ? argv[8] : "";
    const bool upper_priority = mode == "upper";
    const bool lower_priority = mode == "lower";
    const bool bridge_priority = mode == "bridge";
    Search search(k, rank, d, threads, seconds, input_path, output_path,
                  upper_priority, lower_priority, bridge_priority);
    search.run();
}
