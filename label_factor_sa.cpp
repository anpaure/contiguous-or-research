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

struct Evaluation {
    int covered = 0;
    int potential = 0;
    vector<int> by_rank;

    bool better_than(const Evaluation& other) const {
        if (covered != other.covered) return covered > other.covered;
        return potential > other.potential;
    }
};

struct Search {
    int k, d, limit, threads, extra_gap;
    bool has_extra = true;
    double seconds;
    vector<int> central, envelope;
    vector<vector<int>> domains;
    vector<int> global_array;
    Evaluation global_evaluation;
    atomic<long long> global_key{-1};
    mutex global_mutex;
    chrono::steady_clock::time_point deadline;
    string output_path;

    Evaluation evaluate(const vector<int>& a, const vector<int>* weights = nullptr,
                        bool collect_missing = false, vector<int>* missing = nullptr) const {
        vector<uint16_t> count(limit);
        vector<int> previous, current;
        previous.reserve(k + 1);
        current.reserve(k + 1);
        for (int output_position = 0;
             output_position < static_cast<int>(a.size()); ++output_position) {
            const int x = !has_extra ? a[output_position]
                : (output_position == extra_gap ? a.back()
                   : a[output_position - (output_position > extra_gap)]);
            current.clear();
            current.push_back(x);
            for (int old : previous) {
                const int value = old | x;
                if (current.back() != value) current.push_back(value);
            }
            for (int value : current) if (count[value] != 65535) ++count[value];
            previous.swap(current);
        }
        Evaluation result;
        result.by_rank.assign(k + 1, 0);
        for (int mask = 1; mask < limit; ++mask) {
            if (!count[mask]) {
                if (collect_missing && missing) missing->push_back(mask);
                continue;
            }
            ++result.covered;
            ++result.by_rank[popcount(static_cast<unsigned>(mask))];
            int reward = 1024;
            int increment = 256;
            for (int occurrence = 1; occurrence < count[mask] && increment;
                 ++occurrence, increment >>= 1)
                reward += increment;
            result.potential += reward * (weights ? (*weights)[mask] : 1);
        }
        return result;
    }

    bool factor_valid_at(const vector<int>& a, int position) const {
        const int first = max(0, position - d);
        const int last = min(static_cast<int>(central.size()) - 1, position);
        for (int start = first; start <= last; ++start) {
            int value = 0;
            for (int j = start; j <= start + d; ++j) value |= a[j];
            if (value != central[start]) return false;
        }
        return true;
    }

    static long long key(const Evaluation& e) {
        return static_cast<long long>(e.covered) * 1000000000LL + e.potential;
    }

    long long local_score(const Evaluation& e, const vector<int>& weights) const {
        long long weighted_coverage = 0;
        for (int rank = 1; rank <= k; ++rank)
            weighted_coverage += static_cast<long long>(e.by_rank[rank]);
        (void) weights;
        return static_cast<long long>(e.covered) * 10000000LL + e.potential;
    }

    void save() {
        ofstream output(output_path);
        for (int position = 0; position < static_cast<int>(global_array.size()); ++position) {
            const int value = !has_extra ? global_array[position]
                : (position == extra_gap ? global_array.back()
                   : global_array[position - (position > extra_gap)]);
            output << value << ' ';
        }
        output << '\n';
    }

    void report(const Evaluation& e) {
        cerr << "best covered=" << e.covered << '/' << limit - 1
             << " potential=" << e.potential << " ranks";
        for (int rank = 1; rank <= k; ++rank)
            cerr << ' ' << rank << ':' << e.by_rank[rank];
        cerr << '\n';
    }

