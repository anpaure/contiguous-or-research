#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <algorithm>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <random>
#include <string>
#include <vector>
#include <omp.h>

using namespace std;

struct Token {
    int value;
    bool fixed_axis;
};

struct Evaluation {
    int covered = 0;
    int robustness = 0;
    vector<int> counts;

    long long score() const { return 1000000LL * covered + robustness; }
};

struct Box {
    int side;
    int base;
    int volume;

    int encode(int x, int y, int z) const { return (x * base + y) * base + z; }
    void decode(int value, int& x, int& y, int& z) const {
        z = value % base; value /= base;
        y = value % base; value /= base;
        x = value;
    }
    int join(int a, int b) const {
        int ax, ay, az, bx, by, bz;
        decode(a, ax, ay, az); decode(b, bx, by, bz);
        return encode(max(ax, bx), max(ay, by), max(az, bz));
    }
    uint64_t mask(int value) const {
        int x, y, z; decode(value, x, y, z);
        uint64_t answer = 0;
        for (int i = 0; i < x; ++i) answer |= uint64_t(1) << i;
        for (int i = 0; i < y; ++i) answer |= uint64_t(1) << (side + i);
        for (int i = 0; i < z; ++i) answer |= uint64_t(1) << (2 * side + i);
        return answer;
    }
};

static Evaluation evaluate(const Box& box, const vector<Token>& word) {
    Evaluation result;
    result.counts.assign(box.volume, 0);
    for (int left = 0; left < (int)word.size(); ++left) {
        int value = 0;
        for (int right = left; right < (int)word.size(); ++right) {
            value = box.join(value, word[right].value);
            ++result.counts[value];
        }
    }
    for (int value = 1; value < box.volume; ++value) {
        result.covered += result.counts[value] != 0;
        result.robustness += min(result.counts[value], 6);
    }
    return result;
}

static vector<Token> random_word(const Box& box, int n, mt19937_64& rng) {
    vector<Token> word;
    for (int h = 1; h <= box.side; ++h) word.push_back({box.encode(h, 0, 0), true});
    for (int h = 1; h <= box.side; ++h) word.push_back({box.encode(0, h, 0), true});
    for (int h = 1; h <= box.side; ++h) word.push_back({box.encode(0, 0, h), true});
    uniform_int_distribution<int> coordinate(0, box.side);
    while ((int)word.size() < n) {
        int x = coordinate(rng), y = coordinate(rng), z = coordinate(rng);
        if (x + y + z == 0) continue;
        word.push_back({box.encode(x, y, z), false});
    }
    shuffle(word.begin(), word.end(), rng);
    return word;
}

static int random_missing(const Evaluation& e, mt19937_64& rng) {
    vector<int> missing;
    for (int value = 1; value < (int)e.counts.size(); ++value)
        if (!e.counts[value]) missing.push_back(value);
    if (missing.empty()) return 0;
    return missing[rng() % missing.size()];
}

static void mutate(const Box& box, vector<Token>& word, const Evaluation& current,
                   mt19937_64& rng) {
    int n = word.size();
    int kind = rng() % 100;
    if (kind < 38) {
        int i = rng() % n, j = rng() % n;
        swap(word[i], word[j]);
    } else if (kind < 55) {
        int i = rng() % n, j = rng() % n;
        if (i > j) swap(i, j);
        reverse(word.begin() + i, word.begin() + j + 1);
    } else if (kind < 67) {
        int i = rng() % n, j = rng() % n;
        Token token = word[i];
        word.erase(word.begin() + i);
        word.insert(word.begin() + min(j, n - 1), token);
    } else {
        vector<int> flexible;
        for (int i = 0; i < n; ++i) if (!word[i].fixed_axis) flexible.push_back(i);
        if (flexible.empty()) return;
        int pos = flexible[rng() % flexible.size()];
        int x, y, z;
        if (kind < 90 && current.covered + 1 < box.volume) {
            int target = random_missing(current, rng);
            box.decode(target, x, y, z);
            if (kind < 78) {
                // Literal repair; later ordering moves must reuse it in other intervals.
                word[pos].value = target;
                return;
            }
            uniform_int_distribution<int> dx(0, x), dy(0, y), dz(0, z);
            do { x = dx(rng); y = dy(rng); z = dz(rng); } while (x + y + z == 0);
        } else {
            uniform_int_distribution<int> d(0, box.side);
            do { x = d(rng); y = d(rng); z = d(rng); } while (x + y + z == 0);
        }
        word[pos].value = box.encode(x, y, z);
    }
}

