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
#include <fstream>
#include <iostream>
#include <mutex>
#include <numeric>
#include <random>
#include <string>
#include <thread>
#include <vector>

using namespace std;

struct Evaluation {
    int covered = 0;
    int middle = 0;
    array<int, 13> rank{};
};

struct Evaluator {
    vector<uint32_t> stamp = vector<uint32_t>(4096);
    uint32_t generation = 0;
    vector<int> base_suffix;

    explicit Evaluator(const vector<int>& base) {
        int value = 0;
        for (auto it = base.rbegin(); it != base.rend(); ++it) {
            const int next = value | *it;
            if (next != value) base_suffix.push_back(next);
            value = next;
        }
        base_suffix.push_back(0); // intervals beginning at the inserted high bit
    }

    Evaluation operator()(const vector<int>& residue) {
        if (++generation == 0) { fill(stamp.begin(), stamp.end(), 0); ++generation; }
        Evaluation e;
        auto record = [&](int x) {
            if (stamp[x] == generation) return;
            stamp[x] = generation;
            ++e.covered;
            const int r = popcount(static_cast<unsigned>(x));
            ++e.rank[r];
            if (r == 6) ++e.middle;
        };
        record(0);
        array<int, 16> previous{}, current{};
        int previous_size = 0;
        for (int x : residue) {
            int current_size = 0;
            current[current_size++] = x;
            for (int i = 0; i < previous_size; ++i) {
                const int value = previous[i] | x;
                if (value != current[current_size - 1]) current[current_size++] = value;
            }
            for (int i = 0; i < current_size; ++i) record(current[i]);
            previous.swap(current);
            previous_size = current_size;
        }
        int prefix = 0;
        for (int j = -1; j < static_cast<int>(residue.size()); ++j) {
            if (j >= 0) prefix |= residue[j];
            for (int suffix : base_suffix) record(prefix | suffix);
        }
        return e;
    }
};

struct Shared {
    mutex lock;
    atomic<long long> best_key{-1};
    vector<int> best_residue;
    Evaluation best_eval;
    string output;
    vector<int> base;

    void publish(const vector<int>& residue, const Evaluation& e, int id, long long iteration) {
        const long long key = static_cast<long long>(e.covered) * 10000 + e.middle;
        long long old = best_key.load(memory_order_relaxed);
        if (key <= old || !best_key.compare_exchange_strong(old, key)) return;
        lock_guard<mutex> guard(lock);
        if (key <= static_cast<long long>(best_eval.covered) * 10000 + best_eval.middle) return;
        best_eval = e;
        best_residue = residue;
        ofstream out(output);
        for (int x : residue) out << x << ' ';
        out << '\n';
        cerr << "BEST worker=" << id << " iteration=" << iteration
             << " covered=" << e.covered << "/4096 middle=" << e.middle << "/924 ranks";
        for (int r = 0; r <= 12; ++r) cerr << ' ' << r << ':' << e.rank[r];
        cerr << '\n';
        if (e.covered == 4096) {
            ofstream full(output + ".full");
            for (int x : base) full << x << ' ';
            full << (1 << 12) << ' ';
            for (int x : residue) full << ((1 << 12) | x) << ' ';
            full << '\n';
        }
    }
};

static vector<int> materialize(const vector<int>& base, const vector<uint8_t>& selected) {
    vector<int> result;
    result.reserve(792);
    for (int i = 0; i < static_cast<int>(base.size()); ++i)
        if (selected[i]) result.push_back(base[i]);
    return result;
}

static void worker(Shared& shared, int id, chrono::steady_clock::time_point deadline,
                   uint64_t seed) {
    mt19937_64 rng(seed ^ (0x9e3779b97f4a7c15ULL * (id + 1)));
    uniform_real_distribution<double> uniform(0.0, 1.0);
    Evaluator evaluator(shared.base);
    const int n = shared.base.size();
    while (chrono::steady_clock::now() < deadline) {
        vector<uint8_t> selected(n, 1);
        vector<int> order(n);
        iota(order.begin(), order.end(), 0);
        shuffle(order.begin(), order.end(), rng);
        for (int i = 0; i < n - 792; ++i) selected[order[i]] = 0;
        vector<int> residue = materialize(shared.base, selected);
        Evaluation current = evaluator(residue);
        long long current_key = static_cast<long long>(current.covered) * 10000 + current.middle;
        shared.publish(residue, current, id, 0);

        for (long long iteration = 1; iteration <= 250000 &&
             chrono::steady_clock::now() < deadline; ++iteration) {
            int out, in;
            do out = rng() % n; while (!selected[out]);
            do in = rng() % n; while (selected[in]);
            selected[out] = 0; selected[in] = 1;
            vector<int> candidate = materialize(shared.base, selected);
            Evaluation next = evaluator(candidate);
            const long long next_key = static_cast<long long>(next.covered) * 10000 + next.middle;
            const double phase = (iteration % 10000) / 10000.0;
            const double temperature = 12000.0 * pow(1.0e-4, phase) + 1.0;
            if (next_key >= current_key || uniform(rng) < exp((next_key-current_key)/temperature)) {
                residue.swap(candidate); current = next; current_key = next_key;
                shared.publish(residue, current, id, iteration);
            } else {
                selected[out] = 1; selected[in] = 0;
            }
            if (iteration % 10000 == 0) {
                // Restart the annealing temperature without discarding the incumbent.
                shared.publish(residue, current, id, iteration);
            }
        }
    }
}

int main(int argc, char** argv) {
    if (argc < 5) {
        cerr << "usage: k13_residue_search BASE OUTPUT THREADS SECONDS [SEED]\n";
        return 2;
    }
    Shared shared;
    ifstream input(argv[1]);
    for (int x; input >> x;) shared.base.push_back(x);
    if (shared.base.size() != 926) return 2;
    shared.output = argv[2];
    const int threads = stoi(argv[3]);
    const double seconds = stod(argv[4]);
    const uint64_t seed = argc > 5 ? stoull(argv[5]) : 130792ULL;
    const auto deadline = chrono::steady_clock::now() +
        chrono::milliseconds(static_cast<long long>(1000 * seconds));
    vector<thread> pool;
    for (int i = 0; i < threads; ++i) pool.emplace_back(worker, ref(shared), i, deadline, seed);
    for (thread& t : pool) t.join();
    cout << "best=" << shared.best_eval.covered << "/4096 middle="
         << shared.best_eval.middle << "/924\n";
}