    void worker(int id) {
        mt19937_64 random(0xd1b54a32d192ed03ULL * (id + 1) ^
            chrono::high_resolution_clock::now().time_since_epoch().count());
        uniform_real_distribution<double> uniform(0.0, 1.0);
        while (chrono::steady_clock::now() < deadline) {
            vector<int> a;
            {
                lock_guard<mutex> lock(global_mutex);
                a = global_array;
            }
            vector<int> weights(limit, 1);
            Evaluation current = evaluate(a, &weights);
            long long score = local_score(current, weights);
            for (int iteration = 0;
                 iteration < 300000 && chrono::steady_clock::now() < deadline;
                 ++iteration) {
                if (iteration && iteration % 5000 == 0) {
                    vector<int> missing;
                    evaluate(a, &weights, true, &missing);
                    for (int mask : missing) weights[mask] += 5;
                    current = evaluate(a, &weights);
                    score = local_score(current, weights);
                }
                const int move_count = random() % 100 < 75 ? 1 : 2 + random() % 3;
                vector<int> positions, old_values;
                const int base = random() % a.size();
                for (int move = 0; move < move_count; ++move) {
                    int position;
                    if (move_count > 1 && random() % 100 < 80) {
                        const int offset = static_cast<int>(random() % 7) - 3;
                        position = clamp(base + offset, 0, static_cast<int>(a.size()) - 1);
                    } else {
                        position = random() % a.size();
                    }
                    if (find(positions.begin(), positions.end(), position) != positions.end())
                        continue;
                    positions.push_back(position);
                    old_values.push_back(a[position]);
                    if (position < static_cast<int>(envelope.size())) {
                        const vector<int>& domain = domains[position];
                        a[position] = domain[random() % domain.size()];
                    } else {
                        a[position] = 1 + random() % (limit - 1);
                    }
                }
                bool changed = false, valid = true;
                for (int i = 0; i < static_cast<int>(positions.size()); ++i) {
                    changed |= a[positions[i]] != old_values[i];
                    if (positions[i] < static_cast<int>(envelope.size()))
                        valid &= factor_valid_at(a, positions[i]);
                }
                if (!changed || !valid) {
                    for (int i = 0; i < static_cast<int>(positions.size()); ++i)
                        a[positions[i]] = old_values[i];
                    continue;
                }
                Evaluation next = evaluate(a, &weights);
                const long long next_score = local_score(next, weights);
                const double phase = (iteration % 5000) / 5000.0;
                const double temperature = 2.0e7 * pow(1.0e-5, phase) + 1.0;
                if (next_score >= score ||
                    uniform(random) < exp((next_score - score) / temperature)) {
                    current = move(next);
                    score = next_score;
                } else {
                    for (int i = 0; i < static_cast<int>(positions.size()); ++i)
                        a[positions[i]] = old_values[i];
                }

                const Evaluation canonical = evaluate(a);
                const long long candidate_key = key(canonical);
                long long old_key = global_key.load(memory_order_relaxed);
                if (candidate_key > old_key && global_key.compare_exchange_strong(
                        old_key, candidate_key, memory_order_relaxed)) {
                    lock_guard<mutex> lock(global_mutex);
                    if (canonical.better_than(global_evaluation)) {
                        global_evaluation = canonical;
                        global_array = a;
                        report(global_evaluation);
                        save();
                        if (global_evaluation.covered == limit - 1) exit(0);
                    }
                }
            }
        }
    }

    Search(int bits, int slack, int thread_count, double duration,
           vector<int> prescribed, string result_path, vector<int> seed, int gap)
        : k(bits), d(slack), limit(1 << bits), threads(thread_count),
          seconds(duration), central(move(prescribed)), output_path(move(result_path)) {
        const int n = central.size() + d;
        has_extra = gap != -2;
        extra_gap = gap < 0 ? n : clamp(gap, 0, n);
        envelope.assign(n, limit - 1);
        domains.resize(n);
        for (int position = 0; position < n; ++position) {
            for (int i = max(0, position - d);
                 i <= min(static_cast<int>(central.size()) - 1, position); ++i)
                envelope[position] &= central[i];
            for (int submask = envelope[position]; submask;
                 submask = (submask - 1) & envelope[position])
                domains[position].push_back(submask);
        }
        global_array = envelope;
        if (has_extra) global_array.push_back(1);
        if (seed.size() == global_array.size()) global_array.swap(seed);
        global_evaluation = evaluate(global_array);
        global_key.store(key(global_evaluation));
    }

    void run() {
        report(global_evaluation);
        deadline = chrono::steady_clock::now() + chrono::milliseconds(
            static_cast<long long>(seconds * 1000));
        vector<thread> pool;
        for (int id = 0; id < threads; ++id) pool.emplace_back(&Search::worker, this, id);
        for (thread& worker : pool) worker.join();
        save();
    }
};

int main(int argc, char** argv) {
    if (argc < 5) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    const int threads = stoi(argv[3]);
    const double seconds = stod(argv[4]);
    const string output_path = argc > 5 ? argv[5] : "factor_label_best.txt";
    vector<int> seed;
    if (argc > 6) {
        ifstream input(argv[6]);
        for (int value; input >> value;) seed.push_back(value);
    }
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    if (argc > 7) {
        const string mode = argv[7];
        if (mode.find("reverse") != string::npos)
            reverse(central.begin(), central.end());
        if (mode.find("complement") != string::npos)
            for (int& value : central) value ^= (1 << k) - 1;
    }
    const int gap = argc > 8 ? stoi(argv[8]) : -1;
    Search search(k, d, threads, seconds, move(central), output_path, move(seed), gap);
    search.run();
}