int main(int argc, char** argv) {
    if (argc != 6) {
        cerr << "usage: three_box_local_search side length seconds threads output.word\n";
        return 2;
    }
    int side = stoi(argv[1]);
    int n = stoi(argv[2]);
    int seconds = stoi(argv[3]);
    int threads = stoi(argv[4]);
    string output = argv[5];
    Box box{side, side + 1, (side + 1) * (side + 1) * (side + 1)};
    if (n < 3 * side) {
        cerr << "length is below the forced-axis bound\n";
        return 2;
    }

    atomic<bool> solved(false);
    atomic<int> global_best(0);
    mutex output_mutex;
    vector<Token> shared_best_word;
    auto deadline = chrono::steady_clock::now() + chrono::seconds(seconds);

    omp_set_num_threads(threads);
#pragma omp parallel
    {
        int tid = omp_get_thread_num();
        mt19937_64 rng(0x9e3779b97f4a7c15ULL ^
                       (uint64_t)chrono::high_resolution_clock::now().time_since_epoch().count() ^
                       (uint64_t(tid) << 32));
        while (!solved.load(memory_order_relaxed) && chrono::steady_clock::now() < deadline) {
            vector<Token> current;
            {
                lock_guard<mutex> lock(output_mutex);
                if (!shared_best_word.empty() && (rng() % 5 != 0))
                    current = shared_best_word;
            }
            if (current.empty()) current = random_word(box, n, rng);
            else {
                Evaluation temporary = evaluate(box, current);
                for (int kick = 0; kick < 3 + int(rng() % 8); ++kick)
                    mutate(box, current, temporary, rng);
            }
            Evaluation eval = evaluate(box, current);
            const int epoch = 250000;
            for (int iteration = 0; iteration < epoch && !solved.load(memory_order_relaxed); ++iteration) {
                vector<Token> candidate = current;
                mutate(box, candidate, eval, rng);
                Evaluation next = evaluate(box, candidate);
                long long delta = next.score() - eval.score();
                double phase = double(iteration % 25000) / 25000.0;
                double temperature = 1800000.0 * (1.0 - phase) + 15000.0;
                bool accept = delta >= 0;
                if (!accept) {
                    double u = double(rng() >> 11) * (1.0 / 9007199254740992.0);
                    accept = u < exp(double(delta) / temperature);
                }
                if (accept) {
                    current.swap(candidate);
                    eval = std::move(next);
                }

                int old_best = global_best.load(memory_order_relaxed);
                while (eval.covered > old_best &&
                       !global_best.compare_exchange_weak(old_best, eval.covered)) {}
                if (eval.covered > old_best) {
                    lock_guard<mutex> lock(output_mutex);
                    shared_best_word = current;
                    cerr << "best=" << eval.covered << '/' << box.volume - 1
                         << " thread=" << tid << " iteration=" << iteration << '\n';
                    ofstream best(output + ".best");
                    for (int i = 0; i < n; ++i)
                        best << box.mask(current[i].value) << (i + 1 == n ? '\n' : ' ');
                }
                if (eval.covered == box.volume - 1) {
                    lock_guard<mutex> lock(output_mutex);
                    ofstream out(output);
                    for (int i = 0; i < n; ++i)
                        out << box.mask(current[i].value) << (i + 1 == n ? '\n' : ' ');
                    solved.store(true);
                    cerr << "SOLVED thread=" << tid << '\n';
                    break;
                }
            }
        }
    }
    cerr << "finished best=" << global_best.load() << '/' << box.volume - 1 << '\n';
    return solved.load() ? 0 : 1;
}
