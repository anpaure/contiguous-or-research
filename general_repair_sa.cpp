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
    int weighted = 0;
    vector<int> missing;
    bool better_than(const Evaluation& other) const {
        return covered != other.covered ? covered > other.covered
                                        : potential > other.potential;
    }
};

struct Search {
    int k, limit, thread_count;
    double seconds;
    string output_path;
    vector<int> global_array;
    Evaluation global_evaluation;
    atomic<long long> global_key{-1};
    mutex global_mutex;
    chrono::steady_clock::time_point deadline;

    Evaluation evaluate(const vector<int>& a, const vector<int>* weights = nullptr,
                        bool collect_missing = false) const {
        vector<uint16_t> count(limit);
        vector<int> previous, current;
        previous.reserve(k + 1);
        current.reserve(k + 1);
        for (int x : a) {
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
        for (int mask = 1; mask < limit; ++mask) {
            if (!count[mask]) {
                if (collect_missing) result.missing.push_back(mask);
                continue;
            }
            ++result.covered;
            result.weighted += weights ? (*weights)[mask] : 1;
            int reward = 1024, increment = 256;
            for (int occurrence = 1; occurrence < count[mask] && increment;
                 ++occurrence, increment >>= 1)
                reward += increment;
            const int rank = popcount(static_cast<unsigned>(mask));
            const int layer_weight = rank == k / 2 ? 8
                : (abs(rank - k / 2) == 1 ? 4 : 1);
            result.potential += layer_weight * reward;
        }
        return result;
    }

    static long long canonical_key(const Evaluation& e) {
        return static_cast<long long>(e.covered) * 1000000000LL + e.potential;
    }

    static long long local_score(const Evaluation& e) {
        return static_cast<long long>(e.weighted) * 10000000LL + e.potential;
    }

    void save() {
        ofstream output(output_path);
        for (int value : global_array) output << value << ' ';
        output << '\n';
    }

    void report(const Evaluation& e) {
        cerr << "best=" << e.covered << '/' << limit - 1
             << " potential=" << e.potential << " missing";
        Evaluation detailed = evaluate(global_array, nullptr, true);
        for (int mask : detailed.missing) cerr << ' ' << mask;
        cerr << '\n';
    }

    void worker(int id) {
        mt19937_64 random(0x94d049bb133111ebULL * (id + 1) ^
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
            long long score = local_score(current);
            for (int iteration = 0;
                 iteration < 500000 && chrono::steady_clock::now() < deadline;
                 ++iteration) {
                if (iteration && iteration % 5000 == 0) {
                    Evaluation audit = evaluate(a, &weights, true);
                    for (int mask : audit.missing) weights[mask] += 5;
                    current = evaluate(a, &weights);
                    score = local_score(current);
                }
                vector<pair<int, int>> old;
                const int operation = random() % 100;
                if (operation < 65) {
                    const int moves = operation < 50 ? 1 : 2 + random() % 4;
                    const int base = random() % a.size();
                    for (int move = 0; move < moves; ++move) {
                        const int position = operation < 55 ? random() % a.size()
                            : clamp(base + static_cast<int>(random() % 9) - 4,
                                    0, static_cast<int>(a.size()) - 1);
                        if (find_if(old.begin(), old.end(), [&] (auto item) {
                                return item.first == position;
                            }) != old.end()) continue;
                        old.push_back({position, a[position]});
                        const int kind = random() % 10;
                        if (kind < 3) a[position] = 1 << (random() % k);
                        else if (kind < 7) {
                            a[position] ^= 1 << (random() % k);
                            if (!a[position]) a[position] = 1 << (random() % k);
                        } else a[position] = 1 + random() % (limit - 1);
                    }
                } else if (operation < 82) {
                    const int x = random() % a.size(), y = random() % a.size();
                    old.push_back({x, a[x]});
                    if (y != x) old.push_back({y, a[y]});
                    swap(a[x], a[y]);
                } else {
                    int x = random() % a.size(), y = random() % a.size();
                    if (x > y) swap(x, y);
                    for (int position = x; position <= y; ++position)
                        old.push_back({position, a[position]});
                    reverse(a.begin() + x, a.begin() + y + 1);
                }
                Evaluation next = evaluate(a, &weights);
                const long long next_score = local_score(next);
                const double phase = (iteration % 5000) / 5000.0;
                const double temperature = 2.0e7 * pow(1.0e-5, phase) + 1.0;
                if (next_score >= score ||
                    uniform(random) < exp((next_score - score) / temperature)) {
                    current = move(next);
                    score = next_score;
                } else {
                    for (auto [position, value] : old) a[position] = value;
                }

                Evaluation canonical = evaluate(a);
                const long long candidate_key = canonical_key(canonical);
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

    Search(int bits, int threads, double duration, string result_path, vector<int> seed)
        : k(bits), limit(1 << bits), thread_count(threads), seconds(duration),
          output_path(move(result_path)), global_array(move(seed)) {
        global_evaluation = evaluate(global_array);
        global_key.store(canonical_key(global_evaluation));
    }

    void run() {
        report(global_evaluation);
        deadline = chrono::steady_clock::now() + chrono::milliseconds(
            static_cast<long long>(seconds * 1000));
        vector<thread> pool;
        for (int id = 0; id < thread_count; ++id) pool.emplace_back(&Search::worker, this, id);
        for (thread& worker : pool) worker.join();
        save();
    }
};

int main(int argc, char** argv) {
    if (argc < 5) return 2;
    const int k = stoi(argv[1]);
    const int threads = stoi(argv[2]);
    const double seconds = stod(argv[3]);
    vector<int> seed;
    for (int value; cin >> value;) seed.push_back(value);
    if (seed.empty()) return 2;
    Search search(k, threads, seconds, argv[4], move(seed));
    search.run();
}
